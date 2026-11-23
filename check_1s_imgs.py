import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

for ws_id in ['ws-3-2', 'ws-3-3', 'ws-3-4']:
    idx = html.find(f'id="{ws_id}"')
    next_idx = html.find('id="ws-', idx + 10)
    ws_html = html[idx:next_idx]
    imgs = re.findall(r'<img[^>]+>', ws_html)
    print(f"\n{ws_id} has {len(imgs)} images:")
    for img in imgs:
        # don't print base64 data
        clean = re.sub(r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+', '[BASE64]', img)
        print(" ", clean[:150])
