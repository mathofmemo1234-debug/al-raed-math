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

html_content = f'''<!DOCTYPE html>
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
        window.MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
            }},
            options: {{
                renderActions: {{
                    addMenu: []
                }}
            }},
            svg: {{
                fontCache: 'global'
            }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <style>
        :root {{
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
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', 'Cairo', sans-serif;
        }}

        body {{
            background-color: #f1f5f9;
            color: var(--dark);
            line-height: 1.75;
            padding-bottom: 60px;
        }}

        /* Top Sticky Navbar */
        .sticky-nav {{
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
        }}

        .nav-brand {{
            font-size: 1.15rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 12px;
            color: #60a5fa;
        }}

        .nav-links {{
            display: flex;
            gap: 8px;
            list-style: none;
            flex-wrap: wrap;
        }}

        .nav-links a {{
            color: #e2e8f0;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 6px 14px;
            border-radius: var(--radius-sm);
            transition: all 0.2s ease;
            background: rgba(255, 255, 255, 0.08);
        }}

        .nav-links a:hover {{
            background: #2563eb;
            color: #ffffff;
            transform: translateY(-1px);
        }}

        .print-btn-header {{
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
        }}

        .print-btn-header:hover {{
            background: #059669;
        }}

        /* Container */
        .main-container {{
            max-width: 1180px;
            margin: 24px auto;
            padding: 0 16px;
        }}

        /* Hero Banner */
        .hero-banner {{
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #0369a1 100%);
            color: var(--white);
            padding: 36px 32px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            margin-bottom: 36px;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }}

        .hero-tag {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.35);
            color: #ffffff;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 12px;
        }}

        .hero-title {{
            font-size: 2.1rem;
            font-weight: 900;
            margin-bottom: 10px;
            line-height: 1.3;
        }}

        .hero-subtitle {{
            font-size: 1.05rem;
            opacity: 0.95;
            max-width: 900px;
        }}

        /* Section Separators */
        .master-section {{
            margin-bottom: 50px;
        }}

        .section-header-banner {{
            background: var(--white);
            border-right: 8px solid var(--primary);
            padding: 18px 24px;
            border-radius: var(--radius-md);
            margin-bottom: 24px;
            box-shadow: var(--shadow-sm);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .section-header-banner.plans {{ border-right-color: #2563eb; }}
        .section-header-banner.summaries {{ border-right-color: #0d9488; }}
        .section-header-banner.worksheets {{ border-right-color: #d97706; }}

        .section-header-banner h2 {{
            font-size: 1.55rem;
            font-weight: 800;
            color: var(--dark);
        }}

        .section-badge {{
            font-size: 0.85rem;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            background: var(--gray-100);
            border: 1px solid var(--gray-300);
            color: var(--gray-700);
        }}

        /* Unit Cards */
        .unit-card {{
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
        }}

        .unit-title-box {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 16px;
            margin-bottom: 22px;
            border-bottom: 2px solid var(--gray-100);
        }}

        .unit-title-box h3 {{
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .page-range-pill {{
            background: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
        }}

        /* School Official Header Block */
        .school-official-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #0f172a;
            padding-bottom: 14px;
            margin-bottom: 20px;
            background: #ffffff;
        }}

        .sch-info-right {{
            text-align: right;
            font-size: 0.88rem;
            font-weight: 700;
            line-height: 1.5;
            color: #1e293b;
        }}

        .sch-info-right .ministry-name {{
            font-size: 0.82rem;
            color: #475569;
        }}

        .sch-info-right .school-highlight {{
            font-size: 1.05rem;
            color: #1e3a8a;
            font-weight: 900;
        }}

        .sch-logo-center {{
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }}

        .sch-info-left-ar {{
            text-align: left;
            font-size: 0.88rem;
            font-weight: 700;
            line-height: 1.5;
            color: #1e293b;
        }}

        /* Worksheet Paper Container */
        .worksheet-paper {{
            background: var(--white);
            border: 2px solid #1e293b;
            border-radius: var(--radius-md);
            padding: 28px;
            margin-bottom: 34px;
            box-shadow: var(--shadow-sm);
            position: relative;
        }}

        .ws-meta-bar {{
            background: #f8fafc;
            border: 1px dashed var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            font-size: 0.95rem;
            font-weight: 700;
        }}

        .ws-question-block {{
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--gray-200);
        }}

        .ws-q-title {{
            font-weight: 800;
            font-size: 1.05rem;
            margin-bottom: 10px;
            color: var(--primary-dark);
        }}

        .mcq-options-vertical {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 10px 0 10px 18px;
        }}

        .mcq-option-line {{
            background: #f8fafc;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.95rem;
        }}

        /* Solution Toggle Button */
        .solution-btn-container {{
            margin: 20px 0 12px;
            text-align: center;
        }}

        .toggle-solution-btn {{
            background: linear-gradient(135deg, #0d9488, #0f766e);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 24px;
            font-size: 0.95rem;
            font-weight: 800;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(13, 148, 136, 0.2);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}

        .toggle-solution-btn:hover {{
            background: linear-gradient(135deg, #0f766e, #115e59);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(13, 148, 136, 0.3);
        }}

        .toggle-solution-btn.active {{
            background: linear-gradient(135deg, #dc2626, #b91c1c);
        }}

        /* Solution Display Box */
        .worksheet-solution-box {{
            background: #f0fdf4;
            border: 2px solid #22c55e;
            border-radius: var(--radius-md);
            padding: 20px;
            margin-top: 16px;
            animation: fadeIn 0.3s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .worksheet-solution-box h4 {{
            color: #166534;
            font-size: 1.1rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #bbf7d0;
            padding-bottom: 6px;
        }}

        /* Teacher Signature Block */
        .sheet-footer-bar {{
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            margin-top: 28px;
            padding-top: 14px;
            border-top: 2px solid #e2e8f0;
        }}

        .sheet-footer-right {{
            font-size: 0.85rem;
            color: var(--gray-600);
            font-weight: 600;
        }}

        .sheet-footer-left {{
            text-align: left;
            direction: rtl;
        }}

        .teacher-signature-card {{
            background: #f8fafc;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 8px 16px;
            display: inline-block;
            text-align: right;
        }}

        .teacher-sig-label {{
            font-size: 0.8rem;
            color: var(--gray-600);
            font-weight: 700;
            display: block;
        }}

        .teacher-sig-name {{
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--primary);
            border-bottom: 2px solid #1e3a8a;
            padding-bottom: 2px;
            display: inline-block;
        }}

        .teacher-school-subtext {{
            font-size: 0.75rem;
            color: #0d9488;
            font-weight: 700;
            margin-top: 2px;
        }}

        /* Data Tables */
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.95rem;
        }}

        .data-table th, .data-table td {{
            border: 1px solid var(--gray-200);
            padding: 12px 16px;
            text-align: right;
        }}

        .data-table th {{
            background: #f8fafc;
            color: var(--dark);
            font-weight: 700;
        }}

        /* Frayer Model */
        .frayer-box {{
            background: var(--gray-100);
            border: 2px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 16px;
            margin: 18px 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }}

        .frayer-center-title {{
            grid-column: 1 / -1;
            background: var(--primary);
            color: var(--white);
            text-align: center;
            padding: 10px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            font-size: 1.05rem;
        }}

        .frayer-quadrant {{
            background: var(--white);
            border-radius: var(--radius-sm);
            padding: 14px 16px;
            border: 1px solid var(--gray-200);
        }}

        .frayer-quadrant h4 {{
            color: var(--secondary);
            font-size: 0.95rem;
            margin-bottom: 6px;
            border-bottom: 2px solid var(--secondary-light);
            padding-bottom: 4px;
            font-weight: 700;
        }}

        /* STEM Matrix */
        .stem-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 14px;
            margin: 16px 0;
        }}

        .stem-pillar {{
            background: var(--gray-100);
            border-radius: var(--radius-sm);
            padding: 14px;
            border-top: 4px solid var(--secondary);
        }}

        .stem-pillar.s {{ border-top-color: #0284c7; }}
        .stem-pillar.t {{ border-top-color: #6366f1; }}
        .stem-pillar.e {{ border-top-color: #f59e0b; }}
        .stem-pillar.m {{ border-top-color: #10b981; }}

        .stem-pillar h4 {{
            font-size: 1rem;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        /* Rules Cards */
        .rule-card-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }}

        @media (max-width: 768px) {{
            .rule-card-grid {{ grid-template-columns: 1fr; }}
            .frayer-box {{ grid-template-columns: 1fr; }}
            .school-official-header {{ flex-direction: column; gap: 10px; text-align: center; }}
            .sch-info-right, .sch-info-left-ar {{ text-align: center; }}
        }}

        .rule-subcard {{
            border-radius: var(--radius-sm);
            padding: 16px;
            border-right: 5px solid;
        }}

        .rule-subcard.positive {{
            background: #f0fdf4;
            border-color: #22c55e;
        }}

        .rule-subcard.negative {{
            background: #fef2f2;
            border-color: #ef4444;
        }}

        .callout-box {{
            padding: 14px 18px;
            border-radius: var(--radius-sm);
            margin: 14px 0;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .callout-warning {{
            background: var(--danger-light);
            border-right: 5px solid var(--danger);
            color: #991b1b;
        }}

        .nl-svg-container {{
            width: 100%;
            max-width: 480px;
            margin: 12px auto;
            display: block;
        }}

        /* Print Settings */
        @media print {{
            .sticky-nav {{ display: none !important; }}
            .toggle-solution-btn {{ display: none !important; }}
            body {{ background: white !important; padding: 0 !important; }}
            .main-container {{ max-width: 100% !important; margin: 0 !important; padding: 0 !important; }}
            .hero-banner {{ box-shadow: none !important; border-radius: 0 !important; margin-bottom: 20px !important; }}
            .unit-card, .worksheet-paper {{ 
                box-shadow: none !important; 
                page-break-inside: avoid !important;
                margin-bottom: 25px !important;
            }}
            .worksheet-solution-box {{
                display: block !important;
            }}
            .page-break {{
                page-break-before: always !important;
            }}
        }}
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
            <strong>المدارس المتقدمة للتعلم الذكي بجدة</strong> — إعداد المعلم: <strong>أ. محمد عبدالله جمعة</strong>. حقيبة موحدة تضم: خطط التدريس وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية بأزرار إظهار الحل النموذجي، مكتوبة بالكامل بالأرقام العربية المعتمدة، وشاملة الصفحات من ١٣٠ إلى ١٤٧ من كتاب الرياضيات للصف الثالث المتوسط.
        </p>
    </header>

    <!-- ========================================================================= -->
    <!-- القسم الأول: خطط التدريس والتحضير وفق منهجية STEM (متتالية) -->
    <!-- ========================================================================= -->
    <section id="plans-section" class="master-section">
        <div class="section-header-banner plans">
            <h2>📑 القسم الأول: خطط التدريس والتحضير وفق معايير STEM السبعة المعتمدة (متتالية)</h2>
            <span class="section-badge">إعداد: أ. محمد عبدالله جمعة</span>
        </div>

        <!-- الخطة 1: الدرس 4-2 -->
        <article class="unit-card" id="plan-4-2">
            <div class="unit-title-box">
                <h3><span>١️⃣</span> خطة الدرس (٤-٢): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٣٠ – ١٣٤</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الأعداد والعمليات والجبر | <strong>المعيار الوزاري:</strong> حل متباينات الخطوة الواحدة باستخدام الضرب والقسمة وتمثيل مجموعة الحل بيانياً على خط الأعداد.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينات خطية تتضمن خاصية الضرب (في عدد موجب وفي عدد سالب) بخطوات جبرية صحيحة بنسبة إتقان ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يطبق الطالب خاصية القسمة على المتباينات مع عكس اتجاه رمز التباين عند القسمة على عدد سالب دون أي خطأ.</li>
                <li><strong>الهدف ٣:</strong> أن ينمذج الطالب مسألة شراء واقعية من واقع الحياة في صورة متباينة خطية ويحلها ويتحقق من معقولية الناتج.</li>
            </ul>

            <h4 style="margin-top:16px;">٢. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:16px; margin:10px 0;">
                <p><strong>• الحقبنة (ربط الجديد بالسابق وتثبيت المفاهيم):</strong></p>
                <p style="margin-right:16px;">
                    طرح تساؤل استثاري على الطلاب: <em>"إذا كان في جيبك ٨ ريالات ولدى زميلك ٤ ريالات، فمن يملك أكثر؟ بالتأكيد $\text{٨} > \text{٤}$. ماذا لو ضاعفنا المبلغين ٣ مرات؟ تصبح $\text{٢٤} > \text{١٢}$ وتبقى المقارنة صحيحة. ماذا لو عكسنا الموقف وتكبد كل طرف خسارة قدرها ضعف ما يملك (الضرب في $-\text{٢}$)? تصبح النتيجة $-\text{١٦}$ و $-\text{٨}$. من أصبح موقفه المالي أسوأ ودينه أكبر؟ أليس $-\text{١٦} < -\text{٨}$؟ كيف انقلبت كفة المقارنة على خط الأعداد بمجرد الدخول في الاتجاه السالب؟"</em>
                </p>
                
                <p style="margin-top:12px;"><strong>• التمهيد (نشاط تفاعلي مبتكر + تقويم تشخيصي سريع):</strong></p>
                <p style="margin-right:16px;">
                    <strong>النشاط التفاعلي (ميزان الأعداد الذكي):</strong> عرض ميزان ذي كفتين رقمي على الشاشة؛ الكفة اليمنى تحمل ثقلاً مقداره ٨ كجم واليسرى ٤ كجم ($\text{٨} > \text{٤}$). نناقش مع الطلاب: ماذا يحدث إذا قسمنا كل كفة على العدد الموجب ٢؟ تظل اليمنى أثقل ($\text{٤} > \text{٢}$). متى تنقلب الكفة في الرياضيات؟ عند عكس اتجاه القوى إلى الاتجاه السالب.<br>
                    <strong>التقويم التشخيصي السريع:</strong> حل المعادلة الجبرية التالية واذكر العملية المعاكسة: $-\text{٣س} = \text{١٥}$. ما إشارة المعامل المضروب في المتغير؟
                </p>
            </div>

            <!-- تفعيل جدول KWL -->
            <p><strong>• جدول التعلم (KWL):</strong></p>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ماذا نعرف؟ (K)</th>
                        <th>ماذا نريد أن نعرف؟ (W)</th>
                        <th>ماذا تعلمنا؟ (L)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>• حل المعادلات بالضرب والقسمة.<br>• حل المتباينات بالجمع والطرح.<br>• التمثيل البياني على خط الأعداد والدوائر المغلقة والمفتوحة.</td>
                        <td>• كيف تؤثر الإشارة السالبة عند إجراء الضرب والقسمة؟<br>• متى يتعين تغيير اتجاه رمز المتباينة حتماً؟<br>• كيفية كتابة مجموعة الحل بالصفة المميزة.</td>
                        <td>• عند ضرب أو قسمة طرفي متباينة في عدد سالب نعكس اتجاه الرمز فوراً.<br>• الضرب أو القسمة في عدد موجب يبقي الرمز كما هو.<br>• الصفة المميزة: $\{ \text{س} \mid \text{س} > أ \}$.</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">٣. بيئة التعلم (٣ قواعد صفية تخدم طبيعة الأنشطة المقترحة):</h4>
            <ol style="margin: 8px 24px; line-height:1.9;">
                <li><strong>قاعدة فحص إشارة المعامل أولاً:</strong> يلتزم كل طالب في المجموعة قبل الشروع في الضرب أو القسمة بفحص إشارة المعامل بصوت مسموع (موجب = ثبات الرمز، سالب = قلب الرمز).</li>
                <li><strong>قاعدة التمثيل الفوري المتزامن:</strong> كل خطوة جبرية تنتهي برسم سريع لنقطة خط الأعداد (مغلقة/مفتوحة) واتجاه السهم للتأكد البصري من صحة مجموعة الحل.</li>
                <li><strong>قاعدة التعويض الاستكشافي للتحقق:</strong> لا يُعتمد أي حل نهائي داخل الفريق إلا بعد اختيار قيمة عددية من منطقة الحل والتعويض بها في المتباينة الأصلية.</li>
            </ol>

            <h4 style="margin-top:16px;">٤. تنفيذ الدرس (تطوير المحتوى المرفق باستراتيجيات نشطة):</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>العصف الذهني:</strong> توليد أفكار حول المشكلة الرياضية: لدينا المتباينة الصحيحة $\text{٢} < \text{٥}$. اضرب الطرفين في $-\text{٣}$. الناتج العددي هو $-\text{٦}$ و $-\text{١٥}$. ضع علامة المقارنة المناسبة! ماذا تلاحظ؟ وما القاعدة المنطقية التي يجب صياغتها لحماية صحة المتباينة رياضياً؟</li>
                <li><strong>فكر - زاوج - شارك:</strong> نشاط يعالج النقطة الدسمة للضرب في كسر سالب (مثال ٢ ص ١٣٢): حل المتباينة $-\frac{\text{٣}}{\text{٧}}\text{ر} \le \text{٢١}$. فكر بمفردك لتحديد المعكوس الضربي $(-\frac{\text{٧}}{\text{٣}})$، زاوج مع زميلك لضبط اتجاه علامة التباين، وشارك مع الصف الحل النهائي: $\text{ر} \ge -\text{٤٩}$.</li>
                <li><strong>الخرائط الذهنية (رسم شجري ملخص للمحتوى):</strong></li>
            </ul>

            <pre style="background:#f1f5f9; padding:12px; border-radius:8px; font-family:'Courier New', monospace; font-size:0.95rem; line-height:1.6; direction:rtl; text-align:right;">
                       [ حل المتباينات بالضرب أو بالقسمة ]
                                       |
             +-------------------------+-------------------------+
             |                                                   |
      [ الضرب أو القسمة في موجب (+) ]                     [ الضرب أو القسمة في سالب (-) ]
             |                                                   |
   • يبقى اتجاه الإشارة كما هو                             • يُعكس اتجاه رمز المتباينة حتماً
   • مثال: ٣س > ١٢                                       • (< تصبح >) و (≤ تصبح ≥)
     ==> س > ٤                                           • مثال: -٢س ≤ ١٠  ==>  س ≥ -٥
            </pre>

            <!-- مربع فراير للدرس 4-2 -->
            <div class="frayer-box">
                <div class="frayer-center-title">مربع فراير: عكس اتجاه رمز التباين (الضرب / القسمة في سالب)</div>
                <div class="frayer-quadrant">
                    <h4>التعريف الدقيق</h4>
                    <p>قلب اتجاه رمز المقارنة (من $<$ إلى $>$، أو من $\le$ إلى $\ge$) عند ضرب أو قسمة طرفي متباينة صحيحة في عدد سالب لحفظ توازنها وصحتها المنطقية.</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>الخصائص والسمات</h4>
                    <p>• خاص بالعمليات في الأعداد السالبة فقط.<br>• يعكس ترتيب الأعداد على خط الأعداد.<br>• لا يغير نوع الدائرة (مغلقة تبقى مغلقة ومفتوحة تبقى مفتوحة).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>أمثلة منتمية</h4>
                    <p>• $-\text{٢س} < \text{١٠} \implies \text{س} > -\text{٥}$<br>• $-\frac{\text{١}}{\text{٣}}\text{ص} \ge \text{٤} \implies \text{ص} \le -\text{١٢}$<br>• $-\text{٥} > -\text{٨} \implies \text{٥} < \text{٨}$ (ضرب في $-\text{١}$)</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة (أخطاء شائعة)</h4>
                    <p>• $\text{٣س} < -\text{١٥} \implies \text{س} > -\text{٥}$ ❌ (المقسوم عليه موجب فلا نقلب).<br>• $\text{س} - \text{٤} < \text{٧} \implies \text{س} > \text{١١}$ ❌ (الطرح والجمع لا يعكسان الرمز مطلقاً).</p>
                </div>
            </div>

            <p><strong>• الأمثلة التطبيقية المبسطة:</strong></p>
            <div style="background:#f8fafc; border-right:4px solid var(--primary); padding:12px; margin:8px 0;">
                <strong>مثال الشراء من واقع الحياة (ص ١٣٠):</strong> حصل سعود على جائزة قدرها ٢٥٠ ريالاً ويريد شراء زجاجات عطر سعر الواحدة ٤٥ ريالاً. المتباينة: $\text{٤٥ك} \le \text{٢٥٠} \implies \text{ك} \le \text{٥٫٥٥}$. بما أن زجاجات العطر أعداد صحيحة موجبة، فإن أقصى عدد يمكن شراؤه هو <strong>٥ زجاجات</strong>.
            </div>

            <h4 style="margin-top:16px;">٥. التكامل (STEM والواقع):</h4>
            <p><strong>• الربط الحياتي:</strong> التخطيط المالي والمشتريات الأسرية؛ حساب سقف الإنفاق المالي دون تجاوز الميزانية المحددة في عروض الشراء والتخفيضات.</p>
            <div class="stem-grid">
                <div class="stem-pillar s">
                    <h4>🧪 العلوم (Science)</h4>
                    <p>قوانين الضغط والطفو: تحديد الحد الأقصى لحجم الغواصة لتبقى طافية أو غاطسة بتطبيق $P \le \frac{F}{A}$.</p>
                </div>
                <div class="stem-pillar t">
                    <h4>💻 التقنية (Technology)</h4>
                    <p>برمجة شروط اتخاذ القرار: كتابة خوارزمية بايثون تقارن المتغيرات وتعكس الشرط تلقائياً عند المعامل السالب.</p>
                </div>
                <div class="stem-pillar e">
                    <h4>🏗️ الهندسة (Engineering)</h4>
                    <p>حسابات أمان الرافعات الإنشائية: أقصى حمولة مسموحة لكل ذراع وفق عزم الدوران المقاوم: $F \times d \le M_{\text{safe}}$.</p>
                </div>
                <div class="stem-pillar m">
                    <h4>📐 الرياضيات (Math)</h4>
                    <p>خصائص الضرب والقسمة، العمليات على الأعداد الصحيحة والكسور، التباين والصفة المميزة.</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">٦. منظومة التقويم (مقالي مع الحل):</h4>
            <p><strong>• تقويم بنائي (سؤال لكل هدف من الأهداف الثلاثة):</strong></p>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>سؤال الهدف ١:</strong> حل المتباينة: $-\frac{\text{٢}}{\text{٣}}\text{ص} < \text{٦}$، وتحقق من صحة الحل.<br>
                <em>الحل النموذجي:</em> نضرب الطرفين في المعكوس الضربي $(-\frac{\text{٣}}{\text{٢}})$ ونعكس إشارة المتباينة: $\text{ص} > \text{٦} \times (-\frac{\text{٣}}{\text{٢}}) \implies \text{ص} > -\text{٩}$. التحقق: بالتعويض بالصفر $-\frac{\text{٢}}{\text{٣}}(\text{٠}) = \text{٠} < \text{٦}$ (صحيحة دائماً ✔️). مجموعة الحل: $\{ \text{ص} \mid \text{ص} > -\text{٩} \}$.</li>
                <li><strong>سؤال الهدف ٢:</strong> حل المتباينة: $-\text{٦س} \ge -\text{٤٢}$.<br>
                <em>الحل النموذجي:</em> نقسم الطرفين على المعامل السالب $(-\text{٦})$ ونعكس الرمز من $\ge$ إلى $\le$: $\text{س} \le \frac{-\text{٤٢}}{-\text{٦}} \implies \text{س} \le \text{٧}$. مجموعة الحل: $\{ \text{س} \mid \text{س} \le \text{٧} \}$.</li>
                <li><strong>سؤال الهدف ٣:</strong> جمعت دار نشر أكثر من ٥٥٠٠ ريال من بيع كتاب جديد ثمن النسخة منه ١٥ ريالاً (مسألة ١ ص ١٣٣). اكتب متباينة تمثل الموقف وحلها لتجد أقل عدد نسخ تم بيعه.<br>
                <em>الحل النموذجي:</em> بفرض عدد النسخ $\text{ن}$: $\text{١٥ن} > \text{٥٥٠٠} \implies \text{ن} > \frac{\text{٥٥٠٠}}{\text{١٥}} \implies \text{ن} > \text{٣٦٦٫٦٧}$. أقل عدد كامل من النسخ تم بيعه هو <strong>٣٦٧ نسخة</strong>.</li>
            </ul>

            <p><strong>• تقويم ختامي (شامل يربط أجزاء المحتوى):</strong></p>
            <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:12px; margin:8px 0;">
                حل المتباينة $-\frac{\text{ك}}{\text{٣}} \ge -\text{٤}$ واكتب مجموعة حلها بالصفة المميزة ومثلها على خط الأعداد.<br>
                <em>الحل النموذجي:</em> نضرب الطرفين في $(-\text{٣})$ ونقلب الرمز: $\text{ك} \le (-\text{٤}) \times (-\text{٣}) \implies \text{ك} \le \text{١٢}$. مجموعة الحل: $\{ \text{ك} \mid \text{ك} \le \text{١٢} \}$. التمثيل: دائرة مغلقة عند ١٢ وسهم ممتد نحو اليسار.
            </div>

            <p><strong>• الواجب المنزلي (MCQ من ٤ خيارات رأسية وتحديد الحل والتفسير):</strong></p>
            <p>ما مجموعة حل المتباينة: $-\text{٥م} \le \text{٣٠}$؟</p>
            <div class="mcq-options-vertical">
                <div class="mcq-option-line">أ) $\{ \text{م} \mid \text{م} \le -\text{٦} \}$</div>
                <div class="mcq-option-line" style="font-weight:bold; background:#dbeafe;">ب) $\{ \text{م} \mid \text{م} \ge -\text{٦} \}$  (الإجابة الصحيحة)</div>
                <div class="mcq-option-line">ج) $\{ \text{م} \mid \text{م} \ge \text{٦} \}$</div>
                <div class="mcq-option-line">د) $\{ \text{م} \mid \text{م} \le \text{٦} \}$</div>
            </div>
            <p style="font-size:0.9rem; color:#1e40af; margin-right:16px;">
                <strong>التفسير الرياضي:</strong> عند قسمة طرفي المتباينة على العدد السالب $(-\text{٥})$، يتعين حتماً عكس اتجاه إشارة المتباينة من $(\le)$ إلى $(\ge)$، وينتج $\text{٣٠} \div (-\text{٥}) = -\text{٦}$.
            </p>

            <h4 style="margin-top:16px;">٧. الغلق والتلخيص:</h4>
            <p>• استكمال عمود (ماذا تعلمنا؟) في جدول KWL لتأكيد أن الإشارة السالبة تعكس الاتجاه والموجبة تحافظ عليه.<br>
            • <strong>سؤال التحدي الإثرائي (للدرس القادم):</strong> <em>"إذا علمت أن حل المتباينة $أ \cdot \text{س} \ge \text{٢٠}$ هو $\text{س} \le -\text{٥}$، فما قيمة المعامل $أ$؟ وهل هو موجب أم سالب ولماذا؟"</em> (الحل: $أ = -\text{٤}$ وهو سالب حتماً لقلب رمز التباين).</p>
        </article>

        <!-- الخطة 2: الدرس 4-3 -->
        <article class="unit-card page-break" id="plan-4-3">
            <div class="unit-title-box">
                <h3><span>٢️⃣</span> خطة الدرس (٤-٣): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٣٥ – ١٤٠</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار الوزاري:</strong> حل متباينات خطية متعددة الخطوات وتطبيق خاصية التوزيع وتحديد الحالات الخاصة (المجموعة الخالية $\emptyset$ ومجموعة الأعداد الحقيقية $\mathbb{R}$).</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينات خطية تتضمن أكثر من عملية جبرية باتباع ترتيب العمليات المعكوس بدقة تامة بنسبة إتقان ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يطبق الطالب خاصية التوزيع لتجميع المتغيرات في طرف والثوابت في طرف بدقة لا تقل عن ٩٠٪.</li>
                <li><strong>الهدف ٣:</strong> أن يميز الطالب الحالات الخاصة للحل، مفرقاً بين المتباينة التي حلها $\emptyset$ وتلك التي حلها $\mathbb{R}$.</li>
            </ul>

            <h4 style="margin-top:16px;">٢. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:16px; margin:10px 0;">
                <p><strong>• الحقبنة (ربط الجديد بالسابق):</strong></p>
                <p style="margin-right:16px;">
                    طرح موقف تحفيزي واقعي: <em>"مندوب مبيعات في شركة تقنية يتقاضى راتباً شهرياً ثابتاً قدره ٢٥٠٠ ريال بالإضافة إلى عمولة قدرها ٧٥ ريالاً عن كل حاسوب يبيعه. إذا كان طموحه المالي ألا يقل دخله الشهري عن ٧٠٠٠ ريال، فكيف نترجم هذا التحدي إلى متباينة جبرية تجمع بين الضرب والجمع؟ ($\text{٧٥س} + \text{٢٥٠٠} \ge \text{٧٠٠٠}$). ما العملية التي نتخلص منها أولاً: الجمع أم الضرب؟ وكيف يساعدنا درس اليوم في حلها بخطوات منظمة؟"</em>
                </p>
                
                <p style="margin-top:12px;"><strong>• التمهيد (نشاط تفاعلي + تقويم تشخيصي):</strong></p>
                <p style="margin-right:16px;">
                    <strong>النشاط التفاعلي (تفكيك العقد الجبرية):</strong> عرض لغز رياضي: فكرت في عدد، ضربته في ٤ ثم طرحت منه ٦ فكان الناتج أكبر من ١٨. كيف نعكس شريط الأحداث رياضياً للوصول للعدد؟ التخلص من الطرح أولاً بإضافة ٦ ثم القسمة على ٤.<br>
                    <strong>التقويم التشخيصي السريع:</strong> حل المعادلة الجبرية التالية: $\text{٢}(\text{س} + \text{٣}) = \text{١٤}$. ما فائدة خاصية التوزيع في فك الأقواس قبل تجميع المتغيرات؟
                </p>
            </div>

            <!-- جدول KWL -->
            <p><strong>• جدول التعلم (KWL):</strong></p>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ماذا نعرف؟ (K)</th>
                        <th>ماذا نريد أن نعرف؟ (W)</th>
                        <th>ماذا تعلمنا؟ (L)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>• حل متباينات الخطوة الواحدة (جمع/طرح/ضرب/قسمة).<br>• خاصية التوزيع في فك الأقواس.<br>• مفهوم تجميع الحدود المتشابهة.</td>
                        <td>• ما هو الترتيب الصحيح للتخلص من العمليات المتعددة في المتباينة؟<br>• كيف نتصرف إذا وُجد المتغير في كلا طرفي التباين؟<br>• متى يكون حل المتباينة فاي $\emptyset$ أو جميع الأعداد الحقيقية؟</td>
                        <td>• نتخلص من الجمع والطرح أولاً ثم الضرب والقسمة.<br>• نطرح الحد المتغير الأصغر لنقل المتغيرات لجهة واحدة.<br>• إذا انحذف المتغير: عبارة خاطئة تعني $\emptyset$، وعبارة صحيحة دائماً تعني $\mathbb{R}$.</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">٣. بيئة التعلم (٣ قواعد صفية):</h4>
            <ol style="margin: 8px 24px; line-height:1.9;">
                <li><strong>قاعدة فك الأقواس قبل كل شيء:</strong> يُمنع إجراء أي عملية نقل أو تجميع للحدود قبل فك الأقواس بالكامل عبر خاصية التوزيع.</li>
                <li><strong>قاعدة نقل المتغير الأصغر:</strong> نلزم أنفسنا بطرح الحد المتغير ذي المعامل الأصغر لتفادي الإشارات السالبة المعقدة أمام المتغير الرئيسي.</li>
                <li><strong>قاعدة التوقف عند اختفاء المتغير:</strong> إذا حُذف المتغير من الطرفين، يتوقف الطالب فوراً ويقرأ العبارة العددية المتبقية لتحديد نوع الحالة الخاصة.</li>
            </ol>

            <h4 style="margin-top:16px;">٤. تنفيذ الدرس (استراتيجيات نشطة):</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>العصف الذهني:</strong> استعراض المتباينة: $\text{٥} - \text{٢س} \ge \text{١٧}$. ما الخطأ الشائع الذي يقع فيه أغلب الطلاب؟ (اعتبار العدد ٥ مطروحاً في حين أنه مضاف وموجب، ونسيان إشارة السالب للعدد ٢).</li>
                <li><strong>فكر - زاوج - شارك:</strong> حل متباينة التوزيع من الكتاب (مثال ٤ ص ١٣٦): $\text{٣}(\text{ت} + \text{١}) - \text{٤ت} \ge -\text{٥}$. فكر في التوزيع: $\text{٣ت} + \text{٣} - \text{٤ت} \ge -\text{٥}$، زاوج لتجميع الحدود: $-\text{ت} + \text{٣} \ge -\text{٥}$، وشارك الحل: $\text{ت} \le \text{٨}$ بعد القسمة على $-\text{١}$ وقلب الرمز.</li>
                <li><strong>الخرائط الذهنية (رسم شجري):</strong></li>
            </ul>

            <pre style="background:#f1f5f9; padding:12px; border-radius:8px; font-family:'Courier New', monospace; font-size:0.95rem; line-height:1.6; direction:rtl; text-align:right;">
                       [ المتباينات متعددة الخطوات ]
                                     |
           +-------------------------+-------------------------+
           |                                                   |
    [ خوارزمية الحل المعتادة ]                                  [ الحالات الخاصة ]
           |                                                   |
 1. فك الأقواس بخاصية التوزيع                                • حذف المتغير والوصول إلى:
 2. تجميع الحدود والمتغيرات في طرف                             - عبارة مستحيلة (مثل ٥ < ٢)
 3. التخلص من الجمع والطرح                                      ==> مجموعة الحل: ∅ (الخالية)
 4. التخلص من الضرب والقسمة                                   - عبارة صحيحة دائماً (مثل ٤ ≥ ١)
                                                                ==> مجموعة الحل: ℝ (جميع الأعداد)
            </pre>

            <!-- مربع فراير للدرس 4-3 -->
            <div class="frayer-box">
                <div class="frayer-center-title">مربع فراير: المتباينة متعددة الخطوات (Multi-Step Inequality)</div>
                <div class="frayer-quadrant">
                    <h4>التعريف</h4>
                    <p>متباينة جبرية تتطلب إجراء أكثر من عملية عكسية واحدة (توزيع، جمع/طرح، ضرب/قسمة) لعزل المتغير بمفرده في أحد الطرفين.</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>الخصائص</h4>
                    <p>• تعتمد على ترتيب العمليات المعكوس.<br>• قد تحتوي أقواساً أو متغيرات في الطرفين.<br>• تحتمل الحالات الخاصة ($\emptyset$ و $\mathbb{R}$).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>أمثلة منتمية</h4>
                    <p>• $\text{٣س} + \text{٥} > \text{١٧}$<br>• $\text{٢}(\text{ص} - \text{٤}) \le \text{٦ص} + \text{١٠}$<br>• $\frac{\text{ن} - \text{١}}{\text{٣}} \ge \text{٤}$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $\text{س} - \text{٧} < \text{٣}$ (خطوة واحدة - جمع فقط).<br>• $-\text{٤ص} \ge \text{٢٠}$ (خطوة واحدة - قسمة فقط).<br>• $\text{٢س} + \text{٣} = \text{١١}$ (معادلة وليست متباينة).</p>
                </div>
            </div>

            <p><strong>• الأمثلة التطبيقية المبسطة:</strong></p>
            <div style="background:#f8fafc; border-right:4px solid var(--secondary); padding:12px; margin:8px 0;">
                <strong>مثال الحالات الخاصة (مثال ٥ ص ١٣٧):</strong><br>
                أ) $\text{٢}(\text{ص} + \text{٤}) > \text{٢ص} + \text{١٠} \implies \text{٢ص} + \text{٨} > \text{٢ص} + \text{١٠} \implies \text{٨} > \text{١٠}$ (عبارة غير صحيحة أبداً؛ الحل هو $\emptyset$).<br>
                ب) $\text{٣}(\text{م} - \text{٢}) \le \text{٣م} + \text{٥} \implies \text{٣م} - \text{٦} \le \text{٣م} + \text{٥} \implies -\text{٦} \le \text{٥}$ (عبارة صحيحة دائماً؛ الحل هو $\mathbb{R}$).
            </div>

            <h4 style="margin-top:16px;">٥. التكامل (STEM والواقع):</h4>
            <p><strong>• الربط الحياتي:</strong> مقارنة عروض اشتراكات الأندية وباقات الهواتف؛ متى تكون الباقة ذات الاشتراك الشهري الثابت أفضل من باقة الدفع حسب الاستهلاك.</p>
            <p><strong>• منهجية STEM:</strong> نمذجة نقطة التعادل الهندسي والمالي (Break-Even Point) بين تكلفة تشغيل ماكينتين في مصنع: $\text{١٥٠س} + \text{٢٠٠٠} < \text{٢٢٠س} + \text{٦٠٠} \implies \text{س} > \text{٢٠}$ ساعة عمل.</p>

            <h4 style="margin-top:16px;">٦. منظومة التقويم:</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>سؤال بنائي ١:</strong> حل المتباينة: $\frac{\text{س}}{\text{٣}} + \text{٧} \le \text{١٢} \implies \frac{\text{س}}{\text{٣}} \le \text{٥} \implies \text{س} \le \text{١٥}$. الحل: $\{ \text{س} \mid \text{س} \le \text{١٥} \}$.</li>
                <li><strong>سؤال بنائي ٢:</strong> حل المتباينة: $\text{٦}(\text{ص} - \text{٢}) > \text{٢ص} + \text{٨} \implies \text{٦ص} - \text{١٢} > \text{٢ص} + \text{٨} \implies \text{٤ص} > \text{٢٠} \implies \text{ص} > \text{٥}$.</li>
                <li><strong>سؤال بنائي ٣:</strong> حدد نوع حل المتباينة: $\text{٤س} - \text{٣}(\text{س} + \text{١}) \ge \text{س} + \text{٥} \implies -\text{٣} \ge \text{٥}$ (خاطئة) $\implies$ مجموعة الحل هي $\emptyset$.</li>
                <li><strong>تقويم ختامي:</strong> يريد سليمان شراء حاسوب ثمنه ٢١٩٥ ريالاً وبرمجيات بسعر ١٥٠ ريالاً للواحدة ومعه ٣٠٠٠ ريال. المتباينة: $\text{١٥٠ب} + \text{٢١٩٥} \le \text{٣٠٠٠} \implies \text{١٥٠ب} \le \text{٨٠٥} \implies \text{ب} \le \text{٥٫٣٦}$؛ أكبر عدد برمجيات هو <strong>٥ برمجيات</strong>.</li>
                <li><strong>واجب منزلي (MCQ):</strong> ما مجموعة حل المتباينة: $\text{٢}(\text{ك} - \text{٣}) \le \text{٢ك} + \text{٧}$؟
                    <br>أ) $\{ \text{ك} \mid \text{ك} \le \text{١٣} \}$
                    <br>ب) المجموعة الخالية $\emptyset$
                    <br><strong>ج) مجموعة جميع الأعداد الحقيقية $\mathbb{R}$  (الإجابة الصحيحة)</strong>
                    <br>د) $\{ \text{ك} \mid \text{ك} \ge -\text{٦} \}$
                    <br><em>التفسير: بفك القوس ينتج $-\text{٦} \le \text{٧}$ وهي صحيحة دائماً لجميع قيم $\text{ك}$.</em>
                </li>
            </ul>

            <h4 style="margin-top:16px;">٧. الغلق والتلخيص:</h4>
            <p>• استكمال عمود ماذا تعلمنا في KWL.<br>
            • <strong>سؤال إثرائي:</strong> إذا علمت أن محيط مثلث متطابق الأضلاع طول ضلعه $(\text{٢س} - \text{١})$ سم يقع بين ١٥ سم و ٢٧ سم، فكيف نكتب هذا الموقف في متباينة واحدة متصلة؟</p>
        </article>

        <!-- الخطة 3: اختبار منتصف الفصل 4 -->
        <article class="unit-card page-break" id="plan-mid-quiz">
            <div class="unit-title-box">
                <h3><span>٣️⃣</span> خطة تنفيذ وتقويم: اختبار منتصف الفصل الرابع</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٤١ (الدروس ٤-١ إلى ٤-٣)</span>
            </div>

            <h4>١. الأهداف والمهام التقويمية:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>التشخيص والقياس:</strong> قياس مستوى تمكن الطلاب من مهارات الدروس الثلاثة الأولى (الجمع/الطرح، الضرب/القسمة، متعددة الخطوات).</li>
                <li><strong>تحليل الأخطاء:</strong> رصد أخطاء إشارات السالب في الضرب والقسمة، وأخطاء خاصية التوزيع وتجميع الحدود.</li>
                <li><strong>المعالجة والتمايز:</strong> تصميم أنشطة علاجية فورية للطلاب المتعثرين وأنشطة إثرائية للمتفوقين.</li>
            </ul>

            <table class="data-table">
                <thead>
                    <tr>
                        <th>الدرس المرتبط</th>
                        <th>أرقام الأسئلة المقابلة في الكتاب</th>
                        <th>المهارة المستهدفة</th>
                        <th>الوزن النسبي</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>الدرس ٤-١</strong> (الجمع والطرح)</td>
                        <td>الأسئلة: ١، ٢، ٣، ٤، ٥ (مدينة الألعاب)، ٩</td>
                        <td>حل متباينات الجمع والطرح والتمثيل البياني والمسائل الواقعية</td>
                        <td>٣٠٪</td>
                    </tr>
                    <tr>
                        <td><strong>الدرس ٤-٢</strong> (الضرب والقسمة)</td>
                        <td>الأسئلة: ٦، ٧، ٨، ١٠، ١١، ١٢، ١٣، ١٤، ١٥، ١٦، ١٧</td>
                        <td>تطبيق خصائص الضرب والقسمة ومراعاة الإشارة السالبة والكسور</td>
                        <td>٤٠٪</td>
                    </tr>
                    <tr>
                        <td><strong>الدرس ٤-٣</strong> (متعددة الخطوات)</td>
                        <td>الأسئلة: ١٨، ١٩، ٢٠، ٢١، ٢٢، ٢٣</td>
                        <td>التوزيع، تجميع المتغيرات في الطرفين، والمسائل اللفظية المركبة</td>
                        <td>٣٠٪</td>
                    </tr>
                </tbody>
            </table>
        </article>

        <!-- الخطة 4: معمل الجبر / استكشاف -->
        <article class="unit-card page-break" id="plan-lab">
            <div class="unit-title-box">
                <h3><span>٤️⃣</span> خطة تدريس: معمل الجبر (استكشاف العبارات المركبة)</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٤٢</span>
            </div>

            <h4>١. الأهداف الاستكشافية:</h4>
            <ul style="margin: 8px 24px;">
                <li>أن يستكشف الطالب المفهوم المنطقي والرياضي لأداتي الربط <strong>(و)</strong> و <strong>(أو)</strong>.</li>
                <li>أن يحدد قيم صواب العبارات المركبة معللاً إجابته بدقة منطقية تامة.</li>
                <li>أن يمهد ذهنياً للانتقال إلى حل المتباينات المركبة بيانياً وجبرياً.</li>
            </ul>

            <table class="data-table">
                <thead>
                    <tr>
                        <th>أداة الربط</th>
                        <th>المعنى المنطقي والرياضي</th>
                        <th>شرط الصواب</th>
                        <th>مثال الكتاب (ص ١٤٢)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>الرابط (و)</strong></td>
                        <td>التقاطع ($\cap$)</td>
                        <td>تكون صحيحة <strong>فقط إذا كانت كلتا العبارتين صحيحتين</strong> معاً.</td>
                        <td>"للعنكبوت ٨ أرجل (ص) و للحصان ٥ أرجل (خ)" $\implies$ العبارة المركبة <strong>خاطئة</strong>.</td>
                    </tr>
                    <tr>
                        <td><strong>الرابط (أو)</strong></td>
                        <td>الاتحاد ($\cup$)</td>
                        <td>تكون صحيحة إذا كانت <strong>إحدى العبارتين على الأقل صحيحة</strong>.</td>
                        <td>"للعنكبوت ٨ أرجل (ص) أو للحصان ٥ أرجل (خ)" $\implies$ العبارة المركبة <strong>صحيحة</strong>.</td>
                    </tr>
                </tbody>
            </table>
        </article>

        <!-- الخطة 5: الدرس 4-4 -->
        <article class="unit-card page-break" id="plan-4-4">
            <div class="unit-title-box">
                <h3><span>٥️⃣</span> خطة الدرس (٤-٤): حل المتباينات المركبة</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٤٣ – ١٤٧</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار الوزاري:</strong> حل المتباينات المركبة (الوصل والفصل) وتمثيلها بيانياً على خط الأعداد ونمذجة ظواهر الواقع بها.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "و" (تقاطع) ويمثل مجموعة حلها بدقة تامة بنسبة ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "أو" (اتحاد) ويمثلها بيانياً بالأسهم المتعاكسة أو الشاملة بدقة.</li>
                <li><strong>الهدف ٣:</strong> أن يصيغ الطالب متباينة مركبة تمثل موقفاً حياتياً واقعياً (درجات الحرارة، أطوال الموجات، سرعات السير) بصورة صحيحة.</li>
            </ul>

            <h4 style="margin-top:16px;">٢. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:16px; margin:10px 0;">
                <p><strong>• الحقبنة (ربط الجديد بالسابق):</strong></p>
                <p style="margin-right:16px;">
                    طرح تساؤل علمي يربط الفيزياء بالرياضيات: <em>"درجة حرارة الماء السائل عند الضغط الجوي المعتاد يجب أن تكون أكبر من الصفر المئوي وفي الوقت نفسه أقل من ١٠٠ درجة مئوية ($\text{٠} < \text{د} < \text{١٠٠}$). إذا تجمد الماء أو تبخر، فإنه يخرج عن حالته السائلة ($\text{د} \le \text{٠} \text{ أو } \text{د} \ge \text{١٠٠}$). ما الفرق اللغوي والمنطقي بين كلمة 'و' التي ألزمت الشرطين معاً، وكلمة 'أو' التي فتحت المجال لإحدى الحالتين؟ وكيف نترجم هذا الفرق إلى فترات وأسهم على خط الأعداد؟"</em>
                </p>
                
                <p style="margin-top:12px;"><strong>• التمهيد (نشاط تفاعلي + تقويم تشخيصي):</strong></p>
                <p style="margin-right:16px;">
                    <strong>النشاط التفاعلي (بوابات العبور المنطقية):</strong> نمذجة دارة كهربائية على التوالي (المصباح لا يضيء إلا إذا أُغلق المفتاح الأول <strong>و</strong> المفتاح الثاني معاً - تقاطع)، مقابل دارة على التوازي (المصباح يضيء إذا أُغلق المفتاح الأول <strong>أو</strong> الثاني - اتحاد).<br>
                    <strong>التقويم التشخيصي السريع:</strong> مثل بيانياً المتباينتين البسيطتين التاليتين: $\text{س} > \text{٢}$ و $\text{س} \le \text{٦}$. أين تلتقي المنطقتان؟
                </p>
            </div>

            <!-- جدول KWL -->
            <p><strong>• جدول التعلم (KWL):</strong></p>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>ماذا نعرف؟ (K)</th>
                        <th>ماذا نريد أن نعرف؟ (W)</th>
                        <th>ماذا تعلمنا؟ (L)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>• حل المتباينات البسيطة وتمثيلها.<br>• مفهوم التقاطع والاتحاد بين المجموعات.<br>• التمييز بين النقاط المفتوحة والمغلقة.</td>
                        <td>• ما هي المتباينة المركبة؟ وكيف تُكتب بصيغة متصلة؟<br>• ما الفرق في التمثيل البياني بين متباينة "و" ومتباينة "أو"؟<br>• كيف نتصرف إذا لم تتقاطع مناطق الحل في متباينة الوصل؟</td>
                        <td>• متباينة "و" تمثل منطقة التداخل المشتركة ($\cap$)، وإذا انعدم التداخل فالحل هو $\emptyset$.<br>• متباينة "أو" تمثل دمج المنطقتين ($\cup$).<br>• مصطلحات الواقع: "على الأقل" $\ge$، "على الأكثر" $\le$، "يقع بين" $< <$.</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">٣. بيئة التعلم (٣ قواعد صفية):</h4>
            <ol style="margin: 8px 24px; line-height:1.9;">
                <li><strong>قاعدة التلوين الثنائي:</strong> نلزم أنفسنا بتمثيل المتباينة الأولى بلون، والثانية بلون آخر، وتحديد منطقة الحل المشتركة بلون ثالث واضح.</li>
                <li><strong>قاعدة دقة الدوائر:</strong> وجود علامة المساواة ($\le, \ge$) يستوجب دائرة مظللة ممتلئة ●، وغيابها ($<, >$) يستوجب حلقة مفرغة مفتوحة ○.</li>
                <li><strong>قاعدة الأطراف الثلاثة:</strong> ما يتم إجراؤه على الطرف الأوسط للتخلص من الثوابت يجب إجراؤه بالتزامن على الطرفين الأيمن والأيسر.</li>
            </ol>

            <h4 style="margin-top:16px;">٤. تنفيذ الدرس:</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>العصف الذهني:</strong> حللنا متباينة بالرابط "و" فكان الناتج: $\text{س} < \text{٢} \text{ و } \text{س} > \text{٧}$. ما مجموعة الحل؟ هل يمكن لعدد في الوجود أن يكون أصغر من ٢ وأكبر من ٧ في نفس اللحظة؟ وماذا نسمي هذه المجموعة رياضياً؟ (المجموعة الخالية $\emptyset$).</li>
                <li><strong>فكر - زاوج - شارك:</strong> حل متباينة الوصل ثلاثية الأطراف (مثال ١ ص ١٤٣): $-\text{٢} \le \text{س} - \text{٣} < \text{٤}$. فكر في التخلص من $-\text{٣}$، زاوج لإضافة $+\text{٣}$ للأطراف الثلاثة: $\text{١} \le \text{س} < \text{٧}$، وشارك تمثيلها البياني المغلق عند ١ والمفتوح عند ٧.</li>
                <li><strong>الخرائط الذهنية:</strong></li>
            </ul>

            <pre style="background:#f1f5f9; padding:12px; border-radius:8px; font-family:'Courier New', monospace; font-size:0.95rem; line-height:1.6; direction:rtl; text-align:right;">
                       [ المتباينات المركبة ]
                                  |
         +------------------------+------------------------+
         |                                                 |
  [ متباينة الوصل ( و ) ]                           [ متباينة الفصل ( أو ) ]
         |                                                 |
• تعني التقاطع (∩)                                  • تعني الاتحاد (∪)
• يجب تحقق الشرطين معاً                              • يكفي تحقق أحدهما على الأقل
• تكتب غالباً متصلة: أ ≤ س ≤ ب                      • تكتب منفصلة: س < أ أو س > ب
• بيانيا: منطقة التداخل المحصورة                     • بيانيا: شعاعان في اتجاهين متعاكسين
• إذا لم تتقاطع = ∅                                  • إذا تغطى الخط كاملاً = ℝ
            </pre>

            <!-- مربع فراير للدرس 4-4 -->
            <div class="frayer-box">
                <div class="frayer-center-title">مربع فراير: المتباينة المركبة (Compound Inequality)</div>
                <div class="frayer-quadrant">
                    <h4>التعريف</h4>
                    <p>عبارة رياضية مكونة من متباينتين بسيطتين مربوطتين إما بحرف العطف "و" (تقاطع الشروط) أو بحرف العطف "أو" (اتحاد الشروط).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>الخصائص</h4>
                    <p>• متباينة "و" تمثل منطقة التداخل المشتركة.<br>• متباينة "أو" تمثل دمج المنطقتين.<br>• تكتب "و" في صورة متصلة ثلاثية الأطراف ($أ < \text{س} < ب$).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>أمثلة منتمية</h4>
                    <p>• $-\text{٢} \le \text{س} + \text{١} < \text{٥}$<br>• $\text{ص} < -\text{٣} \text{ أو } \text{ص} \ge \text{٢}$<br>• $\text{١٨} \le \text{الحرارة} \le \text{٢٤}$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $\text{٣س} + \text{٤} > \text{١٠}$ (متباينة بسيطة).<br>• $\text{س} = \text{٢} \text{ أو } \text{س} = -\text{١}$ (معادلة وليست متباينة).<br>• $\text{س} < \text{٥}$ (أحادية الشرط).</p>
                </div>
            </div>

            <p><strong>• الأمثلة التطبيقية المبسطة:</strong></p>
            <div style="background:#f8fafc; border-right:4px solid var(--accent); padding:12px; margin:8px 0;">
                <strong>حل متباينة الاتحاد بالرابط "أو" (مثال ٣ ص ١٤٥):</strong><br>
                $-\text{٢م} + \text{٧} \le \text{١٣} \implies -\text{٢م} \le \text{٦} \implies \text{م} \ge -\text{٣}$ (عكسنا الإشارة للقسمة على سالب).<br>
                أو $\text{٥م} + \text{١٢} < \text{٣٧} \implies \text{٥م} < \text{٢٥} \implies \text{م} < \text{٥}$.<br>
                نلاحظ بيانيا: الشعاع الأول يتجه يميناً من $-\text{٣}$ مغلقة، والشعاع الثاني يتجه يساراً من $\text{٥}$ مفتوحة؛ يتداخلان ليغطيا <strong>خط الأعداد كاملاً دون انقطاع</strong>، إذن مجموعة الحل هي $\mathbb{R}$.
            </div>

            <h4 style="margin-top:16px;">٥. التكامل (STEM والواقع):</h4>
            <p><strong>• الربط الحياتي:</strong> قواعد السلامة المرورية والسرعات النظامية على الطرق السريعة بالمملكة: $\text{٨٠} \le \text{ع} \le \text{١٢٠}$ كم/ساعة.</p>
            <p><strong>• منهجية STEM:</strong> هندسة أنظمة التحكم والتحسس الذكي (IoT) في غرف الخوادم ومراكز البيانات؛ ضبط التكييف في النطاق الاقتصادي بالرابط "و": $\text{١٨}^\circ\text{C} \le \text{Temp} \le \text{٢٢}^\circ\text{C}$، وإطلاق الإنذار التلقائي بالرابط "أو": $\text{Temp} < \text{١٠}^\circ\text{C} \text{ أو } \text{Temp} > \text{٣٢}^\circ\text{C}$.</p>

            <h4 style="margin-top:16px;">٦. منظومة التقويم:</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>سؤال بنائي ١:</strong> حل المتباينة: $-\text{٤} < \text{٢س} + \text{٢} \le \text{١٠} \implies -\text{٦} < \text{٢س} \le \text{٨} \implies -\text{٣} < \text{س} \le \text{٤}$. الحل: $\{ \text{س} \mid -\text{٣} < \text{س} \le \text{٤} \}$.</li>
                <li><strong>سؤال بنائي ٢:</strong> حل المتباينة: $\text{س} + \text{٣} < \text{١} \text{ أو } \text{س} - \text{٢} \ge \text{٣} \implies \text{س} < -\text{٢} \text{ أو } \text{س} \ge \text{٥}$.</li>
                <li><strong>سؤال بنائي ٣:</strong> عبر عن الجملة: حرارة الجو لا تقل عن ٢٢ ولا تزيد على ٣٥ درجة: $\text{٢٢} \le \text{د} \le \text{٣٥}$.</li>
                <li><strong>تقويم ختامي:</strong> ناتج جمع ثلاثة أمثال عدد مع أربعة يقع بين $-\text{٨}$ و $\text{١٠}$ (سؤال ٢٣ ص ١٤٧): $-\text{٨} < \text{٣ن} + \text{٤} < \text{١٠} \implies -\text{١٢} < \text{٣ن} < \text{٦} \implies -\text{٤} < \text{ن} < \text{٢}$. الحل: $\{ \text{ن} \mid -\text{٤} < \text{ن} < \text{٢} \}$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> ما التمثيل البياني الذي يعبر عن حل المتباينة: $\text{س} \le -\text{١} \text{ أو } \text{س} > \text{٣}$؟
                    <br>أ) تظليل المنطقة المحصورة بين $-\text{١}$ و $\text{٣}$.
                    <br><strong>ب) سهم متجه لليسار من $-\text{١}$ (دائرة مغلقة) وسهم متجه لليمين من $\text{٣}$ (دائرة مفتوحة).  (الإجابة الصحيحة)</strong>
                    <br>ج) سهم متجه لليمين من $-\text{١}$ وسهم متجه لليسار من $\text{٣}$.
                    <br>د) خط الأعداد مظلل بالكامل دون أي فجوة.
                </li>
            </ul>

            <h4 style="margin-top:16px;">٧. الغلق والتلخيص:</h4>
            <p>• استكمال عمود ماذا تعلمنا في KWL.<br>
            • <strong>سؤال إثرائي:</strong> كيف نربط مفهوم المتباينة المركبة بالرابط "و" بمفهوم متباينات القيمة المطلقة $|\text{س}| < أ$ في الدرس القادم؟</p>
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية) -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">المدارس المتقدمة للتعلم الذكي بجدة | إعداد: أ. محمد عبدالله جمعة</span>
        </div>

        <!-- ملخص الدرس 4-2 -->
        <article class="unit-card" id="summary-4-2">
            {header_html}
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (٤-٢): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب ص ١٣٠ - ١٣٤</span>
            </div>

            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4 style="color:#166534; margin-bottom:8px;">١. الضرب أو القسمة في عدد موجب (+)</h4>
                    <p><strong>يبقى اتجاه إشارة المتباينة كما هو دون أي تغيير:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ > ٠$ فإن $أ \times جـ > ب \times جـ$</p>
                    <p>• مثال: $\frac{\text{س}}{\text{٣}} < \text{٥} \implies \text{س} < \text{١٥}$</p>
                </div>
                <div class="rule-subcard negative">
                    <h4 style="color:#991b1b; margin-bottom:8px;">٢. الضرب أو القسمة في عدد سالب (-)</h4>
                    <p><strong>يجب عكس اتجاه إشارة المتباينة فوراً:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ < ٠$ فإن $أ \times جـ < ب \times جـ$</p>
                    <p>• مثال: $-\text{٢ص} \ge \text{٨} \implies \text{ص} \le -\text{٤}$</p>
                </div>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>تنبيه الاختبارات الحاسم:</strong> إشارة المتباينة تُعكس <u>فقط إذا كان المعامل المقسوم عليه أو المضروب فيه سالباً</u>، ولا نلتفت لإشارة الطرف الآخر! مثال: $\text{٣س} \le -\text{١٢} \implies \text{س} \le -\text{٤}$ (لم نقلب لأن المعامل ٣ موجب).
            </div>

            <h4 style="margin-top:16px;">أمثلة الكتاب المحلولة خطوة بخطوة:</h4>
            <div style="background:#f8fafc; padding:16px; border-radius:8px; margin:10px 0; border-right:4px solid var(--primary);">
                <strong>مثال ١:</strong> حل المتباينة $-\frac{\text{٣}}{\text{٧}}\text{ر} < \text{٢١}$
                <br>• نضرب الطرفين في المعكوس الضربي $(-\frac{\text{٧}}{\text{٣}})$ ونعكس إشارة $<$ إلى $>$:
                $$\text{ر} > \text{٢١} \times \left(-\frac{\text{٧}}{\text{٣}}\right) \implies \text{ر} > -\text{٤٩}$$
                • مجموعة الحل: $\{ \text{ر} \mid \text{ر} > -\text{٤٩} \}$ (دائرة مفتوحة عند $-\text{٤٩}$ وسهم لليمين).
            </div>

            {footer_sig_html}
        </article>

        <!-- ملخص الدرس 4-3 -->
        <article class="unit-card page-break" id="summary-4-3">
            {header_html}
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (٤-٣): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">كتاب الطالب ص ١٣٥ - ١٤٠</span>
            </div>

            <h4>خوارزمية الحل في ٤ خطوات ذهبية:</h4>
            <ol style="margin: 8px 24px; line-height:2;">
                <li><strong>فك الأقواس:</strong> استعمال خاصية التوزيع للتخلص من أي أقواس: $أ(ب + جـ) = أب + أجـ$.</li>
                <li><strong>تجميع المتغيرات:</strong> طرح أو جمع الحد المتغير الأصغر لنقل كل المتغيرات إلى جهة واحدة.</li>
                <li><strong>التخلص من الجمع والطرح:</strong> نقل الثوابت إلى الطرف الآخر بعكس إشارتها.</li>
                <li><strong>التخلص من الضرب والقسمة:</strong> القسمة على المعامل مع تذكر قلب الإشارة إذا كان سالباً.</li>
            </ol>

            <h4 style="margin-top:16px;">الحالات الخاصة (عندما يختفي المتغير تماماً):</h4>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>الحالة</th>
                        <th>النتيجة العددية</th>
                        <th>مجموعة الحل</th>
                        <th>التمثيل البياني</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>المجموعة الخالية ( ∅ )</strong></td>
                        <td>عبارة خاطئة وغير ممكنة (مثل $\text{٥} < \text{٢}$)</td>
                        <td>$\emptyset$ (فاي)</td>
                        <td>خط أعداد فارغ تماماً دون أي تظليل</td>
                    </tr>
                    <tr>
                        <td><strong>جميع الأعداد الحقيقية ( ℝ )</strong></td>
                        <td>عبارة صائبة دائماً (متطابقة مثل $\text{٣} \le \text{٧}$)</td>
                        <td>$\{ \text{س} \mid \text{س} \in \mathbb{R} \}$</td>
                        <td>خط الأعداد مظلل بالكامل بسهمين ممتدين</td>
                    </tr>
                </tbody>
            </table>

            {footer_sig_html}
        </article>

        <!-- ملخص مراجعة اختبار منتصف الفصل 4 ومعمل الجبر -->
        <article class="unit-card page-break" id="summary-mid-quiz">
            {header_html}
            <div class="unit-title-box">
                <h3><span>📖</span> مراجعة مركزة: اختبار منتصف الفصل ومعمل الجبر</h3>
                <span class="page-range-pill">كتاب الطالب ص ١٤١ – ١٤٢</span>
            </div>
            <h4>المفاهيم المحورية لاختبار منتصف الفصل (ص ١٤١):</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>متباينات الجمع والطرح:</strong> $\text{س} - \text{٥} > \text{٣} \implies \text{س} > \text{٨}$.</li>
                <li><strong>متباينات الضرب والقسمة:</strong> المعامل السالب يقلب علامة التباين دائماً: $-\frac{\text{٢}}{\text{٣}}\text{س} < \text{٨} \implies \text{س} > -\text{١٢}$.</li>
                <li><strong>المسائل اللفظية:</strong> "أكثر من" تعني $>$، "أقل من" تعني $<$، "لا يزيد على" تعني $\le$، و"لا يقل عن" تعني $\ge$.</li>
            </ul>

            <h4 style="margin-top:16px;">قواعد معمل الجبر: قراءة العبارات المركبة (ص ١٤٢):</h4>
            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4>أداة الربط "و" (التقاطع ∩)</h4>
                    <p>• تكون <strong>صحيحة فقط</strong> إذا كانت كلتا العبارتين صحيحتين.</p>
                    <p>• مثال: $\text{٥} > \text{٣} \text{ و } \text{٢} < \text{٧}$ $\implies$ <strong>صحيحة</strong>.</p>
                </div>
                <div class="rule-subcard" style="background:#eff6ff; border-color:#3b82f6;">
                    <h4 style="color:#1d4ed8;">أداة الربط "أو" (الاتحاد ∪)</h4>
                    <p>• تكون <strong>صحيحة</strong> إذا كانت إحدى العبارتين على الأقل صحيحة.</p>
                    <p>• مثال: $\text{٥} > \text{٣} \text{ أو } \text{٨} < \text{٢}$ $\implies$ <strong>صحيحة</strong>.</p>
                </div>
            </div>

            {footer_sig_html}
        </article>

        <!-- ملخص الدرس 4-4 -->
        <article class="unit-card page-break" id="summary-4-4">
            {header_html}
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (٤-٤): حل المتباينات المركبة</h3>
                <span class="page-range-pill">كتاب الطالب ص ١٤٣ – ١٤٧</span>
            </div>

            <table class="data-table">
                <thead>
                    <tr>
                        <th>وجه المقارنة</th>
                        <th>متباينة الوصل (الرابط "و")</th>
                        <th>متباينة الفصل (الرابط "أو")</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>الرمز والمعنى</strong></td>
                        <td>تقاطع ($\cap$) - اشتراك الحلين</td>
                        <td>اتحاد ($\cup$) - دمج الحلين</td>
                    </tr>
                    <tr>
                        <td><strong>الصيغة الجبرية</strong></td>
                        <td>غالباً جملة متصلة: $-\text{٣} \le \text{س} < \text{٥}$</td>
                        <td>جملتان منفصلتان بكلمة "أو": $\text{س} < \text{١} \text{ أو } \text{س} \ge \text{٤}$</td>
                    </tr>
                    <tr>
                        <td><strong>التمثيل البياني</strong></td>
                        <td>المنطقة المحصورة بين النقطتين (تداخل)</td>
                        <td>شعاعان ينطلقان في اتجاهين متعاكسين</td>
                    </tr>
                    <tr>
                        <td><strong>الحالات الشائعة</strong></td>
                        <td>إذا لم تتقاطع المنطقتان فالحل هو $\emptyset$</td>
                        <td>إذا تداخل الشعاعان وغطيا الخط فالحل هو $\mathbb{R}$</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">التمثيل البياني البصري:</h4>
            <div style="text-align:center; background:#f8fafc; padding:16px; border-radius:8px; border:1px solid var(--gray-200);">
                <p><strong>تمثيل متباينة الوصل ( $-\text{٢} \le \text{س} < \text{٤}$ ):</strong> مغلقة عند $-\text{٢}$ ومفتوحة عند $\text{٤}$ والتظليل بينهما:</p>
                <svg class="nl-svg-container" viewBox="0 0 400 45">
                    <line x1="20" y1="20" x2="380" y2="20" stroke="#94a3b8" stroke-width="3" />
                    <line x1="120" y1="20" x2="280" y2="20" stroke="#0d9488" stroke-width="6" />
                    <circle cx="120" cy="20" r="6" fill="#0d9488" stroke="#042f2e" stroke-width="2" />
                    <text x="120" y="40" font-size="12" text-anchor="middle" font-weight="bold">-٢</text>
                    <circle cx="280" cy="20" r="6" fill="#ffffff" stroke="#0d9488" stroke-width="2" />
                    <text x="280" y="40" font-size="12" text-anchor="middle" font-weight="bold">٤</text>
                </svg>

                <p style="margin-top:12px;"><strong>تمثيل متباينة الفصل ( $\text{س} \le -\text{١} \text{ أو } \text{س} > \text{٣}$ ):</strong> سهمان متعاكسان:</p>
                <svg class="nl-svg-container" viewBox="0 0 400 45">
                    <line x1="20" y1="20" x2="380" y2="20" stroke="#94a3b8" stroke-width="3" />
                    <line x1="120" y1="20" x2="30" y2="20" stroke="#2563eb" stroke-width="6" />
                    <circle cx="120" cy="20" r="6" fill="#2563eb" stroke="#1e3a8a" stroke-width="2" />
                    <text x="120" y="40" font-size="12" text-anchor="middle" font-weight="bold">-١</text>
                    <line x1="280" y1="20" x2="370" y2="20" stroke="#2563eb" stroke-width="6" />
                    <circle cx="280" cy="20" r="6" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
                    <text x="280" y="40" font-size="12" text-anchor="middle" font-weight="bold">٣</text>
                </svg>
            </div>

            {footer_sig_html}
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية مع أزرار إظهار الحل -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section page-break">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية (متتالية)</h2>
            <span class="section-badge">المدارس المتقدمة للتعلم الذكي بجدة | إعداد: أ. محمد عبدالله جمعة</span>
        </div>

        <!-- ورقة عمل الدرس 4-2 -->
        <article class="worksheet-paper" id="ws-4-2">
            {header_html}
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (٤-٢) حل المتباينات بالضرب أو بالقسمة</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة من بين الخيارات التالية: [٤ درجات]</div>
                
                <p><strong>١) حل المتباينة الجبرية: $\text{٣س} < -\text{٢١}$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{س} < -\text{٧}$</div>
                    <div class="mcq-option-line">ب) $\text{س} > -\text{٧}$</div>
                    <div class="mcq-option-line">ج) $\text{س} < \text{٧}$</div>
                    <div class="mcq-option-line">د) $\text{س} > \text{٧}$</div>
                </div>

                <p><strong>٢) ما مجموعة حل المتباينة: $-\frac{\text{ص}}{\text{٢}} \ge \text{٤}$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ \text{ص} \mid \text{ص} \le -\text{٨} \}$</div>
                    <div class="mcq-option-line">ب) $\{ \text{ص} \mid \text{ص} \ge -\text{٨} \}$</div>
                    <div class="mcq-option-line">ج) $\{ \text{ص} \mid \text{ص} \le \text{٨} \}$</div>
                    <div class="mcq-option-line">د) $\{ \text{ص} \mid \text{ص} \ge \text{٨} \}$</div>
                </div>

                <p><strong>٣) عند قسمة طرفي متباينة صحيحة على عدد حقيقي سالب فإن إشارة المتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) تبقى كما هي دون تغيير</div>
                    <div class="mcq-option-line">ب) تتحول إلى إشارة مساواة</div>
                    <div class="mcq-option-line">ج) يتعين تغيير اتجاهها فوراً</div>
                    <div class="mcq-option-line">د) تصبح القيمة مساوية للصفر</div>
                </div>

                <p><strong>٤) وفر راشد أكثر من ٣٠٠ ريال لشراء كتب سعر الكتاب الواحد ٢٥ ريالاً. المتباينة التي تمثل عدد الكتب ($\text{ك}$) هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{٢٥ك} < \text{٣٠٠}$</div>
                    <div class="mcq-option-line">ب) $\text{٢٥ك} > \text{٣٠٠}$</div>
                    <div class="mcq-option-line">ج) $\text{ك} + \text{٢٥} \ge \text{٣٠٠}$</div>
                    <div class="mcq-option-line">د) $\frac{\text{ك}}{\text{٢٥}} \le \text{٣٠٠}$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع إشارة (✓) أمام العبارة الصحيحة وإشارة (✗) أمام العبارة الخاطئة: [٣ درجات]</div>
                <p>١. ( &nbsp;&nbsp;&nbsp; ) حل المتباينة $-\text{٥س} \ge \text{٣٥}$ هو $\text{س} \ge -\text{٧}$.</p>
                <p>٢. ( &nbsp;&nbsp;&nbsp; ) التمثيل البياني لـ $\text{س} \le \text{٦}$ يتم برسم دائرة مغلقة وسهم متجه لليسار.</p>
                <p>٣. ( &nbsp;&nbsp;&nbsp; ) ضرب طرفي المتباينة في الكسر الموجب $\frac{\text{١}}{\text{٣}}$ يقتضي عكس اتجاه المتباينة.</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية، ومثل مجموعة الحل بيانياً على خط الأعداد: [٣ درجات]</div>
                <p style="text-align:center; font-size:1.25rem; font-weight:bold; margin:10px 0;">$-\frac{\text{٤}}{\text{٥}}\text{م} \le \text{٢٠}$</p>
                <p>خطوات الحل الجبري: ............................................................................................................</p>
                <p>مجموعة الحل بالصفة المميزة: .................................................................................................</p>
                <p>التمثيل البياني: <br>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <!-- Dedicated Solution Toggle Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-2', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (٤-٢)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-2" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي وتوزيع الدرجات (ورقة عمل ٤-٢):</h4>
                <p><strong>السؤال الأول (٤ درجات):</strong> ١) أ ($\text{س} < -\text{٧}$) | ٢) أ ($\{ \text{ص} \mid \text{ص} \le -\text{٨} \}$) | ٣) ج (يتعين تغيير اتجاهها) | ٤) ب ($\text{٢٥ك} > \text{٣٠٠}$). [درجة لكل فقرة]</p>
                <p><strong>السؤال الثاني (٣ درجات):</strong> ١) ( ✗ ) الصواب $\text{س} \le -\text{٧}$ لعكس الإشارة عند القسمة على $-\text{٥}$. | ٢) ( ✓ ). | ٣) ( ✗ ) الضرب في موجب لا يعكس الإشارة. [درجة لكل فقرة]</p>
                <p><strong>السؤال الثالث (٣ درجات):</strong> نضرب في المعكوس الضربي $(-\frac{\text{٥}}{\text{٤}})$ ونعكس الرمز: $\text{م} \ge \text{٢٠} \times (-\frac{\text{٥}}{\text{٤}}) \implies \text{م} \ge -\text{٢٥}$ [درجتان]. مجموعة الحل: $\{ \text{م} \mid \text{م} \ge -\text{٢٥} \}$. التمثيل: دائرة مغلقة عند $-\text{٢٥}$ وسهم مظلل لليمين [درجة].</p>
            </div>

            {footer_sig_html}
        </article>

        <!-- ورقة عمل الدرس 4-3 -->
        <article class="worksheet-paper page-break" id="ws-4-3">
            {header_html}
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (٤-٣) حل المتباينات متعددة الخطوات</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [٤ درجات]</div>
                <p><strong>١) أول خطوة صحيحة للبدء في حل المتباينة $\text{٤س} - \text{٥} > \text{١٩}$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) القسمة على ٤</div>
                    <div class="mcq-option-line">ب) إضافة ٥ للطرفين</div>
                    <div class="mcq-option-line">ج) طرح ٥ من الطرفين</div>
                    <div class="mcq-option-line">د) ضرب الطرفين في ٤</div>
                </div>

                <p><strong>٢) حل المتباينة: $-\text{٣س} + \text{٧} \le \text{٢٢}$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{س} \le -\text{٥}$</div>
                    <div class="mcq-option-line">ب) $\text{س} \ge -\text{٥}$</div>
                    <div class="mcq-option-line">ج) $\text{س} \ge \text{٥}$</div>
                    <div class="mcq-option-line">د) $\text{س} \le \text{٥}$</div>
                </div>

                <p><strong>٣) ما مجموعة حل المتباينة: $\text{٢}(\text{س} + \text{٣}) > \text{٢س} + \text{١١}$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $\text{س} > \text{٥}$</div>
                    <div class="mcq-option-line">د) $\text{س} < \text{٨}$</div>
                </div>

                <p><strong>٤) حل المتباينة: $\text{٥}(\text{ص} - \text{١}) \le \text{٥ص} + \text{٢}$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) مجموعة الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $\text{ص} \ge ٠$</div>
                    <div class="mcq-option-line">د) $\text{ص} \le -\text{٣}$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: اكتب نوع مجموعة الحل (قيمة محددة / $\emptyset$ / $\mathbb{R}$): [٣ درجات]</div>
                <p>١. المتباينة: $\text{٣}(\text{س} - \text{٢}) \ge \text{٣س} + \text{٥}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>٢. المتباينة: $\text{٤}(\text{ن} + \text{٢}) > \text{٤ن} - \text{٣}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>٣. المتباينة: $\text{٢هـ} + \text{٩} < \text{١٥}$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية موضحاً خطوات التوزيع والتبسيط: [٣ درجات]</div>
                <p style="text-align:center; font-size:1.25rem; font-weight:bold; margin:10px 0;">$\text{٣}(\text{ت} + \text{٢}) - \text{٥ت} \ge -\text{٦}$</p>
                <p>خطوة ١ (خاصية التوزيع): .....................................................................................................</p>
                <p>خطوة ٢ (تجميع الحدود وعزل المتغير): ......................................................................................</p>
                <p>مجموعة الحل النهائية: ............................................................................................................</p>
            </div>

            <!-- Dedicated Solution Toggle Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-3', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (٤-٣)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-3" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي وتوزيع الدرجات (ورقة عمل ٤-٣):</h4>
                <p><strong>السؤال الأول (٤ درجات):</strong> ١) ب (إضافة ٥) | ٢) ب ($\text{س} \ge -\text{٥}$ لأن $-\text{٣س} \le \text{١٥}$) | ٣) ب ($\emptyset$ لأن $\text{٦} > \text{١١}$ مستحيلة) | ٤) أ ($\mathbb{R}$ لأن $-\text{٥} \le \text{٢}$ صحيحة دائماً).</p>
                <p><strong>السؤال الثاني (٣ درجات):</strong> ١. $\emptyset$ (لأن $-\text{٦} \ge \text{٥}$ خاطئة) | ٢. $\mathbb{R}$ (لأن $\text{٨} > -\text{٣}$ صائبة دائماً) | ٣. قيمة محددة ($\text{هـ} < \text{٣}$).</p>
                <p><strong>السؤال الثالث (٣ درجات):</strong> $\text{٣ت} + \text{٦} - \text{٥ت} \ge -\text{٦} \implies -\text{٢ت} + \text{٦} \ge -\text{٦} \implies -\text{٢ت} \ge -\text{١٢} \implies \text{ت} \le \text{٦}$ (قلبنا الإشارة بالقسمة على $-\text{٢}$). الحل: $\{ \text{ت} \mid \text{ت} \le \text{٦} \}$.</p>
            </div>

            {footer_sig_html}
        </article>

        <!-- اختبار منتصف الفصل 4 (ص 141) -->
        <article class="worksheet-paper page-break" id="ws-mid-quiz">
            {header_html}
            <div class="ws-meta-bar">
                <span>اختبار منتصف الفصل الرابع (الدروس ٤-١ إلى ٤-٣) - ص ١٤١</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الزمن: ٣٥ دقيقة</span>
                <span>الدرجة الكلية: [ &nbsp;&nbsp;&nbsp; / ١٥ ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء ١: متباينات الجمع والطرح (حل ومثل بيانياً على خط الأعداد): [٣ درجات]</div>
                <p><strong>١) $\text{س} - \text{٨} < \text{٤}$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>٢) $\text{م} + \text{٢} \ge \text{٦}$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>٣) مدينة الألعاب (سؤال ٥ ص ١٤١):</strong> مع حمزة ٦٠ ريالاً، دفع منها ١٠ ريالات تذكرة دخول. اكتب متباينة تبين المبلغ ($\text{س}$) الذي يمكن لحمزة إنفاقه داخل المدينة ثم حلها.<br>
                المتباينة والحل: ................................................................................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء ٢: متباينات الضرب والقسمة (حل وتحقق من صحة الحل): [٤ درجات]</div>
                <p><strong>٤) $\frac{\text{١}}{\text{٣}}\text{ص} \le \text{٥}$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>٥) $-\text{٨س} < \text{٢٤}$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>٦) $-\text{٩ر} \le -\text{٤٥}$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>٧) $\frac{\text{و}}{\text{٦}} > -\text{٣}$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء ٣: متباينات متعددة الخطوات وتطبيقاتها: [٥ درجات]</div>
                <p><strong>٨) $\text{٤أ} - \text{٢} < \text{١٤}$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>٩) $\text{٢س} + \text{١١} \le \text{٥س} - \text{١٠}$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>١٠) $-\text{٢}(\text{٤ب} + \text{١}) < -\text{٣ب} + \text{٨}$</strong><br>
                الحل بالتفصيل: .................................................................................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء ٤: اختيار من متعدد (سؤال ٩ ص ١٤١): [٣ درجات]</div>
                <p><strong>١١) وفرت عزيزة ٥٢ ريالاً لشراء كتاب يزيد ثمنه على ٩٠ ريالاً. ما المبلغ الإضافي الذي يجب أن توفره عزيزة؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) ٣٨ ريالاً</div>
                    <div class="mcq-option-line">ب) أكثر من ٣٨ ريالاً</div>
                    <div class="mcq-option-line">ج) ليس أكثر من ٣٨ ريالاً</div>
                    <div class="mcq-option-line">د) ٣٨ ريالاً على الأكثر</div>
                </div>
            </div>

            <!-- Dedicated Solution Toggle Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-mid', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لاختبار منتصف الفصل (ص ١٤١)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-mid" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 نموذج الإجابة وتوزيع الدرجات المعتمد لاختبار منتصف الفصل:</h4>
                <p>١) $\text{س} < \text{١٢}$ [درجة]. | ٢) $\text{م} \ge \text{٤}$ [درجة]. | ٣) $\text{س} + \text{١٠} \le \text{٦٠} \implies \text{س} \le \text{٥٠}$ ريالاً [درجة].</p>
                <p>٤) $\text{ص} \le \text{١٥}$ [درجة]. | ٥) $\text{س} > -\text{٣}$ لعكس الرمز بالقسمة على سالب [درجة]. | ٦) $\text{ر} \ge \text{٥}$ لعكس الرمز [درجة]. | ٧) $\text{و} > -\text{١٨}$ [درجة].</p>
                <p>٨) $\text{٤أ} < \text{١٦} \implies \text{أ} < \text{٤}$ [١٫٥ درجة]. | ٩) $\text{٢١} \le \text{٣س} \implies \text{س} \ge \text{٧}$ [١٫٥ درجة]. | ١٠) $-\text{٨ب} - \text{٢} < -\text{٣ب} + \text{٨} \implies -\text{٥ب} < \text{١٠} \implies \text{ب} > -\text{٢}$ [درجتان].</p>
                <p>١١) <strong>الخيار الصحيح هو: ب) أكثر من ٣٨ ريالاً</strong>، لأن $\text{س} + \text{٥٢} > \text{٩٠} \implies \text{س} > \text{٣٨}$ [٣ درجات].</p>
            </div>

            {footer_sig_html}
        </article>

        <!-- ورقة تدريب معمل الجبر (ص 142) -->
        <article class="worksheet-paper page-break" id="ws-lab">
            {header_html}
            <div class="ws-meta-bar">
                <span>ورقة تدريب استكشافية: معمل الجبر (قراءة العبارات المركبة) ص ١٤٢</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / ٥ ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">حدد ما إذا كانت كل عبارة صحيحة أم خاطئة مع تفسير السبب رياضياً:</div>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الرقم</th>
                            <th>العبارة المركبة</th>
                            <th>القيمة (صحيحة / خاطئة)</th>
                            <th>التفسير المنطقي والرياضي</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>١</td>
                            <td>العدد ٥ أولي <strong>أو</strong> العدد ٢ فردي</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>٢</td>
                            <td>للمثلث ٣ أضلاع <strong>و</strong> ٣ زوايا</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>٣</td>
                            <td>$\text{١١} > \text{٥}$ &nbsp;<strong>أو</strong>&nbsp; $\text{٩} < \text{٧}$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>٤</td>
                            <td>$-\text{٢} < ٠$ &nbsp;<strong>و</strong>&nbsp; $\text{٣} > \text{٧}$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>٥</td>
                            <td>$\text{٥} > \text{١٠}$ &nbsp;<strong>و</strong>&nbsp; $\text{٤} > -\text{٢}$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Dedicated Solution Toggle Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-lab', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لتدريب معمل الجبر
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-lab" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة لمعمل الجبر (ص ١٤٢):</h4>
                <p>١. <strong>صحيحة</strong> (لأن ٥ أولي صحيحة، والرابط "أو" يكفيه صواب أحد الأمرين).<br>
                ٢. <strong>صحيحة</strong> (لأن كلتا العبارتين صحيحتان مع الرابط "و").<br>
                ٣. <strong>صحيحة</strong> (لأن $\text{١١} > \text{٥}$ صحيحة مع الرابط "أو").<br>
                ٤. <strong>خاطئة</strong> (لأن $\text{٣} > \text{٧}$ خاطئة والرابط "و" يتطلب صواب العبارتين معاً).<br>
                ٥. <strong>خاطئة</strong> (لأن $\text{٥} > \text{١٠}$ خاطئة والرابط "و" يجعل المركبة خاطئة).</p>
            </div>

            {footer_sig_html}
        </article>

        <!-- ورقة عمل الدرس 4-4 -->
        <article class="worksheet-paper page-break" id="ws-4-4">
            {header_html}
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (٤-٤) حل المتباينات المركبة (ص ١٤٣ – ١٤٧)</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [٤ درجات]</div>
                <p><strong>١) مجموعة حل المتباينة المركبة: $\text{س} < \text{٢} \text{ و } \text{س} > \text{٦}$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ \text{س} \mid \text{٢} < \text{س} < \text{٦} \}$</div>
                    <div class="mcq-option-line">ب) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ج) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">د) $\text{س} = \text{٤}$</div>
                </div>

                <p><strong>٢) حل المتباينة المركبة: $-\text{٢} \le \text{س} - \text{٣} < \text{٥}$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{١} \le \text{س} < \text{٨}$</div>
                    <div class="mcq-option-line">ب) $-\text{٥} \le \text{س} < \text{٢}$</div>
                    <div class="mcq-option-line">ج) $\text{١} < \text{س} \le \text{٨}$</div>
                    <div class="mcq-option-line">د) $-\text{١} \le \text{س} < \text{٨}$</div>
                </div>

                <p><strong>٣) "سرعة المركبة لا تقل عن ٧٠ ولا تزيد عن ١١٠ كم/س"، يعبر عنها بالمتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{٧٠} < \text{ع} < \text{١١٠}$</div>
                    <div class="mcq-option-line">ب) $\text{٧٠} \le \text{ع} \le \text{١١٠}$</div>
                    <div class="mcq-option-line">ج) $\text{ع} \le \text{٧٠} \text{ أو } \text{ع} \ge \text{١١٠}$</div>
                    <div class="mcq-option-line">د) $\text{ع} > \text{١١٠}$</div>
                </div>

                <p><strong>٤) التمثيل البياني للمتباينة المركبة $\text{س} \le \text{١} \text{ أو } \text{س} > \text{٤}$ يتكون من:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) قطعة مستقيمة واصلة بين ١ و ٤</div>
                    <div class="mcq-option-line">ب) شعاعين في اتجاهين متعاكسين</div>
                    <div class="mcq-option-line">ج) نقطتين مظللتين فقط</div>
                    <div class="mcq-option-line">د) تظليل خط الأعداد بالكامل</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: مثل كلاً من المتباينات المركبة الآتية بيانيا على خط الأعداد: [٣ درجات]</div>
                <p>١. $-\text{٣} < \text{س} \le \text{٢}$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
                <p style="margin-top:14px;">٢. $\text{ص} \le -\text{٢} \text{ أو } \text{ص} > \text{٣}$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة المركبة التالية، واكتب مجموعة الحل: [٣ درجات]</div>
                <p style="text-align:center; font-size:1.25rem; font-weight:bold; margin:10px 0;">$-\text{٧} \le \text{٢س} + \text{١} < \text{٩}$</p>
                <p>خطوات الحل: ................................................................................................................</p>
                <p>مجموعة الحل: .................................................................................................................</p>
            </div>

            <!-- Dedicated Solution Toggle Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-4', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (٤-٤)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-4" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي (ورقة عمل ٤-٤):</h4>
                <p><strong>السؤال الأول (٤ درجات):</strong> ١) ج ($\emptyset$ لعدم وجود تقاطع) | ٢) أ ($\text{١} \le \text{س} < \text{٨}$ بإضافة $+\text{٣}$) | ٣) ب ($\text{٧٠} \le \text{ع} \le \text{١١٠}$) | ٤) ب (شعاعين متعاكسين).</p>
                <p><strong>السؤال الثاني (٣ درجات):</strong> ١. دائرة مفتوحة عند $-\text{٣}$ ومغلقة عند $\text{٢}$ وتظليل بينهما. | ٢. دائرة مغلقة عند $-\text{٢}$ وسهم لليسار، ودائرة مفتوحة عند $\text{٣}$ وسهم لليمين.</p>
                <p><strong>السؤال الثالث (٣ درجات):</strong> بطرح ١ من الأطراف: $-\text{٨} \le \text{٢س} < \text{٨}$. بالقسمة على ٢: $-\text{٤} \le \text{س} < \text{٤}$. مجموعة الحل: $\{ \text{س} \mid -\text{٤} \le \text{س} < \text{٤} \}$.</p>
            </div>

            {footer_sig_html}
        </article>
    </section>

</div>

<!-- Interactive JS Script for Solution Toggling -->
<script>
    function toggleSolution(id, btn) {{
        var el = document.getElementById(id);
        if (!el) return;
        
        if (el.style.display === "none" || el.style.display === "") {{
            el.style.display = "block";
            btn.innerHTML = '<span class="btn-icon">🔒</span> إخفاء الحل النموذجي';
            btn.classList.add("active");
            if (window.MathJax && window.MathJax.typesetPromise) {{
                window.MathJax.typesetPromise([el]).catch(function (err) {{ console.log(err); }});
            }}
        }} else {{
            el.style.display = "none";
            btn.innerHTML = '<span class="btn-icon">💡</span> إظهار الحل النموذجي';
            btn.classList.remove("active");
        }}
    }}
</script>

<footer style="text-align:center; padding:24px; color:var(--gray-600); font-size:0.9rem; border-top:1px solid var(--gray-200); background:white;">
    المدارس المتقدمة للتعلم الذكي بجدة | إعداد: أ. محمد عبدالله جمعة | تصميم خبير التعليم وفق منهجية STEM والمعايير المعتمدة لوزارة التعليم ٢٠٢٦م
</footer>

</body>
</html>
'''

target_file = r"c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\الحقيبة_الشاملة_المتباينات_الخطية_3م.html"
with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated successfully with official logo, teacher Mohamed Abdullah Jumaa, and full STEM prompt compliance! Size:", os.path.getsize(target_file), "bytes")
