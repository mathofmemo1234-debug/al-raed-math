import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

for ws_num in range(1, 9):
    ws_id = f'ws-3-{ws_num}' if ws_num != 5 else 'ws-mid-ch3'
    idx = html.find(f'id="{ws_id}"')
    if idx == -1:
        # try find ws-
        continue
    # find next ws or end
    next_idx = html.find('id="ws-', idx + 10)
    if next_idx == -1: next_idx = html.find('</section>', idx)
    ws_content = html[idx:next_idx]
    
    questions = re.findall(r'<div class="question-header">[\s\S]*?</div>', ws_content)
    clean_q = [re.sub(r'<[^>]+>', ' ', q).strip() for q in questions]
    print(f"\nWorksheet {ws_id} (Length: {len(ws_content)} chars):")
    for q in clean_q:
        print("  ", q.replace('\n', ' '))
