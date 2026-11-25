# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- QA VERIFICATION FOR 6B ---")
print("1. 'مدارس التعلم الذكي' count:", text.count('مدارس التعلم الذكي'))
print("2. 'مدارس التعلّم الذكي' count:", text.count('مدارس التعلّم الذكي'))
print("3. 'منصة الرائد التعليمية بجدة' count:", text.count('منصة الرائد التعليمية بجدة'))
print("4. LaTeX array count:", text.count(r'\begin{array}'))
print("5. Arabic vert table count:", text.count('arabic-vert-table'))

math_blocks = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', text)
ar_in_math = []
for mb in math_blocks:
    letters = re.findall(r'[\u0621-\u064A]', mb)
    if letters:
        ar_in_math.append((mb, ''.join(letters)))

print(f"6. Math blocks with Arabic letters: {len(ar_in_math)}")
for mb, l in ar_in_math:
    print("   ", mb, "->", l)
