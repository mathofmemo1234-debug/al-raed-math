import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="ws-3-2"')
idx2 = html.find('id="ws-3-3"')
snippet = html[idx:idx2]
print("End of ws-3-2 in 1s:")
print(snippet[-1000:])
