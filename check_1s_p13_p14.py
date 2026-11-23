import sys, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
print("=== Page 13 text ===")
print(doc[12].get_text()[-300:])
print("=== Page 14 text ===")
print(doc[13].get_text())
