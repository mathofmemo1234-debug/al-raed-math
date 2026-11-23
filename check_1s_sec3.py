import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('القسم الثالث: أوراق العمل')
print("Snippet around Section 3 in 1s:")
print(html[idx-100:idx+600])
