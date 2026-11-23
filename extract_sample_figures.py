import sys
import os
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1s.pdf')
out_dir = 'figures_1s'
os.makedirs(out_dir, exist_ok=True)

# Let's inspect pages and extract key figures or render high-res thumbnails/crops
print("Extracting key page figures...")
# We can render specific page regions at 2x or 3x resolution (dpi=150 or 200)
mat = pymupdf.Matrix(2.0, 2.0) # 2x zoom for crisp text & line art

sample_pages = [146, 147, 148, 149, 150, 154, 155, 156, 158, 162, 163, 164, 170, 172, 174, 178, 179, 180, 182, 188, 189, 190, 196, 197, 199]

for p in sample_pages:
    # 0-indexed page is p-1
    page = doc[p-1]
    pix = page.get_pixmap(matrix=mat)
    # Save a rendered image of the page or check drawings
    # We can also detect drawings rectangles
    drawings = page.get_drawings()
    rects = [d['rect'] for d in drawings if d['rect'].width > 50 and d['rect'].height > 50]
    print(f"Page {p}: size={page.rect}, {len(rects)} large drawing rects")

print("Done scanning sample pages.")
