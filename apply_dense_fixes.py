import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

UNIFIED_PRINT_CSS = """
@page {
    size: A4 portrait;
    margin: 5mm 6mm 5mm 6mm;
}

@media print {
    /* Hide screen-only interactive elements */
    .no-print, .sticky-nav, .worksheet-top-toolbar, .print-btn-header, .btn-toggle-answers {
        display: none !important;
    }

    /* Base typography for dense, professional A4 print */
    html, body {
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 7.8pt !important;
        line-height: 1.18 !important;
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

    /* Hero Banner: compact at the start of Page 1 without forcing page break */
    .hero-banner {
        box-shadow: none !important;
        border-radius: 4px !important;
        margin-bottom: 3px !important;
        padding: 3px 6px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
    }
    .hero-title {
        font-size: 1.12rem !important;
        margin-bottom: 2px !important;
    }
    .hero-subtitle {
        font-size: 0.72rem !important;
        line-height: 1.15 !important;
    }

    /* Section 1 (Plans) starts immediately under Hero Banner on Page 1 */
    #section-plans, #plans-section,
    .section-header-banner.plans,
    .hero-banner + #section-plans,
    .hero-banner + #plans-section,
    .hero-banner + .section-header-banner.plans,
    .hero-banner + .mega-section,
    .hero-banner + .master-section {
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    /* Section 2 (Summaries) and Section 3 (Worksheets) start cleanly at the top of fresh pages */
    #section-summaries, #section-worksheets,
    #summaries-section, #worksheets-section,
    .section-header-banner.summaries, .section-header-banner.worksheets {
        page-break-before: page !important;
        break-before: page !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    .section-banner, .section-header-banner, .section-title-banner {
        margin: 0 0 3px 0 !important;
        padding: 3px 6px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .section-banner h2, .section-header-banner h2, .section-title-banner h2 {
        font-size: 1.0rem !important;
        margin: 0 !important;
    }
    .section-banner p, .section-header-banner p, .section-title-banner p {
        font-size: 0.70rem !important;
        margin: 1px 0 0 0 !important;
    }

    /* Lesson Plans: Natural continuous flow with compact spacing */
    .unit-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 3px !important;
        padding: 3px 5px !important;
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
        margin: 2px 0 !important;
        padding: 2px 4px !important;
    }

    /* Student Summaries: Clean page starts with balanced vertical rhythm */
    .summary-card, .student-summary-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 4px !important;
        padding: 5px 8px !important;
        font-size: 8.0pt !important;
        line-height: 1.22 !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }

    .student-summary-card .summary-point,
    .student-summary-card .rule-box,
    .summary-card .summary-point,
    .summary-card .rule-box {
        margin-bottom: 2px !important;
        padding: 2px 5px !important;
    }

    /* Worksheets: Clean page starts by default */
    .worksheet-paper, .worksheet-card, .unit-card.worksheet-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 3px !important;
        padding: 3px 5px !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }

    /* The first card immediately inside any section banner must NEVER break to a new page */
    .section-banner + .student-summary-card,
    .section-banner + .worksheet-card,
    .section-banner + article,
    .section-header-banner + .summary-card,
    .section-header-banner + .student-summary-card,
    .section-header-banner + .worksheet-paper,
    .section-header-banner + .unit-card,
    .section-header-banner + .worksheet-card,
    .section-header-banner + article,
    .section-header-banner.worksheets + article,
    .section-header-banner.worksheets + .unit-card.worksheet-card,
    .section-header-banner.summaries + article,
    .section-header-banner.summaries + .summary-card,
    .section-title-banner + .summary-card,
    .section-title-banner + .student-summary-card,
    .section-title-banner + .worksheet-paper,
    .section-title-banner + .worksheet-card,
    .section-title-banner + article {
        page-break-before: avoid !important;
        break-before: avoid !important;
    }

    /* 6b worksheets fit cleanly on 1 page each */
    #section-worksheets .worksheet-card {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    /* 1s, 1m, 3m worksheets flow cleanly across pages */
    #worksheets-section .worksheet-card,
    .worksheet-paper {
        page-break-inside: auto !important;
        break-inside: auto !important;
    }

    /* Scale SVG geometry diagrams cleanly in print so they don't force page overflows */
    svg {
        max-height: 85px !important;
        width: auto !important;
    }
    .svg-diagram-wrapper, .geo-svg-container, .diagram-container {
        margin: 2px 0 !important;
        padding: 2px !important;
        text-align: center !important;
    }

    /* Headers inside worksheets & summaries */
    .school-official-header, .official-header {
        padding: 2px 3px !important;
        margin-bottom: 2px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .sch-logo-center img, .logo-wrapper img, .header-logo-box img {
        max-height: 22px !important;
        width: auto !important;
    }
    .sch-info-right, .sch-info-left-ar, .header-ministry {
        font-size: 6.4pt !important;
        line-height: 1.1 !important;
    }
    .school-highlight {
        font-size: 6.8pt !important;
    }

    .ws-title-strip, .unit-title-box {
        padding: 2px 3px !important;
        margin-bottom: 2px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .ws-title-strip h3, .unit-title-box h3 {
        font-size: 7.4pt !important;
        margin: 0 !important;
    }

    .student-info-grid, .ws-meta-bar {
        padding: 2px 3px !important;
        margin-bottom: 2px !important;
        font-size: 6.5pt !important;
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
        margin-top: 1px !important;
        margin-bottom: 1px !important;
    }
    .ws-sec-heading, .ws-q-title {
        font-size: 7.2pt !important;
    }

    /* Atomic blocks: avoid breaking inside single question, single callout */
    .ws-question-block, .problem-card, .q-item, .question-card, .q-card, .tf-item,
    .exercise-box, .rule-box, .summary-point, .example-box,
    .national-link-box, .stem-card, .enrichment-challenge {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-bottom: 1.5px !important;
        padding: 1.5px 3px !important;
    }

    .q-text, .tf-text {
        font-size: 7.0pt !important;
        margin-bottom: 1px !important;
    }

    .mcq-options-grid, .mcq-options-vertical {
        gap: 1.5px !important;
        margin: 1.5px 0 !important;
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

    /* Generous student answer space on multi-page worksheets (1m & 3m) to eliminate voids */
    .student-answer-space {
        min-height: 130px !important;
        margin-top: 3px !important;
        padding: 4px !important;
        border: 1.5px dashed #94a3b8 !important;
        background: #fafafa !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    .student-work-area {
        min-height: 65px !important;
        margin-top: 1.5px !important;
        padding: 2.5px !important;
        border: 1.5px dashed #94a3b8 !important;
        background: #fafafa !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* Footers: strictly avoid breaking before footer alone */
    .sheet-footer-bar, .teacher-signature-card, .sig-section {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        page-break-before: avoid !important;
        break-before: avoid !important;
        margin-top: 1.5px !important;
        padding-top: 1px !important;
        font-size: 6.2pt !important;
    }

    /* COMPLETE SUPPRESSION OF ALL WORKSHEET ANSWERS IN PRINT & PDF */
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

    /* Force all MCQ options to appear completely neutral and identical in print */
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

    p {
        margin-top: 1px !important;
        margin-bottom: 1px !important;
    }
}
"""

generator_files = [
    'generator_header_styles.py',
    'generator_1m_header_styles.py',
    'generator_1s_header_styles.py',
    'generator_6b_header_styles.py'
]

for gf in generator_files:
    if os.path.exists(gf):
        content = open(gf, 'r', encoding='utf-8').read()
        new_content = re.sub(r'@media print\s*\{[\s\S]*?\}\s*\}', UNIFIED_PRINT_CSS.strip(), content)
        with open(gf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated generator file: {gf}")

suites = [
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html',
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'
]

for sf in suites:
    if os.path.exists(sf):
        content = open(sf, 'r', encoding='utf-8').read()
        new_content = re.sub(r'@media print\s*\{[\s\S]*?\}\s*\}', UNIFIED_PRINT_CSS.strip(), content)
        with open(sf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated HTML suite: {sf}")

print("Applying changes complete.")
