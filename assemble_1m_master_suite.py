# -*- coding: utf-8 -*-
"""
assemble_1m_master_suite.py: Assembles the complete suite for Grade 7 (1m) pages 109 to 127
and executes comprehensive QA checks.
"""
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

import generator_1m_header_styles

print("Loading 1m components...")

with open('section_1m_plans.html', 'r', encoding='utf-8') as f:
    plans_html = f.read()

with open('section_1m_summaries.html', 'r', encoding='utf-8') as f:
    summaries_html = f.read()

with open('section_1m_worksheets.html', 'r', encoding='utf-8') as f:
    worksheets_html = f.read()

full_html = (
    generator_1m_header_styles.HTML_START +
    plans_html +
    summaries_html +
    worksheets_html +
    generator_1m_header_styles.HTML_JS_AND_END
)

target_path = 'الحقيبة_الشاملة_المعادلات_والقياس_1م.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

file_size = os.path.getsize(target_path)
print(f"Master file written: {target_path}")
print(f"File size: {file_size:,} bytes ({len(full_html):,} characters)")

# =========================================================================
# COMPREHENSIVE QUALITY ASSURANCE CHECKS
# =========================================================================
print("\n--- Running Comprehensive Quality Assurance Checks ---")

# 1. Form-feed characters (\x0c)
ff_count = full_html.count('\x0c')
print(f"1. Form-feed count (\\x0c): {ff_count} {'[PASS]' if ff_count == 0 else '[FAIL]'}")

# 2. Math input error keywords
err_count = full_html.count('Math input error')
print(f"2. 'Math input error' occurrences: {err_count} {'[PASS]' if err_count == 0 else '[FAIL]'}")

# 3. Base64 logo check
has_logo = 'data:image/png;base64,' in full_html
logo_count = full_html.count('data:image/png;base64,')
print(f"3. Official Logo embedded: {has_logo} (appears {logo_count} times) {'[PASS]' if logo_count >= 10 else '[FAIL]'}")

# 4. School Name check
school_name = "منصة الرائد التعليمية"
school_count = full_html.count(school_name)
print(f"4. School Name '{school_name}': appears {school_count} times {'[PASS]' if school_count >= 10 else '[FAIL]'}")

# 5. Teacher Name check
teacher_name = "محمد عبدالله جمعة"
teacher_count = full_html.count(teacher_name)
print(f"5. Teacher Name '{teacher_name}': appears {teacher_count} times {'[PASS]' if teacher_count >= 10 else '[FAIL]'}")

# 6. Check all plans
plans_found = re.findall(r'<article class="unit-card" id="(plan-[^"]*)">', full_html)
print(f"6. Lesson Plans: {plans_found} (Count: {len(plans_found)}) {'[PASS]' if len(plans_found) == 5 else '[FAIL]'}")

# 7. Check all summaries
summaries_found = re.findall(r'<article class="summary-card" id="(summary-[^"]*)">', full_html)
print(f"7. Student Summaries: {summaries_found} (Count: {len(summaries_found)}) {'[PASS]' if len(summaries_found) == 5 else '[FAIL]'}")

# 8. Check all worksheets
worksheets_found = re.findall(r'<article class="worksheet-paper" id="(ws-[^"]*)">', full_html)
print(f"8. Worksheets: {worksheets_found} (Count: {len(worksheets_found)}) {'[PASS]' if len(worksheets_found) == 5 else '[FAIL]'}")

# 9. Check worksheet top toggle buttons
toolbar_buttons = full_html.count('onclick="toggleWorksheetAnswers(')
print(f"9. Worksheet Top Toggle Buttons: {toolbar_buttons} {'[PASS]' if toolbar_buttons == 5 else '[FAIL]'}")

# 10. Check inline solutions
inline_badge_count = full_html.count('inline-answer-badge')
inline_exp_count = full_html.count('inline-explanation')
inline_sol_count = full_html.count('problem-solution-inline')
print(f"10. Inline Solution Elements: badges={inline_badge_count}, explanations={inline_exp_count}, solutions={inline_sol_count} {'[PASS]' if inline_sol_count >= 5 else '[FAIL]'}")

# 11. Check print rules hiding no-print & top toolbar
has_print_rule = '.worksheet-top-toolbar' in full_html and '.no-print { display: none !important; }' in full_html
print(f"11. Print CSS hiding toggle toolbar: {has_print_rule} {'[PASS]' if has_print_rule else '[FAIL]'}")

# 12. Check Western Arabic numerals (0-9) in visible text
clean = re.sub(r'<style[\s\S]*?</style>|<script[\s\S]*?</script>|data:image/png;base64,[A-Za-z0-9+/=]+', '', full_html)
clean = re.sub(r'<[^>]+>', ' ', clean)
ascii_digits = re.findall(r'([0-9]+)', clean)
print(f"12. ASCII digits [0-9] in visible text: {len(ascii_digits)} found. Top: {ascii_digits[:10]}")
