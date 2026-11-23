# -*- coding: utf-8 -*-
"""
upgrade_1m_mid_quiz.py: Enhances plan-mid-quiz to include full 7 criteria.
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

ENHANCED_MID_QUIZ = r"""
        <!-- خطة اختبار منتصف الفصل الثالث -->
        <article class="unit-card" id="plan-mid-quiz">
            <div class="unit-title-box">
                <h3><span>٣️⃣</span> خطة تنفيذ وتقويم: اختبار منتصف الفصل الثالث</h3>
                <span class="page-range-pill">كتاب الطالب: ص ١١٦</span>
            </div>

            <!-- 1. الأهداف والمعايير والمجال -->
            <div class="plan-step-box">
                <div class="plan-step-title">🎯 ١. الأهداف والمعايير والمجال</div>
                <p><strong>المجال:</strong> الجبر والدوال — <strong>المعيار:</strong> تقويم تشخيصي وتكويني شامل لمفاهيم المتغيرات والعبارات ومعادلات الجمع والطرح والضرب واستراتيجية الحل عكسياً (الدروس ٣-١ إلى ٣-٤) وفق معايير وزارة التعليم ٢٠٢٦م.</p>
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
                            <td>أن يحل الطالب معادلات خطية من خطوة واحدة (جمع، طرح، ضرب) بدقة تامة بنسبة ٪١٠٠.</td>
                            <td>تطبيق</td>
                            <td>ورقة اختبار منتصف الفصل المصنفة</td>
                        </tr>
                        <tr>
                            <td>٢</td>
                            <td>أن يترجم الطالب العبارات اللفظية إلى معادلات جبرية والعكس ويحل المسائل باستراتيجية الحل عكسياً بدقة.</td>
                            <td>تحليل وترجمة</td>
                            <td>فقرات المسائل الموضوعية واللفظية</td>
                        </tr>
                        <tr>
                            <td>٣</td>
                            <td>أن يكتشف الطالب فجواته المفاهيمية وينفذ خطة المعالجة الفورية المخصصة في ضوء التغذية الراجعة.</td>
                            <td>تقويم ذاتي وعلاج</td>
                            <td>مصفوفة الفاقد التعليمي والتصويب الزميلي</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 2. الانخراط والتركيز -->
            <div class="plan-step-box">
                <div class="plan-step-title">⚡ ٢. مرحلة الانخراط والتركيز (الربط المعرفي والتهيئة)</div>
                <p><strong>الحقبنة التشخيصية والتنشيطية:</strong></p>
                <ul style="margin: 8px 24px;">
                    <li>«ما الفرق بين العبارة الجبرية والمعادلة؟» (المعادلة تحتوي على إشارة مساواة = وتربط بين طرفين متعادلين).</li>
                    <li>«ما هي أداة التخلص من الجمع؟ (الطرح). وما أداة التخلص من الطرح؟ (الجمع). وما أداة التخلص من الضرب؟ (القسمة).»</li>
                    <li>«في استراتيجية الحل عكسياً، من أي نقطة نبدأ؟» (من النتيجة النهائية ونرجع إلى البداية).</li>
                </ul>

                <p style="margin-top: 14px;"><strong>التمهيد التفاعلي المبتكر:</strong></p>
                <div class="callout-box callout-info">
                    💡 <em>تحدي «طبيب المعادلات - رصد الفيروسات الحسابية»:</em> يُعرض على الشاشة ٣ حلول لمعادلات تحتوي على أخطاء شائعة (مثل نسيان تغيير الإشارة عند الطرح، أو قسمة طرف دون الآخر). يرفع الطلاب إشارات "الخطر" لتشخيص الفيروس الحسابي وتصحيحه قبل بدء جلسة الاختبار الرسمية.
                </div>

                <p style="margin-top: 14px;"><strong>جدول التعلم الذاتي (KWL):</strong></p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th style="width: 35%;">ماذا نتقن مسبقاً؟ (K)</th>
                            <th style="width: 35%;">ما المهارات التي نريد تأكيدها؟ (W)</th>
                            <th style="width: 30%;">ماذا تعلمنا من التقويم؟ (L)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                • كتابة العبارات الجبرية.<br>
                                • حل معادلات الجمع والطرح.<br>
                                • حل معادلات الضرب واستراتيجية الحل عكسياً.
                            </td>
                            <td>
                                • الدقة الحسابية مع الأعداد الصحيحة السالبة.<br>
                                • سرعة نمذجة المسائل الواقعية.<br>
                                • معالجة أي تعثر مفاهيمي قبل الدروس القادمة.
                            </td>
                            <td><em>يُستكمل بعد تصحيح الاختبار</em></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 3. بيئة التعلم -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏫 ٣. بيئة التعلم وقواعد جلسة الاختبار</div>
                <div class="rule-card-grid">
                    <div class="rule-card">
                        <h5>النزاهة والاعتماد الذاتي 🛡️</h5>
                        <p>«الاختبار وسيلة لتشخيص مستواك الحقيقي ونقاط قوتك لتعزيزها وفرص تحسينك لمعالجتها فوراً.»</p>
                    </div>
                    <div class="rule-card">
                        <h5>تسلسل خطوات التبرير ✍️</h5>
                        <p>«كتابة المعادلة، ثم تطبيق العملية العكسية للطرفين بالتساوي، ثم كتابة الناتج النهائي والتحقق.»</p>
                    </div>
                    <div class="rule-card">
                        <h5>الهدوء والتركيز الزمني ⏱️</h5>
                        <p>«توزيع زمن الحصة بين القراءة المتأنية والحل المتزن والمراجعة الدقيقة لكافة الإجابات.»</p>
                    </div>
                </div>
            </div>

            <!-- 4. تنفيذ الدرس ومربع فرير وخريطة المفاهيم -->
            <div class="plan-step-box">
                <div class="plan-step-title">🚀 ٤. تنفيذ خطة الاختبار والمفاهيم المحورية</div>
                
                <p><strong>خريطة مهارات منتصف الفصل الثالث:</strong></p>
                <div class="tree-mindmap">
                    <div class="tree-root">🌳 محاور اختبار منتصف الفصل الثالث (ص ١١٦)</div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">المحور الأول: المتغيرات والعبارات الجبرية</div>
                        <div class="tree-leaf">• التعبير عن العبارات اللفظية بمتغيرات وعمليات جبرية.</div>
                    </div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">المحور الثاني: معادلات الجمع والطرح</div>
                        <div class="tree-leaf">• خاصية الجمع والطرح للمساواة (إضافة النظير الجمعي للطرفين).</div>
                    </div>
                    <div class="tree-branch">
                        <div class="tree-branch-title">المحور الثالث: معادلات الضرب واستراتيجية الحل عكسياً</div>
                        <div class="tree-leaf">• خاصية القسمة للمساواة، وصيغ المسافة ($ف = ع \times ن$)، وتفكيك المسائل بالرجوع للخلف.</div>
                    </div>
                </div>

                <p style="margin-top: 14px;"><strong>مربع فرير (Frayer Model): المفهوم الأساسي «معادلة الخطوة الواحدة»:</strong></p>
                <div class="frayer-box">
                    <div class="frayer-center-title">مفهوم: معادلة الخطوة الواحدة (One-Step Equation)</div>
                    <div class="frayer-quadrant">
                        <h4>التعريف الرياضي الدقيق</h4>
                        <p>جملة رياضية تتضمن علامة التساوي (=) وعملية حسابية واحدة فقط تفصل المتغير عن بقية الحدود، ويتم حلها بتطبيق عملية عكسية واحدة مقابلة.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>الخصائص والمميزات</h4>
                        <p>• حلها مباشر وسريع من سطر واحد.<br>• تعتمد على خاصية المحايد والنظير (الجمعي أو الضربي).<br>• أساس انطلاق المعادلات المعقدة ومتعددة الخطوات.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>أمثلة دالة</h4>
                        <p>• $\text{س} + \text{٥} = \text{١٢} \implies \text{س} = \text{٧}$.<br>• $\text{–}\text{٤}\text{ص} = \text{٢٤} \implies \text{ص} = \text{–}\text{٦}$.</p>
                    </div>
                    <div class="frayer-quadrant">
                        <h4>لا أمثلة</h4>
                        <p>• $\text{٢}\text{س} + \text{٣} = \text{١١}$ (معادلة ذات خطوتين).<br>• $\text{س} + \text{٥} > \text{١٢}$ (متباينة).</p>
                    </div>
                </div>

                <p style="margin-top: 14px;"><strong>مصفوفة المعالجة الفورية للفاقد التعليمي:</strong></p>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>المهارة المستهدفة</th>
                            <th>الخطأ الشائع المتوقع</th>
                            <th>الإجراء العلاجي الفوري المقترح</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>معادلات الضرب السالبة</td>
                            <td>نسيان إشارة السالب عند القسمة في $\text{–}\text{٣}\text{س} = \text{١٥}$</td>
                            <td>تدريب ببطاقات الإشارات الملونة وإعادة التحقق بالضرب العكسي.</td>
                        </tr>
                        <tr>
                            <td>الترجمة من لفظي لجبري</td>
                            <td>عكس ترتيب الطرح مثل "أقل من س بـ ٨"</td>
                            <td>التدريب على جدول الكلمات المفتاحية لمطابقة العبارة بالصيغة الجبرية.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 5. التكامل -->
            <div class="plan-step-box">
                <div class="plan-step-title">🌐 ٥. التكامل ومنهجية STEM</div>
                <div class="stem-grid">
                    <div class="stem-pillar s">
                        <h4>🔬 العلوم</h4>
                        <p>حسابات التكافؤ والكتلة في التفاعلات الكيميائية كمعادلات اتزان متطابقة الطرفين.</p>
                    </div>
                    <div class="stem-pillar t">
                        <h4>💻 التقنية</h4>
                        <p>استخدام الاختبارات الإلكترونية التفاعلية لتحليل نتائج الطلاب واستخراج تقارير الفاقد الفورية.</p>
                    </div>
                    <div class="stem-pillar e">
                        <h4>🏗️ الهندسة</h4>
                        <p>معادلات الاتزان الإنشائي للأحمال والقوى المتوازنة على جانبي الجسور والروافع.</p>
                    </div>
                    <div class="stem-pillar m">
                        <h4>📐 الرياضيات</h4>
                        <p>خصائص علاقة التكافؤ والمساواة (الانعكاس، التماثل، التعدي) في نظام الأعداد الحقيقية.</p>
                    </div>
                </div>
            </div>

            <!-- 6. التقويم -->
            <div class="plan-step-box">
                <div class="plan-step-title">📊 ٦. نماذج فقرات الاختبار وحلولها النموذجية</div>
                <div style="margin: 10px 0;">
                    <p><strong>فقرة ١:</strong> حل المعادلة: $\text{س} + \text{٧} = \text{–}\text{٣}$.</p>
                    <p style="color:#166534; font-weight:700;">الحل: بطرح ٧ من الطرفين: $\text{س} = \text{–}\text{٣} \text{–} \text{٧} = \text{–}\text{١٠}$.</p>
                </div>
                <div style="margin: 10px 0;">
                    <p><strong>فقرة ٢:</strong> حل المعادلة: $\text{–}\text{٥}\text{ص} = \text{٣٥}$.</p>
                    <p style="color:#166534; font-weight:700;">الحل: بالقسمة على (–٥): $\text{ص} = \text{–}\text{٧}$.</p>
                </div>
                <div style="margin: 10px 0;">
                    <p><strong>فقرة الواجب المنزلي (MCQ):</strong> اكتب المعادلة: "أكبر من عدد بـ ٤ يساوي ١٥":</p>
                    <div style="margin: 6px 16px;">
                        <div>(أ) $\text{س} + \text{٤} = \text{١٥}$</div>
                        <div>(ب) $\text{س} \text{–} \text{٤} = \text{١٥}$</div>
                        <div>(ج) $\text{٤}\text{س} = \text{١٥}$</div>
                        <div>(د) $\frac{\text{س}}{\text{٤}} = \text{١٥}$</div>
                    </div>
                    <p style="color:#166534; font-weight:800; margin-top:6px;">الإجابة الصحيحة: (أ)؛ لأن كلمة "أكبر من بـ ٤" تعني إضافة ٤ إلى المتغير س.</p>
                </div>
            </div>

            <!-- 7. الغلق -->
            <div class="plan-step-box">
                <div class="plan-step-title">🏁 ٧. الغلق ونقل أثر التعلم</div>
                <p>«بهذا الاختبار نكون قد أتقنا معادلات الخطوة الواحدة، وأصبحنا مهيئين لدمج العمليات معاً في درس المعادلات ذات الخطوتين!»</p>
            </div>
        </article>
"""

with open('section_1m_plans.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
old_plan = re.search(r'<!-- خطة اختبار منتصف الفصل الثالث -->[\s\S]*?</article>', content).group()
content = content.replace(old_plan, ENHANCED_MID_QUIZ.strip())

with open('section_1m_plans.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Enhanced plan-mid-quiz applied successfully!")
