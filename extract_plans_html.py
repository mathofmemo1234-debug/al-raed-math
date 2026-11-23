# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_plans.py', 'r', encoding='utf-8') as f:
    text = f.read()

# We know:
# 1) PLANS_SECTION_START starts at: <!-- ========================================================================= -->
start_idx = text.find('<!-- ========================================================================= -->')
# 2) PLAN_4_2 starts right after
# 3) Between PLAN_4_2 and PLAN_4_3 there was: """\n\nprint("Plan 4-2 compiled")\n
# Let's clean that out!
html = text[start_idx:]
html = html.replace('"""\n\nprint("Plan 4-2 compiled")', '')
html = html.replace('"""\nprint("Plan 4-2 compiled")', '')
html = html.replace('"""', '')

with open('section_plans.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"section_plans.html written, length: {len(html)}")
# Check all 5 plans exist
import re
plans = re.findall(r'<article class="unit-card" id="(plan-[^"]*)">', html)
print(f"Found plans in section_plans.html: {plans}")
