import os, subprocess, pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_files = [
    ('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.pdf'),
    ('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf'),
    ('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf'),
    ('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')
]

for html, pdf in html_files:
    abs_html = os.path.abspath(html)
    abs_pdf = os.path.abspath(pdf)
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={abs_pdf}',
        abs_html
    ]
    print(f"\nRendering {pdf}...")
    subprocess.run(cmd, check=True)
    doc = pymupdf.open(abs_pdf)
    
    sparse_pages = []
    for i, page in enumerate(doc):
        blocks = page.get_text("blocks")
        if blocks:
            top_y = min(b[1] for b in blocks)
            bot_y = max(b[3] for b in blocks)
            cov = ((bot_y - top_y) / page.rect.height) * 100
        else:
            cov, top_y, bot_y = 0, 0, 0
        if cov < 55:
            txt = page.get_text().strip().replace('\n', ' ')[:50]
            sparse_pages.append((i+1, cov, txt))
            
    print(f"Total Pages: {len(doc)}")
    print(f"Pages with < 55% coverage: {len(sparse_pages)} / {len(doc)}")
    for p, cov, t in sparse_pages:
        print(f"   Page {p:2d} ({cov:.1f}%): {t}")
