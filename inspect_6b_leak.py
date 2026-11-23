import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    c = f.read()

w_idx = c.find('id="section-worksheets"')
ws1_idx = c.find('class="worksheet-card', w_idx)
ws2_idx = c.find('class="worksheet-card', ws1_idx + 20)
ws1_html = c[ws1_idx:ws2_idx]

print("Length of WS1:", len(ws1_html))

# Let's search for MathJax or SVGs or spans with numbers
for m in re.finditer(r'<([^>]+)>([^<]*25,2|[^<]*٢٥,٢|[^<]*الحرمين|[^<]*0.6|[^<]*٠,٦)[^<]*<', ws1_html):
    print(m.group(0)[:150])

print("\n--- Let's search for any class containing ans, solution, badge, tf ---")
for m in re.findall(r'class="([^"]*(?:ans|sol|badge|tf|correct|key)[^"]*)"', ws1_html):
    print(m)
