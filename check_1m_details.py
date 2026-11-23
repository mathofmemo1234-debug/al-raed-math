import pymupdf, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf')
print("Total pages in 1m:", len(doc))

# Pages 20 to 28
for p_idx in range(19, len(doc)):
    page = doc[p_idx]
    blocks = page.get_text('blocks')
    txt = page.get_text().strip()
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    if blocks:
        top_y = min(b[1] for b in blocks)
        bot_y = max(b[3] for b in blocks)
        span = bot_y - top_y
    else:
        span = 0
    print(f"Page {p_idx+1}: span={span:.1f} pt, lines={len(lines)}, First line: {lines[0][:50] if lines else 'EMPTY'}")
