# -*- coding: utf-8 -*-
import re, sys

sys.stdout.reconfigure(encoding='utf-8')

def convert_latex_to_ar_math(text):
    # Protect script and style tags
    saved_blocks = []
    def save_block(m):
        saved_blocks.append(m.group(0))
        return f"___PROTECTED_BLOCK_{len(saved_blocks)-1}___"
    
    text = re.sub(r'<script[\s\S]*?</script>', save_block, text)
    text = re.sub(r'<style[\s\S]*?</style>', save_block, text)

    # 1. First, handle \frac{...}{...} nested or simple
    # Unpack \text inside first
    for _ in range(5):
        text = re.sub(r'\\text\{([^{}]*)\}', r'\1', text)
    
    # Clean basic math commands
    text = text.replace(r'\times', '×')
    text = text.replace(r'\div', '÷')
    text = text.replace(r'\mathbf', '')
    text = text.replace(r'\rightarrow', '←')
    text = text.replace(r'\leftarrow', '→')
    text = text.replace(r'\neq', '≠')
    text = text.replace(r'\ge', '≥')
    text = text.replace(r'\le', '≤')
    text = text.replace(r'\quad', ' ')
    
    # Handle \frac{top}{bottom}
    # Pattern to match \frac{A}{B} where A and B can have balanced braces
    def replace_frac(m):
        top = m.group(1).strip()
        bot = m.group(2).strip()
        return f'<span class="ar-frac"><span class="num">{top}</span><span class="denom">{bot}</span></span>'

    for _ in range(4):
        text = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', replace_frac, text)
    
    # Fix any remaining broken frac like \frac{؟}{\text{٤}
    text = re.sub(r'\\frac\{([^}]+)\}\{\\text\{([^}]+)\}', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', text)
    text = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', text)

    # Convert \( ... \)
    def replace_inline(m):
        inner = m.group(1).strip()
        # Clean any remaining curly braces
        inner = inner.replace('{', '').replace('}', '')
        # Clean minus signs
        inner = inner.replace(' - ', ' − ')
        return f'<span class="ar-math">{inner}</span>'

    text = re.sub(r'\\\(([\s\S]*?)\\\)', replace_inline, text)
    
    # Convert \[ ... \]
    def replace_display(m):
        inner = m.group(1).strip()
        inner = inner.replace('{', '').replace('}', '')
        inner = inner.replace(' - ', ' − ')
        return f'<div class="ar-math-display" style="text-align:center; font-size:1.15rem; font-weight:800; color:#1e3a8a; margin:10px 0; direction:rtl;">{inner}</div>'

    text = re.sub(r'\\\[([\s\S]*?)\\\]', replace_display, text)

    # Clean double spaces or weird remnants
    # Restore protected blocks
    for i, b in enumerate(saved_blocks):
        text = text.replace(f"___PROTECTED_BLOCK_{i}___", b)
        
    return text

# Test cases
test_samples = [
    r'<strong>١)</strong> ناتج ضرب \( \text{٠,٢} \times \text{٠,٣} = \text{٠,٦} \). <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span>',
    r'<strong>٣)</strong> ناتج طرح: \( \text{٤,٥} - \text{٢,٢٥} = \text{٢,٢٥} \). <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span>',
    r'أوجد ناتج: \( \text{١٥,٦} \div \text{٠,٣} = \text{١٥٦} \div \text{٣} = \mathbf{\text{٥٢}} \)',
    r'الكسر المكافئ هو \( \frac{\text{٢}}{\text{٣}} = \frac{\text{٢} \times \text{٣}}{\text{٣} \times \text{٣}} = \frac{\text{٦}}{\text{٩}} \)',
    r'\( \text{١٢,٤} + \text{٨,٧٥} \)',
    r'محاذاة الفواصل العشرية عمودياً \(\rightarrow\) ملء المنازل الخالية بأصفار \(\rightarrow\) الجمع'
]

for s in test_samples:
    print('ORIGINAL:', s)
    print('CLEANED: ', convert_latex_to_ar_math(s))
    print('-'*50)
