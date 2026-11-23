# -*- coding: utf-8 -*-
"""
clean_and_verify_all_math.py
Standardizes math direction across all grade levels:
1. Elementary (6b) & Intermediate (1m, 3m):
   - Math & Writing: ALWAYS 100% Right-To-Left (RTL) in Arabic.
   - Arabic-Indic numerals (٠، ١، ٢، ٣...).
   - No MathJax (MathJax forces LTR which inverts Arabic operations).
   - Use native RTL HTML with .ar-math and .ar-frac.
2. Secondary (1s):
   - Writing: Right-To-Left (Arabic).
   - Math: Left-To-Right (English notation with MathJax).
"""
import re
import sys
import os
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

def convert_latex_to_ar_math(content):
    # 1. Protect <script> and <style>
    saved_blocks = []
    def save_block(m):
        saved_blocks.append(m.group(0))
        return f"___PROTECTED_BLOCK_{len(saved_blocks)-1}___"
    
    content = re.sub(r'<script[\s\S]*?</script>', save_block, content)
    content = re.sub(r'<style[\s\S]*?</style>', save_block, content)

    # 2. Repeatedly unwrap nested \text{...}
    for _ in range(6):
        content = re.sub(r'\\text\{([^{}]*)\}', r'\1', content)

    # 3. Handle standard LaTeX commands
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

    # 4. Handle vertical fractions: \frac{num}{denom} -> <span class="ar-frac"><span class="num">num</span><span class="denom">denom</span></span>
    def replace_frac(m):
        top = m.group(1).strip()
        bot = m.group(2).strip()
        return f'<span class="ar-frac"><span class="num">{top}</span><span class="denom">{bot}</span></span>'

    for _ in range(4):
        content = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', replace_frac, content)
    
    # Catch broken or partially closed fractions like \frac{؟}{\text{٤} or \frac{أ}{ب
    content = re.sub(r'\\frac\{([^}]+)\}\{\\text\{([^}]+)\}', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', content)
    content = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)', r'<span class="ar-frac"><span class="num">\1</span><span class="denom">\2</span></span>', content)

    # 5. Handle inline math \( ... \)
    def replace_inline(m):
        inner = m.group(1).strip()
        inner = inner.replace('{', '').replace('}', '')
        inner = re.sub(r'\s*-\s*', ' − ', inner) # standard Arabic minus
        if not inner:
            return ''
        return f'<span class="ar-math">{inner}</span>'

    content = re.sub(r'\\\(([\s\S]*?)\\\)', replace_inline, content)

    # 6. Handle display math \[ ... \]
    def replace_display(m):
        inner = m.group(1).strip()
        inner = inner.replace('{', '').replace('}', '')
        inner = re.sub(r'\s*-\s*', ' − ', inner)
        return f'<div class="ar-math-display">{inner}</div>'

    content = re.sub(r'\\\[([\s\S]*?)\\\]', replace_display, content)

    # 7. Restore protected blocks
    for i, b in enumerate(saved_blocks):
        content = content.replace(f"___PROTECTED_BLOCK_{i}___", b)

    return content

print("--- STEP 1: Updating generator_6b_header_styles.py ---")
with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    hdr = f.read()

# Replace MathJax in generator_6b_header_styles.py with RTL Arabic Math Styles
old_mathjax_block = re.search(r'<!-- MathJax 3[\s\S]*?<script id="MathJax-script"[\s\S]*?</script>', hdr)
if old_mathjax_block:
    rtl_math_styles = """<!-- Native Arabic RTL Mathematics Styles (Strictly Right-to-Left, No MathJax) -->
    <style>
        .ar-math {
            direction: rtl;
            unicode-bidi: isolate;
            font-weight: 700;
            color: #1e3a8a;
            padding: 0 2px;
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
            text-align: center;
            font-size: 1.15rem;
            font-weight: 800;
            color: #1e3a8a;
            margin: 10px 0;
            direction: rtl;
        }
    </style>"""
    hdr = hdr[:old_mathjax_block.start()] + rtl_math_styles + hdr[old_mathjax_block.end():]
    with open('generator_6b_header_styles.py', 'w', encoding='utf-8') as f:
        f.write(hdr)
    print("generator_6b_header_styles.py: MathJax removed and Arabic RTL styles added! [SUCCESS]")
else:
    print("generator_6b_header_styles.py: MathJax block not found or already replaced.")

print("\n--- STEP 2: Cleaning 6b section files ---")
files_6b = ['section_6b_plans.html', 'section_6b_summaries.html', 'section_6b_worksheets.html']
for fname in files_6b:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    orig_inlines = len(re.findall(r'\\\(', c))
    cleaned = convert_latex_to_ar_math(c)
    rem_inlines = len(re.findall(r'\\\(', cleaned))
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"{fname}: Converted {orig_inlines} LaTeX blocks -> Remaining: {rem_inlines} [SUCCESS]")

print("\n--- STEP 3: Cleaning 6b generator files ---")
generators_6b = ['generator_6b_worksheets.py', 'generator_6b_summaries.py', 'build_6b_plans.py', 'append_6b_plans_full.py']
for fname in generators_6b:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        orig_inlines = len(re.findall(r'\\\(', c))
        cleaned = convert_latex_to_ar_math(c)
        rem_inlines = len(re.findall(r'\\\(', cleaned))
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"{fname}: Converted {orig_inlines} LaTeX blocks -> Remaining: {rem_inlines} [SUCCESS]")

print("\n--- STEP 4: Cleaning lingering LaTeX in 1m and 3m section files ---")
intermediate_files = ['section_1m_plans.html', 'section_1m_worksheets.html', 'section_plans.html', 'section_worksheets.html']
for fname in intermediate_files:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        orig_inlines = len(re.findall(r'\\\(', c))
        cleaned = convert_latex_to_ar_math(c)
        rem_inlines = len(re.findall(r'\\\(', cleaned))
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"{fname}: Converted {orig_inlines} LaTeX blocks -> Remaining: {rem_inlines} [SUCCESS]")

print("\n--- STEP 5: Reassembling 6b Master Suite ---")
subprocess.run([sys.executable, 'assemble_6b_master_suite.py'], check=True)

# Also check master html directly for any lingering mathjax or latex
with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    master_c = f.read()
master_inlines = len(re.findall(r'\\\(', master_c))
print(f"Master 6b HTML remaining LaTeX delimiters: {master_inlines}")
print(f"Master 6b HTML has MathJax: {'MathJax' in master_c}")

print("\n--- STEP 6: Re-rendering 6b PDF with Chrome Headless ---")
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
print("6b PDF re-rendered successfully!")

print("\nAll steps completed successfully.")
