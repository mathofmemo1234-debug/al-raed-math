import sys, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')
print("=== Page 3 text ===")
print(doc[2].get_text()[-400:])
print("=== Page 4 text ===")
print(doc[3].get_text()[:400])
