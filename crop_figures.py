import sys
import os
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('1s.pdf')
out_dir = 'figures_1s'
os.makedirs(out_dir, exist_ok=True)

# For each lesson, let's capture representative figure regions from the textbook pages:
# Lesson 3-1: pages 146-152 (idx 145-151)
# Lesson 3-2: pages 153-161 (idx 152-160)
# Lesson 3-3: pages 162-169 (idx 161-168)
# Lesson 3-4: pages 170-177 (idx 169-176)
# Mid-quiz: page 178 (idx 177)
# Lesson 3-5: pages 179-187 (idx 178-186)
# Lesson 3-6: pages 188-195 (idx 187-194)
# Lesson 3-7: pages 196-200 (idx 195-199)

mat = pymupdf.Matrix(2.0, 2.0) # 2x zoom for sharp images

crops = [
    # (name, page_num, rect_normalized: (x0, y0, x1, y1) in fraction of page)
    ("fig_3_1_classify_angles", 146, (0.05, 0.45, 0.95, 0.85)),
    ("fig_3_1_classify_sides", 148, (0.05, 0.20, 0.95, 0.60)),
    ("fig_3_1_check_1", 147, (0.50, 0.15, 0.95, 0.45)),
    ("fig_3_2_angle_sum", 154, (0.05, 0.25, 0.95, 0.65)),
    ("fig_3_2_exterior_angle", 156, (0.05, 0.20, 0.95, 0.55)),
    ("fig_3_2_exercises", 158, (0.05, 0.15, 0.95, 0.60)),
    ("fig_3_3_congruence_def", 162, (0.05, 0.30, 0.95, 0.70)),
    ("fig_3_3_third_angles", 164, (0.05, 0.20, 0.95, 0.55)),
    ("fig_3_4_sss_postulate", 170, (0.05, 0.30, 0.95, 0.65)),
    ("fig_3_4_sas_postulate", 172, (0.05, 0.25, 0.95, 0.65)),
    ("fig_3_mid_quiz", 178, (0.05, 0.15, 0.95, 0.65)),
    ("fig_3_5_asa_aas", 179, (0.05, 0.30, 0.95, 0.75)),
    ("fig_3_5_summary_cases", 182, (0.05, 0.10, 0.95, 0.60)),
    ("fig_3_5_right_triangles", 186, (0.05, 0.20, 0.95, 0.65)),
    ("fig_3_6_isosceles_thm", 188, (0.05, 0.30, 0.95, 0.70)),
    ("fig_3_6_equilateral", 190, (0.05, 0.20, 0.95, 0.60)),
    ("fig_3_7_coord_placement", 196, (0.05, 0.40, 0.95, 0.85)),
    ("fig_3_7_coord_proof", 198, (0.05, 0.20, 0.95, 0.65)),
]

for name, pno, norm_box in crops:
    page = doc[pno - 1]
    w = page.rect.width
    h = page.rect.height
    clip = pymupdf.Rect(norm_box[0]*w, norm_box[1]*h, norm_box[2]*w, norm_box[3]*h)
    pix = page.get_pixmap(matrix=mat, clip=clip)
    out_path = os.path.join(out_dir, f"{name}.png")
    pix.save(out_path)
    print(f"Saved {out_path} ({pix.width}x{pix.height})")

print("All crop figures extracted successfully.")
