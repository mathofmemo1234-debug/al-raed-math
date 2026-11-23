import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for name in ['الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html']:
    with open(name, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"\n=== {name} ===")
    # find all sections or main divs
    secs = re.findall(r'<section[^>]*id="([^"]*)"', c)
    print("Section IDs:", secs)
    if not secs:
        div_ids = re.findall(r'<div[^>]*id="([^"]*)"', c)
        print("Div IDs:", [d for d in div_ids if 'section' in d or 'work' in d or 'sheet' in d or 'part' in d])
    # find where "أوراق العمل" appears
    pos = c.find('أوراق العمل')
    if pos != -1:
        print("Context around 'أوراق العمل':")
        print(c[max(0, pos-150):pos+250])
