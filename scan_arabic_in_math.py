# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # find all \( ... \) and \[ ... \] and $$ ... $$ and $ ... $
    maths = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', content)
    arabic_in_math = []
    for m in maths:
        # check if contains Arabic letters (excluding arabic digits \u0660-\u0669)
        ar_letters = re.findall(r'[\u0621-\u064A]', m)
        if ar_letters:
            arabic_in_math.append((m, ''.join(ar_letters)))
    
    print(f'=== {fname} ===')
    print(f'Total math blocks: {len(maths)}')
    print(f'Math blocks with Arabic letters: {len(arabic_in_math)}')
    for m, letters in arabic_in_math:
        print(f'  Match: {m} -> Letters: {letters}')
