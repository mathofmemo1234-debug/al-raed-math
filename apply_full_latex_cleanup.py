# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def full_latex_clean(text):
    # Protect script and style tags
    saved_blocks = []
    def save_block(m):
        saved_blocks.append(m.group(0))
        return f"___PROTECTED_BLOCK_{len(saved_blocks)-1}___"
    
    text = re.sub(r'<script[\s\S]*?</script>', save_block, text)
    text = re.sub(r'<style[\s\S]*?</style>', save_block, text)
    text = re.sub(r'\\\[[\s\S]*?\\\]', save_block, text)
    
    # Clean LaTeX math symbols outside display math
    text = text.replace(r'\mathbb{R}', '( ح )')
    text = text.replace(r'\emptyset', '∅')
    text = text.replace(r'\mid', '|')
    text = text.replace(r'\le', '≤').replace(r'\ge', '≥')
    text = text.replace(r'\implies', '⟸')
    text = text.replace(r'\times', '×').replace(r'\div', '÷')
    text = text.replace(r'\quad', ' ')
    text = text.replace(r'\left(', '(').replace(r'\right)', ')')
    text = text.replace(r'\left[', '[').replace(r'\right]', ']')
    
    # Unpack nested \text{...}
    count = 0
    while r'\text{' in text and count < 10:
        text = re.sub(r'\\text\{([^\}\{]*)\}', r'\1', text)
        count += 1
        
    text = text.replace(r'\{', '{').replace(r'\}', '}')
    
    # Clean any remaining \frac outside math
    def clean_frac(m):
        top = m.group(1).strip()
        bot = m.group(2).strip()
        return f"({top} ÷ {bot})"
    text = re.sub(r'\\frac\{([^\}]+)\}\{([^\}]+)\}', clean_frac, text)
    
    # Restore protected blocks
    for i, b in enumerate(saved_blocks):
        text = text.replace(f"___PROTECTED_BLOCK_{i}___", b)
        
    return text

files_to_clean = [
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html',
    'section_plans.html', 'section_summaries.html', 'section_worksheets.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'section_1m_plans.html', 'section_1m_summaries.html', 'section_1m_worksheets.html',
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html',
    'section_6b_plans.html', 'section_6b_summaries.html', 'section_6b_worksheets.html'
]

for fname in files_to_clean:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned = full_latex_clean(content)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"Cleaned {fname} [SUCCESS]")
    except Exception as e:
        print(f"Error cleaning {fname}: {e}")

print("\nAll files cleaned successfully.")
