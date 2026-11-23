import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')
print("Total pages in 6b:", len(doc))
for i in range(15, len(doc)):
    page = doc[i]
    first_line = page.get_text().strip().split('\n')[0][:70]
    print(f"Page {i+1}: {first_line}")
