import json
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

def generate_html_register(output_html="سجل_متابعة_الرياضيات_ثالث_متوسط.html"):
    classes = [
        ("فصل ( 3 / 1 )", students_class_1),
        ("فصل ( 3 / 2 )", students_class_2)
    ]
    
    html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>سجل المتابعة اليومية للطلاب - مادة الرياضيات - ثالث متوسط</title>
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 landscape;
    margin: 5mm 6mm;
  }
  
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  
  body {
    font-family: 'Tajawal', 'Segoe UI', Tahoma, Arial, sans-serif;
    margin: 0;
    padding: 10px;
    background-color: #f1f5f9;
    color: #0f172a;
    direction: rtl;
  }
  
  .no-print-bar {
    max-width: 1100px;
    margin: 0 auto 15px auto;
    background: #ffffff;
    padding: 12px 20px;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  }
  
  .btn-print {
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    color: #ffffff;
    border: none;
    padding: 10px 24px;
    font-size: 14px;
    font-weight: 700;
    border-radius: 8px;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s ease;
  }
  
  .btn-print:hover {
    background: linear-gradient(135deg, #172554, #1d4ed8);
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(37,99,235,0.3);
  }
  
  .badge-info {
    font-size: 13px;
    color: #475569;
    font-weight: 600;
  }
  
  /* Sheet Container: Fits exactly on single A4 Landscape */
  .sheet {
    width: 285mm;
    min-height: 198mm;
    max-height: 200mm;
    margin: 0 auto 20px auto;
    background: #ffffff;
    padding: 6mm 8mm;
    border-radius: 4px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  
  /* Header Section */
  .header-grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    align-items: center;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 5px;
    margin-bottom: 5px;
  }
  
  .hdr-right {
    text-align: right;
    font-size: 11px;
    line-height: 1.35;
    color: #334155;
  }
  
  .hdr-right strong {
    color: #1e3a8a;
    font-size: 12px;
  }
  
  .hdr-center {
    text-align: center;
  }
  
  .main-title {
    font-size: 18px;
    font-weight: 900;
    color: #1e3a8a;
    margin: 0;
    letter-spacing: -0.3px;
  }
  
  .sub-title {
    font-size: 11px;
    font-weight: 700;
    color: #b45309;
    margin-top: 2px;
  }
  
  .hdr-left {
    text-align: left;
    font-size: 11px;
    line-height: 1.35;
    color: #334155;
  }
  
  .badge-class {
    display: inline-block;
    background: #ecfdf5;
    color: #047857;
    font-weight: 800;
    padding: 1px 8px;
    border-radius: 4px;
    border: 1px solid #a7f3d0;
  }
  
  /* Main Table */
  .table-container {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
  }
  
  table.register-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
    font-size: 10px;
    border: 1.5px solid #1e3a8a;
  }
  
  table.register-table th, 
  table.register-table td {
    border: 1px solid #cbd5e1;
    text-align: center;
    vertical-align: middle;
    padding: 0;
    height: 19.5px;
  }
  
  /* Column Widths */
  .col-num {
    width: 24px;
    background-color: #f8fafc;
    font-weight: 800;
    color: #1e3a8a;
  }
  
  .col-name {
    width: 190px;
    text-align: right !important;
    padding-right: 8px !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-weight: 700;
    color: #0f172a;
    border-left: 2px solid #1e3a8a !important;
  }
  
  .col-day {
    width: 28px;
  }
  
  /* Week border separation */
  .col-week-end {
    border-left: 1.8px solid #475569 !important;
  }
  
  /* Header Rows */
  .row-weeks th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    height: 22px;
    border-bottom: 1px solid #3b82f6;
  }
  
  .row-days th {
    background-color: #2563eb;
    color: #ffffff;
    font-size: 9px;
    font-weight: 700;
    height: 18px;
  }
  
  .row-date th {
    background-color: #f1f5f9;
    color: #475569;
    font-size: 9px;
    font-weight: 700;
    height: 17px;
  }
  
  .date-placeholder {
    font-size: 8px;
    color: #94a3b8;
    letter-spacing: -0.5px;
  }
  
  /* Student Rows */
  tr.student-row:nth-child(even) {
    background-color: #f8fafc;
  }
  
  tr.student-row:hover {
    background-color: #eff6ff;
  }
  
  /* Footer Section */
  .footer-container {
    margin-top: 5px;
  }
  
  .legend-box {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 4px 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    font-size: 10px;
    font-weight: 600;
  }
  
  .legend-title {
    color: #1e3a8a;
    font-weight: 800;
  }
  
  .legend-item {
    display: inline-flex;
    align-items: center;
    gap: 3px;
  }
  
  .code {
    display: inline-block;
    padding: 0 4px;
    border-radius: 3px;
    font-weight: 800;
    font-size: 10px;
  }
  
  .code-t { background: #fef3c7; color: #b45309; }
  .code-g { background: #fee2e2; color: #dc2626; }
  .code-z { background: #d1fae5; color: #047857; }
  .code-s { background: #ffedd5; color: #ea580c; }
  .code-w { background: #dbeafe; color: #1d4ed8; }
  .code-m { background: #ccfbf1; color: #0f766e; }
  .code-b { background: #ede9fe; color: #6d28d9; }
  
  .signatures-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    text-align: center;
    margin-top: 6px;
    padding-top: 4px;
    font-size: 11px;
    font-weight: 700;
    color: #334155;
  }
  
  .sig-dots {
    color: #94a3b8;
    font-weight: 400;
  }
  
  @media print {
    body {
      background-color: #ffffff;
      padding: 0;
    }
    .no-print-bar {
      display: none !important;
    }
    .sheet {
      width: 100% !important;
      min-height: 198mm !important;
      max-height: 200mm !important;
      margin: 0 !important;
      padding: 4mm 6mm !important;
      box-shadow: none !important;
      border-radius: 0 !important;
      page-break-after: always !important;
    }
  }
</style>
</head>
<body>

<div class="no-print-bar">
  <div>
    <span style="font-size: 16px; font-weight: 800; color: #1e3a8a;">سجل المتابعة اليومية — مادة الرياضيات (ثالث متوسط)</span>
    <div class="badge-info">معلم المادة: أ. محمد عبدالله جمعة | مجهز للطباعة المباشرة على مقاس A4 بالعرض (Landscape)</div>
  </div>
  <button class="btn-print" onclick="window.print()">
    <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path>
    </svg>
    طباعة السجل (A4 بالعرض)
  </button>
</div>
"""

    weeks = ["الأسبوع الأول", "الأسبوع الثاني", "الأسبوع الثالث", "الأسبوع الرابع", "الأسبوع الخامس"]
    days = ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"]
    week_end_indices = {4, 9, 14, 19, 24}

    for class_name, students in classes:
        html += f"""
<div class="sheet">
  <!-- Header -->
  <div class="header-grid">
    <div class="hdr-right">
      <strong>المملكة العربية السعودية</strong><br>
      وزارة التعليم — الإدارة العامة للتعليم<br>
      منصة الرائد التعليمية<br>
      المرحلة المتوسطة (بنين)
    </div>
    <div class="hdr-center">
      <h1 class="main-title">سجل المتابعة اليومية للطلاب</h1>
      <div class="sub-title">مادة الرياضيات — الفصل الدراسي الأول — العام الدراسي 1448 هـ</div>
    </div>
    <div class="hdr-left">
      الصف: <strong>الثالث المتوسط</strong><br>
      الفصل: <span class="badge-class">{class_name}</span><br>
      معلم المادة: <strong>أ. محمد عبدالله جمعة</strong><br>
      عدد الطلاب: <strong>{len(students)} طالباً</strong>
    </div>
  </div>

  <!-- Table -->
  <div class="table-container">
    <table class="register-table">
      <thead>
        <!-- Row 0: Weeks -->
        <tr class="row-weeks">
          <th rowspan="3" class="col-num">م</th>
          <th rowspan="2" class="col-name" style="text-align: center !important; color: #ffffff !important;">اسم الطالب</th>
"""
        for w in weeks:
            html += f'          <th colspan="5" class="col-week-end">{w}</th>\n'
            
        html += """        </tr>
        <!-- Row 1: Days -->
        <tr class="row-days">
"""
        day_counter = 0
        for _ in weeks:
            for d in days:
                cls_border = ' col-week-end' if day_counter in week_end_indices else ''
                html += f'          <th class="col-day{cls_border}">{d}</th>\n'
                day_counter += 1

        html += """        </tr>
        <!-- Row 2: Dates -->
        <tr class="row-date">
          <th class="col-name" style="text-align: center !important; background: #e2e8f0; color: #1e293b;">التاريخ</th>
"""
        day_counter = 0
        for _ in weeks:
            for _ in days:
                cls_border = ' col-week-end' if day_counter in week_end_indices else ''
                html += f'          <th class="col-day{cls_border}"><span class="date-placeholder">/&nbsp;&nbsp;/</span></th>\n'
                day_counter += 1

        html += """        </tr>
      </thead>
      <tbody>
"""
        for idx, student in enumerate(students):
            html += f"""        <tr class="student-row">
          <td class="col-num">{idx + 1}</td>
          <td class="col-name" title="{student}">{student}</td>
"""
            day_counter = 0
            for _ in weeks:
                for _ in days:
                    cls_border = ' col-week-end' if day_counter in week_end_indices else ''
                    html += f'          <td class="col-day{cls_border}"></td>\n'
                    day_counter += 1
            html += "        </tr>\n"

        html += """      </tbody>
    </table>
  </div>

  <!-- Footer -->
  <div class="footer-container">
    <div class="legend-box">
      <span class="legend-title">📌 مفتاح رموز المتابعة اليومية:</span>
      <span class="legend-item"><span class="code code-t">[ت]</span> تأخير</span>
      <span class="legend-item"><span class="code code-g">[غ]</span> غياب</span>
      <span class="legend-item"><span class="code code-z">[ز]</span> تميز وإبداع</span>
      <span class="legend-item"><span class="code code-s">[س]</span> سلوك ومواظبة</span>
      <span class="legend-item"><span class="code code-w">[و]</span> واجب منزلي</span>
      <span class="legend-item"><span class="code code-m">[م]</span> مشاركة صفية</span>
      <span class="legend-item"><span class="code code-b">[ب]</span> مهمة أدائية / بحث</span>
    </div>

    <div class="signatures-grid">
      <div>معلم المادة: <span style="color:#1e3a8a;">أ. محمد عبدالله جمعة</span></div>
      <div>المشرف التربوي: <span class="sig-dots">...................................................</span></div>
      <div>مدير المدرسة: <span class="sig-dots">...................................................</span></div>
    </div>
  </div>
</div>
"""

    html += """
</body>
</html>
"""
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML Register created: {output_html}")

if __name__ == '__main__':
    generate_html_register()
