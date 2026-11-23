# -*- coding: utf-8 -*-
import base64
import os

with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

logo_html = f'<img src="data:image/png;base64,{logo_b64}" alt="شعار المدارس المتقدمة" style="height: 75px; width: auto; object-fit: contain;">'

header_html = f'''
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بمحافظة جدة</div>
        <div class="school-highlight">المدارس المتقدمة للتعلم الذكي بجدة</div>
        <div>قسم الرياضيات | المرحلة المتوسطة</div>
    </div>
    <div class="sch-logo-center">
        {logo_html}
        <div style="font-size:0.8rem; font-weight:800; color:#1e3a8a; margin-top:3px;">مدارس التعلّم الذكي</div>
    </div>
    <div class="sch-info-left-ar">
        <div>مادة: الرياضيات (الصف الثالث المتوسط)</div>
        <div>الفصل الدراسي الثاني - العام الدراسي ١٤٤٧ / ١٤٤٨هـ (٢٠٢٦م)</div>
        <div>معتمدة وفق معايير وزارة التعليم ومنهجية STEM</div>
    </div>
</div>
'''

footer_sig_html = '''
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>المدارس المتقدمة للتعلم الذكي بجدة | رؤية المملكة ٢٠٣٠</span>
    </div>
    <div class="sheet-footer-left">
        <div class="teacher-signature-card">
            <span class="teacher-sig-label">معلم المادة:</span>
            <span class="teacher-sig-name">أ. محمد عبدالله جمعة</span>
            <div class="teacher-school-subtext">المدارس المتقدمة للتعلم الذكي بجدة</div>
        </div>
    </div>
</div>
'''

def ws_top_toolbar(sheet_id):
    return f'''
<div class="worksheet-top-toolbar no-print">
    <button type="button" class="btn-toggle-answers" onclick="toggleWorksheetAnswers('{sheet_id}', this)">
        <span class="icon">👁️</span> إظهار الإجابة على المسائل
    </button>
    <span class="toolbar-hint">💡 (هذا الزر مخصص للمعلم فقط ولن يظهر مطلقاً للطالب عند الطباعة أو التصدير إلى PDF)</span>
</div>
'''

# Let's write the complete builder script in python that does not use f-strings for LaTeX
script_writer = '''# -*- coding: utf-8 -*-
import base64
import os

with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

logo_html = '<img src="data:image/png;base64,' + logo_b64 + '" alt="شعار المدارس المتقدمة" style="height: 75px; width: auto; object-fit: contain;">'

header_html = """
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بمحافظة جدة</div>
        <div class="school-highlight">المدارس المتقدمة للتعلم الذكي بجدة</div>
        <div>قسم الرياضيات | المرحلة المتوسطة</div>
    </div>
    <div class="sch-logo-center">
        """ + logo_html + """
        <div style="font-size:0.8rem; font-weight:800; color:#1e3a8a; margin-top:3px;">مدارس التعلّم الذكي</div>
    </div>
    <div class="sch-info-left-ar">
        <div>مادة: الرياضيات (الصف الثالث المتوسط)</div>
        <div>الفصل الدراسي الثاني - العام الدراسي ١٤٤٧ / ١٤٤٨هـ (٢٠٢٦م)</div>
        <div>معتمدة وفق معايير وزارة التعليم ومنهجية STEM</div>
    </div>
</div>
"""

footer_sig_html = """
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>المدارس المتقدمة للتعلم الذكي بجدة | رؤية المملكة ٢٠٣٠</span>
    </div>
    <div class="sheet-footer-left">
        <div class="teacher-signature-card">
            <span class="teacher-sig-label">معلم المادة:</span>
            <span class="teacher-sig-name">أ. محمد عبدالله جمعة</span>
            <div class="teacher-school-subtext">المدارس المتقدمة للتعلم الذكي بجدة</div>
        </div>
    </div>
</div>
"""

def ws_top_toolbar(sheet_id):
    return """
<div class="worksheet-top-toolbar no-print">
    <button type="button" class="btn-toggle-answers" onclick="toggleWorksheetAnswers('""" + sheet_id + """', this)">
        <span class="icon">👁️</span> إظهار الإجابة على المسائل
    </button>
    <span class="toolbar-hint">💡 (هذا الزر مخصص للمعلم فقط ولن يظهر مطلقاً للطالب عند الطباعة أو التصدير إلى PDF)</span>
</div>
"""

parts = []

parts.append(r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة الشاملة: المتباينات الخطية | أ. محمد عبدالله جمعة | المدارس المتقدمة للتعلم الذكي بجدة</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <!-- MathJax 3 Configuration for Arabic Mathematics -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
            },
            options: {
                renderActions: {
                    addMenu: []
                }
            },
            svg: {
                fontCache: 'global'
            }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {
            --primary: #1e3a8a;
            --primary-dark: #172554;
            --primary-light: #eff6ff;
            --secondary: #0d9488;
            --secondary-light: #f0fdfa;
            --accent: #d97706;
            --danger: #dc2626;
            --danger-light: #fef2f2;
            --dark: #0f172a;
            --gray-100: #f8fafc;
            --gray-200: #e2e8f0;
            --gray-300: #cbd5e1;
            --gray-600: #475569;
            --gray-700: #334155;
            --white: #ffffff;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -2px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', 'Cairo', sans-serif;
        }

        body {
            background-color: #f1f5f9;
            color: var(--dark);
            line-height: 1.75;
            padding-bottom: 60px;
        }

        /* Top Sticky Navbar */
        .sticky-nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(8px);
            color: var(--white);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            border-bottom: 2px solid #2563eb;
        }

        .nav-brand {
            font-size: 1.15rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #60a5fa;
        }

        .nav-links {
            display: flex;
            gap: 8px;
            list-style: none;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: #e2e8f0;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 6px 14px;
            border-radius: var(--radius-sm);
            transition: all 0.2s ease;
            background: rgba(255, 255, 255, 0.08);
        }

        .nav-links a:hover {
            background: #2563eb;
            color: #ffffff;
            transform: translateY(-1px);
        }

        .print-btn-header {
            background: #10b981;
            color: white;
            border: none;
            padding: 7px 18px;
            border-radius: var(--radius-sm);
            font-weight: 700;
            cursor: pointer;
            transition: background 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .print-btn-header:hover {
            background: #059669;
        }

        /* Container */
        .main-container {
            max-width: 1180px;
            margin: 24px auto;
            padding: 0 16px;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #0369a1 100%);
            color: var(--white);
            padding: 36px 32px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            margin-bottom: 36px;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }

        .hero-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.35);
            color: #ffffff;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2.1rem;
            font-weight: 900;
            margin-bottom: 10px;
            line-height: 1.3;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            opacity: 0.95;
            max-width: 900px;
        }

        /* Section Separators */
        .master-section {
            margin-bottom: 50px;
        }

        .section-header-banner {
            background: var(--white);
            border-right: 8px solid var(--primary);
            padding: 18px 24px;
            border-radius: var(--radius-md);
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .section-header-banner.plans { border-right-color: #2563eb; }
        .section-header-banner.summaries { border-right-color: #0d9488; }
        .section-header-banner.worksheets { border-right-color: #d97706; }

        .section-header-banner h2 {
            font-size: 1.55rem;
            font-weight: 800;
            color: var(--dark);
        }

        .section-badge {
            font-size: 0.85rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            background: var(--gray-100);
            border: 1px solid var(--gray-300);
            color: var(--gray-700);
        }

        /* Unit Cards */
        .unit-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
        }

        .unit-title-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 16px;
            margin-bottom: 22px;
            border-bottom: 2px solid var(--gray-100);
        }

        .unit-title-box h3 {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .page-range-pill {
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
        }

        /* School Official Header Block */
        .school-official-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #0f172a;
            padding-bottom: 14px;
            margin-bottom: 20px;
            background: #ffffff;
        }

        .sch-info-right {
            text-align: right;
            font-size: 0.88rem;
            font-weight: 700;
            line-height: 1.5;
            color: #1e293b;
        }

        .sch-info-right .ministry-name {
            font-size: 0.82rem;
            color: #475569;
        }

        .sch-info-right .school-highlight {
            font-size: 1.05rem;
            color: #1e3a8a;
            font-weight: 900;
        }

        .sch-logo-center {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }

        .sch-info-left-ar {
            text-align: left;
            font-size: 0.88rem;
            font-weight: 700;
            line-height: 1.5;
            color: #1e293b;
        }

        /* Worksheet Paper Container */
        .worksheet-paper {
            background: var(--white);
            border: 2px solid #1e293b;
            border-radius: var(--radius-md);
            padding: 28px;
            margin-bottom: 34px;
            box-shadow: var(--shadow-sm);
            position: relative;
        }

        .ws-meta-bar {
            background: #f8fafc;
            border: 1px dashed var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            font-size: 0.95rem;
            font-weight: 700;
        }

        .ws-question-block {
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--gray-200);
        }

        .ws-q-title {
            font-weight: 800;
            font-size: 1.05rem;
            margin-bottom: 10px;
            color: var(--primary-dark);
        }

        .mcq-options-vertical {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 10px 0 10px 18px;
        }

        .mcq-option-line {
            background: #f8fafc;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.95rem;
        }

        /* INLINE ANSWERS (on the question itself, hidden by default) */
        .inline-answer-badge,
        .inline-explanation,
        .inline-tf-answer,
        .problem-solution-inline {
            display: none;
        }

        /* When worksheet has .show-answers class, reveal inline solutions */
        .worksheet-paper.show-answers .inline-answer-badge {
            display: inline-block !important;
            background: #16a34a;
            color: white;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.82rem;
            font-weight: 800;
        }

        .worksheet-paper.show-answers .inline-explanation {
            display: block !important;
            background: #f0fdf4;
            border-right: 4px solid #16a34a;
            padding: 8px 14px;
            margin: 8px 0 4px;
            color: #166534;
            font-size: 0.9rem;
            border-radius: 0 4px 4px 0;
        }

        .worksheet-paper.show-answers .inline-tf-answer {
            display: inline-block !important;
            background: #ecfdf5;
            border: 1px solid #86efac;
            color: #065f46;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-right: 8px;
        }

        .worksheet-paper.show-answers .problem-solution-inline {
            display: block !important;
            background: #ecfdf5;
            border: 2px solid #86efac;
            border-radius: 8px;
            padding: 14px 18px;
            margin: 10px 0;
            color: #065f46;
            font-size: 0.95rem;
            line-height: 1.8;
        }

        /* Worksheet Top Toolbar */
        .worksheet-top-toolbar {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 10px 16px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .btn-toggle-answers {
            background: #0d9488;
            color: white;
            border: none;
            padding: 8px 18px;
            border-radius: 6px;
            font-size: 0.92rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-toggle-answers:hover {
            background: #0f766e;
            transform: translateY(-1px);
        }

        .btn-toggle-answers.active {
            background: #dc2626;
        }

        .toolbar-hint {
            font-size: 0.82rem;
            color: #64748b;
            font-weight: 600;
        }

        /* Teacher Signature Block */
        .sheet-footer-bar {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            margin-top: 28px;
            padding-top: 14px;
            border-top: 2px solid #e2e8f0;
        }

        .sheet-footer-right {
            font-size: 0.85rem;
            color: var(--gray-600);
            font-weight: 600;
        }

        .sheet-footer-left {
            text-align: left;
            direction: rtl;
        }

        .teacher-signature-card {
            background: #f8fafc;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 8px 16px;
            display: inline-block;
            text-align: right;
        }

        .teacher-sig-label {
            font-size: 0.8rem;
            color: var(--gray-600);
            font-weight: 700;
            display: block;
        }

        .teacher-sig-name {
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--primary);
            border-bottom: 2px solid #1e3a8a;
            padding-bottom: 2px;
            display: inline-block;
        }

        .teacher-school-subtext {
            font-size: 0.75rem;
            color: #0d9488;
            font-weight: 700;
            margin-top: 2px;
        }

        /* Data Tables */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.95rem;
        }

        .data-table th, .data-table td {
            border: 1px solid var(--gray-200);
            padding: 12px 16px;
            text-align: right;
        }

        .data-table th {
            background: #f8fafc;
            color: var(--dark);
            font-weight: 700;
        }

        /* Frayer Model */
        .frayer-box {
            background: var(--gray-100);
            border: 2px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 16px;
            margin: 18px 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }

        .frayer-center-title {
            grid-column: 1 / -1;
            background: var(--primary);
            color: var(--white);
            text-align: center;
            padding: 10px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 1.05rem;
        }

        .frayer-quadrant {
            background: var(--white);
            border-radius: var(--radius-sm);
            padding: 14px 16px;
            border: 1px solid var(--gray-200);
        }

        .frayer-quadrant h4 {
            color: var(--secondary);
            font-size: 0.95rem;
            margin-bottom: 6px;
            border-bottom: 2px solid var(--secondary-light);
            padding-bottom: 4px;
            font-weight: 700;
        }

        /* STEM Matrix */
        .stem-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 14px;
            margin: 16px 0;
        }

        .stem-pillar {
            background: var(--gray-100);
            border-radius: var(--radius-sm);
            padding: 14px;
            border-top: 4px solid var(--secondary);
        }

        .stem-pillar.s { border-top-color: #0284c7; }
        .stem-pillar.t { border-top-color: #6366f1; }
        .stem-pillar.e { border-top-color: #f59e0b; }
        .stem-pillar.m { border-top-color: #10b981; }

        .stem-pillar h4 {
            font-size: 1rem;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Rules Cards */
        .rule-card-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }

        @media (max-width: 768px) {
            .rule-card-grid { grid-template-columns: 1fr; }
            .frayer-box { grid-template-columns: 1fr; }
            .school-official-header { flex-direction: column; gap: 10px; text-align: center; }
            .sch-info-right, .sch-info-left-ar { text-align: center; }
        }

        .rule-subcard {
            border-radius: var(--radius-sm);
            padding: 16px;
            border-right: 5px solid;
        }

        .rule-subcard.positive {
            background: #f0fdf4;
            border-color: #22c55e;
        }

        .rule-subcard.negative {
            background: #fef2f2;
            border-color: #ef4444;
        }

        .callout-box {
            padding: 14px 18px;
            border-radius: var(--radius-sm);
            margin: 14px 0;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .callout-warning {
            background: var(--danger-light);
            border-right: 5px solid var(--danger);
            color: #991b1b;
        }

        .nl-svg-container {
            width: 100%;
            max-width: 480px;
            margin: 12px auto;
            display: block;
        }

        /* Print Settings: Strictly hide toolbar & navigation */
        @media print {
            .sticky-nav, .worksheet-top-toolbar, .no-print { display: none !important; }
            body { background: white !important; padding: 0 !important; }
            .main-container { max-width: 100% !important; margin: 0 !important; padding: 0 !important; }
            .hero-banner { box-shadow: none !important; border-radius: 0 !important; margin-bottom: 20px !important; }
            .unit-card, .worksheet-paper { 
                box-shadow: none !important; 
                page-break-inside: avoid !important;
                margin-bottom: 25px !important;
            }
            .page-break {
                page-break-before: always !important;
            }
        }
    </style>
</head>
<body>

<!-- Navigation Bar -->
<nav class="sticky-nav">
    <div class="nav-brand">
        🏫 المدارس المتقدمة للتعلم الذكي بجدة | المتباينات الخطية (ص ١٣٠ - ١٤٧)
    </div>
    <ul class="nav-links">
        <li><a href="#plans-section">📑 خطط التحضير (STEM)</a></li>
        <li><a href="#summaries-section">📚 الملخصات الشاملة للطلاب</a></li>
        <li><a href="#worksheets-section">📝 أوراق العمل والاختبارات</a></li>
    </ul>
    <button class="print-btn-header" onclick="window.print()">🖨️ طباعة الحقيبة كاملة</button>
</nav>

<div class="main-container">

    <!-- Hero Banner -->
    <header class="hero-banner">
        <span class="hero-tag">المملكة العربية السعودية | وزارة التعليم ٢٠٢٦م</span>
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: المتباينات الخطية</h1>
        <p class="hero-subtitle">
            <strong>المدارس المتقدمة للتعلم الذكي بجدة</strong> — إعداد المعلم: <strong>أ. محمد عبدالله جمعة</strong>. حقيبة موحدة تضم: خطط التدريس وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية بأزرار إظهار الحل النموذجي أعلى كل ورقة مع ظهور الإجابة على نفس المسألة، ومكتوبة بالكامل بالأرقام العربية المعتمدة، وشاملة الصفحات من ١٣٠ إلى ١٤٧ من كتاب الرياضيات للصف الثالث المتوسط.
        </p>
    </header>
""")
''')

with open('append_suite.py', 'w', encoding='utf-8') as f:
    f.write(script_writer)

print("Base builder written successfully")
