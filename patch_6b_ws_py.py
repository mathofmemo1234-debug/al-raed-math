import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('generator_6b_worksheets.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to replace in generator_6b_worksheets.py:
# Find: <div class="tf-text">(<strong>[٠-٩]+[)]</strong>[^<]+)</div>
# Replace with: <div class="tf-text">\1 <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>

def add_student_mark_box(match):
    inner = match.group(1).rstrip()
    if 'student-mark-box' in inner:
        return match.group(0)
    return f'<div class="tf-text">{inner} <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>'

new_content = re.sub(r'<div class="tf-text">(<strong>[٠-٩]+[)]</strong>[\s\S]*?)</div>', add_student_mark_box, content)

matches_found = len(re.findall(r'<div class="tf-text">', new_content))
boxes_added = len(re.findall(r'student-mark-box', new_content))

print(f"Total tf-text: {matches_found}, boxes added: {boxes_added}")

with open('generator_6b_worksheets.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated generator_6b_worksheets.py successfully.")
