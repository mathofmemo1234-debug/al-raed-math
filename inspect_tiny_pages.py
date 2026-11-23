import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

# Inspect 1m Page 17
doc_1m = pymupdf.open('الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf')
print("=== 1M PAGE 16 & 17 ===")
print("Page 16:", doc_1m[15].get_text()[-300:].replace('\n', ' '))
print("Page 17:", doc_1m[16].get_text().replace('\n', ' '))
print("Page 18:", doc_1m[17].get_text()[:300].replace('\n', ' '))

# Inspect 1s Page 19, 25, 27
doc_1s = pymupdf.open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf')
print("\n=== 1S PAGE 18, 19, 20 ===")
print("Page 18:", doc_1s[17].get_text()[-200:].replace('\n', ' '))
print("Page 19:", doc_1s[18].get_text().replace('\n', ' '))
print("Page 20:", doc_1s[19].get_text()[:200].replace('\n', ' '))

print("\n=== 1S PAGE 25 & 27 ===")
print("Page 25:", doc_1s[24].get_text().replace('\n', ' '))
print("Page 27:", doc_1s[26].get_text().replace('\n', ' '))
