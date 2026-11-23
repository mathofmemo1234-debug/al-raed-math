import subprocess

vbs_code = """
Set UAC = CreateObject("Shell.Application")
UAC.ShellExecute "cmd.exe", "/k echo Hello from Elevated", "", "runas", 1
"""
with open("test_elev.vbs", "w") as f:
    f.write(vbs_code)

res = subprocess.run(["cscript", "//nologo", "test_elev.vbs"], capture_output=True, text=True)
print("VBS STDOUT:", res.stdout)
print("VBS STDERR:", res.stderr)
print("VBS Exit:", res.returncode)
