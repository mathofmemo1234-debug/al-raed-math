# -*- coding: utf-8 -*-
"""
Script to build the comprehensive Master HTML suite for Math 3M (pages 130-147).
Features:
- 100% Valid LaTeX Math without escape corruption (fixes Math input error).
- School logo & name: منصة الرائد التعليمية on every worksheet and student summary.
- Dedicated 'إظهار الحل النموذجي' button on each worksheet with interactive toggle.
- Teacher name & signature at the bottom left of every sheet and summary.
- Sequential layout: Plans together, Summaries together, Worksheets together.
- Complete coverage of Lessons 4-2, 4-3, Mid-Chapter Quiz (p. 141), Lab (p. 142), and Lesson 4-4.
"""

import os

# We build the HTML components cleanly
parts = []

parts.append(r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة الشاملة: المتباينات الخطية | منصة الرائد التعليمية</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <!-- MathJax 3 Configuration -->
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

        /* School Official Header Block (Used in Summaries & Worksheets) */
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
            font-size: 1.02rem;
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
            width: 70px;
            height: 70px;
        }

        .sch-info-left {
            text-align: left;
            font-size: 0.88rem;
            font-weight: 700;
            line-height: 1.5;
            color: #1e293b;
            direction: ltr;
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

        /* Bottom Left Teacher Name / Signature Block */
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
                display: block !important; /* Always print solutions in hardcopy if printed */
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
        🏫 منصة الرائد التعليمية | المتباينات الخطية (ص 130 - 147)
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
        <span class="hero-tag">المملكة العربية السعودية | وزارة التعليم 2026</span>
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: المتباينات الخطية</h1>
        <p class="hero-subtitle">
            <strong>منصة الرائد التعليمية</strong> — حقيبة موحدة تضم: خطط التدريس وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية بأزرار إظهار الحل النموذجي، مع التغطية التامة للصفحات 130 إلى 147 من كتاب الرياضيات للصف الثالث المتوسط.
        </p>
    </header>
''')

# Official School Header SVG component
school_header_html = r'''
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بجدة</div>
        <div class="school-highlight">منصة الرائد التعليمية</div>
        <div>قسم الرياضيات | المرحلة المتوسطة</div>
    </div>
    <div class="sch-logo-center">
        <!-- Official Advanced Schools Vector Crest Emblem -->
        <svg class="sch-logo-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="46" fill="url(#grad_bg)" stroke="#1e3a8a" stroke-width="3"/>
            <path d="M50 18 L76 32 V54 C76 68 50 82 50 82 C50 82 24 68 24 54 V32 L50 18 Z" fill="#ffffff" stroke="#0d9488" stroke-width="2.5"/>
            <!-- Book of knowledge -->
            <path d="M34 58 C40 54 46 55 50 58 C54 55 60 54 66 58 V40 C60 36 54 37 50 40 C46 37 40 36 34 40 V58 Z" fill="#1e3a8a"/>
            <!-- Graduation Cap / Smart Tech Leaf -->
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
        <div>مادة: الرياضيات (3م)</div>
        <div>الفصل الدراسي الثاني 2026م</div>
        <div>ورقة عمل وتقويم ختامي</div>
        <div style="color:#0d9488;">معتمدة وفق معايير STEM</div>
    </div>
</div>
'''

# Footer Signature Component
def make_footer_signature():
    return r'''
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>منصة الرائد التعليمية | رؤية المملكة 2030</span>
    </div>
    <div class="sheet-footer-left">
        <div class="teacher-signature-card">
            <span class="teacher-sig-label">إعداد معلم المادة / الأستاذ:</span>
            <span class="teacher-sig-name" contenteditable="true" title="انقر لتعديل الاسم مباشرة">....................................................</span>
            <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
        </div>
    </div>
</div>
'''

# =========================================================================
# SECTION 1: PLANS
# =========================================================================
parts.append(r'''
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
                <h3><span>1️⃣</span> خطة الدرس (4-2): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص 130 – 134</span>
            </div>

            <h4>1. الأهداف والمعايير والمجال (SMART):</h4>
            <p><strong>المجال:</strong> الأعداد والعمليات والجبر | <strong>المعيار:</strong> حل متباينات الخطوة الواحدة باستخدام الضرب والقسمة والتمثيل البياني.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>الهدف 1:</strong> أن يحل الطالب متباينات خطية تتضمن الضرب في عدد موجب أو سالب بخطوات جبرية صحيحة بنسبة إتقان 100%.</li>
                <li><strong>الهدف 2:</strong> أن يطبق الطالب خاصية القسمة على المتباينات مع عكس اتجاه رمز التباين عند القسمة على عدد سالب دون أي خطأ.</li>
                <li><strong>الهدف 3:</strong> أن ينمذج الطالب مسألة شراء واقعية في صورة متباينة خطية ويحلها ويتحقق من معقولية الحل.</li>
            </ul>

            <h4 style="margin-top:16px;">2. مرحلة الانخراط والتركيز (الربط المعرفي):</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>الحقبنة:</strong> "إذا كان $8 > 4$ وضاعفنا المقدارين ثلاث مرات تصبح $24 > 12$. ماذا لو عكسنا الموقف وخسر كل طرف ضعفي ما يملك (الضرب في $-2$)? كيف يصبح وضع الكفتين في المقارنة على خط الأعداد؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> نشاط الميزان ذي الكفتين؛ حل المعادلة: $-3\text{س} = 15$. ما العملية المعاكسة وما إشارة المعامل؟</li>
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

            <h4 style="margin-top:16px;">3. بيئة التعلم (3 قواعد صفية حاسمة):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فحص إشارة المعامل أولاً:</strong> قبل إجراء الضرب أو القسمة، يفحص الطالب إشارة العدد المضروب فيه أو المقسوم عليه.</li>
                <li><strong>قاعدة التمثيل الفوري:</strong> كل حل جبري يُترجم مباشرة إلى نقطة مغلقة/مفتوحة وسهم اتجاه على خط الأعداد.</li>
                <li><strong>قاعدة التعويض الاستكشافي:</strong> التحقق من صحة الحل باختيار عدد من منطقة الحل وتجريبه في المتباينة الأصلية.</li>
            </ol>

            <h4 style="margin-top:16px;">4. استراتيجيات التعلم النشط وتطوير المحتوى:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>العصف الذهني:</strong> استكشاف تحول $2 < 5$ عند الضرب في $-3$ إلى $-6 > -15$، واستنتاج حتمية قلب الرمز لحفظ الصدق الرياضي.</li>
                <li><strong>فكر - زاوج - شارك:</strong> حل المتباينة $-\frac{3}{7}\text{ر} \le 21$ (مثال 2 ص 132) بالضرب في المعكوس الضربي $(-\frac{7}{3})$ وقلب الرمز ليكون $\text{ر} \ge -49$.</li>
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
                    <p>• $-2\text{س} < 10 \implies \text{س} > -5$<br>• $-\frac{1}{3}\text{ص} \ge 4 \implies \text{ص} \le -12$<br>• $-5 > -8 \implies 5 < 8$ (ضرب في $-1$)</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة (أخطاء شائعة)</h4>
                    <p>• $3\text{س} < -15 \implies \text{س} > -5$ ❌ (المقسوم عليه موجب فلا نقلب).<br>• $\text{س} - 4 < 7 \implies \text{س} > 11$ ❌ (الطرح والجمع لا يعكسان الرمز مطلقاً).</p>
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

            <h4 style="margin-top:16px;">6. منظومة التقويم:</h4>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $-\frac{2}{3}\text{ص} < 6 \implies \text{ص} > 6 \times (-\frac{3}{2}) \implies \text{ص} > -9$. مجموعة الحل: $\{ \text{ص} \mid \text{ص} > -9 \}$.</li>
                <li><strong>تقويم ختامي:</strong> جمعت دار نشر أكثر من 5500 ريال من بيع كتاب جديد ثمنه 15 ريالاً. المتباينة: $15\text{ن} > 5500 \implies \text{ن} > 366.67$؛ أقل عدد بيع هو $367$ نسخة.</li>
                <li><strong>الواجب المنزلي (MCQ):</strong> ما حل $-4\text{س} \le 28$؟ 
                    <br>أ) $\text{س} \le -7$ | <strong>ب) $\text{س} \ge -7$</strong> | ج) $\text{س} \ge 7$ | د) $\text{س} \le 7$ (الحل: ب، لعكس الإشارة بالقسمة على $-4$).</li>
            </ul>

            <h4 style="margin-top:16px;">7. الغلق والتحدي الإثرائي:</h4>
            <p><strong>سؤال التحدي:</strong> إذا علمت أن حل المتباينة $أ \cdot \text{س} \ge 20$ هو $\text{س} \le -5$، فما قيمة العدد $أ$؟ (الحل: $أ = -4$، وهو سالب حتماً لقلب إشارة التباين).</p>
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
                <li><strong>الحقبنة:</strong> "مندوب مبيعات يتقاضى راتباً ثابتاً 2500 ريال وعمولة 75 ريالاً لكل قطعة يبيعها. إذا أراد دخلاً شهرياً لا يقل عن 7000 ريال، فكم قطعة يلزمه بيعها؟ كيف نكتبها جبرياً؟ ($75\text{س} + 2500 \ge 7000$) وما أول خطوة لحلها؟"</li>
                <li><strong>التمهيد والتقويم التشخيصي:</strong> حل المعادلة: $3(\text{س} - 2) + 4 = 19$. ما فائدة خاصية التوزيع في فك الأقواس؟</li>
            </ul>

            <h4 style="margin-top:16px;">3. بيئة التعلم (قواعد العمل الصفي):</h4>
            <ol style="margin: 8px 24px;">
                <li><strong>قاعدة فك الأقواس أولاً:</strong> لا يُجرى أي جمع أو طرح قبل التخلص من الأقواس عبر خاصية التوزيع.</li>
                <li><strong>قاعدة تجميع المتغير الأصغر:</strong> نقل الحد المتغير ذي المعامل الأصغر لتفادي التعامل مع المعاملات السالبة إن أمكن.</li>
                <li><strong>قاعدة رصد الحالات الخاصة:</strong> عندما ينحذف المتغير من الطرفين، التوقف فوراً لقراءة العبارة العددية المتبقية.</li>
            </ol>

            <h4 style="margin-top:16px;">4. الاستراتيجيات ومربع فراير:</h4>
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
                    <p>• $3\text{س} + 5 > 17$<br>• $2(\text{ص} - 4) \le 6\text{ص} + 10$<br>• $\frac{\text{ن} - 1}{3} \ge 4$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $\text{س} - 7 < 3$ (خطوة واحدة - جمع فقط).<br>• $-4\text{ص} \ge 20$ (خطوة واحدة - قسمة فقط).<br>• $2\text{س} + 3 = 11$ (معادلة وليست متباينة).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">5. التكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> حساب نقطة التعادل الإنتاجي بين آلتين؛ متى تكون تكلفة تشغيل الآلة الحديثة أقل من التقليدية بدلالة ساعات العمل: $150\text{س} + 2000 < 220\text{س} + 600 \implies \text{س} > 20$ ساعة.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $2(\text{ص} + 4) > 2\text{ص} + 10 \implies 2\text{ص} + 8 > 2\text{ص} + 10 \implies 8 > 10$ (خاطئة دائماً)، إذن الحل هو $\emptyset$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> حل المتباينة $3(\text{س} - 1) \le 3\text{س} + 4$ هو: 
                    <br>أ) $\emptyset$ | <strong>ب) مجموعة الأعداد الحقيقية $\mathbb{R}$</strong> | ج) $\text{س} \le 3$ | د) $\text{س} \ge -1$ (الحل: ب، لأن $-3 \le 4$ صحيحة دائماً).</li>
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
                    <p>• $-2 \le \text{س} + 1 < 5$<br>• $\text{ص} < -3 \text{ أو } \text{ص} \ge 2$<br>• $18 \le \text{الحرارة} \le 24$</p>
                </div>
                <div class="frayer-quadrant">
                    <h4>لا أمثلة</h4>
                    <p>• $3\text{س} + 4 > 10$ (متباينة بسيطة).<br>• $\text{س} = 2 \text{ أو } \text{س} = -1$ (معادلة وليست متباينة).<br>• $\text{س} < 5$ (أحادية الشرط).</p>
                </div>
            </div>

            <h4 style="margin-top:16px;">3. تكامل STEM والتقويم:</h4>
            <p><strong>تطبيق STEM:</strong> برمجة حساسات التكييف الذكية في المباني؛ ضبط درجة الحرارة الطبيعية بين $20^\circ\text{C}$ و $24^\circ\text{C}$ بمتباينة الوصل، وإطلاق جرس الإنذار إذا انخفضت عن $10^\circ\text{C}$ أو ارتفعت عن $35^\circ\text{C}$ بمتباينة الفصل.</p>
            <ul style="margin: 8px 24px;">
                <li><strong>تقويم بنائي:</strong> حل $-3 \le 2\text{س} + 1 < 7 \implies -4 \le 2\text{س} < 6 \implies -2 \le \text{س} < 3$. مجموعة الحل: $\{ \text{س} \mid -2 \le \text{س} < 3 \}$.</li>
                <li><strong>واجب منزلي (MCQ):</strong> مجموعة حل $\text{س} < 2 \text{ و } \text{س} > 5$ هي: 
                    <br>أ) $\{ \text{س} \mid 2 < \text{س} < 5 \}$ | <strong>ب) المجموعة الخالية $\emptyset$</strong> | ج) $\mathbb{R}$ | د) $\text{س} = 3$ (الحل: ب، لانعدام التقاطع).</li>
            </ul>
        </article>
    </section>
''')

# =========================================================================
# SECTION 2: SUMMARIES (WITH SCHOOL HEADER & TEACHER SIGNATURE)
# =========================================================================
parts.append(r'''
    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية) -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">منصة الرائد التعليمية</span>
        </div>
''')

# Summary 4-2
parts.append(r'''
        <!-- ملخص الدرس 4-2 -->
        <article class="unit-card" id="summary-4-2">
''' + school_header_html + r'''
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-2): حل المتباينات بالضرب أو بالقسمة</h3>
                <span class="page-range-pill">كتاب الطالب ص 130 - 134</span>
            </div>

            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4 style="color:#166534; margin-bottom:8px;">1. الضرب أو القسمة في عدد موجب (+)</h4>
                    <p><strong>يبقى اتجاه إشارة المتباينة كما هو دون أي تغيير:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ > 0$ فإن $أ \times جـ > ب \times جـ$</p>
                    <p>• مثال: $\frac{\text{س}}{3} < 5 \implies \text{س} < 15$</p>
                </div>
                <div class="rule-subcard negative">
                    <h4 style="color:#991b1b; margin-bottom:8px;">2. الضرب أو القسمة في عدد سالب (-)</h4>
                    <p><strong>يجب عكس اتجاه إشارة المتباينة فوراً:</strong></p>
                    <p>• إذا كان $أ > ب$ و $جـ < 0$ فإن $أ \times جـ < ب \times جـ$</p>
                    <p>• مثال: $-2\text{ص} \ge 8 \implies \text{ص} \le -4$</p>
                </div>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>تنبيه الاختبارات الحاسم:</strong> إشارة المتباينة تُعكس <u>فقط إذا كان المعامل المقسوم عليه أو المضروب فيه سالباً</u>، ولا نلتفت لإشارة الطرف الآخر! مثال: $3\text{س} \le -12 \implies \text{س} \le -4$ (لم نقلب لأن 3 موجبة).
            </div>

            <h4 style="margin-top:16px;">أمثلة الكتاب المحلولة خطوة بخطوة:</h4>
            <div style="background:#f8fafc; padding:16px; border-radius:8px; margin:10px 0; border-right:4px solid var(--primary);">
                <strong>مثال 1:</strong> حل المتباينة $-\frac{3}{7}\text{ر} < 21$
                <br>• نضرب الطرفين في المعكوس الضربي $(-\frac{7}{3})$ ونعكس إشارة $<$ إلى $>$:
                $$\text{ر} > 21 \times \left(-\frac{7}{3}\right) \implies \text{ر} > -49$$
                • مجموعة الحل: $\{ \text{ر} \mid \text{ر} > -49 \}$ (دائرة مفتوحة عند $-49$ وسهم لليمين).
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Summary 4-3
parts.append(r'''
        <!-- ملخص الدرس 4-3 -->
        <article class="unit-card page-break" id="summary-4-3">
''' + school_header_html + r'''
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-3): حل المتباينات متعددة الخطوات</h3>
                <span class="page-range-pill">كتاب الطالب ص 135 - 140</span>
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
                        <td>$\{ \text{س} \mid \text{س} \in \mathbb{R} \}$</td>
                        <td>خط الأعداد مظلل بالكامل بسهمين ممتدين</td>
                    </tr>
                </tbody>
            </table>
''' + make_footer_signature() + r'''
        </article>
''')

# Summary Mid-Quiz & Lab
parts.append(r'''
        <!-- ملخص مراجعة اختبار منتصف الفصل 4 ومعمل الجبر -->
        <article class="unit-card page-break" id="summary-mid-quiz">
''' + school_header_html + r'''
            <div class="unit-title-box">
                <h3><span>📖</span> مراجعة مركزة: اختبار منتصف الفصل ومعمل الجبر</h3>
                <span class="page-range-pill">كتاب الطالب ص 141 – 142</span>
            </div>
            <h4>المفاهيم المحورية لاختبار منتصف الفصل (ص 141):</h4>
            <ul style="margin: 8px 24px; line-height:1.9;">
                <li><strong>متباينات الجمع والطرح:</strong> $\text{س} - 5 > 3 \implies \text{س} > 8$.</li>
                <li><strong>متباينات الضرب والقسمة:</strong> المعامل السالب يقلب علامة التباين دائماً: $-\frac{2}{3}\text{س} < 8 \implies \text{س} > -12$.</li>
                <li><strong>المسائل اللفظية:</strong> "أكثر من" تعني $>$، "أقل من" تعني $<$، "لا يزيد على" تعني $\le$، و"لا يقل عن" تعني $\ge$.</li>
            </ul>

            <h4 style="margin-top:16px;">قواعد معمل الجبر: قراءة العبارات المركبة (ص 142):</h4>
            <div class="rule-card-grid">
                <div class="rule-subcard positive">
                    <h4>أداة الربط "و" (التقاطع ∩)</h4>
                    <p>• تكون <strong>صحيحة فقط</strong> إذا كانت كلتا العبارتين صحيحتين.</p>
                    <p>• مثال: $5 > 3 \text{ و } 2 < 7$ $\implies$ <strong>صحيحة</strong>.</p>
                </div>
                <div class="rule-subcard" style="background:#eff6ff; border-color:#3b82f6;">
                    <h4 style="color:#1d4ed8;">أداة الربط "أو" (الاتحاد ∪)</h4>
                    <p>• تكون <strong>صحيحة</strong> إذا كانت إحدى العبارتين على الأقل صحيحة.</p>
                    <p>• مثال: $5 > 3 \text{ أو } 8 < 2$ $\implies$ <strong>صحيحة</strong>.</p>
                </div>
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Summary 4-4
parts.append(r'''
        <!-- ملخص الدرس 4-4 -->
        <article class="unit-card page-break" id="summary-4-4">
''' + school_header_html + r'''
            <div class="unit-title-box">
                <h3><span>📖</span> ملخص الدرس (4-4): حل المتباينات المركبة</h3>
                <span class="page-range-pill">كتاب الطالب ص 143 – 147</span>
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
                        <td>غالباً جملة متصلة: $-3 \le \text{س} < 5$</td>
                        <td>جملتان منفصلتان بكلمة "أو": $\text{س} < 1 \text{ أو } \text{س} \ge 4$</td>
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
                <p><strong>تمثيل متباينة الوصل ( $-2 \le \text{س} < 4$ ):</strong> مغلقة عند $-2$ ومفتوحة عند $4$ والتظليل بينهما:</p>
                <svg class="nl-svg-container" viewBox="0 0 400 45">
                    <line x1="20" y1="20" x2="380" y2="20" stroke="#94a3b8" stroke-width="3" />
                    <line x1="120" y1="20" x2="280" y2="20" stroke="#0d9488" stroke-width="6" />
                    <circle cx="120" cy="20" r="6" fill="#0d9488" stroke="#042f2e" stroke-width="2" />
                    <text x="120" y="40" font-size="12" text-anchor="middle" font-weight="bold">-2</text>
                    <circle cx="280" cy="20" r="6" fill="#ffffff" stroke="#0d9488" stroke-width="2" />
                    <text x="280" y="40" font-size="12" text-anchor="middle" font-weight="bold">4</text>
                </svg>

                <p style="margin-top:12px;"><strong>تمثيل متباينة الفصل ( $\text{س} \le -1 \text{ أو } \text{س} > 3$ ):</strong> سهمان متعاكسان:</p>
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
''' + make_footer_signature() + r'''
        </article>
    </section>
''')

# =========================================================================
# SECTION 3: WORKSHEETS & QUIZZES (WITH SOLUTION TOGGLE BUTTONS)
# =========================================================================
parts.append(r'''
    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية مع أزرار إظهار الحل -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section page-break">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية (متتالية)</h2>
            <span class="section-badge">منصة الرائد التعليمية</span>
        </div>
''')

# Worksheet 4-2
parts.append(r'''
        <!-- ورقة عمل الدرس 4-2 -->
        <article class="worksheet-paper" id="ws-4-2">
''' + school_header_html + r'''
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (4-2) حل المتباينات بالضرب أو بالقسمة</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة من بين الخيارات التالية: [4 درجات]</div>
                
                <p><strong>1) حل المتباينة الجبرية: $3\text{س} < -21$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{س} < -7$</div>
                    <div class="mcq-option-line">ب) $\text{س} > -7$</div>
                    <div class="mcq-option-line">ج) $\text{س} < 7$</div>
                    <div class="mcq-option-line">د) $\text{س} > 7$</div>
                </div>

                <p><strong>2) ما مجموعة حل المتباينة: $-\frac{\text{ص}}{2} \ge 4$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ \text{ص} \mid \text{ص} \le -8 \}$</div>
                    <div class="mcq-option-line">ب) $\{ \text{ص} \mid \text{ص} \ge -8 \}$</div>
                    <div class="mcq-option-line">ج) $\{ \text{ص} \mid \text{ص} \le 8 \}$</div>
                    <div class="mcq-option-line">د) $\{ \text{ص} \mid \text{ص} \ge 8 \}$</div>
                </div>

                <p><strong>3) عند قسمة طرفي متباينة صحيحة على عدد حقيقي سالب فإن إشارة المتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) تبقى كما هي دون تغيير</div>
                    <div class="mcq-option-line">ب) تتحول إلى إشارة مساواة</div>
                    <div class="mcq-option-line">ج) يتعين تغيير اتجاهها فوراً</div>
                    <div class="mcq-option-line">د) تصبح القيمة مساوية للصفر</div>
                </div>

                <p><strong>4) وفر راشد أكثر من 300 ريال لشراء كتب سعر الكتاب الواحد 25 ريالاً. المتباينة التي تمثل عدد الكتب ($\text{ك}$) هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $25\text{ك} < 300$</div>
                    <div class="mcq-option-line">ب) $25\text{ك} > 300$</div>
                    <div class="mcq-option-line">ج) $\text{ك} + 25 \ge 300$</div>
                    <div class="mcq-option-line">د) $\frac{\text{ك}}{25} \le 300$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع إشارة (✓) أمام العبارة الصحيحة وإشارة (✗) أمام العبارة الخاطئة: [3 درجات]</div>
                <p>1. ( &nbsp;&nbsp;&nbsp; ) حل المتباينة $-5\text{س} \ge 35$ هو $\text{س} \ge -7$.</p>
                <p>2. ( &nbsp;&nbsp;&nbsp; ) التمثيل البياني لـ $\text{س} \le 6$ يتم برسم دائرة مغلقة وسهم متجه لليسار.</p>
                <p>3. ( &nbsp;&nbsp;&nbsp; ) ضرب طرفي المتباينة في الكسر الموجب $\frac{1}{3}$ يقتضي عكس اتجاه المتباينة.</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية، ومثل مجموعة الحل بيانياً على خط الأعداد: [3 درجات]</div>
                <p style="text-align:center; font-size:1.2rem; font-weight:bold; margin:10px 0;">$-\frac{4}{5}\text{م} \le 20$</p>
                <p>خطوات الحل الجبري: ............................................................................................................</p>
                <p>مجموعة الحل بالصفة المميزة: .................................................................................................</p>
                <p>التمثيل البياني: <br>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <!-- Dedicated Solution Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-2', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (4-2)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-2" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي وتوزيع الدرجات (ورقة عمل 4-2):</h4>
                <p><strong>السؤال الأول (4 درجات):</strong> 1) أ ($\text{س} < -7$) | 2) أ ($\{ \text{ص} \mid \text{ص} \le -8 \}$) | 3) ج (يتعين تغيير اتجاهها) | 4) ب ($25\text{ك} > 300$). [درجة لكل فقرة]</p>
                <p><strong>السؤال الثاني (3 درجات):</strong> 1) ( ✗ ) الصواب $\text{س} \le -7$ لعكس الإشارة عند القسمة على $-5$. | 2) ( ✓ ). | 3) ( ✗ ) الضرب في موجب لا يعكس الإشارة. [درجة لكل فقرة]</p>
                <p><strong>السؤال الثالث (3 درجات):</strong> نضرب في المعكوس الضربي $(-\frac{5}{4})$ ونعكس الرمز: $\text{م} \ge 20 \times (-\frac{5}{4}) \implies \text{م} \ge -25$ [درجتان]. مجموعة الحل: $\{ \text{م} \mid \text{م} \ge -25 \}$. التمثيل: دائرة مغلقة عند $-25$ وسهم مظلل لليمين [درجة].</p>
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Worksheet 4-3
parts.append(r'''
        <!-- ورقة عمل الدرس 4-3 -->
        <article class="worksheet-paper page-break" id="ws-4-3">
''' + school_header_html + r'''
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (4-3) حل المتباينات متعددة الخطوات</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [4 درجات]</div>
                <p><strong>1) أول خطوة صحيحة للبدء في حل المتباينة $4\text{س} - 5 > 19$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) القسمة على 4</div>
                    <div class="mcq-option-line">ب) إضافة 5 للطرفين</div>
                    <div class="mcq-option-line">ج) طرح 5 من الطرفين</div>
                    <div class="mcq-option-line">د) ضرب الطرفين في 4</div>
                </div>

                <p><strong>2) حل المتباينة: $-3\text{س} + 7 \le 22$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\text{س} \le -5$</div>
                    <div class="mcq-option-line">ب) $\text{س} \ge -5$</div>
                    <div class="mcq-option-line">ج) $\text{س} \ge 5$</div>
                    <div class="mcq-option-line">د) $\text{س} \le 5$</div>
                </div>

                <p><strong>3) ما مجموعة حل المتباينة: $2(\text{س} + 3) > 2\text{س} + 11$؟</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $\text{س} > 5$</div>
                    <div class="mcq-option-line">د) $\text{س} < 8$</div>
                </div>

                <p><strong>4) حل المتباينة: $5(\text{ص} - 1) \le 5\text{ص} + 2$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) مجموعة الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ب) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">ج) $\text{ص} \ge 0$</div>
                    <div class="mcq-option-line">د) $\text{ص} \le -3$</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: اكتب نوع مجموعة الحل (قيمة محددة / $\emptyset$ / $\mathbb{R}$): [3 درجات]</div>
                <p>1. المتباينة: $3(\text{س} - 2) \ge 3\text{س} + 5$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>2. المتباينة: $4(\text{ن} + 2) > 4\text{ن} - 3$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
                <p>3. المتباينة: $2\text{هـ} + 9 < 15$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; نوع مجموعة الحل: ( ................................... )</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة التالية موضحاً خطوات التوزيع والتبسيط: [3 درجات]</div>
                <p style="text-align:center; font-size:1.2rem; font-weight:bold; margin:10px 0;">$3(\text{ت} + 2) - 5\text{ت} \ge -6$</p>
                <p>خطوة 1 (خاصية التوزيع): .....................................................................................................</p>
                <p>خطوة 2 (تجميع الحدود وعزل المتغير): ......................................................................................</p>
                <p>مجموعة الحل النهائية: ............................................................................................................</p>
            </div>

            <!-- Dedicated Solution Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-3', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (4-3)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-3" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي وتوزيع الدرجات (ورقة عمل 4-3):</h4>
                <p><strong>السؤال الأول (4 درجات):</strong> 1) ب (إضافة 5) | 2) ب ($\text{س} \ge -5$ لأن $-3\text{س} \le 15$) | 3) ب ($\emptyset$ لأن $6 > 11$ مستحيلة) | 4) أ ($\mathbb{R}$ لأن $-5 \le 2$ صحيحة دائماً).</p>
                <p><strong>السؤال الثاني (3 درجات):</strong> 1. $\emptyset$ (لأن $-6 \ge 5$ خاطئة) | 2. $\mathbb{R}$ (لأن $8 > -3$ صائبة دائماً) | 3. قيمة محددة ($\text{هـ} < 3$).</p>
                <p><strong>السؤال الثالث (3 درجات):</strong> $3\text{ت} + 6 - 5\text{ت} \ge -6 \implies -2\text{ت} + 6 \ge -6 \implies -2\text{ت} \ge -12 \implies \text{ت} \le 6$ (قلبنا الإشارة بالقسمة على $-2$). الحل: $\{ \text{ت} \mid \text{ت} \le 6 \}$.</p>
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Worksheet Mid-Quiz (p. 141)
parts.append(r'''
        <!-- اختبار منتصف الفصل 4 (ص 141) -->
        <article class="worksheet-paper page-break" id="ws-mid-quiz">
''' + school_header_html + r'''
            <div class="ws-meta-bar">
                <span>اختبار منتصف الفصل الرابع (الدروس 4-1 إلى 4-3) - ص 141</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الزمن: 35 دقيقة</span>
                <span>الدرجة الكلية: [ &nbsp;&nbsp;&nbsp; / 15 ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 1: متباينات الجمع والطرح (حل ومثل بيانياً على خط الأعداد): [3 درجات]</div>
                <p><strong>1) $\text{س} - 8 < 4$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>2) $\text{م} + 2 \ge 6$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ........................................... &nbsp;&nbsp;&nbsp;&nbsp; التمثيل: &lt;---|---|---|---|---|---|---&gt;</p>
                <p><strong>3) مدينة الألعاب (سؤال 5 ص 141):</strong> مع حمزة 60 ريالاً، دفع منها 10 ريالات تذكرة دخول. اكتب متباينة تبين المبلغ ($\text{س}$) الذي يمكن لحمزة إنفاقه داخل المدينة ثم حلها.<br>
                المتباينة والحل: ................................................................................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 2: متباينات الضرب والقسمة (حل وتحقق من صحة الحل): [4 درجات]</div>
                <p><strong>4) $\frac{1}{3}\text{ص} \le 5$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>5) $-8\text{س} < 24$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>6) $-9\text{ر} \le -45$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>7) $\frac{\text{و}}{6} > -3$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">الجزء 3: متباينات متعددة الخطوات وتطبيقاتها: [5 درجات]</div>
                <p><strong>8) $4\text{أ} - 2 < 14$</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>9) $2\text{س} + 11 \le 5\text{س} - 10$</strong></p>
                <p>الحل: ................................................... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; الحل: ...................................................</p>
                <p><strong>10) $-2(4\text{ب} + 1) < -3\text{ب} + 8$</strong><br>
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

            <!-- Dedicated Solution Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-mid', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لاختبار منتصف الفصل (ص 141)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-mid" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 نموذج الإجابة وتوزيع الدرجات المعتمد لاختبار منتصف الفصل:</h4>
                <p>1) $\text{س} < 12$ [درجة]. | 2) $\text{م} \ge 4$ [درجة]. | 3) $\text{س} + 10 \le 60 \implies \text{س} \le 50$ ريالاً [درجة].</p>
                <p>4) $\text{ص} \le 15$ [درجة]. | 5) $\text{س} > -3$ لعكس الرمز بالقسمة على سالب [درجة]. | 6) $\text{ر} \ge 5$ لعكس الرمز [درجة]. | 7) $\text{و} > -18$ [درجة].</p>
                <p>8) $4\text{أ} < 16 \implies \text{أ} < 4$ [1.5 درجة]. | 9) $11 + 10 \le 5\text{س} - 2\text{س} \implies 21 \le 3\text{س} \implies \text{س} \ge 7$ [1.5 درجة]. | 10) $-8\text{ب} - 2 < -3\text{ب} + 8 \implies -5\text{ب} < 10 \implies \text{ب} > -2$ [درجتان].</p>
                <p>11) <strong>الخيار الصحيح هو: ب) أكثر من 38 ريالاً</strong>، لأن $\text{س} + 52 > 90 \implies \text{س} > 38$ [3 درجات].</p>
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Worksheet Lab (p. 142)
parts.append(r'''
        <!-- ورقة تدريب معمل الجبر (ص 142) -->
        <article class="worksheet-paper page-break" id="ws-lab">
''' + school_header_html + r'''
            <div class="ws-meta-bar">
                <span>ورقة تدريب استكشافية: معمل الجبر (قراءة العبارات المركبة) ص 142</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / 5 ]</span>
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

            <!-- Dedicated Solution Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-lab', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لتدريب معمل الجبر
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-lab" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة لمعمل الجبر (ص 142):</h4>
                <p>1. <strong>صحيحة</strong> (لأن 5 أولي صحيحة، والرابط "أو" يكفيه صواب أحد الأمرين).<br>
                2. <strong>صحيحة</strong> (لأن كلتا العبارتين صحيحتان مع الرابط "و").<br>
                3. <strong>صحيحة</strong> (لأن $11 > 5$ صحيحة مع الرابط "أو").<br>
                4. <strong>خاطئة</strong> (لأن $3 > 7$ خاطئة والرابط "و" يتطلب صواب العبارتين معاً).<br>
                5. <strong>خاطئة</strong> (لأن $5 > 10$ خاطئة والرابط "و" يجعل المركبة خاطئة).</p>
            </div>
''' + make_footer_signature() + r'''
        </article>
''')

# Worksheet 4-4
parts.append(r'''
        <!-- ورقة عمل الدرس 4-4 -->
        <article class="worksheet-paper page-break" id="ws-4-4">
''' + school_header_html + r'''
            <div class="ws-meta-bar">
                <span>ورقة عمل تقويمية: الدرس (4-4) حل المتباينات المركبة (ص 143 – 147)</span>
                <span>اسم الطالب: ..............................................................</span>
                <span>الشعبة: .............</span>
                <span>الدرجة: [ &nbsp;&nbsp;&nbsp; / 10 ]</span>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [4 درجات]</div>
                <p><strong>1) مجموعة حل المتباينة المركبة: $\text{س} < 2 \text{ و } \text{س} > 6$ هي:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $\{ \text{س} \mid 2 < \text{س} < 6 \}$</div>
                    <div class="mcq-option-line">ب) جميع الأعداد الحقيقية $\mathbb{R}$</div>
                    <div class="mcq-option-line">ج) المجموعة الخالية $\emptyset$</div>
                    <div class="mcq-option-line">د) $\text{س} = 4$</div>
                </div>

                <p><strong>2) حل المتباينة المركبة: $-2 \le \text{س} - 3 < 5$ هو:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $1 \le \text{س} < 8$</div>
                    <div class="mcq-option-line">ب) $-5 \le \text{س} < 2$</div>
                    <div class="mcq-option-line">ج) $1 < \text{س} \le 8$</div>
                    <div class="mcq-option-line">د) $-1 \le \text{س} < 8$</div>
                </div>

                <p><strong>3) "سرعة المركبة لا تقل عن 70 ولا تزيد عن 110 كم/س"، يعبر عنها بالمتباينة:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) $70 < \text{ع} < 110$</div>
                    <div class="mcq-option-line">ب) $70 \le \text{ع} \le 110$</div>
                    <div class="mcq-option-line">ج) $\text{ع} \le 70 \text{ أو } \text{ع} \ge 110$</div>
                    <div class="mcq-option-line">د) $\text{ع} > 110$</div>
                </div>

                <p><strong>4) التمثيل البياني للمتباينة المركبة $\text{س} \le 1 \text{ أو } \text{س} > 4$ يتكون من:</strong></p>
                <div class="mcq-options-vertical">
                    <div class="mcq-option-line">أ) قطعة مستقيمة واصلة بين 1 و 4</div>
                    <div class="mcq-option-line">ب) شعاعين في اتجاهين متعاكسين</div>
                    <div class="mcq-option-line">ج) نقطتين مظللتين فقط</div>
                    <div class="mcq-option-line">د) تظليل خط الأعداد بالكامل</div>
                </div>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: مثل كلاً من المتباينات المركبة الآتية بيانيا على خط الأعداد: [3 درجات]</div>
                <p>1. $-3 < \text{س} \le 2$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
                <p style="margin-top:14px;">2. $\text{ص} \le -2 \text{ أو } \text{ص} > 3$</p>
                <p>&lt;---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---&gt;</p>
            </div>

            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينة المركبة التالية، واكتب مجموعة الحل: [3 درجات]</div>
                <p style="text-align:center; font-size:1.2rem; font-weight:bold; margin:10px 0;">$-7 \le 2\text{س} + 1 < 9$</p>
                <p>خطوات الحل: ................................................................................................................</p>
                <p>مجموعة الحل: .................................................................................................................</p>
            </div>

            <!-- Dedicated Solution Button -->
            <div class="solution-btn-container">
                <button type="button" class="toggle-solution-btn" onclick="toggleSolution('sol-ws-4-4', this)">
                    <span class="btn-icon">💡</span> إظهار الحل النموذجي لورقة العمل (4-4)
                </button>
            </div>

            <!-- Hidden Solution Box -->
            <div id="sol-ws-4-4" class="worksheet-solution-box" style="display: none;">
                <h4>🔑 مفتاح الإجابة النموذجي (ورقة عمل 4-4):</h4>
                <p><strong>السؤال الأول (4 درجات):</strong> 1) ج ($\emptyset$ لعدم وجود تقاطع) | 2) أ ($1 \le \text{س} < 8$ بإضافة $+3$) | 3) ب ($70 \le \text{ع} \le 110$) | 4) ب (شعاعين متعاكسين).</p>
                <p><strong>السؤال الثاني (3 درجات):</strong> 1. دائرة مفتوحة عند $-3$ ومغلقة عند $2$ وتظليل بينهما. | 2. دائرة مغلقة عند $-2$ وسهم لليسار، ودائرة مفتوحة عند $3$ وسهم لليمين.</p>
                <p><strong>السؤال الثالث (3 درجات):</strong> بطرح 1 من الأطراف: $-8 \le 2\text{س} < 8$. بالقسمة على 2: $-4 \le \text{س} < 4$. مجموعة الحل: $\{ \text{س} \mid -4 \le \text{س} < 4 \}$.</p>
            </div>
''' + make_footer_signature() + r'''
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
    منصة الرائد التعليمية | تصميم خبير التعليم وفق منهجية STEM والمعايير المعتمدة لوزارة التعليم 2026
</footer>

</body>
</html>
''')

# Assemble full HTML
full_html = "".join(parts)

out_file = r"c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\الحقيبة_الشاملة_المتباينات_الخطية_3م.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated successfully! File size:", os.path.getsize(out_file), "bytes")
