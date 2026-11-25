# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

suites = [
    ('6ب (السادس الابتدائي)', 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'),
    ('1م (الأول المتوسط)', 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html'),
    ('3م (الثالث المتوسط)', 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html'),
]

all_passed = True

print("================================================================================")
print("              COMPREHENSIVE FINAL QA AUDIT FOR ALL THREE SUITES                 ")
print("================================================================================")

for label, fname in suites:
    print(f"\nAUDITING: {label} [{fname}]")
    print("-" * 75)
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. School name check
    old_sch1 = content.count('مدارس التعلم الذكي')
    old_sch2 = content.count('مدارس التعلّم الذكي')
    new_sch = content.count('منصة الرائد التعليمية بجدة')
    pass_sch = (old_sch1 == 0 and old_sch2 == 0 and new_sch >= 10)
    print(f"1. School Name Update: {new_sch} occurrences | Old variations: {old_sch1 + old_sch2} -> {'[PASS]' if pass_sch else '[FAIL]'}")
    if not pass_sch: all_passed = False
    
    # 2. Dollar sign check
    dollar_count = content.count('$')
    pass_dollar = (dollar_count == 0)
    print(f"2. Dollar signs ($) removed: {dollar_count} remaining -> {'[PASS]' if pass_dollar else '[FAIL]'}")
    if not pass_dollar: all_passed = False
    
    # 3. Arabic words inside MathJax (separated letter risk)
    math_blocks = re.findall(r'(\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\])', content)
    ar_in_math = []
    for mb in math_blocks:
        words = re.findall(r'[\u0621-\u064A]{2,}', mb)
        if words:
            ar_in_math.append((mb, words))
    pass_words = (len(ar_in_math) == 0)
    print(f"3. Arabic words inside MathJax (separated letter bug): {len(ar_in_math)} -> {'[PASS]' if pass_words else '[FAIL]'}")
    if not pass_words:
        all_passed = False
        for mb, w in ar_in_math[:3]:
            print("   Example:", mb[:60], "->", w)
            
    # 4. LaTeX arrays for vertical operations
    array_count = content.count(r'\begin{array}')
    pass_arrays = (array_count == 0)
    print(f"4. LTR LaTeX arrays removed (displaced sign bug): {array_count} -> {'[PASS]' if pass_arrays else '[FAIL]'}")
    if not pass_arrays: all_passed = False
    
    # 5. Teacher signature
    teacher_count = content.count('محمد عبدالله جمعة')
    pass_teacher = (teacher_count >= 10)
    print(f"5. Teacher Name ('محمد عبدالله جمعة'): {teacher_count} occurrences -> {'[PASS]' if pass_teacher else '[FAIL]'}")
    if not pass_teacher: all_passed = False

    # 6. Logo embedding
    logo_count = content.count('data:image/png;base64,')
    pass_logo = (logo_count >= 8)
    print(f"6. Official Logo Base64: {logo_count} occurrences -> {'[PASS]' if pass_logo else '[FAIL]'}")
    if not pass_logo: all_passed = False

    # 7. Form-feeds and Math input error
    ff_count = content.count('\x0c')
    mie_count = content.count('Math input error')
    pass_clean = (ff_count == 0 and mie_count == 0)
    print(f"7. Form-feeds: {ff_count} | 'Math input error': {mie_count} -> {'[PASS]' if pass_clean else '[FAIL]'}")
    if not pass_clean: all_passed = False

print("\n================================================================================")
print(f"OVERALL AUDIT RESULT: {'ALL TESTS PASSED WITH 100% SUCCESS!' if all_passed else 'SOME TESTS FAILED'}")
print("================================================================================")
