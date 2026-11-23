# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('section_6b_plans.html', 'r', encoding='utf-8') as f:
    text = f.read()

plans = re.findall(r'<article class="unit-card" id="(plan-[^"]*)">([\s\S]*?)</article>', text)
print(f"Total plans found in section_6b_plans.html: {len(plans)}")
for pid, pcontent in plans:
    print(f"\n{pid}: length={len(pcontent)}, words={len(pcontent.split())}")
    print(f"  الحقيبة: {'الحقيبة' in pcontent}")
    print(f"  التمهيد: {'التمهيد' in pcontent}")
    print(f"  جدول KWL: {'KWL' in pcontent}")
    print(f"  بيئة التعلم: {'بيئة التعلم' in pcontent}")
    print(f"  مربع فرير: {'فرير' in pcontent}")
    print(f"  مصفوفة STEM: {'STEM' in pcontent}")
    print(f"  التقويم البنائي: {'التقويم البنائي' in pcontent}")
    print(f"  التقويم الختامي: {'التقويم الختامي' in pcontent}")
    print(f"  الواجب: {'الواجب' in pcontent}")
    print(f"  الغلق: {'الغلق' in pcontent}")
