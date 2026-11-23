# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('HTML character count:', len(html))
print('Starts with <!DOCTYPE html>:', html.startswith('<!DOCTYPE html>'))
print('Ends with </html>:', html.strip().endswith('</html>'))
print('Master sections count:', html.count('class="master-section"'))
print('Unit cards count:', html.count('class="unit-card'))
print('Answer boxes count:', html.count('class="answer-box"'))
print('SVG tags count:', html.count('<svg'))
print('Teacher signature count:', html.count('أ. محمد عبدالله جمعة'))
