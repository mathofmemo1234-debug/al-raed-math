import sys
import os
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1s.pdf')

os.makedirs('figures_1s', exist_ok=True)

print("Scanning pages 146 to 200 for embedded images and drawings...")
image_count_per_page = {}
for pno in range(145, 201):
    page = doc[pno]
    imgs = page.get_images()
    drawings = page.get_drawings()
    print(f"Page {pno+1}: {len(imgs)} images, {len(drawings)} vector drawings")
