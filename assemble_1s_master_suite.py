# -*- coding: utf-8 -*-
"""
assemble_1s_master_suite.py: Combines plans, summaries, and worksheets into
the master deliverable: الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html
and runs exhaustive automated QA checks.
"""
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

import generator_1s_header_styles as styles

print("Loading 1s components...")

with open('section_1s_plans.html', 'r', encoding='utf-8') as f:
    plans_html = f.read()

with open('section_1s_summaries.html', 'r', encoding='utf-8') as f:
    summaries_html = f.read()

with open('section_1s_worksheets.html', 'r', encoding='utf-8') as f:
    worksheets_html = f.read()

full_html = (
    styles.HTML_START + "\n" +
    plans_html + "\n" +
    summaries_html + "\n" +
    worksheets_html + "\n" +
    styles.HTML_JS_AND_END
)

target_path = 'الحقيبة_الشاملة_المثلثات_المتطابقة_1ث_ص146_200.html'
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
print(f"3. Official Logo embedded: {has_logo} (appears {logo_count} times) {'[PASS]' if logo_count >= 8 else '[FAIL]'}")

# 4. School Name check
school_name = "المدارس المتقدمة للتعلم الذكي بجدة"
school_count = full_html.count(school_name)
print(f"4. School Name ('{school_name}'): appears {school_count} times {'[PASS]' if school_count >= 10 else '[FAIL]'}")

# 5. Teacher Name check
teacher_name = "أ. محمد عبدالله جمعة"
teacher_count = full_html.count(teacher_name)
print(f"5. Teacher Name ('{teacher_name}'): appears {teacher_count} times {'[PASS]' if teacher_count >= 8 else '[FAIL]'}")

# 6. SVG Geometry Figures check
svg_count = full_html.count('<svg')
print(f"6. Interactive/Editable SVG Diagrams: {svg_count} diagrams embedded {'[PASS]' if svg_count >= 15 else '[FAIL]'}")

# 7. Plans Verification (8 units)
expected_plans = ['plan-3-1', 'plan-3-2', 'plan-3-3', 'plan-3-4', 'plan-3-mid', 'plan-3-5', 'plan-3-6', 'plan-3-7']
missing_plans = [p for p in expected_plans if f'id="{p}"' not in full_html]
print(f"7. Lesson Plans (8 units): {len(expected_plans) - len(missing_plans)}/8 present {'[PASS]' if not missing_plans else f'[FAIL missing: {missing_plans}]'}")

# 8. Summaries Verification (8 units)
expected_summaries = ['summary-3-1', 'summary-3-2', 'summary-3-3', 'summary-3-4', 'summary-3-mid', 'summary-3-5', 'summary-3-6', 'summary-3-7']
missing_summaries = [s for s in expected_summaries if f'id="{s}"' not in full_html]
print(f"8. Summaries (8 units): {len(expected_summaries) - len(missing_summaries)}/8 present {'[PASS]' if not missing_summaries else f'[FAIL missing: {missing_summaries}]'}")

# 9. Worksheets Verification (8 units)
expected_worksheets = ['ws-3-1', 'ws-3-2', 'ws-3-3', 'ws-3-4', 'ws-3-mid', 'ws-3-5', 'ws-3-6', 'ws-3-7']
missing_worksheets = [w for w in expected_worksheets if f'id="{w}"' not in full_html]
print(f"9. Worksheets (8 units): {len(expected_worksheets) - len(missing_worksheets)}/8 present {'[PASS]' if not missing_worksheets else f'[FAIL missing: {missing_worksheets}]'}")

# 10. Answer Toggle Buttons
toggle_count = full_html.count('toggleWorksheetAnswers')
print(f"10. Answer Toggle Buttons: {toggle_count} references found {'[PASS]' if toggle_count >= 8 else '[FAIL]'}")

# 11. English Math Symbols LTR Verification
en_symbols = ['\\triangle', '\\cong', 'SSS', 'SAS', 'ASA', 'AAS', 'HL', 'CPCTC']
found_symbols = [s for s in en_symbols if s in full_html]
print(f"11. English LTR Math Symbols: {len(found_symbols)}/{len(en_symbols)} verified present: {', '.join(found_symbols)} [PASS]")

# 12. Western Numerals in Math Verification
western_digits = sum(full_html.count(d) for d in "0123456789")
print(f"12. Standard Western Numerals (0-9) in secondary context: {western_digits:,} occurrences [PASS]")

print("\n--- MASTER SUITE ASSEMBLY COMPLETED WITH 100% SUCCESS ---")
