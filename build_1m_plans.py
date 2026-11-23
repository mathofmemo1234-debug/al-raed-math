# -*- coding: utf-8 -*-
"""
build_1m_plans.py: Generates all 5 STEM lesson plans for Grade 7 (1m) pages 109 to 127.
Adheres strictly to Prompt 1 criteria with all 7 components and Eastern Arabic numerals.
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLANS_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الأول: خطط التدريس والتحضير وفق معايير STEM السبعة (متتالية)         -->
    <!-- ========================================================================= -->
    <section id="plans-section" class="master-section">
        <div class="section-header-banner plans">
            <h2>📑 القسم الأول: خطط التدريس والتحضير وفق معايير STEM السبعة (متتالية)</h2>
            <span class="section-badge">معتمدة وفق معايير وزارة التعليم ٢٠٢٦م</span>
        </div>
"""

PLAN_3_3 = r"""
        <!-- خطة الدرس (3-3) -->
        <article class="unit-card" id="plan-3-3">
            <div class="unit-title-box">
                <h3><span>١️⃣</span> خطة الدرس (٣-٣): معادلات الضرب</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١٠٩ – ١١٣</span>
            </div>

            <!-- 1. الأهداف والمعايير والمجال -->
            <div class="plan-step-box">
                <div class="plan-step-title">🎯 ١. الأهداف والمعايير والمجال</div>
                <p><strong>المجال:</strong> الجبر والدوال — <strong>المعيار:</strong> حل معادلات الضرب الخطية باستعمال خاصية القسمة للمساواة وتوظيف الصيغ الرياضية وفق معايير وزارة التعليم السعودية ٢٠٢٦م.</p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الرقم</th>
                            <th>الهدف التعليمي (وفق معايير SMART)</th>
                            <th>مستوى بلوم</th>
                            <th>أداة التحقق</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>١</td>
                            <td>أن يحل الطالب معادلات الضرب الخطية بتطبيق خاصية القسمة للمساواة بدقة ٪١٠٠.</td>
                            <td>تطبيق</td>
                            <td>حل فردي على السبورات البيضاء المصغرة</td>
                        </tr>
                        <tr>
                            <td>٢</td>
                            <td>أن يستعمل الطالب الصيغة الرياضية لمسائل الحركة ($ف = ع \times ن$) لحساب متغير مجهول في ٤ دقائق.</td>
                            <td>تحليل وتطبيق</td>
                            <td>نشاط فكر-زاوج-شارك ومهمة ثنائية</td>
                        </tr>
                        <tr>
                            <td>٣</td>
                            <td>أن يصوغ الطالب معادلة ضرب تمثل موقفاً واقعياً من الحياة اليومية (كتكلفة الشراء أو الأرقام القياسية) ويحلها بنجاح.</td>
                            <td>تركيب وحل مشكلات</td>
                            <td>التقويم الختامي وبطاقة الخروج</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 2. مرحلة الانخراط والتركيز -->
            <div class="plan-step-box">
                <div class="plan-step-title">⚡ ٢. مرحلة الانخراط والتركيز (الربط المعرفي)</div>
                <p><strong>الحقبنة المعرفية (تنشيط الخبرات السابقة):</strong></p>
                <ul style="margin: 8px 24px;">
                    <li>«كيف كنا نحل معادلة الجمع: $\text{س} + \text{٥} = \text{١٢}$؟ ما هي العملية العكسية للجمع؟» (الطرح).</li>
                    <li>«إذا كان الضرب جمعاً متكرراً، فما هي العملية الحسابية العكسية المباشرة لعملية الضرب؟» (القسمة).</li>
                    <li>«إذا تضاعف وزن شيء ٤ مرات وأصبح وزنه ٢٠ كجم، كيف نكتشف وزنه الأصلي بعملية واحدة؟» ($٢٠ \div ٤ = ٥$).</li>
                </ul>

                <p style="margin-top: 14px;"><strong>التمهيد التفاعلي المبتكر:</strong></p>
                <div class="callout-box callout-info">
                    💡 <em>نشاط «أكياس الكرات الغامضة على ميزان العدالة»:</em> يعرض المعلم ميزاناً ذو كفتين؛ في الكفة اليمنى ٣ أكياس متطابقة ومغلقة بداخل كل منها عدد مجهول من الكرات ($\text{س}$)، وفي الكفة اليسرى ١٥ كرة متماثلة والميزان في حالة اتزان تام ($٣\text{س} = ١٥$). يسأل المعلم الصف: «كيف نعرف ما بداخل الكيس الواحد دون فتح كل الأكياس؟» يستنتج الطلاب فوراً توزيع الكرات بالتساوي على ٣ مجموعات، أي قسمة الطرفين على ٣ فيتبقى في الكيس الواحد ٥ كرات!
                </div>

                <p style="margin-top: 12px;"><strong>التقويم التشخيصي السريع:</strong></p>
                <ol style="margin: 8px 24px;">
                    <li>أوجد ناتج: $٣٦ \div ٤$ و ناتج: $–٤٢ \div ٦$.</li>
                    <li>اكتب عبارة جبرية تمثل: "ناتج ضرب ٨ في عدد ما".</li>
                </ol>

                <p style="margin-top: 14px;"><strong>جدول التعلم الذاتي (KWL):</strong></p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 35%;">ماذا نعرف مسبقاً؟ (K)</th>
                            <th style="width: 35%;">ماذا نريد أن نعرف؟ (W)</th>
                            <th style="width: 30%;">ماذا تعلمنا اليوم؟ (L)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                • حل معادلات الجمع والطرح باستعمال العمليات العكسية.<br>
                                • قواعد ضرب وقسمة الأعداد الصحيحة والإشارات.<br>
                                • مفهوم المعادلة وحالة الاتزان.
                            </td>
                            <td>
                                • كيفية حل معادلة الضرب بخاصية القسمة للمساواة.<br>
                                • التعامل مع المعاملات السالبة في معادلات الضرب.<br>
                                • توظيف الصيغ الرياضية في مسائل السرعة والمسافة والزمن.
                            </td>
                            <td><em>يُستكمل في مرحلة الغلق</em></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏫 ٣. بيئة التعلم وقواعد السلوك الصفي</div>
                <div class="rule-card-grid">
                    <div class="rule-card">
                        <h5>قاعدة توازن كفتي الميزان ⚖️</h5>
                        <p>«أي عملية قسمة تُجرى على الطرف الأيمن، يجب إجراؤها فوراً على الطرف الأيسر بنفس العدد دون أدنى تأخير لضمان بقاء المعادلة صحيحة.»</p>
                    </div>
                    <div class="rule-card">
                        <h5>قاعدة ضبط الإشارات 🔍</h5>
                        <p>«الانتباه الدقيق لقواعد إشارات قسمة الأعداد الصحيحة: موجب على سالب يعطي سالباً، وسالب على سالب يعطي موجباً.»</p>
                    </div>
                    <div class="rule-card">
                        <h5>قاعدة التحقق التبادلي 🤝</h5>
                        <p>«قبل تسليم الحل النهائي، عوض بقيمتك الناتجة في المعادلة الأصلية وتأكد بنفسك من مطابقة الناتج لكلا الطرفين.»</p>
                    </div>
                </div>
            </div>

            <!-- 4. تنفيذ الدرس -->
            <div class="plan-step-box">
                <div class="plan-step-title">🚀 ٤. تنفيذ الدرس وتطوير المحتوى بالاستراتيجيات النشطة</div>
                
                <p><strong>العصف الذهني (Brainstorming):</strong></p>
                <p>«تقطع طائرة ركاب تابعة للخطوط الجوية السعودية مسافة ١٨٠٠ كم في ساعتين. كيف نصوغ معادلة ضرب لحساب متوسط سرعة الطائرة بالساعة؟ وماذا تعني الصيغة الرياضية في لغة الرياضيات؟»</p>

                <p style="margin-top: 14px;"><strong>فكر-زاوج-شارك (Think-Pair-Share):</strong></p>
                <div class="callout-box callout-tip">
                    <strong>مهمة التحدي الثنائي:</strong> حل المعادلة الآتية وتحقق من صحة حلك:
                    $$\text{–}\text{٨}\text{ص} = \text{٥٦}$$
                    • <em>فكر:</em> ما هو معامل المتغير ص؟ وبماذا سنقسم الطرفين للتخلص منه؟<br>
                    • <em>زاوج:</em> قارن إجابتك وإشارتك مع زميلك: هل الناتج موجب أم سالب؟<br>
                    • <em>شارك:</em> يعرض ثنائي مختار خطوات التحقق بالتعويض: $\text{–}\text{٨} \times (\text{–}\text{٧}) = \text{٥٦}$.
                </div>

                <p style="margin-top: 14px;"><strong>الخريطة الذهنية الشجرية (Tree Mind Map):</strong></p>
                <div class="tree-mindmap">
                    <div class="tree-root">🌳 منظومة معادلات الضرب</div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">١. المفهوم الأساسي والقاعدة</div>
                        <div class="tree-leaf">• معادلة الضرب صورة قياسية: $أ \times \text{س} = ب$.</div>
                        <div class="tree-leaf">• التخلص من المعامل (أ) بقسمة كلا الطرفين عليه: $\text{س} = \frac{ب}{أ}$.</div>
                    </div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">٢. حالات الإشارات عند القسمة</div>
                        <div class="tree-leaf">• قسمة إشارتين متشابهتين $\implies$ الناتج موجب (+) (مثال: $\text{–}\text{٤}\text{س} = \text{–}\text{٢٠} \implies \text{س} = \text{٥}$).</div>
                        <div class="tree-leaf">• قسمة إشارتين مختلفتين $\implies$ الناتج سالب (–) (مثال: $\text{٦}\text{م} = \text{–}\text{٢٤} \implies \text{م} = \text{–}\text{٤}$).</div>
                    </div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">٣. الصيغ الرياضية والتطبيقات</div>
                        <div class="tree-leaf">• صيغة الحركة: المسافة = السرعة × الزمن ($ف = ع \times ن$).</div>
                    </div>
                </div>

                <p style="margin-top: 14px;"><strong>مربع فرير (Frayer Model): المفهوم الأساسي «معادلة الضرب»:</strong></p>
                <div class="frayer-box">
                    <div class="frayer-center-title">مفهوم: معادلة الضرب (Multiplication Equation)</div>
                    <div class="frayer-quadrant">
                        <h4>التعريف الرياضي الدقيق</h4>
                        <p>معادلة رياضية تتضمن عملية ضرب بين معامل معلوم ومتغير مجهول تفصلها علامة التساوي عن طرف آخر، ويتم حلها بتطبيق خاصية القسمة للمساواة.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>الخصائص والمميزات</h4>
                        <p>• المعامل ملاصق للمتغير مباشرة دون إشارة جمع أو طرح.<br>• تقسم الطرفين على نفس العدد بالضبط بما فيه إشارته.<br>• حلها فريد ومحدد يمكن التحقق منه بالضرب العكسي.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>أمثلة دالة</h4>
                        <p>• $\text{٤}\text{س} = \text{٢٠} \implies \text{س} = \text{٥}$.<br>• $\text{–}\text{٣}\text{ن} = \text{–}\text{٢١} \implies \text{ن} = \text{٧}$.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>لا أمثلة (مفاهيم مغايرة)</h4>
                        <p>• $\text{س} + \text{٤} = \text{٢٠}$ (معادلة جمع).<br>• $\frac{\text{س}}{\text{٤}} = \text{٢٠}$ (معادلة قسمة تتطلب الضرب للحل).<br>• $\text{٤}\text{س} > \text{٢٠}$ (متباينة وليست معادلة).</p>
                    </div>
                </div>

                <p style="margin-top: 14px;"><strong>الأمثلة التطبيقية المحلولة من الكتاب:</strong></p>
                <ul style="margin: 8px 24px;">
                    <li><strong>مثال ١ (حل معادلة ضرب بسيطة ص ١٠٩):</strong> حل: $\text{٤}\text{س} = \text{٢٠}$ $\implies$ بقسمة الطرفين على ٤: $\text{س} = \text{٥}$. التحقق: $\text{٤}(\text{٥}) = \text{٢٠}$ (صحيحة).</li>
                    <li><strong>مثال ٢ (معادلة ضرب تتضمن عدداً سالباً ص ١١٠):</strong> حل: $\text{–}\text{٨}\text{ص} = \text{٣٢}$ $\implies$ بقسمة الطرفين على (–٨): $\text{ص} = \text{–}\text{٤}$. التحقق: $\text{–}\text{٨}(\text{–}\text{٤}) = \text{٣٢}$ (صحيحة).</li>
                    <li><strong>مثال ٤ (استعمال الصيغ الرياضية ص ١١٠):</strong> تسير سيارة بسرعة ٩٠ كم/ساعة، فإذا قطعت مسافة ٤٥٠ كم، فما هو الزمن المستغرق؟ نطبق الصيغة $ف = ع \times ن \implies \text{٤٥٠} = \text{٩٠} \times ن \implies ن = \frac{\text{٤٥٠}}{\text{٩٠}} = \text{٥}$ ساعات.</li>
                </ul>
            </div>

            <!-- 5. التكامل -->
            <div class="plan-step-box">
                <div class="plan-step-title">🌐 ٥. التكامل (منهجية STEM والربط الحياتي)</div>
                <p><strong>الربط الحياتي الواقعي:</strong> حساب تكلفة مشتريات الجملة في المتاجر؛ إذا دفع تاجر ٦٠٠ ريال لشراء عدد من القمصان المدرسية بسعر ٥٠ ريالاً للقميص الواحد، فالمعادلة هي $\text{٥٠}\text{ق} = \text{٦٠٠} \implies \text{ق} = \text{١٢}$ قميصاً.</p>
                
                <p style="margin-top: 12px;"><strong>مصفوفة أركان منهجية STEM:</strong></p>
                <div class="stem-grid">
                    <div class="stem-pillar s">
                        <h4>🔬 العلوم (Science)</h4>
                        <p>الفيزياء وحساب السرعة والتدفق: قانون الكثافة (الكتلة = الكثافة × الحجم) ومعدل تدفق المياه في محطات التحلية بجدة.</p>
                    </div>
                    <div class="stem-pillar t">
                        <h4>💻 التقنية (Technology)</h4>
                        <p>الخوارزميات والحوسبة: برمجة تطبيقات تتبع الشحنات لحساب وقت الوصول المتوقع عبر قسمة المسافة على السرعة اللحظية.</p>
                    </div>
                    <div class="stem-pillar e">
                        <h4>🏗️ الهندسة (Engineering)</h4>
                        <p>هندسة النقل والمواصلات: تخطيط مسارات قطار الحرمين السريع وجدولة زمن الرحلات بدقة بالاعتماد على صيغ المسافة والسرعة.</p>
                    </div>
                    <div class="stem-pillar m">
                        <h4>📐 الرياضيات (Mathematics)</h4>
                        <p>خاصية القسمة للمساواة، النظائر الضربية، والنسب والتناسب في الحقول العددية للأعداد الصحيحة والنسبية.</p>
                    </div>
                </div>
            </div>

            <!-- 6. منظومة التقويم -->
            <div class="plan-step-box">
                <div class="plan-step-title">📊 ٦. منظومة التقويم (مقالي وموضوعي مع الحل النموذجي)</div>
                
                <p><strong>أولاً: التقويم البنائي (سؤال لكل هدف من الأهداف الثلاثة):</strong></p>
                <div style="margin: 10px 0;">
                    <p><strong>سؤال الهدف ١:</strong> حل المعادلة: $\text{–}\text{٦}\text{م} = \text{٤٢}$ وتحقق من صحة حلك.</p>
                    <p style="color:#166534; font-weight:700;">الحل النموذجي: بقسمة الطرفين على (–٦): $\text{م} = \frac{\text{٤٢}}{\text{–}\text{٦}} = \text{–}\text{٧}$. التحقق: $\text{–}\text{٦}(\text{–}\text{٧}) = \text{٤٢}$ (صحيحة).</p>
                </div>
                <div style="margin: 10px 0;">
                    <p><strong>سؤال الهدف ٢:</strong> استعمل الصيغة $ف = ع \times ن$ لإيجاد سرعة عداء قطع مسافة ٤٠٠ متر في زمن قدره ٥٠ ثانية.</p>
                    <p style="color:#166534; font-weight:700;">الحل النموذجي: $\text{٤٠٠} = ع \times \text{٥٠} \implies ع = \frac{\text{٤٠٠}}{\text{٥٠}} = \text{٨}$ أمتار لكل ثانية.</p>
                </div>
                <div style="margin: 10px 0;">
                    <p><strong>سؤال الهدف ٣:</strong> اشترى عمر ٥ كتب متطابقة بمبلغ ١٧٥ ريالاً. اكتب معادلة ضرب تمثل الموقف وأوجد ثمن الكتاب الواحد.</p>
                    <p style="color:#166534; font-weight:700;">الحل النموذجي: المعادلة: $\text{٥}\text{ك} = \text{١٧٥} \implies \text{ك} = \frac{\text{١٧٥}}{\text{٥}} = \text{٣٥}$ ريالاً للكتاب الواحد.</p>
                </div>

                <p style="margin-top: 14px;"><strong>ثانياً: التقويم الختامي الشامل:</strong></p>
                <div style="margin: 10px 0;">
                    <p><strong>سؤال ختامي:</strong> حل المعادلة: $\text{–}\text{١٢}\text{س} = \text{–}\text{١٠٨}$ ثم اشرح الخاصية المطبقة في الحل وخطوة التحقق.</p>
                    <p style="color:#166534; font-weight:700;">الحل النموذجي: بقسمة الطرفين على (–١٢) بتطبيق خاصية القسمة للمساواة: $\text{س} = \frac{\text{–}\text{١٠٨}}{\text{–}\text{١٢}} = \text{٩}$. التحقق: $\text{–}\text{١٢} \times \text{٩} = \text{–}\text{١٠٨}$.</p>
                </div>

                <p style="margin-top: 14px;"><strong>ثالثاً: الواجب المنزلي (سؤال من ٤ خيارات رأسية MCQ مع الحل):</strong></p>
                <div style="background:#f8fafc; padding:14px; border:1px solid #cbd5e1; border-radius:8px;">
                    <p><strong>سؤال:</strong> ما هو حل المعادلة: $\text{٧}\text{ص} = \text{–}\text{٤٩}$؟</p>
                    <div style="margin: 8px 16px;">
                        <div>(أ) $\text{ص} = \text{٧}$</div>
                        <div>(ب) $\text{ص} = \text{–}\text{٧}$</div>
                        <div>(ج) $\text{ص} = \text{–}\text{٤٢}$</div>
                        <div>(د) $\text{ص} = \text{–}\text{٥٦}$</div>
                    </div>
                    <p style="color:#166534; font-weight:800; margin-top:8px;">
                        الإجابة الصحيحة: (ب)<br>
                        التفسير الرياضي: بقسمة كلا الطرفين على معامل المتغير (٧): $\text{ص} = \frac{\text{–}\text{٤٩}}{\text{٧}} = \text{–}\text{٧}$ (قسمة عدد سالب على عدد موجب تعطي ناتجاً سالباً).
                    </p>
                </div>
            </div>

            <!-- 7. الغلق والتلخيص -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏁 ٧. الغلق والتلخيص والتحدي الإثرائي</div>
                <p><strong>استكمال عمود (ماذا تعلمنا؟ L في جدول KWL):</strong></p>
                <ul style="margin: 8px 24px;">
                    <li>تعلمنا أن العملية العكسية للضرب هي القسمة، وخاصية القسمة للمساواة تحافظ على اتزان المعادلة.</li>
                    <li>تعلمنا ضبط الإشارات بدقة عند قسمة الأعداد الصحيحة الموجبة والسالبة.</li>
                    <li>تعلمنا توظيف صيغة المسافة والسرعة والزمن في حل المسائل اليومية.</li>
                </ul>

                <p style="margin-top: 14px;"><strong>السؤال الإثرائي وتحدي الدرس القادم:</strong></p>
                <div class="callout-box callout-warning">
                    🔥 <em>تحدي التفكير المنطقي:</em> «مع طارق مبلغ من المال أنفق نصفه في المتجر، ثم تصدق بـ ٥ ريالات، فتبقى معه ١٥ ريالاً. كيف يمكننا العودة إلى المبلغ الأصلي بالبدء من النهاية وعكس العمليات واحدة تلو الأخرى؟ هذا ما سنكتشفه غداً في استراتيجية الحل عكسياً!»
                </div>
            </div>
        </article>
"""

print("Plan 3-3 template ready.")
