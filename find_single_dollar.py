# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '$' in l:
        print(f"L{i+1}: {l.strip()}")
