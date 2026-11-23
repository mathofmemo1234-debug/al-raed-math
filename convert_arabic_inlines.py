import sys, re

# For 3m
with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    text_3m = f.read()

# Replace \( ... \) in 3m body where there are Arabic letters or inline divisions
def replace_inline_3m(match):
    expr = match.group(1).strip()
    return f'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{expr}</span>'

# Only replace in body
head_3m, sep, body_3m = text_3m.partition('<body')
body_3m = re.sub(r'\\\((.*?)\\\)', replace_inline_3m, body_3m)
text_3m = head_3m + sep + body_3m

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'w', encoding='utf-8') as f:
    f.write(text_3m)

print("3m converted successfully.")

# For 1m
with open('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'r', encoding='utf-8') as f:
    text_1m = f.read()

def replace_inline_1m(match):
    expr = match.group(1).strip()
    return f'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">{expr}</span>'

head_1m, sep, body_1m = text_1m.partition('<body')
body_1m = re.sub(r'\\\((.*?)\\\)', replace_inline_1m, body_1m)
text_1m = head_1m + sep + body_1m

with open('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'w', encoding='utf-8') as f:
    f.write(text_1m)

print("1m converted successfully.")
