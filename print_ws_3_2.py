import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('id="ws-3-2"')
next_idx = html.find('id="ws-3-3"')
snippet = html[idx:next_idx]
# remove base64
clean = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', '', snippet)
print("Full ws-3-2:")
print(clean)
