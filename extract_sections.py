# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

import generator_summaries
import generator_worksheets

summaries_html = generator_summaries.get_all_summaries_html()
with open('section_summaries.html', 'w', encoding='utf-8') as f:
    f.write(summaries_html)
print(f"section_summaries.html written, length: {len(summaries_html)}")

worksheets_html = generator_worksheets.get_all_worksheets_html()
with open('section_worksheets.html', 'w', encoding='utf-8') as f:
    f.write(worksheets_html)
print(f"section_worksheets.html written, length: {len(worksheets_html)}")
