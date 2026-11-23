# -*- coding: utf-8 -*-
import re

with open('عرض_السبورة_التفاعلي_الشامل_المثلثات_SSS_SAS.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length:', len(text))
panes = re.findall(r'id="(pane-[^"]+)"', text)
btns = re.findall(r"switchTab\('([^']+)'\)", text)
print('Panes:', panes)
print('Btns:', btns)
print('Match:', set(panes) == set(btns))
