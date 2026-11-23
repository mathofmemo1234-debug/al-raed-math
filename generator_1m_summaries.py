# -*- coding: utf-8 -*-
"""
generator_1m_summaries.py: Student Summaries for Grade 7 (1m) pages 109 to 127:
- Lesson 3-3: معادلات الضرب
- Lesson 3-4: استراتيجية حل المسألة (الحل عكسياً)
- Mid-Chapter 3 Quiz Review: مراجعة منتصف الفصل الثالث
- Lesson 3-5: المعادلات ذات الخطوتين
- Lesson 3-6: القياس: المحيط والمساحة
All include official school header and teacher signature at bottom left.
"""

from generator_1m_header_styles import make_school_header, make_teacher_footer

SUMMARIES_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية)                              -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">مفاهيم وقواعد مركزة وشاملة للمذاكرة الذكية</span>
        </div>
"""

RAW_SUMMARY_3_3 = r"""
        <!-- ملخص الدرس 3-3 -->
        <article class="summary-card" id="summary-3-3">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٣-٣): معادلات الضرب (ص ١٠٩ – ١١٣)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 القاعدة الذهبية لحل معادلات الضرب:</h4>
                <p>العملية العكسية للضرب هي <strong>القسمة</strong>. لحل معادلة ضرب، نطبق <strong>خاصية القسمة للمساواة</strong>: اقسم كلا طرفي المعادلة على معامل المتغير (العدد المضروب في الرمز).</p>
                <div style="background:#f0fdf4; border-right:4px solid #16a34a; padding:12px 18px; margin:10px 0; border-radius:0 8px 8px 0;">
                    <strong>القاعدة بالرموز:</strong> إذا كان $أ \times \text{س} = ب$ (حيث $أ \ne ٠$)، فإن: $\text{س} = \frac{ب}{أ}$.
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 حالات إشارات ناتج القسمة:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>نوع المعادلة</th>
                            <th>مثال توضيحي</th>
                            <th>خطوة الحل</th>
                            <th>قاعدة الإشارة والناتج</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>المعامل والناتج موجبان</td>
                            <td>$\text{٤}\text{س} = \text{٢٠}$</td>
                            <td>بقسمة الطرفين على ٤</td>
                            <td>موجب $\div$ موجب = <strong>موجب</strong> $\implies \text{س} = \text{٥}$</td>
                        </tr>
                        <tr>
                            <td>المعامل سالب والناتج موجب</td>
                            <td>$\text{–}\text{٨}\text{ص} = \text{٣٢}$</td>
                            <td>بقسمة الطرفين على (–٨)</td>
                            <td>موجب $\div$ سالب = <strong>سالب</strong> $\implies \text{ص} = \text{–}\text{٤}$</td>
                        </tr>
                        <tr>
                            <td>المعامل موجب والناتج سالب</td>
                            <td>$\text{٦}\text{م} = \text{–}\text{٤٢}$</td>
                            <td>بقسمة الطرفين على ٦</td>
                            <td>سالب $\div$ موجب = <strong>سالب</strong> $\implies \text{م} = \text{–}\text{٧}$</td>
                        </tr>
                        <tr>
                            <td>المعامل سالب والناتج سالب</td>
                            <td>$\text{–}\text{٥}\text{ك} = \text{–}\text{٤٥}$</td>
                            <td>بقسمة الطرفين على (–٥)</td>
                            <td>سالب $\div$ سالب = <strong>موجب</strong> $\implies \text{ك} = \text{٩}$</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 الصيغة الرياضية لمسائل الحركة والسرعة:</h4>
                <p>الصيغة الرياضية هي معادلة تبين العلاقة بين كميات محددة. ومن أشهرها صيغة المسافة:</p>
                <div style="background:#eff6ff; border:1px solid #bfdbfe; padding:12px 18px; border-radius:8px; margin:8px 0;">
                    $$\text{المسافة} = \text{السرعة} \times \text{الزمن} \quad \implies \quad ف = ع \times ن$$
                    • لإيجاد السرعة: $ع = \frac{ف}{ن}$ &nbsp;&nbsp;|&nbsp;&nbsp; • لإيجاد الزمن: $ن = \frac{ف}{ع}$
                </div>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>خطأ شائع يجب تجنبه:</strong> في المعادلة $\text{–}\text{٤}\text{س} = \text{١٦}$، بعض الطلاب يجمعون ٤ ظناً منهم أنها عملية طرح! تذكر أن العلاقة بين –٤ و س هي علاقة ضرب؛ لذا يجب القسمة على (–٤) كاملاً مع إشارته!
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_3_4 = r"""
        <!-- ملخص الدرس 3-4 -->
        <article class="summary-card" id="summary-3-4">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٣-٤): استراتيجية حل المسألة (الحل عكسياً) (ص ١١٤ – ١١٥)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 متى نستخدم استراتيجية «الحل عكسياً»؟</h4>
                <p>نستخدم هذه الاستراتيجية عندما تعطينا المسألة سلسلة متتابعة من العمليات أو التغيرات (صرف، إضافة، مضاعفة، تنصيف...) وتعطينا في النهاية <strong>النتيجة النهائية المعلومة</strong> وتطلب معرفة <strong>الكمية أو القيمة الابتدائية المجهولة</strong>.</p>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 جدول تحويل العمليات في المسار العكسي:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>العبارة في نص المسألة (المسار الأمامي)</th>
                            <th>العملية الحسابية الأصلية</th>
                            <th>العملية العكسية المطبقة (المسار المعكوس)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>أضاف / اشترى إضافي / ربح / كسب</td>
                            <td>جمع (+)</td>
                            <td><strong>طرح (–)</strong></td>
                        </tr>
                        <tr>
                            <td>أنفق / صرف / تصدق / نقص / نزل</td>
                            <td>طرح (–)</td>
                            <td><strong>جمع (+)</strong></td>
                        </tr>
                        <tr>
                            <td>ضاعف / ضرب / أمثال</td>
                            <td>ضرب ($\times$)</td>
                            <td><strong>قسمة ($\div$)</strong></td>
                        </tr>
                        <tr>
                            <td>نصف / وزع بالتساوي / قسم</td>
                            <td>قسمة ($\div$)</td>
                            <td><strong>ضرب ($\times$)</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout-box callout-tip">
                💡 <strong>التحقق الذاتي الإلزامي:</strong> بعد إيجاد القيمة الابتدائية، أعد قراءة المسألة من بدايتها وطبق العمليات بالترتيب الطبيعي للتأكد من الوصول إلى نفس الرقم النهائي تماماً!
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_MID_QUIZ_1M = r"""
        <!-- ملخص مراجعة منتصف الفصل الثالث -->
        <article class="summary-card" id="summary-mid-quiz">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> مراجعة مركزة: اختبار منتصف الفصل الثالث (ص ١١٦)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 خريطة مراجعة مهارات معادلات الخطوة الواحدة:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>نوع المعادلة</th>
                            <th>الصورة العامة</th>
                            <th>العملية العكسية للحل</th>
                            <th>مثال محلول</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>معادلة جمع</td>
                            <td>$\text{س} + أ = ب$</td>
                            <td>طرح (أ) من الطرفين</td>
                            <td>$\text{س} + \text{٨} = \text{٣} \implies \text{س} = \text{–}\text{٥}$</td>
                        </tr>
                        <tr>
                            <td>معادلة طرح</td>
                            <td>$\text{س} \text{–} أ = ب$</td>
                            <td>إضافة (أ) للطرفين</td>
                            <td>$\text{س} \text{–} \text{٤} = \text{–}\text{٩} \implies \text{س} = \text{–}\text{٥}$</td>
                        </tr>
                        <tr>
                            <td>معادلة ضرب</td>
                            <td>$أ \times \text{س} = ب$</td>
                            <td>قسمة الطرفين على (أ)</td>
                            <td>$\text{–}\text{٣}\text{س} = \text{٢١} \implies \text{س} = \text{–}\text{٧}$</td>
                        </tr>
                        <tr>
                            <td>مسألة عكسية</td>
                            <td>عمليات متسلسلة ونهاية معلومة</td>
                            <td>البدء من النهاية وعكس العمليات</td>
                            <td>عدد طرح منه ٥ ثم ضرب في ٢ فأصبح ١٤ $\implies ١٤ \div ٢ = ٧ + ٥ = ١٢$</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout-box callout-info">
                📌 <strong>مفتاح النجاح في الاختبار:</strong> ميز دائماً بين "حل المعادلة" و "التحقق من صحة الحل". حل المعادلة هو إيجاد قيمة المتغير، والتحقق هو التعويض بتلك القيمة في المعادلة الأصلية للتأكد من تساوي الطرفين.
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_3_5 = r"""
        <!-- ملخص الدرس 3-5 -->
        <article class="summary-card" id="summary-3-5">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٣-٥): المعادلات ذات الخطوتين (ص ١١٧ – ١٢١)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 استراتيجية الخطوتين لحل المعادلة:</h4>
                <p>المعادلة ذات الخطوتين تحتوي على عمليتين حسابيتين. القاعدة الذهبية لحلها هي <strong>عكس ترتيب العمليات</strong>:</p>
                <div class="rule-card-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 16px;">
                    <div class="rule-card" style="border-top-color: #2563eb; background: #eff6ff;">
                        <h5 style="color: #1e40af; font-size:1.05rem;">الخطوة الأولى: التخلص من الجمع أو الطرح</h5>
                        <p>• نتخلص من الثابت المضاف أو المطروح أولاً بإضافة نظيره الجمعي لكلا الطرفين.</p>
                        <p style="font-weight:700; margin-top:4px;">في $\text{٣}\text{س} + \text{٢} = \text{٢٣}$ نطرح ٢ من الطرفين: $\text{٣}\text{س} = \text{٢١}$.</p>
                    </div>
                    <div class="rule-card" style="border-top-color: #10b981; background: #f0fdf4;">
                        <h5 style="color: #047857; font-size:1.05rem;">الخطوة الثانية: التخلص من الضرب أو القسمة</h5>
                        <p>• نتخلص من معامل المتغير بالقسمة أو الضرب في كلا الطرفين.</p>
                        <p style="font-weight:700; margin-top:4px;">نقسم على ٣: $\text{س} = \frac{\text{٢١}}{\text{٣}} = \text{٧}$.</p>
                    </div>
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 نموذج خطوات الحل والتحقق:</h4>
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:14px 18px; margin:8px 0;">
                    <p><strong>حل المعادلة: $\text{–}\text{٢}\text{ص} \text{–} \text{٧} = \text{٣}$</strong></p>
                    <p>• الخطوة ١: أضف ٧ إلى كلا الطرفين $\implies \text{–}\text{٢}\text{ص} = \text{٣} + \text{٧} = \text{١٠}$</p>
                    <p>• الخطوة ٢: اقسم كلا الطرفين على (–٢) $\implies \text{ص} = \frac{\text{١٠}}{\text{–}\text{٢}} = \text{–}\text{٥}$</p>
                    <p>• <strong>التحقق:</strong> $\text{–}\text{٢}(\text{–}\text{٥}) \text{–} \text{٧} = \text{١٠} \text{–} \text{٧} = \text{٣}$ (الطرفان متطابقان ✓).</p>
                </div>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>تنبيه الإشارات:</strong> عندما يكون المعامل سالباً مثل $\text{–}\text{٣}\text{س}$، انتبه أن تقسم على (–٣) وليس على ٣! وتذكر أن قسْمة عدد موجب على عدد سالب تعطي عدداً سالباً دائماً.
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_3_6 = r"""
        <!-- ملخص الدرس 3-6 -->
        <article class="summary-card" id="summary-3-6">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٣-٦): القياس: المحيط والمساحة (ص ١٢٢ – ١٢٧)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 القوانين والصيغ الهندسية للمستطيل والمربع:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الشكل الهندسي</th>
                            <th>صيغة المحيط (الإطار الخارجي)</th>
                            <th>صيغة المساحة (السطح الداخلي)</th>
                            <th>الوحدات القياسية</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>المستطيل</strong> (الطول ل، العرض ض)</td>
                            <td>$مح = ٢ل + ٢ض$ أو $مح = ٢(ل + ض)$</td>
                            <td>$م = ل \times ض$ (الطول × العرض)</td>
                            <td>المحيط: وحدات طولية (م، سم)<br>المساحة: وحدات مربعة (م²، سم²)</td>
                        </tr>
                        <tr>
                            <td><strong>المربع</strong> (طول ضلعه ل)</td>
                            <td>$مح = ٤ل$ (مجموع أضلاعه الأربعة)</td>
                            <td>$م = {ل}^٢$ (الضلع × نفسه)</td>
                            <td>المحيط: وحدات طولية<br>المساحة: وحدات مربعة</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 إيجاد البعد المجهول باستعمال المعادلات:</h4>
                <div style="background:#f0fdfa; border:1px solid #99f6e4; padding:14px 18px; border-radius:8px; margin:8px 0;">
                    <p><strong>١) إذا كانت المساحة معلومة:</strong> نقسم المساحة على البعد المعلوم: $\text{العرض} = \frac{\text{المساحة}}{\text{الطول}}$.</p>
                    <p style="margin-top:6px;"><strong>٢) إذا كان المحيط معلوماً:</strong> نكتب معادلة المحيط ذات الخطوتين ونحلها:</p>
                    <p style="margin-top:4px;">مثال: مستطيل محيطه ٤٠ سم وعرضه ٨ سم $\implies \text{٤٠} = \text{٢}\text{ل} + \text{٢}(\text{٨}) \implies \text{٤٠} = \text{٢}\text{ل} + \text{١٦} \implies \text{٢}\text{ل} = \text{٢٤} \implies \text{ل} = \text{١٢}$ سم.</p>
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 التمييز السريع بين المحيط والمساحة في المسائل الحياتية:</h4>
                <ul style="margin: 8px 24px; line-height: 2;">
                    <li><strong>مسائل المحيط:</strong> سياج حديقة، شريط زينة، إطار لوحة، مضمار جري حول ملعب، حبل تطويق.</li>
                    <li><strong>مسائل المساحة:</strong> ورق جدران، دهان حائط، فرش سجاد، تبليط أرضيات، زراعة عشب في حديقة.</li>
                </ul>
            </div>

            __FOOTER__
        </article>
"""

def get_all_summaries_html():
    s_3_3 = RAW_SUMMARY_3_3.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٣-٣)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    s_3_4 = RAW_SUMMARY_3_4.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٣-٤)", "استراتيجية حل المسألة")).replace("__FOOTER__", make_teacher_footer())
    s_mid = RAW_SUMMARY_MID_QUIZ_1M.replace("__HEADER__", make_school_header("مراجعة منتصف الفصل الثالث", "مراجعة شاملة ومفاهيم")).replace("__FOOTER__", make_teacher_footer())
    s_3_5 = RAW_SUMMARY_3_5.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٣-٥)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    s_3_6 = RAW_SUMMARY_3_6.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٣-٦)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    
    return (
        SUMMARIES_SECTION_START +
        s_3_3 +
        s_3_4 +
        s_mid +
        s_3_5 +
        s_3_6 +
        "\n    </section><!-- /#summaries-section -->\n"
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    html = get_all_summaries_html()
    with open('section_1m_summaries.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"section_1m_summaries.html written successfully, length: {len(html)}")
