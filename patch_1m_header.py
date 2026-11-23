# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_1m_header_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update school name
text = text.replace('مدارس التعلم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
text = text.replace('مدارس التعلّم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')

# 2. Update MathJax config (remove '$')
old_mj = r"""inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],"""

new_mj = r"""inlineMath: [['\\(', '\\)']],
                displayMath: [['\\[', '\\]']],"""

text = text.replace(old_mj, new_mj)

with open('generator_1m_header_styles.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generator_1m_header_styles.py updated successfully.")
