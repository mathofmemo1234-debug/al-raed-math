import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('id="section-plans"')
end_pos = c.find('id="section-summaries"')
plans_html = c[pos:end_pos]

tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*class="([^"]*)"', plans_html[:2000])
print("Tags in section-plans:", tags)

# Check what cards exist
cards = re.findall(r'<div[^>]*class="([^"]*plan[^"]*|[^"]*unit[^"]*)"', plans_html)
print("Plan/unit cards:", set(cards))
