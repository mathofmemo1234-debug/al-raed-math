import pymupdf, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
p15 = doc[14]
p16 = doc[15]

print("Page 15 rect:", p15.rect)
blocks15 = p15.get_text('blocks')
blocks16 = p16.get_text('blocks')

print(f"Page 15 blocks count: {len(blocks15)}, max_y: {max(b[3] for b in blocks15)}")
print(f"Page 16 blocks count: {len(blocks16)}, min_y: {min(b[1] for b in blocks16)}, max_y: {max(b[3] for b in blocks16)}")
