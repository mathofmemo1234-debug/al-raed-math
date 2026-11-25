# -*- coding: utf-8 -*-
"""
generator_1m_header_styles.py: Provides HTML head, styles, school official header,
teacher footer, worksheet toolbar, and print logic for Grade 7 (1m) suite.
"""
import base64

with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

LOGO_DATA_URI = f"data:image/png;base64,{logo_b64}"

HTML_START = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة التعليمية والتدريسية الشاملة: المعادلات الخطية والقياس (ص ١٠٩ - ١٢٧) | الصف الأول المتوسط | أ. محمد عبدالله جمعة | منصة الرائد التعليمية</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    
    <!-- MathJax 3 Configuration for Arabic Mathematics -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['\\(', '\\)']],
                displayMath: [['\\[', '\\]']],
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
            font-family: 'Tajawal', 'Cairo', sans-serif;
        }

        body {
            background-color: #f1f5f9;
            color: var(--dark);
            line-height: 1.8;
            padding-bottom: 60px;
        }

        /* Top Sticky Navigation Bar */
        .sticky-nav {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.97);
            backdrop-filter: blur(8px);
            color: var(--white);
            padding: 12px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            border-bottom: 3px solid #2563eb;
        }

        .nav-brand {
            font-size: 1.1rem;
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
            font-weight: 700;
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
            padding: 8px 18px;
            border-radius: var(--radius-sm);
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .print-btn-header:hover {
            background: #059669;
            transform: translateY(-1px);
        }

        /* Main Container */
        .main-container {
            max-width: 1200px;
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
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .hero-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.35);
            color: #ffffff;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.88rem;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2.15rem;
            font-weight: 900;
            margin-bottom: 10px;
            line-height: 1.35;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            opacity: 0.95;
            max-width: 950px;
            line-height: 1.7;
        }

        /* Master Section Headers */
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
            padding: 5px 14px;
            border-radius: 20px;
            background: var(--gray-100);
            border: 1px solid var(--gray-300);
            color: var(--gray-700);
        }

        /* Lesson Plan Unit Card */
        .unit-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 32px;
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
            font-weight: 800;
            padding: 4px 14px;
            border-radius: 8px;
            font-size: 0.88rem;
            border: 1px solid #bfdbfe;
        }

        .plan-step-box {
            margin-bottom: 24px;
            padding: 20px;
            background: #ffffff;
            border: 1px solid var(--gray-200);
            border-radius: var(--radius-md);
        }

        .plan-step-title {
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--primary-dark);
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 2px solid var(--gray-100);
            padding-bottom: 8px;
        }

        /* School Official Header */
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

        /* Student Summary Card */
        .summary-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 30px;
            margin-bottom: 32px;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
        }

        .summary-title-bar {
            background: linear-gradient(90deg, #f0fdfa 0%, #ffffff 100%);
            border-right: 6px solid var(--secondary);
            padding: 12px 18px;
            margin-bottom: 20px;
            border-radius: 4px;
        }

        .summary-title-bar h3 {
            color: #0f766e;
            font-size: 1.3rem;
            font-weight: 800;
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
            padding: 10px 16px;
            display: flex;
            justify-content: space-between;
            margin-bottom: 22px;
            font-size: 0.95rem;
            font-weight: 700;
            flex-wrap: wrap;
            gap: 8px;
        }

        .ws-question-block {
            margin-bottom: 22px;
            padding-bottom: 18px;
            border-bottom: 1px solid var(--gray-200);
        }

        .ws-question-block:last-child {
            border-bottom: none;
        }

        .ws-q-title {
            font-weight: 800;
            font-size: 1.05rem;
            margin-bottom: 12px;
            color: var(--primary-dark);
        }

        .mcq-options-vertical {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin: 10px 0 10px 14px;
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
            font-weight: 600;
        }

        .worksheet-paper.show-answers .inline-tf-answer {
            display: inline-block !important;
            background: #ecfdf5;
            border: 1px solid #86efac;
            color: #065f46;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.9rem;
            font-weight: 800;
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
            line-height: 1.85;
            font-weight: 600;
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
            gap: 12px;
            flex-wrap: wrap;
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
            flex-wrap: wrap;
            gap: 12px;
        }

        .sheet-footer-right {
            font-size: 0.85rem;
            color: var(--gray-600);
            font-weight: 700;
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
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        .teacher-sig-label {
            font-size: 0.8rem;
            color: var(--gray-600);
            font-weight: 700;
            display: block;
        }

        .teacher-sig-name {
            font-size: 1.05rem;
            font-weight: 900;
            color: var(--primary);
            border-bottom: 2px solid #1e3a8a;
            padding-bottom: 2px;
            display: inline-block;
        }

        .teacher-school-subtext {
            font-size: 0.78rem;
            color: #0d9488;
            font-weight: 800;
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
            font-weight: 800;
        }

        .data-table tr:nth-child(even) td {
            background: #fafbfd;
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
            font-weight: 900;
            font-size: 1.1rem;
        }

        .frayer-quadrant {
            background: var(--white);
            border-radius: var(--radius-sm);
            padding: 14px 16px;
            border: 1px solid var(--gray-200);
        }

        .frayer-quadrant h4 {
            color: var(--secondary);
            font-size: 0.98rem;
            margin-bottom: 6px;
            border-bottom: 2px solid var(--secondary-light);
            padding-bottom: 4px;
            font-weight: 800;
        }

        /* Tree Mind Map */
        .tree-mindmap {
            background: #f8fafc;
            border: 1px solid var(--gray-300);
            border-radius: var(--radius-md);
            padding: 18px;
            margin: 16px 0;
        }

        .tree-root {
            font-weight: 900;
            color: var(--primary);
            font-size: 1.05rem;
            margin-bottom: 10px;
        }

        .tree-branch {
            margin-right: 20px;
            padding-right: 12px;
            border-right: 3px solid #60a5fa;
            margin-bottom: 8px;
        }

        .tree-branch-title {
            font-weight: 800;
            color: #0369a1;
            font-size: 0.95rem;
        }

        .tree-leaf {
            margin-right: 18px;
            color: #334155;
            font-size: 0.9rem;
        }

        /* STEM Matrix */
        .stem-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 14px;
            margin: 16px 0;
        }

        .stem-pillar {
            background: var(--gray-50);
            border-radius: var(--radius-sm);
            padding: 14px;
            border-top: 4px solid var(--secondary);
            border: 1px solid var(--gray-200);
        }

        .stem-pillar.s { border-top: 4px solid #0284c7; }
        .stem-pillar.t { border-top: 4px solid #6366f1; }
        .stem-pillar.e { border-top: 4px solid #f59e0b; }
        .stem-pillar.m { border-top: 4px solid #10b981; }

        .stem-pillar h4 {
            font-size: 1rem;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 800;
        }

        /* Rules Cards */
        .rule-card-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 14px;
            margin: 16px 0;
        }

        .rule-card {
            background: #f8fafc;
            border-radius: var(--radius-sm);
            padding: 14px;
            border-top: 4px solid #2563eb;
            border: 1px solid var(--gray-200);
        }

        .rule-card h5 {
            font-size: 0.95rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 6px;
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

        .callout-info {
            background: var(--primary-light);
            border-right: 5px solid var(--primary);
            color: var(--primary-dark);
        }

        .callout-tip {
            background: var(--secondary-light);
            border-right: 5px solid var(--secondary);
            color: #0f766e;
        }

        /* Question Answer Space for student writing */
        .student-answer-space {
            border: 1px dashed #cbd5e1;
            background: #fafafa;
            border-radius: 6px;
            min-height: 70px;
            padding: 10px;
            margin: 8px 0;
            color: #94a3b8;
            font-size: 0.85rem;
        }

        @media (max-width: 768px) {
            .rule-card-grid { grid-template-columns: 1fr; }
            .frayer-box { grid-template-columns: 1fr; }
            .school-official-header { flex-direction: column; gap: 10px; text-align: center; }
            .sch-info-right, .sch-info-left-ar { text-align: center; }
        }

        /* Print Settings: Strictly hide toolbar & navigation */
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

<!-- Navigation Bar -->
<nav class="sticky-nav no-print">
    <div class="nav-brand">
        🏫 منصة الرائد التعليمية | رياضيات ١م (ص ١٠٩ - ١٢٧)
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
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: المعادلات الخطية والقياس</h1>
        <p class="hero-subtitle">
            <strong>الصف الأول المتوسط (الفصل الدراسي الثاني)</strong> | <strong>منصة الرائد التعليمية</strong> — إعداد المعلم: <strong>أ. محمد عبدالله جمعة</strong>. حقيبة تدريسية وتطبيقية موحدة تضم: خطط التحضير وفق معايير STEM السبعة متتالية، تليها الملخصات الشاملة للطلاب متتالية، تليها أوراق العمل والاختبارات التطبيقية بأزرار إظهار الإجابة المباشرة على المسائل (مخصصة للمعلم ومحجوبة عند الطباعة)، مع التزام تام بالأرقام العربية المعتمدة، وشاملة الصفحات من ١٠٩ إلى ١٢٧ من كتاب الرياضيات.
        </p>
    </header>
"""

def make_school_header(title_right, sheet_type="ورقة عمل وتقويم"):
    return f'''
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بمحافظة جدة</div>
        <div class="school-highlight">منصة الرائد التعليمية</div>
        <div>قسم الرياضيات | المرحلة المتوسطة</div>
    </div>
    <div class="sch-logo-center">
        <img src="{LOGO_DATA_URI}" alt="شعار المنصة" style="height: 72px; width: auto; object-fit: contain;">
        <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">منصة الرائد التعليمية بجدة</span>
    </div>
    <div class="sch-info-left-ar">
        <div>مادة: الرياضيات (الصف الأول المتوسط)</div>
        <div>الفصل الدراسي الثاني - العام الدراسي ١٤٤٧ / ١٤٤٨هـ (٢٠٢٦م)</div>
        <div>{sheet_type}</div>
        <div style="color:#0d9488; font-weight:800;">{title_right}</div>
    </div>
</div>
'''

def make_teacher_footer():
    return '''
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>منصة الرائد التعليمية | تعليم رقمي ومهارات المستقبل | رؤية المملكة ٢٠٣٠</span>
    </div>
    <div class="sheet-footer-left">
        <div class="teacher-signature-card">
            <span class="teacher-sig-label">معلم المادة:</span>
            <span class="teacher-sig-name">أ. محمد عبدالله جمعة</span>
            <div class="teacher-school-subtext">منصة الرائد التعليمية</div>
        </div>
    </div>
</div>
'''

def make_ws_toolbar(sheet_id):
    return f'''
<div class="worksheet-top-toolbar no-print">
    <button type="button" class="btn-toggle-answers" onclick="toggleWorksheetAnswers('{sheet_id}', this)">
        <span class="icon">👁️</span> إظهار الإجابة على المسائل
    </button>
    <span class="toolbar-hint">💡 (هذا الزر مخصص للمعلم فقط ولن يظهر مطلقاً للطالب عند الطباعة أو التصدير إلى PDF)</span>
</div>
'''

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
    print("generator_1m_header_styles.py is ready.")
