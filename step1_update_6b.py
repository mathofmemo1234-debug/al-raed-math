import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update generator_6b_header_styles.py
with open('generator_6b_header_styles.py', 'r', encoding='utf-8') as f:
    styles_code = f.read()

# Add .tf-ans-box and .student-mark-box to CSS if not present
if '.tf-ans-box {' not in styles_code:
    target_pos = styles_code.find('.tf-item {')
    extra_css = """
        .tf-ans-box {
            display: none;
            margin-top: 6px;
            padding: 6px 10px;
            background: #f0fdf4;
            border-radius: 6px;
            border-right: 3px solid #10b981;
        }

        .student-mark-box {
            display: inline-block;
            color: #1e3a8a;
            font-weight: 700;
            margin-right: 8px;
            letter-spacing: 2px;
        }
"""
    styles_code = styles_code[:target_pos] + extra_css + styles_code[target_pos:]

# Update toggleWorksheetAnswers in HTML_JS_AND_END
js_target = r"""function toggleWorksheetAnswers(sheetId, btn) {
    var card = document.getElementById(sheetId);
    if (!card) return;

    var solutions = card.querySelectorAll('.inline-solution-block');
    var badges = card.querySelectorAll('.correct-badge');
    var correctOpts = card.querySelectorAll('.mcq-opt.correct-opt');

    var isHidden = true;
    if (solutions.length > 0) {
        isHidden = (solutions[0].style.display !== 'block');
    }"""

js_replacement = r"""function toggleWorksheetAnswers(sheetId, btn) {
    var card = document.getElementById(sheetId);
    if (!card) return;

    var solutions = card.querySelectorAll('.inline-solution-block');
    var badges = card.querySelectorAll('.correct-badge');
    var correctOpts = card.querySelectorAll('.mcq-opt.correct-opt');
    var tfBoxes = card.querySelectorAll('.tf-ans-box');

    var isHidden = true;
    if (solutions.length > 0) {
        isHidden = (solutions[0].style.display !== 'block');
    } else if (tfBoxes.length > 0) {
        isHidden = (tfBoxes[0].style.display !== 'block');
    }

    tfBoxes.forEach(function(el) {
        el.style.display = isHidden ? 'block' : 'none';
    });"""

if js_target in styles_code:
    styles_code = styles_code.replace(js_target, js_replacement)

with open('generator_6b_header_styles.py', 'w', encoding='utf-8') as f:
    f.write(styles_code)

print("1. generator_6b_header_styles.py updated.")

# 2. Re-generate worksheets section
import subprocess
subprocess.run([sys.executable, 'generator_6b_worksheets.py'], check=True)
print("2. section_6b_worksheets.html regenerated.")

# 3. Assemble 6b master suite
subprocess.run([sys.executable, 'assemble_6b_master_suite.py'], check=True)
print("3. assemble_6b_master_suite.py completed.")
