# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('section_6b_summaries.html', 'r', encoding='utf-8') as f:
    text = f.read()

summaries = re.findall(r'<article class="student-summary-card" id="(summary-[^"]*)">([\s\S]*?)</article>', text)
print(f"Total student summaries found: {len(summaries)}")
for sid, scontent in summaries:
    print(f"\n{sid}: length={len(scontent)}")
    print(f"  Header with School: {'المدارس المتقدمة للتعلم الذكي بجدة' in scontent}")
    print(f"  Logo Base64: {'data:image/png;base64,' in scontent}")
    print(f"  Teacher Signature: {'محمد عبدالله جمعة' in scontent}")
