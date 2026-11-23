# -*- coding: utf-8 -*-
"""
generator_summaries.py: Student Summaries for Lessons 4-2, 4-3, Mid-Quiz/Lab, and 4-4.
All include official school header and teacher signature at bottom left.
Uses raw strings to avoid any python escape issues with LaTeX.
"""

from generator_header_styles import make_school_header, make_teacher_footer

SUMMARIES_SECTION_START = r"""
    <!-- ========================================================================= -->
    <!-- القسم الثاني: الملخصات الشاملة للطلاب (متتالية)                              -->
    <!-- ========================================================================= -->
    <section id="summaries-section" class="master-section page-break">
        <div class="section-header-banner summaries">
            <h2>📚 القسم الثاني: الملخصات الشاملة للطلاب (متتالية)</h2>
            <span class="section-badge">شاملة ومبسطة للمذاكرة المركزة والمراجعة النهائية</span>
        </div>
"""

RAW_SUMMARY_4_2 = r"""
        <!-- ملخص الدرس 4-2 -->
        <article class="summary-card" id="summary-4-2">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٤-٢): حل المتباينات بالضرب أو بالقسمة (ص ١٣٠ – ١٣٤)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 الفكرة الرياضية الجوهرية (القاعدة الذهبية):</h4>
                <p>حل المتباينة بالضرب أو بالقسمة يتبع تماماً قواعد حل المعادلات الخطية مع <strong>استثناء جوهري وحيد وحاسم</strong> يتعلق بإشارة العدد الذي تضرب فيه أو تقسم عليه:</p>
            </div>

            <div class="rule-card-grid" style="grid-template-columns: 1fr 1fr; margin-bottom: 20px;">
                <div class="rule-card" style="border-top-color: #16a34a; background: #f0fdf4;">
                    <h5 style="color: #15803d; font-size:1.05rem;">١) الضرب أو القسمة في عدد موجب ($> ٠$)</h5>
                    <p>• <strong>يبقى اتجاه رمز المتباينة كما هو دون أي تغيير.</strong></p>
                    <p style="font-weight:700; margin-top:4px;">مثال: $\frac{\text{س}}{\text{٣}} \le \text{٥} \implies \text{س} \le \text{١٥}$</p>
                    <p style="font-weight:700;">مثال: $\text{٤}\text{ص} > \text{٢٠} \implies \text{ص} > \text{٥}$</p>
                </div>
                <div class="rule-card" style="border-top-color: #dc2626; background: #fef2f2;">
                    <h5 style="color: #b91c1c; font-size:1.05rem;">٢) الضرب أو القسمة في عدد سالب ($< ٠$) ⚠️</h5>
                    <p>• <strong>يجب عكس اتجاه رمز المتباينة فوراً:</strong></p>
                    <p style="font-weight:700; margin-top:4px;">($\le$ تصبح $\ge$) ، ($\ge$ تصبح $\le$) ، ($<$ تصبح $>$) ، ($>$ تصبح $<$)</p>
                    <p style="font-weight:700; color:#b91c1c;">مثال: $\text{–}\text{٢}\text{س} \ge \text{١٠} \implies \text{س} \le \text{–}\text{٥}$</p>
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 جدول التمييز البياني على خط الأعداد:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>رمز المتباينة</th>
                            <th>المعنى اللفظي</th>
                            <th>نوع الدائرة عند النقطة</th>
                            <th>اتجاه سهم التظليل</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>$\text{س} > أ$</td>
                            <td>أكبر من</td>
                            <td>دائرة مفتوحة $\circ$ (العدد ليس ضمن الحل)</td>
                            <td>يتجه نحو اليمين (الأعداد الأكبر)</td>
                        </tr>
                        <tr>
                            <td>$\text{س} \ge أ$</td>
                            <td>أكبر من أو يساوي (على الأقل)</td>
                            <td>دائرة مغلقة $\bullet$ (العدد ضمن الحل)</td>
                            <td>يتجه نحو اليمين</td>
                        </tr>
                        <tr>
                            <td>$\text{س} < أ$</td>
                            <td>أصغر من</td>
                            <td>دائرة مفتوحة $\circ$</td>
                            <td>يتجه نحو اليسار (الأعداد الأصغر)</td>
                        </tr>
                        <tr>
                            <td>$\text{س} \le أ$</td>
                            <td>أصغر من أو يساوي (على الأكثر)</td>
                            <td>دائرة مغلقة $\bullet$</td>
                            <td>يتجه نحو اليسار</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout-box callout-warning">
                ⚠️ <strong>خطأ شائع يقع فيه الطلاب:</strong> لا تنظر إلى إشارة الثابت في الطرف الآخر، بل انظر فقط إلى <strong>معامل المتغير الملاصق له</strong>! فمثلاً في المتباينة $\text{٣}\text{س} \ge \text{–}\text{١٢}$ نقسم على موجب ٣ ويبقى الرمز كما هو $\text{س} \ge \text{–}\text{٤}$ ولا يُعكس الرمز؛ لأن المقسوم عليه موجب ٣!
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_4_3 = r"""
        <!-- ملخص الدرس 4-3 -->
        <article class="summary-card" id="summary-4-3">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٤-٣): حل المتباينات متعددة الخطوات (ص ١٣٥ – ١٤٠)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 خوارزمية الخطوات الأربع لحل المتباينة متعددة الخطوات:</h4>
                <ol style="margin: 8px 24px; line-height: 2;">
                    <li><strong>الخطوة الأولى (التوزيع):</strong> فك الأقواس بضرب ما خارج القوس في كل حد داخله: $أ(ب + جـ) = أ ب + أ جـ$.</li>
                    <li><strong>الخطوة الثانية (التجميع):</strong> بسط كل طرف بمفرده بجمع الحدود المتشابهة.</li>
                    <li><strong>الخطوة الثالثة (عزل المتغيرات):</strong> اجمع الحدود التي تحتوي على المتغير في أحد الطرفين بنقل المعامل الأصغر.</li>
                    <li><strong>الخطوة الرابعة (عزل الثوابت وحساب الناتج):</strong> تخلص من الثابت بالجمع أو الطرح، ثم اقسم أو اضرب في المعامل (مع تذكر قاعدة عكس الإشارة إذا كان المعامل سالباً!).</li>
                </ol>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 مقارنة الحالات الخاصة عند حذف المتغيرات بالكامل:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>الحالة الناتجة</th>
                            <th>العبارة العددية المتبقية</th>
                            <th>الحكم الرياضي</th>
                            <th>مجموعة الحل والتمثيل البياني</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>عبارة صحيحة دائماً (متطابقة)</td>
                            <td>مثل: $\text{–}\text{٣} \le \text{٥}$ أو $\text{٨} > \text{٢}$</td>
                            <td>صحيحة لجميع الأعداد الحقيقية</td>
                            <td>مجموعة الحل: $\mathbb{R}$ (يظلل خط الأعداد كاملاً بسهمين متعاكسين)</td>
                        </tr>
                        <tr>
                            <td>عبارة خاطئة دائماً (تناقض مستحيل)</td>
                            <td>مثل: $\text{٧} < \text{–}\text{٢}$ أو $\text{٤} \le \text{١}$</td>
                            <td>مستحيلة الحل ولا يوجد عدد يحققها</td>
                            <td>مجموعة الحل: المجموعة الخالية $\emptyset$ (يترك خط الأعداد فارغاً دون تظليل)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout-box callout-tip">
                💡 <strong>استراتيجية ذكية للحل السريع:</strong> عندما يكون لديك المتغير في الطرفين، انقل دائماً المتغير ذو المعامل الأصغر نحو المعامل الأكبر (مثلاً في: $\text{٢}\text{س} + \text{٥} < \text{٥}\text{س} \text{–} \text{٤}$ انقل ٢س إلى الطرف الأيسر) لتحصل دائماً على معامل موجب يجنبك عناء عكس إشارة التباين والوقوع في أخطاء الإشارة السالبة!
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_MID_QUIZ_LAB = r"""
        <!-- مراجعة منتصف الفصل ومعمل الجبر -->
        <article class="summary-card" id="summary-mid-quiz">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> مراجعة مركزة: اختبار منتصف الفصل ومعمل الجبر (ص ١٤١ – ١٤٢)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 جدول المقارنة الجوهرية لأدوات الربط في المنطق الجبري:</h4>
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>وجه المقارنة</th>
                            <th>أداة الربط (و) - الوصل</th>
                            <th>أداة الربط (أو) - الفصل</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>العملية في المجموعات</td>
                            <td><strong>التقاطع ($\cap$):</strong> العناصر المشتركة فقط</td>
                            <td><strong>الاتحاد ($\cup$):</strong> جميع العناصر مجتمعة</td>
                        </tr>
                        <tr>
                            <td>الصيغة الجبرية الشائعة</td>
                            <td>تُكتب مدمجة: $أ \le \text{س} \le ب$</td>
                            <td>تُكتب منفصلة: $\text{س} < أ$ أو $\text{س} > ب$</td>
                        </tr>
                        <tr>
                            <td>الشكل الهندسي على خط الأعداد</td>
                            <td>قطعة مستقيمة محصورة بين نقطتين</td>
                            <td>شعاعان منفصلان يتجهان في اتجاهين متعاكسين</td>
                        </tr>
                        <tr>
                            <td>شرط صحة العبارة</td>
                            <td>يجب أن يتحقق <strong>كلا الشرطين معاً</strong> في آن واحد</td>
                            <td>يكفي تحقق <strong>أحد الشرطين على الأقل</strong></td>
                        </tr>
                        <tr>
                            <td>التناظر مع بوابات المنطق الحاسوبية</td>
                            <td>بوابة AND (توالي كهربائي)</td>
                            <td>بوابة OR (توازي كهربائي)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="callout-box callout-info">
                📌 <strong>نصيحة ذهبية للاختبار:</strong> قبل البدء بحل أي متباينة مركبة، حدد نوع الرابط أولاً: إذا كان (و) فابحث عن منطقة التداخل المشتركة، وإذا كان (أو) فظلل كلتا المنطقتين معاً على نفس خط الأعداد!
            </div>

            __FOOTER__
        </article>
"""

RAW_SUMMARY_4_4 = r"""
        <!-- ملخص الدرس 4-4 -->
        <article class="summary-card" id="summary-4-4">
            __HEADER__
            <div class="summary-title-bar">
                <h3><span>📖</span> ملخص الدرس (٤-٤): حل المتباينات المركبة (ص ١٤٣ – ١٤٧)</h3>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 النوع الأول: متباينات الوصل التي تتضمن (و)</h4>
                <p>• تكون صحيحة فقط عندما تكون كلتا المتباينتين صحيحتين، ومجموعة حلها هي منطقة <strong>تقاطع</strong> التمثيلين البيانيين.</p>
                <div style="background:#f8fafc; padding:12px 18px; border-radius:8px; border:1px solid #e2e8f0; margin:10px 0;">
                    <strong>مثال محلول من الكتاب:</strong> حل: $\text{–}\text{٢} \le \text{س} \text{–} \text{٣} < \text{٤}$<br>
                    • بإضافة ٣ إلى الأطراف الثلاثة بالتساوي: $\text{–}\text{٢} + \text{٣} \le \text{س} < \text{٤} + \text{٣} \implies \text{١} \le \text{س} < \text{٧}$<br>
                    • مجموعة الحل: $\{\text{س} \mid \text{١} \le \text{س} < \text{٧}\}$<br>
                    • التمثيل البياني: دائرة مغلقة عند ١، ودائرة مفتوحة عند ٧، وتظليل المسافة بينهما.
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 النوع الثاني: متباينات الفصل التي تتضمن (أو)</h4>
                <p>• تكون صحيحة إذا كانت إحدى المتباينتين على الأقل صحيحة، ومجموعة حلها هي <strong>اتحاد</strong> التمثيلين البيانيين.</p>
                <div style="background:#f8fafc; padding:12px 18px; border-radius:8px; border:1px solid #e2e8f0; margin:10px 0;">
                    <strong>مثال محلول:</strong> حل: $\text{س} + \text{٣} < \text{١}$ أو $\text{٢}\text{س} \ge \text{٨}$<br>
                    • المتباينة الأولى: $\text{س} < \text{–}\text{٢}$<br>
                    • المتباينة الثانية: $\text{س} \ge \text{٤}$<br>
                    • مجموعة الحل: $\{\text{س} \mid \text{س} < \text{–}\text{٢} \text{ أو } \text{س} \ge \text{٤}\}$<br>
                    • التمثيل البياني: دائرة مفتوحة عند –٢ مع سهم لليسار، ودائرة مغلقة عند ٤ مع سهم لليمين.
                </div>
            </div>

            <div style="margin-bottom: 20px;">
                <h4 style="color:#1e3a8a; margin-bottom:8px; font-weight:800;">🔹 الحالات الخاصة في المتباينات المركبة:</h4>
                <ul style="margin: 8px 24px;">
                    <li><strong>عدم وجود تقاطع في متباينة (و):</strong> إذا كان التمثيلان متعاكسين ولا يشتركان في أي نقطة (مثل: $\text{س} > \text{٥}$ و $\text{س} < \text{٢}$)، فإن مجموعة الحل هي $\emptyset$.</li>
                    <li><strong>تغطية كامل خط الأعداد في متباينة (أو):</strong> إذا تداخل الشعاعان المتعاكسان وغطيا جميع النقاط على خط الأعداد، فإن مجموعة الحل هي $\mathbb{R}$.</li>
                </ul>
            </div>

            __FOOTER__
        </article>
"""

def get_all_summaries_html():
    s_4_2 = RAW_SUMMARY_4_2.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٤-٢)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    s_4_3 = RAW_SUMMARY_4_3.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٤-٣)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    s_mid = RAW_SUMMARY_MID_QUIZ_LAB.replace("__HEADER__", make_school_header("مراجعة منتصف الفصل ومعمل الجبر", "مراجعة شاملة ومفاهيم")).replace("__FOOTER__", make_teacher_footer())
    s_4_4 = RAW_SUMMARY_4_4.replace("__HEADER__", make_school_header("ملخص الطالب: الدرس (٤-٤)", "ملخص ومفاهيم أساسية")).replace("__FOOTER__", make_teacher_footer())
    
    return (
        SUMMARIES_SECTION_START +
        s_4_2 +
        s_4_3 +
        s_mid +
        s_4_4 +
        "\n    </section><!-- /#summaries-section -->\n"
    )

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    html = get_all_summaries_html()
    print(f"Summaries HTML generated successfully, total length: {len(html)}")
