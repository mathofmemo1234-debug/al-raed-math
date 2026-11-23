# -*- coding: utf-8 -*-
"""
generator_6b_summaries.py: Student Summaries for Grade 6 Elementary (6ب) pages 135 to 151:
- Summary 1 (pp. 135-137): مراجعة واختبار الفصل ٣ والاختبار التراكمي (العمليات على الكسور العشرية)
- Summary 2 (pp. 138-139): تهيئة الفصل ٤ (الكسور الاعتيادية والكسور العشرية)
- Summary 3 (pp. 140-144): الدرس (٤-١): القاسم المشترك الأكبر (ق.م.أ)
- Summary 4 (pp. 145-146): معمل الرياضيات: استكشاف الكسور المتكافئة
- Summary 5 (pp. 147-151): الدرس (٤-٢): تبسيط الكسور الاعتيادية ومعمل الأعداد الكسرية
All include official school header and teacher signature card at bottom-left.
"""

from generator_6b_header_styles import make_school_header, make_teacher_footer

SUMMARIES_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثاني: ملخصات الطالب الشاملة والمركزة (٥ ملخصات متتالية)            -->
    <!-- ========================================================================= -->
    <section class="mega-section" id="section-summaries">
        <div class="section-banner">
            <h2>📑 المحور الثاني: ملخصات الطالب التعليمية الشاملة والمصورة</h2>
            <p>مذكرات دراسية مركزة ومجهزة بنماذج مفاهيمية وجداول قواعد وأمثلة محلولة لطلاب الصف السادس الابتدائي (ص ١٣٥ - ١٥١)</p>
        </div>
"""

RAW_SUMMARY_1 = r"""
        <!-- ملخص ١: اختبار الفصل ٣ والتراكمي (العمليات على الكسور العشرية) -->
        <article class="student-summary-card" id="summary-1-ch3-test">
            __HEADER__
            <div class="summary-title-strip">
                <h3>ملخص المراجعة المركزة: العمليات على الكسور العشرية (اختبار الفصل ٣ والاختبار التراكمي)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٣٥ – ١٣٧</span>
            </div>

            <div class="summary-body">
                <div class="summary-grid-2col">
                    <!-- كرت جمع وطرح الكسور العشرية -->
                    <div class="concept-callout">
                        <h4>١. جمع وطرح الكسور العشرية</h4>
                        <p><strong>القاعدة الذهبية:</strong> رتّب الفواصل العشرية فوق بعضها تماماً، وضع أصفاراً في المنازل الفارغة لتتساوى المنازل العشرية، ثم اجمع أو اطرح كالأعداد الكلية وأنزل الفاصلة في مكانها.</p>
                        <div class="arabic-vert-calc-wrapper">
                            <table class="arabic-vert-table">
                                <caption>عملية الجمع الرأسية (الرمز على اليمين):</caption>
                                <tr><td class="sign-col"></td><td class="num-col">١٢,٤٠</td></tr>
                                <tr class="op-divider"><td class="sign-col">+</td><td class="num-col">٠٨,٧٥</td></tr>
                                <tr class="res-row"><td class="sign-col"></td><td class="num-col">٢١,١٥</td></tr>
                            </table>
                            <table class="arabic-vert-table">
                                <caption>عملية الطرح الرأسية (الرمز على اليمين):</caption>
                                <tr><td class="sign-col"></td><td class="num-col">٢٥,٣٠</td></tr>
                                <tr class="op-divider"><td class="sign-col">−</td><td class="num-col">٠٧,٨٥</td></tr>
                                <tr class="res-row"><td class="sign-col"></td><td class="num-col">١٧,٤٥</td></tr>
                            </table>
                        </div>
                    </div>

                    <!-- كرت ضرب الكسور العشرية -->
                    <div class="concept-callout">
                        <h4>٢. ضرب الكسور العشرية</h4>
                        <p><strong>القاعدة الذهبية:</strong> اضرب العددين كما لو كانا عددين كليين دون فواصل، ثم عد مجموع المنازل العشرية على يمين الفاصلة في كلا العددين، وضع الفاصلة في الناتج بعد ذلك العدد من المنازل بدءاً من اليمين.</p>
                        <div class="math-rule-box">
                            <div class="ar-math-display">٣,٦ × ٠,٤ = ١,٤٤</div>
                            (منزلة عشرية واحدة + منزلة عشرية واحدة = منزلتان بالناتج)
                        </div>
                    </div>
                </div>

                <!-- كرت قسمة الكسور العشرية -->
                <div class="concept-callout" style="margin-top:15px;">
                    <h4>٣. قسمة الكسور العشرية</h4>
                    <div class="summary-grid-2col" style="margin-top:10px;">
                        <div style="background:#f8fafc; padding:12px; border-radius:8px;">
                            <strong>أ) القسمة على عدد كلي:</strong><br>
                            نرفع الفاصلة العشرية مباشرة إلى الناتج عند الوصول إليها ثم نكمل القسمة كالمعتاد.<br>
                            مثال: <span class="ar-math">٤,٨ ÷ ٢ = ٢,٤</span>.
                        </div>
                        <div style="background:#f8fafc; padding:12px; border-radius:8px;">
                            <strong>ب) القسمة على كسر عشري:</strong><br>
                            نضرب المقسوم والمقسوم عليه في (<span class="ar-math">١٠</span> أو <span class="ar-math">١٠٠</span> أو <span class="ar-math">١٠٠٠</span>) ليصبح المقسوم عليه عدداً كلياً، ثم نقسم.<br>
                            مثال: <span class="ar-math">١٥,٦ ÷ ٠,٣ = ١٥٦ ÷ ٣ = ٥٢</span>.
                        </div>
                    </div>
                </div>

                <!-- جدول إرشادات الاختبارات المعيارية والتراكمية -->
                <div class="tips-box" style="margin-top:15px;">
                    <h4>💡 إرشادات ذكية للتفوق في الاختبارات المعيارية والتراكمية (ص ١٣٦ - ١٣٧):</h4>
                    <table class="standard-table">
                        <thead>
                            <tr>
                                <th>الاستراتيجية</th>
                                <th>كيف تطبقها؟</th>
                                <th>الفائدة</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>التقدير السريع:</strong></td>
                                <td>قرّب الأعداد العشرية إلى أعداد كلية قريبة قبل البدء بالحساب الدقيق.</td>
                                <td>استبعاد الخيارات غير المنطقية فوراً وتوفير الوقت.</td>
                            </tr>
                            <tr>
                                <td><strong>فحص المنزلة الأخيرة:</strong></td>
                                <td>احسب ضرب أو جمع رقمي الآحاد أو الجزء الأيمن فقط لتحديد الرقم الأخير للناتج.</td>
                                <td>مطابقة رقم الآحاد مع خيارات الإجابة الأربعة.</td>
                            </tr>
                            <tr>
                                <td><strong>التحقق بالعملية العكسية:</strong></td>
                                <td>تحقق من ناتج القسمة بالضرب: (الناتج <span class="ar-math">×</span> المقسوم عليه = المقسوم).</td>
                                <td>ضمان صحة الإجابة بنسبة ١٠٠٪ وعدم فقد أي درجات.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_SUMMARY_2 = r"""
        <!-- ملخص ٢: تهيئة واستعداد الفصل ٤ -->
        <article class="student-summary-card" id="summary-2-ch4-prep">
            __HEADER__
            <div class="summary-title-strip">
                <h3>ملخص التهيئة والاستعداد: الفصل الرابع (الكسور الاعتيادية والكسور العشرية)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٣٨ – ١٣٩</span>
            </div>

            <div class="summary-body">
                <div class="summary-grid-2col">
                    <div class="concept-callout">
                        <h4>١. قواسم الأعداد (Factors)</h4>
                        <p><strong>ما هو القاسم؟</strong> قاسم العدد هو عدد كلي يقسم ذلك العدد بدون أي باقٍ. لإيجاد جميع قواسم عدد، نكتب أزواج الضرب التي تعطي ذلك العدد.</p>
                        <div class="math-rule-box">
                            <strong>قواسم العدد <span class="ar-math">٢٠</span>:</strong><br>
                            <span class="ar-math">١×٢٠=٢٠</span> ، <span class="ar-math">٢×١٠=٢٠</span> ، <span class="ar-math">٤×٥=٢٠</span><br>
                            القواسم هي: <strong><span class="ar-math">١ ، ٢ ، ٤ ، ٥ ، ١٠ ، ٢٠</span></strong>.
                        </div>
                    </div>

                    <div class="concept-callout">
                        <h4>٢. الكسر الاعتيادي ونماذج الأشكال المظللة</h4>
                        <p><strong>بنية الكسر:</strong> الكسر الاعتيادي يكتب على الصورة (البسط / المقام).</p>
                        <ul style="padding-right:20px; font-size:0.95rem;">
                            <li><strong>البسط (العدد العلوي):</strong> يدل على عدد الأجزاء المظللة أو المأخوذة.</li>
                            <li><strong>المقام (العدد السفلي):</strong> يدل على إجمالي عدد الأجزاء المتطابقة كلها.</li>
                        </ul>
                        <div class="math-rule-box">
                            إذا كان لدينا شكل مقسم إلى <span class="ar-math">٦</span> أجزاء متطابقة وظللنا <span class="ar-math">٥</span> منها، فالكسر هو: <strong><span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٦</span></span></span></strong>.
                        </div>
                    </div>
                </div>

                <!-- جدول مراجعة قواعد قابلية القسمة السريعة -->
                <div class="summary-table-box" style="margin-top:15px;">
                    <h4>⚡ جدول قواعد قابلية القسمة السريعة (تساعدك في معرفة القواسم):</h4>
                    <table class="standard-table">
                        <thead>
                            <tr>
                                <th>يقبل العدد القسمة على:</th>
                                <th>القاعدة الذهبية</th>
                                <th>مثال توضيحي</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong><span class="ar-math">٢</span></strong></td>
                                <td>إذا كان آحاده عدداً زوجياً (<span class="ar-math">٠</span>، <span class="ar-math">٢</span>، <span class="ar-math">٤</span>، <span class="ar-math">٦</span>، <span class="ar-math">٨</span>).</td>
                                <td>العدد <span class="ar-math">٤٦</span> يقبل على <span class="ar-math">٢</span> لأن آحاده <span class="ar-math">٦</span>.</td>
                            </tr>
                            <tr>
                                <td><strong><span class="ar-math">٣</span></strong></td>
                                <td>إذا كان مجموع أرقام العدد يقبل القسمة على <span class="ar-math">٣</span>.</td>
                                <td><span class="ar-math">٥٤</span> (<span class="ar-math">٤+٥=٩</span> تقبل على ٣ <span class="ar-math">←</span> يقبل).</td>
                            </tr>
                            <tr>
                                <td><strong><span class="ar-math">٥</span></strong></td>
                                <td>إذا كان رقم آحاده <span class="ar-math">٠</span> أو <span class="ar-math">٥</span>.</td>
                                <td>العدد <span class="ar-math">٧٥</span> يقبل القسمة على <span class="ar-math">٥</span>.</td>
                            </tr>
                            <tr>
                                <td><strong><span class="ar-math">١٠</span></strong></td>
                                <td>إذا كان رقم آحاده <span class="ar-math">٠</span> فقط.</td>
                                <td>العدد <span class="ar-math">١٢٠</span> يقبل القسمة على <span class="ar-math">١٠</span>.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_SUMMARY_3 = r"""
        <!-- ملخص ٣: الدرس (٤-١) القاسم المشترك الأكبر (ق.م.أ) -->
        <article class="student-summary-card" id="summary-3-lesson4-1-gcf">
            __HEADER__
            <div class="summary-title-strip">
                <h3>ملخص الدرس (٤-١): القاسم المشترك الأكبر (ق.م.أ)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٠ – ١٤٤</span>
            </div>

            <div class="summary-body">
                <div class="concept-callout">
                    <h4>🎯 ما هو القاسم المشترك الأكبر (ق.م.أ)؟</h4>
                    <p>تسمى القواسم التي يشترك فيها عددان أو أكثر <strong>قواسم مشتركة</strong>. وأكبر هذه القواسم المشتركة يسمى <strong>القاسم المشترك الأكبر (ق.م.أ)</strong>.</p>
                </div>

                <div class="summary-grid-2col" style="margin-top:15px;">
                    <!-- الطريقة الأولى -->
                    <div class="concept-callout">
                        <h4>الطريقة ١: سرد القواسم المنظمة</h4>
                        <p>مناسبة للأعداد الصغيرة والمتوسطة:</p>
                        <div class="math-rule-box">
                            <strong>مثال: أوجد (ق.م.أ) للعددين <span class="ar-math">١٢</span> و <span class="ar-math">١٨</span>:</strong><br>
                            • قواسم <span class="ar-math">١٢</span>: {<span class="ar-math">١ ، ٢ ، ٣ ، ٤ ، ٦ ، ١٢</span>}<br>
                            • قواسم <span class="ar-math">١٨</span>: {<span class="ar-math">١ ، ٢ ، ٣ ، ٦ ، ٩ ، ١٨</span>}<br>
                            • القواسم المشتركة: {<span class="ar-math">١ ، ٢ ، ٣ ، ٦</span>}<br>
                            • أكبر هذه القواسم هو: <strong>(ق.م.أ) = <span class="ar-math">٦</span></strong>.
                        </div>
                    </div>

                    <!-- الطريقة الثانية -->
                    <div class="concept-callout">
                        <h4>الطريقة ٢: التحليل إلى العوامل الأولية</h4>
                        <p>ممتازة للأعداد الكبيرة والأعداد الثلاثية:</p>
                        <div class="math-rule-box">
                            <strong>مثال: أوجد (ق.م.أ) للعددين <span class="ar-math">٥٤</span> و <span class="ar-math">٦٠</span>:</strong><br>
                            • <span class="ar-math">٥٤ = ٢ × ٣ × ٣ × ٣</span><br>
                            • <span class="ar-math">٦٠ = ٢ × ٢ × ٣ × ٥</span><br>
                            • العوامل المشتركة هي: عامل (<span class="ar-math">٢</span>) وعامل (<span class="ar-math">٣</span>).<br>
                            • نضرب العوامل المشتركة: <span class="ar-math">٢ × ٣ = ٦</span>.
                        </div>
                    </div>
                </div>

                <!-- تطبيقات حياتية مهمة -->
                <div class="summary-application-box" style="margin-top:15px; background:#eff6ff; padding:15px; border-radius:10px; border-right:4px solid #1e3a8a;">
                    <h4>💼 متى نستخدم (ق.م.أ) في المسائل اللفظية والحياة الواقعية؟</h4>
                    <p>نستخدم (ق.م.أ) عند قراءة الكلمات الدلالية التالية: <em>«أكبر عدد ممكن من المجموعات»</em>، <em>«توزيع بالتساوي دون باقٍ»</em>، <em>«أطول قطعة ممكنة متساوية»</em>، <em>«ترتيب صفوف متطابقة»</em>.</p>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_SUMMARY_4 = r"""
        <!-- ملخص ٤: معمل الرياضيات - الكسور المتكافئة -->
        <article class="student-summary-card" id="summary-4-lab-equiv-fractions">
            __HEADER__
            <div class="summary-title-strip">
                <h3>ملخص استكشاف معمل الرياضيات: الكسور المتكافئة (Equivalent Fractions)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٥ – ١٤٦</span>
            </div>

            <div class="summary-body">
                <div class="concept-callout">
                    <h4>🎯 ما هي الكسور المتكافئة؟</h4>
                    <p><strong>الكسور المتكافئة</strong> هي كسور لها القيمة نفسها وتسمي المقدار أو الجزء ذاته من الكل، على الرغم من أن بسوطها ومقاماتها مختلفة الأرقام.</p>
                </div>

                <div class="summary-grid-2col" style="margin-top:15px;">
                    <!-- التكافؤ بالضرب -->
                    <div class="concept-callout">
                        <h4>١. إيجاد كسور متكافئة بالضرب</h4>
                        <p>عند ضرب بسط ومقام الكسر في العدد نفسه (غير الصفر)، فإننا نجزئ كل جزء إلى أجزاء أصغر دون تغيير الكمية الإجمالية:</p>
                        <div class="math-rule-box">
                            <div class="ar-math-display"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٢ × ٢</span><span class="denom">٣ × ٢</span></span> = <span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span>
                              ,  
                            <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span> = <span class="ar-frac"><span class="num">٢ × ٣</span><span class="denom">٣ × ٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></div>
                        </div>
                    </div>

                    <!-- التكافؤ بالقسمة والتبسيط -->
                    <div class="concept-callout">
                        <h4>٢. إيجاد كسور متكافئة بالقسمة (التبسيط)</h4>
                        <p>عند قسمة بسط ومقام الكسر على قاسم مشترك لهما (غير الصفر)، فإننا نجمع الأجزاء الصغيرة في أجزاء أكبر وتسمى هذه العملية <strong>تبسيط الكسر</strong>:</p>
                        <div class="math-rule-box">
                            <div class="ar-math-display"><span class="ar-frac"><span class="num">٦</span><span class="denom">٨</span></span> = <span class="ar-frac"><span class="num">٦ ÷ ٢</span><span class="denom">٨ ÷ ٢</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></div>
                        </div>
                    </div>
                </div>

                <!-- نموذج المقارنة بأشرطة الكسور -->
                <div class="tips-box" style="margin-top:15px;">
                    <h4>📏 كيف نتأكد من التكافؤ باستخدام أشرطة الكسور ونماذج المساحة؟</h4>
                    <p>عند وضع شريط <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span> فوق شريطي <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span>، نجد أنهما يتطابقان في الطول من البداية إلى النهاية تماماً. وبالمثل شريط <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span> يطابق أربعة أشرطة من فئة <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٦</span></span></span> (<span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span></span>).</p>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_SUMMARY_5 = r"""
        <!-- ملخص ٥: الدرس (٤-٢) تبسيط الكسور ومعمل الأعداد الكسرية -->
        <article class="student-summary-card" id="summary-5-lesson4-2-simplifying">
            __HEADER__
            <div class="summary-title-strip">
                <h3>ملخص الدرس (٤-٢): تبسيط الكسور الاعتيادية ومعمل الأعداد الكسرية والكسور غير الفعلية</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٧ – ١٥١</span>
            </div>

            <div class="summary-body">
                <div class="summary-grid-2col">
                    <!-- كرت أبسط صورة -->
                    <div class="concept-callout">
                        <h4>١. الكسر في أبسط صورة</h4>
                        <p>يقال عن الكسر إنه في <strong>أبسط صورة</strong> إذا كان القاسم المشترك الأكبر (ق.م.أ) لبسطه ومقامه هو العدد <span class="ar-math">١</span> فقط.</p>
                        <div class="math-rule-box">
                            <strong>خوارزمية التبسيط السريع:</strong><br>
                            ١) أوجد (ق.م.أ) لكل من البسط والمقام.<br>
                            ٢) اقسم كلاً من البسط والمقام على (ق.م.أ).<br>
                            <strong>مثال:</strong> لتبسيط <span class="ar-math"><span class="ar-frac"><span class="num">١٨</span><span class="denom">٢٤</span></span></span>:<br>
                            (ق.م.أ) للعددين هو <span class="ar-math">٦</span> <span class="ar-math">←</span> <span class="ar-math"><span class="ar-frac"><span class="num">١٨÷٦</span><span class="denom">٢٤÷٦</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>.
                        </div>
                    </div>

                    <!-- كرت تصنيف الكسور (ص 151) -->
                    <div class="concept-callout">
                        <h4>٢. أنواع الكسور (معمل ص ١٥١)</h4>
                        <table class="standard-table" style="font-size:0.9rem;">
                            <thead>
                                <tr>
                                    <th>النوع</th>
                                    <th>التعريف والخاصية</th>
                                    <th>أمثلة</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>الكسر الفعلي</strong></td>
                                    <td>بسطه &lt; مقامه، وقيمته أقل من الواحد الصحيح.</td>
                                    <td><span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span> ، <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٥</span></span></span></td>
                                </tr>
                                <tr>
                                    <td><strong>الكسر غير الفعلي</strong></td>
                                    <td>بسطه &ge; مقامه، وقيمته تساوي الواحد أو أكبر منه.</td>
                                    <td><span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٤</span></span></span> ، <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٣</span></span></span></td>
                                </tr>
                                <tr>
                                    <td><strong>العدد الكسري</strong></td>
                                    <td>يتكون من عدد كلي وبجانبه كسر اعتيادي.</td>
                                    <td><span class="ar-math">١ <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span> ، <span class="ar-math">٢ <span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- التحويل بين الكسر غير الفعلي والعدد الكسري -->
                <div class="concept-callout" style="margin-top:15px;">
                    <h4>🔄 مهارة التحويل المتقاطعة (بين العدد الكسري والكسر غير الفعلي):</h4>
                    <div class="summary-grid-2col">
                        <div style="background:#f8fafc; padding:12px; border-radius:8px;">
                            <strong>من عدد كسري إلى كسر غير فعلي:</strong><br>
                            نضرب العدد الكلي في المقام ونجمع الناتج مع البسط، ويبقى المقام كما هو:<br>
                            <div class="ar-math-display">٢ <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">(٢ × ٤) + ٣</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">٨ + ٣</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">١١</span><span class="denom">٤</span></span></div>
                        </div>
                        <div style="background:#f8fafc; padding:12px; border-radius:8px;">
                            <strong>من كسر غير فعلي إلى عدد كسري:</strong><br>
                            نقسم البسط على المقام: ناتج القسمة هو العدد الكلي، والباقي هو البسط الجديد فوق نفس المقام:<br>
                            <div class="math-rule-box" style="direction:rtl; text-align:center; font-size:1.15rem; font-weight:700;">
                            <span class="ar-math"><span class="ar-frac"><span class="num">١١</span><span class="denom">٤</span></span> ← ١١ ÷ ٤ = ٢</span> والباقي <span class="ar-math">٣ →</span> الناتج في صورة عدد كسري: <strong><span class="ar-math">٢ <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span></strong>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

SUMMARIES_SECTION_END = r"""
    </section><!-- /#section-summaries -->
"""

def get_all_summaries_html():
    s1 = RAW_SUMMARY_1.replace("__HEADER__", make_school_header("ملخص المراجعة المركزة (العمليات على الكسور العشرية)", "ملخص الطالب")).replace("__FOOTER__", make_teacher_footer())
    s2 = RAW_SUMMARY_2.replace("__HEADER__", make_school_header("ملخص تهيئة الفصل الرابع (الكسور الاعتيادية)", "ملخص الطالب")).replace("__FOOTER__", make_teacher_footer())
    s3 = RAW_SUMMARY_3.replace("__HEADER__", make_school_header("ملخص الدرس ٤-١ (القاسم المشترك الأكبر)", "ملخص الطالب")).replace("__FOOTER__", make_teacher_footer())
    s4 = RAW_SUMMARY_4.replace("__HEADER__", make_school_header("ملخص معمل الرياضيات (الكسور المتكافئة)", "ملخص الطالب")).replace("__FOOTER__", make_teacher_footer())
    s5 = RAW_SUMMARY_5.replace("__HEADER__", make_school_header("ملخص الدرس ٤-٢ وتبسيط الكسور والأعداد الكسرية", "ملخص الطالب")).replace("__FOOTER__", make_teacher_footer())
    
    return (
        SUMMARIES_SECTION_START +
        s1 + s2 + s3 + s4 + s5 +
        SUMMARIES_SECTION_END
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    content = get_all_summaries_html()
    with open('section_6b_summaries.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"section_6b_summaries.html written successfully! Total length: {len(content)} chars.")
