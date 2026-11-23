with open('خطة_درس_إثبات_تطابق_المثلثات_SSS_SAS_6Es.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx = text.find('id="engage"')
if idx == -1:
    idx = text.find('التهيئة')
print(text[idx:idx+2500])
