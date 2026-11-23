import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    code = f.read()

js_pos = code.find('HTML_JS_AND_END =')
print(code[js_pos:])
