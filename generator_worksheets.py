# -*- coding: utf-8 -*-
"""
generator_worksheets.py: Worksheets for:
- Lesson 4-2
- Lesson 4-3
- Mid-Chapter 4 Quiz
- Algebra Lab
- Lesson 4-4
Features:
- Base64 Logo and official school header
- Teacher signature at bottom left
- Top toolbar with toggle button (hidden in print)
- Inline solutions on every question (badges, explanation, problem-solution-inline)
- Strictly Eastern Arabic numerals (٠-٩)
"""

from generator_header_styles import make_school_header, make_teacher_footer, make_ws_toolbar

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

RAW_WS_4_2 = r"""
        <!-- ورقة عمل الدرس 4-2 -->
        <article class="worksheet-paper" id="ws-4-2">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٤-٢) حل المتباينات بالضرب أو بالقسمة</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول: اختيار من متعدد -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة علمياً لكل فقرة مما يلي: [٣ درجات]</div>
                
                <!-- الفقرة 1 -->
                <div style="margin-bottom: 16px;">
                    <p><strong>١) ما هي مجموعة حل المتباينة: $\frac{\text{س}}{\text{٥}} \le \text{٤}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{س} \mid \text{س} \le \text{٩}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{س} \mid \text{س} \le \text{٢٠}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{س} \mid \text{س} \ge \text{٢٠}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{س} \mid \text{س} \le \text{١}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بضرب طرفي المتباينة في العدد الموجب (٥): $\text{س} \le \text{٤} \times \text{٥} \implies \text{س} \le \text{٢٠}$. ولا يتغير اتجاه رمز المتباينة لأن الضرب في عدد موجب.
                    </div>
                </div>

                <!-- الفقرة 2 -->
                <div style="margin-bottom: 16px;">
                    <p><strong>٢) ما هي مجموعة حل المتباينة: $\text{–}\text{٣}\text{ص} > \text{١٨}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{ص} \mid \text{ص} > \text{–}\text{٦}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{ص} \mid \text{ص} < \text{–}\text{٦}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{ص} \mid \text{ص} < \text{٦}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{ص} \mid \text{ص} > \text{٦}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بقسمة طرفي المتباينة على العدد السالب (–٣)، <strong>يتعين عكس اتجاه رمز المتباينة</strong> من ($>$) إلى ($<$): $\text{ص} < \frac{\text{١٨}}{\text{–}\text{٣}} \implies \text{ص} < \text{–}\text{٦}$.
                    </div>
                </div>

                <!-- الفقرة 3 -->
                <div style="margin-bottom: 16px;">
                    <p><strong>٣) التعبير الجبري الذي يمثل العبارة: «نصف عدد لا يقل عن ١٢» هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\frac{\text{١}}{\text{٢}}\text{ن} \le \text{١٢}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\frac{\text{١}}{\text{٢}}\text{ن} > \text{١٢}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\frac{\text{١}}{\text{٢}}\text{ن} \ge \text{١٢}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{٢}\text{ن} \ge \text{١٢}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> كلمة "لا يقل عن" تعني أكبر من أو يساوي ($\ge$)، ونصف العدد يكتب $\frac{\text{١}}{\text{٢}}\text{ن}$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني: صح أو خطأ -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أمام العبارة الصحيحة وعلامة (✗) أمام العبارة الخاطئة: [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> عند قسمة طرفي متباينة صحيحة على عدد سالب، يجب عكس اتجاه رمز المتباينة لتظل صحيحة.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ] — وفق خاصية القسمة في عدد سالب للمتباينات.</span>
                    </div>
                    <div>
                        <strong>٢)</strong> في المتباينة $\text{٢}\text{س} \ge \text{–}\text{٨}$ نعكس اتجاه رمز المتباينة لأن الطرف الأيسر عدد سالب.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: العكس يعتمد فقط على إشارة معامل المتغير (المقسوم عليه)، وهنا ٢ موجب فلا تنعكس الإشارة!</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث: حل ومثل بيانيا -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: أوجد مجموعة حل كل متباينة مما يلي ومثل الحل بيانياً على خط الأعداد: [٣ درجات]</div>
                
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{–}\frac{\text{٢}}{\text{٣}}\text{م} \le \text{١٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل والتمثيل البياني للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • نضرب طرفي المتباينة في النظير الضربي لمعامل المتغير وهو $(\text{–}\frac{\text{٣}}{\text{٢}})$.<br>
                        • بما أن العدد المضروب فيه سالب، نعكس اتجاه رمز المتباينة من ($\le$) إلى ($\ge$):<br>
                        $$\text{م} \ge \text{١٢} \times \left(\text{–}\frac{\text{٣}}{\text{٢}}\right) \implies \text{م} \ge \text{–}\text{١٨}$$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{م} \mid \text{م} \ge \text{–}\text{١٨}\}$.<br>
                        • <strong>التمثيل البياني:</strong> رسم خط أعداد، وتحديد نقطة عند العدد (–١٨) بدائرة مغلقة $\bullet$، ورسم سهم متجه نحو اليمين إلى ما لا نهاية.
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{٤}\text{ك} > \text{–}\text{٢٨}$</strong></p>
                    <div class="student-answer-space">خطوات الحل والتمثيل البياني للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بقسمة الطرفين على العدد الموجب (٤):<br>
                        $$\text{ك} > \frac{\text{–}\text{٢٨}}{\text{٤}} \implies \text{ك} > \text{–}\text{٧}$$<br>
                        • لا نغير اتجاه الرمز لأننا قسمنا على عدد موجب.<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{ك} \mid \text{ك} > \text{–}\text{٧}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مفتوحة $\circ$ عند النقطة (–٧)، ورسم سهم متجه نحو اليمين.
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع: مسألة واقعية -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة من واقع الحياة (مهارات حل المشكلات): [درجتان]</div>
                <p>يريد خالد شراء دفاتر مدرسية سعر الدفتر الواحد ٦ ريالات، ومعه مبلغ لا يتجاوز ٤٢ ريالاً. اكتب متباينة تمثل عدد الدفاتر (د) التي يمكن لخالد شراؤها، ثم حلها مبيناً أكبر عدد ممكن من الدفاتر.</p>
                <div class="student-answer-space">المتباينة والحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • صياغة المتباينة: كلمة "لا يتجاوز" تعني أصغر من أو يساوي ($\le$): $\text{٦}\text{د} \le \text{٤٢}$<br>
                    • بالقسمة على ٦: $\text{د} \le \text{٧}$<br>
                    • <strong>التفسير:</strong> أكبر عدد من الدفاتر يمكن لخالد شراؤه دون تجاوز ميزانيته هو <strong>٧ دفاتر</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_4_3 = r"""
        <!-- ورقة عمل الدرس 4-3 -->
        <article class="worksheet-paper" id="ws-4-3">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٤-٣) حل المتباينات متعددة الخطوات</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول: اختيار من متعدد -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل فقرة: [٣ درجات]</div>
                
                <div style="margin-bottom: 16px;">
                    <p><strong>١) ما هي مجموعة حل المتباينة: $\text{٢}\text{س} + \text{٥} \ge \text{١٧}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{س} \mid \text{س} \ge \text{٦}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{س} \mid \text{س} \le \text{٦}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{س} \mid \text{س} \ge \text{١١}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{س} \mid \text{س} \ge \text{٢٢}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بطرح ٥ من الطرفين: $\text{٢}\text{س} \ge \text{١٢} \implies$ بالقسمة على ٢: $\text{س} \ge \text{٦}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) ما هي مجموعة حل المتباينة: $\text{–}\text{٤}\text{ص} \text{–} \text{٣} < \text{١٣}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{ص} \mid \text{ص} < \text{–}\text{٤}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{ص} \mid \text{ص} > \text{–}\text{٤}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{ص} \mid \text{ص} > \text{٤}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{ص} \mid \text{ص} < \text{٤}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بإضافة ٣ للطرفين: $\text{–}\text{٤}\text{ص} < \text{١٦} \implies$ بالقسمة على (–٤) وقلب الإشارة: $\text{ص} > \text{–}\text{٤}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٣) ما هي مجموعة حل المتباينة: $\text{٣}(\text{س} + \text{٢}) > \text{٣}\text{س} + \text{١٠}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) مجموعة الأعداد الحقيقية $\mathbb{R}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) المجموعة الخالية $\emptyset$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{س} \mid \text{س} > \text{٤}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{س} \mid \text{س} < \text{–}\text{٤}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بالتوزيع: $\text{٣}\text{س} + \text{٦} > \text{٣}\text{س} + \text{١٠}$. بطرح ٣س من الطرفين: $\text{٦} > \text{١٠}$ وهي عبارة خاطئة ومستحيلة، فمجموعة الحل هي $\emptyset$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني: صح أو خطأ -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗) مع التعليل: [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> المتباينة $\text{٥}\text{س} \text{–} \text{٢} \le \text{٥}\text{س} + \text{٣}$ مجموعة حلها هي مجموعة الأعداد الحقيقية $\mathbb{R}$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ] — بطرح ٥س يتبقى $\text{–}\text{٢} \le \text{٣}$ وهي عبارة عددية صحيحة دائماً.</span>
                    </div>
                    <div>
                        <strong>٢)</strong> أول خطوة صحيحة لحل المتباينة $\text{–}\text{٢}(\text{س} + \text{٤}) \ge \text{٦}$ هي طرح ٤ من الطرفين.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: القوس محمي بالضرب في –٢؛ لذا الخطوة الأولى هي فك القوس بالتوزيع أو قسمة الطرفين على –٢ أولاً.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث: حل مفصل -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينات التالية جبرياً ومثل الحل بيانياً: [٣ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{٧}\text{حـ} \text{–} \text{٢} \le \text{٣}\text{حـ} + \text{١٤}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بطرح ٣حـ من الطرفين: $\text{٤}\text{حـ} \text{–} \text{٢} \le \text{١٤}$<br>
                        • بإضافة ٢ للطرفين: $\text{٤}\text{حـ} \le \text{١٦}$<br>
                        • بالقسمة على ٤: $\text{حـ} \le \text{٤}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{حـ} \mid \text{حـ} \le \text{٤}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مغلقة $\bullet$ عند النقطة ٤ مع سهم متجه لليسار.
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{–}\text{٢}(\text{ف} + \text{٣}) > \text{٤}(\text{ف} \text{–} \text{٣})$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • فك الأقواس بالتوزيع في الطرفين: $\text{–}\text{٢}\text{ف} \text{–} \text{٦} > \text{٤}\text{ف} \text{–} \text{١٢}$<br>
                        • بإضافة ٢ف للطرفين: $\text{–}\text{٦} > \text{٦}\text{ف} \text{–} \text{١٢}$<br>
                        • بإضافة ١٢ للطرفين: $\text{٦} > \text{٦}\text{ف} \implies \text{ف} < \text{١}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{ف} \mid \text{ف} < \text{١}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مفتوحة $\circ$ عند النقطة ١ مع سهم متجه لليسار.
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع: مسألة تطبيقية -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة تطبيقية واقعية: [درجتان]</div>
                <p>تقدم إحدى شركات الاتصالات عرضين للإنترنت المنزلي: العرض الأول باشتراك شهري ثابت قدره ٨٠ ريالاً بالإضافة إلى ريالين عن كل جيجابايت إضافي. والعرض الثاني باشتراك ثابت قدره ٥٠ ريالاً بالإضافة إلى ٥ ريالات عن كل جيجابايت إضافي. بعد كم جيجابايت يصبح العرض الأول أكثر توفيراً للمشترك؟</p>
                <div class="student-answer-space">خطوات تكوين المتباينة وحلها للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • نفرض عدد الجيجابايت الإضافية = جـ.<br>
                    • تكلفة العرض الأول: $\text{٢}\text{جـ} + \text{٨٠}$ ، تكلفة العرض الثاني: $\text{٥}\text{جـ} + \text{٥٠}$<br>
                    • لكي يكون الأول أكثر توفيراً (أقل تكلفة): $\text{٢}\text{جـ} + \text{٨٠} < \text{٥}\text{جـ} + \text{٥٠}$<br>
                    • بطرح ٢جـ: $\text{٨٠} < \text{٣}\text{جـ} + \text{٥٠} \implies \text{٣٠} < \text{٣}\text{جـ} \implies \text{جـ} > \text{١٠}$<br>
                    • <strong>النتيجة:</strong> يصبح العرض الأول أوفر عندما يزيد استهلاك البيانات الإضافية عن <strong>١٠ جيجابايت</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_MID_QUIZ = r"""
        <!-- ورقة اختبار منتصف الفصل الرابع -->
        <article class="worksheet-paper" id="ws-mid-quiz">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>اختبار تشخيصي وتقويمي:</strong> اختبار منتصف الفصل الرابع (ص ١٤١)</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة النهائية:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٥ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل مما يأتي: [٤ درجات]</div>
                
                <div style="margin-bottom: 14px;">
                    <p><strong>١) حل المتباينة: $\text{س} \text{–} \text{٦} \ge \text{–}\text{٢}$ هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} \ge \text{٤}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{س} \le \text{٤}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} \ge \text{–}\text{٨}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} \le \text{–}\text{٨}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بإضافة ٦ للطرفين: $\text{س} \ge \text{–}\text{٢} + \text{٦} \implies \text{س} \ge \text{٤}$.
                    </div>
                </div>

                <div style="margin-bottom: 14px;">
                    <p><strong>٢) حل المتباينة: $\frac{\text{ص}}{\text{–}\text{٢}} < \text{٥}$ هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{ص} < \text{–}\text{١٠}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{ص} > \text{–}\text{١٠}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{ص} > \text{١٠}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{ص} < \text{١٠}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بالضرب في (–٢) مع عكس اتجاه الرمز: $\text{ص} > \text{–}\text{١٠}$.
                    </div>
                </div>

                <div style="margin-bottom: 14px;">
                    <p><strong>٣) حل المتباينة: $\text{–}\text{٣}\text{س} + \text{٤} \le \text{١٩}$ هو:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} \ge \text{–}\text{٥}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{س} \le \text{–}\text{٥}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} \ge \text{٥}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} \le \text{٥}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> بطرح ٤: $\text{–}\text{٣}\text{س} \le \text{١٥} \implies$ بالقسمة على (–٣) وعكس الرمز: $\text{س} \ge \text{–}\text{٥}$.
                    </div>
                </div>

                <div style="margin-bottom: 14px;">
                    <p><strong>٤) المتباينة التي تمثل "عدد مطروح منه ٨ أكبر من أو يساوي ١٥":</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\text{س} \text{–} \text{٨} \ge \text{١٥}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\text{٨} \text{–} \text{س} \ge \text{١٥}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\text{س} \text{–} \text{٨} > \text{١٥}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\text{س} + \text{٨} \le \text{١٥}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير:</strong> عدد مطروح منه ٨ هو $\text{س} \text{–} \text{٨}$، وأكبر من أو يساوي يعبر عنه بالرمز $\ge$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗): [٣ درجات]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> عند تمثيل المتباينة $\text{س} \ge \text{٣}$ بيانياً، نضع دائرة مغلقة عند النقطة ٣ ويتجه السهم لليمين.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ]</span>
                    </div>
                    <div>
                        <strong>٢)</strong> مجموعة حل المتباينة $\text{٢}\text{س} + \text{١} > \text{٢}\text{س} + \text{٧}$ هي مجموعة الأعداد الحقيقية $\mathbb{R}$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: بحذف ٢س يتبقى $١ > ٧$ وهي خاطئة فالحل هو $\emptyset$.</span>
                    </div>
                    <div>
                        <strong>٣)</strong> إذا كانت $\text{س} < \text{ص}$ فإن $\text{–}\text{٢}\text{س} < \text{–}\text{٢}\text{ص}$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: الضرب في عدد سالب يعكس رمز التباين فتصبح $\text{–}\text{٢}\text{س} > \text{–}\text{٢}\text{ص}$.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينات الآتية واكتب مجموعة الحل ومثلها على خط الأعداد: [٥ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{٥}\text{س} \text{–} \text{٣} \le \text{٢}\text{س} + \text{١٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بطرح ٢س من الطرفين: $\text{٣}\text{س} \text{–} \text{٣} \le \text{١٢}$<br>
                        • بإضافة ٣ للطرفين: $\text{٣}\text{س} \le \text{١٥}$<br>
                        • بالقسمة على ٣: $\text{س} \le \text{٥}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{س} \mid \text{س} \le \text{٥}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مغلقة $\bullet$ عند ٥ وسهم متجه لليسار.
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{–}\text{٣}(\text{ص} \text{–} \text{٢}) > \text{١٢}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • بالتوزيع: $\text{–}\text{٣}\text{ص} + \text{٦} > \text{١٢}$<br>
                        • بطرح ٦: $\text{–}\text{٣}\text{ص} > \text{٦}$<br>
                        • بالقسمة على (–٣) وقلب الرمز: $\text{ص} < \text{–}\text{٢}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{ص} \mid \text{ص} < \text{–}\text{٢}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مفتوحة $\circ$ عند –٢ وسهم متجه لليسار.
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة تطبيقية: [٣ درجات]</div>
                <p>اشترى فيصل أجهزة إلكترونية بمبلغ ٢٤٠ ريالاً، واشترى عدداً من بطاقات الشحن بسعر ٥٠ ريالاً للبطاقة الواحدة. إذا كان إجمالي ما دفعه لا يزيد على ٥٤٠ ريالاً، فما أكبر عدد من بطاقات الشحن يمكن لفيصل شراؤه؟</p>
                <div class="student-answer-space">المتباينة والحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • صياغة المتباينة: $\text{٥٠}\text{ب} + \text{٢٤٠} \le \text{٥٤٠}$<br>
                    • بطرح ٢٤٠ من الطرفين: $\text{٥٠}\text{ب} \le \text{٣٠٠}$<br>
                    • بالقسمة على ٥٠: $\text{ب} \le \text{٦}$<br>
                    • <strong>النتيجة:</strong> أكبر عدد من بطاقات الشحن يمكن لفيصل شراؤه هو <strong>٦ بطاقات</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_LAB = r"""
        <!-- ورقة عمل معمل الجبر -->
        <article class="worksheet-paper" id="ws-lab">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة استقصاء معملي:</strong> معمل الجبر (استكشاف العبارات المركبة ص ١٤٢)</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: الاستكشاف المنطقي للمفاهيم: [٣ درجات]</div>
                <p>صل بين العبارة في العمود (أ) وما يناسبها بيانياً ومنطقياً في العمود (ب):</p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>العمود (أ): العبارة المركبة</th>
                            <th>العمود (ب): التفسير والتمثيل البياني</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>١) $\text{س} \ge \text{٢}$ و $\text{س} \le \text{٦}$</td>
                            <td>
                                ( &nbsp;&nbsp; ) تمثل اتحاد منطقتين منفصلتين بشعاعين متعاكسين.<br>
                                ( &nbsp;&nbsp; ) تمثل منطقة التقاطع المحصورة بين النقطتين ٢ و ٦ بقطعة مستقيمة.
                                <div class="inline-explanation">
                                    💡 <strong>الحل:</strong> العبارة (١) تناسب الخيار الثاني (منطقة تقاطع محصورة لأنها تتضمن أداة الربط "و").
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>٢) $\text{س} < \text{–}\text{١}$ أو $\text{س} > \text{٣}$</td>
                            <td>
                                ( &nbsp;&nbsp; ) تمثل اتحاد الفترتين بشعاع يسار –١ وشعاع يمين ٣.<br>
                                ( &nbsp;&nbsp; ) مجموعة حلها خالية $\emptyset$.
                                <div class="inline-explanation">
                                    💡 <strong>الحل:</strong> العبارة (٢) تناسب الخيار الأول (اتحاد فترتين منفصلتين لأنها تتضمن أداة الربط "أو").
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: قراءة التمثيلات البيانية واستنتاج المتباينة المركبة: [٣ درجات]</div>
                <div style="margin-bottom: 16px;">
                    <p><strong>أ) خط أعداد عليه قطعة مستقيمة مظللة بين النقطة –٣ (دائرة مغلقة) والنقطة ٥ (دائرة مفتوحة). ما المتباينة المركبة الممثلة؟</strong></p>
                    <div class="student-answer-space">إجابة الطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        المتباينة هي متباينة وصل محصورة: $\text{–}\text{٣} \le \text{س} < \text{٥}$<br>
                        أو تكتب بالصيغة المنفصلة: $\text{س} \ge \text{–}\text{٣}$ و $\text{س} < \text{٥}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>ب) خط أعداد عليه شعاع يتجه لليسار من النقطة ٢ (دائرة مفتوحة)، وشعاع يتجه لليمين من النقطة ٧ (دائرة مغلقة). ما المتباينة المركبة الممثلة؟</strong></p>
                    <div class="student-answer-space">إجابة الطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        المتباينة هي متباينة فصل: $\text{س} < \text{٢}$ أو $\text{س} \ge \text{٧}$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: الاستقصاء والتحليل العملي: [٤ درجات]</div>
                <p>إذا كانت المتباينة المركبة هي: $\text{س} \ge \text{٤}$ و $\text{س} \le \text{١}$. ارسم خط الأعداد، ومثل كل متباينة بلون، ثم بين هل توجد منطقة تقاطع مشتركة؟ وما هي مجموعة الحل الناتجة؟</p>
                <div class="student-answer-space">الرسم والاستنتاج للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل والتحليل النموذجي:</strong><br>
                    • عند تمثيل $\text{س} \ge \text{٤}$ نحصل على شعاع ينطلق من ٤ متجهاً لليمين.<br>
                    • عند تمثيل $\text{س} \le \text{١}$ نحصل على شعاع ينطلق من ١ متجهاً لليسار.<br>
                    • <strong>الملاحظة البصرية:</strong> الشعاعان يتباعدان ولا يلتقيان في أي نقطة مشتركة.<br>
                    • <strong>الاستنتاج:</strong> بما أن أداة الربط هي (و) التي تشترط التقاطع، وحيث لا يوجد تقاطع، فإن مجموعة الحل هي <strong>المجموعة الخالية $\emptyset$</strong>.
                </div>
            </div>

            __FOOTER__
        </article>
"""

RAW_WS_4_4 = r"""
        <!-- ورقة عمل الدرس 4-4 -->
        <article class="worksheet-paper" id="ws-4-4">
            __HEADER__
            __TOOLBAR__

            <div class="ws-meta-bar">
                <span><strong>ورقة عمل تقويمية:</strong> الدرس (٤-٤) حل المتباينات المركبة</span>
                <span><strong>اسم الطالب:</strong> ..............................................................</span>
                <span><strong>الشعبة:</strong> .............</span>
                <span><strong>التاريخ:</strong> .... / .... / ١٤٤٧هـ</span>
                <span><strong>الدرجة المستحقة:</strong> [ &nbsp;&nbsp;&nbsp;&nbsp; / ١٠ ]</span>
            </div>

            <!-- السؤال الأول -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الأول: اختر الإجابة الصحيحة لكل فقرة: [٣ درجات]</div>
                
                <div style="margin-bottom: 16px;">
                    <p><strong>١) ما هي مجموعة حل المتباينة المركبة: $\text{–}\text{١} \le \text{س} + \text{٢} \le \text{٥}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{س} \mid \text{١} \le \text{س} \le \text{٧}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{س} \mid \text{–}\text{٣} \le \text{س} \le \text{٣}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\{\text{س} \mid \text{–}\text{٣} < \text{س} < \text{٣}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{س} \mid \text{س} \ge \text{–}\text{٣}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> بطرح ٢ من الأطراف الثلاثة بالتساوي: $\text{–}\text{١} \text{–} \text{٢} \le \text{س} \le \text{٥} \text{–} \text{٢} \implies \text{–}\text{٣} \le \text{س} \le \text{٣}$.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٢) ما هي مجموعة حل المتباينة المركبة: $\text{س} \text{–} \text{١} < \text{–}\text{٣}$ أو $\text{س} + \text{٢} \ge \text{٦}$؟</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{س} \mid \text{–}\text{٢} < \text{س} \le \text{٤}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\{\text{س} \mid \text{س} < \text{–}\text{٢} \text{ أو } \text{س} \ge \text{٤}\}$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) المجموعة الخالية $\emptyset$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) مجموعة الأعداد الحقيقية $\mathbb{R}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> الأولى: $\text{س} < \text{–}\text{٢}$، والثانية: $\text{س} \ge \text{٤}$. وحيث إن الرابط هو "أو" فيكون الحل هو اتحاد المجموعتين.
                    </div>
                </div>

                <div style="margin-bottom: 16px;">
                    <p><strong>٣) مجموعة حل المتباينة المركبة: $\text{س} > \text{٦}$ و $\text{س} < \text{٢}$ هي:</strong></p>
                    <div class="mcq-options-vertical">
                        <div class="mcq-option-line">
                            <span>(أ) $\{\text{س} \mid \text{٢} < \text{س} < \text{٦}\}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ب) $\mathbb{R}$</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(ج) $\emptyset$</span>
                            <span class="inline-answer-badge">✓ الإجابة الصحيحة</span>
                        </div>
                        <div class="mcq-option-line">
                            <span>(د) $\{\text{س} \mid \text{س} > \text{٦}\}$</span>
                        </div>
                    </div>
                    <div class="inline-explanation">
                        💡 <strong>التبرير الرياضي:</strong> يستحيل وجود عدد أكبر من ٦ وأصغر من ٢ في الوقت نفسه؛ فلا يوجد تقاطع إطلاقاً ومجموعة الحل هي $\emptyset$.
                    </div>
                </div>
            </div>

            <!-- السؤال الثاني -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثاني: ضع علامة (✓) أو (✗) مع تصحيح الخطأ: [درجتان]</div>
                <div style="margin: 10px 0; line-height: 2;">
                    <div>
                        <strong>١)</strong> متباينة الوصل التي تحتوي على أداة الربط "و" تعبر رياضياً عن تقاطع مجموعتي الحل.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✓ صحيحة ]</span>
                    </div>
                    <div>
                        <strong>٢)</strong> إذا كان تمثيل متباينة فصل (أو) على خط الأعداد هو شعاعان متعاكسان متداخلان يغطيان جميع الأعداد، فإن مجموعة الحل هي $\emptyset$.
                        ( &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; )
                        <span class="inline-tf-answer">[ الإجابة: ✗ خاطئة ] — التصويب: في متباينة الفصل نأخذ الاتحاد، فإذا غطى التمثيل خط الأعداد كاملاً فإن مجموعة الحل هي جميع الأعداد الحقيقية $\mathbb{R}$.</span>
                    </div>
                </div>
            </div>

            <!-- السؤال الثالث -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الثالث: حل المتباينات المركبة التالية بيانياً وجبرياً: [٣ درجات]</div>
                <div style="margin-bottom: 20px;">
                    <p><strong>أ) $\text{–}\text{٨} < \text{٣}\text{ص} + \text{١} \le \text{١٣}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • نطرح ١ من الأطراف الثلاثة: $\text{–}\text{٨} \text{–} \text{١} < \text{٣}\text{ص} \le \text{١٣} \text{–} \text{١} \implies \text{–}\text{٩} < \text{٣}\text{ص} \le \text{١٢}$<br>
                        • نقسم الأطراف الثلاثة على ٣: $\text{–}\text{٣} < \text{ص} \le \text{٤}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{ص} \mid \text{–}\text{٣} < \text{ص} \le \text{٤}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مفتوحة $\circ$ عند –٣، ودائرة مغلقة $\bullet$ عند ٤، وتظليل المسافة بينهما.
                    </div>
                </div>

                <div style="margin-bottom: 20px;">
                    <p><strong>ب) $\text{٢}\text{م} \text{–} \text{٥} \le \text{–}\text{٩}$ أو $\text{–}\text{٣}\text{م} + \text{٤} < \text{–}\text{٥}$</strong></p>
                    <div class="student-answer-space">خطوات الحل للطالب:</div>
                    <div class="problem-solution-inline">
                        <strong>الحل النموذجي المباشر:</strong><br>
                        • المتباينة الأولى: $\text{٢}\text{م} \le \text{–}\text{٤} \implies \text{م} \le \text{–}\text{٢}$<br>
                        • المتباينة الثانية: $\text{–}\text{٣}\text{م} < \text{–}\text{٩} \implies$ بالقسمة على (–٣) وقلب الرمز: $\text{م} > \text{٣}$<br>
                        • <strong>مجموعة الحل:</strong> $\{\text{م} \mid \text{م} \le \text{–}\text{٢} \text{ أو } \text{م} > \text{٣}\}$.<br>
                        • <strong>التمثيل البياني:</strong> دائرة مغلقة عند –٢ مع سهم لليسار، ودائرة مفتوحة عند ٣ مع سهم لليمين.
                    </div>
                </div>
            </div>

            <!-- السؤال الرابع -->
            <div class="ws-question-block">
                <div class="ws-q-title">السؤال الرابع: مسألة واقعية وتفكير ناقد: [درجتان]</div>
                <p>توصي وزارة الصحة بأن تتراوح نسبة الرطوبة المريحة والصحية داخل الفصول الدراسية المكيفة بمدارس جدة بين ٣٠٪ و ٦٠٪. اكتب متباينة مركبة تمثل نسبة الرطوبة الموصى بها (ر)، ثم مثلها على خط الأعداد، واذكر متباينة تمثل نسبة الرطوبة غير الصحية.</p>
                <div class="student-answer-space">الحل للطالب:</div>
                <div class="problem-solution-inline">
                    <strong>الحل النموذجي المباشر:</strong><br>
                    • <strong>متباينة الرطوبة الصحية (وصل):</strong> $\text{٣٠} \le \text{ر} \le \text{٦٠}$<br>
                    • <strong>التمثيل البياني:</strong> قطعة مستقيمة مغلقة الطرفين بين النقطة ٣٠ والنقطة ٦٠.<br>
                    • <strong>متباينة الرطوبة غير الصحية (فصل):</strong> $\text{ر} < \text{٣٠}$ أو $\text{ر} > \text{٦٠}$.
                </div>
            </div>

            __FOOTER__
        </article>
"""

def get_all_worksheets_html():
    w_4_2 = RAW_WS_4_2.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٤-٢)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-4-2")).replace("__FOOTER__", make_teacher_footer())
    w_4_3 = RAW_WS_4_3.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٤-٣)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-4-3")).replace("__FOOTER__", make_teacher_footer())
    w_mid = RAW_WS_MID_QUIZ.replace("__HEADER__", make_school_header("اختبار منتصف الفصل الرابع", "اختبار تشخيصي وتقويمي")).replace("__TOOLBAR__", make_ws_toolbar("ws-mid-quiz")).replace("__FOOTER__", make_teacher_footer())
    w_lab = RAW_WS_LAB.replace("__HEADER__", make_school_header("ورقة استقصاء معمل الجبر", "نشاط استقصائي وتقويم")).replace("__TOOLBAR__", make_ws_toolbar("ws-lab")).replace("__FOOTER__", make_teacher_footer())
    w_4_4 = RAW_WS_4_4.replace("__HEADER__", make_school_header("ورقة عمل: الدرس (٤-٤)", "ورقة عمل وتقويم بنائي")).replace("__TOOLBAR__", make_ws_toolbar("ws-4-4")).replace("__FOOTER__", make_teacher_footer())
    
    return (
        WORKSHEETS_SECTION_START +
        w_4_2 +
        w_4_3 +
        w_mid +
        w_lab +
        w_4_4 +
        "\n    </section><!-- /#worksheets-section -->\n"
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    html = get_all_worksheets_html()
    print(f"Worksheets HTML generated successfully, total length: {len(html)}")
