# -*- coding: utf-8 -*-
import os
import base64
import subprocess
import sys

# Load logo
logo_path = 'شعار المتقدمة.png'
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')
    logo_data_uri = f"data:image/png;base64,{logo_b64}"
else:
    logo_data_uri = ""

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الإذاعة المدرسية المتميزة: قيمة التعاون (12 دقيقة) | المدارس المتقدمة للتعلم الذكي</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #1e3a8a;
            --primary-dark: #172554;
            --primary-light: #eff6ff;
            --secondary: #0d9488;
            --secondary-light: #f0fdfa;
            --accent: #b45309;
            --accent-gold: #d97706;
            --dark: #0f172a;
            --gray-100: #f8fafc;
            --gray-200: #e2e8f0;
            --gray-300: #cbd5e1;
            --gray-600: #475569;
            --gray-700: #334155;
            --white: #ffffff;
            --radius-sm: 6px;
            --radius-md: 10px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', 'Cairo', sans-serif;
        }}

        @page {{
            size: A4;
            margin: 12mm 14mm;
        }}

        body {{
            background-color: #f1f5f9;
            color: var(--dark);
            line-height: 1.7;
            padding: 20px;
            direction: rtl;
        }}

        .page-container {{
            max-width: 920px;
            margin: 0 auto;
            background: #ffffff;
            padding: 32px;
            border-radius: var(--radius-md);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            border: 1px solid var(--gray-200);
        }}

        /* Print Bar */
        .no-print-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(135deg, #1e3a8a, #0d9488);
            color: #fff;
            padding: 10px 20px;
            border-radius: var(--radius-sm);
            margin-bottom: 20px;
        }}

        .btn-print {{
            background: #f59e0b;
            color: #1e293b;
            font-weight: 800;
            padding: 7px 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.92rem;
            transition: all 0.2s;
        }}

        .btn-print:hover {{
            background: #d97706;
            color: #ffffff;
        }}

        /* Official School Header */
        .school-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px double var(--primary);
            padding-bottom: 12px;
            margin-bottom: 18px;
        }}

        .header-side-right {{
            text-align: right;
            font-size: 0.88rem;
            line-height: 1.55;
            font-weight: 600;
            color: var(--gray-700);
        }}

        .header-side-right .main-title {{
            color: var(--primary);
            font-weight: 800;
            font-size: 0.98rem;
        }}

        .header-side-right .school-name {{
            color: var(--secondary);
            font-weight: 900;
            font-size: 1.1rem;
        }}

        .header-logo-center {{
            text-align: center;
        }}

        .header-logo-center img {{
            max-height: 75px;
            width: auto;
            object-fit: contain;
        }}

        .header-side-left {{
            text-align: left;
            font-size: 0.86rem;
            line-height: 1.55;
            color: var(--gray-700);
        }}

        .tag-badge {{
            display: inline-block;
            background: var(--primary-light);
            color: var(--primary);
            padding: 2px 10px;
            border-radius: 6px;
            font-weight: 700;
            border: 1px solid #bfdbfe;
            margin-top: 4px;
        }}

        /* Title Banner */
        .broadcast-title-banner {{
            text-align: center;
            background: linear-gradient(135deg, #1e3a8a, #1d4ed8);
            color: #ffffff;
            padding: 14px 12px;
            border-radius: var(--radius-sm);
            margin-bottom: 18px;
            border: 1px solid #3b82f6;
        }}

        .broadcast-title-banner h1 {{
            font-size: 1.45rem;
            font-weight: 900;
            margin-bottom: 4px;
            color: #fef08a;
        }}

        .broadcast-title-banner .sub {{
            font-size: 0.95rem;
            color: #e0e7ff;
            font-weight: 600;
        }}

        /* Timing Table */
        .timing-section {{
            margin-bottom: 20px;
        }}

        .timing-section h3 {{
            color: var(--primary);
            margin-bottom: 8px;
            font-size: 1.05rem;
            font-weight: 800;
        }}

        table.timing-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.86rem;
        }}

        table.timing-table th, table.timing-table td {{
            border: 1px solid var(--gray-300);
            padding: 6px 10px;
            text-align: center;
        }}

        table.timing-table th {{
            background: #1e3a8a;
            color: #ffffff;
            font-weight: 800;
        }}

        table.timing-table tr:nth-child(even) {{
            background: #f8fafc;
        }}

        /* Section Cards */
        .section-card {{
            background: #ffffff;
            border: 1px solid var(--gray-200);
            border-right: 4px solid var(--primary);
            border-radius: var(--radius-sm);
            padding: 14px 18px;
            margin-bottom: 14px;
        }}

        .section-card.quran {{ border-right-color: #059669; }}
        .section-card.hadith {{ border-right-color: #0d9488; }}
        .section-card.speech {{ border-right-color: #2563eb; }}
        .section-card.facts {{ border-right-color: #d97706; }}
        .section-card.drama {{ border-right-color: #7c3aed; }}
        .section-card.quiz {{ border-right-color: #e11d48; }}
        .section-card.poetry {{ border-right-color: #0891b2; }}
        .section-card.conclusion {{ border-right-color: #1e3a8a; }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px dashed var(--gray-300);
            padding-bottom: 6px;
            margin-bottom: 10px;
        }}

        .card-header h2 {{
            font-size: 1.1rem;
            font-weight: 800;
            color: var(--primary-dark);
        }}

        .time-pill {{
            background: #fef3c7;
            color: #92400e;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.78rem;
            font-weight: 800;
            border: 1px solid #fde68a;
            margin-right: 6px;
        }}

        .speaker-badge {{
            background: #e0f2fe;
            color: #0369a1;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 700;
        }}

        .dialogue-turn {{
            margin-bottom: 8px;
            line-height: 1.75;
            font-size: 0.94rem;
        }}

        .speaker-name {{
            font-weight: 800;
            color: var(--primary);
            display: inline-block;
            margin-left: 5px;
        }}

        .stage-direction {{
            color: #64748b;
            font-size: 0.84rem;
            font-style: italic;
            font-weight: 600;
        }}

        .quran-box {{
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 6px;
            padding: 12px 16px;
            text-align: center;
            font-family: 'Amiri', serif;
            font-size: 1.25rem;
            line-height: 2.1;
            color: #065f46;
            margin: 8px 0;
        }}

        .hadith-box {{
            background: #f0fdfa;
            border: 1px solid #99f6e4;
            border-radius: 6px;
            padding: 10px 16px;
            font-family: 'Amiri', serif;
            font-size: 1.18rem;
            line-height: 2;
            color: #115e59;
            margin: 8px 0;
            text-align: center;
        }}

        .speech-content {{
            font-size: 0.94rem;
            text-align: justify;
            color: #1e293b;
            line-height: 1.8;
        }}

        .facts-list {{
            list-style: none;
            padding: 0;
        }}

        .facts-list li {{
            position: relative;
            padding-right: 24px;
            margin-bottom: 6px;
            font-size: 0.92rem;
            color: #334155;
            line-height: 1.65;
        }}

        .facts-list li::before {{
            content: "💡";
            position: absolute;
            right: 0;
            top: 1px;
            font-size: 0.9rem;
        }}

        .drama-box {{
            background: #faf5ff;
            border: 1px solid #e9d5ff;
            border-radius: 6px;
            padding: 10px 14px;
            margin: 8px 0;
        }}

        .quiz-card {{
            background: #fff1f2;
            border: 1px solid #fecdd3;
            border-radius: 6px;
            padding: 10px 14px;
            margin-bottom: 8px;
        }}

        .quiz-q {{
            font-weight: 800;
            color: #9f1239;
            font-size: 0.92rem;
        }}

        .quiz-a {{
            color: #4c0519;
            font-size: 0.88rem;
            background: #ffe4e6;
            padding: 2px 8px;
            border-radius: 4px;
            display: inline-block;
            margin-top: 4px;
        }}

        .poem-box {{
            background: #ecfeff;
            border: 1px solid #a5f3fc;
            border-radius: 6px;
            padding: 12px;
            text-align: center;
            font-family: 'Amiri', serif;
            font-size: 1.15rem;
            color: #155e75;
            line-height: 2;
            margin: 8px 0;
        }}

        /* Official Signatures */
        .official-signatures {{
            margin-top: 24px;
            padding-top: 14px;
            border-top: 2px dashed var(--gray-300);
            display: flex;
            justify-content: space-between;
            text-align: center;
        }}

        .sig-block {{
            flex: 1;
        }}

        .sig-role {{
            font-weight: 800;
            color: var(--primary);
            font-size: 0.88rem;
            margin-bottom: 2px;
        }}

        .sig-name {{
            font-weight: 700;
            color: var(--gray-700);
            font-size: 0.84rem;
        }}

        @media print {{
            body {{
                background: #ffffff;
                padding: 0;
            }}
            .page-container {{
                box-shadow: none;
                border: none;
                padding: 0;
                max-width: 100%;
            }}
            .no-print-bar {{
                display: none;
            }}
            .section-card {{
                margin-bottom: 10px;
                padding: 10px 14px;
            }}
        }}
    </style>
</head>
<body>

<div class="page-container">

    <div class="no-print-bar">
        <div>
            <strong>📻 الإذاعة المدرسية الصباحية المعتمدة (12 دقيقة كاملة)</strong>
            <span style="margin-right: 12px; font-size: 0.88rem; opacity: 0.9;">موضوع: التعاون وصنع الأثر</span>
        </div>
        <button class="btn-print" onclick="window.print()">🖨️ طباعة الإذاعة / حفظ كـ PDF</button>
    </div>

    <!-- Official School Header -->
    <header class="school-header">
        <div class="header-side-right">
            <div>المملكة العربية السعودية</div>
            <div class="main-title">وزارة التعليم</div>
            <div>الإدارة العامة للتعليم بمحافظة جدة</div>
            <div class="school-name">المدارس المتقدمة للتعلم الذكي</div>
        </div>

        <div class="header-logo-center">
            {f'<img src="{logo_data_uri}" alt="شعار المدارس المتقدمة للتعلم الذكي">' if logo_data_uri else '<div style="font-weight:900; font-size:1.1rem; color:#1e3a8a;">[شعار المدارس المتقدمة]</div>'}
        </div>

        <div class="header-side-left">
            <div><strong>جماعة:</strong> الإذاعة المدرسية</div>
            <div><strong>النشاط:</strong> النشاط الطلابي الصباحي</div>
            <div><strong>الفصل الدراسي:</strong> الثاني - العام الدراسي الحالي</div>
            <div class="tag-badge">إشراف: أ. محمد عبدالله جمعة</div>
        </div>
    </header>

    <!-- Title Banner -->
    <div class="broadcast-title-banner">
        <h1>🎙️ «قُوَّتُـنَا فِي تَعَاوُنِـنَا .. يَدٌ بِيَدٍ نَبْنِي المَسِيرَةَ ونَصْنَعُ الأَثَر» 🎙️</h1>
        <div class="sub">برنامج إذاعي متكامل، مدروس التوقيت (12 دقيقة بالتمام)، رفيع الصياغة واللغة</div>
    </div>

    <!-- Timing Table -->
    <section class="timing-section">
        <h3>⏱️ جدول خطة التوقيت وتوزيع الأدوار (إجمالي: 12:00 دقيقة)</h3>
        <table class="timing-table">
            <thead>
                <tr>
                    <th style="width: 5%;">#</th>
                    <th style="width: 25%;">فقرة البرنامج</th>
                    <th style="width: 25%;">الطالب المنفذ</th>
                    <th style="width: 20%;">المدة المحددة</th>
                    <th style="width: 25%;">التوقيت التراكمي</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td><strong>شارة البداية والمقدمة الترحيبية</strong></td>
                    <td>مقدم 1 + مقدم 2</td>
                    <td>1 دقيقة و 30 ثانية</td>
                    <td>00:00 - 01:30</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td><strong>آيات عطرة من الذكر الحكيم</strong></td>
                    <td>قارئ الإذاعة: ................</td>
                    <td>1 دقيقة و 30 ثانية</td>
                    <td>01:30 - 03:00</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td><strong>الهدي النبوي الشريف</strong></td>
                    <td>طالب الحديث: ................</td>
                    <td>1 دقيقة و 00 ثانية</td>
                    <td>03:00 - 04:00</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td><strong>كلمة الصباح: فلسفة التعاون</strong></td>
                    <td>خطيب الصباح: ................</td>
                    <td>2 دقيقة و 15 ثانية</td>
                    <td>04:00 - 06:15</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td><strong>هل تعلم؟ (عجائب التعاون في الكون)</strong></td>
                    <td>طالب المعرفة: ................</td>
                    <td>1 دقيقة و 30 ثانية</td>
                    <td>06:15 - 07:45</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td><strong>مشهد مسرحي حواري: سر حزمة العصي</strong></td>
                    <td>طالب 1 + طالب 2</td>
                    <td>2 دقيقة و 00 ثانية</td>
                    <td>07:45 - 09:45</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td><strong>مسابقة الصباح التفاعلية (سؤال وجائزة)</strong></td>
                    <td>مسؤول المسابقة: ................</td>
                    <td>1 دقيقة و 00 ثانية</td>
                    <td>09:45 - 10:45</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td><strong>شعر الصباح ودرر الحكمة</strong></td>
                    <td>شاعر الصباح: ................</td>
                    <td>0 دقيقة و 45 ثانية</td>
                    <td>10:45 - 11:30</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td><strong>دعاء الصباح والختام الرسمي</strong></td>
                    <td>مقدم 1 + مقدم 2</td>
                    <td>0 دقيقة و 30 ثانية</td>
                    <td>11:30 - 12:00</td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- 1. The Introduction -->
    <div class="section-card">
        <div class="card-header">
            <h2>1. المقدمة الإذاعية وشارة الصباح</h2>
            <div>
                <span class="speaker-badge">المقدم 1 & المقدم 2</span>
                <span class="time-pill">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            <span class="stage-direction">(بنبرة واثقة هادئة ومبتسمة):</span>
            بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيم، الحَمْدُ للهِ الَّذِي جَعَلَ الاجْتِمَاعَ رَحْمَة، وَالتَّفَرُّقَ نِقْمَة، وَأَلَّفَ بَيْنَ قُلُوبِ عِبَادِهِ فَأَصْبَحُوا بِنِعْمَتِهِ إِخْوَانَا. وَالصَّلاةُ وَالسَّلامُ عَلَى نَبِيِّ الرَّحْمَة، القَائِلِ بِلِسَانِ الصِّدْق: «يَدُ اللهِ مَعَ الجَمَاعَة».
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            <span class="stage-direction">(بنبرة ترحيبية مفعمة بالحيوية والاعتزاز):</span>
            سَعَادَةَ مُدِيرِ المَدْرَسَةِ الفَاضِل، أَعْزَاءَنَا المُعَلِّمِينَ الكِرَام، إِخْوَانَنَا الطُّلابَ النُّجَبَاء؛ مَعَ إِشْرَاقَةِ هَذَا الصَّبَاحِ المُتَجَدِّد، فِي صَرْحِنَا التَّعْلِيمِيِّ الرَّائِد <strong>«المدارس المتقدمة للتعلم الذكي»</strong>، نُهْدِيكُمْ تَحِيَّةَ الإِسْلامِ الخَالِدَة: فالسَّلامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ تَعَالَى وَبَرَكَاتُه، وَأَسْعَدَ اللهُ صَبَاحَكُمْ بِكُلِّ خَيْرٍ وَفَلاح.
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            قَطْرَةُ المَاءِ بِمُفْرَدِهَا تَجِفُّ فِي لَحْظَة، لَكِنَّهَا حِينَ تَلْتَقِي بِأَخَوَاتِهَا تَغْدُو نَهْراً دَافِقاً يَسْقِي الحَيَاة.. وَاللَّبِنَةُ الوَاحِدَةُ قَدْ تَبْدُو حَجَراً ضَعِيفاً، فَإِذَا ارْتَبَطَتْ بِبَقِيَّةِ اللَّبِنَاتِ شَيَّدَتْ صَرْحاً شَامِخاً يَتَحَدَّى العَوَاصِف.
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            وَمِنْ هُنَا، يُسْعِدُ جَمَاعَةَ الإِذَاعَةِ المَدْرَسِيَّةِ أَنْ تُخَصِّصَ لِقَاءَهَا هَذَا اليَوْمِ لِخُلُقٍ رَفِيعٍ، وَسِرٍّ مِنْ أَسْرَارِ النَّجَاحِ الكُبْرَى.. عَنْ <strong>«قِيمَةِ التَّعَاوُنِ وَالتَّكَاتُف»</strong>. خَيْرُ مَا نَفْتَتِحُ بِهِ دُرُوبَنَا، نُورٌ مِنْ نُورِ السَّمَاء؛ مَعَ القُرْآنِ الكَرِيمِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم القارئ)</span>.
        </div>
    </div>

    <!-- 2. Holy Quran -->
    <div class="section-card quran">
        <div class="card-header">
            <h2>2. نفحات إيمانية: القرآن الكريم</h2>
            <div>
                <span class="speaker-badge">القارئ</span>
                <span class="time-pill">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">القارئ:</span>
            <span class="stage-direction">(يرتل بخشوع وأحكام تجويد واضحة):</span>
            أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيم • بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيم:
        </div>
        <div class="quran-box">
            ﴿ يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تُحِلُّوا شَعَائِرَ اللَّهِ وَلَا الشَّهْرَ الْحَرَامَ وَلَا الْهَدْيَ وَلَا الْقَلَائِدَ وَلَا آمِّينَ الْبَيْتَ الْحَرَامَ يَبْتَغُونَ فَضْلًا مِّن رَّبِّهِمْ وَرِضْوَانًا ۚ وَإِذَا حَلَلْتُمْ فَاصْطَادُوا ۚ وَلَا يَجْرِمَنَّكُمْ شَنَآنُ قَوْمٍ أَن صَدُّوكُمْ عَنِ الْمَسْجِدِ الْحَرَامِ أَن تَعْتَدُوا ۘ وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ ۚ وَاتَّقُوا اللَّهَ ۖ إِنَّ اللَّهَ شَدِيدُ الْعِقَابِ ﴾
            <div style="font-size: 0.9rem; color: #047857; margin-top: 4px;">[سورة المائدة: آية 2]</div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">القارئ:</span>
            صَدَقَ اللهُ العَظِيم.
        </div>
    </div>

    <!-- 3. Prophetic Hadith -->
    <div class="section-card hadith">
        <div class="card-header">
            <h2>3. قطوف السيرة: الهدي النبوي الشريف</h2>
            <div>
                <span class="speaker-badge">طالب الحديث</span>
                <span class="time-pill">⏱️ 1:00 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            وَبَعْدَ أَنْ تَعَطَّرَتِ الأَسْمَاعُ بِكَلَامِ رَبِّ البَرِيَّة، نَمْضِي إِلَى رِيَاضِ السُّنَّةِ النَّبَوِيَّةِ المُطَهَّرَة؛ مَعَ الحَدِيثِ الشَّرِيفِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="hadith-box">
            عَنْ أَبِي مُوسَى الأَشْعَرِيِّ - رَضِيَ اللهُ عَنْهُ - عَنِ النَّبِيِّ ﷺ قَالَ:<br>
            <strong>«إِنَّ المُؤْمِنَ لِلْمُؤْمِنِ كَالْبُنْيَانِ يَشُدُّ بَعْضُهُ بَعْضاً»</strong><br>
            <span style="font-size: 0.98rem;">— وَشَبَّكَ بَيْنَ أَصَابِعِهِ الشَّرِيفَة. [مُتَّفَقٌ عَلَيْه]</span>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">طالب الحديث:</span>
            <span class="stage-direction">(موجز البيان):</span>
            يُرْشِدُنَا النَّبِيُّ ﷺ فِي هَذَا المَثَلِ البَلِيغِ إِلَى أَنَّ تَمَاسُكَ المُجْتَمَعِ لا يَتَحَقَّقُ إِلا بِأَنْ يَكُونَ كُلُّ فَرْدٍ فِيهِ دِعَامَةً لأَخِيه، كَمَا تَتَسَانَدُ لَبِنَاتُ الجِدَارِ فَلا تَسْقُط.
        </div>
    </div>

    <!-- 4. Morning Speech -->
    <div class="section-card speech">
        <div class="card-header">
            <h2>4. كلمة الصباح: «فلسفة التعاون.. كيف يصنع المجموع ما يعجز عنه الفرد؟»</h2>
            <div>
                <span class="speaker-badge">خطيب الصباح</span>
                <span class="time-pill">⏱️ 2:15 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            كَلِمَةُ الصَّبَاحِ هِيَ بَوْصَلَةُ اليَوْمِ وَمِشْعَلُ الفِكْر.. وَمَعَ كَلِمَةِ الصَّبَاحِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="speech-content">
            <p><strong>بِسْمِ اللهِ، وَالحَمْدُ لله، وَالصَّلاةُ وَالسَّلامُ عَلَى رَسُولِ الله..</strong></p>
            <p style="margin-top: 6px;">
                أَيُّهَا الحَفْلُ الكَرِيم: مَا مِنْ إِنْجَازٍ بَشَرِيٍّ عَبْرَ التَّارِيخِ تَحَقَّقَ بِجُهْدِ إِنْسَانٍ بِمُفْرَدِه! إِنَّ المَسَاجِدَ الكُبْرَى، وَالمُسْتَشْفَيَاتِ العِمْلاقَة، وَالمَرْكَبَاتِ الفَضَائِيَّة، بَلْ حَتَّى هَذَا الصَّرْحَ التَّعْلِيمِيَّ الَّذِي نَقِفُ فِي فِنَائِهِ اليَوْم؛ كُلُّهَا لَمْ تَكُنْ لِتَقُومَ لَوْلا أَنَّ أَيْدِيَ كَثِيرَةً ارْتَفَعَتْ مَعاً، وَأَفْكَاراً تَلاقَتْ، وَجُهُوداً تَكَاتَفَت.
            </p>
            <p style="margin-top: 6px;">
                إِنَّ التَّعَاوُنَ لَيْسَ مُجَرَّدَ مُسَاعَدَةٍ عَابِرَةٍ تُقَدِّمُهَا لِصَدِيقِك، بَلْ هُوَ <strong>«عَقْلِيَّةٌ حَضَارِيَّة»</strong> وَنَمَطُ حَيَاة. حِينَ تَتَعَاوَنُ مَعَ زَمِيلِكَ فِي حَلِّ مَسْأَلَةٍ رِيَاضِيَّةٍ مُسْتَعْصِيَة، فَأَنْتَ لا تَمْنَحُهُ حَلّاً فَحَسْب، بَلْ تُشْعِلُ فِكْرَكُمَا مَعاً.. وَحِينَ يَتَعَاوَنُ الفَصْلُ فِي الحِفَاظِ عَلَى نَظَافَتِهِ وَنِظَامِهِ، تَتَحَوَّلُ البِيئَةُ المَدْرَسِيَّةُ إِلَى وَاحَةٍ جَاذِبَةٍ لِلإِبْدَاعِ وَالتَّفَوُّق.
            </p>
            <p style="margin-top: 6px;">
                لِنَتَذَكَّرْ دَائِماً أَنَّ الإِنْسَانَ مَهْمَا بَلَغَ مِنْ ذَكَاءٍ وَقُوَّة، يَبْقَى عَاجِزاً عَنْ بُلُوغِ كُلِّ غَايَاتِهِ وَحْدَه، أَمَّا فِي ظِلِّ رُوحِ الفَرِيقِ الوَاحِد، فَإِنَّ أَقَلَّ الجُهُودِ تُثْمِرُ أَعْظَمَ النَّتَائِج. فَكُونُوا عَوْناً لإِخْوَانِكُم، يَكُنِ اللهُ فِي عَوْنِكُم!
            </p>
        </div>
    </div>

    <!-- 5. Did you know? -->
    <div class="section-card facts">
        <div class="card-header">
            <h2>5. فقرة هل تعلم؟: عجائب التعاون في المخلوقات</h2>
            <div>
                <span class="speaker-badge">طالب المعرفة</span>
                <span class="time-pill">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            مَعْلُومَاتٌ ثَرِيَّة، وَحَقَائِقُ تَبْعَثُ فِي النَّفْسِ الدَّهْشَةَ وَالإِلْهَام.. مَعَ فَقْرَةِ «هَلْ تَعْلَم؟» وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <ul class="facts-list">
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ طُيُورَ الإِوَزِّ حِينَ تُهَاجِر، تَطِيرُ عَلَى شَكْلِ حَرْفِ (V)؛ لأَنَّ حَرَكَةَ أَجْنِحَةِ كُلِّ طَائِرٍ تُوَلِّدُ تَيَّاراً هَوَائِيّاً صَاعِداً يُخَفِّفُ جُهْدَ الطَّائِرِ الَّذِي يَلِيه، مِمَّا يَزِيدُ مَدَى الطَّيَرَانِ بِنِسْبَةِ 71% مُقَارَنَةً بِطَيَرَانِ الطَّائِرِ بِمُفْرَدِه!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ خَلِيَّةَ النَّحْلِ الَّتِي تَضُمُّ عَشَرَاتِ الآلافِ مِنَ النَّحْلات، لا يُمْكِنُ أَنْ تَنْتَجَ قَطْرَةَ عَسَلٍ وَاحِدَةٍ إِلا عَبْرَ نِظَامِ تَعَاوُنٍ شَدِيدِ الدِّقَّة، حَيْثُ تَتَوَزَّعُ المَهَامُّ بَيْنَ الحِرَاسَة، وَالتَّنْظِيف، وَجَمْعِ الرَّحِيق، وَتَرْبِيَةِ الصِّغَار!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ نَمْلَةً وَاحِدَةً لا تَسْتَطِيعُ حَمْلَ وَزْنٍ يَفُوقُ عِدَّةَ غِرَامَات، لَكِنَّ جَمَاعَةَ النَّمْلِ تَتَعَاوَنُ مَعاً لِبِنَاءِ جُسُورٍ حَيَّةٍ بِأَجْسَادِهَا لِتَعْبُرَ فَوْقَ المِيَاهِ وَالمُنْحَدَرَات!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ شَرِكَاتِ الفَضَاءِ وَالتِّكْنُولُوجْيَا الحَدِيثَةَ تُعْتَبَرُ أَنْجَحَ أَمْثِلَةِ التَّعَاوُنِ البَشَرِي، حَيْثُ يَشْتَرِكُ آلافُ العُلَمَاءِ وَالمُهَنْدِسِينَ مِنْ عِدَّةِ تَخَصُّصَاتٍ لإِطْلاقِ صَارُوخٍ وَاحِدٍ إِلَى المَدَار!</li>
        </ul>
    </div>

    <!-- 6. Acting Sketch -->
    <div class="section-card drama">
        <div class="card-header">
            <h2>6. مشهد حواري تمثيلي: «سِرُّ حُزْمَةِ العِصِيّ»</h2>
            <div>
                <span class="speaker-badge">الطالبان: زيد & عمر</span>
                <span class="time-pill">⏱️ 2:00 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            التَّجْرِبَةُ خَيْرُ بُرْهَان، وَالمَشْهَدُ الصَّادِقُ يَرْسَخُ فِي الأَذْهَانِ مَا لا تَرْسَخُهُ الكَلِمَات.. نَتْرُكُكُمْ مَعَ هَذَا المَشْهَدِ التَّمْثِيلِيِّ القَصِيرِ بَيْنَ الطَّالِبَيْن: <span style="border-bottom: 1px dotted #888;">(زيد وعمر)</span>.
        </div>
        <div class="drama-box">
            <div class="dialogue-turn">
                <span class="speaker-name">زيد:</span>
                <span class="stage-direction">(يَقْتَرِبُ مِن عُمَر وَيَرَاهُ يُمْسِكُ أَعْوَاداً خَشَبِيَّةً مَرْبُوطَةً مَعاً):</span>
                صَبَاحُ الخَيْرِ يَا عُمَر! أَرَاكَ تُمْسِكُ هَذِهِ الأَعْوَادَ الخَشَبِيَّةَ مُنْذُ الصَّبَاحِ.. مَاذَا تَصْنَعُ بِهَا يَا صَدِيقِي؟
            </div>
            <div class="dialogue-turn">
                <span class="speaker-name">عمر:</span>
                <span class="stage-direction">(بِابْتِسَامَةٍ وَثِقَة):</span>
                صَبَاحُ النُّورِ يَا زَيْد! أُجْرِي تَجْرِبَةً حَكِيمَةً وَرِثْنَاهَا عَنِ الأَجْدَاد.. دَعْنِي أُشَارِكْكَ إِيَّاهَا: خُذْ هَذَا العُودَ المُنْفَرِد، وَحَاوِلْ أَنْ تَكْسِرَه!
            </div>
            <div class="dialogue-turn">
                <span class="speaker-name">زيد:</span>
                <span class="stage-direction">(يَأْخُذُ العُودَ المُنْفَرِدَ وَيَكْسِرُهُ بِسُهُولَةٍ بَيْنَ أَصَابِعِه):</span>
                هَا هُوَ ذَا قَدْ كُسِرَ فِي طَرْفَةِ عَيْن! لَمْ يُكَلِّفْنِي حَتَّى أَدْنَى مَجْهُود! فَمَا الغَرِيبُ فِي ذَلِك؟
            </div>
            <div class="dialogue-turn">
                <span class="speaker-name">عمر:</span>
                <span class="stage-direction">(يَمُدُّ لَهُ الحُزْمَةَ الكَامِلَةَ المُتَرَابِطَة):</span>
                حَسَناً يَا زَيْد.. خُذِ الآنَ هَذِهِ الحُزْمَةَ المُكَوَّنَةَ مِنْ عَشَرَةِ أَعْوَادٍ مَرْبُوطَةٍ بِإِحْكَام، وَحَاوِلْ كَسْرَهَا!
            </div>
            <div class="dialogue-turn">
                <span class="speaker-name">زيد:</span>
                <span class="stage-direction">(يَقْبِضُ عَلَيْهَا بِكِلْتَا يَدَيْهِ وَيَحَاوِلُ بِكُلِّ قُوَّتِهِ فَيَعْجِزُ وَيَتَنَفَّسُ بِعُمْق):</span>
                عَجِيبٌ أَمْرُهَا! إِنَّهَا صَلْبَةٌ جِدّاً! حَاوَلْتُ بِكُلِّ طَاقَتِي فَلَمْ أَسْتَطِعْ حَتَّى أَنْ أَثْنِيَهَا، رَغْمَ أَنَّ كُلَّ عُودٍ فِيهَا هُوَ عُودٌ ضَعِيفٌ بِمُفْرَدِه!
            </div>
            <div class="dialogue-turn">
                <span class="speaker-name">عمر:</span>
                <span class="stage-direction">(يُوَجِّهُ خِطَابَهُ إِلَى طُلابِ المَدْرَسَةِ فِي الطَّابُورِ بِصَوْتٍ عَالٍ وَمُؤَثِّر):</span>
                أَصَبْتَ يَا زَيْد! هَذَا هُوَ سِرُّ التَّعَاوُن! حِينَ نَكُونُ مُتَفَرِّقِينَ، يَكْسِرُنَا أَبْسَطُ اخْتِلافٍ وَتَهْزِمُنَا أَتْفَهُ الصِّعَاب.. أَمَّا حِينَ نَتَرَابَطُ وَنَتَكَاتَفُ كَهَذِهِ الحُزْمَةِ الوَاحِدَة، فَلَنْ تَسْتَطِيعَ أَعْتَى التَّحَدِّيَاتِ أَنْ تَنْزِعَ هَيْبَتَنَا أَوْ تُعَطِّلَ مَسِيرَتَنَا فِي طَلَبِ العِلْمِ وَبِنَاءِ الوَطَن!
            </div>
        </div>
    </div>

    <!-- 7. Interactive Morning Quiz -->
    <div class="section-card quiz">
        <div class="card-header">
            <h2>7. مسابقة الصباح التفاعلية: «سؤال.. وجائزة»</h2>
            <div>
                <span class="speaker-badge">مسؤول المسابقة</span>
                <span class="time-pill">⏱️ 1:00 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            وَالآنَ مَعَ فَقْرَةِ التَّحَدِّي وَالتَّفَاعُلِ مَعَ أَبْطَالِ الطَّابُورِ الصَّبَاحِيّ؛ مَعَ مُسَابَقَةِ «سُؤَالٌ وَجَائِزَة» وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="quiz-card">
            <div class="quiz-q">❓ السؤال الأول (سريع التفكير):</div>
            <div>مَا هُوَ الطَّائِرُ الَّذِي يَطِيرُ فِي سِرْبٍ عَلَى شَكْلِ حَرْفِ (V) لِيُوَفِّرَ 71% مِن طَاقَةِ طَيَرَانِهِ بِالتَّعَاوُن؟</div>
            <div class="quiz-a">✅ الإجابة الصحيحة: <strong>طائر الإوز البري (Wild Geese).</strong></div>
        </div>
        <div class="quiz-card">
            <div class="quiz-q">❓ السؤال الثاني (آية وحديث):</div>
            <div>فِي أَيِّ سُورَةٍ قُرْآنِيَّةٍ وَرَدَ الأَمْرُ الإِلَهِيُّ الصَّرِيح: ﴿وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ﴾؟</div>
            <div class="quiz-a">✅ الإجابة الصحيحة: <strong>سورة المائدة (الآية 2).</strong></div>
        </div>
        <div class="stage-direction" style="margin-top: 4px;">
            *(ملاحظة للمشرف والمقدم: يتم استدعاء أول طالبين يجيبان بشكل صحيح من الطابور وتسليمهما جائزة رمزية فورية)*.
        </div>
    </div>

    <!-- 8. Poetry and Wisdom -->
    <div class="section-card poetry">
        <div class="card-header">
            <h2>8. درر الحكمة وشعر الصباح</h2>
            <div>
                <span class="speaker-badge">شاعر الصباح</span>
                <span class="time-pill">⏱️ 0:45 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            الشِّعْرُ مِرْآةُ الحِكْمَة، وَالحِكْمَةُ ضَالَّةُ المُؤْمِن.. مَعَ شِعْرِ الصَّبَاحِ وَحِكْمَةِ اليَوْمِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div style="margin: 6px 0; font-size: 0.94rem; color: #1e293b;">
            <strong>💎 حكمة اليوم:</strong> «إِذَا أَرَدْتَ أَنْ تَسِيرَ سَرِيعاً فَسِرْ وَحْدَك، وَإِذَا أَرَدْتَ أَنْ تَصِلَ بَعِيداً فَسِرْ مَعَ الآخَرِين».
        </div>
        <div class="poem-box">
            تَـأْبَى الرِّمَاحُ إِذَا اجْتَمَعْنَ تَكَسُّراً &nbsp;&nbsp;&nbsp;&nbsp; وَإِذَا افْتَرَقْنَ تَكَسَّرَتْ آحَادَا<br>
            بِالتَّعَاوُنِ تَرْتَقِي أُمَمٌ فَمَا &nbsp;&nbsp;&nbsp;&nbsp; عَرَفَ الفَلاحَ مَنِ اسْتَبَدَّ وَأَدْبَرَا<br>
            ابْسُطْ يَدَيْكَ لِمَنْ أَتَاكَ مُعَاوِناً &nbsp;&nbsp;&nbsp;&nbsp; تَجِدِ الحَيَاةَ مَحَبَّةً وَتَيَسُّـرَا
        </div>
    </div>

    <!-- 9. Conclusion and Dua -->
    <div class="section-card conclusion">
        <div class="card-header">
            <h2>9. دعاء الصباح والختام الرسمي</h2>
            <div>
                <span class="speaker-badge">مقدم 1 & مقدم 2</span>
                <span class="time-pill">⏱️ 0:30 د</span>
            </div>
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 1:</span>
            <span class="stage-direction">(يدعو بخشوع ويؤمّن الجميع):</span>
            وَفِي خِتَامِ إِذَاعَتِنَا، نَسْأَلُ اللهَ العَلِيَّ القَدِير:  
            <strong>«اللَّهُمَّ أَلِّفْ بَيْنَ قُلُوبِنَا، وَأَصْلِحْ ذَاتَ بَيْنِنَا، وَاجْعَلْنَا إِخْوَةً مُتَحَابِّينَ مُتَعَاوِنِينَ عَلَى الخَيْر، وَبَارِكْ فِي مَدْرَسَتِنَا وَمُعَلِّمِينَا، وَاجْعَلْ يَوْمَنَا هَذَا يَوْماً مُبَارَكاً حَافِلاً بِالعِلْمِ وَالتَّفَوُّق»</strong>.
        </div>
        <div class="dialogue-turn">
            <span class="speaker-name">المقدم 2:</span>
            شُكْراً لِحُسْنِ اسْتِمَاعِكُمْ وَكَرِيمِ تَفَاعُلِكُم.. طَابَ صَبَاحُكُمْ بِكُلِّ خَيْر، وَدُمْتُمْ صَرْحاً لِلْعِلْمِ وَالمَعْرِفَة.
        </div>
        <div class="dialogue-turn" style="text-align: center; font-weight: 800; font-size: 1.05rem; color: var(--primary); margin-top: 8px;">
            وَالسَّلامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ تَعَالَى وَبَرَكَاتُه!
        </div>
    </div>

    <!-- Official Signatures Block -->
    <footer class="official-signatures">
        <div class="sig-block">
            <div class="sig-role">مقدمو الإذاعة</div>
            <div class="sig-name">جماعة الإذاعة المدرسية</div>
        </div>
        <div class="sig-block">
            <div class="sig-role">المشرف على الإذاعة</div>
            <div class="sig-name">أ. محمد عبدالله جمعة</div>
        </div>
        <div class="sig-block">
            <div class="sig-role">رائد النشاط الطلابي</div>
            <div class="sig-name">أ. ........................</div>
        </div>
        <div class="sig-block">
            <div class="sig-role">مدير المدرسة</div>
            <div class="sig-name">أ. ........................</div>
        </div>
    </footer>

</div>

</body>
</html>
"""

output_html = 'اذاعة_مدرسية_التعاون_12_دقيقة.html'
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

output_pdf = 'اذاعة_مدرسية_التعاون_12_دقيقة.pdf'
abs_html = os.path.abspath(output_html)
abs_pdf = os.path.abspath(output_pdf)
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

cmd = [
    chrome_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={abs_pdf}',
    abs_html
]

subprocess.run(cmd, capture_output=True, text=True)
print("Updated successfully.")
