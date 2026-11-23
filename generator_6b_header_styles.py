# -*- coding: utf-8 -*-
"""
generator_6b_header_styles.py: Official styling, headers, footers, logo embedding,
and interactive toolbar for Grade 6 Elementary (6ب) pages 135 to 151.
"""
import base64

# Read and encode the official Advanced Schools logo
with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

LOGO_DATA_URI = f"data:image/png;base64,{logo_b64}"

HTML_START = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الحقيبة التعليمية الشاملة: الرياضيات للصف السادس الابتدائي (ص ١٣٥ - ١٥١) | أ. محمد عبدالله جمعة</title>
    
    <!-- Google Fonts: Cairo & Tajawal -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Native Arabic RTL Mathematics Styles (Strictly Right-to-Left, No MathJax) -->
    <style>
        .ar-math {
            display: inline-flex;
            flex-direction: row;
            direction: rtl;
            align-items: center;
            gap: 0.25em;
            font-weight: 700;
            color: #1e3a8a;
            vertical-align: middle;
        }
        .ar-math > span:not(.ar-frac) {
            display: inline-block;
            direction: rtl;
        }
        .ar-frac, .ar-math .ar-frac, span.ar-frac {
            display: inline-flex !important;
            flex-direction: column !important;
            vertical-align: middle !important;
            text-align: center !important;
            padding: 0 4px !important;
            font-size: 0.92em !important;
            line-height: 1.05 !important;
            margin: 0 2px !important;
        }
        .ar-frac .num, .ar-math .ar-frac .num {
            display: block !important;
            border-bottom: 2px solid currentColor !important;
            padding-bottom: 2px !important;
            margin-bottom: 1px !important;
            text-align: center !important;
            min-width: 14px;
            font-size: 1em !important;
            line-height: 1.0 !important;
        }
        .ar-frac .denom, .ar-math .ar-frac .denom {
            display: block !important;
            padding-top: 2px !important;
            text-align: center !important;
            min-width: 14px;
            font-size: 1em !important;
            line-height: 1.0 !important;
        }
        .mixed-num {
            display: inline-flex;
            align-items: center;
            direction: rtl;
            gap: 3px;
            vertical-align: middle;
        }
        .ar-math-display {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            gap: 0.35em;
            direction: rtl;
            font-size: 1.15rem;
            font-weight: 800;
            color: #1e3a8a;
            margin: 10px 0;
        }
    </style>

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
            direction: rtl;
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
            font-size: 1.05rem;
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
            font-size: 1.15rem;
            color: #bfdbfe;
            margin-bottom: 20px;
            max-width: 850px;
        }

        .hero-meta-bar {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
            background: rgba(0, 0, 0, 0.25);
            padding: 12px 20px;
            border-radius: var(--radius-md);
            font-size: 0.95rem;
        }

        .hero-meta-item strong {
            color: #93c5fd;
        }

        /* Section Headings */
        .section-banner {
            background: #ffffff;
            border-right: 6px solid #2563eb;
            padding: 20px 24px;
            border-radius: var(--radius-md);
            margin: 40px 0 24px 0;
            box-shadow: var(--shadow-sm);
        }

        .section-banner h2 {
            font-size: 1.6rem;
            color: var(--primary-dark);
            font-weight: 800;
            margin-bottom: 4px;
        }

        .section-banner p {
            color: var(--gray-600);
            font-size: 0.98rem;
        }

        /* Official School Header Component */
        .school-official-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px double #1e3a8a;
            padding-bottom: 14px;
            margin-bottom: 24px;
            direction: rtl;
        }

        .sch-info-right {
            text-align: right;
            font-size: 0.88rem;
            color: #1e293b;
            line-height: 1.6;
        }

        .sch-info-right .ministry-name {
            font-size: 0.92rem;
            font-weight: 800;
            color: #1e3a8a;
        }

        .sch-info-right .school-highlight {
            font-size: 1.05rem;
            font-weight: 900;
            color: #0d9488;
        }

        .sch-logo-center {
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 4px;
        }

        .sch-logo-center img {
            max-height: 80px;
            width: auto;
            object-fit: contain;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.12));
        }

        .sch-info-left-ar {
            text-align: left;
            font-size: 0.88rem;
            color: #1e293b;
            line-height: 1.6;
        }

        .sch-info-left-ar .badge-tag {
            display: inline-block;
            background: #eff6ff;
            color: #1d4ed8;
            padding: 2px 10px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.82rem;
            border: 1px solid #bfdbfe;
            margin-top: 4px;
        }

        /* Official Teacher Signature Footer Bar */
        .sheet-footer-bar {
            margin-top: 32px;
            padding-top: 16px;
            border-top: 2px dashed #cbd5e1;
            display: flex;
            align-items: center;
            justify-content: space-between;
            direction: rtl;
        }

        .sheet-footer-right {
            font-size: 0.85rem;
            color: #64748b;
        }

        .teacher-signature-card {
            background: #ffffff;
            border: 2px solid #2563eb;
            border-radius: var(--radius-md);
            padding: 8px 18px;
            text-align: left;
            display: inline-block;
            box-shadow: var(--shadow-sm);
        }

        .teacher-sig-label {
            font-size: 0.82rem;
            color: #64748b;
            font-weight: 700;
            display: block;
        }

        .teacher-sig-name {
            font-size: 1.05rem;
            color: #1e3a8a;
            font-weight: 900;
        }

        .teacher-school-subtext {
            font-size: 0.78rem;
            color: #0d9488;
            font-weight: 700;
        }

        /* Worksheet Top Dedicated Toolbar */
        .worksheet-top-toolbar {
            background: #eff6ff;
            border: 2px solid #bfdbfe;
            border-radius: var(--radius-md);
            padding: 12px 18px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-sm);
        }

        .btn-toggle-answers {
            background: #2563eb;
            color: #ffffff;
            border: none;
            padding: 8px 18px;
            border-radius: var(--radius-sm);
            font-size: 0.95rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.3);
        }

        .btn-toggle-answers:hover {
            background: #1d4ed8;
            transform: translateY(-1px);
        }

        .toolbar-hint {
            font-size: 0.85rem;
            color: #1e40af;
            font-weight: 600;
        }

        /* Cards for Units, Summaries, Worksheets */
        .unit-card, .student-summary-card, .worksheet-card {
            background: #ffffff;
            border-radius: var(--radius-lg);
            padding: 32px;
            margin-bottom: 36px;
            box-shadow: var(--shadow-md);
            border: 1px solid #e2e8f0;
            page-break-after: always;
        }

        /* Pedagogical Styling */
        .pedagogy-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 20px;
            margin: 16px 0;
        }

        .briefcase-box {
            background: #eff6ff;
            border-right: 5px solid #2563eb;
            padding: 16px 20px;
            border-radius: var(--radius-md);
            margin-bottom: 16px;
        }

        .briefcase-title {
            font-weight: 800;
            color: #1e40af;
            margin-bottom: 6px;
            font-size: 1.05rem;
        }

        .smart-goals-list {
            list-style: none;
            padding: 0;
        }

        .smart-goals-list li {
            padding: 8px 12px;
            background: #ffffff;
            margin-bottom: 8px;
            border-radius: 8px;
            border-right: 4px solid #10b981;
            font-size: 0.95rem;
        }

        /* KWL Table */
        .standard-table {
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0;
            background: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid #cbd5e1;
            font-size: 0.93rem;
        }

        .standard-table th {
            background: #1e3a8a;
            color: #ffffff;
            padding: 10px 14px;
            font-weight: 800;
            text-align: right;
            border: 1px solid #3b82f6;
        }

        .standard-table td {
            padding: 10px 14px;
            border: 1px solid #e2e8f0;
            vertical-align: top;
            line-height: 1.7;
        }

        .standard-table tr:nth-child(even) {
            background: #f8fafc;
        }

        /* Frayer Model Grid */
        .frayer-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }

        .frayer-quadrant {
            background: #ffffff;
            border-radius: var(--radius-md);
            padding: 16px;
            border: 2px solid #e2e8f0;
            box-shadow: var(--shadow-sm);
        }

        .frayer-quad-title {
            font-weight: 800;
            font-size: 1.02rem;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 2px solid #e2e8f0;
        }

        .quad-def { border-color: #3b82f6; }
        .quad-def .frayer-quad-title { color: #1d4ed8; border-color: #bfdbfe; }
        .quad-char { border-color: #10b981; }
        .quad-char .frayer-quad-title { color: #047857; border-color: #a7f3d0; }
        .quad-ex { border-color: #f59e0b; }
        .quad-ex .frayer-quad-title { color: #b45309; border-color: #fde68a; }
        .quad-nonex { border-color: #ef4444; }
        .quad-nonex .frayer-quad-title { color: #b91c1c; border-color: #fecaca; }

        /* Classroom Rules Cards */
        .rules-flex-container {
            display: flex;
            gap: 16px;
            margin: 14px 0;
            flex-wrap: wrap;
        }

        .rule-card {
            flex: 1;
            min-width: 260px;
            background: #ffffff;
            border-radius: var(--radius-md);
            padding: 16px;
            border-top: 4px solid #0d9488;
            box-shadow: var(--shadow-sm);
            border: 1px solid #e2e8f0;
            border-top-width: 4px;
        }

        .rule-title {
            font-weight: 800;
            color: #0f766e;
            margin-bottom: 6px;
        }

        .rule-desc {
            font-size: 0.92rem;
            color: #475569;
        }

        /* STEM Grid */
        .stem-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 14px;
            margin: 16px 0;
        }

        .stem-card {
            background: #ffffff;
            border-radius: var(--radius-md);
            padding: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: var(--shadow-sm);
        }

        .stem-card .stem-header {
            font-weight: 800;
            font-size: 1rem;
            margin-bottom: 8px;
            padding-bottom: 4px;
            border-bottom: 2px solid #e2e8f0;
        }

        .stem-s .stem-header { color: #059669; border-color: #a7f3d0; }
        .stem-t .stem-header { color: #0284c7; border-color: #bae6fd; }
        .stem-e .stem-header { color: #d97706; border-color: #fde68a; }
        .stem-m .stem-header { color: #7c3aed; border-color: #ddd6fe; }

        .stem-body {
            font-size: 0.9rem;
            color: #334155;
            line-height: 1.6;
        }

        /* Tree Map Card */
        .tree-map-card {
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: var(--radius-md);
            padding: 18px;
            margin: 16px 0;
        }

        .tree-content ul {
            padding-right: 20px;
            margin-top: 8px;
        }

        .tree-content li {
            margin-bottom: 6px;
            font-size: 0.94rem;
        }

        /* Solved Examples in Lesson Plans */
        .solved-example {
            background: #f8fafc;
            border-right: 4px solid #6366f1;
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 14px;
        }

        .ex-label {
            font-weight: 800;
            color: #4338ca;
            margin-bottom: 6px;
        }

        .ex-steps {
            font-size: 0.95rem;
            color: #334155;
            line-height: 1.8;
        }

        /* Homework Box */
        .homework-box {
            background: #fffbeb;
            border: 2px dashed #f59e0b;
            border-radius: var(--radius-md);
            padding: 18px;
            margin: 16px 0;
        }

        .hw-question {
            font-weight: 800;
            color: #92400e;
            font-size: 1.05rem;
            margin-bottom: 12px;
        }

        .hw-options-vertical {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 12px;
        }

        .hw-opt {
            background: #ffffff;
            padding: 8px 14px;
            border-radius: 8px;
            border: 1px solid #fde68a;
            font-size: 0.95rem;
        }

        .hw-opt.correct-opt {
            background: #ecfdf5;
            border-color: #10b981;
            color: #065f46;
            font-weight: 700;
        }

        .hw-solution-note {
            background: #ffffff;
            border-radius: 8px;
            padding: 10px 14px;
            border: 1px solid #fcd34d;
            font-size: 0.9rem;
            color: #78350f;
        }

        /* Summary Styling */
        .summary-grid-2col {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin: 16px 0;
        }

        .concept-callout {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 18px;
            box-shadow: var(--shadow-sm);
        }

        .concept-callout h4 {
            color: #1e3a8a;
            font-weight: 800;
            margin-bottom: 10px;
            font-size: 1.05rem;
        }

        .math-rule-box {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 12px;
            margin-top: 10px;
            font-size: 0.95rem;
            direction: rtl;
        }

        /* Arabic Vertical Calculation Tables (RTL-Compliant with Sign on the Right) */
        .arabic-vert-calc-wrapper {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            gap: 36px;
            margin: 12px auto;
            direction: rtl;
            width: 100%;
        }

        .arabic-vert-table {
            display: inline-table;
            direction: rtl;
            border-collapse: collapse;
            font-family: 'Tajawal', 'Cairo', sans-serif;
            font-size: 1.28rem;
            font-weight: 700;
            color: var(--primary-dark);
            background: #ffffff;
            padding: 8px 16px;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            box-shadow: var(--shadow-sm);
        }

        .arabic-vert-table caption {
            font-size: 0.85rem;
            font-weight: 800;
            color: #475569;
            margin-bottom: 4px;
        }

        .arabic-vert-table td {
            padding: 4px 10px;
            vertical-align: middle;
        }

        .arabic-vert-table .sign-col {
            text-align: center;
            width: 32px;
            color: #2563eb;
            font-size: 1.4rem;
            font-weight: 900;
        }

        .arabic-vert-table .num-col {
            text-align: left;
            letter-spacing: 1.5px;
            font-variant-numeric: tabular-nums;
        }

        .arabic-vert-table .op-divider {
            border-bottom: 2.5px solid #1e3a8a;
        }

        .arabic-vert-table .res-row td {
            padding-top: 6px;
            color: #166534;
            font-weight: 900;
        }

        /* Worksheet Question Styling */
        .ws-section-box {
            margin-bottom: 24px;
        }

        .ws-sec-heading {
            font-size: 1.15rem;
            color: var(--primary-dark);
            font-weight: 800;
            margin-bottom: 14px;
            padding-bottom: 6px;
            border-bottom: 2px solid #e2e8f0;
        }

        .q-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: var(--radius-md);
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: var(--shadow-sm);
        }

        .q-text {
            font-size: 1.02rem;
            font-weight: 700;
            margin-bottom: 12px;
            color: #1e293b;
        }

        .mcq-options-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 10px;
            margin-bottom: 12px;
        }

        .mcq-opt {
            background: #f8fafc;
            border: 1.5px solid #cbd5e1;
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .mcq-opt.correct-opt.show-correct {
            background: #ecfdf5;
            border-color: #10b981;
            color: #065f46;
            font-weight: 800;
        }

        .correct-badge {
            display: none;
            background: #10b981;
            color: #ffffff;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
        }

        .correct-badge.show-badge {
            display: inline-block;
        }

        /* Inline Solutions Box directly on questions */
        .inline-solution-block {
            display: none;
            background: #f0fdf4;
            border-right: 4px solid #10b981;
            border-radius: 6px;
            padding: 10px 14px;
            margin-top: 10px;
            font-size: 0.92rem;
            color: #166534;
            line-height: 1.7;
        }

        .inline-solution-block.show-sol {
            display: block;
        }

        .student-work-area {
            border: 1.5px dashed #cbd5e1;
            border-radius: 8px;
            min-height: 60px;
            padding: 10px;
            margin: 10px 0;
            background: #fafafa;
            color: #94a3b8;
            font-size: 0.88rem;
        }

        
        .tf-ans-box {
            display: none;
            margin-top: 6px;
            padding: 6px 10px;
            background: #f0fdf4;
            border-radius: 6px;
            border-right: 3px solid #10b981;
        }

        .student-mark-box {
            display: inline-block;
            color: #1e3a8a;
            font-weight: 700;
            margin-right: 8px;
            letter-spacing: 2px;
        }
.tf-item {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 14px;
            margin-bottom: 12px;
        }

        .tf-text {
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .tf-badge {
            display: inline-block;
            padding: 2px 10px;
            border-radius: 4px;
            font-weight: 800;
            font-size: 0.85rem;
        }

        .tf-correct { background: #dcfce7; color: #166534; border: 1px solid #86efac; }
        .tf-wrong { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }

        /* Print Media Styles: STRICTLY HIDE TOOLBARS AND BUTTONS */
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

<!-- Top Sticky Nav -->
<header class="sticky-nav no-print">
    <div class="nav-brand">
        <span>📘 الحقيبة الشاملة: رياضيات الصف السادس الابتدائي (ص ١٣٥ - ١٥١)</span>
    </div>
    <ul class="nav-links">
        <li><a href="#section-plans">خطط التحضير (٥)</a></li>
        <li><a href="#section-summaries">ملخصات الطالب (٥)</a></li>
        <li><a href="#section-worksheets">أوراق العمل والاختبارات (٥)</a></li>
    </ul>
    <button type="button" class="print-btn-header" onclick="window.print()">
        <span>🖨️ طباعة الحقيبة</span>
    </button>
</header>

<div class="main-container">

    <!-- Hero Header -->
    <section class="hero-banner">
        <span class="hero-tag">🇸🇦 المملكة العربية السعودية | وزارة التعليم ٢٠٢٦م</span>
        <h1 class="hero-title">الحقيبة التعليمية والتدريسية الشاملة: الرياضيات (٦ ب)</h1>
        <p class="hero-subtitle">تغطي اختبار الفصل ٣ والتراكمي ٣، وتهيئة الفصل ٤، والدرس (٤-١) ق.م.أ، ومعمل الكسور المتكافئة، والدرس (٤-٢) تبسيط الكسور ومعمل الأعداد الكسرية (ص ١٣٥ - ١٥١)</p>
        <div class="hero-meta-bar">
            <div class="hero-meta-item"><strong>المدرسة:</strong> المدارس المتقدمة للتعلم الذكي بجدة</div>
            <div class="hero-meta-item"><strong>إعداد المعلم:</strong> أ. محمد عبدالله جمعة</div>
            <div class="hero-meta-item"><strong>الصف:</strong> السادس الابتدائي</div>
            <div class="hero-meta-item"><strong>المنهج:</strong> رياضيات الفصل الدراسي الثاني</div>
        </div>
    </section>
"""

def make_school_header(title_right, sheet_type="ورقة عمل وتقويم"):
    return f'''
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بمحافظة جدة</div>
        <div class="school-highlight">المدارس المتقدمة للتعلم الذكي بجدة</div>
        <div>قسم الرياضيات | المرحلة الابتدائية (الصفوف العليا)</div>
    </div>
    <div class="sch-logo-center">
        <img src="{LOGO_DATA_URI}" alt="شعار المدارس المتقدمة" style="height: 72px; width: auto; object-fit: contain;">
        <span style="font-size:0.78rem; font-weight:800; color:#1e3a8a;">مدارس المتقدمة للتعلم الذكي بجدة</span>
    </div>
    <div class="sch-info-left-ar">
        <div>مادة: الرياضيات (الصف السادس الابتدائي)</div>
        <div>الموضوع: {title_right}</div>
        <span class="badge-tag">{sheet_type}</span>
    </div>
</div>
'''

def make_teacher_footer():
    return '''
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>المدارس المتقدمة للتعلم الذكي بجدة | تعليم ذكي ورؤية طموحة | رؤية المملكة ٢٠٣٠</span>
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
function toggleWorksheetAnswers(sheetId, btn) {
    var card = document.getElementById(sheetId);
    if (!card) return;

    var solutions = card.querySelectorAll('.inline-solution-block');
    var badges = card.querySelectorAll('.correct-badge');
    var correctOpts = card.querySelectorAll('.mcq-opt.correct-opt');
    var tfBoxes = card.querySelectorAll('.tf-ans-box');

    var isHidden = true;
    if (solutions.length > 0) {
        isHidden = (solutions[0].style.display !== 'block');
    } else if (tfBoxes.length > 0) {
        isHidden = (tfBoxes[0].style.display !== 'block');
    }

    tfBoxes.forEach(function(el) {
        el.style.display = isHidden ? 'block' : 'none';
    });

    solutions.forEach(function(el) {
        el.style.display = isHidden ? 'block' : 'none';
    });

    badges.forEach(function(el) {
        el.style.display = isHidden ? 'inline-block' : 'none';
    });

    correctOpts.forEach(function(el) {
        if (isHidden) {
            el.classList.add('show-correct');
        } else {
            el.classList.remove('show-correct');
        }
    });

    if (isHidden) {
        btn.innerHTML = '<span class="icon">🙈</span> إخفاء الإجابة من المسائل';
        btn.style.background = '#059669';
    } else {
        btn.innerHTML = '<span class="icon">👁️</span> إظهار الإجابة على المسائل';
        btn.style.background = '#2563eb';
    }
}
</script>

</body>
</html>
"""

print("generator_6b_header_styles.py updated successfully.")
