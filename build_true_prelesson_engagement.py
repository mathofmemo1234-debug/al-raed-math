# -*- coding: utf-8 -*-
"""
Generate a Large-Font, Black & White, Single-Page A4 Student Engagement / Pre-Lesson Hook Worksheet.
Concept: انخراط وتهيئة قبل معرفة الدرس (Engage & Hook before introducing SSS / SAS).
Focus: Rigidity of triangles, 6 congruence parts vs shortcuts, hands-on thought experiment.
"""

import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>بطاقة انخراط وتهيئة قبل الدرس: لغز ثبات المثلثات والتطابق</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&display=swap" rel="stylesheet">
    <style>
        /* إعدادات الطباعة الدقيقة لصفحة واحدة A4 فقط */
        @page {
            size: A4 portrait;
            margin: 5mm 7mm 5mm 7mm;
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

        /* الحاوية الكلية لصفحة A4 واحدة فقط بدون أي خروج للصفحة الثانية */
        .page-container {
            width: 100%;
            max-width: 196mm;
            height: 282mm;
            max-height: 284mm;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            border: 2.5px solid #000000;
            padding: 7mm 8mm;
            background: #ffffff;
        }

        /* ترويسة البطاقة */
        .header-box {
            border-bottom: 2.2px solid #000000;
            padding-bottom: 5px;
            margin-bottom: 6px;
        }

        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11pt;
            font-weight: 800;
            margin-bottom: 3px;
        }

        .badge-tag {
            background-color: #000000;
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 10.5pt;
            font-weight: 900;
        }

        .main-title {
            text-align: center;
            font-size: 16.5pt;
            font-weight: 900;
            background-color: #f0f0f0;
            border: 2px solid #000000;
            padding: 3px 10px;
            border-radius: 6px;
            margin-bottom: 5px;
        }

        .student-info {
            display: flex;
            justify-content: space-between;
            background: #ffffff;
            border: 1.8px solid #000000;
            border-radius: 5px;
            padding: 4px 10px;
            font-size: 12pt;
            font-weight: 800;
        }

        .dotted-line {
            display: inline-block;
            border-bottom: 2px dotted #000000;
            min-height: 16px;
            vertical-align: bottom;
        }

        /* البطاقات والمهام */
        .task-card {
            border: 2px solid #000000;
            border-radius: 6px;
            padding: 6px 9px;
            margin-bottom: 6px;
            background: #ffffff;
        }

        .task-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #000000;
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 13pt;
            font-weight: 900;
            margin-bottom: 6px;
        }

        .task-body {
            font-size: 12pt;
            font-weight: 800;
        }

        /* الرسوم الهندسية باللون الأسود الناصع */
        svg {
            display: block;
            margin: auto;
        }

        .geo-line {
            stroke: #000000;
            stroke-width: 2.6;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .geo-dashed {
            stroke: #000000;
            stroke-width: 2.2;
            stroke-dasharray: 4,3;
        }

        .geo-text {
            font-family: 'Cairo', sans-serif;
            font-size: 12px;
            font-weight: 900;
            fill: #000000;
        }

        .check-box {
            display: inline-block;
            width: 18px;
            height: 18px;
            border: 2.2px solid #000000;
            border-radius: 3px;
            vertical-align: middle;
            margin-left: 5px;
            background-color: #ffffff;
        }

        /* تذييل الصفحة */
        .footer-box {
            border-top: 2px solid #000000;
            padding-top: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11.5pt;
            font-weight: 800;
        }

        /* زر الطباعة */
        .no-print-bar {
            max-width: 196mm;
            margin: 10px auto 6px auto;
            text-align: center;
        }

        .btn-print {
            background-color: #000000;
            color: #ffffff;
            border: none;
            padding: 8px 26px;
            font-size: 13pt;
            font-weight: 900;
            font-family: 'Cairo', sans-serif;
            border-radius: 6px;
            cursor: pointer;
        }

        .btn-print:hover {
            background-color: #333333;
        }

        @media print {
            .no-print-bar {
                display: none !important;
            }
            body {
                background: none !important;
            }
            .page-container {
                border: 2px solid #000000 !important;
                height: 282mm !important;
                max-height: 282mm !important;
                page-break-after: avoid !important;
                page-break-inside: avoid !important;
            }
        }
    </style>
</head>
<body>

    <!-- زر للطباعة السريعة للشاشة فقط -->
    <div class="no-print-bar">
        <button class="btn-print" onclick="window.print()">🖨️ طباعة بطاقة الانخراط والتهيئة (صفحة A4 واحدة)</button>
    </div>

    <!-- حاوية الورقة الواحدة A4 -->
    <div class="page-container">

        <!-- 1. الترويسة وبيانات الطالب -->
        <header class="header-box">
            <div class="header-top">
                <div>المملكة العربية السعودية — وزارة التعليم</div>
                <div class="badge-tag">نشاط انخراط واستهلال صفي (Engage)</div>
                <div>الزمن المقترح: 5 دقائق</div>
            </div>
            <div class="main-title">
                بطاقة انخراط ذهني: لغز ثبات المثلثات وسر التطابق التام
            </div>
            <div class="student-info">
                <div>اسم الطالب: <span class="dotted-line" style="width: 220px;"></span></div>
                <div>الفصل: <span class="dotted-line" style="width: 70px;"></span></div>
                <div>المجموعة: <span class="dotted-line" style="width: 70px;"></span></div>
                <div>التاريخ: &nbsp;&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;/ 1448هـ</div>
            </div>
        </header>

        <!-- 2. المهمة 1: مفارقة الصلابة وتحدي الأشكال (Hook & Rigidity) -->
        <section class="task-card">
            <div class="task-header">
                <span>⚡ المهمة 1: لغز الصلابة الهندسية (لماذا المثلث تحديداً؟)</span>
                <span style="font-size: 10.5pt; font-weight: 800;">تأمّل الرسم الهندسي</span>
            </div>
            <div class="task-body" style="display: flex; align-items: center; gap: 14px;">
                <!-- رسم مقارنة الإطار الرباعي والمثلث باللون الأسود الواضح -->
                <div style="width: 215px; border: 1.8px solid #000; border-radius: 5px; padding: 4px; text-align: center; background: #fafafa;">
                    <svg width="205" height="85" viewBox="0 0 205 85">
                        <!-- الشكل الرباعي يتشوه ويميل -->
                        <polygon points="15,70 65,70 50,22 10,22" fill="none" class="geo-line" />
                        <!-- سهم الدفع -->
                        <line x1="5" y1="14" x2="22" y2="20" stroke="#000" stroke-width="2.5" stroke-dasharray="2,2" />
                        <polygon points="24,21 16,16 20,26" fill="#000" />
                        <text x="36" y="80" text-anchor="middle" class="geo-text">مربع يميل ويتشوه!</text>

                        <!-- فاصل رأسي -->
                        <line x1="95" y1="10" x2="95" y2="78" stroke="#000" stroke-width="1.5" stroke-dasharray="3,3" />

                        <!-- المثلث الصلب -->
                        <polygon points="115,70 185,70 150,20" fill="none" class="geo-line" />
                        <!-- ذراع التثبيت أو إشارة الصلابة -->
                        <line x1="130" y1="48" x2="170" y2="48" stroke="#000" stroke-width="2.2" />
                        <text x="150" y="80" text-anchor="middle" class="geo-text">مثلث صلب وثابت تماماً</text>
                    </svg>
                </div>

                <!-- نص التحدي والسؤال التفكيري -->
                <div style="flex: 1; display: flex; flex-direction: column; gap: 5px;">
                    <p style="font-size: 12pt; line-height: 1.35;">
                        <strong>شاهد وفكّر:</strong> إذا ضغطنا على رأس إطار رباعي يتغير شكله وتتغير زواياه فوراً، بينما <strong>يستحيل تشويه المثلث</strong> أو تغيير زواياه طالما بقيت أطوال أضلاعه الثلاثة ثابتة!
                    </p>
                    <div style="background: #f4f4f4; border: 1.5px solid #000; border-radius: 4px; padding: 4px 8px; font-size: 11.5pt;">
                        <strong>س: ماذا تستنتج؟</strong> هل تثبيت أطوال الأضلاع الثلاثة في أي مثلث كافٍ لتثبيت قياسات زواياه بالكامل وتحديد شكله الوحيد؟
                        <div style="margin-top: 3px; font-weight: 900;">
                            <label><span class="check-box"></span> نـعـم، الأضلاع الثلاثة تثبّت الزوايا والشكل حتماً.</label>
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            <label><span class="check-box"></span> لا، قد تتغير الزوايا.</label>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. المهمة 2: تنشيط المعرفة السابقة (ماذا يعني تطابق مثلثين؟) -->
        <section class="task-card">
            <div class="task-header">
                <span>🧠 المهمة 2: تنشيط الخبرة السابقة (عناصر التطابق التام الستة)</span>
                <span style="font-size: 10.5pt; font-weight: 800;">كتاب الطالب ص 162</span>
            </div>
            <div class="task-body" style="display: flex; align-items: center; justify-content: space-between; gap: 12px;">
                <!-- رسم توضيحي لعناصر التطابق الستة -->
                <div style="width: 200px; border: 1.8px solid #000; border-radius: 5px; padding: 3px; text-align: center;">
                    <svg width="190" height="75" viewBox="0 0 190 75">
                        <polygon points="15,65 75,65 30,18" fill="none" class="geo-line" />
                        <text x="30" y="14" class="geo-text">A</text>
                        <text x="8" y="70" class="geo-text">B</text>
                        <text x="82" y="70" class="geo-text">C</text>

                        <text x="95" y="44" text-anchor="middle" font-size="16" font-weight="900" fill="#000">≅</text>

                        <polygon points="115,65 175,65 130,18" fill="none" class="geo-line" />
                        <text x="130" y="14" class="geo-text">D</text>
                        <text x="108" y="70" class="geo-text">E</text>
                        <text x="182" y="70" class="geo-text">F</text>
                    </svg>
                    <div style="font-size: 10pt; font-weight: 800;">3 أضلاع متناظرة + 3 زوايا متناظرة</div>
                </div>

                <!-- الأسئلة الاسترجاعية -->
                <div style="flex: 1; font-size: 12pt; line-height: 1.4;">
                    <div>
                        في الدرس السابق، لكي نحكم بأن المثلثين متطابقان <span dir="ltr"><strong>(&Delta;ABC &cong; &Delta;DEF)</strong></span>؛ 
                        كنا نحتاج للتأكد من تطابق <strong>جميع العناصر الستة</strong>:
                    </div>
                    <div style="margin-top: 4px; padding: 4px 8px; border: 1.5px dashed #000; border-radius: 4px; background: #fafafa;">
                        • عدد الأضلاع المتناظرة المتطابقة: ( &nbsp;<strong><span class="dotted-line" style="width: 40px;"></span></strong>&nbsp; ) أضلاع.
                        &nbsp;&nbsp;&nbsp;&nbsp;
                        • عدد الزوايا المتناظرة المتطابقة: ( &nbsp;<strong><span class="dotted-line" style="width: 40px;"></span></strong>&nbsp; ) زوايا.
                        <div style="font-size: 11pt; margin-top: 2px;">
                            المجموع الكلي للعناصر المفحوصة سابقاً = ( <strong>6</strong> عناصر كاملة ).
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. المهمة 3: تفجير التساؤل والفرضيات (Inquiry & Hypothesis) -->
        <section class="task-card">
            <div class="task-header">
                <span>🔥 المهمة 3: تفجير التساؤل (هل نحتاج فعلاً لفحص العناصر الستة كلها؟)</span>
                <span style="font-size: 10.5pt; font-weight: 800;">تحدي المهندس الذكي</span>
            </div>
            <div class="task-body">
                <p style="font-size: 12pt; margin-bottom: 5px;">
                    <strong>تخيل أنك مهندس في موقع بناء:</strong> هل من المنطقي أن تقيس في كل مرة 3 أضلاع و 3 زوايا بالمنقلة لتثبت تطابق قطعتين، أم يمكن إيجاد <strong>شروط مختصرة (أسرار سريعة)</strong> تكفي تماماً لإثبات التطابق بأقل مجهود؟
                </p>

                <!-- التجربتان الذهنيتان لاكتشاف شروط التطابق قبل تسميتها -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 4px;">
                    <!-- التجربة الأولى: الأضلاع الثلاثة -->
                    <div style="border: 1.8px solid #000; border-radius: 5px; padding: 5px; background: #fafafa;">
                        <div style="font-weight: 900; font-size: 12pt; border-bottom: 1.5px solid #000; padding-bottom: 2px; margin-bottom: 3px;">
                            التجربة (أ): إعطاء 3 أطوال أضلاع فقط
                        </div>
                        <p style="font-size: 11.5pt;">
                            لو أعطى المعلم كل طالب في الفصل 3 قِطَع خشبية بأطوال (3cm, 4cm, 5cm):
                            هل يمكن لطالب أن يصنع مثلثاً <u>يختلف في الشكل أو الزوايا</u> عن زميله؟
                        </p>
                        <div style="margin-top: 4px; font-weight: 900; font-size: 11pt;">
                            <label><span class="check-box"></span> نعم، يمكن رسم أشكال مختلفة.</label><br>
                            <label><span class="check-box"></span> لا، مستحيل! الجميع سينتهي لنفس المثلث تماماً.</label>
                        </div>
                    </div>

                    <!-- التجربة الثانية: ضلعان وزاوية محصورة بينهما -->
                    <div style="border: 1.8px solid #000; border-radius: 5px; padding: 5px; background: #fafafa;">
                        <div style="font-weight: 900; font-size: 12pt; border-bottom: 1.5px solid #000; padding-bottom: 2px; margin-bottom: 3px;">
                            التجربة (ب): تثبيت ضلعين والزاوية بينهما
                        </div>
                        <p style="font-size: 11.5pt;">
                            إذا فتحت فرجاراً أو عقربي ساعة بطولين ثابتين وثبّتت فتحة الزاوية بينهما تماماً:
                            هل المسافة بين الطرفين (الضلع الثالث) تكون محددة وثابتة؟
                        </p>
                        <div style="margin-top: 4px; font-weight: 900; font-size: 11pt;">
                            <label><span class="check-box"></span> نعم، يتحدد البعد الثالث تلقائياً وحتماً.</label><br>
                            <label><span class="check-box"></span> لا، يمكن أن يتغير البعد الثالث.</label>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. المهمة 4: نافذة الانطلاق إلى الدرس الجديد (Launch to New Lesson) -->
        <section class="task-card" style="margin-bottom: 2px;">
            <div class="task-header">
                <span>🚀 المهمة 4: توقّعك الذكي لدرس اليوم (بوابة الدخول)</span>
                <span style="font-size: 10.5pt; font-weight: 800;">الفرضية العلمية</span>
            </div>
            <div class="task-body" style="display: flex; align-items: center; justify-content: space-between; gap: 10px;">
                <div style="flex: 1; font-size: 12pt;">
                    <div>
                        <strong>في رأيك:</strong> ما هو أقل عدد كافٍ من عناصر المثلث (أضلاع أو زوايا) لإثبات التطابق التام دون الحاجة لقياس بقية العناصر؟
                        &nbsp;&nbsp;أقل عدد كافٍ هو: [ &nbsp;<strong><span class="dotted-line" style="width: 45px;"></span></strong>&nbsp; عناصر ].
                    </div>
                    <div style="margin-top: 4px; font-size: 11pt; color: #111;">
                        🎯 <strong>الهدف الذي سنثبته في الحصة:</strong> سنكتشف معاً مسلّمتين رياضيتين عظيمتين تتيحان إثبات تطابق أي مثلثين باستخدام 3 عناصر فقط وبدون قياس الستة كاملة!
                    </div>
                </div>
                <div style="width: 140px; border-right: 2px solid #000; padding-right: 8px; text-align: center; font-weight: 800;">
                    <div style="font-size: 10.5pt;">مستوى الحماس والفضول للدرس الجديد:</div>
                    <div style="font-size: 16pt; margin-top: 2px;">🔥 🔥 🔥</div>
                </div>
            </div>
        </section>

        <!-- 6. الفوتر: تفاعل المعلم والملاحظة السريعة -->
        <footer class="footer-box">
            <div>ملاحظة المعلم للتفاعل الاستهلالي: ....................................................</div>
            <div style="font-size: 12pt; font-weight: 900;">تقييم الانخراط: [ &nbsp;&nbsp; متميز ⭐ &nbsp;&nbsp;&nbsp;&nbsp; متفاعل 👍 &nbsp;&nbsp; ]</div>
        </footer>

    </div>

</body>
</html>
'''

output_path = r'c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\بطاقة_انخراط_وتهيئة_قبل_الدرس_تطابق_المثلثات.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Generated Pre-Lesson Engagement & Hook Worksheet at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
