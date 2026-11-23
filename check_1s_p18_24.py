import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
for p in [18, 19, 20, 21, 22, 23, 24]:
    page = doc[p-1]
    blocks = page.get_text("blocks")
    top_y = min(b[1] for b in blocks) if blocks else 0
    bot_y = max(b[3] for b in blocks) if blocks else 0
    cov = ((bot_y - top_y) / page.rect.height) * 100 if blocks else 0
    text = page.get_text().strip().replace('\n', ' ')
    first_line = text[:60]
    last_line = text[-60:]
    print(f"Page {p:2d} (cov={cov:4.1f}%): [FIRST]: {first_line} | [LAST]: {last_line}")
