import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"=== {fname} ===")
    for i, line in enumerate(lines):
        if 'problem-solution-inline' in line and '{' in line:
            print(f"  Line {i+1}:")
            for j in range(max(0, i-2), min(len(lines), i+12)):
                print(f"    {j+1}: {lines[j].rstrip()}")
