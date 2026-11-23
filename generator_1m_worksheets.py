# -*- coding: utf-8 -*-
"""
generator_1m_worksheets.py: Worksheets for Grade 7 (1m) pages 109 to 127:
- Worksheet 3-3: معادلات الضرب
- Worksheet 3-4: استراتيجية حل المسألة (الحل عكسياً)
- Mid-Chapter 3 Quiz: اختبار منتصف الفصل الثالث
- Worksheet 3-5: المعادلات ذات الخطوتين
- Worksheet 3-6: القياس: المحيط والمساحة
Features:
- Official school header with Base64 logo
- Teacher signature at bottom-left
- Top toolbar with toggle button (hidden in PDF print)
- Inline answers directly on each question (badges, explanation, problem-solution-inline)
- Strictly Eastern Arabic numerals (٠-٩)
"""

from generator_1m_header_styles import make_school_header, make_teacher_footer, make_ws_toolbar

WORKSHEETS_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثالث: أوراق العمل والاختبارات التطبيقية مع أزرار إظهار الحل         -->
    <!-- ========================================================================= -->
    <section id="worksheets-section" class="master-section page-break">
        <div class="section-header-banner worksheets">
            <h2>📝 القسم الثالث: أوراق العمل والاختبارات التطبيقية (متتالية)</h2>
            <span class="section-badge">مزودة بأزرار إظهار الإجابة المباشرة على المسائل (مخصصة للمعلم ومحجوبة عند الطباعة)</span>
        </div>
"""

RAW_WS_3_3 = r"""
        <!-- ورقة عمل الدرس 3-3 -->
        <article class="worksheet-paper" id="ws-3-3">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٣-٣) معادلات الضرب</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول: اختيار من متعدد -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل فقرة مما يلي: [٣ درجات]</div>
                
                <div style="margin-bottom: 16px;">
                    <p><strong>١) ما هو حل المعادلة: $\text{٦}\text{س} = \text{٤٢}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} = \text{٦}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{س} = \text{٧}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} = \text{٣٦}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} = \text{٤٨}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بقسمة كلا الطرفين على معامل المتغير (٦): $\text{س} = \frac{\text{٤٢}}{\text{٦}} = \text{٧}$. التحقق: $\text{٦} \times \text{٧} = \text{٤٢}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) ما هو حل المعادلة: $\text{–}\text{٤}\text{ص} = \text{٣٦}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{ص} = \text{–}\text{٩}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{ص} = \text{٩}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{ص} = \text{–}\text{٨}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{ص} = \text{–}\text{١٤٤}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بقسمة كلا الطرفين على (–٤): $\text{ص} = \frac{\text{٣٦}}{\text{–}\text{٤}} = \text{–}\text{٩}$ (قسمة موجب على سالب تعطي ناتجاً سالباً).
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٣) إذا قطعت سيارة مسافة ٣٦٠ كم في ٤ ساعات، فما متوسط سرعتها بالساعة باستعمال الصيغة $ف = ع \times ن$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) ٨٠ كم/س</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) ٨٥ كم/س</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) ٩٠ كم/س</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ١٠٠ كم/س</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> $ف = ع \times ن \implies \text{٣٦٠} = ع \times \text{٤} \implies ع = \frac{\text{٣٦٠}}{\text{٤}} = \text{٩٠}$ كم/ساعة.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني: صح أو خطأ -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗) مع تصحيح الخطأ إن وجد: [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> العملية العكسية المستعملة لحل معادلة الضرب هي عملية القسمة.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ]</span>
                    </div>
                    <div>
                        <strong>٢)</strong> حل المعادلة $\text{–}\text{٥}\text{س} = \text{–}\text{٣٠}$ هو $\text{س} = \text{–}\text{٦}$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: قسمة عدد سالب على عدد سالب تعطي عدداً موجباً: $\text{س} = \frac{\text{–}\text{٣٠}}{\text{–}\text{٥}} = \text{٦}$.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث: حل معادلات -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حُلَّ المعادلات الآتية وتحقق من صحة حلك: [٣ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{–}\text{٩}\text{م} = \text{٧٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بقسمة كلا الطرفين على معامل المتغير (–٩):<br>
                        $$\text{م} = \frac{\text{٧٢}}{\text{–}\text{٩}} \implies \text{م} = \text{–}\text{٨}$$<br>
                        • <strong>التحقق:</strong> التعويض في المعادلة الأصلية: $\text{–}\text{٩} \times (\text{–}\text{٨}) = \text{٧٢}$ (الطرفان متساويان ✓).
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{١٥}\text{ك} = \text{–}\text{٧٥}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بقسمة كلا الطرفين على ١٥:<br>
                        $$\text{ك} = \frac{\text{–}\text{٧٥}}{\text{١٥}} \implies \text{ك} = \text{–}\text{٥}$$<br>
                        • <strong>التحقق:</strong> التعويض في المعادلة الأصلية: $\text{١٥} \times (\text{–}\text{٥}) = \text{–}\text{٧٥}$ (الطرفان متساويان ✓).
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع: مسألة واقعية -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة من واقع الحياة: [درجتان]</div>
                <p>اشترى أحمد ٨ وجبات متطابقة لأفراد أسرته بمبلغ إجمالي قدره ١٩٢ ريالاً. اكتب معادلة ضرب تمثل ثمن الوجبة الواحدة (و)، ثم حلها لإيجاد ثمن الوجبة.</p>
                <div class="student-answer-space">المعادلة والحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • صياغة المعادلة: $\text{٨}\text{و} = \text{١٩٢}$<br>
                    • بقسمة الطرفين على ٨: $\text{و} = \frac{\text{١٩٢}}{\text{٨}} = \text{٢٤}$ ريالاً.<br>
                    • إذن ثمن الوجبة الواحدة هو <strong>٢٤ ريالاً</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_3_4 = r"""
        <!-- ورقة عمل الدرس 3-4 -->
        <article class="worksheet-paper" id="ws-3-4">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل وتدريب:</strong> الدرس (٣-٤) استراتيجية حل المسألة (الحل عكسياً)</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة: [٣ درجات]</div>
                <div style="margin-bottom: 16px;">
                    <p><strong>١) فكر فهد في عدد، ضربه في ٤، ثم أضاف إلى الناتج ٦، فكان الناتج النهائي ٣٠. ما هو هذا العدد؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) ٥</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) ٦</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) ٧</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ٨</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بالعكس: $\text{٣٠} \text{–} \text{٦} = \text{٢٤}$، ثم $\text{٢٤} \div \text{٤} = \text{٦}$. التحقق: $٦ \times ٤ + ٦ = ٢٤ + ٦ = ٣٠$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) العملية العكسية لـ: "أنفق نصف ما معه" في الحل العكسي هي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) القسمة على ٢</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) الضرب في ٢</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) إضافة ٢</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) طرح ٢</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> تنصيف الشيء يعني قسمته على ٢، والعملية العكسية المقابلة للقسمة على ٢ هي الضرب في ٢.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني: مسائل كتابية مفصلة -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: استعمل استراتيجية "الحل عكسياً" لحل المسائل التالية موضحاً خطواتك: [٧ درجات]</div>
                
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) مسألة النقود:</strong> مع فيصل مبلغ من المال، اشترى كتاباً بـ ٢٥ ريالاً، ثم اشترى وجبة غداء بـ ١٥ ريالاً، وتصدق بـ ١٠ ريالات، فتبقى معه في النهاية ٥٠ ريالاً. كم ريالاً كان مع فيصل في البداية؟</p>
                    <div class="student-answer-space">خطوات الحل العكسي والتحقق للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر بالمسار العكسي:</strong><br>
                        • نبدأ من المبلغ المتبقي في النهاية: ٥٠ ريالاً.<br>
                        • نعكس التصدق بـ ١٠ ريالات (نضيف ١٠): $\text{٥٠} + \text{١٠} = \text{٦٠}$ ريالاً.<br>
                        • نعكس شراء الغداء بـ ١٥ ريالاً (نضيف ١٥): $\text{٦٠} + \text{١٥} = \text{٧٥}$ ريالاً.<br>
                        • نعكس شراء الكتاب بـ ٢٥ ريالاً (نضيف ٢٥): $\text{٧٥} + \text{٢٥} = \text{١٠٠}$ ريال.<br>
                        • <strong>المبلغ الأصلي مع فيصل:</strong> <strong>١٠٠ ريال</strong>.<br>
                        • <strong>التحقق:</strong> $١٠٠ \text{–} ٢٥ = ٧٥ \text{–} ١٥ = ٦٠ \text{–} ١٠ = ٥٠$ ريالاً (صحيح ✓).
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) مسألة الحافلة:</strong> انطلقت حافلة ركاب من المحطة المركزية، وفي المحطة الأولى نزل ٥ ركاب وصعد راكبان. وفي المحطة الثانية نزل نصف الركاب الموجودين، فوصلت الحافلة إلى محطتها الأخيرة وبها ١٢ راكباً. كم راكباً كان في الحافلة عند انطلاقها؟</p>
                    <div class="student-answer-space">خطوات الحل العكسي للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • عدد الركاب في المحطة الأخيرة = ١٢ راكباً.<br>
                        • نعكس نزول نصف الركاب (نضرب في ٢): $\text{١٢} \times \text{٢} = \text{٢٤}$ راكباً.<br>
                        • نعكس صعود راكبين (نطرح ٢): $\text{٢٤} \text{–} \text{٢} = \text{٢٢}$ راكباً.<br>
                        • نعكس نزول ٥ ركاب (نضيف ٥): $\text{٢٢} + \text{٥} = \text{٢٧}$ راكباً.<br>
                        • <strong>عدد الركاب عند الانطلاق:</strong> <strong>٢٧ راكباً</strong>.<br>
                        • <strong>التحقق:</strong> $٢٧ \text{–} ٥ = ٢٢ + ٢ = ٢٤ \div ٢ = ١٢$ راكباً (صحيح ✓).
                    </div>
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_MID_QUIZ_1M = r"""
        <!-- اختبار منتصف الفصل الثالث -->
        <article class="worksheet-paper" id="ws-mid-quiz">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>اختبار تشخيصي وتقويمي:</strong> منتصف الفصل الثالث (ص ١١٦)</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة النهائية:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٥ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة علمياً: [٤ درجات]</div>
                <div style="margin-bottom: 14px;">
                    <p><strong>١) حل المعادلة: $\text{س} + \text{٩} = \text{٤}$ هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} = \text{٥}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{س} = \text{–}\text{٥}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} = \text{١٣}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} = \text{–}\text{١٣}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بطرح ٩ من الطرفين: $\text{س} = \text{٤} \text{–} \text{٩} = \text{–}\text{٥}$.
                    </div>
                </div>

                <div style="margin-bottom: 14px;">
                    <p><strong>٢) حل المعادلة: $\text{–}\text{٧}\text{ص} = \text{–}\text{٥٦}$ هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{ص} = \text{–}\text{٨}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{ص} = \text{٨}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{ص} = \text{–}\text{٤٩}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{ص} = \text{–}\text{٦٣}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بالقسمة على (–٧): $\text{ص} = \frac{\text{–}\text{٥٦}}{\text{–}\text{٧}} = \text{٨}$ (سالب $\div$ سالب = موجب).
                    </div>
                </div>

                <div style="margin-bottom: 14px;">
                    <p><strong>٣) التعبير الجبري الذي يمثل: "أقل من عدد بمقدار ٦ يساوي ١٤":</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} \text{–} \text{٦} = \text{١٤}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{٦} \text{–} \text{س} = \text{١٤}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} + \text{٦} = \text{١٤}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{٦}\text{س} = \text{١٤}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> "أقل من عدد بمقدار ٦" تعني طرح ٦ من المتغير: $\text{س} \text{–} \text{٦}$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗): [٣ درجات]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> المعادلة هي جملة رياضية تحتوي على إشارة مساواة (=) تفصل بين عبارتين.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ]</span>
                    </div>
                    <div>
                        <strong>٢)</strong> لحل المعادلة $\text{س} \text{–} \text{٥} = \text{١٢}$ نقوم بطرح ٥ من الطرفين.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: العملية العكسية للطرح هي إضافة ٥ للطرفين.</span>
                    </div>
                    <div>
                        <strong>٣)</strong> إذا كانت سرعة طائرة ٨٠٠ كم/ساعة واستغرقت ٣ ساعات، فإن المسافة المقطوعة هي ٢٤٠٠ كم.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ] — $ف = ع \times ن = ٨٠٠ \times ٣ = ٢٤٠٠$ كم.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المعادلات الآتية وتحقق من صحة حلك: [٥ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{ص} \text{–} \text{١٥} = \text{–}\text{٢٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بإضافة ١٥ لكلا الطرفين: $\text{ص} = \text{–}\text{٢٢} + \text{١٥} \implies \text{ص} = \text{–}\text{٧}$.<br>
                        • <strong>التحقق:</strong> $\text{–}\text{٧} \text{–} \text{١٥} = \text{–}\text{٢٢}$ (صحيحة ✓).
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{–}\text{٨}\text{م} = \text{٩٦}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بقسمة كلا الطرفين على (–٨): $\text{م} = \frac{\text{٩٦}}{\text{–}\text{٨}} \implies \text{م} = \text{–}\text{١٢}$.<br>
                        • <strong>التحقق:</strong> $\text{–}\text{٨} \times (\text{–}\text{١٢}) = \text{٩٦}$ (صحيحة ✓).
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة لفظية: [٣ درجات]</div>
                <p>قُسم عدد طلاب فصل إلى ٤ مجموعات متساوية لإجراء تجربة علمية، فكان في كل مجموعة ٨ طلاب. اكتب معادلة تمثل عدد طلاب الفصل (ط)، ثم حلها لإيجاد إجمالي عدد الطلاب.</p>
                <div class="student-answer-space">المعادلة والحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • صياغة المعادلة: $\frac{\text{ط}}{\text{٤}} = \text{٨}$<br>
                    • بضرب كلا الطرفين في ٤: $\text{ط} = \text{٨} \times \text{٤} = \text{٣٢}$ طالباً.<br>
                    • إجمالي عدد طلاب الفصل هو <strong>٣٢ طالباً</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_3_5 = r"""
        <!-- ورقة عمل الدرس 3-5 -->
        <article class="worksheet-paper" id="ws-3-5">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٣-٥) المعادلات ذات الخطوتين</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل فقرة: [٣ درجات]</div>
                
                <div style="margin-bottom: 16px;">
                    <p><strong>١) ما هو حل المعادلة: $\text{٢}\text{س} + \text{٣} = \text{١٥}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} = \text{٦}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{س} = \text{٩}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} = \text{١٢}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} = \text{٢٤}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بطرح ٣: $\text{٢}\text{س} = \text{١٢} \implies$ بالقسمة على ٢: $\text{س} = \text{٦}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) ما هو حل المعادلة: $\text{–}\text{٣}\text{ص} \text{–} \text{٥} = \text{١٦}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{ص} = \text{–}\text{٧}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{ص} = \text{٧}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{ص} = \text{–}\text{٣}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{ص} = \text{–}\text{١١}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بإضافة ٥: $\text{–}\text{٣}\text{ص} = \text{٢١} \implies$ بالقسمة على (–٣): $\text{ص} = \text{–}\text{٧}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٣) أول خطوة صحيحة لحل المعادلة $\text{٤}\text{س} \text{–} \text{٧} = \text{١٣}$ هي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) قسمة الطرفين على ٤</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) إضافة ٧ إلى كلا الطرفين</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) طرح ٧ من كلا الطرفين</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ضرب الطرفين في ٤</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> القاعدة الذهبية لحل المعادلات ذات الخطوتين هي التخلص أولاً من الجمع أو الطرح (الثابت) قبل التخلص من المعامل المضروب.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗): [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> عند حل المعادلة ذات الخطوتين نتخلص من معامل المتغير المضروب أولاً ثم نتخلص من الثابت.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: نتخلص من الثابت المضاف أو المطروح أولاً ثم نقسم على المعامل.</span>
                    </div>
                    <div>
                        <strong>٢)</strong> حل المعادلة $\frac{\text{س}}{\text{٣}} + \text{٤} = \text{٩}$ هو $\text{س} = \text{١٥}$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ] — بطرح ٤: $\frac{\text{س}}{\text{٣}} = \text{٥} \implies \text{س} = \text{١٥}$.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حُلَّ المعادلات الآتية موضحاً خطواتك بالتفصيل: [٣ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{٥}\text{س} + \text{٨} = \text{–}\text{١٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بطرح ٨ من كلا الطرفين: $\text{٥}\text{س} = \text{–}\text{١٢} \text{–} \text{٨} \implies \text{٥}\text{س} = \text{–}\text{٢٠}$<br>
                        • بقسمة كلا الطرفين على ٥: $\text{س} = \frac{\text{–}\text{٢٠}}{\text{٥}} \implies \text{س} = \text{–}\text{٤}$<br>
                        • <strong>التحقق:</strong> $\text{٥}(\text{–}\text{٤}) + \text{٨} = \text{–}\text{٢٠} + \text{٨} = \text{–}\text{١٢}$ (صحيحة ✓).
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{–}\text{٢}\text{ص} + \text{١١} = \text{–}\text{٥}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بطرح ١١ من كلا الطرفين: $\text{–}\text{٢}\text{ص} = \text{–}\text{٥} \text{–} \text{١١} \implies \text{–}\text{٢}\text{ص} = \text{–}\text{١٦}$<br>
                        • بقسمة كلا الطرفين على (–٢): $\text{ص} = \frac{\text{–}\text{١٦}}{\text{–}\text{٢}} \implies \text{ص} = \text{٨}$<br>
                        • <strong>التحقق:</strong> $\text{–}\text{٢}(\text{٨}) + \text{١١} = \text{–}\text{١٦} + \text{١١} = \text{–}\text{٥}$ (صحيحة ✓).
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة تطبيقية واقعية: [درجتان]</div>
                <p>اشترك بدر في نادٍ رياضي، فدفع رسوم تسجيل قدرها ٧٠ ريالاً، واشتراكاً شهرياً مقداره ٤٠ ريالاً عن كل شهر. إذا دفع بدر إجمالي ٣١٠ ريالات، فكم شهراً استمر اشتراكه؟</p>
                <div class="student-answer-space">المعادلة والحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • نفرض عدد الأشهر = ش.<br>
                    • المعادلة: $\text{٤٠}\text{ش} + \text{٧٠} = \text{٣١٠}$<br>
                    • بطرح ٧٠ من الطرفين: $\text{٤٠}\text{ش} = \text{٢٤٠}$<br>
                    • بقسمة الطرفين على ٤٠: $\text{ش} = \frac{\text{٢٤٠}}{\text{٤٠}} = \text{٦}$ أشهر.<br>
                    • إذن استمر اشتراك بدر لمدة <strong>٦ أشهر</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_3_6 = r"""
        <!-- ورقة عمل الدرس 3-6 -->
        <article class="worksheet-paper" id="ws-3-6">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٣-٦) القياس: المحيط والمساحة</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل فقرة: [٣ درجات]</div>
                
                <div style="margin-bottom: 16px;">
                    <p><strong>١) مستطيل طوله ٨ سم وعرضه ٥ سم، فإن محيطه يساوي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) ١٣ سم</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) ٢٦ سم</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) ٤٠ سم</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ٤٠ سم²</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> المحيط $مح = ٢ل + ٢ض = ٢(\text{٨}) + ٢(\text{٥}) = \text{١٦} + \text{١٠} = \text{٢٦}$ سم.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) مستطيل مساحته ٤٨ م² وعرضه ٦ م، فإن طوله (ل) يساوي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) ٧ م</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) ٨ م</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) ١٢ م</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ٤٢ م</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> $\text{المساحة} = \text{الطول} \times \text{العرض} \implies \text{٤٨} = ل \times \text{٦} \implies ل = \frac{\text{٤٨}}{\text{٦}} = \text{٨}$ أمتار.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٣) مربع طول ضلعه ٧ سم، فإن مساحته تساوي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) ١٤ سم²</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) ٢٨ سم²</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) ٤٩ سم²</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) ٤٩ سم</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> مساحة المربع = $ل \times ل = \text{٧} \times \text{٧} = \text{٤٩}$ سم².
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗): [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> تُقاس المساحة بوحدات الطول المربعة، بينما يُقاس المحيط بوحدات الطول الخطية.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ]</span>
                    </div>
                    <div>
                        <strong>٢)</strong> لحساب كمية الطلاء اللازمة لدهان جدار غرفة، نحتاج إلى حساب محيط الجدار.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: الطلاء يغطي السطح بالكامل؛ لذا يلزم حساب المساحة وليس المحيط.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: أوجد القياسات الهندسية المطلوبة: [٣ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) حديقة مستطيلة الشكل محيطها ٥٤ متراً وطولها ١٧ متراً. أوجد عرض الحديقة (ض).</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • قانون المحيط: $مح = ٢ل + ٢ض$<br>
                        • بالتعويض: $\text{٥٤} = ٢(\text{١٧}) + ٢ض \implies \text{٥٤} = \text{٣٤} + ٢ض$<br>
                        • بطرح ٣٤ من الطرفين: $٢ض = \text{٢٠}$<br>
                        • بالقسمة على ٢: $ض = \text{١٠}$ أمتار.<br>
                        • إذن عرض الحديقة هو <strong>١٠ أمتار</strong>.
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) صالة رياضية مستطيلة الشكل أبعادها ١٢ متراً و ٩ أمتار. احسب كلاً من محيطها ومساحتها.</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • <strong>المحيط:</strong> $مح = ٢(ل + ض) = ٢(\text{١٢} + \text{٩}) = ٢(\text{٢١}) = \text{٤٢}$ متراً.<br>
                        • <strong>المساحة:</strong> $م = ل \times ض = \text{١٢} \times \text{٩} = \text{١٠٨}$ أمتار مربعة (م²).
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة واقعية ومهارات تفكير: [درجتان]</div>
                <p>يريد مقاول تركيب سياج حول أرض فضاء مستطيلة طولها ٢٥ متراً وعرضها ١٥ متراً. فإذا كانت تكلفة المتر الواحد من السياج ٤٠ ريالاً، فكم تبلغ التكلفة الإجمالية لتركيب السياج؟</p>
                <div class="student-answer-space">الحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • الخطوة الأولى (حساب المحيط): $مح = ٢(\text{٢٥}) + ٢(\text{١٥}) = \text{٥٠} + \text{٣٠} = \text{٨٠}$ متراً من السياج.<br>
                    • الخطوة الثانية (حساب التكلفة الإجمالية): $\text{٨٠} \times \text{٤٠} = \text{٣٢٠٠}$ ريال.<br>
                    • التكلفة الكلية لتركيب السياج هي <strong>٣٢٠٠ ريال</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

def get_all_worksheets_html():
    w_3_3 = RAW_WS_3_3.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٣-٣)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-3-3")).replace("__FOOTER__", make_teacher_footer())
    w_3_4 = RAW_WS_3_4.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٣-٤)", "استراتيجية حل المسألة")).replace("__TOOLBAR__", make_ws_toolbar("ws-3-4")).replace("__FOOTER__", make_teacher_footer())
    w_mid = RAW_WS_MID_QUIZ_1M.replace("__HEADER__", make_school_header("اختبار منتصف الفصل الثالث", "اختبار تشخيصي وتقويمي")).replace("__TOOLBAR__", make_ws_toolbar("ws-mid-quiz")).replace("__FOOTER__", make_teacher_footer())
    w_3_5 = RAW_WS_3_5.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٣-٥)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-3-5")).replace("__FOOTER__", make_teacher_footer())
    w_3_6 = RAW_WS_3_6.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٣-٦)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-3-6")).replace("__FOOTER__", make_teacher_footer())
    
    return (
        WORKSHEETS_SECTION_START +
        w_3_3 +
        w_3_4 +
        w_mid +
        w_3_5 +
        w_3_6 +
        "\n    </section><!-- /#worksheets-section -->\n"
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    html = get_all_worksheets_html()
    with open('section_1m_worksheets.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"section_1m_worksheets.html written successfully, length: {len(html)}")
