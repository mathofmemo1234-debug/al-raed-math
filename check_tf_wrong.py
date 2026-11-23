import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    code = f.read()

tf_pos = code.find('.tf-wrong')
print(code[tf_pos:tf_pos+800])
