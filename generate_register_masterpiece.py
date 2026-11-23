import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import os

students_class_1 = [
    "أصيل ممدوح صالح معتوق فراش",
    "الاسر ياسر بن سعيد بن الغامدي",
    "جواد عبدالله علي حمد المومني",
    "حسين محمد حسين علي العمودي",
    "سليمان احمد عبدالعزيز السلامه",
    "صالح محمد صالح الصالحي",
    "طلال علي محمد مسفر القحطاني",
    "عبد الاله احمد محمود عجب نور",
    "عبدالرحمن حسين فؤاد الجراب",
    "عبدالعزيز وليد عبدالمحسن الحقيلي",
    "عبدالله ربيع فؤاد ديب نصري",
    "عبدالله محمد عبدالرحيم الزهراني",
    "عبدالملك عادل محسن باسبعين",
    "عز انور احمد علي مرغلاني",
    "عمر محمد طاهر ريحان نبي بخش",
    "مجد خالد دويل عوض بالعلا",
    "محمد اسامه محمد حميد اللبدي",
    "مؤيد ماجد علي الرديني",
    "همام علي محمد علي الفاهوم",
    "يزن جهاد محمدماهر الساعاتي",
    "يوسف فارس داود سليمان صبحي"
]

students_class_2 = [
    "أحمد رامي أحمد مصلح زعرب",
    "البراء رائد حامد احمد المغامسي",
    "تركي ياسر يوسف عوض الاحمدي",
    "حمزة يزن خالد قرمان",
    "راكان تركي احمد علي الزهراني",
    "سعد فيصل سعد محمدعلي زرين",
    "سلطان فارس سالم سعد القحطاني",
    "صالح محمد صالح العجمه الغامدي",
    "عبدالعزيز احمد عبدالعزيز حميدي السلامه",
    "عبدالعزيز أحمد عبدالعزيز الغامدي",
    "عبدالملك عماد عباس حسن غندورة",
    "علي محمد علي عبدالرحيم علي",
    "فهد ماجد سليمان عبدالله العجلان",
    "فهد مخلد خلف الله سرور الهذلي",
    "محمد عادل حسن عباس شرقاوي",
    "محمد خالد دويل عوض بالعلا",
    "مصطفى عبدالباسط مصطفى زهرا",
    "مهدي محمد مهدي مسعود الوقداني",
    "نايف ماجد علي يوسف المحمدي",
    "وليد أحمد فريد احمد وهيب",
    "وليف ملاذ وليف فيرق",
    "يوسف أيمن طه محمدصالح الصبان",
    "يوسف نادر محمود حسن"
]

def set_cell_width_dxa(cell, dxa_val):
    tcPr = cell._tc.get_or_add_tcPr()
    # remove existing tcW if present
    for existing_w in tcPr.findall(qn('w:tcW')):
        tcPr.remove(existing_w)
    tcW = parse_xml(f'<w:tcW {nsdecls("w")} w:w="{dxa_val}" w:type="dxa"/>')
    tcPr.append(tcW)

def set_cell_margins(cell, top=8, bottom=8, left=15, right=15):
    tcPr = cell._tc.get_or_add_tcPr()
    for existing_m in tcPr.findall(qn('w:tcMar')):
        tcPr.remove(existing_m)
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    for existing_s in tcPr.findall(qn('w:shd')):
        tcPr.remove(existing_s)
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_v_center(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    for existing_v in tcPr.findall(qn('w:vAlign')):
        tcPr.remove(existing_v)
    tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

def set_table_rtl(table):
    tblPr = table._tbl.tblPr
    tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

def set_table_fixed(table):
    tblPr = table._tbl.tblPr
    tblPr.append(parse_xml(f'<w:tblLayout {nsdecls("w")} w:type="fixed"/>'))

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    for existing_b in tcPr.findall(qn('w:tcBorders')):
        tcPr.remove(existing_b)
    borders = ['<w:tcBorders ' + nsdecls("w") + '>']
    for side, border in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        if border:
            val = border.get('val', 'single')
            sz = border.get('sz', '4')
            color = border.get('color', 'CBD5E1')
            borders.append(f'<w:{side} w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>')
        else:
            borders.append(f'<w:{side} w:val="none"/>')
    borders.append('</w:tcBorders>')
    tcPr.append(parse_xml(''.join(borders)))

def set_bidi(p):
    p.paragraph_format.bidi = True
    pPr = p._p.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:bidi {nsdecls("w")}/>'))

def add_run(p, text, bold=False, italic=False, size=8.5, color="0F172A"):
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.name = 'Arial'
    run.font.size = Pt(size)
    r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    run.font.color.rgb = RGBColor(r, g, b)
    rPr = run._r.get_or_add_rPr()
    rPr.append(parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'))
    rPr.append(parse_xml(f'<w:rtl {nsdecls("w")}/>'))
    return run

def create_register_masterpiece(output_path="سجل_متابعة_الرياضيات_ثالث_متوسط_أ_محمد_جمعة.docx"):
    doc = docx.Document()
    
    # Page Setup: A4 Landscape, tight margins for exact 1-page per class fit
    section = doc.sections[0]
    section.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
    section.page_width = Cm(29.7)
    section.page_height = Cm(21.0)
    section.top_margin = Cm(0.5)
    section.bottom_margin = Cm(0.4)
    section.left_margin = Cm(0.7)
    section.right_margin = Cm(0.7)
    
    # Normal Style
    normal = doc.styles['Normal']
    normal.font.name = 'Arial'
    normal.font.size = Pt(8.5)
    normal.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0
    
    # Target total width: 28.3 cm = 16045 dxa
    # Col 0 (م): 0.8 cm = 454 dxa
    # Col 1 (اسم الطالب): 5.3 cm = 3005 dxa
    # Col 2..26 (25 days): 0.89 cm = 504 dxa each * 25 = 12600 dxa
    # 454 + 3005 + 12600 = 16059 dxa = 28.32 cm (perfect fit for 29.7 - 1.4 cm)
    W_NUM = 454
    W_NAME = 3005
    W_DAY = 504
    W_WEEK = W_DAY * 5  # 2520 dxa
    
    classes = [
        ("فصل ( 3 / 1 )", students_class_1),
        ("فصل ( 3 / 2 )", students_class_2)
    ]
    
    for c_idx, (class_name, students) in enumerate(classes):
        if c_idx > 0:
            doc.add_page_break()
            
        # 1. Header Table
        hdr_tbl = doc.add_table(rows=1, cols=3)
        hdr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(hdr_tbl)
        set_table_fixed(hdr_tbl)
        
        c_right = hdr_tbl.rows[0].cells[0]
        c_center = hdr_tbl.rows[0].cells[1]
        c_left = hdr_tbl.rows[0].cells[2]
        
        set_cell_width_dxa(c_right, 4000)
        set_cell_width_dxa(c_center, 8059)
        set_cell_width_dxa(c_left, 4000)
        
        set_cell_margins(c_right, top=4, bottom=4, left=15, right=15)
        set_cell_margins(c_center, top=4, bottom=4, left=15, right=15)
        set_cell_margins(c_left, top=4, bottom=4, left=15, right=15)
        
        # Right info
        pr = c_right.paragraphs[0]
        pr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        pr.paragraph_format.space_before = Pt(0)
        pr.paragraph_format.space_after = Pt(0)
        pr.paragraph_format.line_spacing = 1.0
        set_bidi(pr)
        add_run(pr, "المملكة العربية السعودية\n", bold=True, size=8, color="1E3A8A")
        add_run(pr, "وزارة التعليم  •  المدارس المتقدمة للتعلم الذكي\n", bold=True, size=7.5, color="334155")
        add_run(pr, "المرحلة المتوسطة  —  بنين", size=7, color="64748B")
        
        # Center info
        pc = c_center.paragraphs[0]
        pc.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pc.paragraph_format.space_before = Pt(0)
        pc.paragraph_format.space_after = Pt(0)
        pc.paragraph_format.line_spacing = 1.0
        set_bidi(pc)
        add_run(pc, "سجل المتابعة اليومية للطلاب\n", bold=True, size=13.5, color="1E3A8A")
        add_run(pc, "مادة الرياضيات  •  العام الدراسي 1448 هـ  •  الفصل الدراسي الأول", bold=True, size=8.5, color="D97706")
        
        # Left info
        pl = c_left.paragraphs[0]
        pl.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pl.paragraph_format.space_before = Pt(0)
        pl.paragraph_format.space_after = Pt(0)
        pl.paragraph_format.line_spacing = 1.0
        set_bidi(pl)
        add_run(pl, "الصف: ", size=7.5, color="64748B")
        add_run(pl, f"الثالث المتوسط — {class_name}\n", bold=True, size=8.5, color="047857")
        add_run(pl, "معلم المادة: ", size=7.5, color="64748B")
        add_run(pl, "أ. محمد عبدالله جمعة\n", bold=True, size=8.5, color="1E3A8A")
        add_run(pl, f"عدد الطلاب: {len(students)} طالباً", size=7.5, color="475569")
        
        # Tiny gap
        p_gap = doc.add_paragraph()
        p_gap.paragraph_format.space_before = Pt(0)
        p_gap.paragraph_format.space_after = Pt(1)
        p_gap.paragraph_format.line_spacing = 1.0
        
        # 2. Main Register Table
        total_rows = 3 + len(students)
        tbl = doc.add_table(rows=total_rows, cols=27)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(tbl)
        set_table_fixed(tbl)
        
        # Configure Table Grid explicitly
        tblPr = tbl._tbl.tblPr
        # Remove old tblGrid if any
        for old_grid in tbl._tbl.findall(qn('w:tblGrid')):
            tbl._tbl.remove(old_grid)
            
        tblGrid = OxmlElement('w:tblGrid')
        for w_dxa in [W_NUM, W_NAME] + [W_DAY] * 25:
            gridCol = OxmlElement('w:gridCol')
            gridCol.set(qn('w:w'), str(w_dxa))
            tblGrid.append(gridCol)
        tbl._tbl.insert(tbl._tbl.index(tblPr) + 1, tblGrid)
        
        # Merges
        # Col 0: merge rows 0, 1, 2
        tbl.rows[0].cells[0].merge(tbl.rows[2].cells[0])
        # Col 1: merge rows 0, 1
        tbl.rows[0].cells[1].merge(tbl.rows[1].cells[1])
        # Week headers: merge 5 cols per week
        week_start_cols = [2, 7, 12, 17, 22]
        weeks = ["الأسبوع الأول", "الأسبوع الثاني", "الأسبوع الثالث", "الأسبوع الرابع", "الأسبوع الخامس"]
        for s_col in week_start_cols:
            tbl.rows[0].cells[s_col].merge(tbl.rows[0].cells[s_col + 4])
            
        # Format Row 0 (Weeks & Top Headers)
        r0 = tbl.rows[0]
        trPr0 = r0._tr.get_or_add_trPr()
        trPr0.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        trPr0.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr0.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="280" w:hRule="exact"/>'))
        
        # Col 0 (م)
        c_m = r0.cells[0]
        set_cell_width_dxa(c_m, W_NUM)
        set_cell_background(c_m, "1E3A8A")
        set_cell_v_center(c_m)
        set_cell_margins(c_m, top=4, bottom=4, left=2, right=2)
        p = c_m.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        set_bidi(p)
        add_run(p, "م", bold=True, size=8.5, color="FFFFFF")
        
        # Col 1 (اسم الطالب)
        c_name = r0.cells[1]
        set_cell_width_dxa(c_name, W_NAME)
        set_cell_background(c_name, "1E3A8A")
        set_cell_v_center(c_name)
        set_cell_margins(c_name, top=4, bottom=4, left=15, right=15)
        p = c_name.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        set_bidi(p)
        add_run(p, "اسم الطالب", bold=True, size=9, color="FFFFFF")
        
        # 5 Weeks
        for w_idx, s_col in enumerate(week_start_cols):
            cell = r0.cells[s_col]
            set_cell_width_dxa(cell, W_WEEK)
            set_cell_background(cell, "1E3A8A")
            set_cell_v_center(cell)
            set_cell_margins(cell, top=4, bottom=4, left=4, right=4)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            set_bidi(p)
            add_run(p, weeks[w_idx], bold=True, size=8.5, color="FFFFFF")
            
        # Format Row 1 (Days)
        r1 = tbl.rows[1]
        trPr1 = r1._tr.get_or_add_trPr()
        trPr1.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        trPr1.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr1.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="230" w:hRule="exact"/>'))
        
        days = ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"]
        for s_col in week_start_cols:
            for d_idx, day_name in enumerate(days):
                cell = r1.cells[s_col + d_idx]
                set_cell_width_dxa(cell, W_DAY)
                set_cell_background(cell, "2563EB")
                set_cell_v_center(cell)
                set_cell_margins(cell, top=2, bottom=2, left=1, right=1)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                set_bidi(p)
                d_short = day_name if day_name != "الأربعاء" else "أربعاء"
                add_run(p, d_short, bold=True, size=7, color="FFFFFF")
                
        # Format Row 2 (Dates)
        r2 = tbl.rows[2]
        trPr2 = r2._tr.get_or_add_trPr()
        trPr2.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        trPr2.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr2.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="220" w:hRule="exact"/>'))
        
        c_date_lbl = r2.cells[1]
        set_cell_width_dxa(c_date_lbl, W_NAME)
        set_cell_background(c_date_lbl, "E2E8F0")
        set_cell_v_center(c_date_lbl)
        set_cell_margins(c_date_lbl, top=2, bottom=2, left=15, right=15)
        p = c_date_lbl.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        set_bidi(p)
        add_run(p, "التاريخ", bold=True, size=7.5, color="1E293B")
        
        for c_c in range(2, 27):
            cell = r2.cells[c_c]
            set_cell_width_dxa(cell, W_DAY)
            set_cell_background(cell, "F1F5F9")
            set_cell_v_center(cell)
            set_cell_margins(cell, top=2, bottom=2, left=1, right=1)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            set_bidi(p)
            add_run(p, "/  /", size=6, color="94A3B8")
            
        # Student Rows (Rows 3 .. total_rows - 1)
        for s_idx, student_name in enumerate(students):
            row = tbl.rows[3 + s_idx]
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
            trPr.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="255" w:hRule="exact"/>'))
            
            bg = "F8FAFC" if s_idx % 2 == 1 else "FFFFFF"
            
            # Col 0: م
            c_num = row.cells[0]
            set_cell_width_dxa(c_num, W_NUM)
            set_cell_background(c_num, "F1F5F9" if s_idx % 2 == 1 else "F8FAFC")
            set_cell_v_center(c_num)
            set_cell_margins(c_num, top=2, bottom=2, left=2, right=2)
            p = c_num.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            set_bidi(p)
            add_run(p, str(s_idx + 1), bold=True, size=7.5, color="1E3A8A")
            
            # Col 1: اسم الطالب (FULL WIDTH 3005 dxa = 5.3 cm!)
            c_nm = row.cells[1]
            set_cell_width_dxa(c_nm, W_NAME)
            set_cell_background(c_nm, bg)
            set_cell_v_center(c_nm)
            set_cell_margins(c_nm, top=2, bottom=2, left=10, right=15)
            p = c_nm.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            set_bidi(p)
            add_run(p, f" {student_name}", bold=True, size=8, color="0F172A")
            
            # 25 day cells
            for col_i in range(2, 27):
                cell = row.cells[col_i]
                set_cell_width_dxa(cell, W_DAY)
                set_cell_background(cell, bg)
                set_cell_v_center(cell)
                set_cell_margins(cell, top=2, bottom=2, left=1, right=1)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.0
                set_bidi(p)
                
        # Custom borders
        week_ends = {6, 11, 16, 21, 26}
        for r_i in range(total_rows):
            row = tbl.rows[r_i]
            for c_i in range(len(row.cells)):
                cell = row.cells[c_i]
                b_top = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
                b_bottom = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
                b_left = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
                b_right = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
                
                if c_i in week_ends:
                    b_left = {'val': 'single', 'sz': '8', 'color': '475569'}
                if c_i == 1:
                    b_left = {'val': 'single', 'sz': '8', 'color': '1E3A8A'}
                if c_i == 0:
                    b_left = {'val': 'single', 'sz': '6', 'color': '94A3B8'}
                    
                if r_i == 0:
                    b_top = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
                if r_i == 2:
                    b_bottom = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
                if r_i == total_rows - 1:
                    b_bottom = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
                    
                set_cell_borders(cell, top=b_top, bottom=b_bottom, left=b_left, right=b_right)
                
        # Tiny gap before footer
        p_gap2 = doc.add_paragraph()
        p_gap2.paragraph_format.space_before = Pt(0)
        p_gap2.paragraph_format.space_after = Pt(2)
        p_gap2.paragraph_format.line_spacing = 1.0
        
        # 3. Footer Table: Legend & Signatures
        ftr_tbl = doc.add_table(rows=2, cols=1)
        ftr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(ftr_tbl)
        set_table_fixed(ftr_tbl)
        
        # Legend Row
        c_leg = ftr_tbl.rows[0].cells[0]
        set_cell_width_dxa(c_leg, 16059)
        set_cell_background(c_leg, "F1F5F9")
        set_cell_v_center(c_leg)
        set_cell_margins(c_leg, top=6, bottom=6, left=20, right=20)
        trPr_leg = ftr_tbl.rows[0]._tr.get_or_add_trPr()
        trPr_leg.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        trPr_leg.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="230" w:hRule="exact"/>'))
        
        p_leg = c_leg.paragraphs[0]
        p_leg.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_leg.paragraph_format.space_before = Pt(0)
        p_leg.paragraph_format.space_after = Pt(0)
        p_leg.paragraph_format.line_spacing = 1.0
        set_bidi(p_leg)
        
        add_run(p_leg, "📌 مفتاح رموز المتابعة اليومية:  ", bold=True, size=7.5, color="1E3A8A")
        add_run(p_leg, "[ت] ", bold=True, size=7.5, color="B45309")
        add_run(p_leg, "تأخير    ", size=7.5, color="1E293B")
        add_run(p_leg, "[غ] ", bold=True, size=7.5, color="DC2626")
        add_run(p_leg, "غياب    ", size=7.5, color="1E293B")
        add_run(p_leg, "[ز] ", bold=True, size=7.5, color="047857")
        add_run(p_leg, "تميز وإبداع    ", size=7.5, color="1E293B")
        add_run(p_leg, "[س] ", bold=True, size=7.5, color="D97706")
        add_run(p_leg, "سلوك ومواظبة    ", size=7.5, color="1E293B")
        add_run(p_leg, "[و] ", bold=True, size=7.5, color="2563EB")
        add_run(p_leg, "واجب منزلي    ", size=7.5, color="1E293B")
        add_run(p_leg, "[م] ", bold=True, size=7.5, color="0D9488")
        add_run(p_leg, "مشاركة صفية    ", size=7.5, color="1E293B")
        add_run(p_leg, "[ب] ", bold=True, size=7.5, color="7C3AED")
        add_run(p_leg, "مهمة أدائية / بحث", size=7.5, color="1E293B")
        
        # Signature Row
        c_sig = ftr_tbl.rows[1].cells[0]
        set_cell_width_dxa(c_sig, 16059)
        set_cell_background(c_sig, "FFFFFF")
        set_cell_v_center(c_sig)
        set_cell_margins(c_sig, top=10, bottom=4, left=20, right=20)
        trPr_sig = ftr_tbl.rows[1]._tr.get_or_add_trPr()
        trPr_sig.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        trPr_sig.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="250" w:hRule="exact"/>'))
        
        p_sig = c_sig.paragraphs[0]
        p_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sig.paragraph_format.space_before = Pt(0)
        p_sig.paragraph_format.space_after = Pt(0)
        p_sig.paragraph_format.line_spacing = 1.0
        set_bidi(p_sig)
        
        add_run(p_sig, "معلم المادة: ", bold=True, size=8, color="334155")
        add_run(p_sig, "أ. محمد عبدالله جمعة                              ", bold=True, size=8.5, color="1E3A8A")
        add_run(p_sig, "المشرف التربوي: ", bold=True, size=8, color="334155")
        add_run(p_sig, "..........................................                              ", size=8, color="94A3B8")
        add_run(p_sig, "مدير المدرسة: ", bold=True, size=8, color="334155")
        add_run(p_sig, "..........................................", size=8, color="94A3B8")
        
        set_cell_borders(c_leg,
                         top={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                         bottom={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                         left={'val': 'single', 'sz': '4', 'color': 'CBD5E1'},
                         right={'val': 'single', 'sz': '4', 'color': 'CBD5E1'})
        set_cell_borders(c_sig, top=None, bottom=None, left=None, right=None)
        
    doc.save(output_path)
    print(f"File saved successfully: {output_path}")

if __name__ == '__main__':
    create_register_masterpiece()
