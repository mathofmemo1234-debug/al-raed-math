import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="worksheets-section"')
end_pos = c.find('</section>', pos)
ws_html = c[pos:end_pos]

articles = re.findall(r'<article class="worksheet-paper"[^>]*>(.*?)</article>', ws_html, re.DOTALL)
print(f"Total worksheet articles in 1m: {len(articles)}")

for i, art in enumerate(articles):
    q_titles = re.findall(r'<(?:h3|h4|div)[^>]*class="[^"]*(?:ws-q-title|question-header|title)[^"]*"[^>]*>(.*?)</', art)
    print(f"\n--- Worksheet {i+1} ---")
    for qt in q_titles:
        print("  Q:", re.sub(r'<[^>]+>', '', qt).strip())
