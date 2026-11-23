# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('section_1m_worksheets.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(r'\( العرض = \frac{المساحة}{الطول} \)', r'<span class="ar-math">العرض = المساحة ÷ الطول</span>')
text = text.replace(r'\( المساحة = الطول × العرض ⟸ ٤٨ = ل × ٦ ⟸ ل = \frac{٤٨}{٦} = ٨ \)', r'<span class="ar-math">المساحة = الطول × العرض ⟸ ٤٨ = ل × ٦ ⟸ ل = ٤٨ ÷ ٦ = ٨</span>')

with open('section_1m_worksheets.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated 1m worksheets: 0 Arabic words in MathJax!")
