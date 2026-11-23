# -*- coding: utf-8 -*-
import subprocess, os, pymupdf

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cur = os.path.dirname(os.path.abspath(__file__))

html_test = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&family=Tajawal:wght@500;700;800&display=swap" rel="stylesheet">
<style>
body { font-family: 'Tajawal', sans-serif; font-size: 18px; padding: 30px; direction: rtl; }
.test-row { margin: 15px 0; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; background: #fff; }
.ar-math { direction: rtl; unicode-bidi: isolate; font-weight: 700; color: #1e3a8a; }
.ar-frac {
    display: inline-flex;
    flex-direction: column;
    vertical-align: middle;
    text-align: center;
    padding: 0 3px;
    font-size: 0.95em;
    line-height: 1.1;
}
.ar-frac .num {
    border-bottom: 1.5px solid #1e3a8a;
    padding-bottom: 1px;
}
.ar-frac .denom {
    padding-top: 1px;
}
.mixed-num {
    display: inline-flex;
    align-items: center;
    direction: rtl;
    gap: 2px;
}
</style>
</head>
<body>

<div class="test-row">
  <strong>١) الصواب والخطأ (ضرب عشري):</strong><br>
  ١) ناتج ضرب <span class="ar-math">٠,٢ × ٠,٣ = ٠,٦</span> ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>٢) الصواب والخطأ (طرح عشري):</strong><br>
  ٣) ناتج طرح: <span class="ar-math">٤,٥ − ٢,٢٥ = ٢,٢٥</span> ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
</div>

<div class="test-row">
  <strong>٣) اختيار من متعدد (جمع عشري):</strong><br>
  ١) أوجد ناتج الجمع التالي: <span class="ar-math">١٢,٤ + ٨,٧٥</span>
</div>

<div class="test-row">
  <strong>٤) قسمة عشرية:</strong><br>
  أوجد ناتج: <span class="ar-math">١٥,٦ ÷ ٠,٣ = ١٥٦ ÷ ٣ = ٥٢</span>
</div>

<div class="test-row">
  <strong>٥) كسور متكافئة رأسية:</strong><br>
  الكسر <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> يكافئ: 
  <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٢ × ٣</span><span class="denom">٣ × ٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span>
</div>

<div class="test-row">
  <strong>٦) عدد كسري (٢ وثلاثة أرباع):</strong><br>
  <span class="mixed-num"><span>٢</span><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>
</div>

<div class="test-row">
  <strong>٧) مسألة مقارنة كسور:</strong><br>
  قارن: <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span> &gt; <span class="ar-frac"><span class="num">١</span><span class="denom">٥</span></span></span>
</div>

</body>
</html>"""

html_path = os.path.join(cur, 'test_frac.html')
pdf_path = os.path.join(cur, 'test_frac.pdf')
img_path = os.path.join(cur, 'test_frac.png')

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
pix = page.get_pixmap(dpi=150)
pix.save(img_path)
print('Saved:', img_path)
