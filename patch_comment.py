# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("(without '$' to prevent accidental text capture)", "(without dollar signs to prevent accidental text capture)")

with open('generator_6b_header_styles.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generator_6b_header_styles.py comment updated.")
