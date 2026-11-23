import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        t = f.read()
    
    # Exclude MathJax config block
    body_idx = t.find('<body')
    if body_idx != -1:
        content = t[body_idx:]
    else:
        content = t
        
    inlines = re.findall(r'\\\((.*?)\\\)', content, re.DOTALL)
    bad_inlines = []
    for m in inlines:
        # Check if contains Arabic letters \u0621-\u064A
        if re.search(r'[\u0621-\u064A]', m):
            bad_inlines.append(m.strip())
            
    print(f"=== {fname} ===")
    print(f"  Total MathJax inlines in body: {len(inlines)}")
    print(f"  Inlines with Arabic letters: {len(bad_inlines)}")
    if bad_inlines:
        for b in bad_inlines[:10]:
            print("    BAD:", repr(b))
