# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update build_6b_plans.py
with open('build_6b_plans.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace vertical array
old_array = r"""\[
                                \begin{array}{r@{\quad}l}
                                  \text{١٢,٤٠} \\
                                + \ \text{٠٨,٧٥} \\
                                \hline
                                  \text{٢١,١٥}
                                \end{array}
                                \]"""

new_table = r"""<div class="arabic-vert-calc-wrapper">
                                    <table class="arabic-vert-table">
                                        <caption>خطوات الجمع الرأسي (الرمز على اليمين):</caption>
                                        <tr><td class="sign-col"></td><td class="num-col">١٢,٤٠</td></tr>
                                        <tr class="op-divider"><td class="sign-col">+</td><td class="num-col">٠٨,٧٥</td></tr>
                                        <tr class="res-row"><td class="sign-col"></td><td class="num-col">٢١,١٥</td></tr>
                                    </table>
                                </div>"""

if old_array in text:
    text = text.replace(old_array, new_table)
    print("Replaced vertical array in build_6b_plans.py [SUCCESS]")
else:
    # Try more flexible replacement
    import re
    text = re.sub(r'\\\[\s*\\begin\{array\}[\s\S]*?\\end\{array\}\s*\\\]', new_table, text)
    print("Replaced vertical array via regex in build_6b_plans.py")

# Replace \text{ن}
text = text.replace(r'\( \text{١,٨} \times \text{ن} = \text{٠,٥٤} \)', r'\( \text{١,٨} \times \) ن \( = \text{٠,٥٤} \)')
text = text.replace(r'\(\text{ن}\)', r'ن')
text = text.replace(r'\(\text{ن} = \text{٠,٥٤} \div \text{١,٨} = \text{٥,٤} \div \text{١٨} = \text{٠,٣}\)', r'ن \( = \text{٠,٥٤} \div \text{١,٨} = \text{٥,٤} \div \text{١٨} = \text{٠,٣} \)')
text = text.replace(r'\(\text{ن} = \text{٠,٣}\)', r'ن \( = \text{٠,٣} \)')

with open('build_6b_plans.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("build_6b_plans.py updated successfully.")

# 2. Update append_6b_plans_full.py
with open('append_6b_plans_full.py', 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace(r'\( \frac{\text{أ}}{\text{ب}} \)', r'(أ / ب)')
text2 = text2.replace(r'\( \text{أ} \div \text{ب} \)', r'أ ÷ ب')
text2 = text2.replace(r'\( \frac{\text{بسط}}{\text{مقام}} \)', r'(البسط / المقام)')
text2 = text2.replace(r'\(\text{(ق.م.أ)} = \mathbf{\text{٦}}\)', r'(ق.م.أ) = <strong>٦</strong>')

with open('append_6b_plans_full.py', 'w', encoding='utf-8') as f:
    f.write(text2)
print("append_6b_plans_full.py updated successfully.")
