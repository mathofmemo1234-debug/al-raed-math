# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update generator_header_styles.py
with open('generator_header_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('مدارس التعلم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
text = text.replace('مدارس التعلّم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')

old_mj = r"""inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],"""

new_mj = r"""inlineMath: [['\\(', '\\)']],
                displayMath: [['\\[', '\\]']],"""

text = text.replace(old_mj, new_mj)

with open('generator_header_styles.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generator_header_styles.py updated successfully.")

# 2. Function to clean math in 3m sections
def clean_3m_content(html):
    html = html.replace('مدارس التعلم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
    html = html.replace('مدارس التعلّم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
    
    # Fix the specific paragraph in Think-Pair-Share on negative inequalities where dollars were broken
    # (الحالة الثانية: المعامل عدد سالب ($< ٠$) ... تصبح ... تصبح ...)
    html = re.sub(
        r'🔸\s*الحالة الثانية:\s*المعامل عدد سالب\s*\(\$<\s*٠\$\)\s*</div>\s*'
        r'<div class="tree-leaf">•\s*نضرب أو نقسم الطرفين على العدد السالب\.\s*</div>\s*'
        r'<div class="tree-leaf">•\s*<strong>يجب عكس اتجاه إشارة التباين إجبارياً\s*\(\$\\le\$\s*تصبح\s*\$\\ge\$\s*،\s*و\s*\$>\$\s*تصبح\s*\$<\$\)\.</strong>\s*</div>',
        r'🔸 الحالة الثانية: المعامل عدد سالب (&lt; ٠)</div>\n'
        r'                        <div class="tree-leaf">• نضرب أو نقسم الطرفين على العدد السالب.</div>\n'
        r'                        <div class="tree-leaf">• <strong>يجب عكس اتجاه إشارة التباين إجبارياً (≤ تصبح ≥، و &gt; تصبح &lt;).</strong></div>',
        html
    )
    
    # Replace display math $$ ... $$
    def fix_display_dollar(m):
        inner = m.group(1).strip()
        inner = re.sub(r'\\text\{([\u0621-\u064A٠-٩–\-]+)\}', r'\1', inner)
        inner = inner.replace(r'\text{–}', '−').replace('–', '−')
        return f'<div class="ar-math-display" style="text-align:center; font-size:1.25rem; font-weight:800; color:#1e3a8a; margin:12px 0; direction:rtl;">{inner}</div>'
    
    html = re.sub(r'\$\$([^\$]+)\$\$', fix_display_dollar, html)
    
    # Replace inline math $ ... $
    def fix_inline_dollar(m):
        inner = m.group(1).strip()
        if len(inner) > 150 or '<' in inner or '\n' in inner:
            return inner
        inner = re.sub(r'\\text\{([\u0621-\u064A٠-٩–\-]+)\}', r'\1', inner)
        inner = inner.replace(r'\text{–}', '−').replace(r'\times', '×').replace(r'\div', '÷')
        inner = inner.replace(r'\implies', '⟸').replace(r'\le', '≤').replace(r'\ge', '≥')
        inner = inner.replace(r'\ne', '≠').replace('–', '−')
        
        if r'\frac' in inner:
            return f'\\( {inner} \\)'
        return f'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{inner}</span>'
    
    html = re.sub(r'\$([^\$]+)\$', fix_inline_dollar, html)
    
    return html

for fname in ['section_plans.html', 'section_summaries.html', 'section_worksheets.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_3m_content(content)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"Cleaned {fname}: remaining $ count = {cleaned.count('$')}")
