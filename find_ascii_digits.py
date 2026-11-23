# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'\b([0-9]+)\b', text):
    # Only if not inside tag attributes
    idx = m.start()
    before = text[max(0, idx-40):idx]
    after = text[idx:min(len(text), idx+40)]
    if '="' not in before and 'px' not in after and 'class' not in before and 'id' not in before:
        print(f"Context: ...{before} [ {m.group()} ] {after}...")
