# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('section_6b_worksheets.html', 'r', encoding='utf-8') as f:
    text = f.read()

worksheets = re.findall(r'<article class="worksheet-card" id="(ws-[^"]*)">([\s\S]*?)</article>', text)
print(f"Total worksheets found: {len(worksheets)}")
for wid, wcontent in worksheets:
    print(f"\n{wid}: length={len(wcontent)}")
    print(f"  Toolbar with toggle: {'toggleWorksheetAnswers' in wcontent}")
    print(f"  Header with School: {'المدارس المتقدمة للتعلم الذكي بجدة' in wcontent}")
    print(f"  Logo Base64: {'data:image/png;base64,' in wcontent}")
    print(f"  Teacher Signature: {'محمد عبدالله جمعة' in wcontent}")
    print(f"  Inline solutions: {'inline-solution-block' in wcontent}")
    print(f"  Correct badges: {'correct-badge' in wcontent}")
