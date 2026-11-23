# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def clean_arabic_math_content(html):
    # 1. Update school name
    html = html.replace('مدارس التعلم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
    html = html.replace('مدارس التعلّم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
    
    # 2. Fix the specific paragraph in Think-Pair-Share where dollars were broken
    broken_dollar_pattern = re.compile(
        r'\$\$\s*\\text\{–\}\\text\{٨\}\\text\{ص\}\s*=\s*\\text\{٥٦\}\s*\$\$\s*'
        r'•\s*<em>فكر:</em>([\s\S]*?)•\s*<em>شارك:</em>\s*يعرض ثنائي مختار خطوات التحقق بالتعويض:\s*'
        r'\$\s*\\text\{–\}\\text\{٨\}\s*\\times\s*\(\\text\{–\}\\text\{٧\}\)\s*=\s*\\text\{٥٦\}\s*\$',
        re.MULTILINE
    )
    
    fixed_replacement = (
        r'<div style="text-align:center; font-size:1.25rem; font-weight:800; color:#1e3a8a; margin:10px 0; direction:rtl;">'
        r'−٨ص = ٥٦'
        r'</div>'
        r'• <em>فكر:</em>\1'
        r'• <em>شارك:</em> يعرض ثنائي مختار خطوات التحقق بالتعويض: <span class="ar-math">−٨ × (−٧) = ٥٦</span>'
    )
    html = broken_dollar_pattern.sub(fixed_replacement, html)
    
    # 3. Clean $$ ... $$ blocks
    def fix_display_dollar(m):
        inner = m.group(1).strip()
        # Clean inner of \text{}
        inner = re.sub(r'\\text\{([\u0621-\u064A٠-٩–\-]+)\}', r'\1', inner)
        inner = inner.replace(r'\text{–}', '−').replace('–', '−')
        return f'<div class="ar-math-display" style="text-align:center; font-size:1.25rem; font-weight:800; color:#1e3a8a; margin:12px 0; direction:rtl;">{inner}</div>'
    
    html = re.sub(r'\$\$([^\$]+)\$\$', fix_display_dollar, html)
    
    # 4. Clean $ ... $ inline blocks
    def fix_inline_dollar(m):
        inner = m.group(1).strip()
        # If it has multiline or too long (>150 chars) or contains HTML tags, it's NOT math!
        if len(inner) > 150 or '<' in inner or '\n' in inner:
            return inner
        # Clean \text{} wrappers
        inner = re.sub(r'\\text\{([\u0621-\u064A٠-٩–\-]+)\}', r'\1', inner)
        inner = inner.replace(r'\text{–}', '−').replace(r'\times', '×').replace(r'\div', '÷')
        inner = inner.replace(r'\implies', '⟸').replace(r'\le', '≤').replace(r'\ge', '≥')
        inner = inner.replace(r'\ne', '≠').replace('–', '−')
        
        # If it has \frac, use LaTeX \( ... \)
        if r'\frac' in inner:
            return f'\\( {inner} \\)'
        
        # Otherwise, return clean RTL span
        return f'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{inner}</span>'
    
    html = re.sub(r'\$([^\$]+)\$', fix_inline_dollar, html)
    
    return html

# Process section_1m files
for fname in ['section_1m_plans.html', 'section_1m_summaries.html', 'section_1m_worksheets.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_arabic_math_content(content)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"Cleaned {fname}: remaining $ count = {cleaned.count('$')}")
