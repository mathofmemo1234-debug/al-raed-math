import pymupdf, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')

for p_num in range(22, 27):
    page = doc[p_num-1]
    text = page.get_text()
    print(f"\n==================== PAGE {p_num} ====================")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for l in lines:
        if any(term in l for term in ['صحيحة', 'خاطئة', 'الحل', 'التبرير', 'الإجابة', '✓', '✗']):
            print("  [ALERT]:", l)
        elif 'السؤال' in l:
            print("  [SECTION]:", l)
        elif '(' in l and ')' in l and len(l) < 30:
            print("  [MARK BOX / OPT]:", l)
