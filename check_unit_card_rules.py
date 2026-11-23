import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('الحقيبة_الشاملة_سادس_ابتدائي_ص135_151.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = 0
while True:
    idx = c.find('.unit-card', idx)
    if idx == -1: break
    print(c[idx:idx+150].replace('\n', ' '))
    idx += 10
