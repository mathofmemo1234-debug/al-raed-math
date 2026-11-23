# -*- coding: utf-8 -*-
import sys, os, subprocess, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect what is around pos
pos = text.rfind('ناتج ضرب')
print("Snippet from master HTML:")
print(text[pos-30:pos+200])

# Let's check test_methods.html vs this snippet
# In test_methods.html we had:
# ١) ناتج ضرب <span class="eq-flex"><span>٠,٢</span><span>×</span><span>٠,٣</span><span>=</span><span>٠,٦</span></span> ( &nbsp;&nbsp; )
