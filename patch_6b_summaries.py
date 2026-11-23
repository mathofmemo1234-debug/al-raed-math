# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_summaries.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace vertical arrays in Summary 1
old_arrays_block = r"""<div class="math-rule-box">
                            \[
                            \begin{array}{r@{\quad}l}
                              \text{١٢,٤٠} \\
                            + \ \text{٠٨,٧٥} \\
                            \hline
                              \text{٢١,١٥}
                            \end{array}
                            \qquad
                            \begin{array}{r@{\quad}l}
                              \text{٢٥,٣٠} \\
                            - \ \text{٠٧,٨٥} \\
                            \hline
                              \text{١٧,٤٥}
                            \end{array}
                            \]
                        </div>"""

new_tables_block = r"""<div class="arabic-vert-calc-wrapper">
                            <table class="arabic-vert-table">
                                <caption>عملية الجمع الرأسية (الرمز على اليمين):</caption>
                                <tr><td class="sign-col"></td><td class="num-col">١٢,٤٠</td></tr>
                                <tr class="op-divider"><td class="sign-col">+</td><td class="num-col">٠٨,٧٥</td></tr>
                                <tr class="res-row"><td class="sign-col"></td><td class="num-col">٢١,١٥</td></tr>
                            </table>
                            <table class="arabic-vert-table">
                                <caption>عملية الطرح الرأسية (الرمز على اليمين):</caption>
                                <tr><td class="sign-col"></td><td class="num-col">٢٥,٣٠</td></tr>
                                <tr class="op-divider"><td class="sign-col">−</td><td class="num-col">٠٧,٨٥</td></tr>
                                <tr class="res-row"><td class="sign-col"></td><td class="num-col">١٧,٤٥</td></tr>
                            </table>
                        </div>"""

if old_arrays_block in text:
    text = text.replace(old_arrays_block, new_tables_block)
    print("Replaced Summary 1 arrays [SUCCESS]")
else:
    # regex fallback
    text = re.sub(r'<div class="math-rule-box">\s*\\\[\s*\\begin\{array\}[\s\S]*?\\end\{array\}\s*\\\]\s*</div>', new_tables_block, text)
    print("Replaced Summary 1 arrays via regex")

# Summary 2: البسط والمقام
text = text.replace(r'\( \frac{\text{البسط}}{\text{المقام}} \)', r'(البسط / المقام)')

# Summary 5: والباقي (Image 1 fix)
old_rem = r"""\[
                            \frac{\text{١١}}{\text{٤}} \rightarrow \text{١١} \div \text{٤} = \text{٢} \text{ والباقي } \text{٣} \rightarrow \mathbf{\text{٢} \frac{\text{٣}}{\text{٤}}}
                            \]"""

new_rem = r"""<div class="math-rule-box" style="direction:rtl; text-align:center; font-size:1.15rem; font-weight:700;">
                            \( \frac{\text{١١}}{\text{٤}} \rightarrow \text{١١} \div \text{٤} = \text{٢} \) والباقي \( \text{٣} \leftarrow \) الناتج في صورة عدد كسري: <strong>\( \text{٢} \frac{\text{٣}}{\text{٤}} \)</strong>
                        </div>"""

if old_rem in text:
    text = text.replace(old_rem, new_rem)
    print("Replaced Summary 5 remainder formula [SUCCESS]")
else:
    text = re.sub(r'\\\[\s*\\frac\{\\text\{١١\}\}\{\\text\{٤\}\}[\s\S]*?\\mathbf\{\\text\{٢\}\s*\\frac\{\\text\{٣\}\}\{\\text\{٤\}\}\}\s*\\\]', new_rem, text)
    print("Replaced Summary 5 remainder via regex")

# School name replacement
text = text.replace('مدارس التعلم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')
text = text.replace('مدارس التعلّم الذكي', 'مدارس المتقدمة للتعلم الذكي بجدة')

with open('generator_6b_summaries.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("generator_6b_summaries.py updated successfully.")
