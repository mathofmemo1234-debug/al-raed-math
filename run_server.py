# -*- coding: utf-8 -*-
"""
Smart Mathematics Platform Local Server + High-Precision RTL Exam Export Engine
- Serves static files from the workspace root
- GET  /api/health       -> {"ok": true, "docx": true, "pdf": true}
- POST /api/export/docx  -> Native Microsoft Word (.docx) with strict RTL (w:bidi, w:rtl, w:bidiVisual, w:szCs) and Eastern Arabic numerals
- POST /api/export/pdf   -> Print-ready A4 RTL PDF rendered via Microsoft Edge Headless
"""

import argparse
import base64
import http.server
import io
import json
import os
import re
import socketserver
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(DIRECTORY, "assets", "img", "logo.png")
EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

_TRANS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
_EASTERN_TO_ASCII = str.maketrans("٠١٢٣٤٥٦٧٨٩٫", "0123456789.")
CHOICE_LETTERS = ["أ", "ب", "ج", "د"]
WORD_CHOICE_LETTERS = ["أ", "ب", "جـ", "د"]


def to_eastern(val):
    if val is None:
        return ""
    text = str(val)
    text = re.sub(r"(?<=[0-9٠-٩])\.(?=[0-9٠-٩])", "٫", text)
    return text.translate(_TRANS)


def to_number(val, default=1.0):
    if isinstance(val, (int, float)):
        return float(val)
    if val is None:
        return float(default)
    s = str(val).translate(_EASTERN_TO_ASCII).replace(",", ".").strip()
    try:
        return float(s)
    except ValueError:
        return float(default)


def format_num_clean(val):
    num = round(to_number(val, 0.0), 2)
    if abs(num - round(num)) < 1e-6:
        return to_eastern(str(int(round(num))))
    s = f"{num:.2f}".rstrip("0").rstrip(".")
    return to_eastern(s)


def format_mark_phrase(val):
    num = round(to_number(val, 1.0), 2)
    if abs(num - 1.0) < 1e-6:
        return "١ درجة"
    if abs(num - 2.0) < 1e-6:
        return "درجتان"
    num_str = format_num_clean(num)
    if 3 <= num <= 10 and abs(num - round(num)) < 1e-6:
        return f"{num_str} درجات"
    return f"{num_str} درجة"


def find_edge_exe():
    for p in EDGE_PATHS:
        if os.path.isfile(p):
            return p
    return None


IMG_ROOT_DIR = os.path.realpath(os.path.join(DIRECTORY, "assets", "img"))
TOP_RIBBON_PATH = os.path.join(IMG_ROOT_DIR, "exam_top_ribbon.png")
MOE_LOGO_PATH = os.path.join(IMG_ROOT_DIR, "moe_logo.png")
BOTTOM_RIBBON_PATH = os.path.join(IMG_ROOT_DIR, "exam_bottom_ribbon.png")
_IMAGE_B64_CACHE = {}


def get_logo_base64():
    if os.path.isfile(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            return base64.b64encode(f.read()).decode("ascii")
    return ""


def get_static_asset_base64(path_obj):
    if path_obj and os.path.isfile(path_obj):
        cached = _IMAGE_B64_CACHE.get(path_obj)
        if cached is not None:
            return cached
        try:
            with open(path_obj, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            _IMAGE_B64_CACHE[path_obj] = b64
            return b64
        except OSError:
            return ""
    return ""


def resolve_safe_image_path(rel_path):
    if not rel_path or not isinstance(rel_path, str):
        return None
    cleaned = rel_path.strip().replace("\\", "/").lstrip("/")
    if not cleaned.startswith("assets/img/") or ".." in cleaned:
        return None
    ext = os.path.splitext(cleaned)[1].lower()
    if ext not in (".png", ".jpg", ".jpeg"):
        return None
    abs_path = os.path.realpath(os.path.join(DIRECTORY, cleaned.replace("/", os.sep)))
    if not (abs_path == IMG_ROOT_DIR or abs_path.startswith(IMG_ROOT_DIR + os.sep)):
        return None
    if not os.path.isfile(abs_path):
        return None
    return abs_path


def decode_data_url_image(data_url):
    if not data_url or not isinstance(data_url, str):
        return None, ""
    m = re.match(r"^\s*data:image/(png|jpeg|jpg|webp|gif);base64,([A-Za-z0-9+/=\s]+)\s*$", data_url, re.IGNORECASE)
    if not m:
        return None, ""
    fmt = m.group(1).lower()
    raw_b64 = re.sub(r"\s+", "", m.group(2))
    try:
        raw_bytes = base64.b64decode(raw_b64, validate=True)
    except Exception:
        return None, ""
    if not raw_bytes or len(raw_bytes) > 8 * 1024 * 1024:
        return None, ""
    # Normalize any exotic webp/gif to PNG so python-docx and Edge HTML never reject it
    if fmt in ("webp", "gif"):
        try:
            from PIL import Image as PILImage
            with PILImage.open(io.BytesIO(raw_bytes)) as im:
                out_buf = io.BytesIO()
                im.convert("RGBA").save(out_buf, format="PNG")
                return out_buf.getvalue(), "image/png"
        except Exception:
            return None, ""
    mime = "image/jpeg" if fmt in ("jpg", "jpeg") else "image/png"
    return raw_bytes, mime


def resolve_image_bytes(src_or_data_url):
    if not src_or_data_url or not isinstance(src_or_data_url, str):
        return None, ""
    s = src_or_data_url.strip()
    if s.startswith("data:image/"):
        return decode_data_url_image(s)
    abs_path = resolve_safe_image_path(s)
    if not abs_path:
        return None, ""
    try:
        with open(abs_path, "rb") as f:
            data = f.read()
        ext = os.path.splitext(abs_path)[1].lower()
        mime = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png"
        return data, mime
    except OSError:
        return None, ""


def get_image_base64(rel_or_data_url):
    raw_bytes, _ = resolve_image_bytes(rel_or_data_url)
    if not raw_bytes:
        return ""
    return base64.b64encode(raw_bytes).decode("ascii")


def get_image_data_uri(rel_or_data_url):
    raw_bytes, mime = resolve_image_bytes(rel_or_data_url)
    if not raw_bytes or not mime:
        return ""
    return f"data:{mime};base64,{base64.b64encode(raw_bytes).decode('ascii')}"


def _esc_html(s):
    if not s:
        return ""
    text = str(s)
    powers = []
    def _save_pow(m):
        ph = f"___ARPOW_{len(powers)}___"
        powers.append((to_eastern(m.group(1)), to_eastern(m.group(2))))
        return ph
    text = re.sub(r'<span class="ar-pow"><span class="ar-base">([\s\S]*?)</span><sup class="ar-exp">([\s\S]*?)</sup></span>', _save_pow, text)
    text = to_eastern(text)
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )
    for i, (base, exp) in enumerate(powers):
        ph = f"___ARPOW_{i}___"
        text = text.replace(ph, f'<span class="ar-pow"><span class="ar-base">{base}</span><sup class="ar-exp">{exp}</sup></span>')
    return text


def _group_questions(questions, group_by_type=True):
    if not group_by_type:
        return [{"title": "أسئلة الاختبار", "items": questions}]
    mcqs = [q for q in questions if q.get("type") == "mcq"]
    tfs = [q for q in questions if q.get("type") == "tf"]
    essays = [q for q in questions if q.get("type") not in ("mcq", "tf")]
    sections = []
    ordinals = ["السؤال الأول", "السؤال الثاني", "السؤال الثالث"]
    groups = [
        ("اختر الإجابة الصحيحة لكل فقرة مما يأتي:", mcqs),
        ("ضع علامة (✓) أمام العبارة الصحيحة وعلامة (✗) أمام العبارة الخاطئة:", tfs),
        ("أجب عن المسائل الآتية موضحاً خطوات الحل:", essays),
    ]
    idx = 0
    for desc, items in groups:
        if items:
            sec_title = f"{ordinals[idx]}: {desc}" if idx < len(ordinals) else desc
            sections.append({"title": sec_title, "items": items})
            idx += 1
    return sections


# ============================================================================
# Native RTL Microsoft Word (.docx) Builder via python-docx + lxml
# ============================================================================
def _split_type_runs(items):
    runs = []
    for q in items:
        qt = q.get("type")
        if qt not in ("mcq", "tf", "essay"):
            qt = "mcq" if q.get("options") else ("tf" if isinstance(q.get("is_true"), bool) else "essay")
        if not runs or runs[-1]["type"] != qt:
            runs.append({"type": qt, "items": [q]})
        else:
            runs[-1]["items"].append(q)
    return runs


def build_docx_bytes(payload):
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
    from docx.shared import Cm, Pt, RGBColor

    header = payload.get("header") or {}
    questions = payload.get("questions") or []
    options = payload.get("options") or {}

    include_logo = bool(header.get("includeLogo", True))
    include_answer_key = bool(options.get("includeAnswerKey", True))
    group_by_type = bool(options.get("groupByType", True))

    doc = Document()

    # Page setup: A4 portrait (21.0 x 29.7 cm), 1.25 cm margins -> usable width = 18.5 cm
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.2)
    sec.bottom_margin = Cm(1.2)
    sec.right_margin = Cm(1.25)
    sec.left_margin = Cm(1.25)

    sect_pr = sec._sectPr
    # Apply double page border (thinThickSmallGap / thickThinSmallGap) in valid schema position right after pgMar
    pg_borders = parse_xml(
        f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">'
        f'<w:top w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>'
        f'<w:left w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>'
        f'<w:bottom w:val="thickThinSmallGap" w:sz="24" w:space="18" w:color="000000"/>'
        f'<w:right w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>'
        f'</w:pgBorders>'
    )
    old_pgb = sect_pr.find(qn("w:pgBorders"))
    if old_pgb is not None:
        sect_pr.remove(old_pgb)
    pg_mar = sect_pr.find(qn("w:pgMar"))
    if pg_mar is not None:
        pg_mar.addnext(pg_borders)
    else:
        sect_pr.insert(0, pg_borders)

    if sect_pr.find(qn("w:bidi")) is None:
        sect_pr.append(OxmlElement("w:bidi"))

    # Configure Normal style for Arabic RTL
    normal_style = doc.styles["Normal"]
    normal_style.font.name = "Traditional Arabic"
    normal_style.font.size = Pt(13)
    rpr_style = normal_style._element.get_or_add_rPr()
    rfonts_style = rpr_style.find(qn("w:rFonts"))
    if rfonts_style is None:
        rfonts_style = OxmlElement("w:rFonts")
        rpr_style.insert(0, rfonts_style)
    rfonts_style.set(qn("w:ascii"), "Traditional Arabic")
    rfonts_style.set(qn("w:hAnsi"), "Traditional Arabic")
    rfonts_style.set(qn("w:cs"), "Traditional Arabic")

    def set_p_rtl(p, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=1, space_after=1, line_spacing=1.12, keep_together=False, keep_next=False):
        p.alignment = align
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.line_spacing = line_spacing
        pf.keep_together = keep_together
        pf.keep_with_next = keep_next
        ppr = p._p.get_or_add_pPr()
        if ppr.find(qn("w:bidi")) is None:
            ppr.append(OxmlElement("w:bidi"))

    def _create_single_run(p, text_str, size_val, bold_val, is_sup=False, color_val=None, font_val="Traditional Arabic"):
        clean = to_eastern(text_str)
        run = p.add_run(clean)
        run.bold = bold_val
        run.font.name = font_val
        run.font.size = Pt(size_val)
        if color_val:
            run.font.color.rgb = color_val
        if is_sup:
            run.font.superscript = True
        rpr = run._r.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.insert(0, rfonts)
        rfonts.set(qn("w:ascii"), font_val)
        rfonts.set(qn("w:hAnsi"), font_val)
        rfonts.set(qn("w:cs"), font_val)
        if rpr.find(qn("w:rtl")) is None:
            rpr.append(OxmlElement("w:rtl"))
        sz_val = str(int(round(size_val * 2)))
        for tag in ("w:sz", "w:szCs"):
            el = rpr.find(qn(tag))
            if el is None:
                el = OxmlElement(tag)
                rpr.append(el)
            el.set(qn("w:val"), sz_val)
        if is_sup:
            vert = rpr.find(qn("w:vertAlign"))
            if vert is None:
                vert = OxmlElement("w:vertAlign")
                rpr.append(vert)
            vert.set(qn("w:val"), "superscript")
        if bold_val:
            for tag in ("w:b", "w:bCs"):
                if rpr.find(qn(tag)) is None:
                    rpr.append(OxmlElement(tag))
        return run

    def add_ar_run(p, text, size=13, bold=False, color=None, font_name="Traditional Arabic"):
        if not text:
            return None
        text_str = str(text)
        if '<span class="ar-pow">' not in text_str:
            return _create_single_run(p, text_str, size, bold, False, color, font_name)

        pat = re.compile(r'<span class="ar-pow"><span class="ar-base">([\s\S]*?)</span><sup class="ar-exp">([\s\S]*?)</sup></span>')
        last_end = 0
        last_run = None
        for m in pat.finditer(text_str):
            if m.start() > last_end:
                seg = text_str[last_end:m.start()]
                if seg:
                    last_run = _create_single_run(p, seg, size, bold, False, color, font_name)
            base_part, exp_part = m.group(1), m.group(2)
            _create_single_run(p, base_part, size, bold, False, color, font_name)
            last_run = _create_single_run(p, exp_part, max(6.5, round(size * 0.62)), bold, True, color, font_name)
            last_end = m.end()
        if last_end < len(text_str):
            seg = text_str[last_end:]
            if seg:
                last_run = _create_single_run(p, seg, size, bold, False, color, font_name)
        return last_run

    def set_table_rtl(tbl, borders=True, border_color="000000", col_widths_cm=None, outer_sz="6", inner_sz="4"):
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl_pr = tbl._tbl.tblPr
        if tbl_pr.find(qn("w:bidiVisual")) is None:
            tbl_pr.append(OxmlElement("w:bidiVisual"))
        if col_widths_cm:
            total_dxa = int(round(sum(col_widths_cm) * 567.0))
            old_w = tbl_pr.find(qn("w:tblW"))
            if old_w is not None:
                tbl_pr.remove(old_w)
            tbl_pr.append(parse_xml(f'<w:tblW {nsdecls("w")} w:w="{total_dxa}" w:type="dxa"/>'))
            old_lay = tbl_pr.find(qn("w:tblLayout"))
            if old_lay is not None:
                tbl_pr.remove(old_lay)
            tbl_pr.append(parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>'))
            tbl_grid = tbl._tbl.find(qn("w:tblGrid"))
            if tbl_grid is not None:
                tbl._tbl.remove(tbl_grid)
            grid_cols = "".join(f'<w:gridCol w:w="{int(round(w * 567.0))}"/>' for w in col_widths_cm)
            tbl._tbl.insert(1, parse_xml(f'<w:tblGrid {nsdecls("w")}>{grid_cols}</w:tblGrid>'))

        if borders:
            b_xml = (
                f'<w:tblBorders {nsdecls("w")}>'
                f'<w:top w:val="single" w:sz="{outer_sz}" w:space="0" w:color="{border_color}"/>'
                f'<w:bottom w:val="single" w:sz="{outer_sz}" w:space="0" w:color="{border_color}"/>'
                f'<w:left w:val="single" w:sz="{outer_sz}" w:space="0" w:color="{border_color}"/>'
                f'<w:right w:val="single" w:sz="{outer_sz}" w:space="0" w:color="{border_color}"/>'
                f'<w:insideH w:val="single" w:sz="{inner_sz}" w:space="0" w:color="{border_color}"/>'
                f'<w:insideV w:val="single" w:sz="{inner_sz}" w:space="0" w:color="{border_color}"/>'
                f"</w:tblBorders>"
            )
        else:
            b_xml = (
                f'<w:tblBorders {nsdecls("w")}>'
                '<w:top w:val="none"/><w:bottom w:val="none"/>'
                '<w:left w:val="none"/><w:right w:val="none"/>'
                '<w:insideH w:val="none"/><w:insideV w:val="none"/>'
                "</w:tblBorders>"
            )
        old_b = tbl_pr.find(qn("w:tblBorders"))
        if old_b is not None:
            tbl_pr.remove(old_b)
        tbl_pr.append(parse_xml(b_xml))

    def set_cell_width_dxa(cell, width_cm):
        cell.width = Cm(width_cm)
        tc_pr = cell._tc.get_or_add_tcPr()
        old_w = tc_pr.find(qn("w:tcW"))
        if old_w is not None:
            tc_pr.remove(old_w)
        tc_pr.append(parse_xml(f'<w:tcW {nsdecls("w")} w:w="{int(round(width_cm * 567.0))}" w:type="dxa"/>'))

    def set_cell_shading(cell, fill_hex):
        tc_pr = cell._tc.get_or_add_tcPr()
        old = tc_pr.find(qn("w:shd"))
        if old is not None:
            tc_pr.remove(old)
        tc_pr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

    def set_cell_margins(cell, top=55, bottom=55, left=80, right=80):
        tc_pr = cell._tc.get_or_add_tcPr()
        old = tc_pr.find(qn("w:tcMar"))
        if old is not None:
            tc_pr.remove(old)
        tc_pr.append(parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{top}" w:type="dxa"/>'
            f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
            f'<w:left w:w="{left}" w:type="dxa"/>'
            f'<w:right w:w="{right}" w:type="dxa"/>'
            '</w:tcMar>'
        ))

    def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
        tc_pr = cell._tc.get_or_add_tcPr()
        old = tc_pr.find(qn("w:tcBorders"))
        if old is not None:
            tc_pr.remove(old)
        parts_b = []
        for side, spec in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
            if spec == "none":
                parts_b.append(f'<w:{side} w:val="none"/>')
            elif isinstance(spec, tuple):
                sz, color = spec
                parts_b.append(f'<w:{side} w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>')
        if parts_b:
            tc_pr.append(parse_xml(f'<w:tcBorders {nsdecls("w")}>{"".join(parts_b)}</w:tcBorders>'))

    def set_vmerge(top_cell, bot_cell):
        tp = top_cell._tc.get_or_add_tcPr()
        bp = bot_cell._tc.get_or_add_tcPr()
        for el_pr in (tp, bp):
            old_v = el_pr.find(qn("w:vMerge"))
            if old_v is not None:
                el_pr.remove(old_v)
        tp.append(parse_xml(f'<w:vMerge {nsdecls("w")} w:val="restart"/>'))
        bp.append(parse_xml(f'<w:vMerge {nsdecls("w")}/>'))

    def add_picture_fit(paragraph_or_container, img_bytes, max_width_cm=8.5, max_height_cm=4.2, is_paragraph=False):
        if not img_bytes:
            return
        try:
            from PIL import Image as PILImage
            with PILImage.open(io.BytesIO(img_bytes)) as im:
                w_px, h_px = im.size
        except Exception:
            w_px, h_px = (400, 220)
        if w_px <= 0 or h_px <= 0:
            w_px, h_px = (400, 220)
        cm_per_px = 2.54 / 96.0
        nat_w = w_px * cm_per_px
        nat_h = h_px * cm_per_px
        scale = min(max_width_cm / max(nat_w, 0.1), max_height_cm / max(nat_h, 0.1), 1.0)
        final_w = max(0.8, nat_w * scale)
        final_h = max(0.4, nat_h * scale)
        if is_paragraph:
            run_img = paragraph_or_container.add_run()
            run_img.add_picture(io.BytesIO(img_bytes), width=Cm(final_w), height=Cm(final_h))
        else:
            p_img = paragraph_or_container.add_paragraph()
            set_p_rtl(p_img, WD_ALIGN_PARAGRAPH.CENTER, space_before=3, space_after=2, keep_together=True)
            run_img = p_img.add_run()
            run_img.add_picture(io.BytesIO(img_bytes), width=Cm(final_w), height=Cm(final_h))

    def add_question_image_docx(container, q_obj, max_width_cm=9.0, max_height_cm=4.4):
        src = (q_obj or {}).get("image") or ""
        img_bytes, _ = resolve_image_bytes(src)
        if not img_bytes:
            return
        add_picture_fit(container, img_bytes, max_width_cm=max_width_cm, max_height_cm=max_height_cm, is_paragraph=False)
        cap = (q_obj or {}).get("imageCaption") or ""
        if cap:
            p_cap = container.add_paragraph()
            set_p_rtl(p_cap, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2)
            add_ar_run(p_cap, cap, size=10, bold=False, color=MUTED)

    def prevent_row_split(row):
        tr_pr = row._tr.get_or_add_trPr()
        if tr_pr.find(qn("w:cantSplit")) is None:
            tr_pr.append(OxmlElement("w:cantSplit"))

    total_marks = sum(to_number(q.get("marks", 1), 1.0) for q in questions)
    total_marks_str = format_num_clean(total_marks)

    BLACK = RGBColor(0x00, 0x00, 0x00)
    NAVY = RGBColor(0x1E, 0x3A, 0x8A)
    DARK = RGBColor(0x0F, 0x17, 0x2A)
    MUTED = RGBColor(0x47, 0x55, 0x69)
    GREEN = RGBColor(0x04, 0x78, 0x57)

    # ---- 1. Top Decorative Ribbon + Official 3-Col Header + Green Line ----
    if os.path.isfile(TOP_RIBBON_PATH):
        with open(TOP_RIBBON_PATH, "rb") as f:
            top_rib_bytes = f.read()
        p_rib_top = doc.add_paragraph()
        set_p_rtl(p_rib_top, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0)
        add_picture_fit(p_rib_top, top_rib_bytes, max_width_cm=18.5, max_height_cm=1.1, is_paragraph=True)

    hdr_widths = [6.6, 7.2, 4.7]
    hdr_tbl = doc.add_table(rows=1, cols=3)
    set_table_rtl(hdr_tbl, borders=False, col_widths_cm=hdr_widths)
    prevent_row_split(hdr_tbl.rows[0])
    for idx, w in enumerate(hdr_widths):
        cell = hdr_tbl.rows[0].cells[idx]
        set_cell_width_dxa(cell, w)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell, top=30, bottom=55, left=60, right=60)
        set_cell_borders(cell, top="none", left="none", right="none", bottom=("18", "3F9E35"))

    # Right cell (index 0 in RTL bidiVisual): Ministry / District / School Company / School / Stage
    c_right = hdr_tbl.rows[0].cells[0]
    hdr_right_lines = [
        (header.get("ministry") or "المملكة العربية السعودية", 12, True),
        (header.get("district") or "الإدارة العامة للتعليم بمحافظة جدة", 11.5, True),
        (header.get("schoolCompany") or "", 11.5, True),
        (header.get("school") or "مدارس المتقدمة – للتعلم الذكي (جدة)", 11.5, True),
        (header.get("stage") or "", 11.5, True),
    ]
    non_empty_lines = [ln for ln in hdr_right_lines if (ln[0] or "").strip()]
    if not non_empty_lines:
        non_empty_lines = [("المملكة العربية السعودية", 12, True)]
    for li, (ltxt, lsz, lbold) in enumerate(non_empty_lines):
        p_ln = c_right.paragraphs[0] if li == 0 else c_right.add_paragraph()
        set_p_rtl(p_ln, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.08)
        add_ar_run(p_ln, ltxt, size=lsz, bold=lbold, color=BLACK)

    # Center cell (index 1): MOE logo + Exam Title + Metadata
    c_mid = hdr_tbl.rows[0].cells[1]
    p_m = c_mid.paragraphs[0]
    set_p_rtl(p_m, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.05)
    if os.path.isfile(MOE_LOGO_PATH):
        with open(MOE_LOGO_PATH, "rb") as f:
            add_picture_fit(p_m, f.read(), max_width_cm=4.2, max_height_cm=1.45, is_paragraph=True)
        p_m_title = c_mid.add_paragraph()
    else:
        p_m_title = p_m
    set_p_rtl(p_m_title, WD_ALIGN_PARAGRAPH.CENTER, space_before=1, space_after=1, line_spacing=1.1)
    add_ar_run(p_m_title, header.get("examTitle", "اختبار مادة الرياضيات"), size=13.5, bold=True, color=BLACK)
    p_m_sub1 = c_mid.add_paragraph()
    set_p_rtl(p_m_sub1, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1, line_spacing=1.08)
    add_ar_run(p_m_sub1, f"المادة: {header.get('subject', 'الرياضيات')}  |  الصف: {header.get('grade', '')}  |  الفصل: {header.get('term', 'الأول')}", size=11, bold=True, color=DARK)
    p_m_sub2 = c_mid.add_paragraph()
    set_p_rtl(p_m_sub2, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, line_spacing=1.08)
    add_ar_run(p_m_sub2, f"العام الدراسي: {header.get('year', '١٤٤٨ هـ')}  |  الزمن: {header.get('duration', '٤٥ دقيقة')}", size=11, bold=False, color=MUTED)

    # Left cell (index 2 in RTL bidiVisual): Custom or Default School Logo
    c_left = hdr_tbl.rows[0].cells[2]
    p_l = c_left.paragraphs[0]
    set_p_rtl(p_l, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, line_spacing=1.0)
    if include_logo:
        custom_logo = (header.get("customLogoDataUrl") or "").strip()
        logo_bytes = None
        if custom_logo:
            logo_bytes, _ = resolve_image_bytes(custom_logo)
        if not logo_bytes and os.path.isfile(LOGO_PATH):
            with open(LOGO_PATH, "rb") as f:
                logo_bytes = f.read()
        if logo_bytes:
            add_picture_fit(p_l, logo_bytes, max_width_cm=4.1, max_height_cm=2.2, is_paragraph=True)

    # ---- 2. Student Info + Total Score Box (2 rows x 3 cols, exact .doc layout) ----
    p_sp = doc.add_paragraph()
    set_p_rtl(p_sp, WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=2, line_spacing=1.0)

    stu_widths = [2.8, 12.2, 3.5]
    stu_tbl = doc.add_table(rows=2, cols=3)
    set_table_rtl(stu_tbl, borders=True, border_color="000000", col_widths_cm=stu_widths, outer_sz="6", inner_sz="4")
    for r_idx in range(2):
        prevent_row_split(stu_tbl.rows[r_idx])
        for c_idx, w in enumerate(stu_widths):
            cell = stu_tbl.rows[r_idx].cells[c_idx]
            set_cell_width_dxa(cell, w)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=45, bottom=45, left=75, right=75)

    # Row 0: اسم الطالب | ...... | الدرجة
    set_cell_shading(stu_tbl.rows[0].cells[0], "F2F2F2")
    p_s00 = stu_tbl.rows[0].cells[0].paragraphs[0]
    set_p_rtl(p_s00, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    add_ar_run(p_s00, "اسم الطالب", size=12, bold=True, color=BLACK)

    p_s01 = stu_tbl.rows[0].cells[1].paragraphs[0]
    set_p_rtl(p_s01, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    add_ar_run(p_s01, "." * 82, size=11, bold=False, color=MUTED)

    set_cell_shading(stu_tbl.rows[0].cells[2], "F2F2F2")
    p_s02 = stu_tbl.rows[0].cells[2].paragraphs[0]
    set_p_rtl(p_s02, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    add_ar_run(p_s02, "الدرجة الكلية", size=11.5, bold=True, color=BLACK)

    # Row 1: الصف | grade / (   ) |     / total_marks
    set_cell_shading(stu_tbl.rows[1].cells[0], "F2F2F2")
    p_s10 = stu_tbl.rows[1].cells[0].paragraphs[0]
    set_p_rtl(p_s10, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    add_ar_run(p_s10, "الصف", size=12, bold=True, color=BLACK)

    p_s11 = stu_tbl.rows[1].cells[1].paragraphs[0]
    set_p_rtl(p_s11, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
    add_ar_run(p_s11, f"{header.get('grade', '')}   /   (          )", size=12, bold=True, color=BLACK)

    p_s12 = stu_tbl.rows[1].cells[2].paragraphs[0]
    set_p_rtl(p_s12, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
    add_ar_run(p_s12, f"          /  {total_marks_str}", size=13, bold=True, color=BLACK)

    instructions = (header.get("instructions") or "").strip()
    if instructions:
        p_ins = doc.add_paragraph()
        set_p_rtl(p_ins, WD_ALIGN_PARAGRAPH.RIGHT, space_before=3, space_after=2)
        add_ar_run(p_ins, "تعليمات: ", size=11.5, bold=True, color=NAVY)
        add_ar_run(p_ins, instructions, size=11.5, bold=False, color=MUTED)

    # ---- 3. Question Sections (matching exact .doc tables for ANY count of questions) ----
    sections = _group_questions(questions, group_by_type=group_by_type)
    global_q_num = 0

    for sec_obj in sections:
        sec_items = sec_obj["items"]
        sec_marks = sum(to_number(q.get("marks", 1), 1.0) for q in sec_items)
        sec_marks_str = format_num_clean(sec_marks)

        # Section title + 2-row right-to-left Score Box on left
        sec_hdr_widths = [15.0, 3.5]
        sec_hdr_tbl = doc.add_table(rows=2, cols=2)
        set_table_rtl(sec_hdr_tbl, borders=False, col_widths_cm=sec_hdr_widths)
        for r_i in range(2):
            prevent_row_split(sec_hdr_tbl.rows[r_i])
            for c_i, w in enumerate(sec_hdr_widths):
                c = sec_hdr_tbl.rows[r_i].cells[c_i]
                set_cell_width_dxa(c, w)
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                set_cell_margins(c, top=35, bottom=35, left=60, right=60)

        set_vmerge(sec_hdr_tbl.rows[0].cells[0], sec_hdr_tbl.rows[1].cells[0])
        set_cell_borders(sec_hdr_tbl.rows[0].cells[0], top="none", bottom="none", left="none", right="none")
        set_cell_borders(sec_hdr_tbl.rows[1].cells[0], top="none", bottom="none", left="none", right="none")
        set_p_rtl(sec_hdr_tbl.rows[1].cells[0].paragraphs[0], WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
        p_st = sec_hdr_tbl.rows[0].cells[0].paragraphs[0]
        set_p_rtl(p_st, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0, keep_next=True)
        add_ar_run(p_st, sec_obj["title"], size=13.5, bold=True, color=BLACK)

        c_sb_top = sec_hdr_tbl.rows[0].cells[1]
        set_cell_shading(c_sb_top, "F2F2F2")
        set_cell_borders(c_sb_top, top=("6", "000000"), bottom=("4", "000000"), left=("6", "000000"), right=("6", "000000"))
        p_sbt = c_sb_top.paragraphs[0]
        set_p_rtl(p_sbt, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
        add_ar_run(p_sbt, "الدرجة", size=11, bold=True, color=BLACK)

        c_sb_bot = sec_hdr_tbl.rows[1].cells[1]
        set_cell_borders(c_sb_bot, top=("4", "000000"), bottom=("6", "000000"), left=("6", "000000"), right=("6", "000000"))
        p_sbb = c_sb_bot.paragraphs[0]
        set_p_rtl(p_sbb, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
        add_ar_run(p_sbb, f"          /  {sec_marks_str}", size=12, bold=True, color=BLACK)

        p_gap = doc.add_paragraph()
        set_p_rtl(p_gap, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=2, line_spacing=1.0)

        for run_grp in _split_type_runs(sec_items):
            rtype = run_grp["type"]
            ritems = run_grp["items"]

            if rtype == "mcq":
                # 9-column .doc MCQ Table: Num(1.0) + 4x[Letter(0.85) + Text(3.525)] = 18.5 cm
                mcq_widths = [1.0, 0.85, 3.525, 0.85, 3.525, 0.85, 3.525, 0.85, 3.525]
                mcq_tbl = doc.add_table(rows=2 * len(ritems), cols=9)
                set_table_rtl(mcq_tbl, borders=True, border_color="000000", col_widths_cm=mcq_widths, outer_sz="6", inner_sz="4")

                for idx_in_run, q in enumerate(ritems):
                    global_q_num += 1
                    r0 = mcq_tbl.rows[2 * idx_in_run]
                    r1 = mcq_tbl.rows[2 * idx_in_run + 1]
                    prevent_row_split(r0)
                    prevent_row_split(r1)

                    for ci, w in enumerate(mcq_widths):
                        set_cell_width_dxa(r0.cells[ci], w)
                        set_cell_width_dxa(r1.cells[ci], w)

                    # Merge col 0 vertically across prompt + options
                    set_vmerge(r0.cells[0], r1.cells[0])
                    r0.cells[0].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    set_cell_margins(r0.cells[0], top=45, bottom=45, left=40, right=40)
                    set_cell_margins(r1.cells[0], top=45, bottom=45, left=40, right=40)
                    set_p_rtl(r1.cells[0].paragraphs[0], WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
                    p_num = r0.cells[0].paragraphs[0]
                    set_p_rtl(p_num, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, keep_next=True)
                    add_ar_run(p_num, to_eastern(str(global_q_num)), size=12.5, bold=True, color=BLACK)

                    # Merge cols 1..8 horizontally on prompt row and shade #F2F2F2
                    prompt_cell = r0.cells[1].merge(r0.cells[8])
                    set_cell_width_dxa(prompt_cell, sum(mcq_widths[1:]))
                    set_cell_shading(prompt_cell, "F2F2F2")
                    prompt_cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
                    set_cell_margins(prompt_cell, top=55, bottom=55, left=80, right=80)
                    p_q = prompt_cell.paragraphs[0]
                    set_p_rtl(p_q, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0, keep_together=True, keep_next=True)
                    q_text = q.get("q") or q.get("statement") or ""
                    add_ar_run(p_q, q_text, size=12.5, bold=True, color=BLACK)
                    add_question_image_docx(prompt_cell, q, max_width_cm=10.5, max_height_cm=4.6)

                    # Populate options row: 4 pairs of letter + option text
                    opts = (q.get("options") or [])[:4]
                    while len(opts) < 4:
                        opts.append("")
                    for o_i, opt_val in enumerate(opts):
                        c_let = r1.cells[1 + 2 * o_i]
                        c_val = r1.cells[2 + 2 * o_i]
                        c_let.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                        c_val.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                        set_cell_margins(c_let, top=45, bottom=45, left=30, right=30)
                        set_cell_margins(c_val, top=45, bottom=45, left=60, right=60)
                        p_l = c_let.paragraphs[0]
                        set_p_rtl(p_l, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
                        add_ar_run(p_l, WORD_CHOICE_LETTERS[o_i], size=12, bold=True, color=BLACK)
                        p_v = c_val.paragraphs[0]
                        set_p_rtl(p_v, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
                        add_ar_run(p_v, opt_val, size=12, bold=False, color=DARK)

            elif rtype == "tf":
                # 3-column .doc T/F Table: [1.4, 14.5, 2.6] = 18.5 cm
                tf_widths = [1.4, 14.5, 2.6]
                tf_tbl = doc.add_table(rows=len(ritems) + 1, cols=3)
                set_table_rtl(tf_tbl, borders=True, border_color="000000", col_widths_cm=tf_widths, outer_sz="6", inner_sz="4")

                hdr_row = tf_tbl.rows[0]
                prevent_row_split(hdr_row)
                for ci, w in enumerate(tf_widths):
                    set_cell_width_dxa(hdr_row.cells[ci], w)
                merged_tf_hdr = hdr_row.cells[0].merge(hdr_row.cells[2])
                set_cell_width_dxa(merged_tf_hdr, sum(tf_widths))
                set_cell_shading(merged_tf_hdr, "F2F2F2")
                set_cell_margins(merged_tf_hdr, top=50, bottom=50, left=80, right=80)
                p_tfh = merged_tf_hdr.paragraphs[0]
                set_p_rtl(p_tfh, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, keep_next=True)
                add_ar_run(p_tfh, "ضع علامة ( ✓ ) أمام العبارة الصحيحة وعلامة ( ✗ ) أمام العبارة الخاطئة:", size=12.5, bold=True, color=BLACK)

                for r_i, q in enumerate(ritems, start=1):
                    global_q_num += 1
                    row = tf_tbl.rows[r_i]
                    prevent_row_split(row)
                    for ci, w in enumerate(tf_widths):
                        c = row.cells[ci]
                        set_cell_width_dxa(c, w)
                        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                        set_cell_margins(c, top=50, bottom=50, left=70, right=70)
                    p0 = row.cells[0].paragraphs[0]
                    set_p_rtl(p0, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
                    add_ar_run(p0, to_eastern(str(global_q_num)), size=12.5, bold=True, color=BLACK)

                    p1 = row.cells[1].paragraphs[0]
                    set_p_rtl(p1, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
                    add_ar_run(p1, q.get("statement") or q.get("q") or "", size=12.5, bold=False, color=BLACK)
                    add_question_image_docx(row.cells[1], q, max_width_cm=7.0, max_height_cm=3.5)

                    p2 = row.cells[2].paragraphs[0]
                    set_p_rtl(p2, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
                    add_ar_run(p2, "(          )", size=12.5, bold=True, color=BLACK)

            else:
                # 2-column .doc Essay Table: [1.4, 17.1] = 18.5 cm
                es_widths = [1.4, 17.1]
                es_tbl = doc.add_table(rows=2 * len(ritems), cols=2)
                set_table_rtl(es_tbl, borders=True, border_color="000000", col_widths_cm=es_widths, outer_sz="6", inner_sz="4")

                for idx_in_run, q in enumerate(ritems):
                    global_q_num += 1
                    r0 = es_tbl.rows[2 * idx_in_run]
                    r1 = es_tbl.rows[2 * idx_in_run + 1]
                    prevent_row_split(r0)
                    prevent_row_split(r1)
                    for ci, w in enumerate(es_widths):
                        set_cell_width_dxa(r0.cells[ci], w)
                        set_cell_width_dxa(r1.cells[ci], w)

                    set_vmerge(r0.cells[0], r1.cells[0])
                    r0.cells[0].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    set_cell_margins(r0.cells[0], top=50, bottom=50, left=50, right=50)
                    set_cell_margins(r1.cells[0], top=50, bottom=50, left=50, right=50)
                    set_p_rtl(r1.cells[0].paragraphs[0], WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
                    p_en = r0.cells[0].paragraphs[0]
                    set_p_rtl(p_en, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, keep_next=True)
                    add_ar_run(p_en, to_eastern(str(global_q_num)), size=12.5, bold=True, color=BLACK)

                    c_ep = r0.cells[1]
                    set_cell_shading(c_ep, "F2F2F2")
                    c_ep.vertical_alignment = WD_ALIGN_VERTICAL.TOP
                    set_cell_margins(c_ep, top=55, bottom=55, left=80, right=80)
                    p_ep = c_ep.paragraphs[0]
                    set_p_rtl(p_ep, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0, keep_together=True, keep_next=True)
                    add_ar_run(p_ep, q.get("q") or q.get("statement") or "", size=12.5, bold=True, color=BLACK)
                    add_question_image_docx(c_ep, q, max_width_cm=10.5, max_height_cm=4.6)

                    c_ea = r1.cells[1]
                    c_ea.vertical_alignment = WD_ALIGN_VERTICAL.TOP
                    set_cell_margins(c_ea, top=60, bottom=60, left=80, right=80)
                    lines_count = max(2, min(6, int(round(to_number(q.get("lines", 3), 3)))))
                    for l_i in range(lines_count):
                        p_line = c_ea.paragraphs[0] if l_i == 0 else c_ea.add_paragraph()
                        set_p_rtl(p_line, WD_ALIGN_PARAGRAPH.RIGHT, space_before=2, space_after=3, line_spacing=1.18)
                        prefix = "الحل /  " if l_i == 0 else ""
                        add_ar_run(p_line, prefix + ("." * 102), size=11.5, bold=(l_i == 0), color=MUTED)

            p_after_run = doc.add_paragraph()
            set_p_rtl(p_after_run, WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=3, line_spacing=1.0)

    # ---- 4. Closing Blessing + Teacher & Principal Signatures + Bottom Ribbon ----
    p_end = doc.add_paragraph()
    set_p_rtl(p_end, WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=4, keep_next=True)
    add_ar_run(p_end, "انتهت الأسئلة                   مع خالص الدعوات بالتوفيق والنجاح", size=13, bold=True, color=BLACK)

    sig_widths = [9.25, 9.25]
    sig_tbl = doc.add_table(rows=1, cols=2)
    set_table_rtl(sig_tbl, borders=False, col_widths_cm=sig_widths)
    prevent_row_split(sig_tbl.rows[0])
    teacher_name = header.get("teacher") or "أ. محمد عبدالله جمعة"
    principal_name = header.get("principal") or "حسين عبد الله أزيبي"

    for s_i, (role_lbl, person_name) in enumerate([("معلم المادة", teacher_name), ("مدير المدرسة", principal_name)]):
        c_sig = sig_tbl.rows[0].cells[s_i]
        set_cell_width_dxa(c_sig, sig_widths[s_i])
        set_cell_margins(c_sig, top=30, bottom=40, left=60, right=60)
        p_sig1 = c_sig.paragraphs[0]
        set_p_rtl(p_sig1, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=1)
        add_ar_run(p_sig1, role_lbl, size=12, bold=True, color=BLACK)
        p_sig2 = c_sig.add_paragraph()
        set_p_rtl(p_sig2, WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0)
        add_ar_run(p_sig2, person_name, size=12, bold=True, color=DARK)

    if os.path.isfile(BOTTOM_RIBBON_PATH):
        with open(BOTTOM_RIBBON_PATH, "rb") as f:
            bot_rib_bytes = f.read()
        p_rib_bot = doc.add_paragraph()
        set_p_rtl(p_rib_bot, WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=0, line_spacing=1.0)
        add_picture_fit(p_rib_bot, bot_rib_bytes, max_width_cm=18.5, max_height_cm=0.9, is_paragraph=True)

    # ---- 5. Optional Answer Key Page ----
    if include_answer_key and questions:
        doc.add_page_break()
        p_ak_title = doc.add_paragraph()
        set_p_rtl(p_ak_title, WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=6)
        add_ar_run(p_ak_title, f"نموذج الإجابة وتوزيع الدرجات — {header.get('examTitle', 'اختبار الرياضيات')}", size=14.5, bold=True, color=NAVY)

        ak_widths = [1.4, 3.2, 11.7, 2.2]
        ak_tbl = doc.add_table(rows=len(questions) + 1, cols=4)
        set_table_rtl(ak_tbl, borders=True, border_color="047857", col_widths_cm=ak_widths, outer_sz="6", inner_sz="4")
        ak_headers = ["السؤال", "النوع", "الإجابة النموذجية والشرح", "الدرجة"]
        prevent_row_split(ak_tbl.rows[0])
        for c_i, h_txt in enumerate(ak_headers):
            c = ak_tbl.rows[0].cells[c_i]
            set_cell_width_dxa(c, ak_widths[c_i])
            set_cell_shading(c, "D1FAE5")
            set_cell_margins(c, top=55, bottom=55, left=60, right=60)
            p_h = c.paragraphs[0]
            set_p_rtl(p_h, WD_ALIGN_PARAGRAPH.CENTER if c_i in (0, 3) else WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
            add_ar_run(p_h, h_txt, size=12, bold=True, color=GREEN)

        ordered_questions = []
        for sec_obj in sections:
            ordered_questions.extend(sec_obj["items"])

        for idx_q, q in enumerate(ordered_questions, start=1):
            row = ak_tbl.rows[idx_q]
            prevent_row_split(row)
            q_type = q.get("type") or ("mcq" if q.get("options") else ("tf" if isinstance(q.get("is_true"), bool) else "essay"))
            if q_type == "mcq":
                type_lbl = "اختيار من متعدد"
                corr = int(q.get("correct", 0))
                opts = q.get("options") or []
                letter = WORD_CHOICE_LETTERS[corr] if 0 <= corr < len(WORD_CHOICE_LETTERS) else "أ"
                ans_txt = f"{letter}) {opts[corr] if 0 <= corr < len(opts) else ''}"
                if q.get("explanation"):
                    ans_txt += f" — {q['explanation']}"
            elif q_type == "tf":
                type_lbl = "صواب وخطأ"
                ans_txt = "صواب (✓)" if q.get("is_true") else "خطأ (✗)"
                if q.get("explanation"):
                    ans_txt += f" — {q['explanation']}"
            else:
                type_lbl = "مسألة مقالية"
                ans_txt = q.get("ans") or ""

            vals = [to_eastern(str(idx_q)), type_lbl, ans_txt, format_num_clean(q.get("marks", 1))]
            for c_i, v_txt in enumerate(vals):
                c = row.cells[c_i]
                set_cell_width_dxa(c, ak_widths[c_i])
                set_cell_margins(c, top=48, bottom=48, left=60, right=60)
                p_c = c.paragraphs[0]
                set_p_rtl(p_c, WD_ALIGN_PARAGRAPH.CENTER if c_i in (0, 3) else WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=0)
                add_ar_run(p_c, v_txt, size=11.5, bold=(c_i in (0, 3)), color=GREEN if c_i == 2 else DARK)

        p_ak_tot = doc.add_paragraph()
        set_p_rtl(p_ak_tot, WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=2)
        add_ar_run(p_ak_tot, f"المجموع الكلي للدرجات: {total_marks_str} درجة", size=13, bold=True, color=NAVY)

    def normalize_ooxml_tree(root_el):
        order_specs = {
            qn("w:tblPr"): [
                qn("w:tblStyle"), qn("w:tblpPr"), qn("w:tblOverlap"), qn("w:bidiVisual"),
                qn("w:tblStyleRowBandSize"), qn("w:tblStyleColBandSize"), qn("w:tblW"), qn("w:jc"),
                qn("w:tblCellSpacing"), qn("w:tblInd"), qn("w:tblBorders"), qn("w:shd"),
                qn("w:tblLayout"), qn("w:tblCellMar"), qn("w:tblLook"),
            ],
            qn("w:tcPr"): [
                qn("w:tcW"), qn("w:gridSpan"), qn("w:hMerge"), qn("w:vMerge"),
                qn("w:tcBorders"), qn("w:shd"), qn("w:noWrap"), qn("w:tcMar"),
                qn("w:textDirection"), qn("w:tcFitText"), qn("w:vAlign"), qn("w:hideMark"),
            ],
            qn("w:sectPr"): [
                qn("w:headerReference"), qn("w:footerReference"), qn("w:footnotePr"),
                qn("w:endnotePr"), qn("w:type"), qn("w:pgSz"), qn("w:pgMar"),
                qn("w:paperSrc"), qn("w:pgBorders"), qn("w:lnNumType"), qn("w:pgNumType"),
                qn("w:cols"), qn("w:formProt"), qn("w:vAlign"), qn("w:noEndnote"),
                qn("w:titlePg"), qn("w:textDirection"), qn("w:bidi"), qn("w:rtlGutter"),
                qn("w:docGrid"),
            ],
            qn("w:rPr"): [
                qn("w:rStyle"), qn("w:rFonts"), qn("w:b"), qn("w:bCs"),
                qn("w:i"), qn("w:iCs"), qn("w:color"), qn("w:sz"),
                qn("w:szCs"), qn("w:rtl"),
            ],
        }
        rank_maps = {parent_tag: {t: idx for idx, t in enumerate(tags)} for parent_tag, tags in order_specs.items()}
        for el in root_el.iter():
            rmap = rank_maps.get(el.tag)
            if rmap is not None and len(el) > 1:
                children = list(el)
                indexed = sorted(enumerate(children), key=lambda pair: (rmap.get(pair[1].tag, 999), pair[0]))
                for idx_c, (_, child) in enumerate(indexed):
                    if el[idx_c] is not child:
                        el.insert(idx_c, child)

    normalize_ooxml_tree(doc.element.body)

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


# ============================================================================
# Print-Exact A4 RTL HTML & PDF Builder via Microsoft Edge Headless
# ============================================================================
def build_exam_html(payload):
    header = payload.get("header") or {}
    questions = payload.get("questions") or []
    options = payload.get("options") or {}

    include_logo = bool(header.get("includeLogo", True))
    include_answer_key = bool(options.get("includeAnswerKey", True))
    group_by_type = bool(options.get("groupByType", True))

    total_marks = sum(to_number(q.get("marks", 1), 1.0) for q in questions)
    total_marks_str = format_num_clean(total_marks)

    custom_logo = (header.get("customLogoDataUrl") or "").strip()
    school_logo_uri = ""
    if include_logo:
        school_logo_uri = get_image_data_uri(custom_logo) if custom_logo else ""
        if not school_logo_uri:
            def_b64 = get_logo_base64()
            if def_b64:
                school_logo_uri = f"data:image/png;base64,{def_b64}"
    school_logo_html = f'<img src="{school_logo_uri}" alt="شعار المدرسة" class="school-logo">' if school_logo_uri else ""

    top_rib_b64 = get_static_asset_base64(TOP_RIBBON_PATH)
    moe_logo_b64 = get_static_asset_base64(MOE_LOGO_PATH)
    bot_rib_b64 = get_static_asset_base64(BOTTOM_RIBBON_PATH)

    top_rib_html = f'<img src="data:image/png;base64,{top_rib_b64}" alt="" class="top-ribbon">' if top_rib_b64 else ""
    moe_logo_html = f'<img src="data:image/png;base64,{moe_logo_b64}" alt="وزارة التعليم" class="moe-logo">' if moe_logo_b64 else ""
    bot_rib_html = f'<img src="data:image/png;base64,{bot_rib_b64}" alt="جيل ينتج المعرفة" class="bottom-ribbon">' if bot_rib_b64 else ""

    sections = _group_questions(questions, group_by_type=group_by_type)
    global_q = 0
    sections_html = []

    def render_pdf_fig_html(q_obj, extra_cls=""):
        src = (q_obj or {}).get("image") or ""
        uri = get_image_data_uri(src)
        if not uri:
            return ""
        cap = _esc_html((q_obj or {}).get("imageCaption") or "")
        cap_html = f'<div class="q-fig-cap">{cap}</div>' if cap else ""
        cls_attr = f"q-fig {extra_cls}".strip()
        return (
            f'<div class="{cls_attr}">'
            f'<img src="{uri}" alt="{cap or "شكل السؤال"}" />'
            f'{cap_html}'
            f'</div>'
        )

    for sec_obj in sections:
        items = sec_obj["items"]
        sec_marks = sum(to_number(q.get("marks", 1), 1.0) for q in items)
        sec_head = (
            f'<div class="sec-hdr-bar">'
            f'<div class="sec-title-cell">{_esc_html(sec_obj["title"])}</div>'
            f'<table class="score-box-tbl" dir="rtl">'
            f'<tr><td class="score-box-top">الدرجة</td></tr>'
            f'<tr><td class="score-box-val"><span class="score-blank"></span> / {_esc_html(format_num_clean(sec_marks))}</td></tr>'
            f'</table>'
            f'</div>'
        )

        run_tables = []
        for run_grp in _split_type_runs(items):
            rtype = run_grp["type"]
            ritems = run_grp["items"]
            if rtype == "mcq":
                tbodies = []
                for q in ritems:
                    global_q += 1
                    q_text = _esc_html(q.get("q") or q.get("statement") or "")
                    fig_html = render_pdf_fig_html(q)
                    opts = (q.get("options") or [])[:4]
                    while len(opts) < 4:
                        opts.append("")
                    opt_tds = "".join(
                        f'<td class="mcq-let">{WORD_CHOICE_LETTERS[i]}</td>'
                        f'<td class="mcq-opt">{_esc_html(opt)}</td>'
                        for i, opt in enumerate(opts)
                    )
                    tbodies.append(
                        f'<tbody class="q-pair">'
                        f'<tr>'
                        f'<td rowspan="2" class="q-num-cell">{_esc_html(str(global_q))}</td>'
                        f'<td colspan="8" class="q-prompt-cell">{q_text}{fig_html}</td>'
                        f'</tr>'
                        f'<tr>{opt_tds}</tr>'
                        f'</tbody>'
                    )
                run_tables.append(f'<table class="doc-mcq-tbl" dir="rtl">{"".join(tbodies)}</table>')
            elif rtype == "tf":
                rows_html = []
                for q in ritems:
                    global_q += 1
                    fig_html = render_pdf_fig_html(q, "q-fig-tf")
                    stmt = _esc_html(q.get("statement") or q.get("q") or "")
                    rows_html.append(
                        f'<tr>'
                        f'<td class="tf-num">{_esc_html(str(global_q))}</td>'
                        f'<td class="tf-stmt">{stmt}{fig_html}</td>'
                        f'<td class="tf-ans">( &nbsp;&nbsp;&nbsp;&nbsp; )</td>'
                        f'</tr>'
                    )
                run_tables.append(
                    f'<table class="doc-tf-tbl" dir="rtl">'
                    f'<thead><tr><th colspan="3">ضع علامة ( ✓ ) أمام العبارة الصحيحة وعلامة ( ✗ ) أمام العبارة الخاطئة:</th></tr></thead>'
                    f'<tbody>{"".join(rows_html)}</tbody>'
                    f'</table>'
                )
            else:
                tbodies = []
                for q in ritems:
                    global_q += 1
                    q_text = _esc_html(q.get("q") or q.get("statement") or "")
                    fig_html = render_pdf_fig_html(q)
                    lc = max(2, min(6, int(round(to_number(q.get("lines", 3), 3)))))
                    lines_html = "".join(
                        f'<div class="es-dot">{"<strong>الحل / </strong>" if li == 0 else ""}</div>'
                        for li in range(lc)
                    )
                    tbodies.append(
                        f'<tbody class="q-pair">'
                        f'<tr>'
                        f'<td rowspan="2" class="es-num">{_esc_html(str(global_q))}</td>'
                        f'<td class="es-prompt">{q_text}{fig_html}</td>'
                        f'</tr>'
                        f'<tr>'
                        f'<td class="es-sol">{lines_html}</td>'
                        f'</tr>'
                        f'</tbody>'
                    )
                run_tables.append(f'<table class="doc-es-tbl" dir="rtl">{"".join(tbodies)}</table>')

        sections_html.append(f'<section class="exam-sec">{sec_head}{"".join(run_tables)}</section>')

    answer_key_html = ""
    if include_answer_key and questions:
        ordered_questions = []
        for s in sections:
            ordered_questions.extend(s["items"])
        ak_rows = []
        for idx_q, q in enumerate(ordered_questions, start=1):
            qt = q.get("type") or ("mcq" if q.get("options") else ("tf" if isinstance(q.get("is_true"), bool) else "essay"))
            if qt == "mcq":
                t_lbl = "اختيار من متعدد"
                corr = int(q.get("correct", 0))
                opts = q.get("options") or []
                letter = WORD_CHOICE_LETTERS[corr] if 0 <= corr < len(WORD_CHOICE_LETTERS) else "أ"
                ans_txt = f"{letter}) {opts[corr] if 0 <= corr < len(opts) else ''}"
                if q.get("explanation"):
                    ans_txt += f" — {q['explanation']}"
            elif qt == "tf":
                t_lbl = "صواب وخطأ"
                ans_txt = "صواب (✓)" if q.get("is_true") else "خطأ (✗)"
                if q.get("explanation"):
                    ans_txt += f" — {q['explanation']}"
            else:
                t_lbl = "مسألة مقالية"
                ans_txt = q.get("ans") or ""
            ak_rows.append(
                f'<tr>'
                f'<td class="c-num">{_esc_html(str(idx_q))}</td>'
                f'<td>{_esc_html(t_lbl)}</td>'
                f'<td class="ak-ans">{_esc_html(ans_txt)}</td>'
                f'<td class="c-num">{_esc_html(format_num_clean(q.get("marks", 1)))}</td>'
                f'</tr>'
            )
        answer_key_html = (
            f'<div class="page-break"></div>'
            f'<div class="ak-header">نموذج الإجابة وتوزيع الدرجات — {_esc_html(header.get("examTitle", "اختبار الرياضيات"))}</div>'
            f'<table class="ak-tbl" dir="rtl">'
            f'<thead><tr><th class="c-num">س</th><th>النوع</th><th>الإجابة النموذجية والشرح</th><th class="c-num">الدرجة</th></tr></thead>'
            f'<tbody>{"".join(ak_rows)}</tbody>'
            f'</table>'
            f'<div class="ak-total">المجموع الكلي للدرجات: {_esc_html(total_marks_str)} درجة</div>'
        )

    instructions = (header.get("instructions") or "").strip()
    inst_html = f'<div class="inst-box"><strong>تعليمات:</strong> {_esc_html(instructions)}</div>' if instructions else ""

    right_lines_html = "".join(
        f'<div>{_esc_html(val)}</div>'
        for val in [
            header.get("ministry") or "المملكة العربية السعودية",
            header.get("district") or "الإدارة العامة للتعليم بمحافظة جدة",
            header.get("schoolCompany") or "",
            header.get("school") or "مدارس المتقدمة – للتعلم الذكي (جدة)",
            header.get("stage") or "",
        ]
        if (val or "").strip()
    )

    teacher_name = _esc_html(header.get("teacher") or "أ. محمد عبدالله جمعة")
    principal_name = _esc_html(header.get("principal") or "حسين عبد الله أزيبي")

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{_esc_html(header.get("examTitle", "اختبار الرياضيات"))}</title>
<style>
  @page {{ size: A4 portrait; margin: 8mm; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Cairo', 'Tajawal', 'Segoe UI', 'Arial', sans-serif;
    direction: rtl;
    text-align: right;
    color: #000000;
    background: #ffffff;
    font-size: 12.5px;
    line-height: 1.45;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  .page-frame-fixed {{
    position: fixed;
    top: 0; right: 0; bottom: 0; left: 0;
    border: 2px solid #000000;
    box-shadow: inset 0 0 0 2px #ffffff, inset 0 0 0 3.2px #000000;
    pointer-events: none;
    z-index: 9999;
  }}
  .print-shell-tbl {{ width: 100%; border-collapse: collapse; border: none; }}
  .print-shell-tbl > thead > tr > td {{ height: 4mm; border: none; }}
  .print-shell-tbl > tfoot > tr > td {{ height: 4mm; border: none; }}
  .print-shell-tbl > tbody > tr > td {{ padding: 0 5mm; border: none; vertical-align: top; }}

  .top-ribbon {{ width: 100%; max-height: 36px; display: block; object-fit: cover; margin-bottom: 3px; }}
  .hdr-tbl {{ width: 100%; border-collapse: collapse; border-bottom: 3px solid #3F9E35; margin-bottom: 6px; }}
  .hdr-tbl td {{ border: none; padding: 3px 6px 6px 6px; vertical-align: middle; }}
  .hdr-right {{ width: 35%; text-align: center; font-weight: 700; font-size: 11.5px; line-height: 1.42; }}
  .hdr-mid {{ width: 41%; text-align: center; }}
  .hdr-left {{ width: 24%; text-align: center; }}
  .moe-logo {{ max-height: 48px; width: auto; display: block; margin: 0 auto 3px auto; }}
  .school-logo {{ max-width: 118px; max-height: 76px; width: auto; height: auto; display: block; margin: 0 auto; object-fit: contain; }}
  .hdr-title {{ font-size: 14px; font-weight: 800; color: #000000; }}
  .hdr-sub {{ font-size: 11px; color: #1e293b; font-weight: 600; margin-top: 2px; }}

  .stu-tbl {{ width: 100%; border-collapse: collapse; margin-bottom: 6px; }}
  .stu-tbl td {{ border: 1px solid #000000; padding: 4px 8px; font-size: 12px; }}
  .stu-lbl {{ width: 14%; background: #F2F2F2; font-weight: 800; text-align: center; }}
  .stu-fill {{ width: 67%; text-align: right; font-weight: 700; }}
  .score-box-top {{ width: 19%; background: #F2F2F2; font-weight: 800; text-align: center; font-size: 11.5px; padding: 3px 6px; border: 1px solid #000000; }}
  .score-box-val {{ width: 19%; font-weight: 800; text-align: center; font-size: 13px; padding: 3px 6px; border: 1px solid #000000; }}
  .score-blank {{ display: inline-block; min-width: 28px; }}

  .inst-box {{ background: #fefce8; border: 1px solid #fde047; border-right: 3px solid #eab308; padding: 4px 8px; margin-bottom: 6px; font-size: 11px; }}
  .exam-sec {{ margin-bottom: 8px; }}
  .sec-hdr-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    margin: 7px 0 4px 0;
    break-inside: avoid;
    page-break-inside: avoid;
    break-after: avoid;
    page-break-after: avoid;
  }}
  .sec-title-cell {{ flex: 1; text-align: right; font-weight: 800; font-size: 13.5px; color: #000000; padding-left: 8px; }}
  .score-box-tbl {{ width: 19%; min-width: 110px; border-collapse: collapse; flex-shrink: 0; break-inside: avoid; page-break-inside: avoid; }}

  .doc-mcq-tbl, .doc-tf-tbl, .doc-es-tbl {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 6px;
    border: 1.2px solid #000000;
  }}
  tbody.q-pair {{ break-inside: avoid; page-break-inside: avoid; }}
  .doc-mcq-tbl td, .doc-tf-tbl td, .doc-tf-tbl th, .doc-es-tbl td {{
    border: 1px solid #000000;
    padding: 4px 6px;
    font-size: 12px;
    vertical-align: middle;
  }}
  .q-num-cell, .es-num {{ width: 5.5%; text-align: center; font-weight: 800; background: #ffffff; }}
  .q-prompt-cell, .es-prompt {{ width: 94.5%; background: #F2F2F2; font-weight: 700; text-align: right; vertical-align: top; }}
  .mcq-let {{ width: 4.5%; text-align: center; font-weight: 800; background: #ffffff; }}
  .mcq-opt {{ width: 19.1%; text-align: right; background: #ffffff; }}

  .doc-tf-tbl th {{ background: #F2F2F2; font-weight: 800; text-align: center; }}
  .doc-tf-tbl tr {{ break-inside: avoid; page-break-inside: avoid; }}
  .tf-num {{ width: 8%; text-align: center; font-weight: 800; }}
  .tf-stmt {{ width: 78%; text-align: right; font-weight: 600; }}
  .tf-ans {{ width: 14%; text-align: center; font-weight: 700; white-space: nowrap; }}

  .es-num {{ width: 8%; }}
  .es-prompt {{ width: 92%; }}
  .es-sol {{ width: 92%; background: #ffffff; vertical-align: top; padding: 5px 8px; }}
  .es-dot {{ border-bottom: 1px dotted #64748b; height: 22px; margin-top: 2px; font-size: 11.5px; color: #334155; }}

  .q-fig {{ text-align: center; margin: 5px auto 3px auto; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; background: #ffffff; display: block; width: fit-content; max-width: 94%; }}
  .q-fig img {{ max-width: 280px; max-height: 145px; width: auto; height: auto; display: block; margin: 0 auto; object-fit: contain; }}
  .q-fig.q-fig-tf img {{ max-width: 205px; max-height: 100px; }}
  .q-fig-cap {{ font-size: 10px; color: #475569; margin-top: 2px; }}

  .closing-wrap {{ break-inside: avoid; page-break-inside: avoid; margin-top: 10px; }}
  .closing-blessing {{ text-align: center; font-weight: 800; font-size: 13px; color: #000000; margin-bottom: 6px; }}
  .sig-tbl {{ width: 100%; border-collapse: collapse; border: none; margin-bottom: 6px; }}
  .sig-tbl td {{ width: 50%; border: none; text-align: center; font-weight: 700; font-size: 12px; padding: 2px 6px; }}
  .bottom-ribbon {{ width: 100%; max-height: 28px; display: block; object-fit: contain; }}

  .page-break {{ page-break-before: always; break-before: page; }}
  .ak-header {{ text-align: center; font-size: 15px; font-weight: 800; color: #047857; border: 2px solid #047857; background: #ecfdf5; padding: 7px; margin-bottom: 8px; }}
  .ak-tbl {{ width: 100%; border-collapse: collapse; }}
  .ak-tbl th, .ak-tbl td {{ border: 1px solid #6ee7b7; padding: 4px 7px; font-size: 11.5px; }}
  .ak-tbl th {{ background: #d1fae5; color: #065f46; font-weight: 800; }}
  .ak-tbl tr {{ break-inside: avoid; }}
  .c-num {{ width: 38px; text-align: center; font-weight: 800; color: #1e3a8a; }}
  .ak-ans {{ color: #065f46; font-weight: 600; }}
  .ak-total {{ margin-top: 8px; text-align: left; font-weight: 800; font-size: 13px; color: #1e3a8a; }}

  /* صياغة الأسس والقوى الرياضية (الأس دائماً في أعلى يسار الأساس بالأرقام المشرقية) */
  .ar-pow {{
    display: inline-flex !important;
    flex-direction: row !important;
    direction: rtl !important;
    align-items: flex-start !important;
    unicode-bidi: isolate !important;
    vertical-align: baseline !important;
    margin: 0 2px !important;
    line-height: 1 !important;
    position: relative !important;
  }}
  .ar-base {{
    display: inline-block !important;
    font-family: inherit !important;
    font-size: 1em !important;
    line-height: 1.15 !important;
  }}
  .ar-exp {{
    display: inline-block !important;
    font-size: 0.62em !important;
    font-weight: bold !important;
    line-height: 1 !important;
    font-family: inherit !important;
    transform: translateY(-0.48em) !important;
    position: relative !important;
    top: -0.1em !important;
    margin-right: 2px !important;
    margin-left: 1px !important;
  }}
</style>
</head>
<body>
  <div class="page-frame-fixed"></div>
  <table class="print-shell-tbl" dir="rtl">
    <thead><tr><td></td></tr></thead>
    <tfoot><tr><td></td></tr></tfoot>
    <tbody>
      <tr>
        <td>
          {top_rib_html}
          <table class="hdr-tbl" dir="rtl">
            <tr>
              <td class="hdr-right">{right_lines_html}</td>
              <td class="hdr-mid">
                {moe_logo_html}
                <div class="hdr-title">{_esc_html(header.get("examTitle", "اختبار مادة الرياضيات"))}</div>
                <div class="hdr-sub">المادة: {_esc_html(header.get("subject", "الرياضيات"))} &nbsp;|&nbsp; الصف: {_esc_html(header.get("grade", ""))} &nbsp;|&nbsp; الفصل: {_esc_html(header.get("term", "الأول"))}</div>
                <div class="hdr-sub">العام الدراسي: {_esc_html(header.get("year", "١٤٤٨ هـ"))} &nbsp;|&nbsp; الزمن: {_esc_html(header.get("duration", "٤٥ دقيقة"))}</div>
              </td>
              <td class="hdr-left">{school_logo_html}</td>
            </tr>
          </table>

          <table class="stu-tbl" dir="rtl">
            <tr>
              <td class="stu-lbl">اسم الطالب</td>
              <td class="stu-fill">................................................................................</td>
              <td class="score-box-top">الدرجة الكلية</td>
            </tr>
            <tr>
              <td class="stu-lbl">الصف</td>
              <td class="stu-fill">{_esc_html(header.get("grade", ""))} &nbsp;/&nbsp; ( &nbsp;&nbsp;&nbsp;&nbsp; )</td>
              <td class="score-box-val"><span class="score-blank"></span> / {_esc_html(total_marks_str)}</td>
            </tr>
          </table>

          {inst_html}
          {"".join(sections_html)}

          <div class="closing-wrap">
            <div class="closing-blessing">انتهت الأسئلة &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; مع خالص الدعوات بالتوفيق والنجاح</div>
            <table class="sig-tbl" dir="rtl">
              <tr>
                <td><div>معلم المادة</div><div>{teacher_name}</div></td>
                <td><div>مدير المدرسة</div><div>{principal_name}</div></td>
              </tr>
            </table>
            {bot_rib_html}
          </div>

          {answer_key_html}
        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>"""


def build_pdf_bytes(payload):
    edge_exe = find_edge_exe()
    if not edge_exe:
        raise RuntimeError("Microsoft Edge executable not found for headless PDF generation.")

    html_content = build_exam_html(payload)
    tmp_dir = tempfile.mkdtemp(prefix="raed_exam_pdf_")
    html_path = os.path.join(tmp_dir, "exam.html")
    pdf_path = os.path.join(tmp_dir, "exam.pdf")
    user_data_dir = os.path.join(tmp_dir, "edge_profile")
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        file_url = Path(html_path).resolve().as_uri()
        cmd = [
            edge_exe,
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-extensions",
            "--disable-background-networking",
            "--disable-sync",
            f"--user-data-dir={user_data_dir}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            file_url,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if not os.path.isfile(pdf_path) or os.path.getsize(pdf_path) == 0:
            raise RuntimeError(f"Edge failed to produce PDF (rc={res.returncode}): {res.stderr}")
        with open(pdf_path, "rb") as f:
            return f.read()
    finally:
        # Clean up temporary files safely
        for root, dirs, files in os.walk(tmp_dir, topdown=False):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except OSError:
                    pass
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except OSError:
                    pass
        try:
            os.rmdir(tmp_dir)
        except OSError:
            pass


# ============================================================================
# HTTP Server Handler
# ============================================================================
class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/health":
            edge_ok = find_edge_exe() is not None
            body = json.dumps({"ok": True, "docx": True, "pdf": edge_ok}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._send_cors_headers()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path not in ("/api/export/docx", "/api/export/pdf"):
            self.send_error(404, "Endpoint not found")
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            payload = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            err = json.dumps({"error": f"Invalid JSON payload: {exc}"}).encode("utf-8")
            self.send_response(400)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(err)
            return

        try:
            grade_str = (payload.get("header") or {}).get("grade", "")
            prefix = "exam_grade1m" if "متوسط" in str(grade_str) else "exam_grade6"
            if parsed.path == "/api/export/docx":
                data = build_docx_bytes(payload)
                ctype = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                fname = f"{prefix}.docx"
            else:
                data = build_pdf_bytes(payload)
                ctype = "application/pdf"
                fname = f"{prefix}.pdf"

            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Disposition", f'attachment; filename="{fname}"')
            self._send_cors_headers()
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as exc:
            err = json.dumps({"error": str(exc)}).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self._send_cors_headers()
            self.send_header("Content-Length", str(len(err)))
            self.end_headers()
            self.wfile.write(err)


def start_server(port=PORT, open_browser=True):
    os.chdir(DIRECTORY)
    with ThreadingHTTPServer(("", port), Handler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print("=" * 70)
        print("🚀 منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة")
        print("   المدارس المتقدمة للتعلم الذكي بجدة")
        print("=" * 70)
        print(f"📡 السيرفر يعمل الآن على الرابط: {url}")
        print("   ميزة تصدير الاختبارات (Word .docx و PDF) مفعلة عبر API المحلي.")
        print("   (اضغط Ctrl+C في أي وقت لإيقاف السيرفر)")
        print("=" * 70)
        if open_browser:
            import webbrowser
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nتم إيقاف السيرفر بنجاح.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Raed Math Platform HTTP Server & Exporter")
    parser.add_argument("--port", type=int, default=PORT)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    start_server(port=args.port, open_browser=not args.no_browser)
