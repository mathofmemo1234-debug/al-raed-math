# -*- coding: utf-8 -*-
"""
assemble_6b_master_suite.py: Combines plans, summaries, and worksheets into
the single master deliverable: الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html
and runs exhaustive automated QA checks.
"""
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

from generator_6b_header_styles import HTML_START, HTML_JS_AND_END

print("Reading section files...")
with open('section_6b_plans.html', 'r', encoding='utf-8') as f:
    plans_html = f.read()

with open('section_6b_summaries.html', 'r', encoding='utf-8') as f:
    summaries_html = f.read()

with open('section_6b_worksheets.html', 'r', encoding='utf-8') as f:
    worksheets_html = f.read()

master_html = HTML_START + "\n" + plans_html + "\n" + summaries_html + "\n" + worksheets_html + "\n" + HTML_JS_AND_END

out_path = 'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(master_html)

print(f"Master suite written successfully to {out_path}!")
print(f"Total file size: {len(master_html):,} characters ({len(master_html.encode('utf-8')) / 1024:.1f} KB).")

# QA CHECKS
print("\n--- RUNNING QA CHECKS ---")

# 1. Check for form-feed characters (\x0c)
ff_count = master_html.count('\x0c')
print(f"1. Form-feed characters (\\x0c): {ff_count} {'[PASS]' if ff_count == 0 else '[FAIL]'}")

# 2. Check for Math input error text
mie_count = master_html.count('Math input error')
print(f"2. 'Math input error' text occurrences: {mie_count} {'[PASS]' if mie_count == 0 else '[FAIL]'}")

# 3. Check for School Name
school_count = master_html.count('منصة الرائد التعليمية')
print(f"3. School Name occurrences: {school_count} {'[PASS]' if school_count >= 10 else '[FAIL]'}")

# 4. Check for Teacher Name
teacher_count = master_html.count('محمد عبدالله جمعة')
print(f"4. Teacher Name occurrences: {teacher_count} {'[PASS]' if teacher_count >= 10 else '[FAIL]'}")

# 5. Check for Logo Base64
logo_count = master_html.count('data:image/png;base64,')
print(f"5. Logo Base64 occurrences: {logo_count} {'[PASS]' if logo_count >= 10 else '[FAIL]'}")

# 6. Check for Toggle Buttons
toggle_count = master_html.count('toggleWorksheetAnswers')
print(f"6. Worksheet Toggle Buttons: {toggle_count} {'[PASS]' if toggle_count == 5 else '[FAIL]'}")

# 7. Check for Units/Lessons Coverage
plans_count = len(re.findall(r'<article class="unit-card"', master_html))
summaries_count = len(re.findall(r'<article class="student-summary-card"', master_html))
ws_count = len(re.findall(r'<article class="worksheet-card"', master_html))
print(f"7. Lesson Plans count: {plans_count} (Expected: 5) {'[PASS]' if plans_count == 5 else '[FAIL]'}")
print(f"   Student Summaries count: {summaries_count} (Expected: 5) {'[PASS]' if summaries_count == 5 else '[FAIL]'}")
print(f"   Worksheets count: {ws_count} (Expected: 5) {'[PASS]' if ws_count == 5 else '[FAIL]'}")

# 8. Check @media print rule
has_print_rule = '@media print' in master_html and '.worksheet-top-toolbar' in master_html and 'display: none !important' in master_html
print(f"8. @media print rule hiding toolbar: {'[PASS]' if has_print_rule else '[FAIL]'}")

