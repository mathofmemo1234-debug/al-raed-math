# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2550, 2595):
    if i < len(lines):
        print(f"L{i+1}: {lines[i].rstrip()}")
