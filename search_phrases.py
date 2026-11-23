import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in os.listdir('.'):
    if fname.endswith('.html') or fname.endswith('.py'):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = []
                if 'عكس اتجاه' in content:
                    matches.append('عكس اتجاه')
                if 'بيانياً على خط الأعداد' in content:
                    matches.append('بيانياً على خط الأعداد')
                if 'دائرة مغلقة' in content:
                    matches.append('دائرة مغلقة')
                if matches:
                    print(f"{fname}: {matches}")
        except Exception as e:
            pass
