import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
for p in [18, 19, 21, 22, 23, 24, 25, 26]:
    page = doc[p-1]
    blocks = page.get_text("blocks")
    cov = ((max(b[3] for b in blocks) - min(b[1] for b in blocks)) / page.rect.height) * 100 if blocks else 0
    first_words = page.get_text().strip().replace('\n', ' ')[:80]
    print(f"Page {p:2d} (cov={cov:4.1f}%): {first_words}")
