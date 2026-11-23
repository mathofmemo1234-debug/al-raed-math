# -*- coding: utf-8 -*-
"""
Generate a high-contrast, large-font, black-and-white, strictly ONE-PAGE
Student Engagement Sheet for Triangle Congruence (SSS, SAS).
Designed for perfect printing on 1 sheet of A4 without page breaks or spilling.
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بطاقة انخراط صفي: إثبات تطابق المثلثات (SSS, SAS)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800;900&display=swap" rel="stylesheet">
    <style>
        /* إعدادات الطباعة الدقيقة لورقة واحدة A4 فقط */
        @page {
            size: A4 portrait;
            margin: 6mm 8mm 6mm 8mm;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }

        body {
            font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
            color: #000000;
            background-color: #ffffff;
            line-height: 1.25;
            font-size: 13pt;
        }

        /* حاوية الصفحة الواحدة - محكومة الارتفاع تماماً */
        .page-container {
            width: 100%;
            max-width: 194mm;
            height: 280mm;
            max-height: 282mm;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            border: 2px solid #000000;
            padding: 8mm 9mm;
            background: #ffffff;
        }

        /* شريط الترويسة */
        .header-box {
            border-bottom: 2px solid #000000;
            padding-bottom: 5px;
            margin-bottom: 6px;
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11pt;
            font-weight: 700;
            margin-bottom: 4px;
        }

        .main-title {
            text-align: center;
            font-size: 17pt;
            font-weight: 900;
            background-color: #f0f0f0;
            border: 2px solid #000000;
            padding: 3px 10px;
            border-radius: 6px;
            letter-spacing: 0.2px;
            margin-bottom: 5px;
        }

        .student-info {
            display: flex;
            justify-content: space-between;
            background: #ffffff;
            border: 1.5px solid #000000;
            border-radius: 5px;
            padding: 4px 10px;
            font-size: 12pt;
            font-weight: 800;
        }

        .dotted-line {
            display: inline-block;
            border-bottom: 1.8px dotted #000000;
            min-height: 18px;
            vertical-align: bottom;
        }

        /* أقسام الأنشطة */
        .section-card {
            border: 1.8px solid #000000;
            border-radius: 6px;
            padding: 6px 8px;
            margin-bottom: 6px;
            background: #ffffff;
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 13pt;
            font-weight: 900;
            background: #000000;
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            margin-bottom: 6px;
        }

        .section-body {
            font-size: 12pt;
            font-weight: 700;
        }

        /* الرسوم الهندسية باللون الأسود الناصع */
        svg {
            display: block;
            margin: auto;
        }

        .geo-label {
            font-family: 'Cairo', sans-serif;
            font-size: 13px;
            font-weight: 900;
            fill: #000000;
        }

        .geo-line {
            stroke: #000000;
            stroke-width: 2.4;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .tick-mark {
            stroke: #000000;
            stroke-width: 2.2;
            stroke-linecap: round;
        }

        .angle-arc {
            stroke: #000000;
            stroke-width: 2;
            fill: none;
        }

        /* شبكة الأعمدة */
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 6px;
        }

        /* جدول البرهان */
        .proof-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 4px;
            font-size: 11.5pt;
        }

        .proof-table th, .proof-table td {
            border: 1.5px solid #000000;
            padding: 4px 6px;
            text-align: right;
            font-weight: 800;
        }

        .proof-table th {
            background-color: #eaeaea;
            font-weight: 900;
            text-align: center;
        }

        .check-box {
            display: inline-block;
            width: 18px;
            height: 18px;
            border: 2px solid #000000;
            border-radius: 3px;
            vertical-align: middle;
            margin-left: 4px;
        }

        /* الفوتر وسلم التقييم */
        .footer-bar {
            border-top: 1.8px solid #000000;
            padding-top: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11pt;
            font-weight: 800;
        }

        /* شريط زر الطباعة يظهر فقط على الشاشة ويختفي في الطباعة */
        .screen-toolbar {
            max-width: 194mm;
            margin: 10px auto 5px auto;
            text-align: center;
        }

        .print-btn {
            background-color: #000000;
            color: #ffffff;
            border: none;
            padding: 8px 24px;
            font-size: 13pt;
            font-weight: 900;
            font-family: 'Cairo', sans-serif;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 3px 6px rgba(0,0,0,0.2);
        }

        .print-btn:hover {
            background-color: #333333;
        }

        @media print {
            .screen-toolbar {
                display: none !important;
            }
            body {
                background: none;
            }
            .page-container {
                border: 2px solid #000000 !important;
                height: 280mm !important;
                max-height: 280mm !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }
        }
    </style>
</head>
<body>

    <!-- شريط الإجراءات للشاشة فقط -->
    <div class="screen-toolbar">
        <button class="print-btn" onclick="window.print()">🖨️ طباعة الورقة (صفحة A4 واحدة)</button>
    </div>

    <!-- الحاوية الكلية للصفحة الواحدة -->
    <div class="page-container">

        <!-- 1. الترويسة وبيانات الطالب -->
        <header class="header-box">
            <div class="header-top">
                <div>المملكة العربية السعودية — وزارة التعليم</div>
                <div>مادة: الرياضيات 1-2 (مسارات)</div>
                <div>الدرس 3-4 (ص 170-177)</div>
            </div>
            <div class="main-title">
                بطاقة الانخراط الصفي: إثبات تطابق المثلثات (SSS, SAS)
            </div>
            <div class="student-info">
                <div>اسم الطالب: <span class="dotted-line" style="width: 220px;"></span></div>
                <div>الفصل: <span class="dotted-line" style="width: 70px;"></span></div>
                <div>المجموعة: <span class="dotted-line" style="width: 70px;"></span></div>
                <div>التاريخ: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/ 1448هـ</div>
            </div>
        </header>

        <!-- 2. النشاط الأول: كاشف الزاوية المحصورة (Included Angle) -->
        <section class="section-card">
            <div class="section-header">
                <span>⚡ النشاط 1: كاشف الزاوية المحصورة بين ضلعين (مفتاح المسلمة SAS)</span>
            </div>
            <div class="section-body" style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">
                <!-- رسم المثلث مع تسميات واضحة -->
                <div style="width: 175px; text-align: center; border: 1.5px solid #000; border-radius: 4px; padding: 4px;">
                    <svg width="160" height="95" viewBox="0 0 160 95">
                        <!-- Triangle ABC -->
                        <polygon points="20,80 145,80 85,15" fill="#fcfcfc" stroke="#000000" stroke-width="2.5" />
                        <!-- Vertices labels -->
                        <text x="85" y="11" text-anchor="middle" class="geo-label">A</text>
                        <text x="10" y="86" text-anchor="middle" class="geo-label">B</text>
                        <text x="154" y="86" text-anchor="middle" class="geo-label">C</text>
                        <!-- Highlighted arc at A -->
                        <path d="M 76,28 A 15 15 0 0 0 94,28" class="angle-arc" />
                    </svg>
                    <div style="font-size: 10pt; font-weight: 800;">المثلث ABC</div>
                </div>

                <!-- الأسئلة المباشرة بخط كبير -->
                <div style="flex: 1; display: flex; flex-direction: column; gap: 6px;">
                    <div>
                        <strong>1) ما الزاوية المحصورة</strong> بين الضلعين 
                        <span dir="ltr"><strong>AB</strong></span> و <span dir="ltr"><strong>AC</strong></span>؟
                        &nbsp;&nbsp;الجواب: الزاوية ( &nbsp;&nbsp;&nbsp;&nbsp;<span class="dotted-line" style="width: 80px;"></span>&nbsp;&nbsp;&nbsp;&nbsp; )
                    </div>
                    <div>
                        <strong>2) ما هما الضلعان</strong> اللذان يحصران الزاوية <span dir="ltr"><strong>&ang;B</strong></span>؟
                        &nbsp;&nbsp;الجواب: الضلعان ( &nbsp;<span class="dotted-line" style="width: 60px;"></span>&nbsp; ) و ( &nbsp;<span class="dotted-line" style="width: 60px;"></span>&nbsp; )
                    </div>
                    <div style="font-size: 11pt; color: #111;">
                        💡 <strong>قاعدة سريعة:</strong> رأس الزاوية المحصورة هو دائماً <u>الحرف المشترك</u> بين الضلعين!
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. النشاط الثاني: فك شفرة التطابق (SSS أم SAS؟) -->
        <section class="section-card">
            <div class="section-header">
                <span>🔍 النشاط 2: فحص الأشكال — حدد مسلمة التطابق المناسبة (SSS أم SAS)</span>
            </div>
            <div class="section-body grid-2">
                <!-- الحالة الأولى: SSS -->
                <div style="border: 1.5px solid #000; border-radius: 4px; padding: 5px; text-align: center;">
                    <svg width="220" height="85" viewBox="0 0 220 85">
                        <!-- Triangle 1 -->
                        <polygon points="15,75 90,75 35,20" fill="none" class="geo-line" />
                        <text x="35" y="15" class="geo-label">A</text>
                        <text x="8" y="80" class="geo-label">B</text>
                        <text x="96" y="80" class="geo-label">C</text>
                        <!-- Ticks on Tri 1 -->
                        <!-- AB tick 1 -->
                        <line x1="22" y1="46" x2="28" y2="49" class="tick-mark" />
                        <!-- BC tick 2 -->
                        <line x1="50" y1="71" x2="50" y2="79" class="tick-mark" />
                        <line x1="55" y1="71" x2="55" y2="79" class="tick-mark" />
                        <!-- AC tick 3 -->
                        <line x1="60" y1="45" x2="66" y2="49" class="tick-mark" />
                        <line x1="63" y1="42" x2="69" y2="46" class="tick-mark" />
                        <line x1="66" y1="39" x2="72" y2="43" class="tick-mark" />

                        <!-- Triangle 2 -->
                        <polygon points="125,75 200,75 145,20" fill="none" class="geo-line" />
                        <text x="145" y="15" class="geo-label">D</text>
                        <text x="118" y="80" class="geo-label">E</text>
                        <text x="206" y="80" class="geo-label">F</text>
                        <!-- Ticks on Tri 2 -->
                        <!-- DE tick 1 -->
                        <line x1="132" y1="46" x2="138" y2="49" class="tick-mark" />
                        <!-- EF tick 2 -->
                        <line x1="160" y1="71" x2="160" y2="79" class="tick-mark" />
                        <line x1="165" y1="71" x2="165" y2="79" class="tick-mark" />
                        <!-- DF tick 3 -->
                        <line x1="170" y1="45" x2="176" y2="49" class="tick-mark" />
                        <line x1="173" y1="42" x2="179" y2="46" class="tick-mark" />
                        <line x1="176" y1="39" x2="182" y2="43" class="tick-mark" />
                    </svg>
                    <div style="margin-top: 3px;">
                        المسلمة المناسبة هي: &nbsp;
                        <strong>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</strong>
                    </div>
                </div>

                <!-- الحالة الثانية: SAS -->
                <div style="border: 1.5px solid #000; border-radius: 4px; padding: 5px; text-align: center;">
                    <svg width="220" height="85" viewBox="0 0 220 85">
                        <!-- Triangle 1 -->
                        <polygon points="15,75 85,75 20,20" fill="none" class="geo-line" />
                        <text x="18" y="15" class="geo-label">J</text>
                        <text x="8" y="80" class="geo-label">K</text>
                        <text x="92" y="80" class="geo-label">L</text>
                        <!-- Ticks on Tri 1 -->
                        <!-- JK tick 1 -->
                        <line x1="14" y1="48" x2="22" y2="48" class="tick-mark" />
                        <!-- KL tick 2 -->
                        <line x1="48" y1="71" x2="48" y2="79" class="tick-mark" />
                        <line x1="53" y1="71" x2="53" y2="79" class="tick-mark" />
                        <!-- Angle K arc -->
                        <path d="M 28,75 A 12 12 0 0 0 16,63" class="angle-arc" />

                        <!-- Triangle 2 -->
                        <polygon points="125,75 195,75 130,20" fill="none" class="geo-line" />
                        <text x="128" y="15" class="geo-label">X</text>
                        <text x="118" y="80" class="geo-label">Y</text>
                        <text x="202" y="80" class="geo-label">Z</text>
                        <!-- Ticks on Tri 2 -->
                        <!-- XY tick 1 -->
                        <line x1="124" y1="48" x2="132" y2="48" class="tick-mark" />
                        <!-- YZ tick 2 -->
                        <line x1="158" y1="71" x2="158" y2="79" class="tick-mark" />
                        <line x1="163" y1="71" x2="163" y2="79" class="tick-mark" />
                        <!-- Angle Y arc -->
                        <path d="M 138,75 A 12 12 0 0 0 126,63" class="angle-arc" />
                    </svg>
                    <div style="margin-top: 3px;">
                        المسلمة المناسبة هي: &nbsp;
                        <strong>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]</strong>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. النشاط الثالث: إكمال برهان سريع (خاصية الانعكاس والضلع المشترك) -->
        <section class="section-card">
            <div class="section-header">
                <span>📝 النشاط 3: إكمال برهان ذي عمودين (استخدام الضلع المشترك)</span>
            </div>
            <div class="section-body" style="display: flex; gap: 10px; align-items: center;">
                <!-- رسم الشكل المشترك مع القطر BD -->
                <div style="width: 155px; text-align: center; border: 1.5px solid #000; border-radius: 4px; padding: 3px;">
                    <svg width="145" height="95" viewBox="0 0 145 95">
                        <!-- Kite / Shared diagonal shape -->
                        <polygon points="72,12 135,48 72,85 10,48" fill="none" class="geo-line" />
                        <!-- Diagonal BD (Shared side) -->
                        <line x1="10" y1="48" x2="135" y2="48" stroke="#000000" stroke-width="2.5" stroke-dasharray="4,2" />
                        <!-- Vertex labels -->
                        <text x="72" y="9" text-anchor="middle" class="geo-label">A</text>
                        <text x="4" y="52" text-anchor="middle" class="geo-label">B</text>
                        <text x="72" y="94" text-anchor="middle" class="geo-label">C</text>
                        <text x="141" y="52" text-anchor="middle" class="geo-label">D</text>
                        <!-- Congruence ticks -->
                        <line x1="39" y1="28" x2="43" y2="34" class="tick-mark" /> <!-- AB -->
                        <line x1="39" y1="67" x2="43" y2="61" class="tick-mark" /> <!-- BC -->
                        <!-- Double ticks -->
                        <line x1="102" y1="30" x2="106" y2="36" class="tick-mark" /> <!-- AD -->
                        <line x1="105" y1="28" x2="109" y2="34" class="tick-mark" />
                        <line x1="102" y1="65" x2="106" y2="59" class="tick-mark" /> <!-- CD -->
                        <line x1="105" y1="67" x2="109" y2="61" class="tick-mark" />
                    </svg>
                    <div style="font-size: 9.5pt; font-weight: 800;">الشكل الهندسي</div>
                </div>

                <!-- جدول إكمال البرهان -->
                <div style="flex: 1;">
                    <div style="font-size: 11pt; margin-bottom: 3px;">
                        <strong>المعطيات:</strong> <span dir="ltr">AB &cong; CB</span> ، و <span dir="ltr">AD &cong; CD</span>
                        &nbsp;|&nbsp;
                        <strong>المطلوب:</strong> إثبات أن <span dir="ltr">&Delta;ABD &cong; &Delta;CBD</span>
                    </div>

                    <table class="proof-table">
                        <thead>
                            <tr>
                                <th style="width: 50%;">العبارات</th>
                                <th style="width: 50%;">المبررات</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1) <span dir="ltr">AB &cong; CB</span> ، و <span dir="ltr">AD &cong; CD</span></td>
                                <td>1) معطيات</td>
                            </tr>
                            <tr>
                                <td>2) <span dir="ltr">BD &cong; BD</span> (ضلع مشترك)</td>
                                <td>2) خاصية ............................................</td>
                            </tr>
                            <tr>
                                <td>3) <span dir="ltr">&Delta;ABD &cong; &Delta;CBD</span></td>
                                <td>3) مسلمة ............................................</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- 5. النشاط الرابع: تذكرة الخروج والتفكير الناقد (Exit Ticket) -->
        <section class="section-card" style="margin-bottom: 2px;">
            <div class="section-header">
                <span>🎯 النشاط 4: تذكرة الخروج وتحدي التفكير الناقد (دقيقة واحدة)</span>
            </div>
            <div class="section-body" style="display: flex; align-items: center; justify-content: space-between; gap: 12px;">
                <div style="flex: 1;">
                    <p style="font-size: 12pt; font-weight: 800;">
                        إذا علمتَ أن في مثلثين: تطابق ضلعان وزاوية <u>غير محصورة</u> بينهما (<span dir="ltr">SSA</span>)؛ فهل يكفي ذلك دائماً لإثبات تطابقهما؟
                    </p>
                    <div style="margin-top: 6px; display: flex; align-items: center; gap: 18px; font-size: 12pt; font-weight: 900;">
                        <label><span class="check-box"></span> نـعـم، يكفي</label>
                        <label><span class="check-box"></span> لا، لا يكفي (حالة غير صالحة للتطابق)</label>
                    </div>
                </div>
                <div style="border-right: 2px solid #000; padding-right: 12px; min-width: 180px; text-align: center;">
                    <div style="font-size: 11pt; font-weight: 800; margin-bottom: 4px;">التقييم الذاتي السريع:</div>
                    <div style="font-size: 10.5pt; font-weight: 700;">
                        <div><span class="check-box"></span> فهمت بنسبة 100%</div>
                        <div><span class="check-box"></span> أحتاج تدريباً بسيطاً</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 6. الفوتر: التوقيع والدرجة -->
        <footer class="footer-bar">
            <div>ملاحظات وتوقيع المعلم: ....................................................</div>
            <div style="font-size: 12pt; font-weight: 900;">الدرجة المستحقة: [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 10 ]</div>
        </footer>

    </div>

</body>
</html>
'''

output_path = r'c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\ورقة_انخراط_تطابق_المثلثات_SSS_SAS_ورقة_واحدة.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Generated single page engagement worksheet at: {output_path}")
