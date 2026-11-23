# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- QA VERIFICATION FOR 1M ---")
print("1. 'مدارس التعلم الذكي' count:", text.count('مدارس التعلم الذكي'))
print("2. 'مدارس التعلّم الذكي' count:", text.count('مدارس التعلّم الذكي'))
print("3. 'مدارس المتقدمة للتعلم الذكي بجدة' count:", text.count('مدارس المتقدمة للتعلم الذكي بجدة'))
print("4. Remaining $ count:", text.count('$'))

math_blocks = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', text)
ar_in_math = []
for mb in math_blocks:
    # check for 2+ consecutive arabic letters
    words = re.findall(r'[\u0621-\u064A]{2,}', mb)
    if words:
        ar_in_math.append((mb, words))

print(f"5. Math blocks with Arabic words: {len(ar_in_math)}")
for mb, w in ar_in_math[:10]:
    print("   ", mb[:60], "->", w)
