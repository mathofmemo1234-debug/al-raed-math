# -*- coding: utf-8 -*-
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1m.pdf')

for idx in range(105, 132):
    text = doc[idx].get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_few = " | ".join(lines[:4])
    print(f"PDF Index {idx}: {first_few[:100]}")
