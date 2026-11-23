import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_المعادلات_والقياس_1م.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== DEEP AUDIT FOR 1M ===")
print("File length:", len(text), "chars, lines:", len(text.splitlines()))

# 1. School name check
school_corr = text.count('مدارس المتقدمة للتعلم الذكي بجدة')
school_corr_al = text.count('المدارس المتقدمة للتعلم الذكي بجدة')
print(f"School names: 'مدارس المتقدمة...' = {school_corr}, 'المدارس المتقدمة...' = {school_corr_al}")
old_schools = re.findall(r'مدارس التعلم الذكي(?! بجدة)', text)
print(f"Old school names found: {len(old_schools)}")

# 2. Teacher name check
teacher = text.count('محمد عبدالله جمعة')
print(f"Teacher name count: {teacher}")

# 3. Logo check
logo = text.count('data:image/png;base64')
print(f"Base64 logo count: {logo}")

# 4. Check for dollar signs
dollars = text.count('$')
print(f"Dollar signs count: {dollars}")

# 5. Check for MathJax inline math \( ... \)
math_inlines = re.findall(r'\\\((.*?)\\\)', text, re.DOTALL)
print(f"MathJax inline expressions: {len(math_inlines)}")

# Check for Arabic words inside math
ar_words_in_math = []
for m in math_inlines:
    # find Arabic characters
    ar_chars = re.findall(r'[\u0621-\u064A]', m)
    if ar_chars:
        ar_words_in_math.append((m, ar_chars))

print(f"MathJax inlines with Arabic letters: {len(ar_words_in_math)}")
if ar_words_in_math:
    for m, chars in ar_words_in_math[:10]:
        print(f"  Expr: '{m.strip()}' -> chars: {chars}")

# 6. Check for ASCII digits
# exclude <style>, <script>, color codes (#ffffff), attributes (width="100")
body_start = text.find('<body>')
body_text = text[body_start:] if body_start != -1 else text

# Strip script and style tags
clean_body = re.sub(r'<script.*?</script>', '', body_text, flags=re.DOTALL)
clean_body = re.sub(r'<style.*?</style>', '', clean_body, flags=re.DOTALL)
# Strip HTML tags
pure_text = re.sub(r'<[^>]+>', ' ', clean_body)

ascii_digits = re.findall(r'\b\d+\b', pure_text)
print(f"Pure text ASCII digit numbers: {len(ascii_digits)}")
if ascii_digits:
    print("  First 10 ASCII numbers:", ascii_digits[:10])

# 7. Check for fractions: are there ( ÷ ) or \frac?
frac_div = re.findall(r'\([\u0660-\u0669\d\s]+÷[\u0660-\u0669\d\s]+\)', text)
print(f"Fractions written as (س ÷ ص): {len(frac_div)}")
if frac_div:
    print("  Examples:", frac_div[:5])

frac_math = re.findall(r'\\frac', text)
print(f"Fractions written as \\frac: {len(frac_math)}")

# 8. Check for raw backslashes
raw_slashes = re.findall(r'\\[a-zA-Z]+', pure_text)
print(f"Raw LaTeX tokens in visible text: {len(raw_slashes)}")
if raw_slashes:
    print("  Tokens:", set(raw_slashes))

# 9. Check for vertical operations or tables
vert_tables = text.count('arabic-vert-table')
print(f"RTL vertical tables: {vert_tables}")

# 10. Check if answers are inline and toggle button exists
toggles = text.count('toggleAllAnswers')
print(f"Toggle buttons/scripts: {toggles}")
inline_answers = text.count('problem-solution-inline')
print(f"Inline answers count: {inline_answers}")
