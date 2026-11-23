import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf')
print("=== 1M PAGE 14 & 15 ===")
print("Page 14:", doc[13].get_text()[-300:].replace('\n', ' '))
print("Page 15:", doc[14].get_text().replace('\n', ' '))
