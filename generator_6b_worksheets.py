# -*- coding: utf-8 -*-
"""
generator_6b_worksheets.py: Interactive Worksheets and Tests for Grade 6 Elementary (6ب) pages 135 to 151:
- Worksheet 1: اختبار الفصل ٣ والاختبار التراكمي ٣ (العمليات على الكسور العشرية ص ١٣٥ - ١٣٧)
- Worksheet 2: تهيئة الفصل ٤ (الكسور الاعتيادية والكسور العشرية ص ١٣٨ - ١٣٩)
- Worksheet 3: الدرس (٤-١) القاسم المشترك الأكبر (ق.م.أ ص ١٤٠ - ١٤٤)
- Worksheet 4: استكشاف معمل الرياضيات: الكسور المتكافئة (ص ١٤٥ - ١٤٦)
- Worksheet 5: الدرس (٤-٢) تبسيط الكسور الاعتيادية ومعمل الأعداد الكسرية والكسور غير الفعلية (ص ١٤٧ - ١٥١)

Includes:
- Dedicated top toolbar button [ 👁️ إظهار الإجابة على المسائل ] with .no-print
- Inline solutions directly on each question (correct option highlighted, step-by-step solution box)
- Official school header with Base64 logo and school name: المدارس المتقدمة للتعلم الذكي بجدة
- Teacher signature card at bottom-left: أ. محمد عبدالله جمعة
- Strictly Eastern Arabic numerals (٠-٩)
"""

from generator_6b_header_styles import make_school_header, make_teacher_footer, make_ws_toolbar

WORKSHEETS_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التفاعلية (٥ أوراق عمل متتالية)         -->
    <!-- ========================================================================= -->
    <section class="mega-section" id="section-worksheets">
        <div class="section-banner">
            <h2>📝 المحور الثالث: أوراق العمل والاختبارات التفاعلية الشاملة</h2>
            <p>أوراق عمل واختبارات معيارية مجهزة بحلول تفاعلية مدمجة على المسائل نفسها وزر تحكم علوي خاص بالمعلم (ص ١٣٥ - ١٥١)</p>
        </div>
"""

RAW_WS_1 = r"""
        <!-- ورقة عمل ١: اختبار الفصل ٣ والتراكمي ٣ -->
        <article class="worksheet-card" id="ws-1-ch3-test">
            __TOOLBAR__
            __HEADER__

            <div class="ws-title-strip">
                <h3>ورقة عمل واختبار قياسي: العمليات على الكسور العشرية (اختبار الفصل ٣ والاختبار التراكمي ٣)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٣٥ – ١٣٧</span>
            </div>

            <!-- معلومات الطالب -->
            <div class="student-info-grid">
                <div><strong>اسم الطالب:</strong> ............................................................</div>
                <div><strong>الصف:</strong> السادس الابتدائي ( ... )</div>
                <div><strong>التاريخ:</strong> ..... / ..... / ١٤٤٨ هـ</div>
                <div><strong>الدرجة المستحقة:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / ٢٠</div>
            </div>

            <div class="ws-body">
                <!-- القسم الأول: الاختيار من متعدد -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">أ</span> السؤال الأول: اختر الإجابة الصحيحة من بين الخيارات المتاحة (٤ درجات):</h4>
                    
                    <!-- س1 -->
                    <div class="q-card">
                        <div class="q-text"><strong>١)</strong> أوجد ناتج الجمع التالي: <span class="ar-math">١٢,٤ + ٨,٧٥</span></div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٢٠,١٥</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">٢١,١٥</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">٢١,٥</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">٩٩,٩</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            نحاذي الفواصل العشرية ونضع صفراً للموازنة: <span class="ar-math">١٢,٤٠ + ٨,٧٥ = ٢١,١٥</span>.
                        </div>
                    </div>

                    <!-- س2 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٢)</strong> أوجد ناتج الضرب: <span class="ar-math">٣,٦ × ٠,٤</span></div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">١٤,٤</span></div>
                            <div class="mcq-opt">ب) <span class="ar-math">٠,١٤٤</span></div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math">١,٤٤</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١٤٤</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            نضرب كأعداد كلية: <span class="ar-math">٣٦ × ٤ = ١٤٤</span>. مجموع المنازل العشرية منزلتان (واحدة في <span class="ar-math">٣,٦</span> وواحدة في <span class="ar-math">٠,٤</span>)، فنضع الفاصلة بعد منزلتين من اليمين: <strong><span class="ar-math">١,٤٤</span></strong>.
                        </div>
                    </div>

                    <!-- س3 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٣)</strong> ناتج قسمة: <span class="ar-math">١٥,٦ ÷ ٠,٣</span> يساوي:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٥,٢</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">٥٢</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">٠,٥٢</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">٥٢٠</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            نضرب كلاً من المقسوم والمقسوم عليه في <span class="ar-math">١٠</span> للتخلص من الفاصلة في المقسوم عليه: <span class="ar-math">١٥٦ ÷ ٣ = ٥٢</span>.
                        </div>
                    </div>

                    <!-- س4 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٤)</strong> اشترى أحمد <span class="ar-math">٢,٥</span> كجم من العنب بسعر <span class="ar-math">٦</span> ريالات للكيلوجرام الواحد، فكم دفع للبائع؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">١٢</span> ريالاً</div>
                            <div class="mcq-opt">ب) <span class="ar-math">١٤,٥</span> ريالاً</div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math">١٥</span> ريالاً <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١٥٠</span> ريالاً</div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            التكلفة = الوزن <span class="ar-math">×</span> السعر = <span class="ar-math">٢,٥ × ٦</span>. <span class="ar-math">٢٥ × ٦ = ١٥٠</span>. بوضع الفاصلة بعد منزلة واحدة: <strong><span class="ar-math">١٥</span> ريالاً</strong>.
                        </div>
                    </div>
                </div>

                <!-- القسم الثاني: الصواب والخطأ -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ب</span> السؤال الثاني: ضع علامة (✓) أمام العبارة الصحيحة وعلامة (✗) أمام العبارة الخاطئة (٣ درجات):</h4>
                    
                    <div class="tf-item">
                        <div class="tf-text"><strong>١)</strong> ناتج ضرب <span class="ar-math">٠,٢ × ٠,٣ = ٠,٦</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-wrong">العبارة خاطئة (✗)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير الرياضي:</strong> <span class="ar-math">٢ × ٣ = ٦</span>، وبما أن لدينا منزلتين عشريتين فالناتج الصحيح هو <strong><span class="ar-math">٠,٠٦</span></strong> وليس <span class="ar-math">٠,٦</span>.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٢)</strong> عند قسمة كسر عشري على العدد <span class="ar-math">١٠</span> تتحرك الفاصلة العشرية منزلة واحدة إلى اليسار. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير الرياضي:</strong> القسمة على قوى العشرة تصغر قيمة العدد بتحريك الفاصلة لليسار بعدد الأصفار.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٣)</strong> ناتج طرح: <span class="ar-math">٤,٥ − ٢,٢٥ = ٢,٢٥</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير الرياضي:</strong> بمحاذاة الفواصل: <span class="ar-math">٤,٥٠ − ٢,٢٥ = ٢,٢٥</span>.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- القسم الثالث: المسائل المقالية -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ج</span> السؤال الثالث: المسائل المقالية والرياضية من واقع الحياة (٣ درجات):</h4>
                    
                    <div class="q-card">
                        <div class="q-text"><strong>مسألة قطار الحرمين السريع:</strong> قطع قطار الحرمين السريع مسافة <span class="ar-math">٣١٢,٥</span> كم في زمن قدره <span class="ar-math">١,٢٥</span> ساعة بين محطتي جدة والمدينة المنورة. احسب السرعة المتوسطة للقطار بالكيلومتر لكل ساعة موضحاً خطوات القسمة.</div>
                        <div class="student-work-area">
                            <em>مساحة إجابة الطالب وحساب العمليات:</em>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 خطوات الحل التفصيلية للدرجة الكاملة:</strong><br>
                            ١) قانون السرعة = المسافة <span class="ar-math">÷</span> الزمن = <span class="ar-math">٣١٢,٥ ÷ ١,٢٥</span>.<br>
                            ٢) التخلص من فاصلة المقسوم عليه بالضرب في <span class="ar-math">١٠٠</span>:<br>
                            <span class="ar-math">٣١٢,٥ × ١٠٠ = ٣١٢٥٠   ,   ١,٢٥ × ١٠٠ = ١٢٥</span>.<br>
                            ٣) نقسم: <span class="ar-math">٣١٢٥٠ ÷ ١٢٥ = ٢٥٠</span>.<br>
                            إذن سرعة القطار = <strong><span class="ar-math">٢٥٠</span> كم/ساعة</strong>.
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_WS_2 = r"""
        <!-- ورقة عمل ٢: تهيئة الفصل ٤ -->
        <article class="worksheet-card" id="ws-2-ch4-prep">
            __TOOLBAR__
            __HEADER__

            <div class="ws-title-strip">
                <h3>ورقة عمل تقويمية: تهيئة واستعداد الفصل الرابع (الكسور الاعتيادية والكسور العشرية)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٣٨ – ١٣٩</span>
            </div>

            <!-- معلومات الطالب -->
            <div class="student-info-grid">
                <div><strong>اسم الطالب:</strong> ............................................................</div>
                <div><strong>الصف:</strong> السادس الابتدائي ( ... )</div>
                <div><strong>التاريخ:</strong> ..... / ..... / ١٤٤٨ هـ</div>
                <div><strong>الدرجة المستحقة:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / ٢٠</div>
            </div>

            <div class="ws-body">
                <!-- أ: الاختيار من متعدد -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">أ</span> السؤال الأول: اختر الإجابة الصحيحة علمياً ورياضياً (٤ درجات):</h4>

                    <!-- س1 -->
                    <div class="q-card">
                        <div class="q-text"><strong>١)</strong> جميع قواسم العدد <span class="ar-math">١٥</span> هي:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">١ ، ١٥</span> فقط</div>
                            <div class="mcq-opt">ب) <span class="ar-math">٣ ، ٥</span> فقط</div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math">١ ، ٣ ، ٥ ، ١٥</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١ ، ٢ ، ٣ ، ٥ ، ١٥</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            أزواج الضرب للعدد <span class="ar-math">١٥</span> هي: <span class="ar-math">١ × ١٥ = ١٥</span> و <span class="ar-math">٣ × ٥ = ١٥</span>. إذن القواسم هي <span class="ar-math">١ ، ٣ ، ٥ ، ١٥</span>.
                        </div>
                    </div>

                    <!-- س2 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٢)</strong> ما الكسر الذي يمثل <span class="ar-math">٥</span> أجزاء مظللة من أصل <span class="ar-math">٨</span> أجزاء متطابقة؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٨</span><span class="denom">٥</span></span></span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٨</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٨</span></span></span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٣</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            البسط = عدد الأجزاء المظللة (<span class="ar-math">٥</span>)، والمقام = إجمالي عدد الأجزاء المتطابقة (<span class="ar-math">٨</span>). إذن الكسر هو <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٨</span></span></span>.
                        </div>
                    </div>

                    <!-- س3 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٣)</strong> كم عدد قواسم العدد <span class="ar-math">١٢</span>؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٤</span> قواسم</div>
                            <div class="mcq-opt">ب) <span class="ar-math">٥</span> قواسم</div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math">٦</span> قواسم <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">٨</span> قواسم</div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            قواسم <span class="ar-math">١٢</span> هي: <span class="ar-math">١ ، ٢ ، ٣ ، ٤ ، ٦ ، ١٢</span>. وعدها الإجمالي هو <span class="ar-math">٦</span> قواسم.
                        </div>
                    </div>

                    <!-- س4 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٤)</strong> أي الأعداد التالية يقبل القسمة على <span class="ar-math">٢</span> و <span class="ar-math">٥</span> معاً في الوقت نفسه؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٢٥</span></div>
                            <div class="mcq-opt">ب) <span class="ar-math">٣٤</span></div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math">٥٠</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">٥٥</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            العدد الذي يقبل على <span class="ar-math">٢</span> و <span class="ar-math">٥</span> معاً يجب أن يكون رقم آحاده <span class="ar-math">٠</span> (أي يقبل على <span class="ar-math">١٠</span>). والعدد هو <span class="ar-math">٥٠</span>.
                        </div>
                    </div>
                </div>

                <!-- ب: الصواب والخطأ -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ب</span> السؤال الثاني: ضع علامة (✓) أو (✗) مع تصحيح الخطأ (٣ درجات):</h4>

                    <div class="tf-item">
                        <div class="tf-text"><strong>١)</strong> العدد <span class="ar-math">٧</span> هو عدد أولي لأن له قاسمين فقط هما <span class="ar-math">١</span> و <span class="ar-math">٧</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> العدد الأولي تعريفه عدد كلي أكبر من ١ له قاسمان مختلفان فقط هما ١ والعدد نفسه.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٢)</strong> في الكسر الاعتيادي <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٧</span></span></span> يسمى الرقم <span class="ar-math">٧</span> بالبسط. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-wrong">العبارة خاطئة (✗)</span>
                            <div class="inline-solution-block">
                                <strong>التصحيح:</strong> الرقم العلوي (<span class="ar-math">٣</span>) هو البسط، بينما الرقم السفلي (<span class="ar-math">٧</span>) هو <strong>المقام</strong>.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٣)</strong> العدد <span class="ar-math">٩</span> من قواسم العدد <span class="ar-math">٣٦</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> لأن <span class="ar-math">٩ × ٤ = ٣٦</span> دون أي باقٍ.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ج: سؤال تطبيقي مقالي -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ج</span> السؤال الثالث: المسألة التطبيقية (٣ درجات):</h4>
                    <div class="q-card">
                        <div class="q-text">اكتب جميع قواسم العدد <span class="ar-math">٢٤</span> مستعملاً أزواج الضرب المنظمة، ثم ارسم شكلاً هندسياً يمثل الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٦</span></span></span>.</div>
                        <div class="student-work-area">
                            <em>مساحة إجابة الطالب ورسم النموذج:</em>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 الحل النموذجي:</strong><br>
                            ١) أزواج ضرب <span class="ar-math">٢٤</span>: <span class="ar-math">١ × ٢٤</span> ، <span class="ar-math">٢ × ١٢</span> ، <span class="ar-math">٣ × ٨</span> ، <span class="ar-math">٤ × ٦</span>.<br>
                            القواسم مرتبة هي: <strong><span class="ar-math">١ ، ٢ ، ٣ ، ٤ ، ٦ ، ٨ ، ١٢ ، ٢٤</span></strong>.<br>
                            ٢) لرسم <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٦</span></span></span>: نرسم مستطيلاً نقسمه بالمسطرة إلى <span class="ar-math">٦</span> أجزاء متطابقة تماماً، ونظلل <span class="ar-math">٥</span> أجزاء منها.
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_WS_3 = r"""
        <!-- ورقة عمل ٣: الدرس (٤-١) ق.م.أ -->
        <article class="worksheet-card" id="ws-3-lesson4-1-gcf">
            __TOOLBAR__
            __HEADER__

            <div class="ws-title-strip">
                <h3>ورقة عمل واختبار إتقان: الدرس (٤-١) القاسم المشترك الأكبر (ق.م.أ)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٠ – ١٤٤</span>
            </div>

            <!-- معلومات الطالب -->
            <div class="student-info-grid">
                <div><strong>اسم الطالب:</strong> ............................................................</div>
                <div><strong>الصف:</strong> السادس الابتدائي ( ... )</div>
                <div><strong>التاريخ:</strong> ..... / ..... / ١٤٤٨ هـ</div>
                <div><strong>الدرجة المستحقة:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / ٢٠</div>
            </div>

            <div class="ws-body">
                <!-- أ: الاختيار من متعدد -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">أ</span> السؤال الأول: اختر الإجابة الصحيحة (٤ درجات):</h4>

                    <!-- س1 -->
                    <div class="q-card">
                        <div class="q-text"><strong>١)</strong> القاسم المشترك الأكبر (ق.م.أ) للعددين <span class="ar-math">٨</span> و <span class="ar-math">١٢</span> هو:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٢</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">٤</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">٦</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">٢٤</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            قواسم <span class="ar-math">٨</span>: {<span class="ar-math">١، ٢، ٤، ٨</span>}<br>
                            قواسم <span class="ar-math">١٢</span>: {<span class="ar-math">١، ٢، ٣، ٤، ٦، ١٢</span>}<br>
                            القواسم المشتركة: {<span class="ar-math">١، ٢، ٤</span>} <span class="ar-math">←</span> أكبرها هو <strong><span class="ar-math">٤</span></strong>.
                        </div>
                    </div>

                    <!-- س2 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٢)</strong> ما القاسم المشترك الأكبر للعددين <span class="ar-math">٥٤</span> و <span class="ar-math">٦٠</span> (كتاب الطالب ص ١٤١)؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٣</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">٦</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">٩</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١٢</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل بالتحليل الأولي:</strong><br>
                            <span class="ar-math">٥٤ = ٢ × ٣ × ٣ × ٣</span><br>
                            <span class="ar-math">٦٠ = ٢ × ٢ × ٣ × ٥</span><br>
                            العوامل المشتركة هي <span class="ar-math">٢ × ٣ = ٦</span>.
                        </div>
                    </div>

                    <!-- س3 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٣)</strong> القاسم المشترك الأكبر للأعداد الثلاثة <span class="ar-math">٢٤</span> و <span class="ar-math">٣٢</span> و <span class="ar-math">٤٠</span> هو:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٤</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">٨</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">١٢</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١٦</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            العوامل المشتركة بين الأعداد الثلاثة هي: <span class="ar-math">٢ × ٢ × ٢ = ٨</span>.
                        </div>
                    </div>

                    <!-- س4 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٤)</strong> إذا كان العددان أوليين فيما بينهما (مثل <span class="ar-math">٨</span> و <span class="ar-math">٩</span>) فإن (ق.م.أ) لهما يساوي:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) صفراً</div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">١</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) حاصل ضربهما</div>
                            <div class="mcq-opt">د) مجموعهما</div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 القاعدة الرياضية:</strong> القاسم المشترك الوحيد بين أي عددين أوليين فيما بينهما هو العدد <strong><span class="ar-math">١</span></strong>.
                        </div>
                    </div>
                </div>

                <!-- ب: الصواب والخطأ -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ب</span> السؤال الثاني: ضع علامة (✓) أو (✗) مع التعليل (٣ درجات):</h4>

                    <div class="tf-item">
                        <div class="tf-text"><strong>١)</strong> (ق.م.أ) للعددين <span class="ar-math">١٠</span> و <span class="ar-math">٣٠</span> هو العدد <span class="ar-math">١٠</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> بما أن العدد <span class="ar-math">٣٠</span> يقبل القسمة على <span class="ar-math">١٠</span>، فإن (ق.م.أ) هو العدد الأصغر (<span class="ar-math">١٠</span>).
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٢)</strong> يمكن أن يكون القاسم المشترك الأكبر لعددين أكبر من أحدهما. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-wrong">العبارة خاطئة (✗)</span>
                            <div class="inline-solution-block">
                                <strong>التصحيح:</strong> (ق.م.أ) يكون دائماً أصغر من أو يساوي أصغر العددين؛ لأنه يقسمهما.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٣)</strong> العدد <span class="ar-math">٦</span> هو قاسم مشترك للعددين <span class="ar-math">١٨</span> و <span class="ar-math">٢٤</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> كلا العددين يقبل القسمة على <span class="ar-math">٦</span> دون باقٍ (<span class="ar-math">١٨÷٦=٣</span> و <span class="ar-math">٢٤÷٦=٤</span>).
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ج: مسألة تطبيقية -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ج</span> السؤال الثالث: مسألة واقعية وتطبيق حياتي (٣ درجات):</h4>
                    <div class="q-card">
                        <div class="q-text"><strong>مسألة باقات الزهور:</strong> لدى منسق زهور في جدة <span class="ar-math">٣٦</span> وردة حمراء و <span class="ar-math">٤٨</span> وردة بيضاء. يريد توزيعها بالتساوي في مزهريات بحيث تحتوي كل مزهرية على نفس العدد من كل لون دون أي زيادة. ما أكبر عدد من المزهريات يمكن تجهيزه؟ وما محتويات كل مزهرية؟</div>
                        <div class="student-work-area">
                            <em>مساحة إجابة الطالب وتطبيق التحليل الأولي:</em>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 الحل الكامل والنموذجي:</strong><br>
                            ١) نوجد ق.م.أ للعددين <span class="ar-math">٣٦</span> و <span class="ar-math">٤٨</span>:<br>
                            • <span class="ar-math">٣٦ = ٢ × ٢ × ٣ × ٣</span><br>
                            • <span class="ar-math">٤٨ = ٢ × ٢ × ٢ × ٢ × ٣</span><br>
                            • العوامل المشتركة = <span class="ar-math">٢ × ٢ × ٣ = ١٢</span>.<br>
                            ٢) أكبر عدد من المزهريات = <strong><span class="ar-math">١٢</span> مزهرية</strong>.<br>
                            ٣) محتويات كل مزهرية: <span class="ar-math">٣٦÷١٢ = ٣</span> وردات حمراء، و <span class="ar-math">٤٨÷١٢ = ٤</span> وردات بيضاء.
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_WS_4 = r"""
        <!-- ورقة عمل ٤: معمل الكسور المتكافئة -->
        <article class="worksheet-card" id="ws-4-lab-equiv-fractions">
            __TOOLBAR__
            __HEADER__

            <div class="ws-title-strip">
                <h3>ورقة عمل استكشافية: معمل الرياضيات (الكسور المتكافئة)</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٥ – ١٤٦</span>
            </div>

            <!-- معلومات الطالب -->
            <div class="student-info-grid">
                <div><strong>اسم الطالب:</strong> ............................................................</div>
                <div><strong>الصف:</strong> السادس الابتدائي ( ... )</div>
                <div><strong>التاريخ:</strong> ..... / ..... / ١٤٤٨ هـ</div>
                <div><strong>الدرجة المستحقة:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / ٢٠</div>
            </div>

            <div class="ws-body">
                <!-- أ: الاختيار من متعدد -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">أ</span> السؤال الأول: اختر الإجابة الصحيحة بالنماذج والحساب (٤ درجات):</h4>

                    <!-- س1 -->
                    <div class="q-card">
                        <div class="q-text"><strong>١)</strong> أي الكسور التالية يكافئ الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٩</span></span></span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٦</span></span></span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٢</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل بالنماذج والحساب:</strong><br>
                            بضرب البسط والمقام في <span class="ar-math">٣</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٢×٣</span><span class="denom">٣×٣</span></span> = <span class="ar-frac"><span class="num">٦</span><span class="denom">٩</span></span></span>.
                        </div>
                    </div>

                    <!-- س2 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٢)</strong> ما العدد المناسب في المربع ليصبح الكسران متكافئين: <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span> = <span class="ar-frac"><span class="num">؟</span><span class="denom">٢٠</span></span></span>؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math">٩</span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math">١٢</span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math">١٥</span></div>
                            <div class="mcq-opt">د) <span class="ar-math">١٨</span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل:</strong> ضرب المقام <span class="ar-math">٥</span> في <span class="ar-math">٤</span> ليعطي <span class="ar-math">٢٠</span>، فنضرب البسط <span class="ar-math">٣</span> في <span class="ar-math">٤</span> ليكون الناتج <strong><span class="ar-math">١٢</span></strong>.
                        </div>
                    </div>

                    <!-- س3 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٣)</strong> عند قسمة بسط ومقام الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٨</span><span class="denom">١٢</span></span></span> على العدد <span class="ar-math">٤</span> نحصل على الكسر المكافئ:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span></span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٤</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل:</strong> <span class="ar-math"><span class="ar-frac"><span class="num">٨÷٤</span><span class="denom">١٢÷٤</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span>.
                        </div>
                    </div>

                    <!-- س4 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٤)</strong> أي زوج من الكسور التالية يمثل كسرين متكافئين؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٦</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٨</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٥</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٧</span></span></span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">١٠</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٨</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل:</strong> كلاهما يكافئ النصف (<span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>): <span class="ar-math"><span class="ar-frac"><span class="num">٣÷٣</span><span class="denom">٦÷٣</span></span> = <span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span> و <span class="ar-math"><span class="ar-frac"><span class="num">٤÷٤</span><span class="denom">٨÷٤</span></span> = <span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>.
                        </div>
                    </div>
                </div>

                <!-- ب: الصواب والخطأ -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ب</span> السؤال الثاني: ضع علامة (✓) أو (✗) (٣ درجات):</h4>

                    <div class="tf-item">
                        <div class="tf-text"><strong>١)</strong> شريط الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span> يطابق تماماً في الطول شريطين من فئة <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> ربعان يشكلان نصفاً: <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span> + <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٢)</strong> إضافة العدد نفسه إلى بسط ومقام كسر يعطي كسراً مكافئاً له دائماً. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-wrong">العبارة خاطئة (✗)</span>
                            <div class="inline-solution-block">
                                <strong>التصحيح:</strong> الجمع لا يعطي تكافؤاً؛ التكافؤ ينتج فقط عن <strong>ضرب أو قسمة</strong> حدي الكسر على نفس العدد غير الصفر.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٣)</strong> تسمى عملية تجزئة أشرطة الكسور إلى أجزاء أكبر بقسمة حديها عملية تبسيط الكسر. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> مطابق لما ورد في استكشاف معمل الرياضيات ص ١٤٦.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ج: مسألة تطبيقية -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ج</span> السؤال الثالث: مسألة النمذجة الرياضية (٣ درجات):</h4>
                    <div class="q-card">
                        <div class="q-text">اكتب كسرين مكافئين للكسر <span class="ar-math"><span class="ar-frac"><span class="num">٤</span><span class="denom">٦</span></span></span>، أحدهما بقسمة البسط والمقام على قاسم مشترك، والآخر بضربهما في عدد من اختيارك.</div>
                        <div class="student-work-area">
                            <em>مساحة إجابة الطالب وتطبيق القواعد:</em>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 الحل النموذجي:</strong><br>
                            ١) بالقسمة على <span class="ar-math">٢</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٤÷٢</span><span class="denom">٦÷٢</span></span> = <span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span> (وهو في أبسط صورة).<br>
                            ٢) بالضرب في <span class="ar-math">٢</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٤×٢</span><span class="denom">٦×٢</span></span> = <span class="ar-frac"><span class="num">٨</span><span class="denom">١٢</span></span></span> (أو بالضرب في أي عدد آخر).
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

RAW_WS_5 = r"""
        <!-- ورقة عمل ٥: الدرس (٤-٢) تبسيط الكسور ومعمل ص ١٥١ -->
        <article class="worksheet-card" id="ws-5-lesson4-2-simplifying">
            __TOOLBAR__
            __HEADER__

            <div class="ws-title-strip">
                <h3>ورقة عمل واختبار نهائي: الدرس (٤-٢) تبسيط الكسور ومعمل الأعداد الكسرية والكسور غير الفعلية</h3>
                <span class="page-ref-badge">كتاب الطالب: ص ١٤٧ – ١٥١</span>
            </div>

            <!-- معلومات الطالب -->
            <div class="student-info-grid">
                <div><strong>اسم الطالب:</strong> ............................................................</div>
                <div><strong>الصف:</strong> السادس الابتدائي ( ... )</div>
                <div><strong>التاريخ:</strong> ..... / ..... / ١٤٤٨ هـ</div>
                <div><strong>الدرجة المستحقة:</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / ٢٠</div>
            </div>

            <div class="ws-body">
                <!-- أ: الاختيار من متعدد -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">أ</span> السؤال الأول: اختر الإجابة الصحيحة علمياً ورياضياً (٤ درجات):</h4>

                    <!-- س1 -->
                    <div class="q-card">
                        <div class="q-text"><strong>١)</strong> الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١٨</span><span class="denom">٢٤</span></span></span> مكتوباً في أبسط صورة هو:</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٩</span><span class="denom">١٢</span></span></span></div>
                            <div class="mcq-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٨</span></span></span></div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٣</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل النموذجية على المسألة:</strong><br>
                            ق.م.أ للعددين <span class="ar-math">١٨</span> و <span class="ar-math">٢٤</span> هو <span class="ar-math">٦</span>. بالقسمة على <span class="ar-math">٦</span>: <span class="ar-math"><span class="ar-frac"><span class="num">١٨÷٦</span><span class="denom">٢٤÷٦</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span>.
                        </div>
                    </div>

                    <!-- س2 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٢)</strong> في حديقة <span class="ar-math">٢١</span> طائر حسون من أصل <span class="ar-math">٣٥</span> طائراً. اكتب الكسر الدال على طيور الحسون في أبسط صورة (ص ١٤٨):</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٢</span><span class="denom">٥</span></span></span></div>
                            <div class="mcq-opt correct-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٣</span><span class="denom">٧</span></span></span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٥</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل:</strong> كلا العددين يقبل القسمة على <span class="ar-math">٧</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٢١÷٧</span><span class="denom">٣٥÷٧</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٥</span></span></span>.
                        </div>
                    </div>

                    <!-- س3 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٣)</strong> أي الكسور التالية مكتوب في أبسط صورة أصلاً ولا يمكن تبسيطه أكثر؟</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">١٠</span></span></span></div>
                            <div class="mcq-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٩</span><span class="denom">١٥</span></span></span></div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٥</span><span class="denom">٧</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">١٢</span><span class="denom">١٦</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة الحل:</strong> العددان <span class="ar-math">٥</span> و <span class="ar-math">٧</span> أوليان وقاسمهما المشترك الوحيد هو <span class="ar-math">١</span>، إذن الكسر في أبسط صورة.
                        </div>
                    </div>

                    <!-- س4 -->
                    <div class="q-card">
                        <div class="q-text"><strong>٤)</strong> الكسر غير الفعلي المكافئ للعدد الكسري <span class="ar-math">٢ <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span></span> هو (معمل ص ١٥١):</div>
                        <div class="mcq-options-grid">
                            <div class="mcq-opt">أ) <span class="ar-math"><span class="ar-frac"><span class="num">٦</span><span class="denom">٤</span></span></span></div>
                            <div class="mcq-opt">ب) <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٤</span></span></span></div>
                            <div class="mcq-opt correct-opt">ج) <span class="ar-math"><span class="ar-frac"><span class="num">٩</span><span class="denom">٤</span></span></span> <span class="correct-badge">✓ الإجابة الصحيحة</span></div>
                            <div class="mcq-opt">د) <span class="ar-math"><span class="ar-frac"><span class="num">٨</span><span class="denom">٤</span></span></span></div>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 طريقة التحويل:</strong> <span class="ar-math">٢ <span class="ar-frac"><span class="num">١</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">(٢×٤)+١</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">٨+١</span><span class="denom">٤</span></span> = <span class="ar-frac"><span class="num">٩</span><span class="denom">٤</span></span></span>.
                        </div>
                    </div>
                </div>

                <!-- ب: الصواب والخطأ -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ب</span> السؤال الثاني: ضع علامة (✓) أو (✗) مع تصحيح الخطأ إن وجد (٣ درجات):</h4>

                    <div class="tf-item">
                        <div class="tf-text"><strong>١)</strong> يكون الكسر في أبسط صورة إذا كان القاسم المشترك الأكبر لبسطه ومقامه هو <span class="ar-math">١</span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> هذا هو التعريف الدقيق المعتمد لكتاب الرياضيات للصف السادس ص ١٤٨.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٢)</strong> يسمى الكسر <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٤</span></span></span> كسراً فعلياً لأن بسطه أكبر من مقامه. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-wrong">العبارة خاطئة (✗)</span>
                            <div class="inline-solution-block">
                                <strong>التصحيح:</strong> يسمى <strong>كسراً غير فعلي</strong> (Improper Fraction)؛ لأن الكسر الفعلي يكون بسطه أصغر من مقامه.
                            </div>
                        </div>
                    </div>

                    <div class="tf-item">
                        <div class="tf-text"><strong>٣)</strong> تبسيط الكسر <span class="ar-math"><span class="ar-frac"><span class="num">١٠</span><span class="denom">٢٠</span></span></span> هو <span class="ar-math"><span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>. <span class="student-mark-box">( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )</span></div>
                        <div class="tf-ans-box">
                            <span class="tf-badge tf-correct">العبارة صحيحة (✓)</span>
                            <div class="inline-solution-block">
                                <strong>التبرير:</strong> بقسمة البسط والمقام على <span class="ar-math">١٠</span>: <span class="ar-math"><span class="ar-frac"><span class="num">١٠÷١٠</span><span class="denom">٢٠÷١٠</span></span> = <span class="ar-frac"><span class="num">١</span><span class="denom">٢</span></span></span>.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- ج: المسائل المقالية -->
                <div class="ws-section-box">
                    <h4 class="ws-sec-heading"><span class="badge-num">ج</span> السؤال الثالث: المسائل التطبيقية (٣ درجات):</h4>
                    
                    <div class="q-card">
                        <div class="q-text"><strong>مسألة المشي الرياضي:</strong> قضى عمر <span class="ar-math">٤٥</span> دقيقة في المشي بحديقة الروضة في جدة. اكتب الكسر الاعتيادي في أبسط صورة الذي يمثل هذا الوقت من الساعة الكاملة (<span class="ar-math">٦٠</span> دقيقة)، ثم حول الكسر غير الفعلي <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٣</span></span></span> إلى عدد كسري.</div>
                        <div class="student-work-area">
                            <em>مساحة إجابة الطالب وحساب التبسيط والتحويل:</em>
                        </div>
                        <div class="inline-solution-block">
                            <strong>💡 الحل التفصيلي:</strong><br>
                            ١) كسر الوقت = <span class="ar-math"><span class="ar-frac"><span class="num">٤٥</span><span class="denom">٦٠</span></span></span>. ق.م.أ للعددين <span class="ar-math">٤٥</span> و <span class="ar-math">٦٠</span> هو <span class="ar-math">١٥</span>.<br>
                            بقسمة حدي الكسر على <span class="ar-math">١٥</span>: <span class="ar-math"><span class="ar-frac"><span class="num">٤٥÷١٥</span><span class="denom">٦٠÷١٥</span></span> = <span class="ar-frac"><span class="num">٣</span><span class="denom">٤</span></span></span> من الساعة (ثلاثة أرباع الساعة).<br>
                            ٢) لتحويل <span class="ar-math"><span class="ar-frac"><span class="num">٧</span><span class="denom">٣</span></span></span>: نقسم <span class="ar-math">٧÷٣ = ٢</span> والباقي <span class="ar-math">١</span>. إذن العدد الكسري هو: <strong><span class="ar-math">٢ <span class="ar-frac"><span class="num">١</span><span class="denom">٣</span></span></span></strong>.
                        </div>
                    </div>
                </div>
            </div>
            __FOOTER__
        </article>
"""

WORKSHEETS_SECTION_END = r"""
    </section><!-- /#section-worksheets -->
"""

def get_all_worksheets_html():
    w1 = RAW_WS_1.replace("__TOOLBAR__", make_ws_toolbar("ws-1-ch3-test")).replace("__HEADER__", make_school_header("اختبار الفصل ٣ والاختبار التراكمي ٣", "ورقة عمل وتقويم")).replace("__FOOTER__", make_teacher_footer())
    w2 = RAW_WS_2.replace("__TOOLBAR__", make_ws_toolbar("ws-2-ch4-prep")).replace("__HEADER__", make_school_header("تهيئة الفصل الرابع (الكسور الاعتيادية)", "ورقة عمل وتقويم")).replace("__FOOTER__", make_teacher_footer())
    w3 = RAW_WS_3.replace("__TOOLBAR__", make_ws_toolbar("ws-3-lesson4-1-gcf")).replace("__HEADER__", make_school_header("الدرس ٤-١ (القاسم المشترك الأكبر)", "ورقة عمل وتقويم")).replace("__FOOTER__", make_teacher_footer())
    w4 = RAW_WS_4.replace("__TOOLBAR__", make_ws_toolbar("ws-4-lab-equiv-fractions")).replace("__HEADER__", make_school_header("معمل الرياضيات (الكسور المتكافئة)", "ورقة عمل وتقويم")).replace("__FOOTER__", make_teacher_footer())
    w5 = RAW_WS_5.replace("__TOOLBAR__", make_ws_toolbar("ws-5-lesson4-2-simplifying")).replace("__HEADER__", make_school_header("الدرس ٤-٢ وتبسيط الكسور والأعداد الكسرية", "ورقة عمل وتقويم")).replace("__FOOTER__", make_teacher_footer())

    return (
        WORKSHEETS_SECTION_START +
        w1 + w2 + w3 + w4 + w5 +
        WORKSHEETS_SECTION_END
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    content = get_all_worksheets_html()
    with open('section_6b_worksheets.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"section_6b_worksheets.html written successfully! Total length: {len(content)} chars.")
