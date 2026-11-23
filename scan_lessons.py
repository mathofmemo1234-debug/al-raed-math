import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1s.pdf')

print(f"Total pages: {len(doc)}")

# Pages 146 to 200 (PDF index 145 to 199)
lessons = []
for p in range(145, 201):
    page = doc[p]
    text = page.get_text()
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    first_few = " | ".join(lines[:4])
    print(f"Page {p+1} (idx {p}): {first_few}")
