import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for name in ['الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html']:
    with open(name, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\n=== {name} ===")
    pos = c.find('id="worksheets-section"')
    snippet = c[pos:pos+3000]
    articles = re.findall(r'<article[^>]*class="([^"]*)"', snippet)
    print("Article classes inside worksheets-section:", articles[:5])
    divs = re.findall(r'<div[^>]*class="([^"]*)"', snippet)
    print("Div classes inside worksheets-section:", divs[:10])
