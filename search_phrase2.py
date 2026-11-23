import os, sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in os.listdir('.'):
    if fname.endswith('.html') or fname.endswith('.py'):
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'يقتضي عكس' in content or 'يقتضي' in content:
                    print(f"{fname} matches 'يقتضي'")
        except Exception:
            pass
