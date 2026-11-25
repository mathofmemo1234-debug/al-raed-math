# -*- coding: utf-8 -*-
"""
generator_1s_header_styles.py: Provides HTML head, styles, school official header,
teacher footer, worksheet toolbar, and print logic for Grade 10 (1st Secondary - First Term - Paths).
Chapter 3: Congruent Triangles (المثلثات المتطابقة) pages 146 to 200.
Conforms strictly to English math symbols (LTR) and Arabic prose (RTL),
with high-precision geometric figures and full STEM integration.
"""
import base64
import os

logo_b64 = ""
if os.path.exists('شعار المتقدمة.png'):
    with open('شعار المتقدمة.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')

LOGO_DATA_URI = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""

HTML_START = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة التعليمية والتدريسية الشاملة: المثلثات المتطابقة (ص 146 – 200) | الصف الأول الثانوي | أ. محمد عبدالله جمعة | منصة الرائد التعليمية</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    
    <!-- MathJax 3 Configuration for Secondary Mathematics (English Symbols LTR inside Arabic RTL Context) -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['\\(', '\\)'], ['$', '$']],
                displayMath: [['\\[', '\\]'], ['$$', '$$']],
                processEscapes: true
            },
            options: {
                renderActions: {
                    addMenu: []
                }
            },
            chtml: {
                fontURL: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/output/chtml/fonts/woff-v2'
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
            --success: #16a34a;
            --success-light: #f0fdf4;
            --purple: #7c3aed;
            --purple-light: #f5f3ff;
            --dark: #0f172a;
            --gray-50: #f8fafc;
            --gray-100: #f1f5f9;
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
        }

        body {
            font-family: 'Tajawal', 'Cairo', sans-serif;
            background-color: #f1f5f9;
            color: var(--dark);
            line-height: 1.75;
            direction: rtl;
            text-align: right;
            padding-bottom: 60px;
        }

        .main-container {
            max-width: 1280px;
            margin: 0 auto;
            padding: 24px 20px;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #1e3a8a 0%, #1e1b4b 60%, #0f172a 100%);
            color: var(--white);
            border-radius: var(--radius-lg);
            padding: 36px 32px;
            margin-bottom: 24px;
            box-shadow: var(--shadow-lg);
            border: 1px solid rgba(255,255,255,0.1);
            position: relative;
            overflow: hidden;
        }

        .hero-banner::after {
            content: "△ ≅ △";
            position: absolute;
            left: 20px;
            top: 20px;
            font-size: 85px;
            font-weight: 900;
            color: rgba(255,255,255,0.04);
            pointer-events: none;
            font-family: serif;
        }

        .hero-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            color: #93c5fd;
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 14px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .hero-title {
            font-family: 'Cairo', sans-serif;
            font-size: 30px;
            font-weight: 900;
            margin-bottom: 12px;
            line-height: 1.3;
            color: #ffffff;
        }

        .hero-subtitle {
            font-size: 15px;
            color: #cbd5e1;
            line-height: 1.8;
            max-width: 1050px;
        }

        .hero-meta-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 18px;
        }

        .meta-pill {
            background: rgba(255,255,255,0.12);
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            color: #e2e8f0;
        }

        /* Sticky Navigation Bar */
        .sticky-nav {
            position: sticky;
            top: 12px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border-radius: var(--radius-md);
            padding: 10px 18px;
            margin-bottom: 28px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }

        .nav-brand {
            font-weight: 800;
            font-size: 14px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 8px;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            font-weight: 700;
            font-size: 13px;
            color: var(--gray-700);
            padding: 8px 14px;
            border-radius: var(--radius-sm);
            transition: all 0.2s ease;
        }

        .nav-links a:hover {
            background-color: var(--primary-light);
            color: var(--primary);
        }

        .print-btn-header {
            background-color: var(--primary);
            color: var(--white);
            border: none;
            border-radius: var(--radius-sm);
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: background-color 0.2s;
        }

        .print-btn-header:hover {
            background-color: var(--primary-dark);
        }

        /* Master Sections */
        .master-section {
            margin-bottom: 40px;
        }

        .section-header-banner {
            padding: 20px 24px;
            border-radius: var(--radius-md);
            margin-bottom: 24px;
            color: var(--white);
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
        }

        .section-header-banner.plans {
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        }

        .section-header-banner.summaries {
            background: linear-gradient(135deg, #0d9488 0%, #14b8a6 100%);
        }

        .section-header-banner.worksheets {
            background: linear-gradient(135deg, #7c3aed 0%, #9333ea 100%);
        }

        .section-header-banner h2 {
            font-family: 'Cairo', sans-serif;
            font-size: 20px;
            font-weight: 800;
            margin: 0;
        }

        .section-badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Unit Cards */
        .unit-card {
            background: var(--white);
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            box-shadow: var(--shadow-sm);
            padding: 24px;
            margin-bottom: 28px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .unit-card:hover {
            box-shadow: var(--shadow-md);
        }

        .unit-title-box {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 14px;
            border-bottom: 2px solid var(--gray-100);
            margin-bottom: 18px;
        }

        .unit-title-box h3 {
            font-family: 'Cairo', sans-serif;
            font-size: 18px;
            font-weight: 800;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .page-range-pill {
            background: var(--gray-100);
            color: var(--gray-700);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            border: 1px solid var(--gray-200);
        }

        /* 7 STEM Step Boxes */
        .plan-step-box {
            background: var(--gray-50);
            border-radius: var(--radius-sm);
            border-right: 4px solid var(--primary);
            padding: 16px 18px;
            margin-bottom: 16px;
        }

        .plan-step-box.engage {
            border-right-color: var(--accent);
            background: #fffbeb;
        }

        .plan-step-box.stem {
            border-right-color: var(--secondary);
            background: #f0fdfa;
        }

        .plan-step-box.eval {
            border-right-color: var(--purple);
            background: #f5f3ff;
        }

        .plan-step-box.closure {
            border-right-color: var(--success);
            background: #f0fdf4;
        }

        .plan-step-title {
            font-family: 'Cairo', sans-serif;
            font-weight: 800;
            font-size: 15px;
            color: var(--dark);
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* Tables */
        .data-table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
            font-size: 13px;
            background: var(--white);
            border-radius: var(--radius-sm);
            overflow: hidden;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        .data-table th, .data-table td {
            padding: 10px 12px;
            border: 1px solid var(--gray-200);
            text-align: right;
        }

        .data-table th {
            background-color: var(--gray-100);
            color: var(--primary);
            font-weight: 800;
        }

        .data-table tr:nth-child(even) td {
            background-color: var(--gray-50);
        }

        /* Two-column Proof Table */
        .proof-table {
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0;
            font-size: 13.5px;
            background: var(--white);
            border: 2px solid var(--primary);
            border-radius: var(--radius-sm);
            overflow: hidden;
        }

        .proof-table th {
            background-color: var(--primary);
            color: var(--white);
            padding: 10px 14px;
            font-weight: 800;
            text-align: center;
        }

        .proof-table td {
            padding: 10px 14px;
            border: 1px solid var(--gray-200);
            vertical-align: top;
        }

        .proof-col-stmt {
            width: 50%;
            border-left: 2px solid var(--primary);
            direction: ltr;
            text-align: left;
            font-family: 'Times New Roman', serif;
        }

        .proof-col-reason {
            width: 50%;
            direction: rtl;
            text-align: right;
            font-weight: 500;
        }

        /* Official School Header Bar */
        .official-header {
            background: var(--white);
            border: 2px solid var(--gray-200);
            border-radius: var(--radius-md);
            padding: 14px 18px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .header-ministry {
            font-size: 12px;
            font-weight: 700;
            line-height: 1.5;
            color: var(--gray-700);
        }

        .header-logo-box {
            text-align: center;
        }

        .header-logo-img {
            max-height: 60px;
            object-fit: contain;
        }

        .header-sheet-info {
            text-align: left;
            direction: ltr;
            font-size: 12px;
            color: var(--gray-700);
        }

        .header-sheet-info span {
            display: block;
            direction: rtl;
            text-align: right;
            font-weight: 600;
        }

        /* Student Metadata Form in Worksheets */
        .student-meta-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 12px;
            background: var(--gray-50);
            border: 1px dashed var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 10px 14px;
            margin-bottom: 18px;
            font-size: 13px;
        }

        .student-meta-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .meta-field-line {
            flex: 1;
            border-bottom: 1px dotted #94a3b8;
            height: 16px;
        }

        /* Worksheet Top Toolbar */
        .worksheet-top-toolbar {
            background: #fdf4ff;
            border: 1px solid #f0abfc;
            border-radius: var(--radius-sm);
            padding: 10px 14px;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }

        .btn-toggle-answers {
            background-color: var(--purple);
            color: var(--white);
            border: none;
            border-radius: var(--radius-sm);
            padding: 7px 14px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }

        .btn-toggle-answers:hover {
            background-color: #6d28d9;
        }

        .btn-toggle-answers.active {
            background-color: #4b5563;
        }

        .toolbar-hint {
            font-size: 12px;
            color: #86198f;
            font-weight: 600;
        }

        /* Questions & Question Blocks */
        .question-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-sm);
            padding: 16px;
            margin-bottom: 16px;
            position: relative;
        }

        .question-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .q-number-badge {
            background: var(--primary);
            color: var(--white);
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 800;
        }

        .q-dok-badge {
            background: var(--gray-100);
            color: var(--gray-600);
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
        }

        .q-body {
            font-size: 14.5px;
            line-height: 1.8;
            color: var(--dark);
            margin-bottom: 12px;
        }

        .mcq-options-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-top: 10px;
        }

        .mcq-option {
            background: var(--gray-50);
            border: 1px solid var(--gray-200);
            border-radius: 6px;
            padding: 8px 12px;
            font-size: 13.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .mcq-letter {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--white);
            border: 1.5px solid var(--primary);
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 800;
            flex-shrink: 0;
        }

        /* Teacher Hidden/Revealed Answer Box */
        .answer-box {
            display: none;
            background: #f0fdf4;
            border: 1.5px solid #86efac;
            border-radius: var(--radius-sm);
            padding: 12px 16px;
            margin-top: 14px;
            font-size: 13.5px;
            color: #14532d;
        }

        .show-answers .answer-box {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .answer-box-title {
            font-weight: 800;
            color: #15803d;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Geometry Visual Containers */
        .geometry-figure-container {
            margin: 14px 0;
            text-align: center;
            background: #ffffff;
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-sm);
            padding: 12px;
        }

        .figure-title {
            font-weight: 700;
            font-size: 13px;
            color: var(--primary);
            margin-bottom: 8px;
        }

        .svg-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: auto;
        }

        .geom-svg {
            max-width: 100%;
            height: auto;
            display: block;
        }

        /* Book Extracted Figure Box */
        .book-figure-box {
            background: #ffffff;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-sm);
            padding: 10px;
            margin: 14px 0;
            text-align: center;
        }

        .book-figure-box img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .figure-caption {
            font-size: 12px;
            color: var(--gray-600);
            margin-top: 6px;
            font-weight: 600;
        }

        /* Concept Cards & Flashcards */
        .concept-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin: 16px 0;
        }

        .concept-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-top: 4px solid var(--secondary);
            border-radius: var(--radius-sm);
            padding: 16px;
        }

        .concept-card h4 {
            color: var(--secondary);
            font-family: 'Cairo', sans-serif;
            font-size: 15px;
            font-weight: 800;
            margin-bottom: 8px;
        }

        /* Mistake Warning Alert */
        .mistake-alert {
            background: #fef2f2;
            border-right: 4px solid #ef4444;
            border-radius: var(--radius-sm);
            padding: 12px 14px;
            margin: 12px 0;
            font-size: 13px;
            color: #991b1b;
        }

        .mistake-alert strong {
            display: block;
            margin-bottom: 4px;
        }

        /* Teacher Footer Bar */
        .sheet-footer-bar {
            margin-top: 24px;
            padding-top: 14px;
            border-top: 1.5px solid var(--gray-200);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 12px;
            color: var(--gray-600);
        }

        .teacher-signature-card {
            text-align: left;
            line-height: 1.4;
        }

        .teacher-sig-name {
            font-weight: 800;
            color: var(--primary);
        }

        /* Print Specific Styles */
        @page {
    size: A4 portrait;
    margin: 8mm 8mm 10mm 8mm;
}

@page {
    size: A4 portrait;
    margin: 7mm 8mm 8mm 8mm;
}

@page {
    size: A4 portrait;
    margin: 7mm 8mm 8mm 8mm;
}

@page {
    size: A4 portrait;
    margin: 6mm 8mm 7mm 8mm;
}

@page {
    size: A4 portrait;
    margin: 6mm 7mm 6mm 7mm;
}

@page {
    size: A4 portrait;
    margin: 5mm 6mm 5mm 6mm;
}

@page {
    size: A4 portrait;
    margin: 5mm 6mm 5mm 6mm;
}

@media print {
    /* 1. HIDE SCREEN-ONLY & INTERACTIVE ELEMENTS */
    .no-print, .sticky-nav, .worksheet-top-toolbar, .print-btn-header, .btn-toggle-answers,
    .section-header-banner.worksheets, .section-title-banner.worksheets,
    #worksheets-section > .section-header-banner,
    #section-worksheets > .section-header-banner {
        display: none !important;
    }

    /* 2. COMPLETE SUPPRESSION OF ALL WORKSHEET ANSWERS IN PRINT & PDF */
    .inline-answer-badge,
    .inline-explanation,
    .problem-solution-inline,
    .inline-tf-answer,
    .tf-ans-box,
    .tf-badge,
    .inline-solution-block,
    .correct-badge,
    .answer-box {
        display: none !important;
    }

    /* 3. NEUTRAL MCQ OPTIONS FOR PRINT (NO COLORING OR HIGHLIGHTING) */
    .mcq-opt, .mcq-option, .mcq-option-line,
    .mcq-opt.correct-opt, .mcq-opt.correct-opt.show-correct,
    .hw-opt.correct-opt {
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        color: #1e293b !important;
        font-weight: 500 !important;
        box-shadow: none !important;
    }

    .student-mark-box {
        display: inline-block !important;
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* 4. BASE TYPOGRAPHY & MARGINS */
    html, body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 7.5pt !important;
        line-height: 1.15 !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }

    .main-container {
        max-width: 100% !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 5. HERO BANNER */
    .hero-banner {
        box-shadow: none !important;
        border-radius: 4px !important;
        margin-bottom: 2px !important;
        padding: 2px 5px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
    }
    .hero-title { font-size: 1.05rem !important; margin-bottom: 1px !important; }
    .hero-subtitle { font-size: 0.68rem !important; line-height: 1.12 !important; }

    /* 6. SECTION FLOW & HEADERS */
    #section-plans, #plans-section,
    .section-header-banner.plans {
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    /* Section 2 (Summaries) banner */
    #section-summaries, #summaries-section,
    .section-header-banner.summaries {
        page-break-before: page !important;
        break-before: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin: 0 0 2px 0 !important;
        padding: 2px 5px !important;
    }

    .section-banner, .section-header-banner, .section-title-banner {
        margin: 0 0 2px 0 !important;
        padding: 2px 5px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .section-banner h2, .section-header-banner h2, .section-title-banner h2 {
        font-size: 0.95rem !important;
        margin: 0 !important;
    }
    .section-banner p, .section-header-banner p, .section-title-banner p {
        font-size: 0.68rem !important;
        margin: 1px 0 0 0 !important;
    }

    /* 7. LESSON PLANS: continuous natural flow without awkward breaks */
    .unit-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 2px !important;
        padding: 2px 4px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: auto !important;
        break-before: auto !important;
    }

    .unit-card .pedagogy-box,
    .unit-card .briefcase-box,
    .unit-card .plan-step,
    .unit-card .step-box,
    .unit-card .example-box,
    .unit-card .smart-goals-box,
    .unit-card .standards-box {
        margin: 1.5px 0 !important;
        padding: 1.5px 3px !important;
    }

    /* 8. STUDENT SUMMARIES: flow naturally without forcing empty page starts */
    .summary-card, .student-summary-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 3px !important;
        padding: 4px 6px !important;
        font-size: 7.8pt !important;
        line-height: 1.18 !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: auto !important;
        break-before: auto !important;
    }

    .student-summary-card .summary-point,
    .student-summary-card .rule-box,
    .summary-card .summary-point,
    .summary-card .rule-box {
        margin-bottom: 1.5px !important;
        padding: 1.5px 3px !important;
    }

    /* 9. WORKSHEETS: STRICTLY 1 A4 PAGE PER WORKSHEET */
    .worksheet-card,
    .worksheet-paper,
    .unit-card.worksheet-card,
    #section-worksheets .worksheet-card,
    #worksheets-section .worksheet-paper,
    #worksheets-section .unit-card.worksheet-card {
        box-shadow: none !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding: 2px 4px !important;
        font-size: 7.1pt !important;
        line-height: 1.13 !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* Worksheet Official Headers */
    .school-official-header, .official-header, .ws-header, .sheet-header {
        margin-bottom: 1px !important;
        padding-bottom: 1px !important;
        border-bottom: 1px solid #0f766e !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .sch-logo-center img, .header-logo-box img {
        max-height: 20px !important;
        width: auto !important;
    }
    .sch-info-right, .sch-info-left-ar, .header-ministry {
        font-size: 6.0pt !important;
        line-height: 1.08 !important;
    }
    .school-highlight {
        font-size: 6.4pt !important;
    }

    .ws-title-strip, .unit-title-box {
        padding: 1px 2px !important;
        margin-bottom: 1px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .ws-title-strip h3, .unit-title-box h3 {
        font-size: 6.9pt !important;
        margin: 0 !important;
    }

    .student-info-grid, .ws-meta-bar {
        padding: 1px 2px !important;
        margin-bottom: 1px !important;
        font-size: 6.1pt !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6,
    .ws-sec-heading, .ws-q-title, .question-header, .unit-card-header, .plan-header {
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-top: 0.5px !important;
        margin-bottom: 0.5px !important;
    }
    .ws-sec-heading, .ws-q-title {
        font-size: 6.8pt !important;
    }

    /* Question blocks inside worksheets */
    .ws-question-block, .problem-card, .q-item, .question-card, .q-card, .tf-item,
    .exercise-box, .rule-box, .summary-point, .example-box,
    .national-link-box, .stem-card, .enrichment-challenge {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-bottom: 1px !important;
        padding: 1px 2.5px !important;
    }

    .q-text, .tf-text {
        font-size: 6.8pt !important;
        margin-bottom: 0.5px !important;
    }

    .mcq-options-grid, .mcq-options-vertical {
        gap: 1px !important;
        margin: 0.5px 0 !important;
    }

    /* Student handwritten work/answer spaces */
    .student-answer-space,
    .student-work-area,
    .answer-drawing-area {
        min-height: 28px !important;
        max-height: 40px !important;
        margin-top: 1px !important;
        padding: 1.5px !important;
        border: 1px dashed #94a3b8 !important;
        background: #fafafa !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* SVGs in 1s geometry worksheets */
    .worksheet-card svg,
    .worksheet-paper svg,
    .geometry-diagram-svg,
    svg {
        max-height: 65px !important;
        width: auto !important;
    }

    /* Tables */
    table {
        page-break-inside: auto !important;
        break-inside: auto !important;
        width: 100% !important;
        border-collapse: collapse !important;
        font-size: 6.6pt !important;
        margin-bottom: 2px !important;
    }
    thead {
        display: table-header-group !important;
    }
    tr {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    th, td {
        padding: 1px 2.5px !important;
        line-height: 1.08 !important;
    }

    /* Footers */
    .sheet-footer-bar, .teacher-signature-card, .sig-section {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 1px !important;
        padding-top: 0.5px !important;
        font-size: 5.9pt !important;
    }

    p {
        margin-top: 0.5px !important;
        margin-bottom: 0.5px !important;
    }
}
    </style>
</head>
<body>

<div class="main-container">

    <!-- Header Banner -->
    <header class="hero-banner">
        <span class="hero-tag">المملكة العربية السعودية | وزارة التعليم 2026م</span>
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: المثلثات المتطابقة</h1>
        <p class="hero-subtitle">
            <strong>الصف الأول الثانوي (مسارات) — الفصل الدراسي الأول</strong> | <strong>منصة الرائد التعليمية</strong> — إعداد المعلم: <strong>أ. محمد عبدالله جمعة</strong>. حقيبة تدريسية وتطبيقية موحدة ومتسلسلة بالكامل تشمل: خطط التحضير وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة ومطويات المفاهيم للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية المجهزة بأزرار إظهار الحل النموذجي للمعلم (محجوبة تلقائياً عند الطباعة)، مع التزام تام بالرموز الرياضية الإنجليزية LTR والشرح العربي RTL، والرسومات الهندسية المعتمدة والمحررة بدقة بالغة، لكامل كتاب الطالب من ص 146 إلى ص 200.
        </p>
        <div class="hero-meta-pills">
            <span class="meta-pill">📘 الفصل الثالث: المثلثات المتطابقة</span>
            <span class="meta-pill">📏 الصفحات: ص 146 – 200</span>
            <span class="meta-pill">📐 8 وحدات تدريسية وتطبيقية متكاملة</span>
            <span class="meta-pill">🔬 معايير STEM ورؤية السعودية 2030</span>
            <span class="meta-pill">🔤 الرموز: إنجليزية LTR | الشرح: عربي RTL</span>
        </div>
    </header>

    <!-- Sticky Navigation Bar -->
    <nav class="sticky-nav no-print">
        <div class="nav-brand">
            🏫 منصة الرائد التعليمية | رياضيات 1 ثانوي مسارات (ص 146 – 200)
        </div>
        <ul class="nav-links">
            <li><a href="#plans-section">📑 خطط التحضير (STEM)</a></li>
            <li><a href="#summaries-section">📚 الملخصات ومطويات المفاهيم</a></li>
            <li><a href="#worksheets-section">📝 أوراق العمل والاختبارات</a></li>
        </ul>
        <button class="print-btn-header" onclick="window.print()">🖨️ طباعة الحقيبة كاملة</button>
    </nav>
"""

def make_school_header(sheet_title, subtitle, sheet_number=""):
    return f"""
    <div class="official-header">
        <div class="header-ministry">
            المملكة العربية السعودية<br>
            وزارة التعليم 2026م<br>
            منصة الرائد التعليمية
        </div>
        <div class="header-logo-box">
            {f'<img src="{LOGO_DATA_URI}" alt="شعار المتقدمة" class="header-logo-img">' if LOGO_DATA_URI else '<strong>منصة الرائد التعليمية</strong>'}
        </div>
        <div class="header-sheet-info">
            <span><strong>المادة:</strong> الرياضيات 1-1 مسارات</span>
            <span><strong>الوحدة:</strong> المثلثات المتطابقة</span>
            <span><strong>الصفحات:</strong> ص 146 – 200</span>
        </div>
    </div>
    """

def make_student_meta_form():
    return """
    <div class="student-meta-grid">
        <div class="student-meta-item">
            <strong>اسم الطالب:</strong>
            <span class="meta-field-line"></span>
        </div>
        <div class="student-meta-item">
            <strong>الصف:</strong>
            <span>الأول الثانوي / شعبة: .....</span>
        </div>
        <div class="student-meta-item">
            <strong>التاريخ:</strong>
            <span>.... / .... / 1448هـ</span>
        </div>
        <div class="student-meta-item">
            <strong>الدرجة المستحقة:</strong>
            <span>[ ..... / 10 ]</span>
        </div>
    </div>
    """

def make_ws_toolbar(sheet_id):
    return f"""
    <div class="worksheet-top-toolbar no-print">
        <button type="button" class="btn-toggle-answers" onclick="toggleWorksheetAnswers('{sheet_id}', this)">
            <span class="icon">👁️</span> إظهار الإجابة على المسائل
        </button>
        <span class="toolbar-hint">💡 (هذا الزر مخصص للمعلم فقط ولن يظهر مطلقاً للطالب عند الطباعة أو التصدير إلى PDF)</span>
    </div>
    """

def make_teacher_footer():
    return """
    <div class="sheet-footer-bar">
        <div class="sheet-footer-right">
            <span>منصة الرائد التعليمية | تعليم رقمي ومهارات المستقبل وفق رؤية المملكة 2030</span>
        </div>
        <div class="sheet-footer-left">
            <div class="teacher-signature-card">
                <span class="teacher-sig-label">معلم المادة:</span>
                <span class="teacher-sig-name">أ. محمد عبدالله جمعة</span>
                <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
            </div>
        </div>
    </div>
    """

HTML_JS_AND_END = r"""
</div><!-- /.main-container -->

<!-- Interactive Script for Answers Toggling -->
<script>
    function toggleWorksheetAnswers(wsId, btn) {
        var sheet = document.getElementById(wsId);
        if (!sheet) return;
        
        var isShowing = sheet.classList.contains('show-answers');
        if (isShowing) {
            sheet.classList.remove('show-answers');
            btn.classList.remove('active');
            btn.innerHTML = '<span class="icon">👁️</span> إظهار الإجابة على المسائل';
        } else {
            sheet.classList.add('show-answers');
            btn.classList.add('active');
            btn.innerHTML = '<span class="icon">🙈</span> إخفاء الإجابة من المسائل';
        }
        
        // Typeset math if needed
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise([sheet]);
        }
    }
</script>
</body>
</html>
"""

if __name__ == "__main__":
    print("generator_1s_header_styles.py compiled successfully.")
