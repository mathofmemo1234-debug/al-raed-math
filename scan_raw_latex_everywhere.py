# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

latex_commands = [
    r'\\mathbb', r'\\emptyset', r'\\mid', r'\\text', r'\\le', r'\\ge',
    r'\\implies', r'\\times', r'\\div', r'\\frac', r'\\{', r'\\}', r'\\quad', r'\\begin'
]

files = [
    'الحقيبة_الشاملة_المتباينات_الخطية_3م.html',
    'الحقيبة_الشاملة_المعادلات_والقياس_1م.html',
    'الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html',
    'section_plans.html', 'section_summaries.html', 'section_worksheets.html',
    'section_1m_plans.html', 'section_1m_summaries.html', 'section_1m_worksheets.html',
    'section_6b_plans.html', 'section_6b_summaries.html', 'section_6b_worksheets.html'
]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        continue
    
    # Remove properly enclosed math \( ... \) and \[ ... \]
    cleaned = re.sub(r'\\\(.*?\\\)', '', content, flags=re.DOTALL)
    cleaned = re.sub(r'\\\[.*?\\\]', '', cleaned, flags=re.DOTALL)
    
    # Also ignore inside <script> and <style>
    cleaned = re.sub(r'<script[\s\S]*?</script>', '', cleaned)
    cleaned = re.sub(r'<style[\s\S]*?</style>', '', cleaned)
    
    # Search for any unescaped / raw LaTeX commands in the cleaned HTML
    found_cmds = {}
    for cmd in latex_commands:
        matches = re.findall(cmd, cleaned)
        if matches:
            found_cmds[cmd] = len(matches)
            
    if found_cmds:
        print(f"=== {fname} ===")
        for cmd, cnt in found_cmds.items():
            print(f"  {cmd}: {cnt}")
            # print sample
            sample = re.findall(r'([^>\n]{0,30}' + cmd + r'[^<\n]{0,30})', cleaned)
            for s in sample[:3]:
                print(f"    sample: {s.strip()}")
