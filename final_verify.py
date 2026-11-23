# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

filepath = 'الحقيبة_الشاملة_المتباينات_الخطية_3م.html'
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

print("File exists:", os.path.exists(filepath))
print("File size:", len(c), "chars /", os.path.getsize(filepath), "bytes")
print("Section 1 (Plans) in file:", 'id="plans-section"' in c)
print("Section 2 (Summaries) in file:", 'id="summaries-section"' in c)
print("Section 3 (Worksheets) in file:", 'id="worksheets-section"' in c)
print("Has 4-2 plan:", 'id="plan-4-2"' in c)
print("Has 4-3 plan:", 'id="plan-4-3"' in c)
print("Has mid-quiz plan:", 'id="plan-mid-quiz"' in c)
print("Has algebra lab plan:", 'id="plan-lab"' in c)
print("Has 4-4 plan:", 'id="plan-4-4"' in c)
print("Has 4-2 summary:", 'id="summary-4-2"' in c)
print("Has 4-3 summary:", 'id="summary-4-3"' in c)
print("Has mid-quiz summary:", 'id="summary-mid-quiz"' in c)
print("Has 4-4 summary:", 'id="summary-4-4"' in c)
print("Has 4-2 worksheet:", 'id="ws-4-2"' in c)
print("Has 4-3 worksheet:", 'id="ws-4-3"' in c)
print("Has mid-quiz test:", 'id="ws-mid-quiz"' in c)
print("Has lab worksheet:", 'id="ws-lab"' in c)
print("Has 4-4 worksheet:", 'id="ws-4-4"' in c)
print("Total toggle buttons:", c.count('btn-toggle-answers'))
print("Total school headers with logo:", c.count('class="school-official-header"'))
print("Total teacher signature cards:", c.count('class="teacher-signature-card"'))
