# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # find $...$
    math_dollar = re.findall(r'\$([^\$]+)\$', text)
    arabic_in_dollar = []
    for m in math_dollar:
        ar_letters = re.findall(r'[\u0621-\u064A]', m)
        if ar_letters:
            arabic_in_dollar.append((m, ''.join(ar_letters)))
    
    print(f"\n--- {fname} ---")
    print(f"Total $ blocks: {len(math_dollar)}")
    print(f"$ blocks with Arabic letters: {len(arabic_in_dollar)}")
    for m, letters in arabic_in_dollar:
        print(f"  ${m}$ -> {letters}")
