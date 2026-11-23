import pymupdf, sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.pdf',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.pdf',
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.pdf'
]

for fn in files:
    doc = pymupdf.open(fn)
    print(f"\n==================== {fn} ====================")
    for i, p in enumerate(doc):
        txt = p.get_text()
        if 'ورقة عمل' in txt or 'أوراق العمل' in txt or 'ورقة' in txt:
            # Check for leaked solution phrases
            leak_words = [
                'الإجابة النموذجية',
                'الحل بالتفصيل',
                'تفسير الإجابة',
                'حل ورقة العمل',
                'نموذج الإجابة',
                'مفتاح الحل'
            ]
            leaks = [w for w in leak_words if w in txt]
            if leaks:
                print(f"Page {i+1}: POSSIBLE LEAK -> {leaks}")
