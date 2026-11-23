import sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html']:
    with open(name, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {name} ===")
    cards = c.count('class="worksheet-card')
    print(f"Worksheet cards count: {cards}")
    # find where .worksheet-card appears
    idx = 0
    while True:
        idx = c.find('.worksheet-card', idx)
        if idx == -1: break
        # print the next 200 chars
        print("  Found at:", idx)
        print("    ", c[idx:idx+150].replace('\n', ' '))
        idx += 15
