import os, subprocess, pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
html_files = [
    ('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf'),
    ('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf'),
    ('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf'),
    ('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.pdf')
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
    print(f"\n==========================================")
    print(f"Rendering {pdf}...")
    subprocess.run(cmd, check=True)
    doc = pymupdf.open(abs_pdf)
    print(f"Total Pages: {len(doc)}")
    
    sparse_pages = []
    leaks = []
    for i, page in enumerate(doc):
        blocks = page.get_text("blocks")
        txt = page.get_text()
        if blocks:
            top_y = min(b[1] for b in blocks)
            bot_y = max(b[3] for b in blocks)
            cov = ((bot_y - top_y) / page.rect.height) * 100
        else:
            cov, top_y, bot_y = 0, 0, 0
            
        if cov < 55:
            first_line = txt.strip().splitlines()[0] if txt.strip() else 'EMPTY'
            sparse_pages.append((i+1, cov, first_line[:50]))
            
        # Check answer leaks
        for bad in ['الإجابة النموذجية', 'الحل بالتفصيل', 'تفسير الإجابة', 'الخيار الصحيح هو']:
            if bad in txt and ('ورقة عمل' in txt or 'أوراق العمل' in txt or 'ورقة' in txt):
                leaks.append((i+1, bad))

    print(f"Pages with < 55% coverage: {len(sparse_pages)} / {len(doc)}")
    for p, cov, t in sparse_pages:
        print(f"   Page {p:2d} ({cov:.1f}%): {t}")
    if leaks:
        print(f"   [WARNING] Leaks found: {leaks}")
    else:
        print(f"   [SUCCESS] Zero answer leaks!")

