# -*- coding: utf-8 -*-
"""
Final Master Generator for Math 3M (pages 130 to 147)
Strict Requirements:
1. All in ONE single HTML file (الحقيبة_الشاملة_المتباينات_الخطية_3م.html).
2. Fix 'Math input error' completely: 100% valid LaTeX with raw strings, safe MathJax parsing.
3. School Logo + Name: "منصة الرائد التعليمية" on EVERY worksheet and student summary.
4. Dedicated 'إظهار الحل النموذجي' button on each worksheet with interactive toggle.
5. Teacher Name & Signature at the bottom-left of every worksheet and student summary.
6. Arabic Numerals Only (الأرقام العربية المشرقية: ٠، ١، ٢، ٣، ٤، ٥، ٦، ٧، ٨، ٩) in all text, math values, and headings.
7. Sequential order: All Plans first -> All Summaries second -> All Worksheets third.
8. Full coverage: Lesson 4-2, Lesson 4-3, Mid-Chapter Quiz (p. 141), Algebra Lab (p. 142), Lesson 4-4.
"""

import os
import sys

# We construct the HTML content with raw strings and exact Arabic numerals
html_code = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة الشاملة: المتباينات الخطية | منصة الرائد التعليمية</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <!-- MathJax 3 Configuration for Arabic Mathematics -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
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

        /* Official School Header Component (for Summaries & Worksheets) */
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

        .sch-logo-svg {
            width: 72px;
            height: 72px;
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
            gap: 10px;
            font-size: 0.95rem;
        }

        /* Dedicated Solution Toggle Button */
        .solution-btn-container {
            margin: 20px 0 12px;
            text-align: center;
        }

        .toggle-solution-btn {
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
        }

        .toggle-solution-btn:hover {
            background: linear-gradient(135deg, #0f766e, #115e59);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(13, 148, 136, 0.3);
        }

        .toggle-solution-btn.active {
            background: linear-gradient(135deg, #dc2626, #b91c1c);
        }

        /* Dedicated Solution Display Box */
        .worksheet-solution-box {
            background: #f0fdf4;
            border: 2px solid #22c55e;
            border-radius: var(--radius-md);
            padding: 20px;
            margin-top: 16px;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .worksheet-solution-box h4 {
            color: #166534;
            font-size: 1.1rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid #bbf7d0;
            padding-bottom: 6px;
        }

        /* Bottom-Left Teacher Signature Block */
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
            border-bottom: 2px dashed #93c5fd;
            padding-bottom: 2px;
            min-width: 190px;
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

        /* Print Settings */
        @media print {
            .sticky-nav { display: none !important; }
            .toggle-solution-btn { display: none !important; }
            body { background: white !important; padding: 0 !important; }
            .main-container { max-width: 100% !important; margin: 0 !important; padding: 0 !important; }
            .hero-banner { box-shadow: none !important; border-radius: 0 !important; margin-bottom: 20px !important; }
            .unit-card, .worksheet-paper { 
                box-shadow: none !important; 
                page-break-inside: avoid !important;
                margin-bottom: 25px !important;
            }
            .worksheet-solution-box {
                display: block !important;
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
        🏫 منصة الرائد التعليمية | المتباينات الخطية (ص ١٣٠ - ١٤٧)
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
            <strong>منصة الرائد التعليمية</strong> — حقيبة موحدة تضم: خطط التدريس وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية بأزرار إظهار الحل النموذجي، مكتوبة بالكامل بالأرقام العربية المعتمدة، وشاملة الصفحات من ١٣٠ إلى ١٤٧ من كتاب الرياضيات للصف الثالث المتوسط.
        </p>
    </header>

    <!-- ========================================================================= -->
    <!-- القسم الأول: خطط التدريس والتحضير وفق منهجية STEM (متتالية) -->
    <!-- ========================================================================= -->
    <section id="plans-section" class="master-section">
        <div class="section-header-banner plans">
            <h2>📑 القسم الأول: خطط التدريس والتحضير وفق معايير STEM السبعة (متتالية)</h2>
            <span class="section-badge">منصة الرائد التعليمية</span>
        </div>

        <!-- الخطة 1: الدرس 4-2 -->
        <article class="unit-card" id="plan-4-2">
            <div class="unit-title-box">
                <h3><span>١️⃣</span> خطة الدرس (٤-٢): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٣٠ – ١٣٤</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الأعداد والعمليات والجبر | <strong>المعيار:</strong> حل متباينات الخطوة الواحدة باستخدام الضرب والقسمة والتمثيل البياني.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينات خطية تتضمن الضرب في عدد موجب أو سالب بخطوات جبرية صحيحة بنسبة إتقان ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يطبق الطالب خاصية القسمة على المتباينات مع عكس اتجاه رمز التباين عند القسمة على عدد سالب دون أي خطأ.</li>
                <li><strong>الهدف ٣:</strong> أن ينمذج الطالب مسألة شراء واقعية في صورة متباينة خطية ويحلها ويتحقق من معقولية الحل.</li>
            </ul>

            <h4 style="margin-top:16px;">٢. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>الحقبنة:</strong> "إذا كان $\text{٨} > \text{٤}$ وضاعفنا المقدارين ثلاث مرات تصبح $\text{٢٤} > \text{١٢}$. ماذا لو عكسنا الموقف وخسر كل طرف ضعفي ما يملك (الضرب في $-\text{٢}$)? كيف يصبح وضع الكفتين في المقارنة على خط الأعداد؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> نشاط الميزان ذي الكفتين؛ حل المعادلة: $-\text{٣س} = \text{١٥}$. ما العملية المعاكسة وما إشارة المعامل؟</li>
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
                        <td>• حل المعادلات بالضرب والقسمة.<br>• حل المتباينات بالجمع والطرح.<br>• تمثيل المتباينة على خط الأعداد.</td>
                        <td>• كيف تؤثر الإشارة السالبة عند الضرب والقسمة؟<br>• متى ينعكس اتجاه رمز التباين؟<br>• كتابة مجموعة الحل بالصفة المميزة.</td>
                        <td>• عند الضرب أو القسمة في سالب نعكس الإشارة فوراً.<br>• الضرب في موجب يبقي الإشارة كما هي.<br>• الصفة المميزة: $\{ \text{س} \mid \text{س} > أ \}$.</td>
                    </tr>
                </tbody>
            </table>

            <h4 style="margin-top:16px;">٣. بيئة التعلم (٣ قواعد صفية حاسمة):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فحص إشارة المعامل أولاً:</strong> قبل إجراء الضرب أو القسمة، يفحص الطالب إشارة العدد المضروب فيه أو المقسوم عليه.</li>
                <li><strong>قاعدة التمثيل الفوري:</strong> كل حل جبري يُترجم مباشرة إلى نقطة مغلقة/مفتوحة وسهم اتجاه على خط الأعداد.</li>
                <li><strong>قاعدة التعويض الاستكشافي:</strong> التحقق من صحة الحل باختيار عدد من منطقة الحل وتجريبه في المتباينة الأصلية.</li>
            </ol>

            <h4 style="margin-top:16px;">٤. استراتيجيات التعلم النشط وتطوير المحتوى:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>العصف الذهني:</strong> استكشاف تحول $\text{٢} < \text{٥}$ عند الضرب في $-\text{٣}$ إلى $-\text{٦} > -\text{١٥}$، واستنتاج حتمية قلب الرمز لحفظ الصدق الرياضي.</li>
                <li><strong>فكر - زاوج - شارك:</strong> حل المتباينة $-\frac{\text{٣}}{\text{٧}}\text{ر} \le \text{٢١}$ (مثال ٢ ص ١٣٢) بالضرب في المعكوس الضربي $(-\frac{\text{٧}}{\text{٣}})$ وقلب الرمز ليكون $\text{ر} \ge -\text{٤٩}$.</li>
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
                    <p>• $-\text{٢س} < \text{١٠} \implies \text{س} > -\text{٥}$<br>• $-\frac{\text{١}}{\text{٣}}\text{ص} \ge \text{٤} \implies \text{ص} \le -\text{١٢}$<br>• $-\text{٥} > -\text{٨} \implies \text{٥} < \text{٨}$ (ضرب في $-\text{١}$)</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة (أخطاء شائعة)</h4>
                    <p>• $\text{٣س} < -\text{١٥} \implies \text{س} > -\text{٥}$ ❌ (المقسوم عليه موجب فلا نقلب).<br>• $\text{س} - \text{٤} < \text{٧} \implies \text{س} > \text{١١}$ ❌ (الطرح والجمع لا يعكسان الرمز مطلقاً).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">٥. التكامل مع منهجية STEM والواقع:</h4>
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

            <h4 style="margin-top:16px;">٦. منظومة التقويم:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $-\frac{\text{٢}}{\text{٣}}\text{ص} < \text{٦} \implies \text{ص} > \text{٦} \times (-\frac{\text{٣}}{\text{٢}}) \implies \text{ص} > -\text{٩}$. مجموعة الحل: $\{ \text{ص} \mid \text{ص} > -\text{٩} \}$.</li>
                <li><strong>تقويم ختامي:</strong> جمعت دار نشر أكثر من ٥٥٠٠ ريال من بيع كتاب جديد ثمنه ١٥ ريالاً. المتباينة: $\text{١٥ن} > \text{٥٥٠٠} \implies \text{ن} > \text{٣٦٦٫٦٧}$؛ أقل عدد بيع هو $\text{٣٦٧}$ نسخة.</li>
                <li><strong>الواجب المنزلي (MCQ):</strong> ما حل $-\text{٤س} \le \text{٢٨}$؟ 
                    <br>أ) $\text{س} \le -\text{٧}$ | <strong>ب) $\text{س} \ge -\text{٧}$</strong> | ج) $\text{س} \ge \text{٧}$ | د) $\text{س} \le \text{٧}$ (الحل: ب، لعكس الإشارة بالقسمة على $-\text{٤}$).</li>
            </ul>

            <h4 style="margin-top:16px;">٧. الغلق والتحدي الإثرائي:</h4>
            <p><strong>سؤال التحدي:</strong> إذا علمت أن حل المتباينة $أ \cdot \text{س} \ge \text{٢٠}$ هو $\text{س} \le -\text{٥}$، فما قيمة العدد $أ$؟ (الحل: $أ = -\text{٤}$، وهو سالب حتماً لقلب إشارة التباين).</p>
        </article>

        <!-- الخطة 2: الدرس 4-3 -->
        <article class="unit-card" id="plan-4-3">
            <div class="unit-title-box">
                <h3><span>٢️⃣</span> خطة الدرس (٤-٣): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٣٥ – ١٤٠</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار:</strong> حل متباينات خطية تتضمن عدة عمليات وخاصية التوزيع وتمييز الحالات الخاصة.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينات خطية متعددة الخطوات باتباع الترتيب المعكوس للعمليات بنسبة إتقان ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يطبق الطالب خاصية التوزيع لتجميع المتغيرات في طرف والثوابت في طرف بدقة لا تقل عن ٩٠٪.</li>
                <li><strong>الهدف ٣:</strong> أن يميز الطالب المتباينات التي حلها هو المجموعة الخالية $\emptyset$ وتلك التي حلها مجموعة الأعداد الحقيقية $\mathbb{R}$.</li>
            </ul>

            <h4 style="margin-top:16px;">٢. مرحلة الانخراط والتركيز:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>الحقبنة:</strong> "مندوب مبيعات يتقاضى راتباً ثابتاً ٢٥٠٠ ريال وعمولة ٧٥ ريالاً لكل قطعة يبيعها. إذا أراد دخلاً شهرياً لا يقل عن ٧٠٠٠ ريال، فكم قطعة يلزمه بيعها؟ كيف نكتبها جبرياً؟ ($\text{٧٥س} + \text{٢٥٠٠} \ge \text{٧٠٠٠}$) وما أول خطوة لحلها؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> حل المعادلة: $\text{٣}(\text{س} - \text{٢}) + \text{٤} = \text{١٩}$. ما فائدة خاصية التوزيع في فك الأقواس؟</li>
            </ul>

            <h4 style="margin-top:16px;">٣. بيئة التعلم (قواعد العمل الصفي):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فك الأقواس أولاً:</strong> لا يُجرى أي جمع أو طرح قبل التخلص من الأقواس عبر خاصية التوزيع.</li>
                <li><strong>قاعدة تجميع المتغير الأصغر:</strong> نقل الحد المتغير ذي المعامل الأصغر لتفادي التعامل مع المعاملات السالبة إن أمكن.</li>
                <li><strong>قاعدة رصد الحالات الخاصة:</strong> عندما ينحذف المتغير من الطرفين، التوقف فوراً لقراءة العبارة العددية المتبقية.</li>
            </ol>

            <h4 style="margin-top:16px;">٤. الاستراتيجيات ومربع فراير:</h4>
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
                    <p>• $\text{٣س} + \text{٥} > \text{١٧}$<br>• $\text{٢}(\text{ص} - \text{٤}) \le \text{٦ص} + \text{١٠}$<br>• $\frac{\text{ن} - \text{١}}{\text{٣}} \ge \text{٤}$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $\text{س} - \text{٧} < \text{٣}$ (خطوة واحدة - جمع فقط).<br>• $-\text{٤ص} \ge \text{٢٠}$ (خطوة واحدة - قسمة فقط).<br>• $\text{٢س} + \text{٣} = \text{١١}$ (معادلة وليست متباينة).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">٥. التكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> حساب نقطة التعادل الإنتاجي بين آلتين؛ متى تكون تكلفة تشغيل الآلة الحديثة أقل من التقليدية بدلالة ساعات العمل: $\text{١٥٠س} + \text{٢٠٠٠} < \text{٢٢٠س} + \text{٦٠٠} \implies \text{س} > \text{٢٠}$ ساعة.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $\text{٢}(\text{ص} + \text{٤}) > \text{٢ص} + \text{١٠} \implies \text{٢ص} + \text{٨} > \text{٢ص} + \text{١٠} \implies \text{٨} > \text{١٠}$ (خاطئة دائماً)، إذن الحل هو $\emptyset$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> حل المتباينة $\text{٣}(\text{س} - \text{١}) \le \text{٣س} + \text{٤}$ هو: 
                    <br>أ) $\emptyset$ | <strong>ب) مجموعة الأعداد الحقيقية $\mathbb{R}$</strong> | ج) $\text{س} \le \text{٣}$ | د) $\text{س} \ge -\text{١}$ (الحل: ب، لأن $-\text{٣} \le \text{٤}$ صحيحة دائماً).</li>
            </ul>
        </article>

        <!-- الخطة 3: اختبار منتصف الفصل 4 -->
        <article class="unit-card" id="plan-mid-quiz">
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
        <article class="unit-card" id="plan-lab">
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
        <article class="unit-card" id="plan-4-4">
            <div class="unit-title-box">
                <h3><span>٥️⃣</span> خطة الدرس (٤-٤): حل المتباينات المركبة</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٤٣ – ١٤٧</span>
            </div>

            <h4>١. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الجبر والدوال | <strong>المعيار:</strong> حل المتباينات المركبة (الوصل والفصل) وتمثيلها بيانياً ونمذجة ظواهر الواقع بها.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف ١:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "و" (تقاطع) ويمثل مجموعة حلها بدقة ١٠٠٪.</li>
                <li><strong>الهدف ٢:</strong> أن يحل الطالب متباينة مركبة تتضمن أداة الربط "أو" (اتحاد) ويمثلها بيانياً بالأسهم المتعاكسة أو الشاملة.</li>
                <li><strong>الهدف ٣:</strong> أن يصيغ الطالب متباينة مركبة تمثل موقفاً حياتياً (درجات الحرارة، أطوال الموجات، السرعات) بصورة صحيحة.</li>
            </ul>

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

            <h4 style="margin-top:16px;">٣. تكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> برمجة حساسات التكييف الذكية في المباني؛ ضبط درجة الحرارة الطبيعية بين $\text{٢٠}^\circ\text{C}$ و $\text{٢٤}^\circ\text{C}$ بمتباينة الوصل، وإطلاق جرس الإنذار إذا انخفضت عن $\text{١٠}^\circ\text{C}$ أو ارتفعت عن $\text{٣٥}^\circ\text{C}$ بمتباينة الفصل.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $-\text{٣} \le \text{٢س} + \text{١} < \text{٧} \implies -\text{٤} \le \text{٢س} < \text{٦} \implies -\text{٢} \le \text{س} < \text{٣}$. مجموعة الحل: $\{ \text{س} \mid -\text{٢} \le \text{س} < \text{٣} \}$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> مجموعة حل $\text{س} < \text{٢} \text{ و } \text{س} > \text{٥}$ هي: 
                    <br>أ) $\{ \text{س} \mid \text{٢} < \text{س} < \text{٥} \}$ | <strong>ب) المجموعة الخالية $\emptyset$</strong> | ج) $\mathbb{R}$ | د) $\text{س} = \text{٣}$ (الحل: ب، لانعدام التقاطع).</li>
            </ul>
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية) -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">منصة الرائد التعليمية</span>
        </div>

        <!-- ملخص الدرس 4-2 -->
        <article class="unit-card" id="summary-4-2">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                        <defs>
                            <linearGradient id="grad_bg" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#eff6ff" />
                                <stop offset="100%" stop-color="#ccfbf1" />
                            </linearGradient>
                        </defs>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ملخص الطالب المركز</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رؤية المملكة ٢٠٣٠</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ملخص الدرس 4-3 -->
        <article class="unit-card page-break" id="summary-4-3">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ملخص الطالب المركز</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رؤية المملكة ٢٠٣٠</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ملخص مراجعة اختبار منتصف الفصل 4 ومعمل الجبر -->
        <article class="unit-card page-break" id="summary-mid-quiz">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>مراجعة الاختبار والمعمل</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رؤية المملكة ٢٠٣٠</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ملخص الدرس 4-4 -->
        <article class="unit-card page-break" id="summary-4-4">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ملخص الطالب المركز</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رؤية المملكة ٢٠٣٠</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>
    </section>

    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية مع أزرار إظهار الحل -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section page-break">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية (متتالية)</h2>
            <span class="section-badge">منصة الرائد التعليمية</span>
        </div>

        <!-- ورقة عمل الدرس 4-2 -->
        <article class="worksheet-paper" id="ws-4-2">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ورقة عمل وتقويم بنائي</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رياضيات ٣م</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ورقة عمل الدرس 4-3 -->
        <article class="worksheet-paper page-break" id="ws-4-3">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ورقة عمل وتقويم بنائي</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رياضيات ٣م</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- اختبار منتصف الفصل 4 (ص 141) -->
        <article class="worksheet-paper page-break" id="ws-mid-quiz">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>اختبار منتصف الفصل ٤</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رياضيات ٣م</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ورقة تدريب معمل الجبر (ص 142) -->
        <article class="worksheet-paper page-break" id="ws-lab">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ورقة تدريب استكشافية</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رياضيات ٣م</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>

        <!-- ورقة عمل الدرس 4-4 -->
        <article class="worksheet-paper page-break" id="ws-4-4">
            <div class="school-official-header">
                <div class="sch-info-right">
                    <div class="ministry-name">المملكة العربية السعودية</div>
                    <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
                    <div class="school-highlight">منصة الرائد التعليمية</div>
                    <div>قسم الرياضيات | المرحلة المتوسطة</div>
                </div>
                <div class="sch-logo-center">
                    <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
                        <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
                        <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
                        <polygon points="50,26 64,33 50,40 36,33" fill="#f59e0b"/>
                        <circle cx="50" cy="48" r="3" fill="#0d9488"/>
                    </svg>
                    <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس التعلّم الذكي</span>
                </div>
                <div class="sch-info-left-ar">
                    <div>مادة: الرياضيات (٣م)</div>
                    <div>الفصل الدراسي الثاني ٢٠٢٦م</div>
                    <div>ورقة عمل وتقويم ختامي</div>
                    <div style="color:#0d9488;">معتمد وفق معايير STEM</div>
                </div>
            </div>

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

            <div class="sheet-footer-bar">
                <div class="sheet-footer-right">
                    <span>منصة الرائد التعليمية | رياضيات ٣م</span>
                </div>
                <div class="sheet-footer-left">
                    <div class="teacher-signature-card">
                        <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
                        <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
                        <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
                    </div>
                </div>
            </div>
        </article>
    </section>

</div>

<!-- Interactive JS Script for Solution Toggling -->
<script>
    function toggleSolution(id, btn) {
        var el = document.getElementById(id);
        if (!el) return;
        
        if (el.style.display === "none" || el.style.display === "") {
            el.style.display = "block";
            btn.innerHTML = '<span class="btn-icon">🔒</span> إخفاء الحل النموذجي';
            btn.classList.add("active");
            if (window.MathJax && window.MathJax.typesetPromise) {
                window.MathJax.typesetPromise([el]).catch(function (err) { console.log(err); });
            }
        } else {
            el.style.display = "none";
            btn.innerHTML = '<span class="btn-icon">💡</span> إظهار الحل النموذجي';
            btn.classList.remove("active");
        }
    }
</script>

<footer style="text-align:center; padding:24px; color:var(--gray-600); font-size:0.9rem; border-top:1px solid var(--gray-200); background:white;">
    منصة الرائد التعليمية | تصميم خبير التعليم وفق منهجية STEM والمعايير المعتمدة لوزارة التعليم ٢٠٢٦م
</footer>

</body>
</html>
'''

target_path = r"c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\الحقيبة_الشاملة_المتباينات_الخطية_3م.html"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Master file generated with 100% Arabic numerals & clean LaTeX! Size:", os.path.getsize(target_path), "bytes")
