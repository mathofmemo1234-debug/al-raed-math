# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- DETAILED CHECK FOR 6B ---")

# 1. Check fractions
fractions = re.findall(r'\\\(.*?\\frac.*?\\\)', text)
print(f"1. Proper vertical fractions in MathJax: {len(fractions)}")
for fr in fractions[:5]:
    print("   -", fr)

# 2. Check for Arabic words in MathJax
all_math = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', text)
ar_words_in_math = []
for m in all_math:
    w = re.findall(r'[\u0621-\u064A]{2,}', m)
    if w:
        ar_words_in_math.append((m, w))
print(f"2. Arabic words in MathJax: {len(ar_words_in_math)}")

# 3. Check vertical calculation tables (sign on right)
vert_tables = text.count('arabic-vert-table')
print(f"3. RTL Vertical calculation tables: {vert_tables}")

# 4. Check for 'والباقي' rendering
print(f"4. 'والباقي' inside math: {text.count(r'\\text{ والباقي }')}")
print(f"   'والباقي' in HTML: {text.count('والباقي')}")

# 5. Check school name
print(f"5. 'منصة الرائد التعليمية بجدة': {text.count('منصة الرائد التعليمية بجدة')}")
print(f"   Old variations: {text.count('مدارس التعلّم الذكي') + text.count('مدارس التعلم الذكي')}")
