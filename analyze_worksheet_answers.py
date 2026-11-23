import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html',
    'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html'
]

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    
    print(f"=== {fn} ===")
    
    # Check if there is toggleWorksheetAnswers or .answer-box or .correct-opt or .tf-ans-box
    print("Has .answer-box:", ".answer-box" in html)
    print("Has .correct-badge:", ".correct-badge" in html)
    print("Has .correct-opt:", ".correct-opt" in html)
    print("Has .tf-ans-box:", ".tf-ans-box" in html)
    print("Has .tf-badge:", ".tf-badge" in html)
    
    # Check print CSS for worksheets
    print_matches = re.findall(r'@media print\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}', html)
    print(f"Found {len(print_matches)} @media print blocks")
    for pm in print_matches:
        if any(w in pm for w in ['answer', 'badge', 'correct', 'worksheet', 'tf']):
            print("  Print rule match snippet:", pm[:200].replace('\n', ' '))
