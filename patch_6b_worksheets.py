# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_worksheets.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('مدارس التعلم الذكي', 'منصة الرائد التعليمية بجدة')
text = text.replace('مدارس التعلّم الذكي', 'منصة الرائد التعليمية بجدة')

with open('generator_6b_worksheets.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generator_6b_worksheets.py updated successfully.")
