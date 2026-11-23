# -*- coding: utf-8 -*-
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob("*.html"):
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    if r'\frac{المساحة}{الطول}' in t:
        print(f"Found in {f}")
        t = t.replace(r'\( العرض = \frac{المساحة}{الطول} \)', r'<span class="ar-math">العرض = المساحة ÷ الطول</span>')
        t = t.replace(r'\frac{المساحة}{الطول}', r'(المساحة ÷ الطول)')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(t)
        print(f"Replaced in {f}")
