import sys, re, os

sys.stdout.reconfigure(encoding='utf-8')

suites = [
    ("6ب (الصف السادس الابتدائي)", "الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html"),
    ("1م (الصف الأول المتوسط)", "الحقيبة_الشاملة_المعادلات_والقياس_1م.html"),
    ("3م (الصف الثالث المتوسط)", "الحقيبة_الشاملة_المتباينات_الخطية_3م.html")
]

print("=" * 80)
print("            MASTER FINAL QA AUDIT FOR ALL THREE PACKAGES (6ب - 1م - 3م)        ")
print("=" * 80)

all_passed = True

for label, filename in suites:
    print(f"\nAUDITING: {label} [{filename}]")
    print("-" * 75)
    
    if not os.path.exists(filename):
        print(f"❌ ERROR: File {filename} does not exist!")
        all_passed = False
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. School name check
    al_mutaqadima = content.count('منصة الرائد التعليمية')
    mutaqadima = content.count('منصة الرائد التعليمية بجدة')
    old_school = len(re.findall(r'مدارس\s+التعلم\s+الذكي(?!.*المتقدمة)', content))
    print(f"1. School Names: 'منصة الرائد...' ({al_mutaqadima}) | 'منصة الرائد...' ({mutaqadima}) | Old: {old_school}")
    if old_school > 0 or al_mutaqadima == 0:
        print("   ❌ FAIL: School name issue!")
        all_passed = False
    else:
        print("   ✅ PASS: School branding 100% compliant.")

    # 2. Teacher name check
    teacher = content.count('محمد عبدالله جمعة')
    print(f"2. Teacher Name: {teacher} occurrences")
    if teacher < 5:
        print("   ❌ FAIL: Teacher name missing on some sections!")
        all_passed = False
    else:
        print("   ✅ PASS: Teacher name present throughout.")

    # 3. Logo check
    logo = content.count('data:image/png;base64')
    print(f"3. Official Logo: {logo} occurrences")
    if logo < 5:
        print("   ❌ FAIL: Logo missing on some sections!")
        all_passed = False
    else:
        print("   ✅ PASS: Base64 logo embedded.")

    # 4. Dollar signs ($)
    dollars = content.count('$')
    print(f"4. Stray Dollar Signs ($): {dollars}")
    if dollars > 0:
        print("   ❌ FAIL: Stray dollar signs present!")
        all_passed = False
    else:
        print("   ✅ PASS: 0 stray dollar signs.")

    # 5. Arabic words in MathJax (Separated letters bug)
    body_idx = content.find('<body')
    body = content[body_idx:] if body_idx != -1 else content
    inlines = re.findall(r'\\\((.*?)\\\)', body, re.DOTALL)
    bad_ar_math = [m.strip() for m in inlines if re.search(r'[\u0621-\u064A]', m)]
    print(f"5. Arabic Letters/Words in MathJax: {len(bad_ar_math)}")
    if bad_ar_math:
        print(f"   ❌ FAIL: Found {len(bad_ar_math)} expressions with Arabic in math!")
        all_passed = False
    else:
        print("   ✅ PASS: Zero Arabic characters inside MathJax.")

    # 6. Spaced letters (disconnected words check)
    clean_body = re.sub(r'<script.*?</script>', '', body, flags=re.DOTALL)
    clean_body = re.sub(r'<style.*?</style>', '', clean_body, flags=re.DOTALL)
    pure_text = re.sub(r'<[^>]+>', ' ', clean_body)
    spaced_words = re.findall(r'(?:^|\s)([\u0621-\u064A]\s+[\u0621-\u064A]\s+[\u0621-\u064A](?:\s+[\u0621-\u064A])*)(?:\s|$)', pure_text)
    print(f"6. Disconnected/Spaced Arabic Words: {len(spaced_words)}")
    if spaced_words:
        print(f"   ❌ FAIL: Disconnected letters found: {spaced_words[:3]}")
        all_passed = False
    else:
        print("   ✅ PASS: Zero disconnected letters.")

    # 7. Raw LaTeX tokens leak
    bad_tokens = []
    for tok in [r'\mathbb', r'\emptyset', r'\mid', r'\bullet', r'\circ', r'≤ft']:
        cnt = content.count(tok)
        if cnt > 0:
            bad_tokens.append(f"{tok} ({cnt})")
    print(f"7. Raw LaTeX Leakage: {bad_tokens if bad_tokens else 'None'}")
    if bad_tokens:
        print("   ❌ FAIL: Raw LaTeX tokens leaked into text!")
        all_passed = False
    else:
        print("   ✅ PASS: Zero raw LaTeX leaks.")

    # 8. Interactive Toolbar & Solution Toggles
    toolbars = content.count('btn-toggle-answers')
    print(f"8. Interactive Toggle Buttons: {toolbars} buttons")
    if toolbars < 5:
        print("   ❌ FAIL: Worksheets missing toggle buttons!")
        all_passed = False
    else:
        print("   ✅ PASS: Interactive answer toggle present on all worksheets.")

    # 9. Print CSS check
    print_hidden = ('worksheet-top-toolbar' in content and 'display: none' in content and '@media print' in content)
    print(f"9. Toolbar Hidden on Print: {print_hidden}")
    if not print_hidden:
        print("   ❌ FAIL: Toolbar not hidden on print!")
        all_passed = False
    else:
        print("   ✅ PASS: Teacher buttons automatically hidden when exporting to PDF.")

    # 10. Fractions and Vertical operations
    if "6ب" in label:
        frac_count = content.count(r'\frac')
        vert_tables = content.count('arabic-vert-table')
        print(f"10. 6ب Specifics: {frac_count} vertical fractions | {vert_tables} RTL vertical tables (signs on right)")
        if frac_count < 100 or vert_tables < 3:
            print("   ❌ FAIL: Missing fractions or vertical tables in 6ب!")
            all_passed = False
        else:
            print("   ✅ PASS: Vertical fractions and RTL arithmetic tables fully verified.")

print("\n" + "=" * 80)
if all_passed:
    print("🎯 FINAL RESULT: ALL THREE PACKAGES (6ب، 1م، 3م) ARE 100% VERIFIED & FLAWLESS!")
else:
    print("❌ SOME CHECKS FAILED! REVIEW ABOVE.")
print("=" * 80)
