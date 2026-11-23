# -*- coding: utf-8 -*-
import subprocess, os, pymupdf

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html_test = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
body { font-family: sans-serif; font-size: 20px; padding: 30px; direction: rtl; }
.test-row { margin: 20px 0; padding: 10px; border-bottom: 1px solid #ccc; }
.ar-math { direction: rtl; unicode-bidi: isolate; font-weight: 700; color: #1e3a8a; }
.ar-math-embed { direction: rtl; unicode-bidi: bidi-override; font-weight: 700; color: #1e3a8a; }
.flex-math { display: inline-flex; flex-direction: row; direction: rtl; font-weight: 700; color: #1e3a8a; }
</style>
</head>
<body>
<div class="test-row">
  <strong>تجربة 1 (نص عادي مباشر):</strong><br>
  ١) ناتج ضرب ٠,٢ × ٠,٣ = ٠,٦ ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>تجربة 2 (span ar-math isolate):</strong><br>
  ١) ناتج ضرب <span class="ar-math">٠,٢ × ٠,٣ = ٠,٦</span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>تجربة 3 (bdi dir=rtl):</strong><br>
  ١) ناتج ضرب <bdi dir="rtl">٠,٢ × ٠,٣ = ٠,٦</bdi> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>تجربة 4 (طرح - عادي):</strong><br>
  ٣) ناتج طرح: ٤,٥ - ٢,٢٥ = ٢,٢٥ ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>تجربة 5 (طرح - مع ar-math isolate):</strong><br>
  ٣) ناتج طرح: <span class="ar-math">٤,٥ − ٢,٢٥ = ٢,٢٥</span> ( &nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>تجربة 6 (معادلة سادس - قسمة):</strong><br>
  أوجد ناتج: <span class="ar-math">١٥,٦ ÷ ٠,٣ = ٥٢</span>
</div>
</body>
</html>"""

with open('test_bidi.html', 'w', encoding='utf-8') as f:
    f.write(html_test)

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--print-to-pdf=test_bidi.pdf',
    os.path.abspath('test_bidi.html')
]
subprocess.run(cmd, check=True)

doc = pymupdf.open('test_bidi.pdf')
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('test_bidi.png')
print('Saved test_bidi.png successfully!')
