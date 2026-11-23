import pymupdf, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.pdf')
# check page 18
page = doc[17]
text = page.get_text()

# Check for explanation text that is inside inline-solution-block
explanation_phrases = [
    'التوضيح والخطوات',
    'الخيار الصحيح هو',
    'التعليل النموذجي',
    'الخطوات التفصيلية',
    'نقوم بجمع الأعداد العشرية بمحاذاة الفواصل'
]

for ep in explanation_phrases:
    if ep in text:
        print(f"FOUND EXPLANATION: {ep}")
    else:
        print(f"NOT found (correctly hidden): {ep}")
