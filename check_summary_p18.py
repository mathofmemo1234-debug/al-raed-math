import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')
print("=== PAGE 18 (Summary 2) ===")
print(doc[17].get_text()[:600])
