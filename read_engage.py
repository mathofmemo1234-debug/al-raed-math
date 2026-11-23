with open('خطة_درس_إثبات_تطابق_المثلثات_SSS_SAS.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="engage"')
print(text[idx:idx+2500])
