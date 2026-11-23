# -*- coding: utf-8 -*-
import re, sys, os, subprocess, pymupdf

sys.stdout.reconfigure(encoding='utf-8')

def tokenize_ar_math(expr):
    frac_map = {}
    def save_frac(m):
        key = f"___FRAC_{len(frac_map)}___"
        frac_map[key] = m.group(0)
        return f" {key} "
    
    clean_expr = re.sub(r'<span class="ar-frac">[\s\S]*?</span>\s*</span>', save_frac, expr)
    
    other_map = {}
    def save_tag(m):
        key = f"___TAG_{len(other_map)}___"
        other_map[key] = m.group(0)
        return f" {key} "
    
    clean_expr = re.sub(r'<[^>]+>', save_tag, clean_expr)
    
    # Split by operators and whitespace
    parts = re.split(r'(\s+|[=×÷+−≤≥<>≠←→⟸]|(?<=\s)-(?=\s))', clean_expr)
    
    span_tokens = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        for k, v in frac_map.items():
            p = p.replace(k, v)
        for k, v in other_map.items():
            p = p.replace(k, v)
            
        if p.startswith('<span class="ar-frac">') and p.endswith('</span>'):
            span_tokens.append(p)
        else:
            span_tokens.append(f'<span>{p}</span>')
            
    if len(span_tokens) <= 1:
        # Just restore and return inner text without extra span
        res = clean_expr
        for k, v in frac_map.items():
            res = res.replace(k, v)
        for k, v in other_map.items():
            res = res.replace(k, v)
        return res.strip()
        
    return ' '.join(span_tokens)

def convert_latex_to_ar_math(content):
    saved_blocks = []
    def save_block(m):
        saved_blocks.append(m.group(0))
        return f"___PROTECTED_BLOCK_{len(saved_blocks)-1}___"
    
    content = re.sub(r'<script[\s\S]*?</script>', save_block, content)
    content = re.sub(r'<style[\s\S]*?</style>', save_block, content)

    for _ in range(6):
        content = re.sub(r'\\text\{([^{}]*)\}', r'\1', content)

    content = content.replace(r'\times', '×')
    content = content.replace(r'\div', '÷')
    content = content.replace(r'\mathbf', '')
    content = content.replace(r'\rightarrow', '←')
    content = content.replace(r'\leftarrow', '→')
    content = content.replace(r'\neq', '≠')
    content = content.replace(r'\ge', '≥')
    content = content.replace(r'\le', '≤')
    content = content.replace(r'\quad', ' ')
    content = content.replace(r'\approx', '≈')

    def replace_frac(m):
        top = m.group(1).strip()
        bot = m.group(2).strip()
        return f'<span class="ar-frac"><span class="num">{top}</span><span class="denom">{bot}</span></span>'

    for _ in range(4):
        content = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', replace_frac, content)
    
    content = re.sub(r'\\frac\{([^}]+)\}\{\\text\{([^}]+)\}', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', content)
    content = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', content)

    def replace_inline(m):
        inner = m.group(1).strip()
        inner = inner.replace('{', '').replace('}', '')
        inner = re.sub(r'\s*-\s*', ' − ', inner)
        if not inner:
            return ''
        tokenized = tokenize_ar_math(inner)
        return f'<span class="ar-math">{tokenized}</span>'

    content = re.sub(r'\\\(([\s\S]*?)\\\)', replace_inline, content)

    # If there are existing <span class="ar-math"> without inner spans from previous run, tokenize them
    def re_tokenize(m):
        inner = m.group(1)
        if '<span>' in inner or '<span class="ar-frac">' in inner:
            return m.group(0)
        tokenized = tokenize_ar_math(inner)
        return f'<span class="ar-math">{tokenized}</span>'

    content = re.sub(r'<span class="ar-math">([\s\S]*?)</span>', re_tokenize, content)

    def replace_display(m):
        inner = m.group(1).strip()
        inner = inner.replace('{', '').replace('}', '')
        inner = re.sub(r'\s*-\s*', ' − ', inner)
        tokenized = tokenize_ar_math(inner)
        return f'<div class="ar-math-display">{tokenized}</div>'

    content = re.sub(r'\\\[([\s\S]*?)\\\]', replace_display, content)

    for i, b in enumerate(saved_blocks):
        content = content.replace(f"___PROTECTED_BLOCK_{i}___", b)

    return content

# 1. Update generator_6b_header_styles.py
with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    hdr = f.read()

# Update ar-math CSS in generator_6b_header_styles.py
css_pattern = r'/\* Native Arabic RTL Mathematics Styles[\s\S]*?</style>'
new_css = """/* Native Arabic RTL Mathematics Styles (Strictly Right-to-Left, No MathJax) */
    <style>
        .ar-math {
            display: inline-flex;
            flex-direction: row;
            direction: rtl;
            align-items: center;
            gap: 0.25em;
            font-weight: 700;
            color: #1e3a8a;
            vertical-align: middle;
        }
        .ar-frac {
            display: inline-flex;
            flex-direction: column;
            vertical-align: middle;
            text-align: center;
            padding: 0 3px;
            font-size: 0.95em;
            line-height: 1.1;
        }
        .ar-frac .num {
            border-bottom: 1.5px solid currentColor;
            padding-bottom: 1px;
        }
        .ar-frac .denom {
            padding-top: 1px;
        }
        .ar-math-display {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            gap: 0.35em;
            direction: rtl;
            font-size: 1.15rem;
            font-weight: 800;
            color: #1e3a8a;
            margin: 10px 0;
        }
    </style>"""

if re.search(css_pattern, hdr):
    hdr = re.sub(css_pattern, new_css, hdr)
    with open('generator_6b_header_styles.py', 'w', encoding='utf-8') as f:
        f.write(hdr)
    print("Updated generator_6b_header_styles.py CSS!")

# 2. Clean section_6b files
for fname in ['section_6b_plans.html', 'section_6b_summaries.html', 'section_6b_worksheets.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    c = convert_latex_to_ar_math(c)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Tokenized {fname} successfully!")

# 3. Reassemble
subprocess.run([sys.executable, 'assemble_6b_master_suite.py'], check=True)

# 4. Render to PDF
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_path = os.path.abspath('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html')
pdf_path = os.path.abspath('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    html_path
]
subprocess.run(cmd, check=True)
print("PDF rendered successfully!")

# 5. Crop True/False section on page 15
doc = pymupdf.open(pdf_path)
page = doc[14]
clip = pymupdf.Rect(0, 330, page.rect.width, 500)
pix = page.get_pixmap(dpi=200, clip=clip)
pix.save('page_15_tf_verified.png')
print("Saved page_15_tf_verified.png!")

# 6. Extract visual word order
words = page.get_text('words', clip=clip)
from collections import defaultdict
lines = defaultdict(list)
for w in words:
    line_y = round(w[1] / 8) * 8
    lines[line_y].append(w)

print("\n=== EXTRACTED VISUAL ORDER IN VERIFIED PDF ===")
for y in sorted(lines.keys()):
    row = sorted(lines[y], key=lambda w: -w[0])
    text_rtl = ' '.join(w[4] for w in row)
    print(f'y={y:3d}: {text_rtl}')
