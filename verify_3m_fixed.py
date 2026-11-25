# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- QA VERIFICATION FOR 3M ---")
print("1. 'مدارس التعلم الذكي' count:", text.count('مدارس التعلم الذكي'))
print("2. 'مدارس التعلّم الذكي' count:", text.count('مدارس التعلّم الذكي'))
print("3. 'منصة الرائد التعليمية بجدة' count:", text.count('منصة الرائد التعليمية بجدة'))
print("4. Remaining $ count:", text.count('$'))

math_blocks = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', text)
ar_in_math = []
for mb in math_blocks:
    words = re.findall(r'[\u0621-\u064A]{2,}', mb)
    if words:
        ar_in_math.append((mb, words))

print(f"5. Math blocks with Arabic words: {len(ar_in_math)}")
for mb, w in ar_in_math[:10]:
    print("   ", mb[:60], "->", w)
