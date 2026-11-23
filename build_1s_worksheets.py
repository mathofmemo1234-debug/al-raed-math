# -*- coding: utf-8 -*-
"""
build_1s_worksheets.py: Generates all 8 interactive worksheets and tests
for Grade 10 (1st Secondary - First Term - Paths) pages 146 to 200.
Using raw strings to ensure 100% clean LaTeX typesetting and zero escaping bugs.
"""
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

import svg_geometry_library as svg_lib
import generator_1s_header_styles as styles

WORKSHEETS_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية (8 أوراق عمل متتالية)      -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية (8 أوراق عمل متتالية)</h2>
            <span class="section-badge">مجهزة بأزرار إظهار الإجابة للمعلم ومحجوبة عند الطباعة</span>
        </div>
"""

def generate_ws_1():
    header = styles.make_school_header("ورقة عمل تطبيقية: تصنيف المثلثات", "الفصل 3: الدرس 3-1 (ص 146 – 152)", "1")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-1")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws1_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-1) -->
        <article class="unit-card worksheet-card" id="ws-3-1">
            <div class="unit-title-box">
                <h3><span>1️⃣</span> ورقة عمل (3-1): تصنيف المثلثات (Classifying Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 146 – 152</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر رمز الإجابة الصحيحة لكل فقرة من الفقرات الآتية:</div>

                <!-- فقرة 1 -->
                <p><strong>1.</strong> مثلث قياسات زواياه هي: \(28^\circ, 62^\circ, 90^\circ\). يصنف وفق زواياه بأنه مثلث:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> حاد الزوايا (Acute)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> قائم الزاوية (Right)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> منفرج الزاوية (Obtuse)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> متطابق الزوايا (Equiangular)</div>
                </div>

                <!-- فقرة 2 -->
                <p style="margin-top:14px;"><strong>2.</strong> إذا كانت أطوال أضلاع مثلث هي: \(7\text{ cm}, 7\text{ cm}, 10\text{ cm}\)، فإن تصنيفه وفق أضلاعه هو:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> مختلف الأضلاع (Scalene)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> متطابق الأضلاع (Equilateral)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> متطابق الضلعين (Isosceles)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> متطابق الزوايا (Equiangular)</div>
                </div>

                <!-- فقرة 3 -->
                <p style="margin-top:14px;"><strong>3.</strong> أي من مجموعات الزوايا الآتية تمثل قياسات زوايا مثلث حاد الزوايا؟</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(45^\circ, 45^\circ, 90^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(30^\circ, 40^\circ, 110^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(55^\circ, 60^\circ, 65^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(20^\circ, 70^\circ, 90^\circ\)</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (B)</strong> قائم الزاوية؛ لاحتوائه على زاوية قياسها \(90^\circ\).</p>
                    <p><strong>2. (C)</strong> متطابق الضلعين؛ لوجود ضلعين متطابقين طول كل منهما \(7\text{ cm}\).</p>
                    <p><strong>3. (C)</strong> \(55^\circ, 60^\circ, 65^\circ\)؛ لأن جميع قياسات الزوايا أصغر تماماً من \(90^\circ\).</p>
                </div>
            </div>

            <!-- السؤال الثاني: الصواب والخطأ -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (صواب / خطأ)</span>
                    <span class="q-dok-badge">DOK 2 (فهم وتحليل)</span>
                </div>
                <div class="q-body">ضع علامة (✓) أمام العبارة الصحيحة وعلامة (✗) أمام العبارة الخاطئة مع تصحيح الخطأ إن وجد:</div>
                <p>1. ( &emsp; ) يمكن أن يحوي المثلث الواحد زاويتين منفرجتين في الوقت نفسه.</p>
                <p>2. ( &emsp; ) كل مثلث متطابق الأضلاع هو حتماً مثلث متطابق الضلعين.</p>
                <p>3. ( &emsp; ) إذا تطابقت زوايا مثلث فإن أطوال أضلاعه تكون مختلفة.</p>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الثاني:</div>
                    <p>1. <strong>(✗) خطأ؛</strong> لأن مجموع قياسات زوايا المثلث يساوي \(180^\circ\)، وزاويتان منفرجتان مجموعهما يتجاوز \(180^\circ\).</p>
                    <p>2. <strong>(✓) صواب؛</strong> لأن المثلث المتطابق الأضلاع يحوي 3 أضلاع متطابقة، وبالتالي يحقق شرط وجود ضلعين متطابقين على الأقل.</p>
                    <p>3. <strong>(✗) خطأ؛</strong> المثلث متطابق الزوايا يكون دائماً متطابق الأضلاع.</p>
                </div>
            </div>

            <!-- السؤال الثالث: المسألة التطبيقية الهندسية والجبرية -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثالث (تطبيق هندسي وجبري)</span>
                    <span class="q-dok-badge">DOK 3 (تفكير استراتيجي ونمذجة)</span>
                </div>
                <div class="q-body">
                    في الشكل الهندسي المقابل، \(\triangle ABC\) مثلث متطابق الضلعين فيه \(AB = AC\)، والنقطة \(D\) تقع على منتصف القاعدة \(BC\).<br>
                    إذا كان: \(AB = 4x + 3\) و \(AC = 6x - 7\) و \(BD = 2x + 1\).<br>
                    <strong>المطلوب:</strong><br>
                    أ) أوجد قيمة المتغير \(x\).<br>
                    ب) أوجد أطوال الأضلاع: \(AB\), \(AC\), \(BC\).<br>
                    جـ) احسب محيط \(\triangle ABC\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات الحل النموذجي بالتفصيل:</div>
                    <p><strong>أ) إيجاد قيمة \(x\):</strong><br>
                    بما أن المثلث متطابق الضلعين وفيه \(AB = AC\):<br>
                    \[6x - 7 = 4x + 3 \implies 6x - 4x = 3 + 7 \implies 2x = 10 \implies x = 5\]
                    </p>
                    <p><strong>ب) حساب أطوال الأضلاع:</strong><br>
                    طول \(AB = 4(5) + 3 = 20 + 3 = 23\).<br>
                    طول \(AC = 6(5) - 7 = 30 - 7 = 23\).<br>
                    طول نصف القاعدة \(BD = 2(5) + 1 = 11\).<br>
                    بما أن \(D\) نقطة المنتصف فإن طول القاعدة كاملة: \(BC = 2 \times BD = 2 \times 11 = 22\).
                    </p>
                    <p><strong>جـ) حساب المحيط:</strong><br>
                    محيط المثلث \(P = AB + AC + BC = 23 + 23 + 22 = 68\) وحدة طول.
                    </p>
                </div>
            </div>

            <!-- السؤال الرابع: تحدي مهارات التفكير العليا -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الرابع (تحدٍّ إثرائي DOK 4)</span>
                    <span class="q-dok-badge">مهارات تفكير عليا</span>
                </div>
                <div class="q-body">
                    <strong>اكتشف الخطأ وتبرير المنطق الرياضي:</strong><br>
                    يدّعي خالد أن المثلث الذي إحداثيات رؤوسه في المستوى الديكارتي هي \(A(0, 0)\), \(B(4, 0)\), \(C(2, 2\sqrt{3})\) هو مثلث متطابق الأضلاع.<br>
                    بينما يدّعي سعد أنه مثلث متطابق الضلعين فقط وليس متطابق الأضلاع.<br>
                    باستعمال قانون المسافة بين نقطتين، احسب أطوال الأضلاع الثلاثة بدقة لتحديد من منهما على صواب، مع ذكر تصنيف المثلث وفق زواياه.
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل والتحليل الرياضي الدقيق:</div>
                    <p>نطبق قانون المسافة: \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\):<br>
                    1. طول \(AB = \sqrt{(4 - 0)^2 + (0 - 0)^2} = \sqrt{16} = 4\).<br>
                    2. طول \(AC = \sqrt{(2 - 0)^2 + (2\sqrt{3} - 0)^2} = \sqrt{4 + 12} = \sqrt{16} = 4\).<br>
                    3. طول \(BC = \sqrt{(2 - 4)^2 + (2\sqrt{3} - 0)^2} = \sqrt{(-2)^2 + 12} = \sqrt{4 + 12} = \sqrt{16} = 4\).<br>
                    <strong>الاستنتاج:</strong> الأضلاع الثلاثة متطابقة وطول كل منها 4 وحدات (\(AB = AC = BC = 4\)).<br>
                    إذن <strong>خالد على صواب تام؛</strong> المثلث متطابق الأضلاع (Equilateral).<br>
                    وتصنيفه وفق زواياه هو: <strong>متطابق الزوايا (Equiangular)</strong> وقياس كل زاوية فيه يساوي \(60^\circ\).
                    </p>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_2():
    header = styles.make_school_header("ورقة عمل تطبيقية: زوايا المثلثات", "الفصل 3: الدرس 3-2 (ص 153 – 161)", "2")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-2")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws2_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-2) -->
        <article class="unit-card worksheet-card" id="ws-3-2">
            <div class="unit-title-box">
                <h3><span>2️⃣</span> ورقة عمل (3-2): زوايا المثلثات (Angles of Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 153 – 161</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر رمز الإجابة الصحيحة في كل مما يأتي:</div>

                <p><strong>1.</strong> في \(\triangle ABC\)، إذا كان \(m\angle A = 40^\circ\) و \(m\angle B = 75^\circ\)، فإن قياس الزاوية الثالثة \(m\angle C\) يساوي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(55^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(65^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(70^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(85^\circ\)</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> قياس الزاوية الخارجية لمثلث يساوي دائماً:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> مجموع الزاويتين الداخليتين البعيدتين عنها</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> ضعف الزاوية المجاورة لها</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> دائماً زاوية منفرجة</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(180^\circ\) ناقص مجموع زوايا المثلث</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> في أي مثلث قائم الزاوية، تكون الزاويتان الحادتان دائماً:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> متكاملتين (مجموعهما \(180^\circ\))</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> متتامتين (مجموعهما \(90^\circ\))</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> متطابقتين حتماً</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> منفرجتين</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (B)</strong> \(65^\circ\)؛ لأن \(180^\circ - (40^\circ + 75^\circ) = 180^\circ - 115^\circ = 65^\circ\).</p>
                    <p><strong>2. (A)</strong> مجموع قياسي الزاويتين الداخليتين البعيدتين عنها وفق نظرية الزاوية الخارجية.</p>
                    <p><strong>3. (B)</strong> متتامتين وفق النتيجة 3.1 للمثلث القائم (\(m\angle 1 + m\angle 2 = 90^\circ\)).</p>
                </div>
            </div>

            <!-- السؤال الثاني: مسألة الزاوية الخارجية والجبر -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (تطبيق نظري وجبري)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    في الشكل الهندسي المقابل، امتد الضلع \(QR\) إلى النقطة \(S\) مشكلاً زاوية خارجية قياسها \((7x - 20)^\circ\).<br>
                    وكان قياسا الزاويتين الداخليتين البعيدتين هما: \(m\angle P = (2x + 15)^\circ\) و \(m\angle Q = (3x - 5)^\circ\).<br>
                    <strong>المطلوب:</strong><br>
                    1. اكتب معادلة جبرية تربط بين الزوايا استناداً لنظرية الزاوية الخارجية.<br>
                    2. أوجد قيمة \(x\).<br>
                    3. احسب قياس كل من الزوايا الثلاث: \(m\angle P\), \(m\angle Q\), \(m\angle PRS\).<br>
                    4. احسب قياس الزاوية الداخلية المجاورة \(m\angle PRQ\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات الحل النموذجي بالتفصيل:</div>
                    <p><strong>1. المعادلة الجبرية:</strong><br>
                    قياس الزاوية الخارجية = مجموع قياسي الزاويتين الداخليتين البعيدتين:<br>
                    \[7x - 20 = (2x + 15) + (3x - 5)\]
                    </p>
                    <p><strong>2. حل المعادلة:</strong><br>
                    \[7x - 20 = 5x + 10 \implies 7x - 5x = 10 + 20 \implies 2x = 30 \implies x = 15\]
                    </p>
                    <p><strong>3. حساب قياسات الزوايا:</strong><br>
                    \[m\angle P = 2(15) + 15 = 30 + 15 = 45^\circ\]
                    \[m\angle Q = 3(15) - 5 = 45 - 5 = 40^\circ\]
                    \[m\angle PRS = 7(15) - 20 = 105 - 20 = 85^\circ\]
                    التحقق: \(45^\circ + 40^\circ = 85^\circ\) (صحيح تماماً).
                    </p>
                    <p><strong>4. قياس الزاوية المجاورة \(\angle PRQ\):</strong><br>
                    بما أنهما تشكلان زاوية مستقيمة (زوج خطي):<br>
                    \[m\angle PRQ = 180^\circ - 85^\circ = 95^\circ\]
                    </p>
                </div>
            </div>

            <!-- السؤال الثالث: برهان هندسي قصير -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثالث (استدلال وبرهان)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    <strong>البرهان الهندسي:</strong> أثبت أن قياس أي زاوية خارجية لمثلث متطابق الأضلاع يساوي دائماً \(120^\circ\).
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ البرهان المنطقي:</div>
                    <p>1. بما أن المثلث متطابق الأضلاع، فإنه متطابق الزوايا، وقياس كل زاوية داخلية فيه يساوي \(60^\circ\).<br>
                    2. الزاويتان الداخليتان البعيدتان عن أي زاوية خارجية قياس كل منهما \(60^\circ\).<br>
                    3. بحسب نظرية الزاوية الخارجية للمثلث، فإن قياس الزاوية الخارجية يساوي مجموع قياسي الزاويتين الداخليتين البعيدتين:<br>
                    \[m\angle ext = 60^\circ + 60^\circ = 120^\circ\]
                    (أو بالاعتماد على الزاوية المستقيمة: \(180^\circ - 60^\circ = 120^\circ\)). وهو المطلوب إثباته.
                    </p>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_3():
    header = styles.make_school_header("ورقة عمل تطبيقية: المثلثات المتطابقة", "الفصل 3: الدرس 3-3 (ص 162 – 169)", "3")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-3")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws3_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-3) -->
        <article class="unit-card worksheet-card" id="ws-3-3">
            <div class="unit-title-box">
                <h3><span>3️⃣</span> ورقة عمل (3-3): المثلثات المتطابقة (Congruent Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 162 – 169</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر الإجابة الصحيحة:</div>

                <p><strong>1.</strong> إذا كان \(\triangle ABC \cong \triangle DFE\)، فإن الضلع المناظر للضلع \(\overline{BC}\) هو:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(\overline{DE}\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(\overline{FE}\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(\overline{DF}\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(\overline{EF}\)</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> إذا كان \(\triangle JKL \cong \triangle PQR\)، وكان \(m\angle J = 50^\circ\) و \(m\angle K = 70^\circ\)، فإن قياس \(\angle R\) يساوي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(50^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(60^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(70^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(120^\circ\)</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> العبارة التي تعبر عن خاصية التعدي لتطابق المثلثات هي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(\triangle ABC \cong \triangle ABC\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> إذا كان \(\triangle ABC \cong \triangle DEF\) فإن \(\triangle DEF \cong \triangle ABC\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> إذا كان \(\triangle 1 \cong \triangle 2\) و \(\triangle 2 \cong \triangle 3\) فإن \(\triangle 1 \cong \triangle 3\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> إذا تطابقت زوايا مثلثين فإنهما متطابقان</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (B)</strong> \(\overline{FE}\)؛ لأن الحرفين الثاني والثالث في \(\triangle ABC\) يقابلهما الحرفان الثاني والثالث في \(\triangle DFE\).</p>
                    <p><strong>2. (B)</strong> \(60^\circ\)؛ لأن \(m\angle L = 180^\circ - (50^\circ + 70^\circ) = 60^\circ\)، وبما أن \(\angle R\) تناظر \(\angle L\) (CPCTC) فإن \(m\angle R = 60^\circ\).</p>
                    <p><strong>3. (C)</strong> خاصية التعدي (Transitive Property).</p>
                </div>
            </div>

            <!-- السؤال الثاني: تطبيق CPCTC والجبر -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (حل وتطبيق جبري)</span>
                    <span class="q-dok-badge">DOK 2</span>
                </div>
                <div class="q-body">
                    في الشكل المقابل، المضلعان متطابقان: \(ABCD \cong WXYZ\).<br>
                    إذا كان: \(AB = 2x + 4\), \(WX = 18\), \(BC = 12\), \(XY = 3y - 3\).<br>
                    <strong>المطلوب:</strong><br>
                    1. حدد جميع أزواج الأضلاع المتناظرة المتطابقة.<br>
                    2. أوجد قيمة كل من المتغيرين \(x\) و \(y\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الثاني:</div>
                    <p><strong>1. أزواج الأضلاع المتناظرة المتطابقة:</strong><br>
                    \(\overline{AB} \cong \overline{WX}\)، \(\overline{BC} \cong \overline{XY}\)، \(\overline{CD} \cong \overline{YZ}\)، \(\overline{DA} \cong \overline{ZW}\).
                    </p>
                    <p><strong>2. حساب قيم المتغيرات:</strong><br>
                    بما أن \(AB = WX \implies 2x + 4 = 18 \implies 2x = 14 \implies x = 7\).<br>
                    بما أن \(BC = XY \implies 12 = 3y - 3 \implies 3y = 15 \implies y = 5\).
                    </p>
                </div>
            </div>

            <!-- السؤال الثالث: برهان نظرية الزاوية الثالثة -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثالث (برهان ذو عمودين)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    <strong>المعطيات:</strong> في \(\triangle ABC\) و \(\triangle DEF\): \(\angle A \cong \angle D\) و \(\angle B \cong \angle E\).<br>
                    <strong>المطلوب:</strong> إثبات أن \(\angle C \cong \angle F\) (برهان نظرية الزاوية الثالثة).
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ البرهان ذو العمودين:</div>
                    <table class="proof-table">
                        <thead>
                            <tr>
                                <th>العبارات (Statements)</th>
                                <th>التبريرات (Reasons)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="proof-col-stmt">1. \(\angle A \cong \angle D\), \(\angle B \cong \angle E\)</td>
                                <td class="proof-col-reason">1. معطيات (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">2. \(m\angle A = m\angle D\), \(m\angle B = m\angle E\)</td>
                                <td class="proof-col-reason">2. تعريف تطابق الزوايا (Def. of Congruent Angles)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">3. \(m\angle A + m\angle B + m\angle C = 180^\circ\)<br>\(m\angle D + m\angle E + m\angle F = 180^\circ\)</td>
                                <td class="proof-col-reason">3. نظرية مجموع قياسات زوايا المثلث (Triangle Angle-Sum)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">4. \(m\angle A + m\angle B + m\angle C = m\angle D + m\angle E + m\angle F\)</td>
                                <td class="proof-col-reason">4. خاصية التعويض / التعدي للمساواة (Substitution Property)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">5. \(m\angle D + m\angle E + m\angle C = m\angle D + m\angle E + m\angle F\)</td>
                                <td class="proof-col-reason">5. خاصية التعويض (Substitution of \(A\) and \(B\))</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">6. \(m\angle C = m\angle F \implies \angle C \cong \angle F\)</td>
                                <td class="proof-col-reason">6. خاصية الطرح للمساواة وتعريف التطابق. وهو المطلوب.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_4():
    header = styles.make_school_header("ورقة عمل تطبيقية: إثبات تطابق المثلثات SSS, SAS", "الفصل 3: الدرس 3-4 (ص 170 – 177)", "4")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-4")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws4_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-4) -->
        <article class="unit-card worksheet-card" id="ws-3-4">
            <div class="unit-title-box">
                <h3><span>4️⃣</span> ورقة عمل (3-4): إثبات تطابق المثلثات SSS, SAS</h3>
                <span class="page-range-pill">كتاب الطالب: ص 170 – 177</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر رمز الإجابة الصحيحة:</div>

                <p><strong>1.</strong> مسلمة التطابق بضلعين والزاوية المحصورة بينهما يرمز لها بالرمز:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> SSS</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> SAS</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> ASA</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> AAS</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> الزاوية المحصورة بين الضلعين \(\overline{XY}\) و \(\overline{YZ}\) في \(\triangle XYZ\) هي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(\angle X\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(\angle Y\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(\angle Z\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> الزاوية الخارجية</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> عندما يشترك مثلثان في ضلع واحد مثل \(\overline{BD}\)، فإن التبرير الرياضي لتطابق الضلع مع نفسه (\(BD \cong BD\)) هو:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> خاصية الانعكاس للتطابق (Reflexive)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> خاصية التماثل (Symmetric)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> تعريف نقطة المنتصف</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> مسلمة الجمع</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (B)</strong> SAS (Side-Angle-Side).</p>
                    <p><strong>2. (B)</strong> \(\angle Y\)؛ لأن الرأس المشترك بين الضلعين \(XY\) و \(YZ\) هو \(Y\).</p>
                    <p><strong>3. (A)</strong> خاصية الانعكاس للتطابق.</p>
                </div>
            </div>

            <!-- السؤال الثاني: برهان ذو عمودين بمسلمة SSS -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (برهان هندسي كامل)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    في الشكل الهندسي المقابل:<br>
                    <strong>المعطيات:</strong> \(\overline{AB} \cong \overline{CD}\) و \(\overline{AD} \cong \overline{CB}\).<br>
                    <strong>المطلوب:</strong> اكتب برهاناً ذا عمودين لإثبات أن \(\triangle ABD \cong \triangle CDB\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات البرهان ذي العمودين الكامل:</div>
                    <table class="proof-table">
                        <thead>
                            <tr>
                                <th>العبارات (Statements)</th>
                                <th>التبريرات (Reasons)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="proof-col-stmt">1. \(\overline{AB} \cong \overline{CD}\)</td>
                                <td class="proof-col-reason">1. معطى (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">2. \(\overline{AD} \cong \overline{CB}\)</td>
                                <td class="proof-col-reason">2. معطى (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">3. \(\overline{BD} \cong \overline{DB}\)</td>
                                <td class="proof-col-reason">3. خاصية الانعكاس للتطابق (Reflexive Property)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">4. \(\triangle ABD \cong \triangle CDB\)</td>
                                <td class="proof-col-reason">4. مسلمة التطابق بثلاثة أضلاع (SSS Postulate). وهو المطلوب.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- السؤال الثالث: برهان في المستوى الإحداثي -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثالث (هندسة إحداثية)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    إحداثيات رؤوس المثلثين هما: \(\triangle ABC\) رؤوسه \(A(1, 1), B(0, 3), C(2, 5)\)، و \(\triangle EFG\) رؤوسه \(E(1, -1), F(2, 5), G(4, 3)\).<br>
                    <strong>المطلوب:</strong> احسب أطوال أضلاع المثلثين باستعمال قانون المسافة، ثم حدد ما إذا كان \(\triangle ABC \cong \triangle EFG\) أم لا مع التوضيح.
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي بالتفصيل:</div>
                    <p><strong>1. حساب أطوال أضلاع \(\triangle ABC\):</strong><br>
                    \(AB = \sqrt{(0 - 1)^2 + (3 - 1)^2} = \sqrt{1 + 4} = \sqrt{5}\).<br>
                    \(BC = \sqrt{(2 - 0)^2 + (5 - 3)^2} = \sqrt{4 + 4} = \sqrt{8}\).<br>
                    \(AC = \sqrt{(2 - 1)^2 + (5 - 1)^2} = \sqrt{1 + 16} = \sqrt{17}\).
                    </p>
                    <p><strong>2. حساب أطوال أضلاع \(\triangle EFG\):</strong><br>
                    \(EF = \sqrt{(2 - 1)^2 + (5 - (-1))^2} = \sqrt{1 + 36} = \sqrt{37}\).<br>
                    \(FG = \sqrt{(4 - 2)^2 + (3 - 5)^2} = \sqrt{4 + 4} = \sqrt{8}\).<br>
                    \(EG = \sqrt{(4 - 1)^2 + (3 - (-1))^2} = \sqrt{9 + 16} = \sqrt{25} = 5\).
                    </p>
                    <p><strong>3. المقارنة والاستنتاج:</strong><br>
                    أطوال أضلاع \(\triangle ABC\) هي: \(\sqrt{5}, \sqrt{8}, \sqrt{17}\).<br>
                    أطوال أضلاع \(\triangle EFG\) هي: \(\sqrt{37}, \sqrt{8}, 5\).<br>
                    الأضلاع المتناظرة ليست متطابقة (\(AB \neq EF\) و \(AC \neq EG\)).<br>
                    <strong>النتيجة:</strong> \(\triangle ABC \not\cong \triangle EFG\)؛ المثلثان غير متطابقين.
                    </p>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_5():
    header = styles.make_school_header("اختبار منتصف الفصل الثالث", "مراجعة وتقويم شامل للدروس (3-1 إلى 3-4) ص 178", "5")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-mid")
    footer = styles.make_teacher_footer()
    
    raw_body = r"""
        <!-- اختبار منتصف الفصل الثالث -->
        <article class="unit-card worksheet-card" id="ws-3-mid">
            <div class="unit-title-box">
                <h3><span>5️⃣</span> ورقة عمل تقويمية: اختبار منتصف الفصل الثالث (ص 178)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 178 (الدروس 3-1 إلى 3-4)</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- أسئلة الاختبار الشامل -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">القسم الأول (الاختيار من متعدد)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>

                <p><strong>1.</strong> صنف \(\triangle ABC\) الذي رؤوسه \(A(-2, -1), B(-1, 3), C(2, 0)\) وفق أضلاعه:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> مختلف الأضلاع</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> متطابق الضلعين</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> متطابق الأضلاع</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> لا يمكن تحديده</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> قياس الزاوية الخارجية لمثلث متطابق الأضلاع يساوي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(60^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(90^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(120^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(180^\circ\)</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> إذا كان \(\triangle ABC \cong \triangle DEF\)، وكان \(m\angle A = 3x + 10\) و \(m\angle D = 5x - 20\)، فإن قيمة \(x\) تساوي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> 10</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> 15</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> 20</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> 25</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للقسم الأول:</div>
                    <p><strong>1. (B) متطابق الضلعين:</strong><br>
                    \(AB = \sqrt{(-1 - (-2))^2 + (3 - (-1))^2} = \sqrt{1 + 16} = \sqrt{17}\).<br>
                    \(BC = \sqrt{(2 - (-1))^2 + (0 - 3)^2} = \sqrt{9 + 9} = \sqrt{18}\).<br>
                    \(AC = \sqrt{(2 - (-2))^2 + (0 - (-1))^2} = \sqrt{16 + 1} = \sqrt{17}\).<br>
                    بما أن \(AB = AC = \sqrt{17}\)، فالمثلث متطابق الضلعين.
                    </p>
                    <p><strong>2. (C)</strong> \(120^\circ\)؛ لأن \(60^\circ + 60^\circ = 120^\circ\).</p>
                    <p><strong>3. (B) 15:</strong><br>
                    بما أن \(\angle A \cong \angle D \implies 5x - 20 = 3x + 10 \implies 2x = 30 \implies x = 15\).
                    </p>
                </div>
            </div>

            <!-- سؤال المقالي الحسابي والبرهان -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">القسم الثاني (سؤال مقالي وبرهان)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    في شكل هندسي، إذا كانت النقطة \(M\) هي نقطة منتصف القطعة \(\overline{JL}\)، وكانت النقطة \(M\) تقع على القطعة \(\overline{KN}\) بحيث \(KM = MN\)، والزاوية \(\angle JMN\) متقابلة بالرأس مع \(\angle LMK\).<br>
                    <strong>المطلوب:</strong> اكتب برهاناً ذا عمودين يثبت أن \(\triangle JMN \cong \triangle LMK\).
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات البرهان ذي العمودين:</div>
                    <table class="proof-table">
                        <thead>
                            <tr>
                                <th>العبارات (Statements)</th>
                                <th>التبريرات (Reasons)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="proof-col-stmt">1. \(M\) نقطة منتصف \(\overline{JL}\)</td>
                                <td class="proof-col-reason">1. معطى (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">2. \(\overline{JM} \cong \overline{LM}\)</td>
                                <td class="proof-col-reason">2. تعريف نقطة المنتصف (Def. of Midpoint)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">3. \(\angle JMN \cong \angle LMK\)</td>
                                <td class="proof-col-reason">3. الزاويتان المتقابلتان بالرأس متطابقتان (Vertical Angles)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">4. \(\overline{MN} \cong \overline{MK}\)</td>
                                <td class="proof-col-reason">4. معطى (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">5. \(\triangle JMN \cong \triangle LMK\)</td>
                                <td class="proof-col-reason">5. مسلمة SAS (ضلعان وزاوية محصورة). وهو المطلوب.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__FOOTER__', footer))

def generate_ws_6():
    header = styles.make_school_header("ورقة عمل تطبيقية: إثبات تطابق المثلثات ASA, AAS وتطابق المثلثات القائمة", "الفصل 3: الدرس 3-5 (ص 179 – 187)", "6")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-5")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws6_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-5) -->
        <article class="unit-card worksheet-card" id="ws-3-5">
            <div class="unit-title-box">
                <h3><span>6️⃣</span> ورقة عمل (3-5): إثبات تطابق المثلثات ASA, AAS وتطابق المثلثات القائمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص 179 – 187</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر الإجابة الصحيحة:</div>

                <p><strong>1.</strong> لإثبات تطابق مثلثين بمسلمة ASA، يجب أن يتطابق:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> زاويتان والضلع المحصور بينهما</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> ضلعان والزاوية المحصورة بينهما</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> ثلاثة أضلاع متناظرة</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> زاويتان وضلع غير محصور</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> تنص نظرية HL لتطابق المثلثات القائمة على تطابق:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> ساقين في كل مثلث</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> وتر وساق في مثلثين قائمين</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> وترين وزاوية حادة</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> زاويتين حادتين</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> أي من الحالات الآتية لا تثبت التطابق بين المثلثات العامة؟</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> SSS</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> AAS</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> AAA</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> SAS</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (A)</strong> زاويتان والضلع المحصور بينهما (Angle-Side-Angle).</p>
                    <p><strong>2. (B)</strong> وتر وساق (Hypotenuse-Leg) في مثلثين قائمين.</p>
                    <p><strong>3. (C)</strong> AAA (تطابق الزوايا يثبت التشابه فقط ولا يضمن التطابق مطلقاً).</p>
                </div>
            </div>

            <!-- السؤال الثاني: برهان نظرية HL -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (برهان وتطبيق المثلث القائم)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    في الشكل المقابل، \(\overline{AD}\) عمودي على \(\overline{BC}\)، و \(\overline{AB} \cong \overline{AC}\).<br>
                    <strong>المطلوب:</strong> اكتب برهاناً ذا عمودين لإثبات أن \(\triangle ABD \cong \triangle ACD\) ثم استنتج أن \(D\) هي نقطة منتصف \(\overline{BC}\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات البرهان ذي العمودين:</div>
                    <table class="proof-table">
                        <thead>
                            <tr>
                                <th>العبارات (Statements)</th>
                                <th>التبريرات (Reasons)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="proof-col-stmt">1. \(\overline{AD} \perp \overline{BC}\)</td>
                                <td class="proof-col-reason">1. معطى (Given)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">2. \(\angle ADB\) و \(\angle ADC\) زاويتان قائمتان</td>
                                <td class="proof-col-reason">2. تعريف المستقيمات المتعامدة (Def. of Perpendicular)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">3. \(\triangle ABD\) و \(\triangle ACD\) مثلثان قائما الزاوية</td>
                                <td class="proof-col-reason">3. تعريف المثلث القائم (Def. of Right Triangle)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">4. \(\overline{AB} \cong \overline{AC}\) (الوتران متطابقان)</td>
                                <td class="proof-col-reason">4. معطى (Given Hypotenuses)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">5. \(\overline{AD} \cong \overline{AD}\) (ساق مشتركة)</td>
                                <td class="proof-col-reason">5. خاصية الانعكاس للتطابق (Reflexive Leg)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">6. \(\triangle ABD \cong \triangle ACD\)</td>
                                <td class="proof-col-reason">6. نظرية الوتر وساق (HL Theorem)</td>
                            </tr>
                            <tr>
                                <td class="proof-col-stmt">7. \(\overline{BD} \cong \overline{CD} \implies D\) منتصف \(\overline{BC}\)</td>
                                <td class="proof-col-reason">7. العناصر المتناظرة في المثلثات المتطابقة متطابقة (CPCTC) وتعريف نقطة المنتصف. وهو المطلوب.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_7():
    header = styles.make_school_header("ورقة عمل تطبيقية: المثلثات المتطابقة الضلعين والأضلاع", "الفصل 3: الدرس 3-6 (ص 188 – 195)", "7")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-6")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws7_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-6) -->
        <article class="unit-card worksheet-card" id="ws-3-6">
            <div class="unit-title-box">
                <h3><span>7️⃣</span> ورقة عمل (3-6): المثلثات المتطابقة الضلعين والمتطابقة الأضلاع</h3>
                <span class="page-range-pill">كتاب الطالب: ص 188 – 195</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر رمز الإجابة الصحيحة:</div>

                <p><strong>1.</strong> في مثلث متطابق الضلعين، إذا كان قياس إحدى زاويتي القاعدة يساوي \(70^\circ\)، فإن قياس زاوية الرأس يساوي:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(40^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(55^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(70^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(110^\circ\)</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> قياس كل زاوية في أي مثلث متطابق الأضلاع يساوي دائماً:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \(45^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \(60^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \(90^\circ\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \(120^\circ\)</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> تنص نظرية المثلث المتطابق الضلعين على أنه إذا تطابق ضلعان في مثلث فإن:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> الزاويتين المقابلتين لهما متطابقتان</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> جميع زوايا المثلث متطابقة</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> محيط المثلث يساوي \(180\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> المثلث يكون قائم الزاوية</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (A)</strong> \(40^\circ\)؛ لأن الزاوية الثانية للقاعدة تساوي \(70^\circ\) أيضاً، فيكون قياس الرأس: \(180^\circ - (70^\circ + 70^\circ) = 180^\circ - 140^\circ = 40^\circ\).</p>
                    <p><strong>2. (B)</strong> \(60^\circ\) دائماً؛ لأن \(180^\circ / 3 = 60^\circ\).</p>
                    <p><strong>3. (A)</strong> الزاويتين المقابلتين لهما متطابقتان (\(\angle B \cong \angle C\)).</p>
                </div>
            </div>

            <!-- السؤال الثاني: حل المسألة الجبرية المركبة -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (تطبيق جبري وهندسي)</span>
                    <span class="q-dok-badge">DOK 3</span>
                </div>
                <div class="q-body">
                    في الشكل المقابل، \(\triangle ABC\) متطابق الضلعين فيه \(AB = AC\).<br>
                    قياس زاويتي القاعدة هما: \(m\angle B = (5x - 8)^\circ\) و \(m\angle C = (3x + 16)^\circ\).<br>
                    وقياس زاوية الرأس معطى بالعبارة الجبرية: \(m\angle A = (2y + 10)^\circ\).<br>
                    <strong>المطلوب:</strong><br>
                    1. أوجد قيمة المتغير \(x\).<br>
                    2. احسب القياس الفعلي لزاويتي القاعدة \(m\angle B\) و \(m\angle C\).<br>
                    3. احسب قياس زاوية الرأس \(m\angle A\)، ثم أوجد قيمة المتغير \(y\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات الحل النموذجي بالتفصيل:</div>
                    <p><strong>1. إيجاد قيمة \(x\):</strong><br>
                    بما أن المثلث متطابق الضلعين، فإن زاويتي القاعدة متطابقتان (\(m\angle B = m\angle C\)):<br>
                    \[5x - 8 = 3x + 16 \implies 5x - 3x = 16 + 8 \implies 2x = 24 \implies x = 12\]
                    </p>
                    <p><strong>2. حساب قياس زاويتي القاعدة:</strong><br>
                    \[m\angle B = 5(12) - 8 = 60 - 8 = 52^\circ\]
                    \[m\angle C = 3(12) + 16 = 36 + 16 = 52^\circ\]
                    (الزاويتان متطابقتان وتساوي كل منهما \(52^\circ\)).
                    </p>
                    <p><strong>3. حساب قياس زاوية الرأس وقيمة \(y\):</strong><br>
                    مجموع زوايا المثلث يساوي \(180^\circ\):<br>
                    \[m\angle A = 180^\circ - (52^\circ + 52^\circ) = 180^\circ - 104^\circ = 76^\circ\]
                    بما أن \(m\angle A = 2y + 10\):<br>
                    \[2y + 10 = 76 \implies 2y = 66 \implies y = 33\]
                    </p>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_ws_8():
    header = styles.make_school_header("ورقة عمل تطبيقية: المثلثات والبرهان الإحداثي", "الفصل 3: الدرس 3-7 (ص 196 – 200)", "8")
    meta = styles.make_student_meta_form()
    toolbar = styles.make_ws_toolbar("ws-3-7")
    footer = styles.make_teacher_footer()
    svg_ex = svg_lib.svg_ws8_exercise()
    
    raw_body = r"""
        <!-- ورقة عمل (3-7) -->
        <article class="unit-card worksheet-card" id="ws-3-7">
            <div class="unit-title-box">
                <h3><span>8️⃣</span> ورقة عمل (3-7): المثلثات والبرهان الإحداثي (Coordinate Proof)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 196 – 200</span>
            </div>

            __HEADER__
            __META__
            __TOOLBAR__

            <!-- السؤال الأول: الاختيار من متعدد -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الأول (موضوعي)</span>
                    <span class="q-dok-badge">DOK 1 - DOK 2</span>
                </div>
                <div class="q-body">اختر رمز الإجابة الصحيحة:</div>

                <p><strong>1.</strong> عند وضع مثلث في المستوى الإحداثي لكتابة برهان إحداثي، فإن أفضل وضع لنقطة الأصل \(O(0, 0)\) هو أن تكون:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> في منتصف المثلث تماماً</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> رأساً من رؤوس المثلث</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> خارج المثلث بعيداً عنه</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> في الربع الرابع سالبة</div>
                </div>

                <p style="margin-top:14px;"><strong>2.</strong> مثلث متطابق الضلعين رأسه يقع على محور \(y\) عند النقطة \((0, b)\)، وقاعدته منطبقة على محور \(x\). إذا كان أحد رأسي القاعدة عند \((a, 0)\)، فإن الرأس الآخر يقع عند:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> \((0, -b)\)</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> \((-a, 0)\)</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> \((a, b)\)</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> \((-a, -b)\)</div>
                </div>

                <p style="margin-top:14px;"><strong>3.</strong> القانون المستعمل لإثبات أن ضلعين متوازيان في البرهان الإحداثي هو قانون:</p>
                <div class="mcq-options-grid">
                    <div class="mcq-option"><span class="mcq-letter">A</span> المسافة بين نقطتين</div>
                    <div class="mcq-option"><span class="mcq-letter">B</span> نقطة المنتصف</div>
                    <div class="mcq-option"><span class="mcq-letter">C</span> الميل (\(m_1 = m_2\))</div>
                    <div class="mcq-option"><span class="mcq-letter">D</span> نظرية فيثاغورس</div>
                </div>

                <div class="answer-box">
                    <div class="answer-box-title">✅ الحل النموذجي للسؤال الأول:</div>
                    <p><strong>1. (B)</strong> رأساً من رؤوس المثلث؛ لتسهيل الحسابات وجعل إحداثيات ذلك الرأس \((0, 0)\).</p>
                    <p><strong>2. (B)</strong> \((-a, 0)\)؛ بسبب التماثل حول محور \(y\).</p>
                    <p><strong>3. (C)</strong> قانون الميل؛ لأن المستقيمين المتوازيين لهما الميل نفسه (\(m_1 = m_2\)).</p>
                </div>
            </div>

            <!-- السؤال الثاني: كتابة برهان إحداثي كامل -->
            <div class="question-card">
                <div class="question-header">
                    <span class="q-number-badge">السؤال الثاني (برهان إحداثي DOK 3)</span>
                    <span class="q-dok-badge">استدلال وبرهان إحداثي</span>
                </div>
                <div class="q-body">
                    في المستوى الإحداثي، \(\triangle OBC\) رؤوسه: \(O(0, 0)\), \(B(2a, 0)\), \(C(2b, 2c)\).<br>
                    لتكن النقطة \(M\) هي منتصف الضلع \(\overline{OC}\)، والنقطة \(N\) هي منتصف الضلع \(\overline{BC}\).<br>
                    <strong>المطلوب:</strong> اكتب برهاناً إحداثياً لإثبات أن:<br>
                    أ) القطعة المنصفة \(\overline{MN}\) توازي الضلع \(\overline{OB}\).<br>
                    ب) طول القطعة المنصفة \(MN\) يساوي نصف طول الضلع \(OB\).
                </div>
                __SVG_EX__

                <div class="answer-box">
                    <div class="answer-box-title">✅ خطوات البرهان الإحداثي الكامل:</div>
                    <p><strong>1. إيجاد إحداثيات نقطتي المنتصف \(M\) و \(N\):</strong><br>
                    بقانون نقطة المنتصف \((\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2})\):<br>
                    إحداثيات \(M\) منتصف \(OC\):<br>
                    \[M = \left( \frac{0 + 2b}{2}, \frac{0 + 2c}{2} \right) = (b, c)\]
                    إحداثيات \(N\) منتصف \(BC\):<br>
                    \[N = \left( \frac{2a + 2b}{2}, \frac{0 + 2c}{2} \right) = (a + b, c)\]
                    </p>
                    <p><strong>2. إثبات التوازي باستعمال قانون الميل:</strong><br>
                    ميل القطعة \(\overline{MN}\):<br>
                    \[m_{MN} = \frac{c - c}{(a + b) - b} = \frac{0}{a} = 0\]
                    ميل الضلع \(\overline{OB}\) الواقع على محور \(x\):<br>
                    \[m_{OB} = \frac{0 - 0}{2a - 0} = \frac{0}{2a} = 0\]
                    بما أن \(m_{MN} = m_{OB} = 0\)، فإن: \(\overline{MN} \parallel \overline{OB}\). (وهو المطلوب الأول).
                    </p>
                    <p><strong>3. إثبات العلاقة بين الأطوال بقانون المسافة:</strong><br>
                    طول \(\overline{OB}\):<br>
                    \[OB = \sqrt{(2a - 0)^2 + (0 - 0)^2} = \sqrt{4a^2} = 2a\]
                    طول \(\overline{MN}\):<br>
                    \[MN = \sqrt{((a + b) - b)^2 + (c - c)^2} = \sqrt{a^2 + 0} = a\]
                    نلاحظ أن: \(MN = a = \frac{1}{2}(2a) = \frac{1}{2} OB\).<br>
                    إذن طول القطعة المنصفة يساوي نصف طول الضلع المقابل. وهو المطلوب إثباته بالكامل.
                    </p>
                </div>
            </div>

            __FOOTER__
        </article>
    """
    return (raw_body
            .replace('__HEADER__', header)
            .replace('__META__', meta)
            .replace('__TOOLBAR__', toolbar)
            .replace('__SVG_EX__', svg_ex)
            .replace('__FOOTER__', footer))

def generate_all_worksheets():
    return (
        WORKSHEETS_SECTION_START +
        generate_ws_1() +
        generate_ws_2() +
        generate_ws_3() +
        generate_ws_4() +
        generate_ws_5() +
        generate_ws_6() +
        generate_ws_7() +
        generate_ws_8() +
        "\n    </section>\n"
    )

if __name__ == "__main__":
    worksheets = generate_all_worksheets()
    with open('section_1s_worksheets.html', 'w', encoding='utf-8') as f:
        f.write(worksheets)
    print(f"section_1s_worksheets.html written successfully ({len(worksheets):,} characters).")
