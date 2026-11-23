# -*- coding: utf-8 -*-
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob("*.html") + glob.glob("*.py"):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        c1 = content.count('مدارس التعلم الذكي')
        c2 = content.count('مدارس التعلّم الذكي')
        if c1 > 0 or c2 > 0:
            print(f"{f}: 'مدارس التعلم الذكي'={c1}, 'مدارس التعلّم الذكي'={c2}")
    except Exception as e:
        pass
