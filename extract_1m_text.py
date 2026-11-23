# -*- coding: utf-8 -*-
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1m.pdf')

full_text = []
for idx in range(108, 127):
    page_text = doc[idx].get_text()
    full_text.append(f"\n{'='*40}\nPDF INDEX {idx} | PRINTED PAGE ~{idx+1}\n{'='*40}\n")
    full_text.append(page_text)

extracted_text = "".join(full_text)
with open('extracted_1m_pages_109_127.txt', 'w', encoding='utf-8') as f:
    f.write(extracted_text)

print(f"Extracted pages 109-127 from 1m.pdf: {len(extracted_text)} chars")
