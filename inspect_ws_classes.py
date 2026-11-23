import sys
sys.stdout.reconfigure(encoding='utf-8')

for name in ['الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html']:
    with open(name, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\n=== {name} ===")
    w_idx = c.find('id="section-worksheets"')
    if w_idx != -1:
        snippet = c[w_idx:w_idx+2000]
        # find the first few tags with class
        import re
        tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*class="([^"]*)"', snippet)
        print("First tags after section-worksheets:", tags[:10])
