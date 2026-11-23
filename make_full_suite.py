# -*- coding: utf-8 -*-
import base64
import os

with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

logo_img_tag = f'<img src="data:image/png;base64,{logo_b64}" alt="شعار المدارس المتقدمة" style="height: 75px; width: auto; object-fit: contain;">'

script_content = r'''# -*- coding: utf-8 -*-
import base64

with open('شعار المتقدمة.png', 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

logo_html = f'<img src="data:image/png;base64,{logo_b64}" alt="شعار المدارس المتقدمة" style="height: 75px; width: auto; object-fit: contain;">'

header_template = f'''
<div class="school-official-header">
    <div class="sch-info-right">
        <div class="ministry-name">المملكة العربية السعودية</div>
        <div class="ministry-name">وزارة التعليم - الإدارة العامة للتعليم بمحافظة جدة</div>
        <div class="school-highlight">المدارس المتقدمة للتعلم الذكي بجدة</div>
        <div>قسم الرياضيات | المرحلة المتوسطة</div>
    </div>
    <div class="sch-logo-center">
        {logo_html}
        <div style="font-size:0.8rem; font-weight:800; color:#1e3a8a; margin-top:3px;">مدارس التعلّم الذكي</div>
    </div>
    <div class="sch-info-left-ar">
        <div>مادة: الرياضيات (الصف الثالث المتوسط)</div>
        <div>الفصل الدراسي الثاني - العام الدراسي ١٤٤٧ / ١٤٤٨هـ (٢٠٢٦م)</div>
        <div>معتمدة وفق معايير وزارة التعليم ومنهجية STEM</div>
    </div>
</div>
'''

footer_sig_template = '''
<div class="sheet-footer-bar">
    <div class="sheet-footer-right">
        <span>المدارس المتقدمة للتعلم الذكي بجدة | رؤية المملكة ٢٠٣٠</span>
    </div>
    <div class="sheet-footer-left">
        <div class="teacher-signature-card">
            <span class="teacher-sig-label">معلم المادة:</span>
            <span class="teacher-sig-name">أ. محمد عبدالله جمعة</span>
            <div class="teacher-school-subtext">المدارس المتقدمة للتعلم الذكي بجدة</div>
        </div>
    </div>
</div>
'''
'''

print("Base script template ready")
