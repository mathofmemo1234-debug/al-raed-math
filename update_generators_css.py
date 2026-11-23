import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')
from apply_perfect_print_css import PERFECT_PRINT_CSS

gen_files = [
    'generator_6b_header_styles.py',
    'generator_1m_header_styles.py',
    'generator_1s_header_styles.py',
    'generator_header_styles.py'
]

for fn in gen_files:
    if not os.path.exists(fn):
        print(f"Skipping {fn} (not found)")
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if @media print is in content
    m = re.search(r'@media\s+print\s*\{.*?\n\}\s*\n', content, re.DOTALL)
    if m:
        content = content[:m.start()] + PERFECT_PRINT_CSS + content[m.end():]
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated @media print in {fn}")
    else:
        print(f"Could not find exact @media print in {fn}")

