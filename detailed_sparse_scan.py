import pymupdf, sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf',
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf',
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.pdf'
]

for fn in files:
    doc = pymupdf.open(fn)
    print(f"\n==================== {fn} ({len(doc)} pages) ====================")
    for i, p in enumerate(doc):
        blocks = p.get_text('blocks')
        if blocks:
            top_y = min(b[1] for b in blocks)
            bot_y = max(b[3] for b in blocks)
            cov = (bot_y - top_y) / p.rect.height * 100
        else:
            cov = 0
        txt = p.get_text().strip()
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        if cov < 60:
            print(f"Page {i+1:2d}: cov={cov:.1f}%, lines={len(lines):2d} | Start: {lines[0][:35]}... | End: {lines[-1][:35]}...")
