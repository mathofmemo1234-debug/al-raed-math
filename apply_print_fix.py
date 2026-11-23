import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# The comprehensive, robust print CSS architecture
PRINT_CSS = """
@page {
    size: A4 portrait;
    margin: 8mm 8mm 10mm 8mm;
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
        font-size: 8.8pt !important;
        line-height: 1.25 !important;
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

    /* Hero Banner: compact at the start */
    .hero-banner {
        box-shadow: none !important;
        border-radius: 4px !important;
        margin-bottom: 8px !important;
        padding: 8px 12px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
    }
    .hero-title {
        font-size: 1.25rem !important;
        margin-bottom: 4px !important;
    }
    .hero-subtitle {
        font-size: 0.8rem !important;
        line-height: 1.25 !important;
    }

    /* Master sections flow continuously without forced page gaps */
    .master-section, .mega-section {
        margin: 0 !important;
        padding: 0 !important;
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }
    .section-title-banner {
        margin: 8px 0 6px 0 !important;
        padding: 6px 10px !important;
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    .section-title-banner h2 {
        font-size: 1.15rem !important;
        margin: 0 !important;
    }
    .section-title-banner p {
        font-size: 0.8rem !important;
        margin: 2px 0 0 0 !important;
    }

    /* Lesson Plans: Natural continuous flow */
    .unit-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 10px !important;
        padding: 8px 10px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: auto !important;
        break-before: auto !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }

    /* Student Summaries: Clean page starts */
    .summary-card, .student-summary-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 10px !important;
        padding: 8px 10px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }
    /* Unless it's the very first summary right after the section banner */
    .section-title-banner + .summary-card,
    .section-title-banner + .student-summary-card {
        page-break-before: avoid !important;
        break-before: avoid !important;
    }

    /* Worksheets: Clean page starts */
    .worksheet-paper, .worksheet-card, .unit-card.worksheet-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        margin-top: 0 !important;
        margin-bottom: 10px !important;
        padding: 8px 10px !important;
        page-break-inside: auto !important;
        break-inside: auto !important;
        page-break-before: page !important;
        break-before: page !important;
        page-break-after: auto !important;
        break-after: auto !important;
    }
    /* Unless it's the very first worksheet right after the section banner */
    .section-title-banner + .worksheet-paper,
    .section-title-banner + .worksheet-card,
    .section-title-banner + .unit-card.worksheet-card {
        page-break-before: avoid !important;
        break-before: avoid !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6,
    .school-official-header, .official-header,
    .ws-meta-bar, .unit-card-header, .plan-header {
        page-break-after: avoid !important;
        break-after: avoid !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    .school-official-header, .official-header {
        padding: 4px 6px !important;
        margin-bottom: 5px !important;
    }
    .sch-logo-center img, .logo-wrapper img {
        max-height: 38px !important;
        width: auto !important;
    }
    .sch-info-right, .sch-info-left-ar {
        font-size: 7.2pt !important;
        line-height: 1.15 !important;
    }
    .school-highlight {
        font-size: 7.8pt !important;
    }

    .ws-meta-bar {
        padding: 3px 6px !important;
        margin-bottom: 5px !important;
        font-size: 7.5pt !important;
    }

    /* Atomic blocks: avoid breaking inside single question, single callout */
    .ws-question-block, .problem-card, .q-item, .question-card,
    .exercise-box, .rule-box, .summary-point, .example-box,
    .national-link-box, .stem-card, .enrichment-challenge {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-bottom: 4px !important;
        padding: 4px 6px !important;
    }

    /* Tables */
    table {
        page-break-inside: auto !important;
        break-inside: auto !important;
        width: 100% !important;
        border-collapse: collapse !important;
        font-size: 7.6pt !important;
        margin-bottom: 4px !important;
    }
    thead {
        display: table-header-group !important;
    }
    tr {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }
    th, td {
        padding: 2px 4px !important;
        line-height: 1.15 !important;
    }

    /* Lined student answer space */
    .student-answer-space {
        min-height: 80px !important;
        margin-top: 5px !important;
        padding: 6px !important;
        border: 1.5px dashed #94a3b8 !important;
        background: #fafafa !important;
        page-break-inside: avoid !important;
        break-inside: avoid !important;
    }

    /* Footers */
    .sheet-footer-bar, .teacher-signature-card, .sig-section {
        page-break-inside: avoid !important;
        break-inside: avoid !important;
        margin-top: 6px !important;
        padding-top: 4px !important;
    }
    .sheet-footer-bar {
        page-break-before: avoid !important;
        break-before: avoid !important;
    }

    /* Inline solution badge hidden in print */
    .inline-answer-badge, .inline-explanation, .problem-solution-inline, .inline-tf-answer {
        display: none !important;
    }

    p {
        margin-top: 1px !important;
        margin-bottom: 2px !important;
    }
}
"""

# Update generator files
generator_files = [
    'generator_header_styles.py',
    'generator_1m_header_styles.py',
    'generator_1s_header_styles.py',
    'generator_6b_header_styles.py'
]

for gf in generator_files:
    if os.path.exists(gf):
        content = open(gf, 'r', encoding='utf-8').read()
        # replace @media print block
        new_content = re.sub(r'@media print\s*\{[\s\S]*?\}\s*\}', PRINT_CSS.strip(), content)
        with open(gf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated generator file: {gf}")

# Update HTML files
suites = [
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html',
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'
]

for sf in suites:
    if os.path.exists(sf):
        content = open(sf, 'r', encoding='utf-8').read()
        new_content = re.sub(r'@media print\s*\{[\s\S]*?\}\s*\}', PRINT_CSS.strip(), content)
        with open(sf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated HTML suite: {sf}")

print("\nAll files successfully patched with unified print optimization!")
