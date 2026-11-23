# -*- coding: utf-8 -*-
import subprocess

panes = ['pane-engage', 'pane-explore', 'pane-explain', 'pane-engineer', 'pane-elaborate', 'pane-evaluate']

with open('عرض_السبورة_التفاعلي_الشامل_المثلثات_SSS_SAS.html', 'r', encoding='utf-8') as f:
    orig = f.read()

for p in panes:
    # Modify active pane
    temp = orig
    for other in panes:
        if other == p:
            temp = temp.replace(f'id="{other}" class="stage-pane hidden space-y-6"', f'id="{other}" class="stage-pane space-y-6"')
            temp = temp.replace(f'id="{other}" class="stage-pane space-y-6"', f'id="{other}" class="stage-pane space-y-6"') # keep active
            temp = temp.replace(f'id="btn-{other}" class="nav-btn px-3.5 py-1.5 rounded-xl font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5"', f'id="btn-{other}" class="nav-btn active px-3.5 py-1.5 rounded-xl font-black transition flex items-center gap-1.5"')
        else:
            temp = temp.replace(f'id="{other}" class="stage-pane space-y-6"', f'id="{other}" class="stage-pane hidden space-y-6"')
            temp = temp.replace(f'id="btn-{other}" class="nav-btn active px-3.5 py-1.5 rounded-xl font-black transition flex items-center gap-1.5"', f'id="btn-{other}" class="nav-btn px-3.5 py-1.5 rounded-xl font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-1.5"')

    temp_file = f'temp_{p}.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(temp)

    # Take screenshot
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        f"--screenshot=C:\\Users\\TOSHIBA\\{p}.png",
        "--window-size=1280,1100",
        f"file:///C:/Users/TOSHIBA/.gemini/antigravity/scratch/تحضر/{temp_file}"
    ]
    subprocess.run(cmd, capture_output=True)
    print(f"Captured {p}")
