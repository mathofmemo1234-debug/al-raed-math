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

def create_full_document(filename="سجل_متابعة_الرياضيات_ثالث_متوسط_أ_محمد_جمعة.docx"):
    doc = docx.Document()
    
    # Configure A4 Landscape with 0.8 cm top/bottom, 1.0 cm left/right margins
    section = doc.sections[0]
    section.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
    section.page_width = Cm(29.7)
    section.page_height = Cm(21.0)
    section.top_margin = Cm(0.7)
    section.bottom_margin = Cm(0.7)
    section.left_margin = Cm(1.0)
    section.right_margin = Cm(1.0)
    
    # Configure Normal Style Font
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(9)
    normal_style.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    
    classes_data = [
        ("فصل ( 3 / 1 )", students_class_1),
        ("فصل ( 3 / 2 )", students_class_2)
    ]
    
    for page_idx, (class_name, students) in enumerate(classes_data):
        if page_idx > 0:
            doc.add_page_break()
            
        # 1. Header Table (3 columns, 1 row)
        hdr_tbl = doc.add_table(rows=1, cols=3)
        hdr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(hdr_tbl)
        
        hdr_widths = [Cm(7.5), Cm(12.7), Cm(7.5)]
        row0 = hdr_tbl.rows[0]
        for i, w in enumerate(hdr_widths):
            row0.cells[i].width = w
            set_cell_margins(row0.cells[i], top=20, bottom=40, left=40, right=40)
            
        # Right cell: Ministry & School info
        c_right = row0.cells[0]
        p_r = c_right.paragraphs[0]
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_r.paragraph_format.space_before = Pt(0)
        p_r.paragraph_format.space_after = Pt(1)
        p_r.paragraph_format.line_spacing = 1.05
        set_bidi(p_r)
        add_run(p_r, "المملكة العربية السعودية\n", bold=True, size=9, color="1E3A8A")
        add_run(p_r, "وزارة التعليم\n", bold=True, size=8.5, color="334155")
        add_run(p_r, "المدارس المتقدمة للتعلم الذكي\n", bold=True, size=8.5, color="1E3A8A")
        add_run(p_r, "المرحلة المتوسطة", size=8, color="64748B")
        
        # Center cell: Title banner
        c_center = row0.cells[1]
        p_c = c_center.paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c.paragraph_format.space_before = Pt(0)
        p_c.paragraph_format.space_after = Pt(2)
        set_bidi(p_c)
        add_run(p_c, "سجل المتابعة اليومية للطلاب\n", bold=True, size=15, color="1E3A8A")
        add_run(p_c, f"مادة الرياضيات  —  العام الدراسي 1448 هـ  —  الفصل الدراسي الأول", bold=True, size=9.5, color="D97706")
        
        # Left cell: Class & Teacher Info Box
        c_left = row0.cells[2]
        p_l = c_left.paragraphs[0]
        p_l.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(1)
        p_l.paragraph_format.line_spacing = 1.05
        set_bidi(p_l)
        add_run(p_l, f"الصف: ", bold=True, size=8.5, color="64748B")
        add_run(p_l, "الثالث المتوسط  |  ", bold=True, size=9, color="1E3A8A")
        add_run(p_l, f"{class_name}\n", bold=True, size=9.5, color="047857")
        add_run(p_l, f"معلم المادة: ", bold=True, size=8.5, color="64748B")
        add_run(p_l, "أ. محمد عبدالله جمعة\n", bold=True, size=9.5, color="1E3A8A")
        add_run(p_l, f"عدد الطلاب: ", size=8, color="64748B")
        add_run(p_l, f"{len(students)} طالباً", bold=True, size=8.5, color="334155")
        
        # Small gap
        p_gap = doc.add_paragraph()
        p_gap.paragraph_format.space_before = Pt(0)
        p_gap.paragraph_format.space_after = Pt(2)
        
        # 2. Main Daily Register Table (27 columns)
        # Rows: 3 header rows + len(students) rows
        num_student_rows = len(students)
        total_rows = 3 + num_student_rows
        
        tbl = doc.add_table(rows=total_rows, cols=27)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(tbl)
        
        # Column widths:
        # Col 0 (م): 0.85 cm
        # Col 1 (اسم الطالب): 4.85 cm
        # Col 2..26 (25 days): 0.88 cm each
        col_widths = [Cm(0.85), Cm(4.85)] + [Cm(0.88)] * 25
        
        # Apply column grid widths
        tblPr = tbl._tbl.tblPr
        tblGrid = OxmlElement('w:tblGrid')
        for w in col_widths:
            gridCol = OxmlElement('w:gridCol')
            gridCol.set(qn('w:w'), str(int(w.inches * 1440)))
            tblGrid.append(gridCol)
        tbl._tbl.insert(tbl._tbl.index(tblPr) + 1, tblGrid)
        
        # Merges for headers
        # Col 0 (م): merge rows 0, 1, 2
        tbl.rows[0].cells[0].merge(tbl.rows[2].cells[0])
        # Col 1 (اسم الطالب): merge rows 0, 1
        tbl.rows[0].cells[1].merge(tbl.rows[1].cells[1])
        # Row 0 Weeks:
        weeks = ["الأسبوع الأول", "الأسبوع الثاني", "الأسبوع الثالث", "الأسبوع الرابع", "الأسبوع الخامس"]
        week_start_cols = [2, 7, 12, 17, 22]
        for w_idx, s_col in enumerate(week_start_cols):
            tbl.rows[0].cells[s_col].merge(tbl.rows[0].cells[s_col + 4])
            
        # Format Header Row 0
        r0 = tbl.rows[0]
        # 'م' cell
        c_m = r0.cells[0]
        set_cell_background(c_m, "1E3A8A")
        set_cell_v_center(c_m)
        set_cell_margins(c_m, top=20, bottom=20, left=10, right=10)
        p = c_m.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_bidi(p)
        add_run(p, "م", bold=True, size=9.5, color="FFFFFF")
        
        # 'اسم الطالب' cell
        c_name = r0.cells[1]
        set_cell_background(c_name, "1E3A8A")
        set_cell_v_center(c_name)
        set_cell_margins(c_name, top=20, bottom=20, left=40, right=40)
        p = c_name.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_bidi(p)
        add_run(p, "اسم الطالب", bold=True, size=10, color="FFFFFF")
        
        # Week headers
        week_bg_colors = ["1E3A8A", "1E40AF", "1D4ED8", "2563EB", "3B82F6"]
        for w_idx, s_col in enumerate(week_start_cols):
            cell = r0.cells[s_col]
            set_cell_background(cell, "1E3A8A")
            set_cell_v_center(cell)
            set_cell_margins(cell, top=20, bottom=20, left=20, right=20)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_bidi(p)
            add_run(p, weeks[w_idx], bold=True, size=9.5, color="FFFFFF")
            
        # Format Header Row 1 (Days of the week)
        r1 = tbl.rows[1]
        days = ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"]
        for w_idx, s_col in enumerate(week_start_cols):
            for d_idx, day_name in enumerate(days):
                cell = r1.cells[s_col + d_idx]
                set_cell_background(cell, "2563EB")
                set_cell_v_center(cell)
                set_cell_margins(cell, top=15, bottom=15, left=5, right=5)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_bidi(p)
                # Shorten day name slightly for tight column width
                d_short = day_name if day_name != "الأربعاء" else "أربعاء"
                add_run(p, d_short, bold=True, size=7.5, color="FFFFFF")
                
        # Format Header Row 2 (Date row)
        r2 = tbl.rows[2]
        # Col 1 is 'التاريخ'
        c_date_lbl = r2.cells[1]
        set_cell_background(c_date_lbl, "E2E8F0")
        set_cell_v_center(c_date_lbl)
        set_cell_margins(c_date_lbl, top=15, bottom=15, left=40, right=40)
        p = c_date_lbl.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_bidi(p)
        add_run(p, "التاريخ", bold=True, size=8, color="1E293B")
        
        # Daily date placeholders
        for c_idx in range(2, 27):
            cell = r2.cells[c_idx]
            set_cell_background(cell, "F1F5F9")
            set_cell_v_center(cell)
            set_cell_margins(cell, top=10, bottom=10, left=2, right=2)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_bidi(p)
            add_run(p, "/  /", size=6.5, color="64748B")
            
        # Format Student Rows
        for s_idx, student_name in enumerate(students):
            row = tbl.rows[3 + s_idx]
            
            # Row height (approx 0.54 cm for compact fit)
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:trHeight {nsdecls("w")} w:val="310" w:hRule="atLeast"/>'))
            
            bg_color = "F8FAFC" if s_idx % 2 == 1 else "FFFFFF"
            
            # Number cell
            c_num = row.cells[0]
            set_cell_background(c_num, "F1F5F9" if s_idx % 2 == 1 else "F8FAFC")
            set_cell_v_center(c_num)
            set_cell_margins(c_num, top=10, bottom=10, left=5, right=5)
            p = c_num.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_bidi(p)
            add_run(p, str(s_idx + 1), bold=True, size=8.5, color="1E3A8A")
            
            # Student Name cell
            c_name = row.cells[1]
            set_cell_background(c_name, bg_color)
            set_cell_v_center(c_name)
            set_cell_margins(c_name, top=10, bottom=10, left=20, right=30)
            p = c_name.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            set_bidi(p)
            add_run(p, f" {student_name}", bold=True, size=9, color="0F172A")
            
            # 25 day cells
            for c_idx in range(2, 27):
                cell = row.cells[c_idx]
                set_cell_background(cell, bg_color)
                set_cell_v_center(cell)
                set_cell_margins(cell, top=5, bottom=5, left=2, right=2)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_bidi(p)
                
        # Apply borders across all cells
        apply_custom_borders(tbl, total_rows)
        
        # 3. Footer Table: Legend & Signatures
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        
        ftr_tbl = doc.add_table(rows=2, cols=1)
        ftr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_rtl(ftr_tbl)
        
        # Legend Row
        c_leg = ftr_tbl.rows[0].cells[0]
        c_leg.width = Cm(27.7)
        set_cell_background(c_leg, "F1F5F9")
        set_cell_margins(c_leg, top=25, bottom=25, left=40, right=40)
        p_leg = c_leg.paragraphs[0]
        p_leg.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_bidi(p_leg)
        
        add_run(p_leg, "📌 مفتاح رموز المتابعة اليومية:  ", bold=True, size=8.5, color="1E3A8A")
        add_run(p_leg, " [ت] ", bold=True, size=8.5, color="B45309")
        add_run(p_leg, "تأخير    ", size=8, color="1E293B")
        add_run(p_leg, " [غ] ", bold=True, size=8.5, color="DC2626")
        add_run(p_leg, "غياب    ", size=8, color="1E293B")
        add_run(p_leg, " [ز] ", bold=True, size=8.5, color="047857")
        add_run(p_leg, "تميز وإبداع    ", size=8, color="1E293B")
        add_run(p_leg, " [س] ", bold=True, size=8.5, color="D97706")
        add_run(p_leg, "سلوك ومواظبة    ", size=8, color="1E293B")
        add_run(p_leg, " [و] ", bold=True, size=8.5, color="2563EB")
        add_run(p_leg, "واجب منزلي    ", size=8, color="1E293B")
        add_run(p_leg, " [م] ", bold=True, size=8.5, color="0D9488")
        add_run(p_leg, "مشاركة صفية    ", size=8, color="1E293B")
        add_run(p_leg, " [ب] ", bold=True, size=8.5, color="7C3AED")
        add_run(p_leg, "مهمة أدائية / بحث", size=8, color="1E293B")
        
        # Signatures Row
        c_sig = ftr_tbl.rows[1].cells[0]
        c_sig.width = Cm(27.7)
        set_cell_background(c_sig, "FFFFFF")
        set_cell_margins(c_sig, top=35, bottom=20, left=40, right=40)
        p_sig = c_sig.paragraphs[0]
        p_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_bidi(p_sig)
        
        add_run(p_sig, "معلم المادة: ", bold=True, size=9, color="334155")
        add_run(p_sig, "أ. محمد عبدالله جمعة                        ", bold=True, size=9.5, color="1E3A8A")
        add_run(p_sig, "المشرف التربوي: ", bold=True, size=9, color="334155")
        add_run(p_sig, "..........................................                        ", size=9, color="94A3B8")
        add_run(p_sig, "مدير المدرسة: ", bold=True, size=9, color="334155")
        add_run(p_sig, "..........................................", size=9, color="94A3B8")
        
        # Set border for footer table
        set_cell_borders(c_leg, 
                         top={'val':'single', 'sz':'4', 'color':'CBD5E1'},
                         bottom={'val':'single', 'sz':'4', 'color':'CBD5E1'},
                         left={'val':'single', 'sz':'4', 'color':'CBD5E1'},
                         right={'val':'single', 'sz':'4', 'color':'CBD5E1'})
        set_cell_borders(c_sig,
                         top=None,
                         bottom=None,
                         left=None,
                         right=None)

    doc.save(filename)
    print(f"File saved successfully as: {filename}")

def set_bidi(paragraph):
    paragraph.paragraph_format.bidi = True
    pPr = paragraph._p.get_or_add_pPr()
    pPr.append(parse_xml(f'<w:bidi {nsdecls("w")}/>'))

def add_run(paragraph, text, bold=False, italic=False, size=9, color="0F172A"):
    run = paragraph.add_run(text)
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

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_cell_margins(cell, top=20, bottom=20, left=40, right=40):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>'))

def set_cell_v_center(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

def set_table_rtl(table):
    tblPr = table._tbl.tblPr
    tblPr.append(parse_xml(f'<w:bidiVisual {nsdecls("w")}/>'))

def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
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

def apply_custom_borders(tbl, total_rows):
    # Apply crisp borders to the table cells
    # Week end column boundaries: cols 6, 11, 16, 21, 26
    week_ends = {6, 11, 16, 21, 26}
    
    for r_idx in range(total_rows):
        row = tbl.rows[r_idx]
        for c_idx in range(len(row.cells)):
            cell = row.cells[c_idx]
            
            # Default thin border
            border_top = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
            border_bottom = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
            border_left = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
            border_right = {'val': 'single', 'sz': '4', 'color': 'CBD5E1'}
            
            # In RTL:
            # left border is the left side of the cell.
            # right border is the right side of the cell.
            # If this cell is the left-most edge of a week, give it a slightly darker left border
            if c_idx in week_ends:
                border_left = {'val': 'single', 'sz': '8', 'color': '475569'}
            if c_idx == 1: # After student name
                border_left = {'val': 'single', 'sz': '8', 'color': '1E3A8A'}
            if c_idx == 0: # After number
                border_left = {'val': 'single', 'sz': '6', 'color': '94A3B8'}
                
            # Header top borders
            if r_idx == 0:
                border_top = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
            if r_idx == 2:
                border_bottom = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
            if r_idx == total_rows - 1:
                border_bottom = {'val': 'single', 'sz': '10', 'color': '1E3A8A'}
                
            set_cell_borders(cell, top=border_top, bottom=border_bottom, left=border_left, right=border_right)

if __name__ == '__main__':
    create_full_document()
