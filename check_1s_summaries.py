import sys, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
# summaries are from page 9 to 14
for p in range(8, 15):
    page = doc[p]
    blocks = page.get_text('blocks')
    top_y = min(b[1] for b in blocks) if blocks else 0
    bot_y = max(b[3] for b in blocks) if blocks else 0
    cov = (bot_y - top_y) / page.rect.height * 100
    first_line = page.get_text().strip().splitlines()[0] if page.get_text().strip() else 'EMPTY'
    print(f"Page {p+1:2d}: cov={cov:.1f}%, first_line: {first_line[:40]}")
