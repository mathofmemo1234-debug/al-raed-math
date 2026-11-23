# -*- coding: utf-8 -*-
import sys

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة التعليمية الشاملة | المتباينات الخطية (رياضيات 3م - الفصل الثاني)</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <!-- MathJax for Arabic & Professional Math Rendering -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
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
            --accent-light: #fffbeb;
            --danger: #dc2626;
            --danger-light: #fef2f2;
            --dark: #0f172a;
            --gray-100: #f8fafc;
            --gray-200: #e2e8f0;
            --gray-300: #cbd5e1;
            --gray-600: #475569;
            --gray-700: #334155;
            --white: #ffffff;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
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
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(8px);
            color: var(--white);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            border-bottom: 2px solid var(--primary);
        }

        .nav-brand {
            font-size: 1.15rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 10px;
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
            padding: 7px 16px;
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

        /* Master Header Banner */
        .hero-banner {
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 50%, #0369a1 100%);
            color: var(--white);
            padding: 40px 32px;
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-lg);
            margin-bottom: 36px;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .hero-banner::after {
            content: "∑ ∫ π";
            position: absolute;
            left: -20px;
            bottom: -30px;
            font-size: 8rem;
            color: rgba(255, 255, 255, 0.05);
            font-weight: 900;
            pointer-events: none;
            user-select: none;
        }

        .hero-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #bae6fd;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2.2rem;
            font-weight: 900;
            margin-bottom: 10px;
            line-height: 1.3;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            opacity: 0.92;
            max-width: 850px;
        }

        /* Section Big Separators */
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

        /* Lesson Card Container */
        .unit-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
            transition: border-color 0.2s;
        }

        .unit-card:hover {
            border-color: var(--gray-300);
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

        /* General Tables */
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

        /* Frayer Model Styling */
        .frayer-box {
            background: var(--gray-100);
            border: 2px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 16px;
            margin: 18px 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            position: relative;
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

        /* Rules Boxes */
        .rule-card-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }

        @media (max-width: 768px) {
            .rule-card-grid { grid-template-columns: 1fr; }
            .frayer-box { grid-template-columns: 1fr; }
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

        /* Worksheets Styling */
        .worksheet-paper {
            background: var(--white);
            border: 2px solid #334155;
            border-radius: var(--radius-md);
            padding: 28px;
            margin-bottom: 30px;
            box-shadow: var(--shadow-sm);
        }

        .ws-header {
            border-bottom: 2px solid #334155;
            padding-bottom: 14px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .ws-header-center {
            text-align: center;
        }

        .ws-header-center h3 {
            font-size: 1.35rem;
            font-weight: 800;
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
            font-weight: 600;
        }

        .ws-question-block {
            margin-bottom: 20px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--gray-200);
        }

        .ws-q-title {
            font-weight: 700;
            font-size: 1.05rem;
            margin-bottom: 10px;
            color: var(--primary-dark);
        }

        .mcq-options-vertical {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 10px 0 10px 20px;
        }

        .mcq-option-line {
            background: #f8fafc;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.95rem;
        }

        /* Answer Key Collapsible */
        .answer-key-box {
            background: #f0fdf4;
            border: 2px solid #86efac;
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-top: 20px;
        }

        .answer-key-box h4 {
            color: #166534;
            font-size: 1.05rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Number Line SVG Container */
        .nl-svg-container {
            width: 100%;
            max-width: 480px;
            margin: 12px auto;
            display: block;
        }

        /* Alert Callouts */
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

        .callout-info {
            background: var(--primary-light);
            border-right: 5px solid var(--primary);
            color: #1e3a8a;
        }

        .callout-success {
            background: #ecfdf5;
            border-right: 5px solid #10b981;
            color: #065f46;
        }

        /* Print Settings */
        @media print {
            .sticky-nav { display: none !important; }
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

<!-- Sticky Header Navigation -->
<nav class="sticky-nav">
    <div class="nav-brand">
        📐 رياضيات 3م | المتباينات الخطية (ص 130 - 147)
    </div>
    <ul class="nav-links">
        <li><a href="#plans-section">📑 خطط التدريس والتحضير (STEM)</a></li>
        <li><a href="#summaries-section">📚 الملخصات الشاملة للطلاب</a></li>
        <li><a href="#worksheets-section">📝 أوراق العمل والاختبارات</a></li>
    </ul>
    <button class="print-btn-header" onclick="window.print()">🖨️ طباعة الحقيبة كاملة</button>
</nav>

<div class="main-container">

    <!-- Hero Title Banner -->
    <header class="hero-banner">
        <span class="hero-tag">المملكة العربية السعودية | وزارة التعليم 2026</span>
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: المتباينات الخطية</h1>
        <p class="hero-subtitle">
            ملف موحد متكامل يحتوي على: <strong>خطط التدريس وفق معايير STEM السبعة</strong> (متتالية)، تليها <strong>الملخصات الشاملة للطالب</strong> (متتالية)، ثم <strong>أوراق العمل واختبارات منتصف الفصل ونماذج الإجابة</strong> (متتالية)، شاملةً الصفحات من 130 إلى 147 من كتاب الرياضيات للصف الثالث المتوسط.
        </p>
    </header>

    <!-- ========================================================================= -->
    <!-- القسم الأول: خطط التدريس والتحضير وفق منهجية STEM (متتالية) -->
    <!-- ========================================================================= -->
    <section id="plans-section" class="master-section">
        <div class="section-header-banner plans">
            <h2>📑 القسم الأول: خطط التدريس والتحضير وفق معايير STEM السبعة (متتالية)</h2>
            <span class="section-badge">دليل المعلم الاحترافي</span>
        </div>

        <!-- الخطة 1: الدرس 4-2 -->
        <article class="unit-card" id="plan-4-2">
            <div class="unit-title-box">
                <h3><span>1️⃣</span> خطة الدرس (4-2): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص 130 – 134</span>
            </div>

            <h4>1. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الأعداد والعمليات والجبر | <strong>المعيار:</strong> حل متباينات الخطوة الواحدة باستخدام العمليات العكسية وتمثيل مجموعة الحل بيانياً.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف 1:</strong> أن يحل الطالب متباينات خطية تتضمن الضرب في عدد حقيقي موجب أو سالب بدقة تامة بنسبة إتقان 100%.</li>
                <li><strong>الهدف 2:</strong> أن يطبق الطالب خاصية القسمة على المتباينات مع عكس اتجاه رمز التباين عند القسمة على عدد سالب دون أي خطأ.</li>
                <li><strong>الهدف 3:</strong> أن ينمذج الطالب مسألة شراء واقعية في صورة متباينة خطية ويحلها مفسراً معنى النتيجة في سياق الحياة اليومية.</li>
            </ul>

            <h4 style="margin-top:16px;">2. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>الحقبنة:</strong> "إذا كان $8 > 4$ وضاعفنا المقدارين ثلاث مرات تصبح $24 > 12$. ماذا لو عكسنا الموقف وخسر كل طرف ضعفي ما يملك (الضرب في $-2$)? كيف يصبح وضع الكفتين في المقارنة على خط الأعداد؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> نشاط الميزان ذي الكفتين، وتقويم سريع لحل المعادلة: $-4س = 20$. ما إشارة المعامل وما خطوة التخلص منه؟</li>
            </ul>

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
                        <td>• حل المعادلات الخطية بالضرب والقسمة.<br>• حل المتباينات بالجمع والطرح.<br>• التمثيل البياني على خط الأعداد.</td>
                        <td>• كيف تؤثر الإشارة السالبة عند الضرب والقسمة؟<br>• متى ينعكس اتجاه رمز التباين؟<br>• كتابة مجموعة الحل بالصفة المميزة.</td>
                        <td>• عند الضرب أو القسمة في سالب نعكس الإشارة فوراً.<br>• الضرب في موجب لا يغير اتجاه التباين.<br>• الصفة المميزة: $\{ س \mid س > أ \}$.</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">3. بيئة التعلم (3 قواعد صفية حاسمة):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فحص إشارة المعامل أولاً:</strong> قبل إجراء الضرب أو القسمة، يفحص الطالب إشارة العدد المضروب فيه أو المقسوم عليه.</li>
                <li><strong>قاعدة التمثيل الفوري:</strong> كل حل جبري يُترجم مباشرة إلى نقطة (مغلقة/مفتوحة) وسهم اتجاه على خط الأعداد.</li>
                <li><strong>قاعدة التعويض الاستكشافي:</strong> التحقق من صحة الحل باختيار عدد من منطقة الحل وتجريبه في المتباينة الأصلية.</li>
            </ol>

            <h4 style="margin-top:16px;">4. استراتيجيات التعلم النشط وتطوير المحتوى:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>العصف الذهني:</strong> استكشاف تحول $2 < 5$ عند الضرب في $-3$ إلى $-6 > -15$، واستنتاج حتمية قلب الرمز لحفظ الصدق الرياضي.</li>
                <li><strong>فكر - زاوج - شارك:</strong> حل المتباينة $-\frac{3}{7}ر \le 21$ (مثال 2 ص 132) بالضرب في المعكوس الضربي $(-\frac{7}{3})$.</li>
            </ul>

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
                    <p>• $-2س < 10 \implies س > -5$<br>• $-\frac{1}{3}ص \ge 4 \implies ص \le -12$<br>• $-5 > -8 \implies 5 < 8$ (ضرب في $-1$)</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة (أخطاء شائعة)</h4>
                    <p>• $3س < -15 \implies س > -5$ ❌ (المقسوم عليه موجب فلا نقلب).<br>• $س - 4 < 7 \implies س > 11$ ❌ (الطرح والجمع لا يعكسان الرمز مطلقاً).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">5. التكامل مع منهجية STEM والواقع:</h4>
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

            <h4 style="margin-top:16px;">6. منظومة التقويم الثلاثية:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي (مقالي):</strong> حل $-\frac{2}{3} ص < 6 \implies ص > 6 \times (-\frac{3}{2}) \implies ص > -9$. التحقق: بالتعويض بالصفر $0 < 6$ (صحيح ✔️).</li>
                <li><strong>تقويم ختامي:</strong> جمعت دار نشر أكثر من 5500 ريال من بيع كتاب جديد ثمنه 15 ريالاً. المتباينة: $15ن > 5500 \implies ن > 366.67$؛ أقل عدد بيع هو $367$ نسخة.</li>
                <li><strong>واجب منزلي (MCQ):</strong> ما حل $-4س \le 28$؟ 
                    <br>أ) $س \le -7$ | <strong>ب) $س \ge -7$</strong> | ج) $س \ge 7$ | د) $س \le 7$ (الحل: ب، لعكس الإشارة بالقسمة على $-4$).</li>
            </ul>

            <h4 style="margin-top:16px;">7. الغلق والتحدي الإثرائي:</h4>
            <p><strong>سؤال التحدي:</strong> إذا علمت أن حل المتباينة $أ \cdot س \ge 20$ هو $س \le -5$، فما قيمة العدد $أ$؟ (الحل: $أ = -4$، وهو سالب حتماً لقلب إشارة التباين).</p>
        </article>

        <!-- الخطة 2: الدرس 4-3 -->
        <article class="unit-card" id="plan-4-3">
            <div class="unit-title-box">
                <h3><span>2️⃣</span> خطة الدرس (4-3): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">كتاب الطالب: ص 135 – 140</span>
            </div>

            <h4>1. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار:</strong> حل متباينات خطية تتضمن عدة عمليات وخاصية التوزيع وتمييز الحالات الخاصة.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف 1:</strong> أن يحل الطالب متباينات خطية متعددة الخطوات باتباع الترتيب المعكوس للعمليات بنسبة إتقان 100%.</li>
                <li><strong>الهدف 2:</strong> أن يطبق الطالب خاصية التوزيع لتجميع المتغيرات في طرف والثوابت في طرف بدقة لا تقل عن 90%.</li>
                <li><strong>الهدف 3:</strong> أن يميز الطالب المتباينات التي حلها هو المجموعة الخالية $\emptyset$ وتلك التي حلها مجموعة الأعداد الحقيقية $\mathbb{R}$.</li>
            </ul>

            <h4 style="margin-top:16px;">2. مرحلة الانخراط والتركيز:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>الحقبنة:</strong> "مندوب مبيعات يتقاضى راتباً ثابتاً 2500 ريال وعمولة 75 ريالاً لكل قطعة يبيعها. إذا أراد دخلاً شهرياً لا يقل عن 7000 ريال، فكم قطعة يلزمه بيعها؟ كيف نكتبها جبرياً؟ ($75س + 2500 \ge 7000$) وما أول خطوة لحلها؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> حل المعادلة: $3(س - 2) + 4 = 19$. ما فائدة خاصية التوزيع في فك الأقواس؟</li>
            </ul>

            <h4 style="margin-top:16px;">3. بيئة التعلم (قواعد العمل الصفي):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فك الأقواس أولاً:</strong> لا يُجرى أي جمع أو طرح قبل التخلص من الأقواس عبر خاصية التوزيع.</li>
                <li><strong>قاعدة تجميع المتغير الأصغر:</strong> نقل الحد المتغير ذي المعامل الأصغر لتفادي التعامل مع المعاملات السالبة إن أمكن.</li>
                <li><strong>قاعدة رصد الحالات الخاصة:</strong> عندما ينحذف المتغير من الطرفين، التوقف فوراً لقراءة العبارة العددية المتبقية.</li>
            </ol>

            <h4 style="margin-top:16px;">4. الاستراتيجيات ومربع فراير:</h4>
            <!-- مربع فراير للدرس 4-3 -->
            <div class="frayer-box">
                <div class="frayer-center-title">مربع فراير: المتباينة متعددة الخطوات (Multi-Step Inequality)</div>
                <div class="frayer-quadrant">
                    <h4>التعريف</h4>
                    <p>متباينة جبرية تتطلب إجراء أكثر من عملية عكسية واحدة (مثل: التوزيع، ثم الجمع أو الطرح، ثم الضرب أو القسمة) لعزل المتغير بمفرده.</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>الخصائص</h4>
                    <p>• تعتمد على ترتيب العمليات المعكوس.<br>• قد تحتوي أقواساً أو متغيرات في الطرفين.<br>• تقبل الحالات الخاصة ($\emptyset$ و $\mathbb{R}$).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>أمثلة منتمية</h4>
                    <p>• $3س + 5 > 17$<br>• $2(ص - 4) \le 6ص + 10$<br>• $\frac{ن - 1}{3} \ge 4$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $س - 7 < 3$ (خطوة واحدة - جمع فقط).<br>• $-4ص \ge 20$ (خطوة واحدة - قسمة فقط).<br>• $2س + 3 = 11$ (معادلة وليست متباينة).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">5. التكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> حساب نقطة التعادل الإنتاجي بين آلتين؛ متى تكون تكلفة تشغيل الآلة الحديثة أقل من التقليدية بدلالة ساعات العمل.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $2(ص + 4) > 2ص + 10 \implies 2ص + 8 > 2ص + 10 \implies 8 > 10$ (خاطئة دائماً)، إذن الحل هو $\emptyset$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> حل المتباينة $3(س - 1) \le 3س + 4$ هو: 
                    <br>أ) $\emptyset$ | <strong>ب) مجموعة الأعداد الحقيقية $\mathbb{R}$</strong> | ج) $س \le 3$ | د) $س \ge -1$ (الحل: ب، لأن $-3 \le 4$ صحيحة دائماً).</li>
            </ul>
        </article>

        <!-- الخطة 3: اختبار منتصف الفصل 4 -->
        <article class="unit-card" id="plan-mid-quiz">
            <div class="unit-title-box">
                <h3><span>3️⃣</span> خطة تنفيذ وتقويم: اختبار منتصف الفصل الرابع</h3>
                <span class="page-range-pill">كتاب الطالب: ص 141 (الدروس 4-1 إلى 4-3)</span>
            </div>

            <h4>1. الأهداف والمهام التقويمية:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>التشخيص والقياس:</strong> قياس مستوى تمكن الطلاب من مهارات الدروس الثلاثة الأولى (الجمع/الطرح، الضرب/القسمة، متعددة الخطوات).</li>
                <li><strong>تحليل الأخطاء:</strong> رصد أخطاء إشارات السالب في الضرب والقسمة، وأخطاء خاصية التوزيع وتجميع الحدود.</li>
                <li><strong>المعالجة والتمايز:</strong> تصميم أنشطة علاجية فورية للطلاب المتعثرين وأنشطة إثرائية للمتفوقين.</li>
            </ul>

            <h4 style="margin-top:16px;">2. جدول مصفوفة الاختبار ومستويات الصعوبة (ص 141):</h4>
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
                        <td><strong>الدرس 4-1</strong> (الجمع والطرح)</td>
                        <td>الأسئلة: 1، 2، 3، 4، 5 (مدينة الألعاب)، 9</td>
                        <td>حل متباينات الجمع والطرح والتمثيل البياني والمسائل الواقعية</td>
                        <td>30%</td>
                    </tr>
                    <tr>
                        <td><strong>الدرس 4-2</strong> (الضرب والقسمة)</td>
                        <td>الأسئلة: 6، 7، 8، 10، 11، 12، 13، 14، 15، 16، 17</td>
                        <td>تطبيق خصائص الضرب والقسمة ومراعاة الإشارة السالبة والكسور</td>
                        <td>40%</td>
                    </tr>
                    <tr>
                        <td><strong>الدرس 4-3</strong> (متعددة الخطوات)</td>
                        <td>الأسئلة: 18، 19، 20، 21، 22، 23</td>
                        <td>التوزيع، تجميع المتغيرات في الطرفين، والمسائل اللفظية المركبة</td>
                        <td>30%</td>
                    </tr>
                </tbody>
            </table>
        </article>

        <!-- الخطة 4: معمل الجبر / استكشاف -->
        <article class="unit-card" id="plan-lab">
            <div class="unit-title-box">
                <h3><span>4️⃣</span> خطة تدريس: معمل الجبر (استكشاف العبارات المركبة)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 142</span>
            </div>

            <h4>1. الأهداف الاستكشافية:</h4>
            <ul style="margin: 8px 24px;">
                <li>أن يستكشف الطالب المفهوم المنطقي والرياضي لأداتي الربط <strong>(و)</strong> و <strong>(أو)</strong>.</li>
                <li>أن يحدد قيم صواب العبارات المركبة معللاً إجابته بدقة منطقية تامة.</li>
                <li>أن يمهد ذهنياً للانتقال إلى حل المتباينات المركبة بيانياً وجبرياً.</li>
            </ul>

            <h4 style="margin-top:16px;">2. سير النشاط والتدريس:</h4>
            <p><strong>المناقشة اللغوية والرياضية:</strong> مقارنة الاستعمال اليومي لكلمة "أو" (أحد الأمرين لا كلاهما) بالمعنى الرياضي (أحد الأمرين أو كلاهما). وكلمة "و" التي تلزم حدوث الشرطين معاً.</p>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>أداة الربط</th>
                        <th>المعنى المنطقي والرياضي</th>
                        <th>شرط الصواب</th>
                        <th>مثال الكتاب (ص 142)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>الرابط (و)</strong></td>
                        <td>التقاطع ($\cap$)</td>
                        <td>تكون صحيحة <strong>فقط إذا كانت كلتا العبارتين صحيحتين</strong> معاً.</td>
                        <td>"للعنكبوت 8 أرجل (ص) و للحصان 5 أرجل (خ)" $\implies$ العبارة المركبة <strong>خاطئة</strong>.</td>
                    </tr>
                    <tr>
                        <td><strong>الرابط (أو)</strong></td>
                        <td>الاتحاد ($\cup$)</td>
                        <td>تكون صحيحة إذا كانت <strong>إحدى العبارتين على الأقل صحيحة</strong>.</td>
                        <td>"للعنكبوت 8 أرجل (ص) أو للحصان 5 أرجل (خ)" $\implies$ العبارة المركبة <strong>صحيحة</strong>.</td>
                    </tr>
                </tbody>
            </table>
        </article>

        <!-- الخطة 5: الدرس 4-4 -->
        <article class="unit-card" id="plan-4-4">
            <div class="unit-title-box">
                <h3><span>5️⃣</span> خطة الدرس (4-4): حل المتباينات المركبة</h3>
                <span class="page-range-pill">كتاب الطالب: ص 143 – 147</span>
            </div>

            <h4>1. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار:</strong> حل المتباينات المركبة (الوصل والفصل) وتمثيلها بيانياً ونمذجة ظواهر الواقع بها.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف 1:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "و" (تقاطع) ويمثل مجموعة حلها بدقة 100%.</li>
                <li><strong>الهدف 2:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "أو" (اتحاد) ويمثلها بيانياً بالأسهم المتعاكسة أو الشاملة.</li>
                <li><strong>الهدف 3:</strong> أن يصيغ الطالب متباينة مركبة تمثل موقفاً حياتياً (درجات الحرارة، أطوال الموجات، السرعات) بصورة صحيحة.</li>
            </ul>

            <h4 style="margin-top:16px;">2. مربع فراير وخريطة المفاهيم:</h4>
            <div class="frayer-box">
                <div class="frayer-center-title">مربع فراير: المتباينة المركبة (Compound Inequality)</div>
                <div class="frayer-quadrant">
                    <h4>التعريف</h4>
                    <p>عبارة رياضية مكونة من متباينتين بسيطتين مربوطتين إما بحرف العطف "و" (تقاطع الشروط) أو بحرف العطف "أو" (اتحاد الشروط).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>الخصائص</h4>
                    <p>• متباينة "و" تمثل منطقة التداخل المشتركة.<br>• متباينة "أو" تمثل دمج المنطقتين.<br>• تكتب "و" في صورة متصلة ثلاثية الأطراف ($أ < س < ب$).</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>أمثلة منتمية</h4>
                    <p>• $-2 \le س + 1 < 5$<br>• $ص < -3 \text{ أو } ص \ge 2$<br>• $18 \le \text{الحرارة} \le 24$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $3س + 4 > 10$ (متباينة بسيطة).<br>• $س = 2 \text{ أو } س = -1$ (معادلة وليست متباينة).<br>• $س < 5$ (أحادية الشرط).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">3. تكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> برمجة حساسات التكييف الذكية في المباني؛ ضبط درجة الحرارة الطبيعية بين $20^\circ\text{C}$ و $24^\circ\text{C}$ بمتباينة الوصل، وإطلاق جرس الإنذار إذا انخفضت عن $10^\circ\text{C}$ أو ارتفعت عن $35^\circ\text{C}$ بمتباينة الفصل.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $-3 \le 2س + 1 < 7 \implies -4 \le 2س < 6 \implies -2 \le س < 3$. مجموعة الحل: $\{ س \mid -2 \le س < 3 \}$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> مجموعة حل $س < 2 \text{ و } س > 5$ هي: 
                    <br>أ) $\{ س \mid 2 < س < 5 \}$ | <strong>ب) المجموعة الخالية $\emptyset$</strong> | ج) $\mathbb{R}$ | د) $س = 3$ (الحل: ب، لانعدام التقاطع).</li>
            </ul>
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية) -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">مذكرة المذاكرة والمراجعة المركزة</span>
        </div>

        <!-- ملخص الدرس 4-2 -->
        <article class="unit-card" id="summary-4-2">
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-2): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">ص 130 - 134</span>
            </div>

            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4 style="color:#166534; margin-bottom:8px;">1. الضرب أو القسمة في عدد موجب (+)</h4>
                    <p><strong>يبقى اتجاه إشارة المتباينة كما هو دون أي تغيير:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ > 0$ فإن $أ \times جـ > ب \times جـ$</p>
                    <p>• مثال: $\frac{س}{3} < 5 \implies س < 15$</p>
                </div>
                <div class="rule-subcard negative">
                    <h4 style="color:#991b1b; margin-bottom:8px;">2. الضرب أو القسمة في عدد سالب (-)</h4>
                    <p><strong>يجب عكس اتجاه إشارة المتباينة فوراً:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ < 0$ فإن $أ \times جـ < ب \times جـ$</p>
                    <p>• مثال: $-2ص \ge 8 \implies ص \le -4$</p>
                </div>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>تنبيه الاختبارات الحاسم:</strong> إشارة المتباينة تُعكس <u>فقط إذا كان المعامل المقسوم عليه أو المضروب فيه سالباً</u>، ولا نلتفت لإشارة الطرف الآخر! مثال: $3س \le -12 \implies س \le -4$ (لم نقلب لأن 3 موجبة).
            </div>

            <h4 style="margin-top:16px;">أمثلة الكتاب المحلولة خطوة بخطوة:</h4>
            <div style="background:#f8fafc; padding:16px; border-radius:8px; margin:10px 0; border-right:4px solid var(--primary);">
                <strong>مثال 1:</strong> حل المتباينة $-\frac{3}{7} ر < 21$
                <br>• نضرب الطرفين في المعكوس الضربي $(-\frac{7}{3})$ ونعكس إشارة $<$ إلى $>$:
                $$ر > 21 \times \left(-\frac{7}{3}\right) \implies ر > -49$$
                • مجموعة الحل: $\{ ر \mid ر > -49 \}$ (دائرة مفتوحة عند $-49$ وسهم لليمين).
            </div>
        </article>

        <!-- ملخص الدرس 4-3 -->
        <article class="unit-card" id="summary-4-3">
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-3): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">ص 135 - 140</span>
            </div>

            <h4>خوارزمية الحل في 4 خطوات ذهبية:</h4>
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
                        <td>عبارة خاطئة وغير ممكنة (مثل $5 < 2$)</td>
                        <td>$\emptyset$ (فاي)</td>
                        <td>خط أعداد فارغ تماماً دون أي تظليل</td>
                    </tr>
                    <tr>
                        <td><strong>جميع الأعداد الحقيقية ( ℝ )</strong></td>
                        <td>عبارة صائبة دائماً (متطابقة مثل $3 \le 7$)</td>
                        <td>$\{ س \mid س \in \mathbb{R} \}$</td>
                        <td>خط الأعداد مظلل بالكامل بسهمين ممتدين</td>
                    </tr>
                </tbody>
            </table>
        </article>

        <!-- ملخص مراجعة اختبار منتصف الفصل 4 -->
        <article class="unit-card" id="summary-mid-quiz">
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص ومراجعة مركزة: اختبار منتصف الفصل الرابع</h3>
                <span class="page-range-pill">ص 141 (مراجعة الدروس 4-1 إلى 4-3)</span>
            </div>
            <p><strong>المفاهيم المحورية للاختبار:</strong></p>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>متباينات الجمع والطرح:</strong> إذا كان $س - 4 > 6 \implies س > 10$. وإذا كان $س + 3 \le 7 \implies س \le 4$.</li>
                <li><strong>متباينات الضرب والقسمة:</strong> انتبه جيداً لمعامل المتغير؛ إن كان سالباً اقلب إشارة المتباينة فوراً.</li>
                <li><strong>المسائل اللفظية:</strong> "لا يزيد على" تعني $\le$، و"لا يقل عن" تعني $\ge$، و"أكثر من" تعني $>$، و"أقل من" تعني $<$.</li>
            </ul>
        </article>

        <!-- ملخص معمل الجبر -->
        <article class="unit-card" id="summary-lab">
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص معمل الجبر: قراءة العبارات المركبة</h3>
                <span class="page-range-pill">ص 142</span>
            </div>
            <p><strong>قواعد الصواب والخطأ المنطقية:</strong></p>
            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4>أداة الربط "و" (التقاطع ∩)</h4>
                    <p>• تكون <strong>صحيحة فقط</strong> إذا كانت كلتا العبارتين صحيحتين.</p>
                    <p>• إذا كانت إحداهما خطأ فالعبارة المركبة بأكملها خاطئة.</p>
                </div>
                <div class="rule-subcard" style="background:#eff6ff; border-color:#3b82f6;">
                    <h4 style="color:#1d4ed8;">أداة الربط "أو" (الاتحاد ∪)</h4>
                    <p>• تكون <strong>صحيحة</strong> إذا كانت إحدى العبارتين على الأقل صحيحة.</p>
                    <p>• لا تكون خاطئة إلا إذا كانت العبارتان معاً خاطئتين.</p>
                </div>
            </div>
        </article>

        <!-- ملخص الدرس 4-4 -->
        <article class="unit-card" id="summary-4-4">
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-4): حل المتباينات المركبة</h3>
                <span class="page-range-pill">ص 143 - 147</span>
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
                        <td>غالباً جملة متصلة: $-3 \le س < 5$</td>
                        <td>جملتان منفصلتان بكلمة "أو": $س < 1 \text{ أو } س \ge 4$</td>
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
                <p><strong>تمثيل متباينة الوصل ( $-2 \le س < 4$ ):</strong> مغلقة عند $-2$ ومفتوحة عند $4$ والتظليل بينهما:</p>
                <svg class="nl-svg-container" viewBox="0 0 400 45">
                    <line x1="20" y1="20" x2="380" y2="20" stroke="#94a3b8" stroke-width="3" />
                    <line x1="120" y1="20" x2="280" y2="20" stroke="#0d9488" stroke-width="6" />
                    <circle cx="120" cy="20" r="6" fill="#0d9488" stroke="#042f2e" stroke-width="2" />
                    <text x="120" y="40" font-size="12" text-anchor="middle" font-weight="bold">-2</text>
                    <circle cx="280" cy="20" r="6" fill="#ffffff" stroke="#0d9488" stroke-width="2" />
                    <text x="280" y="40" font-size="12" text-anchor="middle" font-weight="bold">4</text>
                </svg>

                <p style="margin-top:12px;"><strong>تمثيل متباينة الفصل ( $س \le -1 \text{ أو } س > 3$ ):</strong> سهمان متعاكسان:</p>
                <svg class="nl-svg-container" viewBox="0 0 400 45">
                    <line x1="20" y1="20" x2="380" y2="20" stroke="#94a3b8" stroke-width="3" />
                    <line x1="120" y1="20" x2="30" y2="20" stroke="#2563eb" stroke-width="6" />
                    <circle cx="120" cy="20" r="6" fill="#2563eb" stroke="#1e3a8a" stroke-width="2" />
                    <text x="120" y="40" font-size="12" text-anchor="middle" font-weight="bold">-1</text>
                    <line x1="280" y1="20" x2="370" y2="20" stroke="#2563eb" stroke-width="6" />
                    <circle cx="280" cy="20" r="6" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
                    <text x="280" y="40" font-size="12" text-anchor="middle" font-weight="bold">3</text>
                </svg>
            </div>
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية مع نماذج الإجابة (متتالية) -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section page-break">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية مع نماذج الإجابة (متتالية)</h2>
            <span class="section-badge">جاهزة للطباعة والتنفيذ المباشر</span>
        </div>

        <!-- ورقة عمل الدرس 4-2 -->
        <article class="worksheet-paper" id="ws-4-2">
            <div class="ws-header">
                <div>المملكة العربية السعودية<br>وزارة التعليم - مادة الرياضيات</div>
                <div class="ws-header-center">
                    <h3>ورقة عمل تقويمية: الدرس (4-2) حل المتباينات بالضرب أو بالقسمة</h3>
                    <small>الصف: الثالث المتوسط | الفصل الدراسي الثاني</small>
                </div>
                <div>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</div>
            </div>

            <div class="ws-meta-bar">
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>التاريخ: .... / .... / 2026م</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة من بين الخيارات التالية: [4 درجات]</div>
                
                <p><strong>1) حل المتباينة الجبرية: $3س < -21$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $س < -7$</div>
                    <div class="mcq-option-line">ب) $س > -7$</div>
                    <div class="mcq-option-line">ج) $س < 7$</div>
                    <div class="mcq-option-line">د) $س > 7$</div>
                </div>

                <p><strong>2) ما مجموعة حل المتباينة: $-\frac{ص}{2} \ge 4$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ ص \mid ص \le -8 \}$</div>
                    <div class="mcq-option-line">ب) $\{ ص \mid ص \ge -8 \}$</div>
                    <div class="mcq-option-line">ج) $\{ ص \mid ص \le 8 \}$</div>
                    <div class="mcq-option-line">د) $\{ ص \mid ص \ge 8 \}$</div>
                </div>

                <p><strong>3) عند قسمة طرفي متباينة صحيحة على عدد حقيقي سالب فإن إشارة المتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) تبقى كما هي دون تغيير</div>
                    <div class="mcq-option-line">ب) تتحول إلى إشارة مساواة</div>
                    <div class="mcq-option-line">ج) يتعين تغيير اتجاهها فوراً</div>
                    <div class="mcq-option-line">د) تصبح القيمة مساوية للصفر</div>
                </div>

                <p><strong>4) وفر راشد أكثر من 300 ريال لشراء كتب سعر الكتاب الواحد 25 ريالاً. المتباينة التي تمثل عدد الكتب (ك) هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $25ك < 300$</div>
                    <div class="mcq-option-line">ب) $25ك > 300$</div>
                    <div class="mcq-option-line">ج) $ك + 25 \ge 300$</div>
                    <div class="mcq-option-line">د) $\frac{ك}{25} \le 300$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع إشارة (✓) أمام العبارة الصحيحة وإشارة (✗) أمام العبارة الخاطئة: [3 درجات]</div>
                <p>1. ( &nbsp;&nbsp;&nbsp; ) حل المتباينة $-5س \ge 35$ هو $س \ge -7$.</p>
                <p>2. ( &nbsp;&nbsp;&nbsp; ) التمثيل البياني لـ $س \le 6$ يتم برسم دائرة مغلقة وسهم متجه لليسار.</p>
                <p>3. ( &nbsp;&nbsp;&nbsp; ) ضرب طرفي المتباينة في الكسر الموجب $\frac{1}{3}$ يقتضي عكس اتجاه المتباينة.</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية، ومثل مجموعة الحل بيانياً على خط الأعداد: [3 درجات]</div>
                <p style="text-align:center; font-size:1.15rem; font-weight:bold; margin:10px 0;">$-\frac{4}{5} م \le 20$</p>
                <p>خطوات الحل الجبري: ............................................................................................................</p>
                <p>مجموعة الحل بالصفة المميزة: .................................................................................................</p>
                <p>التمثيل البياني: <br>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <div class="answer-key-box">
                <h4>🔑 مفتاح الإجابة النموذجي (ورقة عمل 4-2):</h4>
                <p><strong>السؤال الأول:</strong> 1) أ ($س < -7$) | 2) أ ($\{ ص \mid ص \le -8 \}$) | 3) ج (يتعين تغيير اتجاهها) | 4) ب ($25ك > 300$).</p>
                <p><strong>السؤال الثاني:</strong> 1) ( ✗ ) الصواب $س \le -7$ لعكس الإشارة عند القسمة على $-5$. | 2) ( ✓ ). | 3) ( ✗ ) الضرب في عدد موجب لا يعكس الإشارة.</p>
                <p><strong>السؤال الثالث:</strong> نضرب في المعكوس الضربي $(-\frac{5}{4})$ ونعكس الرمز: $م \ge 20 \times (-\frac{5}{4}) \implies م \ge -25$. مجموعة الحل: $\{ م \mid م \ge -25 \}$. التمثيل: دائرة مغلقة عند $-25$ وسهم مظلل لليمين.</p>
            </div>
        </article>

        <!-- ورقة عمل الدرس 4-3 -->
        <article class="worksheet-paper page-break" id="ws-4-3">
            <div class="ws-header">
                <div>المملكة العربية السعودية<br>وزارة التعليم - مادة الرياضيات</div>
                <div class="ws-header-center">
                    <h3>ورقة عمل تقويمية: الدرس (4-3) حل المتباينات متعددة الخطوات</h3>
                    <small>الصف: الثالث المتوسط | الفصل الدراسي الثاني</small>
                </div>
                <div>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</div>
            </div>

            <div class="ws-meta-bar">
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>التاريخ: .... / .... / 2026م</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [4 درجات]</div>
                <p><strong>1) أول خطوة صحيحة للبدء في حل المتباينة $4س - 5 > 19$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) القسمة على 4</div>
                    <div class="mcq-option-line">ب) إضافة 5 للطرفين</div>
                    <div class="mcq-option-line">ج) طرح 5 من الطرفين</div>
                    <div class="mcq-option-line">د) ضرب الطرفين في 4</div>
                </div>

                <p><strong>2) حل المتباينة: $-3س + 7 \le 22$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $س \le -5$</div>
                    <div class="mcq-option-line">ب) $س \ge -5$</div>
                    <div class="mcq-option-line">ج) $س \ge 5$</div>
                    <div class="mcq-option-line">د) $س \le 5$</div>
                </div>

                <p><strong>3) ما مجموعة حل المتباينة: $2(س + 3) > 2س + 11$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $س > 5$</div>
                    <div class="mcq-option-line">د) $س < 8$</div>
                </div>

                <p><strong>4) حل المتباينة: $5(ص - 1) \le 5ص + 2$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) مجموعة الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $ص \ge 0$</div>
                    <div class="mcq-option-line">د) $ص \le -3$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: اكتب نوع مجموعة الحل (قيمة محددة / $\emptyset$ / $\mathbb{R}$): [3 درجات]</div>
                <p>1. المتباينة: $3(س - 2) \ge 3س + 5$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>2. المتباينة: $4(ن + 2) > 4ن - 3$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>3. المتباينة: $2هـ + 9 < 15$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية موضحاً خطوات التوزيع والتبسيط: [3 درجات]</div>
                <p style="text-align:center; font-size:1.15rem; font-weight:bold; margin:10px 0;">$3(ت + 2) - 5ت \ge -6$</p>
                <p>خطوة 1 (خاصية التوزيع): .....................................................................................................</p>
                <p>خطوة 2 (تجميع الحدود وعزل المتغير): ......................................................................................</p>
                <p>مجموعة الحل النهائية: ............................................................................................................</p>
            </div>

            <div class="answer-key-box">
                <h4>🔑 مفتاح الإجابة النموذجي (ورقة عمل 4-3):</h4>
                <p><strong>السؤال الأول:</strong> 1) ب (إضافة 5) | 2) ب ($س \ge -5$ لأن $-3س \le 15$) | 3) ب ($\emptyset$ لأن $6 > 11$ مستحيلة) | 4) أ ($\mathbb{R}$ لأن $-5 \le 2$ صحيحة دائماً).</p>
                <p><strong>السؤال الثاني:</strong> 1. $\emptyset$ (لأن $-6 \ge 5$ خاطئة) | 2. $\mathbb{R}$ (لأن $8 > -3$ صائبة دائماً) | 3. قيمة محددة ($هـ < 3$).</p>
                <p><strong>السؤال الثالث:</strong> $3ت + 6 - 5ت \ge -6 \implies -2ت + 6 \ge -6 \implies -2ت \ge -12 \implies ت \le 6$ (قلبنا الإشارة بالقسمة على $-2$). الحل: $\{ ت \mid ت \le 6 \}$.</p>
            </div>
        </article>

        <!-- ورقة اختبار منتصف الفصل 4 (ص 141) -->
        <article class="worksheet-paper page-break" id="ws-mid-quiz">
            <div class="ws-header">
                <div>المملكة العربية السعودية<br>وزارة التعليم - مادة الرياضيات</div>
                <div class="ws-header-center">
                    <h3>اختبار منتصف الفصل الرابع (الدروس 4-1 إلى 4-3)</h3>
                    <small>مطابق للأسئلة المعتمدة في كتاب الطالب ص 141</small>
                </div>
                <div>الدرجة الكلية: [ &nbsp;&nbsp;&nbsp; / 15 ]</div>
            </div>

            <div class="ws-meta-bar">
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الزمن: 35 دقيقة</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 1: متباينات الجمع والطرح (حل ومثل بيانياً على خط الأعداد): [3 درجات]</div>
                <p><strong>1) $س - 8 < 4$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>2) $م + 2 \ge 6$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>3) مدينة الألعاب (سؤال 5 ص 141):</strong> مع حمزة 60 ريالاً، دفع منها 10 ريالات تذكرة دخول. اكتب متباينة تبين المبلغ ($س$) الذي يمكن لحمزة إنفاقه داخل المدينة ثم حلها.<br>
                المتباينة والحل: ................................................................................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 2: متباينات الضرب والقسمة (حل وتحقق من صحة الحل): [4 درجات]</div>
                <p><strong>4) $\frac{1}{3} ص \le 5$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>5) $-8س < 24$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>6) $-9ر \le -45$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>7) $\frac{و}{6} > -3$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 3: متباينات متعددة الخطوات وتطبيقاتها: [5 درجات]</div>
                <p><strong>8) $4أ - 2 < 14$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>9) $2س + 11 \le 5س - 10$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>10) $-2(4ب + 1) < -3ب + 8$</strong><br>
                الحل بالتفصيل: .................................................................................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 4: اختيار من متعدد (سؤال 9 ص 141): [3 درجات]</div>
                <p><strong>11) وفرت عزيزة 52 ريالاً لشراء كتاب يزيد ثمنه على 90 ريالاً. ما المبلغ الإضافي الذي يجب أن توفره عزيزة؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) 38 ريالاً</div>
                    <div class="mcq-option-line">ب) أكثر من 38 ريالاً</div>
                    <div class="mcq-option-line">ج) ليس أكثر من 38 ريالاً</div>
                    <div class="mcq-option-line">د) 38 ريالاً على الأكثر</div>
                </div>
            </div>

            <div class="answer-key-box">
                <h4>🔑 مفتاح الإجابة وتوزيع درجات اختبار منتصف الفصل:</h4>
                <p>1) $س < 12$ (درجة). | 2) $م \ge 4$ (درجة). | 3) $س + 10 \le 60 \implies س \le 50$ ريالاً (درجة).</p>
                <p>4) $ص \le 15$ (درجة). | 5) $س > -3$ لعكس الرمز بالقسمة على سالب (درجة). | 6) $ر \ge 5$ لعكس الرمز (درجة). | 7) $و > -18$ (درجة).</p>
                <p>8) $4أ < 16 \implies أ < 4$ (درجة ونصف). | 9) $11 + 10 \le 5س - 2س \implies 21 \le 3س \implies س \ge 7$ (درجة ونصف). | 10) $-8ب - 2 < -3ب + 8 \implies -5ب < 10 \implies ب > -2$ (درجتان).</p>
                <p>11) <strong>الخيار الصحيح هو: ب) أكثر من 38 ريالاً</strong>، لأن $س + 52 > 90 \implies س > 38$ (3 درجات).</p>
            </div>
        </article>

        <!-- ورقة تدريب معمل الجبر (ص 142) -->
        <article class="worksheet-paper page-break" id="ws-lab">
            <div class="ws-header">
                <div>المملكة العربية السعودية<br>وزارة التعليم - مادة الرياضيات</div>
                <div class="ws-header-center">
                    <h3>ورقة تدريب استكشافية: معمل الجبر (قراءة العبارات المركبة)</h3>
                    <small>كتاب الطالب ص 142</small>
                </div>
                <div>الدرجة: [ &nbsp;&nbsp;&nbsp; / 5 ]</div>
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
                            <td>1</td>
                            <td>العدد 5 أولي <strong>أو</strong> العدد 2 فردي</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>للمثلث 3 أضلاع <strong>و</strong> 3 زوايا</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>$11 > 5$ &nbsp;<strong>أو</strong>&nbsp; $9 < 7$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>$-2 < 0$ &nbsp;<strong>و</strong>&nbsp; $3 > 7$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>$5 > 10$ &nbsp;<strong>و</strong>&nbsp; $4 > -2$</td>
                            <td>...............................</td>
                            <td>...........................................................................</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="answer-key-box">
                <h4>🔑 مفتاح الإجابة لمعمل الجبر:</h4>
                <p>1. <strong>صحيحة</strong> (لأن 5 أولي صحيحة، والرابط "أو" يكفيه صواب أحد الأمرين).<br>
                2. <strong>صحيحة</strong> (لأن كلتا العبارتين صحيحتان مع الرابط "و").<br>
                3. <strong>صحيحة</strong> (لأن $11 > 5$ صحيحة مع الرابط "أو").<br>
                4. <strong>خاطئة</strong> (لأن $3 > 7$ خاطئة والرابط "و" يتطلب صواب العبارتين معاً).<br>
                5. <strong>خاطئة</strong> (لأن $5 > 10$ خاطئة والرابط "و" يجعل المركبة خاطئة).</p>
            </div>
        </article>

        <!-- ورقة عمل الدرس 4-4 -->
        <article class="worksheet-paper page-break" id="ws-4-4">
            <div class="ws-header">
                <div>المملكة العربية السعودية<br>وزارة التعليم - مادة الرياضيات</div>
                <div class="ws-header-center">
                    <h3>ورقة عمل تقويمية: الدرس (4-4) حل المتباينات المركبة</h3>
                    <small>الصف: الثالث المتوسط | كتاب الطالب ص 143 – 147</small>
                </div>
                <div>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</div>
            </div>

            <div class="ws-meta-bar">
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>التاريخ: .... / .... / 2026م</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [4 درجات]</div>
                <p><strong>1) مجموعة حل المتباينة المركبة: $س < 2 \text{ و } س > 6$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ س \mid 2 < س < 6 \}$</div>
                    <div class="mcq-option-line">ب) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ج) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">د) $س = 4$</div>
                </div>

                <p><strong>2) حل المتباينة المركبة: $-2 \le س - 3 < 5$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $1 \le س < 8$</div>
                    <div class="mcq-option-line">ب) $-5 \le س < 2$</div>
                    <div class="mcq-option-line">ج) $1 < س \le 8$</div>
                    <div class="mcq-option-line">د) $-1 \le س < 8$</div>
                </div>

                <p><strong>3) "سرعة المركبة لا تقل عن 70 ولا تزيد عن 110 كم/س"، يعبر عنها بالمتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $70 < ع < 110$</div>
                    <div class="mcq-option-line">ب) $70 \le ع \le 110$</div>
                    <div class="mcq-option-line">ج) $ع \le 70 \text{ أو } ع \ge 110$</div>
                    <div class="mcq-option-line">د) $ع > 110$</div>
                </div>

                <p><strong>4) التمثيل البياني للمتباينة المركبة $س \le 1 \text{ أو } س > 4$ يتكون من:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) قطعة مستقيمة واصلة بين 1 و 4</div>
                    <div class="mcq-option-line">ب) شعاعين في اتجاهين متعاكسين</div>
                    <div class="mcq-option-line">ج) نقطتين مظللتين فقط</div>
                    <div class="mcq-option-line">د) تظليل خط الأعداد بالكامل</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: مثل كلاً من المتباينات المركبة الآتية بيانيا على خط الأعداد: [3 درجات]</div>
                <p>1. $-3 < س \le 2$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
                <p style="margin-top:14px;">2. $ص \le -2 \text{ أو } ص > 3$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة المركبة التالية، واكتب مجموعة الحل: [3 درجات]</div>
                <p style="text-align:center; font-size:1.15rem; font-weight:bold; margin:10px 0;">$-7 \le 2س + 1 < 9$</p>
                <p>خطوات الحل: ................................................................................................................</p>
                <p>مجموعة الحل: .................................................................................................................</p>
            </div>

            <div class="answer-key-box">
                <h4>🔑 مفتاح الإجابة النموذجي (ورقة عمل 4-4):</h4>
                <p><strong>السؤال الأول:</strong> 1) ج ($\emptyset$ لعدم وجود تقاطع) | 2) أ ($1 \le س < 8$ بإضافة $+3$) | 3) ب ($70 \le ع \le 110$) | 4) ب (شعاعين متعاكسين).</p>
                <p><strong>السؤال الثاني:</strong> 1. دائرة مفتوحة عند $-3$ ومغلقة عند $2$ وتظليل بينهما. | 2. دائرة مغلقة عند $-2$ وسهم لليسار، ودائرة مفتوحة عند $3$ وسهم لليمين.</p>
                <p><strong>السؤال الثالث:</strong> بطرح 1 من الأطراف: $-8 \le 2س < 8$. بالقسمة على 2: $-4 \le س < 4$. مجموعة الحل: $\{ س \mid -4 \le س < 4 \}$.</p>
            </div>
        </article>
    </section>

</div>

<footer style="text-align:center; padding:24px; color:var(--gray-600); font-size:0.9rem; border-top:1px solid var(--gray-200); background:white;">
    تصميم خبير التعليم وفق منهجية STEM والمعايير المعتمدة لوزارة التعليم 2026 | رياضيات الصف الثالث المتوسط
</footer>

</body>
</html>
"""

output_path = r"c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\الحقيبة_الشاملة_المتباينات_الخطية_3م.html"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Master HTML created successfully at:", output_path)
