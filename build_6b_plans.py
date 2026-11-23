# -*- coding: utf-8 -*-
"""
build_6b_plans.py: Generates all 5 STEM lesson plans for Grade 6 Elementary (6ب) pages 135 to 151.
Adheres strictly to Prompt 1 criteria with all 7 pedagogical components and Eastern Arabic numerals.
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLANS_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الأول: خطط التحضير الدراسي وفق نموذج STEM المطور (٥ خطط متتالية)      -->
    <!-- ========================================================================= -->
    <section class="mega-section" id="section-plans">
        <div class="section-banner">
            <h2>📘 المحور الأول: خطط التحضير والتدريس وفق معايير STEM ورؤية ٢٠٣٠</h2>
            <p>تحضير تربوي شامل ومتسلسل لدروس واختبارات الصف السادس الابتدائي (ص ١٣٥ - ١٥١) - ٥ خطط درسية متتالية ومفصلة بالكامل</p>
        </div>
"""

PLAN_1 = r"""
        <!-- الخطة الأولى: اختبار الفصل ٣ والاختبار التراكمي ٣ -->
        <article class="unit-card" id="plan-1-ch3-test">
            <div class="unit-header">
                <div class="unit-badge">الخطة الدراسية الأولى (ص ١٣٥ – ١٣٧)</div>
                <h3 class="unit-title">خطة مراجعة وتقويم: اختبار الفصل الثالث والاختبار التراكمي (العمليات على الكسور العشرية)</h3>
                <div class="unit-meta">
                    <span><strong>الصف:</strong> السادس الابتدائي</span> |
                    <span><strong>المادة:</strong> الرياضيات</span> |
                    <span><strong>المجال:</strong> الأعداد والعمليات عليها</span> |
                    <span><strong>الفصل ٣:</strong> العمليات على الكسور العشرية</span>
                </div>
            </div>

            <!-- 1. الأهداف والمعايير والمجال -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">١</span> نواتج التعلم والمعايير المستهدفة (الأهداف السلوكية SMART)</h4>
                <div class="pedagogy-box">
                    <p>تم صياغة الأهداف وفق المعايير الوطنية لتعليم الرياضيات ٢٠٢٦ ومؤشرات قياس الأداء:</p>
                    <ul class="smart-goals-list">
                        <li><strong>هدف معرفي:</strong> أن يسترجع الطالب القواعد الحسابية للعمليات الأربع (الجمع، الطرح، الضرب، القسمة) على الكسور العشرية مع تحديد موضع الفاصلة العشرية بدقة بنسبة إتقان لا تقل عن ٩٠٪.</li>
                        <li><strong>هدف مهاري:</strong> أن يحل الطالب مسائل رياضية وتطبيقية متنوعة تتضمن العمليات على الكسور العشرية وتقدير نواتجها باستخدام استراتيجيات الحساب الذهني بنجاح تام.</li>
                        <li><strong>هدف وجداني وقيمي:</strong> أن يثمن الطالب أهمية الدقة الرياضية في المعاملات المالية والحياتية وتطبيقات القياس المعياري في المشاريع الوطنية بالمملكة.</li>
                    </ul>
                </div>
            </div>

            <!-- 2. مرحلة الانخراط والتركيز -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٢</span> مرحلة الانخراط والتركيز (Engage & Focus)</h4>
                <div class="pedagogy-box">
                    <div class="briefcase-box">
                        <div class="briefcase-title">💼 الحقيبة التعليمية المحفزة (سؤال الانطلاق):</div>
                        <p>«إذا كنت أمين صندوق في متجر تموينات ذكي في جدة، واشترى عميل مشتريات قيمتها <span class="ar-math">٤٥,٧٥</span> ريالاً، ودفع ورقة نقدية من فئة <span class="ar-math">١٠٠</span> ريال، ثم أضاف سلعة بقيمة <span class="ar-math">٣,٥٠</span> ريالات عليها ضريبة؛ كيف تضمن احتساب المبلغ المتبقي والضريبة بدقة متناهية وسرعة فائقة دون أي خطأ في الفاصلة العشرية؟»</p>
                    </div>

                    <div class="intro-activity-box">
                        <h5>🎯 التمهيد التفاعلي المبتكر وتقويم تشخيصي سريع:</h5>
                        <p><strong>نشاط "تحدي الفاصلة الذكية":</strong> تُعرض بطاقات رقمية سريعة على الشاشة التفاعلية، ويُطلب من الطلاب تحديد موضع الفاصلة في النواتج ذهنياً خلال ٢٠ ثانية.</p>
                        <table class="standard-table">
                            <thead>
                                <tr>
                                    <th>المسألة التشخيصية</th>
                                    <th>المهارة المستهدفة</th>
                                    <th>الإجابة المتوقعة</th>
                                    <th>المعالجة الفورية</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="ar-math">١٢,٣ + ٤,٢٥</span></td>
                                    <td>محاذاة الفواصل وإضافة صفر للتكافؤ</td>
                                    <td><span class="ar-math">١٦,٥٥</span></td>
                                    <td>التأكيد على وضع الفاصلة فوق الفاصلة وإضافة المنازل الخالية.</td>
                                </tr>
                                <tr>
                                    <td><span class="ar-math">٠,٦ × ٠,٤</span></td>
                                    <td>عد المنازل العشرية في الضرب</td>
                                    <td><span class="ar-math">٠,٢٤</span></td>
                                    <td>جمع المنازل على يمين الفاصلة: منزلة + منزلة = منزلتان.</td>
                                </tr>
                                <tr>
                                    <td><span class="ar-math">٤,٨ ÷ ٢</span></td>
                                    <td>قسمة كسر عشري على عدد كلي</td>
                                    <td><span class="ar-math">٢,٤</span></td>
                                    <td>رفع الفاصلة مباشرة في ناتج القسمة عند الوصول إليها.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- جدول KWL -->
                    <div class="kwl-table-wrapper">
                        <h5>📊 جدول التعلم الذاتي المنظم (KWL Table):</h5>
                        <table class="standard-table kwl-table">
                            <thead>
                                <tr>
                                    <th style="width:33%;">ماذا أعرف مسبقاً؟ (K)</th>
                                    <th style="width:33%;">ماذا أريد أن أعرف/أتقن؟ (W)</th>
                                    <th style="width:34%;">ماذا تعلمت بعد الدرس؟ (L)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        • منازل الأعداد العشرية (أعشار، أجزاء المئة).<br>
                                        • جمع وطرح الكسور العشرية بمحاذاة الفاصلة.<br>
                                        • التقدير بالتقريب إلى أقرب عدد كلي.
                                    </td>
                                    <td>
                                        • كيفية حل الاختبارات المعيارية والتراكمية بزمن قياسي.<br>
                                        • التعامل مع قسمة كسر عشري على كسر عشري آخر بتحريك الفاصلة.<br>
                                        • التحقق من معقولية الحل في المسائل اللفظية المعقدة.
                                    </td>
                                    <td>
                                        <span class="l-column-highlight">
                                        (يُستكمل في الغلق):<br>
                                        • إتقان استراتيجيات استبعاد الإجابات الخاطئة في الاختيار من متعدد.<br>
                                        • الضرب في قوى العشرة لتحويل المقسوم عليه إلى عدد كلي.<br>
                                        • الربط التراكمي بين الجبر والعمليات على الأعداد.
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 3. بيئة التعلم والقواعد الصفية -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٣</span> بيئة التعلم والقواعد الصفية الداعمة</h4>
                <div class="rules-flex-container">
                    <div class="rule-card">
                        <div class="rule-icon">⏱️</div>
                        <div class="rule-title">إدارة الوقت المعياري</div>
                        <div class="rule-desc">تخصيص دقيقة ونصف لكل سؤال موضوعي في اختبار الفصل لتدريب الطلاب على سرعة التفكير والدقة في الاختبارات المعيارية.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">🤝</div>
                        <div class="rule-title">المناقشة البناءة الثنائية</div>
                        <div class="rule-desc">عند حل المسائل المقالية، يشرح كل طالب لزميله خطوة محاذاة الفواصل وضرب المقادير مع احترام وجهات النظر.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">📐</div>
                        <div class="rule-title">تنظيم خط الدفتر والمسودة</div>
                        <div class="rule-desc">استخدام خط رأسي فاصل في ورقة الإجابة للمسودة الحسابية وترتيب المنازل رأسياً لمنع تداخل الأرقام.</div>
                    </div>
                </div>
            </div>

            <!-- 4. استراتيجيات التعلم النشط ونماذج التدريس -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٤</span> استراتيجيات التدريس النشط والتنفيذ الإجرائي</h4>
                <div class="pedagogy-box">
                    <div class="strategies-tag-cloud">
                        <span class="strat-pill">العصف الذهني للبدائل</span>
                        <span class="strat-pill">فكر - زاوج - شارك (Think-Pair-Share)</span>
                        <span class="strat-pill">الخريطة المفاهيمية الشجرية</span>
                        <span class="strat-pill">مربع فرير لمفهوم الكسر العشري</span>
                    </div>

                    <!-- خريطة شجرية -->
                    <div class="tree-map-card">
                        <h5>🌳 الخريطة الشجرية لمراجعة العمليات على الكسور العشرية:</h5>
                        <div class="tree-content">
                            <strong>العمليات على الكسور العشرية:</strong>
                            <ul>
                                <li><strong>الجمع والطرح:</strong> محاذاة الفواصل العشرية عمودياً <span class="ar-math">←</span> ملء المنازل الخالية بأصفار <span class="ar-math">←</span> إجراء العملية وتنزيل الفاصلة بمكانها.</li>
                                <li><strong>الضرب:</strong> ضرب الأعداد بدون فواصل كأنها أعداد كلية <span class="ar-math">←</span> عد المنازل العشرية في كلا العاملين <span class="ar-math">←</span> وضع الفاصلة بالناتج من اليمين.</li>
                                <li><strong>القسمة:</strong>
                                    <ul>
                                        <li>على عدد كلي: نرفع الفاصلة مباشرة إلى الناتج ثم نقسم كالمعتاد.</li>
                                        <li>على كسر عشري: نضرب المقسوم والمقسوم عليه في <span class="ar-math">١٠</span> أو <span class="ar-math">١٠٠</span> أو <span class="ar-math">١٠٠٠</span> ليصبح المقسوم عليه عدداً كلياً.</li>
                                    </ul>
                                </li>
                                <li><strong>التقدير وحل المسائل:</strong> استعمال التقريب، أو تجمع البيانات لتقدير معقولية الإجابات وسرعة اتخاذ القرار.</li>
                            </ul>
                        </div>
                    </div>

                    <!-- مربع فرير -->
                    <div class="frayer-model-card">
                        <h5>🔲 نموذج فرير (Frayer Model) لتحليل مفهوم "العمليات على الكسور العشرية":</h5>
                        <div class="frayer-grid">
                            <div class="frayer-quadrant quad-def">
                                <div class="frayer-quad-title">التعريف الرياضي (Definition)</div>
                                <p>إجراء العمليات الحسابية الأساسية (الجمع، الطرح، الضرب، القسمة) على أعداد تتضمن فواصل عشرية تعبر عن أجزاء من قوى العشرة (<span class="ar-math">١٠</span>، <span class="ar-math">١٠٠</span>، <span class="ar-math">١٠٠٠</span>).</p>
                            </div>
                            <div class="frayer-quadrant quad-char">
                                <div class="frayer-quad-title">الخصائص الجوهرية (Characteristics)</div>
                                <p>• قيمة المنزلة تتغير بالانتقال يميناً أو يساراً بمقدار عشرة أمثال.<br>
                                • الفاصلة تفصل بين الجزء الكلي والأجزاء الكسرية.<br>
                                • الصفر على أقصى يمين الجزء العشري لا يغير قيمة الكسر.</p>
                            </div>
                            <div class="frayer-quadrant quad-ex">
                                <div class="frayer-quad-title">أمثلة دالة وتطبيقية (Examples)</div>
                                <p>• <span class="ar-math">٥,٤ + ٣,٨٥ = ٩,٢٥</span><br>
                                • <span class="ar-math">١,٥ × ٠,٣ = ٠,٤٥</span><br>
                                • <span class="ar-math">٦,٤ ÷ ٠,٨ = ٦٤ ÷ ٨ = ٨</span></p>
                            </div>
                            <div class="frayer-quadrant quad-nonex">
                                <div class="frayer-quad-title">أمثلة غير دالة وغير صحيحة (Non-Examples)</div>
                                <p>• جمع <span class="ar-math">١,٢ + ٠,٣٤ = ٠,٤٦</span> (خطأ ناتج عن عدم محاذاة الفواصل).<br>
                                • كتابة <span class="ar-math">٠,٢ × ٠,٣ = ٠,٦</span> (خطأ نسيان منزلة الصفر: الناتج الصحيح <span class="ar-math">٠,٠٦</span>).</p>
                            </div>
                        </div>
                    </div>

                    <!-- أمثلة الكتاب المحلولة ص 135 و 136 -->
                    <div class="book-examples-card">
                        <h5>📖 أمثلة الكتاب المعتمدة المحلولة خطوة بخطوة (ص ١٣٥ - ١٣٦):</h5>
                        <div class="solved-example">
                            <div class="ex-label">مثال ١ (اختبار الفصل ٣ - ص ١٣٥، سؤال ١): أوجد ناتج الجمع: <span class="ar-math">١٢,٤ + ٨,٧٥</span></div>
                            <div class="ex-steps">
                                <strong>خطوات الحل المنظمة:</strong><br>
                                ١) نكتب العددين عمودياً بحيث تكون الفواصل العشرية فوق بعضها تماماً:
                                <div class="arabic-vert-calc-wrapper">
                                    <table class="arabic-vert-table">
                                        <caption>خطوات الجمع الرأسي (الرمز على اليمين):</caption>
                                        <tr><td class="sign-col"></td><td class="num-col">١٢,٤٠</td></tr>
                                        <tr class="op-divider"><td class="sign-col">+</td><td class="num-col">٠٨,٧٥</td></tr>
                                        <tr class="res-row"><td class="sign-col"></td><td class="num-col">٢١,١٥</td></tr>
                                    </table>
                                </div>
                                ٢) وضعنا صفراً على يمين الرقم <span class="ar-math">٤</span> لتتساوى المنازل العشرية (جزآن من مئة).<br>
                                ٣) نجمع من اليمين: <span class="ar-math">٠ + ٥ = ٥</span>، ثم <span class="ar-math">٤ + ٧ = ١١</span> (نكتب <span class="ar-math">١</span> ونعيد تجميع <span class="ar-math">١</span> مع الآحاد)، وننزل الفاصلة في مكانها.<br>
                                ٤) ناتج الجمع هو: <strong><span class="ar-math">٢١,١٥</span></strong>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٢ (اختبار الفصل ٣ - ص ١٣٥، سؤال ٧): أوجد ناتج الضرب: <span class="ar-math">٣,٦ × ٠,٤</span></div>
                            <div class="ex-steps">
                                <strong>خطوات الحل المنظمة:</strong><br>
                                ١) نضرب العددين كما لو كانا عددين كليين دون فواصل: <span class="ar-math">٣٦ × ٤ = ١٤٤</span>.<br>
                                ٢) نعد المنازل العشرية في العددين: في <span class="ar-math">٣,٦</span> منزلة واحدة، وفي <span class="ar-math">٠,٤</span> منزلة واحدة <span class="ar-math">→</span> المجموع منزلتان.<br>
                                ٣) نعد منزلتين من اليمين في الناتج <span class="ar-math">١٤٤</span> ونضع الفاصلة: <strong><span class="ar-math">١,٤٤</span></strong>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٣ (اختبار تراكمي ٣ - ص ١٣٦، سؤال مقالي ٥): أوجد ناتج: <span class="ar-math">١٥,٦ ÷ ٠,٣</span></div>
                            <div class="ex-steps">
                                <strong>خطوات الحل المنظمة:</strong><br>
                                ١) المقسوم عليه هو <span class="ar-math">٠,٣</span> (كسر عشري)، لذا نضرب كلاً من المقسوم والمقسوم عليه في <span class="ar-math">١٠</span> للتخلص من الفاصلة بالمقسوم عليه:
                                <div class="ar-math-display">١٥,٦ × ١٠ = ١٥٦   ,   ٠,٣ × ١٠ = ٣</div>
                                ٢) نقسم الآن كأعداد كلية: <span class="ar-math">١٥٦ ÷ ٣</span>.<br>
                                ٣) <span class="ar-math">١٥ ÷ ٣ = ٥</span>، ثم <span class="ar-math">٦ ÷ ٣ = ٢</span>.<br>
                                ٤) ناتج القسمة النهائي هو: <strong><span class="ar-math">٥٢</span></strong>.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5. التكامل ومصفوفة STEM -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٥</span> الربط الحياتي ومصفوفة تكامل STEM</h4>
                <div class="stem-grid">
                    <div class="stem-card stem-s">
                        <div class="stem-header">🔬 العلوم (Science)</div>
                        <div class="stem-body">حساب كثافة المحاليل الكيميائية في المختبر المدرسي بقياس كتل بالجرام وسوائل بالمليلتر تحتوي على كسور عشرية دقيقة.</div>
                    </div>
                    <div class="stem-card stem-t">
                        <div class="stem-header">💻 التقنية (Technology)</div>
                        <div class="stem-body">برمجة أجهزة الدفع الإلكتروني (مدى / Apple Pay) لمعالجة العمليات الحسابية للضريبة والمتبقي باستخدام لغة الخوارزميات الرقمية.</div>
                    </div>
                    <div class="stem-card stem-e">
                        <div class="stem-header">🏗️ الهندسة (Engineering)</div>
                        <div class="stem-body">قياس أبعاد واجهات المباني الخرسانية بدقة أجزاء السنتيمتر في مشاريع تطوير كورنيش جدة ومدينة نيوم.</div>
                    </div>
                    <div class="stem-card stem-m">
                        <div class="stem-header">📐 الرياضيات (Mathematics)</div>
                        <div class="stem-body">تطبيق خوارزميات العمليات الأربع، وقوانين المنازل العشرية، وإجراء المقارنات والتحقق المعياري من صحة النواتج.</div>
                    </div>
                </div>
                <div class="national-link-box">
                    <strong>🇸🇦 الربط برؤية المملكة ٢٠٣٠ والمجتمع:</strong> يربط المعلم مهارة الحساب العشري السريع والتقدير بإدارة ميزانية المشاريع الريادية للشباب السعودي وتوسيع استخدام التجارة الرقمية المعتمدة على الفوترة الإلكترونية السحابية المطبقة عبر هيئة الزكاة والضريبة والجمارك.
                </div>
            </div>

            <!-- 6. منظومة التقويم الشامل -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٦</span> منظومة التقويم المتكاملة (بنائي - ختامي - واجب)</h4>
                <div class="pedagogy-box">
                    <h5>📝 أولاً: التقويم البنائي المتدرج (Formative Assessment):</h5>
                    <div class="formative-q-box">
                        <div class="q-item">
                            <span class="q-badge">سؤال ١ (تذكر وفهم):</span> احسب ناتج: <span class="ar-math">٢٥,٣ − ٧,٨٥</span>.
                            <div class="q-ans"><strong>الجواب النموذجي:</strong> نضع صفراً ليصبح <span class="ar-math">٢٥,٣٠ − ٧,٨٥</span>. الطرح بالاستلاف يعطي الناتج: <strong><span class="ar-math">١٧,٤٥</span></strong>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٢ (تطبيق وتحليل):</span> اشترى خالد <span class="ar-math">٣,٥</span> كجم من التمر السكري بسعر <span class="ar-math">٢٤</span> ريالاً للكيلوجرام الواحد. فما التكلفة الكلية؟
                            <div class="q-ans"><strong>الجواب النموذجي:</strong> نضرب <span class="ar-math">٣,٥ × ٢٤</span>. <span class="ar-math">٣٥ × ٢٤ = ٨٤٠</span>. بوضع الفاصلة بعد منزلة واحدة يصبح الناتج: <strong><span class="ar-math">٨٤</span> ريالاً</strong>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٣ (تقويم وتفكير عليا):</span> إذا كان ناتج ضرب <span class="ar-math">١,٨ ×</span> ن <span class="ar-math">= ٠,٥٤</span>، فما قيمة ن؟
                            <div class="q-ans"><strong>الجواب النموذجي:</strong> ن <span class="ar-math">= ٠,٥٤ ÷ ١,٨ = ٥,٤ ÷ ١٨ = ٠,٣</span>. إذن <strong>ن <span class="ar-math">= ٠,٣</span></strong>.</div>
                        </div>
                    </div>

                    <h5>🎯 ثانياً: التقويم الختامي الشامل (Summative Assessment):</h5>
                    <div class="summative-q-box">
                        <p><strong>المسألة الختامية:</strong> قطع قطار الحرمين السريع مسافة <span class="ar-math">٣١٢,٥</span> كيلومتراً في زمن قدره <span class="ar-math">١,٢٥</span> ساعة. احسب معدل السرعة المتوسطة للقطار بالكيلومتر لكل ساعة.</p>
                        <div class="q-ans">
                            <strong>الحل النموذجي المكتمل:</strong><br>
                            المعدل = المسافة <span class="ar-math">÷</span> الزمن = <span class="ar-math">٣١٢,٥ ÷ ١,٢٥</span>.<br>
                            نضرب كلاً من المقسوم والمقسوم عليه في <span class="ar-math">١٠٠</span> للتخلص من الفاصلة: <span class="ar-math">٣١٢٥٠ ÷ ١٢٥</span>.<br>
                            بالقسمة المطولة: <span class="ar-math">٣١٢٥٠ ÷ ١٢٥ = ٢٥٠</span>.<br>
                            إذن سرعة القطار هي <strong><span class="ar-math">٢٥٠</span> كم/ساعة</strong>، وهي سرعة واقعية مطابقة لمواصفات قطار الحرمين بالمملكة.
                        </div>
                    </div>

                    <h5>🏠 ثالثاً: الواجب المنزلي المعياري (Homework MCQ):</h5>
                    <div class="homework-box">
                        <p class="hw-question"><strong>سؤال الواجب:</strong> ما قيمة التعبير الرياضي التالي: <span class="ar-math">٧,٢ ÷ ٠,٠٩</span>؟</p>
                        <div class="hw-options-vertical">
                            <div class="hw-opt">أ) <span class="ar-math">٠,٨</span></div>
                            <div class="hw-opt">ب) <span class="ar-math">٨</span></div>
                            <div class="hw-opt correct-opt">ج) <span class="ar-math">٨٠</span> (الإجابة الصحيحة)</div>
                            <div class="hw-opt">د) <span class="ar-math">٨٠٠</span></div>
                        </div>
                        <div class="hw-solution-note">
                            <strong>التفسير الرياضي الدقيق:</strong> لتحويل المقسوم عليه (<span class="ar-math">٠,٠٩</span>) إلى عدد كلي، نضرب في <span class="ar-math">١٠٠</span>. نضرب المقسوم أيضاً في <span class="ar-math">١٠٠</span>: <span class="ar-math">٧,٢ × ١٠٠ = ٧٢٠</span>. تصبح المسألة <span class="ar-math">٧٢٠ ÷ ٩ = ٨٠</span>. لذا فالخيار الصحيح هو (ج).
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. الغلق والتلخيص -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٧</span> الغلق المعرفي والمهمة الإثرائية للدرس القادم</h4>
                <div class="closing-box">
                    <p><strong>غلق الدرس وتأكيد عمود التعلم (L):</strong> يناقش المعلم مع الطلاب ما تم إنجازه، ويسجلون في دفاترهم ملخصاً من سطرين حول: "كيف أضمن عدم نسيان الفاصلة في عمليات الضرب والقسمة".</p>
                    <div class="enrichment-challenge">
                        <strong>🌟 سؤال التحدي الإثرائي (تمهيد للفصل الرابع):</strong> «إذا كان لديك كسر عشري هو <span class="ar-math">٠,٧٥</span>، فكيف تحوله إلى كسر اعتيادي في صورة بسط ومقام، وما المشترك بين البسط والمقام لتبسيطه إلى أقصى حد؟»
                    </div>
                </div>
            </div>
        </article>
"""

print("Plan 1 defined successfully.")
