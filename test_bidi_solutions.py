# -*- coding: utf-8 -*-
import subprocess, os, pymupdf, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cur = os.path.dirname(os.path.abspath(__file__))

html_test = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
body { font-family: sans-serif; font-size: 20px; padding: 30px; direction: rtl; }
.test-row { margin: 15px 0; padding: 10px; border-bottom: 1px solid #ccc; }

/* Method 1: inline-flex */
.eq-flex {
    display: inline-flex;
    flex-direction: row;
    direction: rtl;
    align-items: center;
    gap: 4px;
    font-weight: 700;
    color: #1e3a8a;
}

/* Method 2: RLM characters */
.eq-rlm {
    font-weight: 700;
    color: #1e3a8a;
}

/* Method 3: bdi on each token */
.eq-bdi {
    direction: rtl;
    font-weight: 700;
    color: #1e3a8a;
}

/* Method 4: CSS unicode-bidi override */
.eq-override {
    unicode-bidi: bidi-override;
    direction: rtl;
    font-weight: 700;
    color: #1e3a8a;
}
</style>
</head>
<body>

<div class="test-row">
  <strong>الطريقة 1 (inline-flex):</strong><br>
  ١) ناتج ضرب <span class="eq-flex"><span>٠,٢</span><span>×</span><span>٠,٣</span><span>=</span><span>٠,٦</span></span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>الطريقة 2 (RLM علامات الاتجاه العربي):</strong><br>
  ١) ناتج ضرب <span class="eq-rlm">&rlm;٠,٢&rlm; &times; &rlm;٠,٣&rlm; = &rlm;٠,٦&rlm;</span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>الطريقة 1 مع الطرح:</strong><br>
  ٣) ناتج طرح: <span class="eq-flex"><span>٤,٥</span><span>−</span><span>٢,٢٥</span><span>=</span><span>٢,٢٥</span></span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>الطريقة 2 مع الطرح:</strong><br>
  ٣) ناتج طرح: <span class="eq-rlm">&rlm;٤,٥&rlm; &minus; &rlm;٢,٢٥&rlm; = &rlm;٢,٢٥&rlm;</span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>الطريقة 1 مع الجمع (اختيار من متعدد):</strong><br>
  ١) أوجد ناتج: <span class="eq-flex"><span>١٢,٤</span><span>+</span><span>٨,٧٥</span></span>
</div>

<div class="test-row">
  <strong>الطريقة 2 مع الجمع (اختيار من متعدد):</strong><br>
  ١) أوجد ناتج: <span class="eq-rlm">&rlm;١٢,٤&rlm; + &rlm;٨,٧٥&rlm;</span>
</div>

<div class="test-row">
  <strong>الطريقة 1 مع القسمة:</strong><br>
  أوجد ناتج: <span class="eq-flex"><span>١٥,٦</span><span>÷</span><span>٠,٣</span><span>=</span><span>٥٢</span></span>
</div>

<div class="test-row">
  <strong>الطريقة 2 مع القسمة:</strong><br>
  أوجد ناتج: <span class="eq-rlm">&rlm;١٥,٦&rlm; &divide; &rlm;٠,٣&rlm; = &rlm;٥٢&rlm;</span>
</div>

</body>
</html>"""

html_path = os.path.join(cur, 'test_methods.html')
pdf_path = os.path.join(cur, 'test_methods.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_test)

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    html_path
]
subprocess.run(cmd, check=True)

doc = pymupdf.open(pdf_path)
page = doc[0]
words = page.get_text('words')

lines = defaultdict(list)
for w in words:
    line_y = round(w[1] / 12) * 12
    lines[line_y].append(w)

print("=== EXTRACTED VISUAL ORDER (RIGHT TO LEFT) ===")
for y in sorted(lines.keys()):
    row = sorted(lines[y], key=lambda w: -w[0])
    text_rtl = ' '.join(w[4] for w in row)
    print(f'y={y:3d}: {text_rtl}')
