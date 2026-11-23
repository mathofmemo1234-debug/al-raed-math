# -*- coding: utf-8 -*-
"""
build_1s_summaries.py: Generates all 8 student summaries and concept organizers
for Grade 10 (1st Secondary - First Term - Paths) pages 146 to 200.
Includes:
- Crisp editable SVG geometry diagrams
- English mathematical symbols LTR inside MathJax
- Standard Western numerals (1, 2, 3...) in formulas
- Arabic pedagogical explanations RTL
- Step-by-step proof methods, theorem comparison tables, and misconception alerts.
"""
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

import svg_geometry_library as svg_lib

SUMMARIES_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة ومطويات المفاهيم للطلاب (8 ملخصات متتالية)  -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة ومطويات المفاهيم للطلاب (8 ملخصات متتالية)</h2>
            <span class="section-badge">مفاهيم وقوانين وبراهين هندسية محررة بدقة بالغة</span>
        </div>
"""

def generate_summary_1():
    svg_angles = svg_lib.svg_classify_by_angles()
    svg_sides = svg_lib.svg_classify_by_sides()
    svg_alg = svg_lib.svg_algebra_sides_exercise()
    body = r"""
        <!-- ملخص الدرس (3-1) -->
        <article class="unit-card" id="summary-3-1">
            <div class="unit-title-box">
                <h3><span>1️⃣</span> ملخص الدرس (3-1): تصنيف المثلثات (Classifying Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 146 – 152</span>
            </div>

            <!-- بطاقة المفاهيم الأساسية -->
            <div class="concept-grid">
                <div class="concept-card">
                    <h4>📐 أولاً: التصنيف وفقاً للزوايا</h4>
                    <ul>
                        <li><strong>مثلث حاد الزوايا (Acute):</strong> جميع زواياه حادة (قياس كل منها \(< 90^\circ\)).</li>
                        <li><strong>مثلث متطابق الزوايا (Equiangular):</strong> جميع زواياه متطابقة وقياس كل منها \(60^\circ\).</li>
                        <li><strong>مثلث منفرج الزاوية (Obtuse):</strong> يحوي زاوية واحدة منفرجة (\(> 90^\circ\)).</li>
                        <li><strong>مثلث قائم الزاوية (Right):</strong> يحوي زاوية واحدة قائمة (\(= 90^\circ\)).</li>
                    </ul>
                </div>
                <div class="concept-card">
                    <h4>📏 ثانياً: التصنيف وفقاً للأضلاع</h4>
                    <ul>
                        <li><strong>مثلث متطابق الأضلاع (Equilateral):</strong> أضلاعه الثلاثة متطابقة تماماً.</li>
                        <li><strong>مثلث متطابق الضلعين (Isosceles):</strong> يحوي ضلعين متطابقين على الأقل.</li>
                        <li><strong>مثلث مختلف الأضلاع (Scalene):</strong> لا يوجد فيه أي ضلعين متطابقين.</li>
                    </ul>
                </div>
            </div>

            <!-- الأشكال الهندسية المحررة -->
            __SVG_ANGLES__
            __SVG_SIDES__

            <!-- الربط الجبري وحساب الأطوال -->
            <div class="plan-step-box">
                <div class="plan-step-title">🧮 استراتيجية حل مسائل الجبر في المثلثات المتطابقة الضلعين والأضلاع</div>
                <p>عندما يطلب إيجاد قيمة متغير أو أطوال أضلاع مثلث متطابق الضلعين أو متطابق الأضلاع، نتبع الخطوات الآتية:</p>
                <ol style="margin-right: 20px; line-height: 2;">
                    <li><strong>تحديد العلاقة الهندسية:</strong> نحدد الضلعين المتطابقين بناءً على المعطيات أو علامات التطابق (Tick marks)، مثلاً: \(AB = AC\).</li>
                    <li><strong>بناء المعادلة الجبرية:</strong> نعوض بالقيم المعطاة: \(5x - 0.5 = 4x + 1\).</li>
                    <li><strong>حل المعادلة:</strong> بطرح \(4x\) وإضافة \(0.5\) للطرفين: \(x = 1.5\).</li>
                    <li><strong>حساب الأطوال الفعلية:</strong> نعوض بقيمة \(x\) في كل عبارة جبرية لحساب أطوال الأضلاع والتأكد من تطابقها: \(AB = 5(1.5) - 0.5 = 7\)، \(AC = 4(1.5) + 1 = 7\).</li>
                </ol>
            </div>
            __SVG_ALG__

            <!-- تنبيه الأخطاء الشائعة -->
            <div class="mistake-alert">
                <strong>⚠️ انتبه للأخطاء الشائعة:</strong>
                المثلث المتطابق الأضلاع هو أيضاً مثلث متطابق الضلعين (لأنه يحقق شرط وجود ضلعين متطابقين على الأقل)، ولكن العكس غير صحيح؛ فالمثلث المتطابق الضلعين ليس بالضرورة متطابق الأضلاع. كذلك لا يمكن لأي مثلث أن يحوي أكثر من زاوية قائمة واحدة أو أكثر من زاوية منفرجة واحدة.
            </div>
        </article>
    """
    return body.replace('__SVG_ANGLES__', svg_angles).replace('__SVG_SIDES__', svg_sides).replace('__SVG_ALG__', svg_alg)

def generate_summary_2():
    svg_sum = svg_lib.svg_triangle_angle_sum()
    svg_ext = svg_lib.svg_exterior_angle()
    body = r"""
        <!-- ملخص الدرس (3-2) -->
        <article class="unit-card" id="summary-3-2">
            <div class="unit-title-box">
                <h3><span>2️⃣</span> ملخص الدرس (3-2): زوايا المثلثات (Angles of Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 153 – 161</span>
            </div>

            <!-- جدول النظريات والنتائج -->
            <table class="data-table">
                <thead>
                    <tr>
                        <th>النظرية / النتيجة</th>
                        <th>التعبير اللفظي</th>
                        <th>الصيغة والرموز الرياضية (LTR)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>نظرية مجموع قياسات زوايا المثلث</strong><br>(Triangle Angle-Sum Theorem)</td>
                        <td>مجموع قياسات الزوايا الداخلية لأي مثلث يساوي دائماً \(180^\circ\).</td>
                        <td>\[m\angle A + m\angle B + m\angle C = 180^\circ\]</td>
                    </tr>
                    <tr>
                        <td><strong>نظرية الزاوية الخارجية للمثلث</strong><br>(Exterior Angle Theorem)</td>
                        <td>قياس الزاوية الخارجية لمثلث يساوي مجموع قياسي الزاويتين الداخليتين البعيدتين عنها.</td>
                        <td>\[m\angle 4 = m\angle 1 + m\angle 2\]</td>
                    </tr>
                    <tr>
                        <td><strong>النتيجة 3.1: الزاويتان الحادتان في مثلث قائم</strong></td>
                        <td>الزاويتان الحادتان في أي مثلث قائم الزاوية تكونان متتامتين دائماً.</td>
                        <td>\[m\angle A + m\angle B = 90^\circ\]</td>
                    </tr>
                    <tr>
                        <td><strong>النتيجة 3.2: استقامة الزوايا</strong></td>
                        <td>لا يمكن لمثلث أن يحوي أكثر من زاوية قائمة واحدة، أو أكثر من زاوية منفرجة واحدة.</td>
                        <td>\[m\angle \ge 90^\circ \text{ لزاوية واحدة فقط على الأكثر}\]</td>
                    </tr>
                </tbody>
            </table>

            <!-- الأشكال الهندسية المحررة -->
            __SVG_SUM__
            __SVG_EXT__

            <!-- خطوات حل مسائل الزوايا المركبة -->
            <div class="plan-step-box">
                <div class="plan-step-title">💡 الدليل الإرشادي لحساب الزوايا في الأشكال المركبة (مثل ص 158 و 159)</div>
                <ul style="margin-right: 20px; line-height: 2;">
                    <li><strong>البحث عن مثلث يحوي معلومين:</strong> إذا كان المثلث يحوي زاويتين معلومتين، ابدأ به فوراً باستخدام: \(m\angle 3 = 180^\circ - (m\angle 1 + m\angle 2)\).</li>
                    <li><strong>استثمار التقابل بالرأس والتحالف والتناظر:</strong> الزوايا المتقابلة بالرأس متطابقة وتنقلك من مثلث إلى مثلث مجاور.</li>
                    <li><strong>استخدام الزاوية المستقيمة:</strong> الزاويتان المتجاورتان على خط مستقيم مجموعهما \(180^\circ\).</li>
                    <li><strong>توظيف الزاوية الخارجية مباشرة:</strong> توفر عليك خطوتين لحساب الزاوية دون الحاجة لحساب الزاوية المجاورة لها أولاً.</li>
                </ul>
            </div>

            <div class="mistake-alert">
                <strong>⚠️ خطأ شائع يجب الحذر منه:</strong>
                الزاوية الخارجية لا تساوي أي زاوية مجاورة لها، بل تساوي مجموع الزاويتين <em>البعيدتين عنها</em>. الزاوية المجاورة لها تشكل معها زوجاً خطياً متكاملاً مجموعه \(180^\circ\).
            </div>
        </article>
    """
    return body.replace('__SVG_SUM__', svg_sum).replace('__SVG_EXT__', svg_ext)

def generate_summary_3():
    svg_cpctc = svg_lib.svg_congruent_triangles_cpctc()
    body = r"""
        <!-- ملخص الدرس (3-3) -->
        <article class="unit-card" id="summary-3-3">
            <div class="unit-title-box">
                <h3><span>3️⃣</span> ملخص الدرس (3-3): المثلثات المتطابقة (Congruent Triangles)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 162 – 169</span>
            </div>

            <div class="concept-grid">
                <div class="concept-card">
                    <h4>🔗 تعريف المضلعات المتطابقة (CPCTC)</h4>
                    <p>يتطابق مضلعان إذا وفقط إذا كانت أجزاؤهما المتناظرة متطابقة. ويعبر عن ذلك اختصاراً بالإنجليزية بـ <strong>CPCTC</strong>:</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold; color:#1e3a8a;">Corresponding Parts of Congruent Triangles are Congruent</p>
                    <p>يتضمن ذلك 6 عناصر: 3 أزواج من الأضلاع المتناظرة المتطابقة + 3 أزواج من الزوايا المتناظرة المتطابقة.</p>
                </div>
                <div class="concept-card">
                    <h4>📐 نظرية الزاوية الثالثة (Third Angles Theorem)</h4>
                    <p>إذا تطابقت زاويتان في مثلث مع زاويتين مناظرتين في مثلث آخر، فإن الزاوية الثالثة في المثلث الأول تطابق حتماً الزاوية الثالثة في المثلث الثاني:</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold;">If \(\angle A \cong \angle D\) and \(\angle B \cong \angle E\), then \(\angle C \cong \angle F\).</p>
                </div>
            </div>

            __SVG_CPCTC__

            <!-- جدول خصائص تطابق المثلثات -->
            <table class="data-table">
                <thead>
                    <tr>
                        <th>الخاصية</th>
                        <th>الصيغة الرمزية (LTR)</th>
                        <th>الشرح اللفظي</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>الانعكاس (Reflexive)</strong></td>
                        <td>\[\triangle ABC \cong \triangle ABC\]</td>
                        <td>أي مثلث يطابق نفسه دائماً.</td>
                    </tr>
                    <tr>
                        <td><strong>التماثل (Symmetric)</strong></td>
                        <td>\[\triangle ABC \cong \triangle DEF \implies \triangle DEF \cong \triangle ABC\]</td>
                        <td>إذا طابق مثلث أول مثلثاً ثانياً، فإن الثاني يطابق الأول.</td>
                    </tr>
                    <tr>
                        <td><strong>التعدي (Transitive)</strong></td>
                        <td>\[\triangle ABC \cong \triangle DEF \text{ and } \triangle DEF \cong \triangle JKL \implies \triangle ABC \cong \triangle JKL\]</td>
                        <td>إذا طابق مثلث مثلثين آخرين، فإن المثلثين الآخرين متطابقان.</td>
                    </tr>
                </tbody>
            </table>

            <div class="mistake-alert">
                <strong>⚠️ انتبه لترتيب الرؤوس في عبارة التطابق:</strong>
                كتابة \(\triangle ABC \cong \triangle DEF\) تعني أن \(A \leftrightarrow D\)، \(B \leftrightarrow E\)، \(C \leftrightarrow F\). إذا غيّر الطالب ترتيب حرف واحد فقط مثل كتابة \(\triangle ABC \cong \triangle EDF\) فإن العبارة تصبح خاطئة رياضياً.
            </div>
        </article>
    """
    return body.replace('__SVG_CPCTC__', svg_cpctc)

def generate_summary_4():
    svg_sss_sas = svg_lib.svg_sss_and_sas()
    body = r"""
        <!-- ملخص الدرس (3-4) -->
        <article class="unit-card" id="summary-3-4">
            <div class="unit-title-box">
                <h3><span>4️⃣</span> ملخص الدرس (3-4): إثبات تطابق المثلثات SSS, SAS</h3>
                <span class="page-range-pill">كتاب الطالب: ص 170 – 177</span>
            </div>

            <div class="concept-grid">
                <div class="concept-card">
                    <h4>🔺 مسلمة التطابق بثلاثة أضلاع (SSS)</h4>
                    <p><strong>Side-Side-Side:</strong> إذا تطابقت أضلاع مثلث مع الأضلاع المناظرة لها في مثلث آخر، فإن المثلثين متطابقان.</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold; color:#2563eb;">\(AB \cong DE, BC \cong EF, AC \cong DF \implies \triangle ABC \cong \triangle DEF\)</p>
                </div>
                <div class="concept-card">
                    <h4>📐 مسلمة التطابق بضلعين والزاوية المحصورة (SAS)</h4>
                    <p><strong>Side-Angle-Side:</strong> إذا تطابق ضلعان والزاوية المحصورة بينهما في مثلث مع نظائرها في مثلث آخر، فإن المثلثين متطابقان.</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold; color:#0d9488;">\(AB \cong DE, \angle B \cong \angle E, BC \cong EF \implies \triangle ABC \cong \triangle DEF\)</p>
                </div>
            </div>

            __SVG_SSS_SAS__

            <!-- استراتيجية البرهان في المستوى الإحداثي -->
            <div class="plan-step-box">
                <div class="plan-step-title">📍 خطوات إثبات تطابق مثلثين في المستوى الإحداثي باستعمال مسلمة SSS</div>
                <ol style="margin-right: 20px; line-height: 2;">
                    <li><strong>حساب أطوال أضلاع المثلث الأول الثلاثة:</strong> باستعمال قانون المسافة بين نقطتين:
                    \[d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]
                    </li>
                    <li><strong>حساب أطوال أضلاع المثلث الثاني الثلاثة:</strong> بنفس القانون لكل ضلع مناظر.</li>
                    <li><strong>المقارنة الدقيقة:</strong> إذا تساوت الأطوال الثلاثة المتناظرة، فإن الأضلاع متطابقة (\(\cong\)).</li>
                    <li><strong>النتيجة النهائية:</strong> يتطابق المثلثان وفق مسلمة SSS.</li>
                </ol>
            </div>

            <div class="mistake-alert">
                <strong>⚠️ ما هي الزاوية المحصورة؟</strong>
                الزاوية المحصورة بين الضلعين \(AB\) و \(BC\) هي الزاوية التي يشترك فيها الضلعان وهي \(\angle B\). إذا كانت الزاوية المعطاة غير محصورة (مثل \(\angle A\) أو \(\angle C\))، فإننا نكون أمام حالة SSA (ضلعان وزاوية غير محصورة) وهي <em>ليست حالة تطابق</em> ولا تثبت تطابق المثلثات أبداً!
            </div>
        </article>
    """
    return body.replace('__SVG_SSS_SAS__', svg_sss_sas)

def generate_summary_5():
    return r"""
        <!-- ملخص مراجعة منتصف الفصل الثالث -->
        <article class="unit-card" id="summary-3-mid">
            <div class="unit-title-box">
                <h3><span>5️⃣</span> ملخص مراجعة منتصف الفصل الثالث (ص 178)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 178 (مراجعة الدروس 3-1 إلى 3-4)</span>
            </div>

            <!-- خريطة المفاهيم الموحدة -->
            <div class="plan-step-box">
                <div class="plan-step-title">🗺️ خريطة المفاهيم الشاملة للنصف الأول من الفصل الثالث</div>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الدرس</th>
                            <th>المفاهيم والنظريات الأساسية</th>
                            <th>القوانين والصيغ المعتمدة (LTR)</th>
                            <th>مفتاح الحل الذكي</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>3-1: تصنيف المثلثات</strong></td>
                            <td>تصنيف الزوايا (حاد، قائم، منفرج، متطابق الزوايا) وتصنيف الأضلاع (متطابق الأضلاع، متطابق الضلعين، مختلف الأضلاع).</td>
                            <td>معادلات التساوي: \(d_1 = d_2\) لحساب المتغيرات.</td>
                            <td>ابحث عن علامات التطابق، أو الزوايا القائمة والمنفرجة.</td>
                        </tr>
                        <tr>
                            <td><strong>3-2: زوايا المثلثات</strong></td>
                            <td>مجموع زوايا المثلث \(180^\circ\)، نظرية الزاوية الخارجية، وتتام الزاويتين الحادتين في القائم.</td>
                            <td>\[m\angle A + m\angle B + m\angle C = 180^\circ\]
                            \[m\angle ext = m\angle 1 + m\angle 2\]</td>
                            <td>الزاوية الخارجية = مجموع البعيدتين فوراً دون حساب المجاورة.</td>
                        </tr>
                        <tr>
                            <td><strong>3-3: المثلثات المتطابقة</strong></td>
                            <td>تطابق المضلعات CPCTC، ترتيب الرؤوس، نظرية الزاوية الثالثة، وخصائص التطابق.</td>
                            <td>\[\triangle ABC \cong \triangle DEF \implies 6 \text{ pairs congruent}\]</td>
                            <td>الترتيب هو الأساس؛ الحرف الأول يقابل الأول دائماً.</td>
                        </tr>
                        <tr>
                            <td><strong>3-4: إثبات التطابق SSS, SAS</strong></td>
                            <td>تطابق ثلاثة أضلاع SSS، وتطابق ضلعين وزاوية محصورة SAS، والمسافة في المستوى الإحداثي.</td>
                            <td>\[d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\]</td>
                            <td>تأكد أن الزاوية محصورة بين الضلعين؛ الضلع المشترك يطابق نفسه بالانعكاس.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- جدول المصطلحات الإنجليزية الأساسية للمرحلة الثانوية -->
            <div class="plan-step-box stem">
                <div class="plan-step-title">🔤 مسرد المصطلحات الرياضية والرموز الإنجليزية المعتمدة (Glossary)</div>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>المصطلح بالعربية</th>
                            <th>المصطلح بالإنجليزية</th>
                            <th>الرمز المعتمد</th>
                            <th>الاستعمال الرياضي</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>مثلث متطابق الأضلاع</td><td>Equilateral Triangle</td><td>Equilateral</td><td>جميع الأضلاع الثلاثة متطابقة</td></tr>
                        <tr><td>مثلث متطابق الضلعين</td><td>Isosceles Triangle</td><td>Isosceles</td><td>ضلعان متطابقان على الأقل</td></tr>
                        <tr><td>مثلث مختلف الأضلاع</td><td>Scalene Triangle</td><td>Scalene</td><td>لا توجد أضلاع متطابقة</td></tr>
                        <tr><td>رمز التطابق</td><td>Congruence Symbol</td><td>\(\cong\)</td><td>\(\triangle ABC \cong \triangle DEF\)</td></tr>
                        <tr><td>الأجزاء المتناظرة متطابقة</td><td>Corresponding Parts</td><td>CPCTC</td><td>استنتاج تطابق باقي العناصر بعد البرهان</td></tr>
                        <tr><td>ضلع - ضلع - ضلع</td><td>Side-Side-Side</td><td>SSS</td><td>مسلمة التطابق بثلاثة أضلاع</td></tr>
                        <tr><td>ضلع - زاوية محصورة - ضلع</td><td>Side-Angle-Side</td><td>SAS</td><td>مسلمة التطابق بضلعين وزاوية محصورة</td></tr>
                    </tbody>
                </table>
            </div>
        </article>
    """

def generate_summary_6():
    svg_asa_aas = svg_lib.svg_asa_and_aas()
    svg_hl = svg_lib.svg_hl_right_triangles()
    body = r"""
        <!-- ملخص الدرس (3-5) -->
        <article class="unit-card" id="summary-3-5">
            <div class="unit-title-box">
                <h3><span>6️⃣</span> ملخص الدرس (3-5): إثبات تطابق المثلثات ASA, AAS ومعمل تطابق المثلثات القائمة</h3>
                <span class="page-range-pill">كتاب الطالب: ص 179 – 187</span>
            </div>

            <!-- مقارنة ASA و AAS -->
            <div class="concept-grid">
                <div class="concept-card">
                    <h4>📐 مسلمة التطابق بزاويتين وضلع محصور (ASA)</h4>
                    <p><strong>Angle-Side-Angle:</strong> إذا تطابقت زاويتان والضلع المحصور بينهما في مثلث مع نظائرها في مثلث آخر، فإن المثلثين متطابقان.</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold; color:#2563eb;">\(\angle A \cong \angle D, AB \cong DE, \angle B \cong \angle E \implies \triangle ABC \cong \triangle DEF\)</p>
                </div>
                <div class="concept-card">
                    <h4>📐 نظرية التطابق بزاويتين وضلع غير محصور (AAS)</h4>
                    <p><strong>Angle-Angle-Side:</strong> إذا تطابقت زاويتان وضلع غير محصور في مثلث مع نظائرها في مثلث آخر، فإن المثلثين متطابقان.</p>
                    <p style="direction:ltr; text-align:center; font-weight:bold; color:#0d9488;">\(\angle A \cong \angle D, \angle B \cong \angle E, BC \cong EF \implies \triangle ABC \cong \triangle DEF\)</p>
                </div>
            </div>

            __SVG_ASA_AAS__

            <!-- معمل الهندسة: تطابق المثلثات القائمة وحالات HL, LL, HA, LA -->
            <div class="plan-step-box">
                <div class="plan-step-title">⭐ حالات خاصة لتطابق المثلثات القائمة (ص 186 – 187)</div>
                <p>في المثلث القائم الزاوية، الزاوية القائمة (\(90^\circ\)) معلومة دائماً، لذا تكفي معلومتان إضافيتان فقط لإثبات التطابق:</p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الحالة والرمز</th>
                            <th>الاسم الكامل</th>
                            <th>الشروط المطلوبة</th>
                            <th>الأصل من حالات المثلثات العامة</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>HL</strong></td>
                            <td>وتر وساق (Hypotenuse-Leg)</td>
                            <td>تطابق الوتر وأحد الساقين في مثلثين قائمين.</td>
                            <td>حالة خاصة بالمثلث القائم مشتقة من نظرية فيثاغورس.</td>
                        </tr>
                        <tr>
                            <td><strong>LL</strong></td>
                            <td>ساق وساق (Leg-Leg)</td>
                            <td>تطابق ساقي القائمة في المثلثين.</td>
                            <td>تكافئ مسلمة SAS (الزاوية القائمة محصورة بين الساقين).</td>
                        </tr>
                        <tr>
                            <td><strong>HA</strong></td>
                            <td>وتر وزاوية حادة (Hypotenuse-Angle)</td>
                            <td>تطابق الوتر وإحدى الزاويتين الحادتين.</td>
                            <td>تكافئ نظرية AAS.</td>
                        </tr>
                        <tr>
                            <td><strong>LA</strong></td>
                            <td>ساق وزاوية حادة (Leg-Angle)</td>
                            <td>تطابق أحد الساقين وإحدى الزاويتين الحادتين.</td>
                            <td>تكافئ مسلمة ASA أو نظرية AAS (حسب موقع الساق).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            __SVG_HL__

            <!-- الجدول الماستر لحالات التطابق الخمس -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏆 الدليل الشامل لمعايير تطابق المثلثات الخمسة المعتمدة</div>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الحالة</th>
                            <th>العناصر المتطابقة</th>
                            <th>الموقع الهندسي</th>
                            <th>هل تطبق على أي مثلث؟</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>SSS</strong></td><td>3 أضلاع</td><td>جميع الأضلاع المتناظرة</td><td>نعم، لجميع المثلثات</td></tr>
                        <tr><td><strong>SAS</strong></td><td>ضلعان وزاوية</td><td>الزاوية محصورة بين الضلعين تماماً</td><td>نعم، لجميع المثلثات</td></tr>
                        <tr><td><strong>ASA</strong></td><td>زاويتان وضلع</td><td>الضلع محصور بين الزاويتين تماماً</td><td>نعم، لجميع المثلثات</td></tr>
                        <tr><td><strong>AAS</strong></td><td>زاويتان وضلع</td><td>الضلع غير محصور (يقابل إحدى الزاويتين)</td><td>نعم، لجميع المثلثات</td></tr>
                        <tr><td><strong>HL</strong></td><td>وتر وساق</td><td>الوتر وساق في مثلث قائم الزاوية</td><td>خاصة بالمثلثات القائمة فقط</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="mistake-alert">
                <strong>⚠️ انتبه: حالتان لا تكفيان لإثبات التطابق أبداً!</strong><br>
                1. <strong>AAA (ثلاث زوايا):</strong> تثبت التشابه فقط ولا تثبت التطابق أبداً (يمكن رسم مثلثين زواياهما متطابقة وأحدهما صغير والآخر عملاق).<br>
                2. <strong>SSA (ضلعان وزاوية غير محصورة):</strong> لا تثبت التطابق في المثلثات العامة (حالة غموض Ambiguous Case قد تعطي مثلثين مختلفين)، ما لم تكن الزاوية قائمة وتكون الحالة HL.
            </div>
        </article>
    """
    return body.replace('__SVG_ASA_AAS__', svg_asa_aas).replace('__SVG_HL__', svg_hl)

def generate_summary_7():
    svg_iso = svg_lib.svg_isosceles_anatomy()
    body = r"""
        <!-- ملخص الدرس (3-6) -->
        <article class="unit-card" id="summary-3-6">
            <div class="unit-title-box">
                <h3><span>7️⃣</span> ملخص الدرس (3-6): المثلثات المتطابقة الضلعين والمتطابقة الأضلاع</h3>
                <span class="page-range-pill">كتاب الطالب: ص 188 – 195</span>
            </div>

            <!-- تشريح المثلث المتطابق الضلعين -->
            __SVG_ISO__

            <table class="data-table">
                <thead>
                    <tr>
                        <th>النظرية / النتيجة</th>
                        <th>النص والرموز (LTR)</th>
                        <th>الأهمية التطبيقية في حل المسائل</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>نظرية المثلث المتطابق الضلعين</strong><br>(Isosceles Triangle Theorem)</td>
                        <td>إذا تطابق ضلعان في مثلث فإن الزاويتين المقابلتين لهما متطابقتان:
                        \[AB \cong AC \implies \angle B \cong \angle C\]</td>
                        <td>تسمح بمساواة زاويتي القاعدة وحساب قياسهما جبرياً.</td>
                    </tr>
                    <tr>
                        <td><strong>عكس نظرية المثلث المتطابق الضلعين</strong><br>(Converse of Isosceles Thm)</td>
                        <td>إذا تطابقت زاويتان في مثلث فإن الضلعين المقابلين لهما متطابقان:
                        \[\angle B \cong \angle C \implies AB \cong AC\]</td>
                        <td>تسمح بإثبات تطابق الساقين بمعلومية تطابق زاويتي القاعدة.</td>
                    </tr>
                    <tr>
                        <td><strong>نتيجة المثلث المتطابق الأضلاع</strong><br>(Equilateral Corollary)</td>
                        <td>يكون المثلث متطابق الأضلاع إذا وفقط إذا كان متطابق الزوايا:
                        \[AB \cong BC \cong AC \iff \angle A \cong \angle B \cong \angle C\]</td>
                        <td>التطابق في الأضلاع يستلزم التطابق في الزوايا والعكس صحيح.</td>
                    </tr>
                    <tr>
                        <td><strong>قياس زوايا المتطابق الأضلاع</strong></td>
                        <td>قياس كل زاوية في أي مثلث متطابق الأضلاع يساوي دائماً:
                        \[m\angle = \frac{180^\circ}{3} = 60^\circ\]</td>
                        <td>ثابت هندسي حاسم: لا توجد زاوية في مثلث متطابق الأضلاع غير \(60^\circ\).</td>
                    </tr>
                </tbody>
            </table>

            <!-- قواعد حل معادلات المثلثات المتطابقة الضلعين -->
            <div class="plan-step-box">
                <div class="plan-step-title">🧮 معادلات زوايا المثلث المتطابق الضلعين</div>
                <p>إذا كانت زاوية الرأس هي \(\angle A\)، وزاويتا القاعدة هما \(\angle B, \angle C\):</p>
                <ul>
                    <li>حساب زاويتي القاعدة بمعلومية زاوية الرأس:
                    \[m\angle B = m\angle C = \frac{180^\circ - m\angle A}{2}\]
                    </li>
                    <li>حساب زاوية الرأس بمعلومية إحدى زاويتي القاعدة:
                    \[m\angle A = 180^\circ - 2(m\angle B)\]
                    </li>
                </ul>
            </div>

            <div class="mistake-alert">
                <strong>⚠️ خطأ شائع:</strong>
                الخلط بين زاوية الرأس وزاويتي القاعدة. زاوية الرأس تقع دائماً بين الساقين المتطابقين، بينما زاويتا القاعدة تقعان عند طرفي القاعدة ومقابلتين للساقين المتطابقين.
            </div>
        </article>
    """
    return body.replace('__SVG_ISO__', svg_iso)

def generate_summary_8():
    svg_coord = svg_lib.svg_coordinate_proof_placement()
    body = r"""
        <!-- ملخص الدرس (3-7) -->
        <article class="unit-card" id="summary-3-7">
            <div class="unit-title-box">
                <h3><span>8️⃣</span> ملخص الدرس (3-7): المثلثات والبرهان الإحداثي (Coordinate Proof)</h3>
                <span class="page-range-pill">كتاب الطالب: ص 196 – 200</span>
            </div>

            <!-- بطاقة مفهوم البرهان الإحداثي -->
            <div class="concept-grid">
                <div class="concept-card">
                    <h4>📍 ما هو البرهان الإحداثي؟</h4>
                    <p>هو برهان يوظف رسم الأشكال الهندسية في المستوى الإحداثي واستعمال الجبر وقوانينه لإثبات صحة المبرهنات والعلاقات الهندسية العامة دون التقيد بأرقام خاصة.</p>
                </div>
                <div class="concept-card">
                    <h4>📐 القواعد الأربع للوضع الذكي للمثلث</h4>
                    <ol style="margin-right: 15px; font-size: 13px;">
                        <li>اجعل نقطة الأصل \(O(0, 0)\) رأساً للمثلث.</li>
                        <li>اجعل ضلعاً منطبقاً على أحد المحورين (عادة محور \(x\)).</li>
                        <li>اجعل الشكل في الربع الأول قدر الإمكان لتكون الإحداثيات موجبة.</li>
                        <li>استعمل مضاعفات المتغيرات (\(2a, 2b\)) لتجنب الكسور عند حساب نقاط المنتصف.</li>
                    </ol>
                </div>
            </div>

            __SVG_COORD__

            <!-- القوانين الجبرية الثلاثة المعتمدة في البرهان الإحداثي -->
            <table class="data-table">
                <thead>
                    <tr>
                        <th>القانون الهندسي</th>
                        <th>الصيغة الجبرية الرمزية (LTR)</th>
                        <th>الغرض واستخدامه في البرهان</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>صيغة المسافة بين نقطتين</strong><br>(Distance Formula)</td>
                        <td>\[d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\]</td>
                        <td>لإثبات تطابق الأضلاع والقطع المستقيمة (\(\overline{AB} \cong \overline{CD}\)).</td>
                    </tr>
                    <tr>
                        <td><strong>صيغة نقطة المنتصف</strong><br>(Midpoint Formula)</td>
                        <td>\[M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)\]</td>
                        <td>لإيجاد إحداثيات نقاط المنتصف وإثبات تنصيف القطع المستقيمة.</td>
                    </tr>
                    <tr>
                        <td><strong>صيغة الميل</strong><br>(Slope Formula)</td>
                        <td>\[m = \frac{y_2 - y_1}{x_2 - x_1}\]</td>
                        <td>لإثبات التوازي (\(m_1 = m_2\)) أو التعامد (\(m_1 \cdot m_2 = -1\)).</td>
                    </tr>
                </tbody>
            </table>

            <!-- أمثلة التسمية الرمزية للرؤوس المجهولة -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏷️ تسمية الرؤوس المجهولة في أشكال خاصة:</div>
                <ul style="margin-right: 20px; line-height: 2;">
                    <li><strong>مثلث قائم الزاوية متطابق الضلعين:</strong> الرؤوس هي \((0, 0)\)، \((a, 0)\)، \((0, a)\).</li>
                    <li><strong>مثلث متطابق الضلعين قاعدته على محور \(x\) ونقطة منتصفها الأصل:</strong> الرؤوس هي \((-a, 0)\)، \((a, 0)\)، \((0, b)\).</li>
                    <li><strong>مثلث متطابق الضلعين رأسه على محور \(y\):</strong> الرؤوس هي \((0, 0)\)، \((2a, 0)\)، \((a, b)\).</li>
                </ul>
            </div>

            <div class="mistake-alert">
                <strong>⚠️ تجنب الأخطاء القاتلة في البرهان الإحداثي:</strong>
                لا تستخدم أرقاماً عددية محددة (مثل \(2, 5, 8\)) في البرهان الإحداثي، لأن البرهان العددي يثبت الحالة لمثلث واحد فقط ولا يعتبر برهاناً عاماً! البرهان الصحيح يجب أن يستخدم متغيرات جبرية عامة مثل \(a, b, c\).
            </div>
        </article>
    """
    return body.replace('__SVG_COORD__', svg_coord)

def generate_all_summaries():
    return (
        SUMMARIES_SECTION_START +
        generate_summary_1() +
        generate_summary_2() +
        generate_summary_3() +
        generate_summary_4() +
        generate_summary_5() +
        generate_summary_6() +
        generate_summary_7() +
        generate_summary_8() +
        "\n    </section>\n"
    )

if __name__ == "__main__":
    summaries = generate_all_summaries()
    with open('section_1s_summaries.html', 'w', encoding='utf-8') as f:
        f.write(summaries)
    print(f"section_1s_summaries.html written successfully ({len(summaries):,} characters).")
