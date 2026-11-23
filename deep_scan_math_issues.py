# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"\n==========================================")
    print(f"FILE: {fname}")
    print(f"==========================================")
    
    # 1. Search for vertical arrays
    arrays = re.findall(r'(\\begin\{array\}[\s\S]*?\\end\{array\})', text)
    print(f"Vertical arrays count: {len(arrays)}")
    for a in arrays:
        print("  Array:")
        for l in a.splitlines():
            print("    ", l)
            
    # 2. Search for words in math mode \( ... \) or \[ ... \] or $ ... $
    math_blocks = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|\$[^\$]+\$)', text)
    separated_letter_risks = []
    for mb in math_blocks:
        # check for arabic words (2+ arabic characters)
        ar_words = re.findall(r'[\u0621-\u064A]{2,}', mb)
        if ar_words:
            separated_letter_risks.append((mb, ar_words))
            
    print(f"Math blocks containing Arabic words (risk of separated letters): {len(separated_letter_risks)}")
    for mb, w in separated_letter_risks[:10]:
        print(f"  {mb[:50]} -> {w}")
