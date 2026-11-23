import subprocess

methods = [
    # Method 1: simple quotes
    r'''powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"''',
    # Method 2: cmd /k with ~s0 short path
    r'''powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath cmd.exe -ArgumentList '/k', '%~s0' -Verb RunAs"''',
    # Method 3: cmd /k with full path
    r'''powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath cmd.exe -ArgumentList '/k \"\"%~f0\"\"' -Verb RunAs"''',
]

for idx, m in enumerate(methods):
    print(f"--- Testing Method {idx+1} ---")
    script = f"""@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Attempting elevation...
    {m}
    echo Finished attempt.
    exit /b
)
echo Admin verified!
"""
    with open('test_run.bat', 'w', encoding='utf-8') as f:
        f.write(script)
    res = subprocess.run(['cmd.exe', '/c', 'test_run.bat'], capture_output=True, text=True, encoding='utf-8')
    print("STDOUT:", res.stdout.strip())
    print("STDERR:", res.stderr.strip())
