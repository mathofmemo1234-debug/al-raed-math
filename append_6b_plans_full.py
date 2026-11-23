# -*- coding: utf-8 -*-
"""
append_6b_plans_full.py: Completes Plans 2, 3, 4, 5 for 6ب (pages 135-151)
and generates section_6b_plans.html.
"""
import sys
import build_6b_plans as b

sys.stdout.reconfigure(encoding='utf-8')

PLAN_2 = r"""
        <!-- الخطة الثانية: تهيئة واستعداد الفصل ٤ -->
        <article class="unit-card" id="plan-2-ch4-prep">
            <div class="unit-header">
                <div class="unit-badge">الخطة الدراسية الثانية (ص ١٣٨ – ١٣٩)</div>
                <h3 class="unit-title">خطة التهيئة والاستعداد: الفصل الرابع (الكسور الاعتيادية والكسور العشرية)</h3>
                <div class="unit-meta">
                    <span><strong>الصف:</strong> السادس الابتدائي</span> |
                    <span><strong>المادة:</strong> الرياضيات</span> |
                    <span><strong>المجال:</strong> الأعداد والعمليات عليها</span> |
                    <span><strong>الفصل ٤:</strong> الكسور الاعتيادية والكسور العشرية</span>
                </div>
            </div>

            <!-- 1. الأهداف والمعايير -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">١</span> نواتج التعلم والمعايير المستهدفة (الأهداف SMART)</h4>
                <div class="pedagogy-box">
                    <ul class="smart-goals-list">
                        <li><strong>هدف معرفي:</strong> أن يحدد الطالب قواسم الأعداد الكلية بدقة، ويتعرف على بنية الكسر الاعتيادي (البسط والمقام) ونماذجه الهندسية بنسبة إتقان ٩٠٪.</li>
                        <li><strong>هدف مهاري:</strong> أن يمثل الطالب الكسور الاعتيادية كنماذج بصرية مظللة ويقارن بين الأجزاء المقتطعة من الواحد الصحيح بثقة وسرعة.</li>
                        <li><strong>هدف وجداني:</strong> أن يدرك الطالب أهمية النمذجة الرياضية وتقسيم الموارد في الحياة العملية والمشروعات التطبيقية بالمملكة.</li>
                    </ul>
                </div>
            </div>

            <!-- 2. الانخراط والتركيز -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٢</span> مرحلة الانخراط والتركيز (Engage & Focus)</h4>
                <div class="pedagogy-box">
                    <div class="briefcase-box">
                        <div class="briefcase-title">💼 الحقيبة التعليمية المحفزة:</div>
                        <p>«إذا طلب منك مهندس معماري في مشروع حديقة الملك سلمان تصميم ممر للمشاة مبلط بـ <span class="ar-math">٢٤</span> بلاطة رخامية، ويراد تقسيمها في صفوف متساوية تماماً بدون كسر أي بلاطة؛ ما التشكيلات الممكنة لترتيب هذا الممر، وما علاقة ذلك بقواسم العدد <span class="ar-math">٢٤</span>؟»</p>
                    </div>

                    <div class="intro-activity-box">
                        <h5>🎯 التمهيد التفاعلي وتقويم تشخيصي سريع:</h5>
                        <p><strong>نشاط "تحدي المستطيلات المتساوية":</strong> رسم كافة المستطيلات التي مساحتها <span class="ar-math">١٢</span> وحدة مربعة على شبكة المربعات لاكتشاف قواسم العدد <span class="ar-math">١٢</span>.</p>
                        <table class="standard-table">
                            <thead>
                                <tr>
                                    <th>السؤال التشخيصي</th>
                                    <th>المهارة المستهدفة</th>
                                    <th>الإجابة النموذجية</th>
                                    <th>العلاج الفوري</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>اكتب جميع قواسم العدد <span class="ar-math">١٨</span></td>
                                    <td>تحديد قواسم الأعداد (عوامل الضرب)</td>
                                    <td><span class="ar-math">١ ، ٢ ، ٣ ، ٦ ، ٩ ، ١٨</span></td>
                                    <td>كتابة أزواج الضرب: <span class="ar-math">١×١٨</span>، <span class="ar-math">٢×٩</span>، <span class="ar-math">٣×٦</span>.</td>
                                </tr>
                                <tr>
                                    <td>ما الكسر الذي يمثل <span class="ar-math">٣</span> أجزاء مظللة من أصل <span class="ar-math">٨</span> أجزاء متطابقة؟</td>
                                    <td>التعبير عن النموذج بكسر اعتيادي</td>
                                    <td><span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٨</span></span></span></td>
                                    <td>التأكيد على أن البسط = الأجزاء المظللة، والمقام = الكل.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- KWL -->
                    <div class="kwl-table-wrapper">
                        <h5>📊 جدول التعلم الذاتي (KWL Table):</h5>
                        <table class="standard-table kwl-table">
                            <thead>
                                <tr>
                                    <th>ماذا أعرف؟ (K)</th>
                                    <th>ماذا أريد أن أعرف؟ (W)</th>
                                    <th>ماذا تعلمت؟ (L)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        • قواسم الأعداد الصغيرة من جدول الضرب.<br>
                                        • البسط يعبر عن الجزء والمقام يعبر عن الكل.
                                    </td>
                                    <td>
                                        • كيف أربط بين القواسم وتبسيط الكسور وتحويلها؟<br>
                                        • ما العلاقة بين الكسور الاعتيادية والكسور العشرية؟
                                    </td>
                                    <td>
                                        <span class="l-column-highlight">
                                        (يُستكمل في الغلق):<br>
                                        • أزواج القواسم المنظمة تسهل إيجاد القاسم المشترك الأكبر.<br>
                                        • الكسر الاعتيادي يمثل عملية قسمة البسط على المقام.
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٣</span> بيئة التعلم والقواعد الصفية</h4>
                <div class="rules-flex-container">
                    <div class="rule-card">
                        <div class="rule-icon">🎨</div>
                        <div class="rule-title">الدقة في التظليل والنمذجة</div>
                        <div class="rule-desc">استخدام المسطرة والألوان للتظليل الدقيق والتأكد من تطابق المساحات المجزأة.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">🗣️</div>
                        <div class="rule-title">التحدث بلغة الرياضيات</div>
                        <div class="rule-desc">استعمال المصطلحات الرياضية الدقيقة: (بسط، مقام، قاسم، زوج ضربي، خط الكسر).</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">💡</div>
                        <div class="rule-title">المشاركة الإيجابية المتكافئة</div>
                        <div class="rule-desc">إتاحة الفرصة لكل عضو في المجموعة لمشاركة زوج من أزواج قواسم العدد المطلوب.</div>
                    </div>
                </div>
            </div>

            <!-- 4. استراتيجيات التدريس النشط -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٤</span> الاستراتيجيات النشطة والتنفيذ الإجرائي</h4>
                <div class="pedagogy-box">
                    <div class="strategies-tag-cloud">
                        <span class="strat-pill">العصف الذهني لقواسم الأعداد</span>
                        <span class="strat-pill">فكر - زاوج - شارك</span>
                        <span class="strat-pill">خريطة مفاهيم الكسور</span>
                        <span class="strat-pill">نموذج فرير لمفهوم الكسر الاعتيادي</span>
                    </div>

                    <div class="tree-map-card">
                        <h5>🌳 الخريطة الشجرية لمهارات تهيئة الفصل الرابع:</h5>
                        <div class="tree-content">
                            <strong>محاور التهيئة والاستعداد:</strong>
                            <ul>
                                <li><strong>قواسم الأعداد:</strong> أزواج الأعداد التي حاصل ضربها يساوي العدد المعطى (تبدأ دائماً بالعدد <span class="ar-math">١</span> وتنتهي بالعدد نفسه).</li>
                                <li><strong>الكسور الاعتيادية:</strong>
                                    <ul>
                                        <li><strong>البسط (العلوي):</strong> عدد الأجزاء المختارة أو المظللة.</li>
                                        <li><strong>المقام (السفلي):</strong> العدد الإجمالي للأجزاء المتطابقة التي يشتمل عليها الكل.</li>
                                    </ul>
                                </li>
                                <li><strong>الربط بين الكسور وقسمة الأعداد:</strong> الكسر (أ / ب) هو نفسه التعبير أ ÷ ب.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="frayer-model-card">
                        <h5>🔲 نموذج فرير لمفهوم "الكسر الاعتيادي":</h5>
                        <div class="frayer-grid">
                            <div class="frayer-quadrant quad-def">
                                <div class="frayer-quad-title">التعريف الرياضي</div>
                                <p>عدد يمثل جزءاً أو أكثر من أجزاء متطابقة من كل أو مجموعة، ويكتب على صورة (البسط / المقام) حيث المقام لا يساوي صفراً.</p>
                            </div>
                            <div class="frayer-quadrant quad-char">
                                <div class="frayer-quad-title">الخصائص الأساسية</div>
                                <p>• المقام يعبر عن عدد التقسيمات المتساوية للواحد الصحيح.<br>
                                • كلما كبر المقام صغرت قيمة الجزء إذا ثبت البسط.<br>
                                • إذا تساوى البسط والمقام فإن الكسر يساوي الواحد الصحيح (<span class="ar-math">١</span>).</p>
                            </div>
                            <div class="frayer-quadrant quad-ex">
                                <div class="frayer-quad-title">أمثلة دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>، <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>، <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٨</span></span></span><br>
                                • ٣ قطع بيتزا من أصل ٨ قطع متطابقة.</p>
                            </div>
                            <div class="frayer-quadrant quad-nonex">
                                <div class="frayer-quad-title">أمثلة غير دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٠</span></span></span> (غير معرف لأن المقام صفر).<br>
                                • تقسيم تفاحة إلى نصفين غير متساويين (ليست أجزاء متطابقة).</p>
                            </div>
                        </div>
                    </div>

                    <div class="book-examples-card">
                        <h5>📖 أمثلة الكتاب المحلولة (التهيئة ص ١٣٨ – ١٣٩):</h5>
                        <div class="solved-example">
                            <div class="ex-label">مثال ١ (التهيئة ص ١٣٩، سؤال ٩): أوجد قواسم العدد <span class="ar-math">٢٠</span></div>
                            <div class="ex-steps">
                                <strong>طريقة أزواج الضرب المنظمة:</strong><br>
                                <span class="ar-math">١ × ٢٠ = ٢٠</span><br>
                                <span class="ar-math">٢ × ١٠ = ٢٠</span><br>
                                <span class="ar-math">٤ × ٥ = ٢٠</span><br>
                                إذن قواسم العدد <span class="ar-math">٢٠</span> مرتبة تصاعدياً هي: <strong><span class="ar-math">١ ، ٢ ، ٤ ، ٥ ، ١٠ ، ٢٠</span></strong>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٢ (التهيئة ص ١٣٩، سؤال ١٧): اكتب الكسر الذي يمثل الجزء المظلل في شكل مقسم إلى ٦ مثلثات متطابقة ظلل منها ٥</div>
                            <div class="ex-steps">
                                <strong>خطوات الحل:</strong><br>
                                ١) نعد الأجزاء المظللة: <span class="ar-math">٥</span> أجزاء <span class="ar-math">→</span> تمثل البسط.<br>
                                ٢) نعد جميع الأجزاء المتطابقة في الشكل: <span class="ar-math">٦</span> أجزاء <span class="ar-math">→</span> تمثل المقام.<br>
                                ٣) الكسر الاعتيادي هو: <strong><span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٦</span></span></span></strong>.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5. التكامل وSTEM -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٥</span> الربط الحياتي ومصفوفة تكامل STEM</h4>
                <div class="stem-grid">
                    <div class="stem-card stem-s">
                        <div class="stem-header">🔬 العلوم</div>
                        <div class="stem-body">تحديد نسبة الغازات في الغلاف الجوي كأجزاء من الكل (الأكسجين يشكل حوالي خمس الغلاف الجوي).</div>
                    </div>
                    <div class="stem-card stem-t">
                        <div class="stem-header">💻 التقنية</div>
                        <div class="stem-body">تمثيل سعة التخزين المستهلكة في الأقراص الصلبة والهواتف الذكية على هيئة أشرطة دائرية مجزأة.</div>
                    </div>
                    <div class="stem-card stem-e">
                        <div class="stem-header">🏗️ الهندسة</div>
                        <div class="stem-body">توزيع الأعمدة الخرسانية وفواصل التمدد الإنشائية على مسافات منتظمة تمثل قواسم الطول الكلي للجسر.</div>
                    </div>
                    <div class="stem-card stem-m">
                        <div class="stem-header">📐 الرياضيات</div>
                        <div class="stem-body">توظيف خوارزميات إيجاد العوامل وقواعد قابلية القسمة والربط بين الكسور والنسب.</div>
                    </div>
                </div>
            </div>

            <!-- 6. منظومة التقويم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٦</span> منظومة التقويم المتكاملة</h4>
                <div class="pedagogy-box">
                    <h5>📝 التقويم البنائي:</h5>
                    <div class="formative-q-box">
                        <div class="q-item">
                            <span class="q-badge">سؤال ١:</span> اذكر جميع قواسم العدد <span class="ar-math">٢٨</span>.
                            <div class="q-ans"><strong>الجواب:</strong> <span class="ar-math">١ ، ٢ ، ٤ ، ٧ ، ١٤ ، ٢٨</span>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٢:</span> ما الكسر الذي يمثل تسعة أشهر من السنة الهجرية الكاملة؟
                            <div class="q-ans"><strong>الجواب:</strong> السنة الهجرية تتكون من <span class="ar-math">١٢</span> شهراً، إذن الكسر هو <span class="ar-math"><span class="ar-frac"><span class="num">٩</span><span class="denom">١٢</span></span></span>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٣:</span> أي من الأعداد التالية ليس قاسماً للعدد <span class="ar-math">٣٦</span>: (<span class="ar-math">٣</span>، <span class="ar-math">٤</span>، <span class="ar-math">٨</span>، <span class="ar-math">٩</span>)؟
                            <div class="q-ans"><strong>الجواب:</strong> العدد <strong><span class="ar-math">٨</span></strong>؛ لأن <span class="ar-math">٣٦</span> لا تقبل القسمة على <span class="ar-math">٨</span> بدون باقٍ (<span class="ar-math">٣٦ ÷ ٨ = ٤,٥</span>).</div>
                        </div>
                    </div>

                    <h5>🎯 التقويم الختامي:</h5>
                    <div class="summative-q-box">
                        <p><strong>المسألة:</strong> حديقة مستطيلة الشكل في واجهة جدة البحرية مساحتها <span class="ar-math">٣٦</span> متراً مربعاً. اذكر جميع الأبعاد الممكنة للحديقة بأعداد كلية (أزواج قواسم المساحة).</p>
                        <div class="q-ans"><strong>الحل:</strong> الأبعاد الممكنة (الطول <span class="ar-math">×</span> العرض) هي أزواج قواسم <span class="ar-math">٣٦</span>: (<span class="ar-math">٣٦ × ١</span>)، (<span class="ar-math">١٨ × ٢</span>)، (<span class="ar-math">١٢ × ٣</span>)، (<span class="ar-math">٩ × ٤</span>)، (<span class="ar-math">٦ × ٦</span>).</div>
                    </div>

                    <h5>🏠 الواجب المنزلي المعياري:</h5>
                    <div class="homework-box">
                        <p class="hw-question"><strong>سؤال الواجب:</strong> ما عدد قواسم العدد <span class="ar-math">١٦</span>؟</p>
                        <div class="hw-options-vertical">
                            <div class="hw-opt">أ) <span class="ar-math">٣</span> قواسم</div>
                            <div class="hw-opt">ب) <span class="ar-math">٤</span> قواسم</div>
                            <div class="hw-opt correct-opt">ج) <span class="ar-math">٥</span> قواسم (<span class="ar-math">١، ٢، ٤، ٨، ١٦</span>) (الإجابة الصحيحة)</div>
                            <div class="hw-opt">د) <span class="ar-math">٦</span> قواسم</div>
                        </div>
                        <div class="hw-solution-note">
                            <strong>التفسير:</strong> قواسم <span class="ar-math">١٦</span> هي: <span class="ar-math">١×١٦</span>، <span class="ar-math">٢×٨</span>، <span class="ar-math">٤×٤</span>. وبما أن الرقم <span class="ar-math">٤</span> لا يكرر عند السرد، فالقواسم هي: <span class="ar-math">١ ، ٢ ، ٤ ، ٨ ، ١٦</span> وعددها <span class="ar-math">٥</span> قواسم.
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. الغلق -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٧</span> الغلق والتحدي الإثرائي</h4>
                <div class="closing-box">
                    <p><strong>غلق الدرس:</strong> كتابة الطلاب في عمود (L): "القواسم هي الأعداد التي تقسم عدداً دون باقٍ، والكسور تمثل أجزاء متطابقة".</p>
                    <div class="enrichment-challenge">
                        <strong>🌟 سؤال التحدي للدرس القادم:</strong> «إذا كان لديك عددان هما <span class="ar-math">١٢</span> و <span class="ar-math">١٨</span>، فما هي القواسم التي يشتركان فيها معاً، وما أكبر هذا القواسم المشتركة؟»
                    </div>
                </div>
            </div>
        </article>
"""

PLAN_3 = r"""
        <!-- الخطة الثالثة: الدرس (٤-١) القاسم المشترك الأكبر (ق.م.أ) -->
        <article class="unit-card" id="plan-3-lesson4-1-gcf">
            <div class="unit-header">
                <div class="unit-badge">الخطة الدراسية الثالثة (ص ١٤٠ – ١٤٤)</div>
                <h3 class="unit-title">خطة الدرس (٤-١): القاسم المشترك الأكبر (ق.م.أ)</h3>
                <div class="unit-meta">
                    <span><strong>الصف:</strong> السادس الابتدائي</span> |
                    <span><strong>المادة:</strong> الرياضيات</span> |
                    <span><strong>المجال:</strong> الأعداد والعمليات عليها</span> |
                    <span><strong>موضوع الدرس:</strong> إيجاد (ق.م.أ) لعددين أو أكثر</span>
                </div>
            </div>

            <!-- 1. الأهداف والمعايير -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">١</span> نواتج التعلم والمعايير المستهدفة (الأهداف SMART)</h4>
                <div class="pedagogy-box">
                    <ul class="smart-goals-list">
                        <li><strong>هدف معرفي:</strong> أن يعرّف الطالب مفهوم القاسم المشترك والقاسم المشترك الأكبر (ق.م.أ) بدقة رياضية بنسبة إتقان ١٠٠٪.</li>
                        <li><strong>هدف مهاري:</strong> أن يجد الطالب (ق.م.أ) لمجموعات عددية من عددين أو ثلاثة أعداد بطريقتين: (١) كتابة القواسم المنظمة، (٢) التحليل إلى العوامل الأولية بشجرة العوامل.</li>
                        <li><strong>هدف وجداني:</strong> أن يوظف الطالب مهارة إيجاد (ق.م.أ) في حل مسائل توزيع الموارد وتعبئة المنتجات بالتساوي دون هدر.</li>
                    </ul>
                </div>
            </div>

            <!-- 2. الانخراط والتركيز -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٢</span> مرحلة الانخراط والتركيز (Engage & Focus)</h4>
                <div class="pedagogy-box">
                    <div class="briefcase-box">
                        <div class="briefcase-title">💼 الحقيبة التعليمية المحفزة:</div>
                        <p>«يرتب محل لبيع الفطائر في شارع التحلية بجدة <span class="ar-math">٢٤</span> فطيرة جبن، و <span class="ar-math">٣٢</span> فطيرة لحم، و <span class="ar-math">٤٠</span> فطيرة زعتر في صفوف متساوية في ثلاجة العرض بحيث يحتوي كل صف على العدد نفسه من نوع واحد فقط. ما أكبر عدد من الفطائر يمكن وضعه في كل صف دون أي زيادة؟»</p>
                    </div>

                    <div class="intro-activity-box">
                        <h5>🎯 التمهيد التفاعلي وتقويم تشخيصي سريع:</h5>
                        <p><strong>نشاط "شجرة العوامل الذكية":</strong> يوزع المعلم بطاقات بها الأعداد <span class="ar-math">١٢</span> و <span class="ar-math">١٨</span> ويتنافس الطلاب في رسم شجرة العوامل السريعة للوصول إلى الأعداد الأولية.</p>
                        <table class="standard-table">
                            <thead>
                                <tr>
                                    <th>السؤال التشخيصي</th>
                                    <th>المهارة المستهدفة</th>
                                    <th>الإجابة المتوقعة</th>
                                    <th>العلاج السريع</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>حلل العدد <span class="ar-math">٢٤</span> إلى عوامله الأولية</td>
                                    <td>التحليل إلى عوامل أولية</td>
                                    <td><span class="ar-math">٢ × ٢ × ٢ × ٣ = ٢^٣ × ٣</span></td>
                                    <td>استخدام شجرة العوامل بدءاً من <span class="ar-math">٤×٦</span> أو <span class="ar-math">٢×١٢</span>.</td>
                                </tr>
                                <tr>
                                    <td>هل العدد <span class="ar-math">٩</span> عدد أولي؟ وضح.</td>
                                    <td>التمييز بين الأولي وغير الأولي</td>
                                    <td>لا، لأن له ٣ قواسم هي: <span class="ar-math">١ ، ٣ ، ٩</span>.</td>
                                    <td>تذكير الطالب بأن العدد الأولي له قاسمان فقط: الواحد والعدد نفسه.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- KWL -->
                    <div class="kwl-table-wrapper">
                        <h5>📊 جدول التعلم الذاتي (KWL Table):</h5>
                        <table class="standard-table kwl-table">
                            <thead>
                                <tr>
                                    <th>ماذا أعرف؟ (K)</th>
                                    <th>ماذا أريد أن أعرف؟ (W)</th>
                                    <th>ماذا تعلمت؟ (L)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        • قواسم الأعداد الفردية والزوجية.<br>
                                        • مفهوم الأعداد الأولية وتحليل الأعداد.
                                    </td>
                                    <td>
                                        • ما هو القاسم المشترك الأكبر (ق.م.أ)؟<br>
                                        • متى تكون طريقة التحليل بالعوامل أفضل من طريقة السرد؟<br>
                                        • كيف نجد ق.م.أ لثلاثة أعداد كبيرة؟
                                    </td>
                                    <td>
                                        <span class="l-column-highlight">
                                        (يُستكمل في الغلق):<br>
                                        • ق.م.أ هو أكبر قاسم مشترك بين الأعداد.<br>
                                        • في التحليل الأولي: ق.م.أ هو حاصل ضرب العوامل الأولية المشتركة فقط بأصغر تكرار.
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٣</span> بيئة التعلم والقواعد الصفية</h4>
                <div class="rules-flex-container">
                    <div class="rule-card">
                        <div class="rule-icon">📋</div>
                        <div class="rule-title">التسلسل في سرد القواسم</div>
                        <div class="rule-desc">كتابة القواسم في أزواج مرتبة لتجنب نسيان أي قاسم للعدد.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">🔍</div>
                        <div class="rule-title">التحقق بالدوائر المشتركة</div>
                        <div class="rule-desc">استخدام أشكال ڤن (Venn Diagrams) أو وضع دوائر ملونة حول العوامل المشتركة.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">⏱️</div>
                        <div class="rule-title">الهدوء والتركيز الفردي</div>
                        <div class="rule-desc">تخصيص دقيقة للتفكير الفردي الصامت قبل التداول مع الزميل المجاور.</div>
                    </div>
                </div>
            </div>

            <!-- 4. استراتيجيات التدريس النشط -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٤</span> الاستراتيجيات النشطة والتنفيذ الإجرائي</h4>
                <div class="pedagogy-box">
                    <div class="strategies-tag-cloud">
                        <span class="strat-pill">طريقة السرد المنظم للقواسم</span>
                        <span class="strat-pill">طريقة شجرة العوامل الأولية</span>
                        <span class="strat-pill">فكر - زاوج - شارك</span>
                        <span class="strat-pill">مربع فرير لمفهوم (ق.م.أ)</span>
                    </div>

                    <div class="tree-map-card">
                        <h5>🌳 الخريطة الشجرية لطرق إيجاد القاسم المشترك الأكبر (ق.م.أ):</h5>
                        <div class="tree-content">
                            <strong>طرق إيجاد (ق.م.أ):</strong>
                            <ul>
                                <li><strong>الطريقة الأولى (سرد القواسم):</strong>
                                    <ul>
                                        <li>١) نكتب قائمة بجميع قواسم كل عدد.</li>
                                        <li>٢) نحدد القواسم المشتركة بين القوائم.</li>
                                        <li>٣) نختار أكبر هذه القواسم المشتركة وهو (ق.م.أ). (مناسبة للأعداد الصغيرة).</li>
                                    </ul>
                                </li>
                                <li><strong>الطريقة الثانية (التحليل إلى العوامل الأولية):</strong>
                                    <ul>
                                        <li>١) نحلل كل عدد إلى عوامله الأولية بشجرة العوامل.</li>
                                        <li>٢) نحدد العوامل الأولية المشتركة بين جميع الأعداد.</li>
                                        <li>٣) نضرب العوامل المشتركة ذات التكرار الأقل، وحاصل الضرب هو (ق.م.أ). (ممتازة للأعداد الكبيرة).</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="frayer-model-card">
                        <h5>🔲 نموذج فرير لمفهوم "القاسم المشترك الأكبر (ق.م.أ)":</h5>
                        <div class="frayer-grid">
                            <div class="frayer-quadrant quad-def">
                                <div class="frayer-quad-title">التعريف الرياضي</div>
                                <p>أكبر عدد كلي يقسم عددين أو أكثر في الوقت نفسه بدون باقٍ، ويرمز له بالرمز (ق.م.أ).</p>
                            </div>
                            <div class="frayer-quadrant quad-char">
                                <div class="frayer-quad-title">الخصائص الأساسية</div>
                                <p>• يكون دائماً أصغر من أو يساوي أصغر الأعداد المعطاة.<br>
                                • إذا كان أحد العددين مضاعفاً للآخر، فإن ق.م.أ لهما هو العدد الأصغر.<br>
                                • إذا كان العددان أوليين فيما بينهما فإن ق.م.أ لهما يساوي <span class="ar-math">١</span>.</p>
                            </div>
                            <div class="frayer-quadrant quad-ex">
                                <div class="frayer-quad-title">أمثلة دالة</div>
                                <p>• للعددين <span class="ar-math">٨</span> و <span class="ar-math">١٢</span>: قواسمهما المشتركة <span class="ar-math">١، ٢، ٤</span> <span class="ar-math">←</span> ق.م.أ = <span class="ar-math">٤</span>.<br>
                                • للأعداد <span class="ar-math">٦</span> و <span class="ar-math">١٨</span> <span class="ar-math">←</span> ق.م.أ = <span class="ar-math">٦</span>.</p>
                            </div>
                            <div class="frayer-quadrant quad-nonex">
                                <div class="frayer-quad-title">أمثلة غير دالة</div>
                                <p>• القول بأن ق.م.أ للعددين <span class="ar-math">٨</span> و <span class="ar-math">١٢</span> هو <span class="ar-math">٢٤</span> (هذا مضاعف وليس قاسماً).<br>
                                • اختيار قاسم مشترك ليس هو الأكبر كاختيار <span class="ar-math">٢</span> للعددين <span class="ar-math">٨</span> و <span class="ar-math">١٢</span>.</p>
                            </div>
                        </div>
                    </div>

                    <!-- أمثلة الكتاب ص 140 - 142 -->
                    <div class="book-examples-card">
                        <h5>📖 أمثلة الكتاب المعتمدة المحلولة (ص ١٤٠ – ١٤٢):</h5>
                        <div class="solved-example">
                            <div class="ex-label">مثال ١ (ص ١٤١، مثال ٣ من واقع الحياة): أوجد (ق.م.أ) للعددين <span class="ar-math">٥٤</span> و <span class="ar-math">٦٠</span> بالتحليل إلى العوامل الأولية</div>
                            <div class="ex-steps">
                                <strong>خطوات الحل المنظمة:</strong><br>
                                ١) نحلل العدد <span class="ar-math">٥٤</span> إلى عوامل أولية:
                                <div class="ar-math-display">٥٤ = ٢ × ٣ × ٣ × ٣</div>
                                ٢) نحلل العدد <span class="ar-math">٦٠</span> إلى عوامل أولية:
                                <div class="ar-math-display">٦٠ = ٢ × ٢ × ٣ × ٥</div>
                                ٣) نحدد العوامل الأولية المشتركة: يشتركان في عامل واحد من <span class="ar-math">٢</span>، وعامل واحد من <span class="ar-math">٣</span>.<br>
                                ٤) نضرب العوامل المشتركة: <span class="ar-math">٢ × ٣ = ٦</span>.<br>
                                إذن القاسم المشترك الأكبر (ق.م.أ) = <strong>٦</strong>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٢ (ص ١٤٢، مثال ٤ من واقع الحياة - ثلاجة الفطائر): أوجد (ق.م.أ) للأعداد <span class="ar-math">٢٤</span> و <span class="ar-math">٣٢</span> و <span class="ar-math">٤٠</span></div>
                            <div class="ex-steps">
                                <strong>خطوات الحل بالتحليل:</strong><br>
                                • <span class="ar-math">٢٤ = ٢ × ٢ × ٢ × ٣</span><br>
                                • <span class="ar-math">٣٢ = ٢ × ٢ × ٢ × ٢ × ٢</span><br>
                                • <span class="ar-math">٤٠ = ٢ × ٢ × ٢ × ٥</span><br>
                                العوامل الأولية المشتركة بين الأعداد الثلاثة هي: <span class="ar-math">٢ × ٢ × ٢</span>.<br>
                                حاصل ضربها: <span class="ar-math">٢ × ٢ × ٢ = ٨</span>.<br>
                                إذن أكبر عدد من الفطائر في كل صف هو <strong><span class="ar-math">٨</span> فطائر</strong>.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5. التكامل وSTEM -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٥</span> الربط الحياتي ومصفوفة تكامل STEM</h4>
                <div class="stem-grid">
                    <div class="stem-card stem-s">
                        <div class="stem-header">🔬 العلوم</div>
                        <div class="stem-body">تقسيم العينات المخبرية وعينات التربة والصخور من جبال طويق إلى مجموعات متساوية لإجراء التجارب الموازية.</div>
                    </div>
                    <div class="stem-card stem-t">
                        <div class="stem-header">💻 التقنية</div>
                        <div class="stem-body">تشفير البيانات وحساب أطوال مفاتيح التشفير الرقمي (RSA) المعتمدة على الأعداد الأولية والقواسم المشتركة.</div>
                    </div>
                    <div class="stem-card stem-e">
                        <div class="stem-header">🏗️ الهندسة</div>
                        <div class="stem-body">تقطيع ألواح الزجاج والرخام لتكسية واجهات الأبراج دون أي هدر في المواد الخام.</div>
                    </div>
                    <div class="stem-card stem-m">
                        <div class="stem-header">📐 الرياضيات</div>
                        <div class="stem-body">استخدام شجرة العوامل، ونظرية الحساب الأساسية، وقوانين الأسس وقواسم الأعداد.</div>
                    </div>
                </div>
            </div>

            <!-- 6. منظومة التقويم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٦</span> منظومة التقويم المتكاملة</h4>
                <div class="pedagogy-box">
                    <h5>📝 التقويم البنائي:</h5>
                    <div class="formative-q-box">
                        <div class="q-item">
                            <span class="q-badge">سؤال ١:</span> أوجد (ق.م.أ) للعددين <span class="ar-math">١٥</span> و <span class="ar-math">٢٠</span> بطريقة سرد القواسم.
                            <div class="q-ans"><strong>الجواب:</strong> قواسم <span class="ar-math">١٥</span>: {<span class="ar-math">١، ٣، ٥، ١٥</span>}، قواسم <span class="ar-math">٢٠</span>: {<span class="ar-math">١، ٢، ٤، ٥، ١٠، ٢٠</span>}. القواسم المشتركة: {<span class="ar-math">١، ٥</span>}. إذن <strong>ق.م.أ = <span class="ar-math">٥</span></strong>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٢:</span> أوجد (ق.م.أ) للعددين <span class="ar-math">٣٠</span> و <span class="ar-math">٤٥</span> بالتحليل الأولي.
                            <div class="q-ans"><strong>الجواب:</strong> <span class="ar-math">٣٠ = ٢ × ٣ × ٥</span> ، <span class="ar-math">٤٥ = ٣ × ٣ × ٥</span>. المشترك: <span class="ar-math">٣ × ٥ = ١٥</span>. إذن <strong>ق.م.أ = <span class="ar-math">١٥</span></strong>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٣:</span> متى يكون (ق.م.أ) لعددين مساوياً لأحدهما؟ وضح بمثال.
                            <div class="q-ans"><strong>الجواب:</strong> عندما يكون أحد العددين قاسماً للعدد الآخر (أي أن الأكبر مضاعف للأصغر)، مثل العددان <span class="ar-math">٦</span> و <span class="ar-math">١٢</span>؛ ق.م.أ لهما هو <strong><span class="ar-math">٦</span></strong>.</div>
                        </div>
                    </div>

                    <h5>🎯 التقويم الختامي:</h5>
                    <div class="summative-q-box">
                        <p><strong>المسألة:</strong> أرادت جمعية خيرية في مكة المكرمة توزيع <span class="ar-math">٣٦</span> حقيبة مدرسية و <span class="ar-math">٤٨</span> صندوق قرطاسية على عدد من الفصول في مدارس تحفيظ القرآن، بحيث يحصل كل فصل على العدد نفسه تماماً دون باقٍ. ما أكبر عدد من الفصول يمكن أن يستفيد من هذا التوزيع؟</p>
                        <div class="q-ans"><strong>الحل:</strong> المطلوب هو إيجاد ق.م.أ للعددين <span class="ar-math">٣٦</span> و <span class="ar-math">٤٨</span>. بالتحليل: <span class="ar-math">٣٦ = ٢ × ٢ × ٣ × ٣</span>، <span class="ar-math">٤٨ = ٢ × ٢ × ٢ × ٢ × ٣</span>. العوامل المشتركة: <span class="ar-math">٢ × ٢ × ٣ = ١٢</span>. أكبر عدد من الفصول هو <strong><span class="ar-math">١٢</span> فصلاً</strong>، ويحصل كل فصل على ٣ حقائب و ٤ صناديق قرطاسية.</div>
                    </div>

                    <h5>🏠 الواجب المنزلي المعياري:</h5>
                    <div class="homework-box">
                        <p class="hw-question"><strong>سؤال الواجب:</strong> القاسم المشترك الأكبر (ق.م.أ) للعددين <span class="ar-math">١٨</span> و <span class="ar-math">٣٠</span> هو:</p>
                        <div class="hw-options-vertical">
                            <div class="hw-opt">أ) <span class="ar-math">٢</span></div>
                            <div class="hw-opt">ب) <span class="ar-math">٣</span></div>
                            <div class="hw-opt correct-opt">ج) <span class="ar-math">٦</span> (الإجابة الصحيحة)</div>
                            <div class="hw-opt">د) <span class="ar-math">٩</span></div>
                        </div>
                        <div class="hw-solution-note">
                            <strong>التفسير:</strong> قواسم <span class="ar-math">١٨</span> هي: <span class="ar-math">١، ٢، ٣، ٦، ٩، ١٨</span>. قواسم <span class="ar-math">٣٠</span> هي: <span class="ar-math">١، ٢، ٣، ٥، ٦، ١٠، ١٥، ٣٠</span>. القواسم المشتركة هي: <span class="ar-math">١، ٢، ٣، ٦</span>. وأكبرها هو <span class="ar-math">٦</span>.
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. الغلق -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٧</span> الغلق والتحدي الإثرائي</h4>
                <div class="closing-box">
                    <p><strong>غلق الدرس وتأكيد عمود التعلم (L):</strong> يسجل الطلاب: "ق.م.أ يفيدنا في تقسيم الأشياء إلى مجموعات متساوية بأكبر قياس ممكن دون باقٍ".</p>
                    <div class="enrichment-challenge">
                        <strong>🌟 سؤال التحدي للدرس القادم:</strong> «إذا كان ق.م.أ للعددين <span class="ar-math">١٢</span> و <span class="ar-math">١٦</span> هو <span class="ar-math">٤</span>، فكيف نستخدم هذا القاسم لتبسيط الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١٢</span><span class="denom">١٦</span></span></span> وإيجاد كسر مكافئ له في أبسط صورة؟»
                    </div>
                </div>
            </div>
        </article>
"""

PLAN_4 = r"""
        <!-- الخطة الرابعة: استكشاف معمل الرياضيات - الكسور المتكافئة -->
        <article class="unit-card" id="plan-4-lab-equiv-fractions">
            <div class="unit-header">
                <div class="unit-badge">الخطة الدراسية الرابعة (ص ١٤٥ – ١٤٦)</div>
                <h3 class="unit-title">خطة استكشاف معمل الرياضيات: الكسور المتكافئة (استعمال النماذج وأشرطة الكسور)</h3>
                <div class="unit-meta">
                    <span><strong>الصف:</strong> السادس الابتدائي</span> |
                    <span><strong>المادة:</strong> الرياضيات</span> |
                    <span><strong>المجال:</strong> معمل الرياضيات والاستكشاف البصري</span> |
                    <span><strong>الموضوع:</strong> النمذجة الحسية للكسور المتكافئة</span>
                </div>
            </div>

            <!-- 1. الأهداف والمعايير -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">١</span> نواتج التعلم والمعايير المستهدفة (الأهداف SMART)</h4>
                <div class="pedagogy-box">
                    <ul class="smart-goals-list">
                        <li><strong>هدف معرفي:</strong> أن يستنتج الطالب مفهوم الكسور المتكافئة عملياً بأنها كسور تصف الكمية ذاتها من الكل بنسبة إتقان ١٠٠٪.</li>
                        <li><strong>هدف مهاري:</strong> أن ينشئ الطالب كسوراً متكافئة باستخدام أشرطة الكسور ونماذج المساحة، ويستنتج قاعدة الضرب وقاعدة القسمة للتكافؤ بدقة متناهية.</li>
                        <li><strong>هدف وجداني:</strong> أن ينمي الطالب مهارات التفكير البصري والعمل اليدوي الاستكشافي وروح الفريق في معمل الرياضيات.</li>
                    </ul>
                </div>
            </div>

            <!-- 2. الانخراط والتركيز -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٢</span> مرحلة الانخراط والتركيز (Engage & Focus)</h4>
                <div class="pedagogy-box">
                    <div class="briefcase-box">
                        <div class="briefcase-title">💼 الحقيبة التعليمية المحفزة:</div>
                        <p>«إذا طلبت أسرة فطيرتي بيتزا متطابقتين تماماً في الحجم، وقُطعت الأولى إلى نصفين فأكل ماجد نصفاً (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>)، بينما قُطعت الثانية إلى <span class="ar-math">٤</span> أرباع متساوية فأكلت سارة ربعين (<span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٤</span></span></span>). هل أكل أحدهما أكثر من الآخر؟ وكيف تثبت للمشاهد بالنماذج الحسية أنهما أكلا المقدار نفسه بالضبط؟»</p>
                    </div>

                    <div class="intro-activity-box">
                        <h5>🎯 التمهيد التفاعلي وتقويم تشخيصي سريع:</h5>
                        <p><strong>نشاط "تطابق الأشرطة الملونة":</strong> يأخذ كل طالب شريطاً يمثل الواحد الصحيح، وشريطين يمثل كل منهما النصف، ويضعهما متطابقين ليتحقق بصرياً من تطابق الأطوال.</p>
                        <table class="standard-table">
                            <thead>
                                <tr>
                                    <th>السؤال التشخيصي</th>
                                    <th>المهارة المستهدفة</th>
                                    <th>الإجابة المتوقعة</th>
                                    <th>العلاج السريع</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>كم ربعاً في النصف الواحد؟ (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span> = <span class="ar-frac"><span class="num">؟</span><span class="denom">٤</span></span></span>)</td>
                                    <td>تطابق الأجزاء بالنماذج</td>
                                    <td>ربعان (<span class="ar-math">٢</span>)</td>
                                    <td>مطابقة قطعتي ربع فوق شريط النصف في المعمل.</td>
                                </tr>
                                <tr>
                                    <td>إذا ضربنا بسط كسر في <span class="ar-math">٣</span>، فبماذا يجب ضرب مقامه ليبقى الكسر نفسه؟</td>
                                    <td>إدراك مبدأ التوازن الرياضي</td>
                                    <td>نضرب المقام في <span class="ar-math">٣</span> أيضاً.</td>
                                    <td>التأكيد على أن ضرب البسط والمقام في نفس العدد كالضرب في الواحد الصحيح.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- KWL -->
                    <div class="kwl-table-wrapper">
                        <h5>📊 جدول التعلم الذاتي (KWL Table):</h5>
                        <table class="standard-table kwl-table">
                            <thead>
                                <tr>
                                    <th>ماذا أعرف؟ (K)</th>
                                    <th>ماذا أريد أن أعرف؟ (W)</th>
                                    <th>ماذا تعلمت؟ (L)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        • قراءة وكتابة الكسور بالنماذج.<br>
                                        • الكسور تصف أجزاء من الكل.
                                    </td>
                                    <td>
                                        • كيف تثبت أشرطة الكسور تكافؤ كسرين بصرياً؟<br>
                                        • كيف نولد كسوراً مكافئة بدون استخدام النماذج؟<br>
                                        • ما العلاقة بين التكافؤ وعملية التبسيط؟
                                    </td>
                                    <td>
                                        <span class="l-column-highlight">
                                        (يُستكمل في الغلق):<br>
                                        • ضرب أو قسمة البسط والمقام على نفس العدد لا يغير قيمة الكسر بل يجزئ أجزاءه.<br>
                                        • تجميع الأجزاء الصغيرة المتطابقة يسمى تبسيط الكسر.
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٣</span> بيئة التعلم والقواعد الصفية</h4>
                <div class="rules-flex-container">
                    <div class="rule-card">
                        <div class="rule-icon">🧩</div>
                        <div class="rule-title">المحافظة على أدوات المعمل</div>
                        <div class="rule-desc">الحفاظ على أشرطة الكسور البلاستيكية والورقية وإعادتها لمغلفاتها بعد انتهاء النشاط الاستكشافي.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">👥</div>
                        <div class="rule-title">التناوب في التجريب اليدوي</div>
                        <div class="rule-desc">يتناوب أعضاء المجموعة في تركيب الأشرطة وكتابة الكسر المكافئ المقابل على اللوح الأبيض المصغر.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">📏</div>
                        <div class="rule-title">المحاذاة الرأسية الدقيقة</div>
                        <div class="rule-desc">محاذاة حواف أشرطة الكسور من الطرف الأيمن لضمان قياس التكافؤ بموضوعية تامة.</div>
                    </div>
                </div>
            </div>

            <!-- 4. استراتيجيات التدريس النشط -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٤</span> الاستراتيجيات النشطة والتنفيذ الإجرائي</h4>
                <div class="pedagogy-box">
                    <div class="strategies-tag-cloud">
                        <span class="strat-pill">الاستكشاف الموجه بالمعمل</span>
                        <span class="strat-pill">النمذجة بأشرطة الكسور</span>
                        <span class="strat-pill">فكر - زاوج - شارك</span>
                        <span class="strat-pill">مربع فرير للكسور المتكافئة</span>
                    </div>

                    <div class="tree-map-card">
                        <h5>🌳 الخريطة الشجرية لاستنتاجات معمل الكسور المتكافئة:</h5>
                        <div class="tree-content">
                            <strong>الكسور المتكافئة (Equivalent Fractions):</strong>
                            <ul>
                                <li><strong>المفهوم البصري:</strong> كسور لها أطوال أو مساحات مظللة متطابقة تماماً من الكل نفسه.</li>
                                <li><strong>طريقة التوليد بالضرب (تجزئة الأجزاء):</strong> نضرب البسط والمقام في العدد نفسه غير الصفر:
                                    <div class="ar-math-display"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٢ × ٣</span><span class="denom">٣ × ٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></div>
                                </li>
                                <li><strong>طريقة التوليد بالقسمة (تجميع الأجزاء - التبسيط):</strong> نقسم البسط والمقام على قاسم مشترك غير الصفر:
                                    <div class="ar-math-display"><span class="ar-frac"><span class="num">٦</span><span class="denom">٨</span></span> = <span class="ar-frac"><span class="num">٦ ÷ ٢</span><span class="denom">٨ ÷ ٢</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></div>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="frayer-model-card">
                        <h5>🔲 نموذج فرير لمفهوم "الكسور المتكافئة":</h5>
                        <div class="frayer-grid">
                            <div class="frayer-quadrant quad-def">
                                <div class="frayer-quad-title">التعريف الرياضي</div>
                                <p>هي الكسور التي تسمي الكمية أو المقدار نفسه، ولها القيمة ذاتها على خط الأعداد رغم اختلاف أرقام بسوطها ومقاماتها.</p>
                            </div>
                            <div class="frayer-quadrant quad-char">
                                <div class="frayer-quad-title">الخصائص الأساسية</div>
                                <p>• حاصل ضرب طرفيها يساوي حاصل ضرب وسطيها (الضرب التبادلي متساوٍ).<br>
                                • تنتج من ضرب أو قسمة حدي الكسر على نفس العدد غير الصفر.<br>
                                • تمثل النقطة نفسها تماماً على خط الأعداد.</p>
                            </div>
                            <div class="frayer-quadrant quad-ex">
                                <div class="frayer-quad-title">أمثلة دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">٤</span><span class="denom">٨</span></span></span><br>
                                • <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span><br>
                                • <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">١٠</span></span></span></p>
                            </div>
                            <div class="frayer-quadrant quad-nonex">
                                <div class="frayer-quad-title">أمثلة غير دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span> (ليسا متكافئين؛ كميتان مختلفتان).<br>
                                • جمع عدد للبسط والمقام: <span class="ar-math"><span class="ar-frac"><span class="num">١+٢</span><span class="denom">٣+٢</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span> ≠ <span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span> (الجمع لا يعطي تكافؤاً).</p>
                            </div>
                        </div>
                    </div>

                    <!-- أنشطة الكتاب ص 145 - 146 -->
                    <div class="book-examples-card">
                        <h5>📖 أنشطة المعمل المحلولة بالتفصيل (ص ١٤٥ – ١٤٦):</h5>
                        <div class="solved-example">
                            <div class="ex-label">نشاط ١ (ص ١٤٥): أوجد كسرين مكافئين للكسر <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span> باستعمال أشرطة الكسور</div>
                            <div class="ex-steps">
                                <strong>الخطوات العملية بالمعمل:</strong><br>
                                ١) نضع شريطين يمثل كل منهما <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span> بجانب بعضهما، ليمثلا معاً الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>.<br>
                                ٢) نبحث عن أشرطة الأسداس (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٦</span></span></span>) التي تطابق هذا الطول: نجد أن <span class="ar-math">٤</span> أسداس تطابق تماماً ثلثين، إذن <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span></span>.<br>
                                ٣) نبحث عن أشرطة الأتساع (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٩</span></span></span>): نجد أن <span class="ar-math">٦</span> أتساع تطابق الطول نفسه تماماً، إذن <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span>.<br>
                                <strong>الاستنتاج الحسابي:</strong> نلاحظ أن <span class="ar-math"><span class="ar-frac"><span class="num">٢ × ٢</span><span class="denom">٣ × ٢</span></span> = <span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span></span> ، و <span class="ar-math"><span class="ar-frac"><span class="num">٢ × ٣</span><span class="denom">٣ × ٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">نشاط ٢ (تحليل النتائج ص ١٤٦، سؤال ٨): استعمل نماذج الكسور لتحدد ما إذا كان الكسران <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٦</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٨</span></span></span> متكافئين أم لا؟</div>
                            <div class="ex-steps">
                                <strong>طريقة التحليل بالمعمل:</strong><br>
                                • شريط <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٦</span></span></span> يطابق بالضبط شريط النصف (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>).<br>
                                • شريط <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٨</span></span></span> يطابق أيضاً بالضبط شريط النصف (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>).<br>
                                وبما أن كلا الكسرين يكافئان <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>، فإن <strong>الكسرين متكافئان</strong>، وعملية التجزئة هذه تسمى <strong>تبسيط الكسر</strong>.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5. التكامل وSTEM -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٥</span> الربط الحياتي ومصفوفة تكامل STEM</h4>
                <div class="stem-grid">
                    <div class="stem-card stem-s">
                        <div class="stem-header">🔬 العلوم</div>
                        <div class="stem-body">تخفيف وتركيز المحاليل: إضافة مقدارين متكافئين من المذيب يحافظ على نفس نسبة التركيز الكيميائي.</div>
                    </div>
                    <div class="stem-card stem-t">
                        <div class="stem-header">💻 التقنية</div>
                        <div class="stem-body">تغيير دقة شاشات العرض (Resolution): عرض صورة بأبعاد ٤K أو Full HD مع الحفاظ على النسبة الباعية المتكافئة (١٦:٩).</div>
                    </div>
                    <div class="stem-card stem-e">
                        <div class="stem-header">🏗️ الهندسة</div>
                        <div class="stem-body">رسم المخططات الهندسية بمقاييس رسم متكافئة (كل ١ سم على المخطط يكافئ ٢ متر على أرض الواقع).</div>
                    </div>
                    <div class="stem-card stem-m">
                        <div class="stem-header">📐 الرياضيات</div>
                        <div class="stem-body">قواعد التكافؤ بالضرب والقسمة وخاصية التناسب والضرب التبادلي والتحويلات الكسرية.</div>
                    </div>
                </div>
            </div>

            <!-- 6. منظومة التقويم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٦</span> منظومة التقويم المتكاملة</h4>
                <div class="pedagogy-box">
                    <h5>📝 التقويم البنائي:</h5>
                    <div class="formative-q-box">
                        <div class="q-item">
                            <span class="q-badge">سؤال ١:</span> أوجد كسراً مكافئاً للكسر <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span></span> يكون مقامه <span class="ar-math">٢٠</span>.
                            <div class="q-ans"><strong>الجواب:</strong> بما أن المقام ضرب في <span class="ar-math">٤</span> (<span class="ar-math">٥ × ٤ = ٢٠</span>)، نضرب البسط في <span class="ar-math">٤</span> (<span class="ar-math">٣ × ٤ = ١٢</span>). الكسر هو: <strong><span class="ar-math"><span class="ar-frac"><span class="num">١٢</span><span class="denom">٢٠</span></span></span></strong>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٢:</span> هل الكسران <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٧</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٢١</span></span></span> متكافئان؟ وضح كيف عرفت ذلك.
                            <div class="q-ans"><strong>الجواب:</strong> نعم متكافئان؛ لأن ضرب كل من بسط ومقام <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٧</span></span></span> في <span class="ar-math">٣</span> يعطي <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٢١</span></span></span>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٣:</span> كسر يكافئ <span class="ar-math"><span class="ar-frac"><span class="num">١٠</span><span class="denom">١٥</span></span></span> وبسطه <span class="ar-math">٢</span>، فما هو مقامه؟
                            <div class="q-ans"><strong>الجواب:</strong> قسمنا البسط على <span class="ar-math">٥</span> (<span class="ar-math">١٠ ÷ ٥ = ٢</span>)، فنقسم المقام على <span class="ar-math">٥</span> (<span class="ar-math">١٥ ÷ ٥ = ٣</span>). الكسر هو <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>، إذن مقامه هو <strong><span class="ar-math">٣</span></strong>.</div>
                        </div>
                    </div>

                    <h5>🎯 التقويم الختامي:</h5>
                    <div class="summative-q-box">
                        <p><strong>المسألة:</strong> لدى مزارع في واحة الأحساء حقل نخيل، استصلح منه <span class="ar-math"><span class="ar-frac"><span class="num">٨</span><span class="denom">١٢</span></span></span>. اكتب كسرين مكافئين لهذا الكسر، أحدهما بالضرب والآخر بالقسمة، ومثلهما على خط الأعداد.</p>
                        <div class="q-ans"><strong>الحل:</strong> بالقسمة: بقسمة البسط والمقام على <span class="ar-math">٤</span> نحصل على <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>. بالضرب: بضرب البسط والمقام في <span class="ar-math">٢</span> نحصل على <span class="ar-math"><span class="ar-frac"><span class="num">١٦</span><span class="denom">٢٤</span></span></span>. وجميعها تمثل نفس المسافة والنقطة على خط الأعداد.</div>
                    </div>

                    <h5>🏠 الواجب المنزلي المعياري:</h5>
                    <div class="homework-box">
                        <p class="hw-question"><strong>سؤال الواجب:</strong> العدد المناسب في المربع ليصبح الكسران متكافئين: <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٧</span></span> = <span class="ar-frac"><span class="num">؟</span><span class="denom">٢٨</span></span></span> هو:</p>
                        <div class="hw-options-vertical">
                            <div class="hw-opt">أ) <span class="ar-math">١٢</span></div>
                            <div class="hw-opt correct-opt">ب) <span class="ar-math">١٦</span> (الإجابة الصحيحة)</div>
                            <div class="hw-opt">ج) <span class="ar-math">٢٠</span></div>
                            <div class="hw-opt">د) <span class="ar-math">٢٤</span></div>
                        </div>
                        <div class="hw-solution-note">
                            <strong>التفسير:</strong> لمضاعفة المقام من <span class="ar-math">٧</span> إلى <span class="ar-math">٢٨</span> ضربنا في <span class="ar-math">٤</span>. إذن نضرب البسط <span class="ar-math">٤</span> في <span class="ar-math">٤</span> فيكون الناتج <span class="ar-math">١٦</span>.
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. الغلق -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٧</span> الغلق والتحدي الإثرائي</h4>
                <div class="closing-box">
                    <p><strong>غلق الدرس وتأكيد عمود التعلم (L):</strong> يلخص الطلاب: "الكسور المتكافئة تتولد بضرب أو قسمة حدي الكسر على نفس العدد، وقسمتهما على القاسم المشترك تعطي أبسط صورة".</p>
                    <div class="enrichment-challenge">
                        <strong>🌟 سؤال التحدي للدرس القادم:</strong> «إذا كان لديك كسر كبير مثل <span class="ar-math"><span class="ar-frac"><span class="num">٢٤</span><span class="denom">٣٦</span></span></span>، فما هو أكبر عدد يمكنك قسمة البسط والمقام عليه مرة واحدة لتبسيطه إلى أبسط صورة في خطوة واحدة فقط؟»
                    </div>
                </div>
            </div>
        </article>
"""

PLAN_5 = r"""
        <!-- الخطة الخامسة: الدرس (٤-٢) تبسيط الكسور الاعتيادية ومعمل الأعداد الكسرية والكسور غير الفعلية -->
        <article class="unit-card" id="plan-5-lesson4-2-simplifying">
            <div class="unit-header">
                <div class="unit-badge">الخطة الدراسية الخامسة (ص ١٤٧ – ١٥١)</div>
                <h3 class="unit-title">خطة الدرس (٤-٢): تبسيط الكسور الاعتيادية ومعمل الأعداد الكسرية والكسور غير الفعلية</h3>
                <div class="unit-meta">
                    <span><strong>الصف:</strong> السادس الابتدائي</span> |
                    <span><strong>المادة:</strong> الرياضيات</span> |
                    <span><strong>المجال:</strong> الأعداد والعمليات عليها</span> |
                    <span><strong>موضوع الدرس:</strong> كتابة الكسور في أبسط صورة والربط بالنماذج</span>
                </div>
            </div>

            <!-- 1. الأهداف والمعايير -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">١</span> نواتج التعلم والمعايير المستهدفة (الأهداف SMART)</h4>
                <div class="pedagogy-box">
                    <ul class="smart-goals-list">
                        <li><strong>هدف معرفي:</strong> أن يعرف الطالب متى يكون الكسر في أبسط صورة (ق.م.أ لبسطه ومقامه هو ١)، ويميز بين الكسر الفعلي والكسر غير الفعلي والعدد الكسري بدقة ١٠٠٪.</li>
                        <li><strong>هدف مهاري:</strong> أن يبسط الطالب الكسور الاعتيادية بقسمة البسط والمقام على (ق.م.أ)، ويمثل الكسور غير الفعلية والأعداد الكسرية بالنماذج بنجاح تام.</li>
                        <li><strong>هدف وجداني:</strong> أن يقدّر الطالب قيمة التبسيط والوضوح في عرض البيانات الإحصائية والتقارير الرياضية في الحياة اليومية.</li>
                    </ul>
                </div>
            </div>

            <!-- 2. الانخراط والتركيز -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٢</span> مرحلة الانخراط والتركيز (Engage & Focus)</h4>
                <div class="pedagogy-box">
                    <div class="briefcase-box">
                        <div class="briefcase-title">💼 الحقيبة التعليمية المحفزة:</div>
                        <p>«في دراسة إحصائية بيئية أجريت في محمية الوعول بالمملكة، وجد الباحثون أن <span class="ar-math">١٨</span> طائراً من أصل <span class="ar-math">٢٤</span> طائراً تم رصدها هي من طيور الحمام القمري النادر. كيف يعبر الباحث عن هذه النسبة بكسر في أبسط صورة ممكنة ليسهل نشرها في التقرير العلمي الدولي؟ وماذا لو كان عدد الطيور المرصودة <span class="ar-math">٣٠</span> من سعة المحمية <span class="ar-math">٢٤</span> (كسر غير فعلي ص ١٥١)؟»</p>
                    </div>

                    <div class="intro-activity-box">
                        <h5>🎯 التمهيد التفاعلي وتقويم تشخيصي سريع:</h5>
                        <p><strong>نشاط "تحدي الاختزال السريع":</strong> بطاقات تعرض كسوراً، ويحدد الطلاب هل الكسر في أبسط صورة برفع الإشارة الخضراء أو يحتاج لتبسيط برفع الإشارة الصفراء.</p>
                        <table class="standard-table">
                            <thead>
                                <tr>
                                    <th>السؤال التشخيصي</th>
                                    <th>المهارة المستهدفة</th>
                                    <th>الإجابة المتوقعة</th>
                                    <th>العلاج السريع</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>هل الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٧</span></span></span> في أبسط صورة؟ ولماذا؟</td>
                                    <td>فهم مفهوم أبسط صورة</td>
                                    <td>نعم، لأن ق.م.أ للعددين <span class="ar-math">٣</span> و <span class="ar-math">٧</span> هو <span class="ar-math">١</span>.</td>
                                    <td>التأكيد على أنه إذا كان العددان أوليين فإن الكسر في أبسط صورة حتماً.</td>
                                </tr>
                                <tr>
                                    <td>أوجد (ق.م.أ) للعددين <span class="ar-math">١٢</span> و <span class="ar-math">١٦</span></td>
                                    <td>ربط التبسيط بـ (ق.م.أ)</td>
                                    <td><span class="ar-math">٤</span></td>
                                    <td>مراجعة درس ق.م.أ لاستخدامه المباشر في خطوة التبسيط.</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- KWL -->
                    <div class="kwl-table-wrapper">
                        <h5>📊 جدول التعلم الذاتي (KWL Table):</h5>
                        <table class="standard-table kwl-table">
                            <thead>
                                <tr>
                                    <th>ماذا أعرف؟ (K)</th>
                                    <th>ماذا أريد أن أعرف؟ (W)</th>
                                    <th>ماذا تعلمت؟ (L)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        • إيجاد القاسم المشترك الأكبر (ق.م.أ).<br>
                                        • مفهوم الكسور المتكافئة بالقسمة.
                                    </td>
                                    <td>
                                        • متى يقال تحديداً أن الكسر في أبسط صورة؟<br>
                                        • كيف نبسط الكسر في خطوة واحدة بدلاً من عدة خطوات؟<br>
                                        • ما الفرق بين الكسر الفعلي والكسر غير الفعلي والعدد الكسري (ص ١٥١)؟
                                    </td>
                                    <td>
                                        <span class="l-column-highlight">
                                        (يُستكمل في الغلق):<br>
                                        • الكسر يكون في أبسط صورة إذا كان ق.م.أ للبسط والمقام = ١.<br>
                                        • الكسر غير الفعلي بسطه <span class="ar-math">≥</span> مقامه، والعدد الكسري يتكون من عدد كلي وكسر اعتيادي.
                                        </span>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٣</span> بيئة التعلم والقواعد الصفية</h4>
                <div class="rules-flex-container">
                    <div class="rule-card">
                        <div class="rule-icon">⚡</div>
                        <div class="rule-title">التبسيط المباشر بخطوة واحدة</div>
                        <div class="rule-desc">البحث دائماً عن (ق.م.أ) للقسمة عليه مباشرة وتوفير الوقت والجهد الحسابي.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">📐</div>
                        <div class="rule-title">التثبت من ناتج التبسيط</div>
                        <div class="rule-desc">فحص الكسر الناتج للتأكد من عدم وجود أي قاسم مشترك آخر بين البسط والمقام غير الواحد.</div>
                    </div>
                    <div class="rule-card">
                        <div class="rule-icon">🤝</div>
                        <div class="rule-title">المشاركة التعاونية المتبادلة</div>
                        <div class="rule-desc">طالب يقوم بإيجاد (ق.م.أ) وزميله ينفذ عملية القسمة والتبسيط ثم يتبادلان الأدوار.</div>
                    </div>
                </div>
            </div>

            <!-- 4. استراتيجيات التدريس النشط -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٤</span> الاستراتيجيات النشطة والتنفيذ الإجرائي</h4>
                <div class="pedagogy-box">
                    <div class="strategies-tag-cloud">
                        <span class="strat-pill">القسمة على (ق.م.أ)</span>
                        <span class="strat-pill">فكر - زاوج - شارك</span>
                        <span class="strat-pill">خريطة مفاهيم تصنيف الكسور</span>
                        <span class="strat-pill">مربع فرير لمفهوم "أبسط صورة"</span>
                    </div>

                    <div class="tree-map-card">
                        <h5>🌳 الخريطة الشجرية لتبسيط الكسور وتصنيفها (ص ١٤٧ – ١٥١):</h5>
                        <div class="tree-content">
                            <strong>الكسور الاعتيادية وتبسيطها:</strong>
                            <ul>
                                <li><strong>تبسيط الكسور:</strong> قسمة البسط والمقام على قاسمهما المشترك الأكبر (ق.م.أ) للوصول إلى كسر مكافئ لا يمكن تبسيطه أكثر.</li>
                                <li><strong>أنواع الكسور (معمل ص ١٥١):</strong>
                                    <ul>
                                        <li><strong>كسر فعلي:</strong> بسطه أصغر من مقامه، وقيمته أقل من الواحد الصحيح (مثل: <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>).</li>
                                        <li><strong>كسر غير فعلي:</strong> بسطه أكبر من أو يساوي مقامه، وقيمته أكبر من أو تساوي الواحد الصحيح (مثل: <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٤</span></span></span>).</li>
                                        <li><strong>عدد كسري:</strong> يتكون من عدد كلي وبجانبه كسر اعتيادي (مثل: <span class="ar-math">١ <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span>).</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="frayer-model-card">
                        <h5>🔲 نموذج فرير لمفهوم "الكسر في أبسط صورة":</h5>
                        <div class="frayer-grid">
                            <div class="frayer-quadrant quad-def">
                                <div class="frayer-quad-title">التعريف الرياضي</div>
                                <p>حالة الكسر الاعتيادي التي يكون فيها القاسم المشترك الأكبر (ق.م.أ) لبسطه ومقامه هو العدد <span class="ar-math">١</span> فقط.</p>
                            </div>
                            <div class="frayer-quadrant quad-char">
                                <div class="frayer-quad-title">الخصائص الأساسية</div>
                                <p>• لا توجد عوامل مشتركة بين البسط والمقام سوى الواحد.<br>
                                • يمثل التعبير الأكثر إيجازاً ودقة للكمية المجزأة.<br>
                                • الكسر الناتج يكافئ الكسر الأصلي تماماً في القيمة.</p>
                            </div>
                            <div class="frayer-quadrant quad-ex">
                                <div class="frayer-quad-title">أمثلة دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span> (ق.م.أ للعددين ٣ و ٤ هو ١).<br>
                                • <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٥</span></span></span>، <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٦</span></span></span>، <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">١٠</span></span></span></p>
                            </div>
                            <div class="frayer-quadrant quad-nonex">
                                <div class="frayer-quad-title">أمثلة غير دالة</div>
                                <p>• <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٨</span></span></span> (ليس في أبسط صورة لأن كلاً من ٦ و ٨ يقبل القسمة على ٢).<br>
                                • <span class="ar-math"><span class="ar-frac"><span class="num">١٥</span><span class="denom">٢٠</span></span></span> (يقبلان القسمة على ٥).</p>
                            </div>
                        </div>
                    </div>

                    <!-- أمثلة الكتاب المحلولة ص 147 - 150 ومعمل 151 -->
                    <div class="book-examples-card">
                        <h5>📖 أمثلة الكتاب المعتمدة المحلولة (ص ١٤٧ – ١٥١):</h5>
                        <div class="solved-example">
                            <div class="ex-label">مثال ١ (ص ١٤٨، مثال ٢): اكتب الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١٨</span><span class="denom">٢٤</span></span></span> في أبسط صورة</div>
                            <div class="ex-steps">
                                <strong>خطوات الحل المنظمة:</strong><br>
                                ١) نجد (ق.م.أ) للبسط (<span class="ar-math">١٨</span>) والمقام (<span class="ar-math">٢٤</span>):<br>
                                • قواسم <span class="ar-math">١٨</span>: <span class="ar-math">١ ، ٢ ، ٣ ، ٦ ، ٩ ، ١٨</span><br>
                                • قواسم <span class="ar-math">٢٤</span>: <span class="ar-math">١ ، ٢ , ٣ ، ٤ ، ٦ ، ٨ ، ١٢ ، ٢٤</span><br>
                                • أكبر قاسم مشترك هو <span class="ar-math">٦</span>.<br>
                                ٢) نقسم كلاً من البسط والمقام على <span class="ar-math">٦</span>:
                                <div class="ar-math-display"><span class="ar-frac"><span class="num">١٨ ÷ ٦</span><span class="denom">٢٤ ÷ ٦</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></div>
                                ٣) نتحقق: قواسم <span class="ar-math">٣</span> و <span class="ar-math">٤</span> المشتركة هي <span class="ar-math">١</span> فقط. إذن الكسر في أبسط صورة هو <strong><span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span></strong>.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٢ (ص ١٤٨، مثال ٣ من واقع الحياة - طيور): في حديقة <span class="ar-math">٢١</span> طائر حسون من بين <span class="ar-math">٣٥</span> طائراً. اكتب الكسر في أبسط صورة</div>
                            <div class="ex-steps">
                                <strong>خطوات الحل:</strong><br>
                                ١) الكسر الأصلي يمثل نسبة طيور الحسون: <span class="ar-math"><span class="ar-frac"><span class="num">٢١</span><span class="denom">٣٥</span></span></span>.<br>
                                ٢) نلاحظ أن كلاً من <span class="ar-math">٢١</span> و <span class="ar-math">٣٥</span> يقبل القسمة على <span class="ar-math">٧</span> (حيث ق.م.أ لهما هو <span class="ar-math">٧</span>).<br>
                                ٣) نقسم حدي الكسر على <span class="ar-math">٧</span>:
                                <div class="ar-math-display"><span class="ar-frac"><span class="num">٢١ ÷ ٧</span><span class="denom">٣٥ ÷ ٧</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span></div>
                                إذن طيور الحسون تمثل <strong><span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span></span></strong> من طيور الحديقة.
                            </div>
                        </div>

                        <div class="solved-example">
                            <div class="ex-label">مثال ٣ (معمل الرياضيات ص ١٥١): أنشئ نموذجاً يمثل العدد الكسري <span class="ar-math">١ <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span> واكتبه على صورة كسر غير فعلي</div>
                            <div class="ex-steps">
                                <strong>خطوات النمذجة والحل:</strong><br>
                                ١) نمثل الواحد الصحيح بـ <span class="ar-math">٤</span> أرباع كاملة (<span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٤</span></span></span>).<br>
                                ٢) نضيف ربعاً إضافياً (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span>).<br>
                                ٣) نجمع عدد الأرباع: <span class="ar-math">٤ + ١ = ٥</span> أرباع.<br>
                                ٤) الكسر غير الفعلي هو: <strong><span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٤</span></span></span></strong>.
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 5. التكامل وSTEM -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٥</span> الربط الحياتي ومصفوفة تكامل STEM</h4>
                <div class="stem-grid">
                    <div class="stem-card stem-s">
                        <div class="stem-header">🔬 العلوم</div>
                        <div class="stem-body">كتابة نسب العناصر في المركبات الكيميائية بأبسط صيغة جزيئية وأولية معتمدة دولياً.</div>
                    </div>
                    <div class="stem-card stem-t">
                        <div class="stem-header">💻 التقنية</div>
                        <div class="stem-body">ضغط الملفات الرقمية وتقليص حجم الصور (Compression) مع الحفاظ على نقاء الألوان وتناسق الأبعاد.</div>
                    </div>
                    <div class="stem-card stem-e">
                        <div class="stem-header">🏗️ الهندسة</div>
                        <div class="stem-body">تحديد نسب الخلطات الخرسانية (إسمنت : رمل : بحص) بأبسط صورة وفق كود البناء السعودي.</div>
                    </div>
                    <div class="stem-card stem-m">
                        <div class="stem-header">📐 الرياضيات</div>
                        <div class="stem-body">توظيف خوارزميات القسمة وتطبيق (ق.م.أ) والتحويل بين الكسور الفعلية وغير الفعلية والأعداد الكسرية.</div>
                    </div>
                </div>
            </div>

            <!-- 6. منظومة التقويم -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٦</span> منظومة التقويم المتكاملة</h4>
                <div class="pedagogy-box">
                    <h5>📝 التقويم البنائي:</h5>
                    <div class="formative-q-box">
                        <div class="q-item">
                            <span class="q-badge">سؤال ١:</span> اكتب الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٨</span><span class="denom">١٢</span></span></span> في أبسط صورة.
                            <div class="q-ans"><strong>الجواب:</strong> ق.م.أ للبسط والمقام هو <span class="ar-math">٤</span>. بالقسمة على <span class="ar-math">٤</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٨ ÷ ٤</span><span class="denom">١٢ ÷ ٤</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٢:</span> اكتب الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١٥</span><span class="denom">٤٥</span></span></span> في أبسط صورة بخطوة واحدة.
                            <div class="q-ans"><strong>الجواب:</strong> ق.م.أ للعددين هو <span class="ar-math">١٥</span>. بالقسمة على <span class="ar-math">١٥</span>: <span class="ar-math"><span class="ar-frac"><span class="num">١٥ ÷ ١٥</span><span class="denom">٤٥ ÷ ١٥</span></span> = <span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span>.</div>
                        </div>
                        <div class="q-item">
                            <span class="q-badge">سؤال ٣ (ص ١٥١):</span> صنف الكسر التالي إلى فعلي أو غير فعلي أو عدد كسري: <span class="ar-math"><span class="ar-frac"><span class="num">١١</span><span class="denom">٧</span></span></span>.
                            <div class="q-ans"><strong>الجواب:</strong> هو <strong>كسر غير فعلي</strong>؛ لأن بسطه (<span class="ar-math">١١</span>) أكبر من مقامه (<span class="ar-math">٧</span>).</div>
                        </div>
                    </div>

                    <h5>🎯 التقويم الختامي:</h5>
                    <div class="summative-q-box">
                        <p><strong>المسألة:</strong> أمضى فيصل <span class="ar-math">٤٠</span> دقيقة في ممارسة رياضة المشي على واجهة جدة البحرية. ما الكسر الاعتيادي في أبسط صورة الذي يمثل هذا الوقت من الساعة الكاملة (<span class="ar-math">٦٠</span> دقيقة)؟</p>
                        <div class="q-ans"><strong>الحل:</strong> الكسر هو <span class="ar-math"><span class="ar-frac"><span class="num">٤٠</span><span class="denom">٦٠</span></span></span>. ق.م.أ للعددين <span class="ar-math">٤٠</span> و <span class="ar-math">٦٠</span> هو <span class="ar-math">٢٠</span>. بقسمة البسط والمقام على <span class="ar-math">٢٠</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٤٠ ÷ ٢٠</span><span class="denom">٦٠ ÷ ٢٠</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>. إذن أمضى فيصل <strong><span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span> الساعة</strong> (ثلثي الساعة).</div>
                    </div>

                    <h5>🏠 الواجب المنزلي المعياري:</h5>
                    <div class="homework-box">
                        <p class="hw-question"><strong>سؤال الواجب:</strong> الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٢٤</span><span class="denom">٣٢</span></span></span> مكتوباً في أبسط صورة هو:</p>
                        <div class="hw-options-vertical">
                            <div class="hw-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">١٢</span><span class="denom">١٦</span></span></span></div>
                            <div class="hw-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٨</span></span></span></div>
                            <div class="hw-opt correct-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span> (الإجابة الصحيحة)</div>
                            <div class="hw-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span></div>
                        </div>
                        <div class="hw-solution-note">
                            <strong>التفسير:</strong> ق.م.أ للعددين <span class="ar-math">٢٤</span> و <span class="ar-math">٣٢</span> هو <span class="ar-math">٨</span>. بقسمة البسط والمقام على <span class="ar-math">٨</span>: <span class="ar-math">٢٤÷٨ = ٣</span> و <span class="ar-math">٣٢÷٨ = ٤</span>، فنحصل على <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>. أما الخياران (أ) و (ب) فهما كسران مكافئان ولكنهما ليسا في أبسط صورة.
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. الغلق -->
            <div class="plan-subblock">
                <h4 class="subblock-title"><span class="badge-num">٧</span> الغلق والتحدي الإثرائي</h4>
                <div class="closing-box">
                    <p><strong>غلق الدرس وتأكيد عمود التعلم (L):</strong> يسجل الطلاب: "تبسيط الكسر يتم بقسمة حدي الكسر على (ق.م.أ)، والكسر الناتج يكون مكافئاً له تماماً لكن بأبسط الأرقام".</p>
                    <div class="enrichment-challenge">
                        <strong>🌟 سؤال التحدي للدرس القادم:</strong> «إذا كان لديك الكسر غير الفعلي <span class="ar-math"><span class="ar-frac"><span class="num">١٣</span><span class="denom">٤</span></span></span>، فكيف تحوله بالقسمة المطولة إلى عدد كسري يتكون من عدد كلي وكسر اعتيادي في أبسط صورة؟»
                    </div>
                </div>
            </div>
        </article>
"""

PLANS_SECTION_END = r"""
    </section><!-- /#section-plans -->
"""

full_plans_html = b.PLANS_SECTION_START + b.PLAN_1 + PLAN_2 + PLAN_3 + PLAN_4 + PLAN_5 + PLANS_SECTION_END

with open('section_6b_plans.html', 'w', encoding='utf-8') as f:
    f.write(full_plans_html)

print(f"section_6b_plans.html written successfully! Total length: {len(full_plans_html)} chars.")
