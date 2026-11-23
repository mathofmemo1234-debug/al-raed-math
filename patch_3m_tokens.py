import sys

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace \bullet with ● and \circ with ○
text = text.replace(r'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">\bullet</span>', '<span style="font-size:1.2rem; color:#1e3a8a;">●</span>')
text = text.replace(r'<span class="ar-math" style="direction:rtl; font-weight:700; color:#1e3a8a;">\circ</span>', '<span style="font-size:1.2rem; color:#1e3a8a;">○</span>')
text = text.replace(r'\bullet', '●')
text = text.replace(r'\circ', '○')
text = text.replace('≤ft', '')

with open('الحقيبة_الشاملة_المتباينات_الخطية_3م.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patched 3m tokens successfully.")
