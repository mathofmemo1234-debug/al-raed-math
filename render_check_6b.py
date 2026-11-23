import subprocess, os, sys, pymupdf

sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'
pdf_file = 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf'

abs_html = os.path.abspath(html_file)
abs_pdf = os.path.abspath(pdf_file)

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={abs_pdf}',
    abs_html
]

print("Rendering 6b to PDF...")
subprocess.run(cmd, check=True)
print("Rendering done.")

doc = pymupdf.open(abs_pdf)
print(f"Total pages in 6b PDF: {len(doc)}")

sparse_pages = []
for i, page in enumerate(doc):
    blocks = page.get_text("blocks")
    if blocks:
        top_y = min(b[1] for b in blocks)
        bot_y = max(b[3] for b in blocks)
        cov = ((bot_y - top_y) / page.rect.height) * 100
    else:
        cov, top_y, bot_y = 0, 0, 0
    
    txt = page.get_text().strip().replace('\n', ' ')[:65]
    if cov < 55:
        sparse_pages.append((i+1, cov, txt))
    print(f"Page {i+1:2d}: cov={cov:5.1f}%, top={top_y:5.1f}, bot={bot_y:5.1f} | {txt}")

print(f"\nTotal pages with cov < 55%: {len(sparse_pages)} / {len(doc)}")
