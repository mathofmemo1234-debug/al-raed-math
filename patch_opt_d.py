# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'section_worksheets.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace(
        '<span>(د) {س | س < –٤}</span>',
        '<span>(د) <span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{س | س < –٤}</span></span>'
    )
    text = text.replace(
        '<span>(د) {ص | ص < ٤}</span>',
        '<span>(د) <span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{ص | ص < ٤}</span></span>'
    )
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)

print("Updated styling for option (د).")
