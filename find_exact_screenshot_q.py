# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'مجموعة الأعداد الحقيقية' in l and ('emptyset' in l or 'mathbb' in l or 'أ)' in l or '(أ)' in l):
        print(f"L{i+1}:")
        for j in range(max(0, i-2), min(len(lines), i+12)):
            print(f"  {lines[j]}")
        print("="*60)
