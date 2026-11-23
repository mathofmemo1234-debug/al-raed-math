import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

PERFECT_PRINT_CSS = """@media print {
    /* ==========================================================================
       1. HIDE SCREEN-ONLY & INTERACTIVE CONTROLS
       ========================================================================== */
    .no-print, .sticky-nav, .worksheet-top-toolbar, .print-btn-header, .btn-toggle-answers,
    .section-header-banner.worksheets, .section-title-banner.worksheets,
    #worksheets-section > .section-header-banner,
    #worksheets-section > .section-banner,
    #section-worksheets > .section-header-banner,
    #section-worksheets > .section-banner {
        display: none !important;
    }

    /* ==========================================================================
       2. ABSOLUTE ZERO ANSWER LEAKS IN WORKSHEETS FOR PRINT & PDF
       ========================================================================== */
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

    /* Force all MCQ options to appear completely neutral and identical */
    .mcq-opt, .mcq-option, .mcq-option-line,
    .mcq-opt.correct-opt, .mcq-opt.correct-opt.show-correct,
    .hw-opt.correct-opt {
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        color: #1e293b !important;
        font-weight: 500 !important;
        box-shadow: none !important;
    }

    /* Clear designated student mark space for True/False */
    .student-mark-box {
        display: inline-block !important;
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* ==========================================================================
       3. BASE TYPOGRAPHY & MARGINS (DENSE, BALANCED A4)
       ========================================================================== */
    html, body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 7.2pt !important;
        line-height: 1.12 !important;
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

    /* ==========================================================================
       4. HERO BANNER
       ========================================================================== */
    .hero-banner {
        box-shadow: none !important;
        border-radius: 3px !important;
        margin-bottom: 1.5px !important;
        padding: 2px 4px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
    }
    .hero-title { font-size: 1.02rem !important; margin-bottom: 1px !important; }
    .hero-subtitle { font-size: 0.66rem !important; line-height: 1.10 !important; }

    /* ==========================================================================
       5. SECTION FLOW & HEADERS
       ========================================================================== */
    #section-plans, #plans-section,
    .section-header-banner.plans {
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    #section-summaries, #summaries-section,
    .section-header-banner.summaries {
        page-break-before: page !important;
        break-before: page !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin: 0 0 1.5px 0 !important;
        padding: 2px 4px !important;
    }

    .section-banner, .section-header-banner, .section-title-banner {
        margin: 0 0 1.5px 0 !important;
        padding: 2px 4px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .section-banner h2, .section-header-banner h2, .section-title-banner h2 {
        font-size: 0.92rem !important;
        margin: 0 !important;
    }
    .section-banner p, .section-header-banner p, .section-title-banner p {
        font-size: 0.66rem !important;
        margin: 0.5px 0 0 0 !important;
    }

    /* ==========================================================================
       6. LESSON PLANS: CONTINUOUS HIGH-DENSITY FLOW (NO AWKWARD 2-LINE SPILLS)
       ========================================================================== */
    .unit-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 3px !important;
        margin-top: 0 !important;
        margin-bottom: 1.5px !important;
        padding: 2px 3.5px !important;
        font-size: 7.0pt !important;
        line-height: 1.10 !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }

    .unit-card .pedagogy-box,
    .unit-card .briefcase-box,
    .unit-card .plan-step,
    .unit-card .step-box,
    .unit-card .example-box,
    .unit-card .smart-goals-box,
    .unit-card .standards-box {
        margin: 1px 0 !important;
        padding: 1px 2px !important;
    }

    /* ==========================================================================
       7. STUDENT SUMMARIES: BALANCED DENSITY & FLOW
       ========================================================================== */
    .summary-card, .student-summary-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 3px !important;
        margin-top: 0 !important;
        margin-bottom: 2px !important;
        padding: 3px 5px !important;
        font-size: 7.2pt !important;
        line-height: 1.12 !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }

    .student-summary-card .summary-point,
    .student-summary-card .rule-box,
    .summary-card .summary-point,
    .summary-card .rule-box {
        margin-bottom: 1px !important;
        padding: 1px 2.5px !important;
    }

    /* ==========================================================================
       8. WORKSHEETS: STRICTLY EXACTLY 1 A4 PAGE PER WORKSHEET (ZERO SPILLOVER)
       ========================================================================== */
    .worksheet-card,
    .worksheet-paper,
    .unit-card.worksheet-card,
    #section-worksheets .worksheet-card,
    #worksheets-section .worksheet-paper,
    #worksheets-section .unit-card.worksheet-card {
        box-shadow: none !important;
        border: 1px solid #94a3b8 !important;
        border-radius: 3px !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        padding: 1.5px 3px !important;
        font-size: 6.8pt !important;
        line-height: 1.10 !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* Official Ministry Worksheet Headers */
    .school-official-header, .official-header, .ws-header, .sheet-header {
        margin-bottom: 0.5px !important;
        padding-bottom: 0.5px !important;
        border-bottom: 1px solid #0f766e !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .sch-logo-center img, .header-logo-box img {
        max-height: 18px !important;
        width: auto !important;
    }
    .sch-info-right, .sch-info-left-ar, .header-ministry {
        font-size: 5.8pt !important;
        line-height: 1.05 !important;
    }
    .school-highlight {
        font-size: 6.2pt !important;
    }

    .ws-title-strip, .unit-title-box {
        padding: 0.5px 1.5px !important;
        margin-bottom: 0.5px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .ws-title-strip h3, .unit-title-box h3 {
        font-size: 6.7pt !important;
        margin: 0 !important;
    }

    .student-info-grid, .ws-meta-bar {
        padding: 0.5px 1.5px !important;
        margin-bottom: 0.5px !important;
        font-size: 5.9pt !important;
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
        font-size: 6.6pt !important;
    }

    /* Question blocks */
    .ws-question-block, .problem-card, .q-item, .question-card, .q-card, .tf-item,
    .exercise-box, .rule-box, .summary-point, .example-box,
    .national-link-box, .stem-card, .enrichment-challenge {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-bottom: 0.5px !important;
        padding: 0.5px 2px !important;
    }

    .q-text, .tf-text {
        font-size: 6.6pt !important;
        margin-bottom: 0.5px !important;
    }

    .mcq-options-grid, .mcq-options-vertical {
        gap: 0.5px !important;
        margin: 0.5px 0 !important;
    }

    /* Designated student handwritten solving spaces */
    .student-answer-space,
    .student-work-area,
    .answer-drawing-area {
        min-height: 25px !important;
        max-height: 36px !important;
        margin-top: 0.5px !important;
        padding: 1px !important;
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
        max-height: 55px !important;
        width: auto !important;
    }

    /* Tables */
    table {
        page-break-inside: auto !important;
        break-inside: auto !important;
        width: 100% !important;
        border-collapse: collapse !important;
        font-size: 6.4pt !important;
        margin-bottom: 1px !important;
    }
    thead {
        display: table-header-group !important;
    }
    tr {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    th, td {
        padding: 0.5px 2px !important;
        line-height: 1.05 !important;
    }

    /* Footers */
    .sheet-footer-bar, .teacher-signature-card, .sig-section {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 0.5px !important;
        padding-top: 0.5px !important;
        font-size: 5.8pt !important;
    }

    p {
        margin-top: 0.5px !important;
        margin-bottom: 0.5px !important;
    }
}
"""

html_files = [
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html',
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html'
]

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'@media\s+print\s*\{.*?\n\}\s*\n', content, re.DOTALL)
    if m:
        content = content[:m.start()] + PERFECT_PRINT_CSS + content[m.end():]
        print(f"Replaced @media print in {fn}")
    else:
        idx = content.find('</style>')
        if idx != -1:
            content = content[:idx] + "\n" + PERFECT_PRINT_CSS + "\n" + content[idx:]
            print(f"Inserted @media print before </style> in {fn}")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML files updated successfully!")
