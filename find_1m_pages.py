# -*- coding: utf-8 -*-
import sys
import fitz # PyMuPDF

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('1m.pdf')
print(f"Total pages in 1m.pdf: {len(doc)}")

# Let's search for printed page numbers 109 to 127
# Or scan pages 95 to 140 to find where printed page 109 is located.

for i in range(len(doc)):
    text = doc[i].get_text()
    if "109" in text or "١٠٩" in text:
        # Check first 200 chars or if it looks like page 109
        first_lines = "\n".join(text.split("\n")[:5])
        print(f"PDF page index {i} mentions 109/١٠٩:\n{first_lines}\n---")
