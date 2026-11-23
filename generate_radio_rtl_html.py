# -*- coding: utf-8 -*-
"""
Script to create a complete, beautifully designed RTL HTML file for the 12-minute School Radio Broadcast.
"""

import os
import base64
import subprocess

logo_path = 'شعار المتقدمة.png'
logo_b64 = ""
if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')
logo_uri = f"data:image/png;base64,{logo_b64}" if logo_b64 else ""

html_text = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الإذاعة المدرسية المتميزة: قيمة التعاون (12 دقيقة) | المدارس المتقدمة للتعلم الذكي</title>
    
    <!-- خطوط جوجل العربية الفاخرة: تجوال، كايرو، والأميري -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@500;600;700;800;900&family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #1e3a8a;
            --primary-dark: #0f172a;
            --primary-light: #eff6ff;
            --secondary: #0d9488;
            --secondary-light: #f0fdfa;
            --gold: #d97706;
            --gold-light: #fef3c7;
            --emerald: #059669;
            --emerald-light: #ecfdf5;
            --purple: #7c3aed;
            --purple-light: #faf5ff;
            --rose: #e11d48;
            --rose-light: #fff1f2;
            --cyan: #0891b2;
            --cyan-light: #ecfeff;
            --gray-50: #f8fafc;
            --gray-100: #f1f5f9;
            --gray-200: #e2e8f0;
            --gray-300: #cbd5e1;
            --gray-600: #475569;
            --gray-700: #334155;
            --gray-800: #1e293b;
            --white: #ffffff;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
            --shadow-lg: 0 10px 25px rgba(0,0,0,0.1);
            --radius: 12px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Tajawal', 'Cairo', sans-serif;
            -webkit-font-smoothing: antialiased;
        }}

        body {{
            background: #f1f5f9;
            color: var(--gray-800);
            line-height: 1.8;
            padding: 24px 16px;
            direction: rtl;
            text-align: right;
        }}

        .main-wrapper {{
            max-width: 950px;
            margin: 0 auto;
            background: var(--white);
            padding: 36px 40px;
            border-radius: var(--radius);
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--gray-200);
        }}

        /* شريط الأدوات العلوي ومؤقت الإذاعة */
        .interactive-bar {{
            background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%);
            color: var(--white);
            padding: 14px 20px;
            border-radius: var(--radius);
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            box-shadow: 0 4px 14px rgba(30, 58, 138, 0.25);
        }}

        .timer-display-group {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .timer-clock {{
            background: rgba(0, 0, 0, 0.35);
            padding: 6px 16px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 1.45rem;
            font-weight: 800;
            letter-spacing: 2px;
            color: #fef08a;
            border: 1px solid rgba(254, 240, 138, 0.3);
        }}

        .timer-btn {{
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.4);
            color: var(--white);
            padding: 6px 14px;
            border-radius: 6px;
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .timer-btn:hover {{
            background: rgba(255, 255, 255, 0.35);
        }}

        .btn-print {{
            background: #f59e0b;
            color: #1e293b;
            font-weight: 800;
            padding: 8px 22px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.95rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
            transition: all 0.2s;
        }}

        .btn-print:hover {{
            background: #d97706;
            color: #ffffff;
            transform: translateY(-1px);
        }}

        /* الترويسة المدرسية الرسمية */
        .school-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 3px double var(--primary);
            padding-bottom: 18px;
            margin-bottom: 24px;
            gap: 16px;
        }}

        .header-right {{
            text-align: right;
            font-size: 0.92rem;
            line-height: 1.6;
            color: var(--gray-700);
            font-weight: 600;
        }}

        .header-right .country {{
            font-weight: 700;
            color: var(--gray-800);
        }}

        .header-right .ministry {{
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--primary);
        }}

        .header-right .school {{
            font-size: 1.18rem;
            font-weight: 900;
            color: var(--secondary);
            margin-top: 2px;
        }}

        .header-center {{
            text-align: center;
        }}

        .header-center img {{
            max-height: 85px;
            width: auto;
            object-fit: contain;
            filter: drop-shadow(0 2px 5px rgba(0,0,0,0.1));
        }}

        .header-left {{
            text-align: left;
            font-size: 0.88rem;
            line-height: 1.6;
            color: var(--gray-700);
        }}

        .tag-supervisor {{
            display: inline-block;
            background: var(--primary-light);
            color: var(--primary);
            padding: 3px 12px;
            border-radius: 6px;
            font-weight: 800;
            border: 1px solid #bfdbfe;
            margin-top: 5px;
            font-size: 0.86rem;
        }}

        /* لافتة عنوان الإذاعة */
        .broadcast-banner {{
            text-align: center;
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
            color: var(--white);
            padding: 20px 16px;
            border-radius: var(--radius);
            margin-bottom: 26px;
            border: 2px solid #3b82f6;
            box-shadow: 0 4px 15px rgba(30, 58, 138, 0.2);
        }}

        .broadcast-banner h1 {{
            font-size: 1.65rem;
            font-weight: 900;
            color: #fef08a;
            margin-bottom: 6px;
            letter-spacing: -0.3px;
        }}

        .broadcast-banner .banner-subtitle {{
            font-size: 1.02rem;
            color: #e0e7ff;
            font-weight: 600;
        }}

        /* جدول إدارة التوقيت */
        .timing-wrapper {{
            margin-bottom: 28px;
        }}

        .timing-title {{
            color: var(--primary);
            font-size: 1.18rem;
            font-weight: 800;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        table.timing-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            box-shadow: var(--shadow-sm);
            border-radius: 8px;
            overflow: hidden;
        }}

        table.timing-table th {{
            background: #1e3a8a;
            color: var(--white);
            padding: 10px 14px;
            font-weight: 800;
            text-align: center;
            border: 1px solid #1e3a8a;
        }}

        table.timing-table td {{
            padding: 8px 12px;
            text-align: center;
            border: 1px solid var(--gray-300);
            font-weight: 600;
        }}

        table.timing-table tr:nth-child(even) {{
            background: #f8fafc;
        }}

        table.timing-table tr:hover {{
            background: #eff6ff;
        }}

        /* بطاقات الفقرات الإذاعية */
        .section-card {{
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-right: 5px solid var(--primary);
            border-radius: var(--radius);
            padding: 18px 22px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            page-break-inside: avoid;
        }}

        .section-card.quran {{ border-right-color: var(--emerald); }}
        .section-card.hadith {{ border-right-color: var(--secondary); }}
        .section-card.speech {{ border-right-color: #2563eb; }}
        .section-card.facts {{ border-right-color: var(--gold); }}
        .section-card.drama {{ border-right-color: var(--purple); }}
        .section-card.quiz {{ border-right-color: var(--rose); }}
        .section-card.poetry {{ border-right-color: var(--cyan); }}
        .section-card.conclusion {{ border-right-color: var(--primary); }}

        .card-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px dashed var(--gray-300);
            padding-bottom: 8px;
            margin-bottom: 14px;
            flex-wrap: wrap;
            gap: 8px;
        }}

        .card-title-text {{
            font-size: 1.18rem;
            font-weight: 800;
            color: var(--primary-dark);
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .card-badges {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .speaker-badge {{
            background: #e0f2fe;
            color: #0369a1;
            padding: 3px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 700;
            border: 1px solid #bae6fd;
        }}

        .time-badge {{
            background: var(--gold-light);
            color: #92400e;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 800;
            border: 1px solid #fde68a;
        }}

        .dialogue-row {{
            margin-bottom: 12px;
            line-height: 1.85;
            font-size: 0.98rem;
        }}

        .speaker-label {{
            font-weight: 800;
            color: var(--primary);
            margin-left: 6px;
            display: inline-block;
        }}

        .acting-cue {{
            color: #64748b;
            font-size: 0.88rem;
            font-style: italic;
            font-weight: 600;
            margin-left: 4px;
        }}

        /* الصناديق الخاصة للقرآن والحديث والشعر */
        .quran-container {{
            background: var(--emerald-light);
            border: 1px solid #a7f3d0;
            border-radius: 8px;
            padding: 18px 22px;
            text-align: center;
            font-family: 'Amiri', serif;
            font-size: 1.35rem;
            line-height: 2.3;
            color: #065f46;
            margin: 12px 0;
            box-shadow: inset 0 1px 4px rgba(0,0,0,0.02);
        }}

        .hadith-container {{
            background: var(--secondary-light);
            border: 1px solid #99f6e4;
            border-radius: 8px;
            padding: 16px 20px;
            text-align: center;
            font-family: 'Amiri', serif;
            font-size: 1.25rem;
            line-height: 2.1;
            color: #115e59;
            margin: 12px 0;
        }}

        .speech-body {{
            font-size: 0.98rem;
            text-align: justify;
            color: #1e293b;
            line-height: 1.9;
        }}

        .speech-body p {{
            margin-bottom: 8px;
        }}

        .facts-items {{
            list-style: none;
            padding: 0;
        }}

        .facts-items li {{
            position: relative;
            padding-right: 28px;
            margin-bottom: 10px;
            font-size: 0.96rem;
            color: #334155;
            line-height: 1.75;
        }}

        .facts-items li::before {{
            content: "💡";
            position: absolute;
            right: 0;
            top: 1px;
            font-size: 1rem;
        }}

        .drama-container {{
            background: var(--purple-light);
            border: 1px solid #e9d5ff;
            border-radius: 8px;
            padding: 14px 18px;
            margin: 10px 0;
        }}

        .quiz-item {{
            background: var(--rose-light);
            border: 1px solid #fecdd3;
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 10px;
        }}

        .quiz-question {{
            font-weight: 800;
            color: #9f1239;
            font-size: 0.96rem;
            margin-bottom: 4px;
        }}

        .quiz-answer {{
            color: #4c0519;
            font-size: 0.92rem;
            background: #ffe4e6;
            padding: 3px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-top: 4px;
        }}

        .poem-container {{
            background: var(--cyan-light);
            border: 1px solid #a5f3fc;
            border-radius: 8px;
            padding: 16px;
            text-align: center;
            font-family: 'Amiri', serif;
            font-size: 1.25rem;
            color: #155e75;
            line-height: 2.2;
            margin: 10px 0;
        }}

        /* التوقيعات الرسمية في نهاية الصفحة */
        .official-signatures-box {{
            margin-top: 32px;
            padding-top: 18px;
            border-top: 2px dashed var(--gray-300);
            display: flex;
            justify-content: space-between;
            text-align: center;
            gap: 12px;
        }}

        .sig-col {{
            flex: 1;
        }}

        .sig-col .col-role {{
            font-weight: 800;
            color: var(--primary);
            font-size: 0.92rem;
            margin-bottom: 4px;
        }}

        .sig-col .col-name {{
            font-weight: 700;
            color: var(--gray-700);
            font-size: 0.88rem;
        }}

        /* توجيهات الطباعة */
        @media print {{
            @page {{
                size: A4;
                margin: 12mm 14mm;
            }}
            body {{
                background: var(--white);
                padding: 0;
            }}
            .main-wrapper {{
                border: none;
                box-shadow: none;
                padding: 0;
                max-width: 100%;
            }}
            .interactive-bar {{
                display: none !important;
            }}
            .section-card {{
                box-shadow: none;
                margin-bottom: 12px;
                padding: 10px 14px;
            }}
        }}
    </style>
</head>
<body>

<div class="main-wrapper">

    <!-- شريط تفاعلي مع مؤقت البث وزر الطباعة -->
    <div class="interactive-bar">
        <div class="timer-display-group">
            <span>⏱️ <strong>مؤقت الإذاعة (12 دقيقة):</strong></span>
            <div class="timer-clock" id="stopwatch">00:00</div>
            <button class="timer-btn" onclick="startTimer()">تشغيل</button>
            <button class="timer-btn" onclick="pauseTimer()">إيقاف</button>
            <button class="timer-btn" onclick="resetTimer()">إعادة</button>
        </div>
        <div>
            <button class="btn-print" onclick="window.print()">🖨️ طباعة الإذاعة الرسمية (PDF)</button>
        </div>
    </div>

    <!-- ترويسة المدرسة الرسمية المعتمدة -->
    <header class="school-header">
        <div class="header-right">
            <div class="country">المملكة العربية السعودية</div>
            <div class="ministry">وزارة التعليم</div>
            <div>الإدارة العامة للتعليم بمحافظة جدة</div>
            <div class="school">المدارس المتقدمة للتعلم الذكي</div>
        </div>

        <div class="header-center">
            {f'<img src="{logo_uri}" alt="شعار المدارس المتقدمة للتعلم الذكي">' if logo_uri else '<div style="font-weight:900; font-size:1.15rem; color:#1e3a8a;">[شعار المدارس المتقدمة]</div>'}
        </div>

        <div class="header-left">
            <div><strong>جماعة:</strong> الإذاعة المدرسية</div>
            <div><strong>النشاط:</strong> النشاط الطلابي الصباحي</div>
            <div><strong>الفصل الدراسي:</strong> الثاني - 1447 / 1448 هـ</div>
            <div class="tag-supervisor">إشراف: أ. محمد عبدالله جمعة</div>
        </div>
    </header>

    <!-- لافتة عنوان الإذاعة الصباحية -->
    <div class="broadcast-banner">
        <h1>🎙️ «قُوَّتُـنَا فِي تَعَاوُنِـنَا .. يَدٌ بِيَدٍ نَبْنِي المَسِيرَةَ ونَصْنَعُ الأَثَر» 🎙️</h1>
        <div class="banner-subtitle">برنامج إذاعي متكامل، مدروس التوقيت (12 دقيقة بالتمام)، رفيع الصياغة واللغة</div>
    </div>

    <!-- جدول إدارة الوقت وتوزيع المهام -->
    <section class="timing-wrapper">
        <div class="timing-title">⏱️ خطة إدارة الوقت وتوزيع الأدوار (إجمالي: 12:00 دقيقة)</div>
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
                    <td><strong>آيات عطرة من القرآن الكريم</strong></td>
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
                    <td><strong>مشهد حواري تمثيلي: سر حزمة العصي</strong></td>
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

    <!-- الفقرة 1: المقدمة الإذاعية -->
    <article class="section-card">
        <div class="card-top">
            <div class="card-title-text">
                <span>🎙️</span>
                <span>1. المقدمة الإذاعية وشارة الصباح</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">المقدم 1 & المقدم 2</span>
                <span class="time-badge">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            <span class="acting-cue">(بنبرة واثقة وهادئة ومبتسمة):</span>
            بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيم، الحَمْدُ للهِ الَّذِي جَعَلَ الاجْتِمَاعَ رَحْمَة، وَالتَّفَرُّقَ نِقْمَة، وَأَلَّفَ بَيْنَ قُلُوبِ عِبَادِهِ فَأَصْبَحُوا بِنِعْمَتِهِ إِخْوَانَا. وَالصَّلاةُ وَالسَّلامُ عَلَى نَبِيِّ الرَّحْمَة، القَائِلِ بِلِسَانِ الصِّدْق: «يَدُ اللهِ مَعَ الجَمَاعَة».
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            <span class="acting-cue">(بنبرة ترحيبية مفعمة بالحيوية والاعتزاز):</span>
            سَعَادَةَ مُدِيرِ المَدْرَسَةِ الفَاضِل، أَعْزَاءَنَا المُعَلِّمِينَ الكِرَام، إِخْوَانَنَا الطُّلابَ النُّجَبَاء؛ مَعَ إِشْرَاقَةِ هَذَا الصَّبَاحِ المُتَجَدِّد، فِي صَرْحِنَا التَّعْلِيمِيِّ الرَّائِد <strong>«المدارس المتقدمة للتعلم الذكي»</strong>، نُهْدِيكُمْ تَحِيَّةَ الإِسْلامِ الخَالِدَة: فالسَّلامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ تَعَالَى وَبَرَكَاتُه، وَأَسْعَدَ اللهُ صَبَاحَكُمْ بِكُلِّ خَيْرٍ وَفَلاح.
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            قَطْرَةُ المَاءِ بِمُفْرَدِهَا تَجِفُّ فِي لَحْظَة، لَكِنَّهَا حِينَ تَلْتَقِي بِأَخَوَاتِهَا تَغْدُو نَهْراً دَافِقاً يَسْقِي الحَيَاة.. وَاللَّبِنَةُ الوَاحِدَةُ قَدْ تَبْدُو حَجَراً ضَعِيفاً، فَإِذَا ارْتَبَطَتْ بِبَقِيَّةِ اللَّبِنَاتِ شَيَّدَتْ صَرْحاً شَامِخاً يَتَحَدَّى العَوَاصِف.
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            وَمِنْ هُنَا، يُسْعِدُ جَمَاعَةَ الإِذَاعَةِ المَدْرَسِيَّةِ أَنْ تُخَصِّصَ لِقَاءَهَا هَذَا اليَوْمِ لِخُلُقٍ رَفِيعٍ عَنْ <strong>«قِيمَةِ التَّعَاوُنِ وَالتَّكَاتُف»</strong>. خَيْرُ مَا نَفْتَتِحُ بِهِ دُرُوبَنَا، نُورٌ مِنْ نُورِ السَّمَاء؛ مَعَ القُرْآنِ الكَرِيمِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم القارئ)</span>.
        </div>
    </article>

    <!-- الفقرة 2: القرآن الكريم -->
    <article class="section-card quran">
        <div class="card-top">
            <div class="card-title-text">
                <span>📖</span>
                <span>2. نفحات إيمانية: القرآن الكريم</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">قارئ الإذاعة</span>
                <span class="time-badge">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">القارئ:</span>
            <span class="acting-cue">(يرتل بخشوع وتجويد هادئ ومتقن):</span>
            أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيم • بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيم:
        </div>
        <div class="quran-container">
            ﴿ يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تُحِلُّوا شَعَائِرَ اللَّهِ وَلَا الشَّهْرَ الْحَرَامَ وَلَا الْهَدْيَ وَلَا الْقَلَائِدَ وَلَا آمِّينَ الْبَيْتَ الْحَرَامَ يَبْتَغُونَ فَضْلًا مِّن رَّبِّهِمْ وَرِضْوَانًا ۚ وَإِذَا حَلَلْتُمْ فَاصْطَادُوا ۚ وَلَا يَجْرِمَنَّكُمْ شَنَآنُ قَوْمٍ أَن صَدُّوكُمْ عَنِ الْمَسْجِدِ الْحَرَامِ أَن تَعْتَدُوا ۘ <strong>وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ ۚ وَاتَّقُوا اللَّهَ ۖ إِنَّ اللَّهَ شَدِيدُ الْعِقَابِ</strong> ﴾
            <div style="font-size: 0.92rem; color: #047857; margin-top: 6px;">[سورة المائدة: آية 2]</div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">القارئ:</span>
            صَدَقَ اللهُ العَظِيم.
        </div>
    </article>

    <!-- الفقرة 3: الحديث النبوي الشريف -->
    <article class="section-card hadith">
        <div class="card-top">
            <div class="card-title-text">
                <span>✨</span>
                <span>3. قطوف السيرة: الهدي النبوي الشريف</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">طالب الحديث</span>
                <span class="time-badge">⏱️ 1:00 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            وَبَعْدَ أَنْ تَعَطَّرَتِ الأَسْمَاعُ بِكَلَامِ رَبِّ البَرِيَّة، نَمْضِي إِلَى رِيَاضِ السُّنَّةِ النَّبَوِيَّةِ المُطَهَّرَة؛ مَعَ الحَدِيثِ الشَّرِيفِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="hadith-container">
            عَنْ أَبِي مُوسَى الأَشْعَرِيِّ - رَضِيَ اللهُ عَنْهُ - عَنِ النَّبِيِّ ﷺ قَالَ:<br>
            <strong>«إِنَّ المُؤْمِنَ لِلْمُؤْمِنِ كَالْبُنْيَانِ يَشُدُّ بَعْضُهُ بَعْضاً»</strong><br>
            <span style="font-size: 1.02rem;">— وَشَبَّكَ بَيْنَ أَصَابِعِهِ الشَّرِيفَة. [مُتَّفَقٌ عَلَيْه]</span>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">طالب الحديث:</span>
            <span class="acting-cue">(بيان موجز ومؤثر):</span>
            يُرْشِدُنَا النَّبِيُّ ﷺ فِي هَذَا المَثَلِ البَلِيغِ إِلَى أَنَّ تَمَاسُكَ المُجْتَمَعِ لا يَتَحَقَّقُ إِلا بِأَنْ يَكُونَ كُلُّ فَرْدٍ فِيهِ دِعَامَةً لأَخِيه، كَمَا تَتَسَانَدُ لَبِنَاتُ الجِدَارِ فَلا تَسْقُط.
        </div>
    </article>

    <!-- الفقرة 4: كلمة الصباح -->
    <article class="section-card speech">
        <div class="card-top">
            <div class="card-title-text">
                <span>🎙️</span>
                <span>4. كلمة الصباح: «فلسفة التعاون.. كيف يصنع المجموع ما يعجز عنه الفرد؟»</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">خطيب الصباح</span>
                <span class="time-badge">⏱️ 2:15 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            كَلِمَةُ الصَّبَاحِ هِيَ بَوْصَلَةُ اليَوْمِ وَمِشْعَلُ الفِكْر.. وَمَعَ كَلِمَةِ الصَّبَاحِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="speech-body">
            <p><strong>بِسْمِ اللهِ، وَالحَمْدُ لله، وَالصَّلاةُ وَالسَّلامُ عَلَى رَسُولِ الله..</strong></p>
            <p>
                أَيُّهَا الحَفْلُ الكَرِيم: مَا مِنْ إِنْجَازٍ بَشَرِيٍّ عَبْرَ التَّارِيخِ تَحَقَّقَ بِجُهْدِ إِنْسَانٍ بِمُفْرَدِه! إِنَّ المَسَاجِدَ الكُبْرَى، وَالمُسْتَشْفَيَاتِ العِمْلاقَة، وَالمَرْكَبَاتِ الفَضَائِيَّة، بَلْ حَتَّى هَذَا الصَّرْحَ التَّعْلِيمِيَّ الَّذِي نَقِفُ فِي فِنَائِهِ اليَوْم؛ كُلُّهَا لَمْ تَكُنْ لِتَقُومَ لَوْلا أَنَّ أَيْدِيَ كَثِيرَةً ارْتَفَعَتْ مَعاً، وَأَفْكَاراً تَلاقَتْ، وَجُهُوداً تَكَاتَفَت.
            </p>
            <p>
                إِنَّ التَّعَاوُنَ لَيْسَ مُجَرَّدَ مُسَاعَدَةٍ عَابِرَةٍ تُقَدِّمُهَا لِصَدِيقِك، بَلْ هُوَ <strong>«عَقْلِيَّةٌ حَضَارِيَّة»</strong> وَنَمَطُ حَيَاة. حِينَ تَتَعَاوَنُ مَعَ زَمِيلِكَ فِي حَلِّ مَسْأَلَةٍ رِيَاضِيَّةٍ مُسْتَعْصِيَة، فَأَنْتَ لا تَمْنَحُهُ حَلّاً فَحَسْب، بَلْ تُشْعِلُ فِكْرَكُمَا مَعاً.. وَحِينَ يَتَعَاوَنُ الفَصْلُ فِي الحِفَاظِ عَلَى نَظَافَتِهِ وَنِظَامِهِ، تَتَحَوَّلُ البِيئَةُ المَدْرَسِيَّةُ إِلَى وَاحَةٍ جَاذِبَةٍ لِلإِبْدَاعِ وَالتَّفَوُّق.
            </p>
            <p>
                لِنَتَذَكَّرْ دَائِماً أَنَّ الإِنْسَانَ مَهْمَا بَلَغَ مِنْ ذَكَاءٍ وَقُوَّة، يَبْقَى عَاجِزاً عَنْ بُلُوغِ كُلِّ غَايَاتِهِ وَحْدَه، أَمَّا فِي ظِلِّ رُوحِ الفَرِيقِ الوَاحِد، فَإِنَّ أَقَلَّ الجُهُودِ تُثْمِرُ أَعْظَمَ النَّتَائِج. فَكُونُوا عَوْناً لإِخْوَانِكُم، يَكُنِ اللهُ فِي عَوْنِكُم!
            </p>
        </div>
    </article>

    <!-- الفقرة 5: هل تعلم؟ -->
    <article class="section-card facts">
        <div class="card-top">
            <div class="card-title-text">
                <span>💡</span>
                <span>5. فقرة هل تعلم؟: عجائب التعاون في الكائنات الحية</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">طالب المعرفة</span>
                <span class="time-badge">⏱️ 1:30 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            مَعْلُومَاتٌ ثَرِيَّة، وَحَقَائِقُ تَبْعَثُ فِي النَّفْسِ الدَّهْشَةَ وَالإِلْهَام.. مَعَ فَقْرَةِ «هَلْ تَعْلَم؟» وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <ul class="facts-items">
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ طُيُورَ الإِوَزِّ حِينَ تُهَاجِر، تَطِيرُ عَلَى شَكْلِ حَرْفِ (V)؛ لأَنَّ حَرَكَةَ أَجْنِحَةِ كُلِّ طَائِرٍ تُوَلِّدُ تَيَّاراً صَاعِداً يُخَفِّفُ جُهْدَ الطَّائِرِ الَّذِي يَلِيه، مِمَّا يَزِيدُ مَدَى الطَّيَرَانِ بِنِسْبَةِ <strong>71%</strong> مُقَارَنَةً بِطَيَرَانِ الطَّائِرِ بِمُفْرَدِه!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ خَلِيَّةَ النَّحْلِ الَّتِي تَضُمُّ عَشَرَاتِ الآلاف، لا يُمْكِنُ أَنْ تَنْتَجَ قَطْرَةَ عَسَلٍ وَاحِدَةٍ إِلا عَبْرَ نِظَامِ تَعَاوُنٍ شَدِيدِ الدِّقَّة، بَيْنَ الحِرَاسَة، وَالتَّنْظِيف، وَجَمْعِ الرَّحِيق، وَتَرْبِيَةِ الصِّغَار!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ نَمْلَةً وَاحِدَةً لا تَقْدِرُ عَلَى حَمْلِ حِمْلٍ كَبِير، لَكِنَّ مَجْمُوعَةَ النَّمْلِ تَتَعَاوَنُ مَعاً لِبِنَاءِ <strong>جُسُورٍ حَيَّةٍ بِأَجْسَادِهَا</strong> لِتَعْبُرَ بَقِيَّةُ المُسْتَعْمَرَةِ فَوْقَ المِيَاهِ وَالمُنْحَدَرَات!</li>
            <li><strong>هَلْ تَعْلَمُ</strong> أَنَّ أَعْظَمَ مَشَارِيعِ الفَضَاءِ وَالتِّكْنُولُوجْيَا الحَدِيثَةِ هِيَ نِتَاجُ فِرَقِ عَمَلٍ تَضُمُّ آلافَ العُلَمَاءِ وَالمُهَنْدِسِينَ مِنْ مُخْتَلَفِ التَّخَصُّصَات!</li>
        </ul>
    </article>

    <!-- الفقرة 6: المشهد التمثيلي -->
    <article class="section-card drama">
        <div class="card-top">
            <div class="card-title-text">
                <span>🎭</span>
                <span>6. مشهد حواري تمثيلي: «سِرُّ حُزْمَةِ العِصِيّ»</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">الطالبان: زيد & عمر</span>
                <span class="time-badge">⏱️ 2:00 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            التَّجْرِبَةُ خَيْرُ بُرْهَان، وَالمَشْهَدُ الصَّادِقُ يَرْسَخُ فِي الأَذْهَانِ مَا لا تَرْسَخُهُ الكَلِمَات.. نَتْرُكُكُمْ مَعَ هَذَا المَشْهَدِ التَّمْثِيلِيِّ القَصِيرِ بَيْنَ الطَّالِبَيْن: <span style="border-bottom: 1px dotted #888;">(زيد وعمر)</span>.
        </div>
        <div class="drama-container">
            <div class="dialogue-row">
                <span class="speaker-label">زيد:</span>
                <span class="acting-cue">(يَقْتَرِبُ مِن عُمَر وَيَرَاهُ يُمْسِكُ أَعْوَاداً خَشَبِيَّةً مَرْبُوطَةً مَعاً):</span>
                صَبَاحُ الخَيْرِ يَا عُمَر! أَرَاكَ تُمْسِكُ هَذِهِ الأَعْوَادَ الخَشَبِيَّةَ مُنْذُ الصَّبَاحِ.. مَاذَا تَصْنَعُ بِهَا يَا صَدِيقِي؟
            </div>
            <div class="dialogue-row">
                <span class="speaker-label">عمر:</span>
                <span class="acting-cue">(بِابْتِسَامَةٍ وَثِقَة):</span>
                صَبَاحُ النُّورِ يَا زَيْد! أُجْرِي تَجْرِبَةً حَكِيمَةً وَرِثْنَاهَا عَنِ الأَجْدَاد.. خُذْ هَذَا العُودَ المُنْفَرِد، وَحَاوِلْ أَنْ تَكْسِرَه!
            </div>
            <div class="dialogue-row">
                <span class="speaker-label">زيد:</span>
                <span class="acting-cue">(يَأْخُذُ العُودَ المُنْفَرِدَ وَيَكْسِرُهُ بِسُهُولَةٍ بَيْنَ أَصَابِعِه):</span>
                هَا هُوَ ذَا قَدْ كُسِرَ فِي طَرْفَةِ عَيْن! لَمْ يُكَلِّفْنِي حَتَّى أَدْنَى مَجْهُود! فَمَا الغَرِيبُ فِي ذَلِك؟
            </div>
            <div class="dialogue-row">
                <span class="speaker-label">عمر:</span>
                <span class="acting-cue">(يَمُدُّ لَهُ الحُزْمَةَ الكَامِلَةَ المُتَرَابِطَة):</span>
                حَسَناً يَا زَيْد.. خُذِ الآنَ هَذِهِ الحُزْمَةَ المُكَوَّنَةَ مِنْ عَشَرَةِ أَعْوَادٍ مَرْبُوطَةٍ بِإِحْكَام، وَحَاوِلْ كَسْرَهَا!
            </div>
            <div class="dialogue-row">
                <span class="speaker-label">زيد:</span>
                <span class="acting-cue">(يَقْبِضُ عَلَيْهَا بِكِلْتَا يَدَيْهِ وَيَحَاوِلُ بِكُلِّ قُوَّتِهِ فَيَعْجِزُ وَيَتَنَفَّسُ بِعُمْق):</span>
                عَجِيبٌ أَمْرُهَا! إِنَّهَا صَلْبَةٌ جِدّاً! حَاوَلْتُ بِكُلِّ طَاقَتِي فَلَمْ أَسْتَطِعْ حَتَّى أَنْ أَثْنِيَهَا، رَغْمَ أَنَّ كُلَّ عُودٍ فِيهَا ضَعِيفٌ بِمُفْرَدِه!
            </div>
            <div class="dialogue-row">
                <span class="speaker-label">عمر:</span>
                <span class="acting-cue">(يُوَجِّهُ خِطَابَهُ لِطُلابِ المَدْرَسَةِ فِي الطَّابُورِ بِصَوْتٍ عَالٍ وَمُؤَثِّر):</span>
                أَصَبْتَ يَا زَيْد! هَذَا هُوَ سِرُّ التَّعَاوُن! حِينَ نَكُونُ مُتَفَرِّقِينَ، يَكْسِرُنَا أَبْسَطُ اخْتِلافٍ وَتَهْزِمُنَا أَتْفَهُ الصِّعَاب.. أَمَّا حِينَ نَتَرَابَطُ كَهَذِهِ الحُزْمَةِ الوَاحِدَة، فَلَنْ تَسْتَطِيعَ أَعْتَى التَّحَدِّيَاتِ أَنْ تَنْزِعَ هَيْبَتَنَا أَوْ تُعَطِّلَ مَسِيرَتَنَا فِي طَلَبِ العِلْمِ وَبِنَاءِ الوَطَن!
            </div>
        </div>
    </article>

    <!-- الفقرة 7: مسابقة الصباح التفاعلية -->
    <article class="section-card quiz">
        <div class="card-top">
            <div class="card-title-text">
                <span>🎯</span>
                <span>7. مسابقة الصباح التفاعلية: «سؤال.. وجائزة»</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">مسؤول المسابقة</span>
                <span class="time-badge">⏱️ 1:00 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            وَالآنَ مَعَ فَقْرَةِ التَّحَدِّي وَالتَّفَاعُلِ مَعَ أَبْطَالِ الطَّابُورِ الصَّبَاحِيّ؛ مَعَ مُسَابَقَةِ «سُؤَالٌ وَجَائِزَة» وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div class="quiz-item">
            <div class="quiz-question">❓ السؤال الأول (سريع التفكير):</div>
            <div>مَا هُوَ الطَّائِرُ الَّذِي يَطِيرُ فِي سِرْبٍ عَلَى شَكْلِ حَرْفِ (V) لِيُوَفِّرَ 71% مِن طَاقَةِ طَيَرَانِهِ بِالتَّعَاوُن؟</div>
            <div class="quiz-answer">✅ الإجابة الصحيحة: <strong>طائر الإوز البري (Wild Geese).</strong></div>
        </div>
        <div class="quiz-item">
            <div class="quiz-question">❓ السؤال الثاني (آية قرآنية):</div>
            <div>فِي أَيِّ سُورَةٍ قُرْآنِيَّةٍ وَرَدَ قَوْلُهُ تَعَالَى: ﴿وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَىٰ وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ﴾؟</div>
            <div class="quiz-answer">✅ الإجابة الصحيحة: <strong>سورة المائدة (الآية 2).</strong></div>
        </div>
        <div class="acting-cue" style="margin-top: 6px;">
            *(توجيه للمشرف والمقدم: يتم استدعاء أول طالبين يجيبان بشكل صحيح من الطابور وتسليمهما جائزة رمزية فورية لتشجيع الحماس)*.
        </div>
    </article>

    <!-- الفقرة 8: درر الحكمة وشعر الصباح -->
    <article class="section-card poetry">
        <div class="card-top">
            <div class="card-title-text">
                <span>📜</span>
                <span>8. درر الحكمة وشعر الصباح</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">شاعر الصباح</span>
                <span class="time-badge">⏱️ 0:45 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            الشِّعْرُ مِرْآةُ الحِكْمَة، وَالحِكْمَةُ ضَالَّةُ المُؤْمِن.. مَعَ شِعْرِ الصَّبَاحِ وَحِكْمَةِ اليَوْمِ وَالطَّالِب: <span style="border-bottom: 1px dotted #888;">(اسم الطالب)</span>.
        </div>
        <div style="margin: 8px 0; font-size: 0.96rem; color: #1e293b;">
            <strong>💎 حكمة اليوم:</strong> «إِذَا أَرَدْتَ أَنْ تَسِيرَ سَرِيعاً فَسِرْ وَحْدَك، وَإِذَا أَرَدْتَ أَنْ تَصِلَ بَعِيداً فَسِرْ مَعَ الآخَرِين».
        </div>
        <div class="poem-container">
            تَـأْبَى الرِّمَاحُ إِذَا اجْتَمَعْنَ تَكَسُّراً &nbsp;&nbsp;&nbsp;&nbsp; وَإِذَا افْتَرَقْنَ تَكَسَّرَتْ آحَادَا<br>
            بِالتَّعَاوُنِ تَرْتَقِي أُمَمٌ فَمَا &nbsp;&nbsp;&nbsp;&nbsp; عَرَفَ الفَلاحَ مَنِ اسْتَبَدَّ وَأَدْبَرَا<br>
            ابْسُطْ يَدَيْكَ لِمَنْ أَتَاكَ مُعَاوِناً &nbsp;&nbsp;&nbsp;&nbsp; تَجِدِ الحَيَاةَ مَحَبَّةً وَتَيَسُّـرَا
        </div>
    </article>

    <!-- الفقرة 9: دعاء الصباح والختام -->
    <article class="section-card conclusion">
        <div class="card-top">
            <div class="card-title-text">
                <span>🤲</span>
                <span>9. دعاء الصباح والختام الرسمي</span>
            </div>
            <div class="card-badges">
                <span class="speaker-badge">مقدم 1 & مقدم 2</span>
                <span class="time-badge">⏱️ 0:30 د</span>
            </div>
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 1:</span>
            <span class="acting-cue">(يدعو بخشوع ويؤمّن الجميع):</span>
            وَفِي خِتَامِ إِذَاعَتِنَا، نَسْأَلُ اللهَ العَلِيَّ القَدِير:  
            <strong>«اللَّهُمَّ أَلِّفْ بَيْنَ قُلُوبِنَا، وَأَصْلِحْ ذَاتَ بَيْنِنَا، وَاجْعَلْنَا إِخْوَةً مُتَحَابِّينَ مُتَعَاوِنِينَ عَلَى الخَيْر، وَبَارِكْ فِي مَدْرَسَتِنَا وَمُعَلِّمِينَا، وَاجْعَلْ يَوْمَنَا هَذَا يَوْماً مُبَارَكاً حَافِلاً بِالعِلْمِ وَالتَّفَوُّق»</strong>.
        </div>
        <div class="dialogue-row">
            <span class="speaker-label">المقدم 2:</span>
            شُكْراً لِحُسْنِ اسْتِمَاعِكُمْ وَكَرِيمِ تَفَاعُلِكُم.. طَابَ صَبَاحُكُمْ بِكُلِّ خَيْر، وَدُمْتُمْ صَرْحاً لِلْعِلْمِ وَالمَعْرِفَة.
        </div>
        <div class="dialogue-row" style="text-align: center; font-weight: 800; font-size: 1.12rem; color: var(--primary); margin-top: 10px;">
            وَالسَّلامُ عَلَيْكُمْ وَرَحْمَةُ اللهِ تَعَالَى وَبَرَكَاتُه!
        </div>
    </article>

    <!-- جدول الاعتماد والتوقيعات الرسمية -->
    <footer class="official-signatures-box">
        <div class="sig-col">
            <div class="col-role">مقدمو الإذاعة</div>
            <div class="col-name">جماعة الإذاعة المدرسية</div>
        </div>
        <div class="sig-col">
            <div class="col-role">المشرف على الإذاعة</div>
            <div class="col-name">أ. محمد عبدالله جمعة</div>
        </div>
        <div class="sig-col">
            <div class="col-role">رائد النشاط الطلابي</div>
            <div class="col-name">أ. ........................</div>
        </div>
        <div class="sig-col">
            <div class="col-role">مدير المدرسة</div>
            <div class="col-name">أ. ........................</div>
        </div>
    </footer>

</div>

<!-- كود جافاسكريبت لإدارة مؤقت الإذاعة التفاعلي -->
<script>
    let timerSeconds = 0;
    let timerInterval = null;

    function formatTime(totalSec) {{
        const m = Math.floor(totalSec / 60);
        const s = totalSec % 60;
        return (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
    }}

    function startTimer() {{
        if (timerInterval) return;
        timerInterval = setInterval(() => {{
            timerSeconds++;
            document.getElementById('stopwatch').innerText = formatTime(timerSeconds);
            if (timerSeconds === 720) {{ // 12 minutes
                document.getElementById('stopwatch').style.color = '#ef4444';
            }}
        }}, 1000);
    }}

    function pauseTimer() {{
        clearInterval(timerInterval);
        timerInterval = null;
    }}

    function resetTimer() {{
        pauseTimer();
        timerSeconds = 0;
        document.getElementById('stopwatch').innerText = '00:00';
        document.getElementById('stopwatch').style.color = '#fef08a';
    }}
</script>

</body>
</html>
"""

# Save to main folder
out_file1 = 'اذاعة_مدرسية_التعاون_12_دقيقة.html'
with open(out_file1, 'w', encoding='utf-8') as f:
    f.write(html_text)

# Save to اوراق عمل folder as well
out_folder = 'اوراق عمل'
if os.path.exists(out_folder):
    out_file2 = os.path.join(out_folder, 'اذاعة_مدرسية_التعاون_12_دقيقة.html')
    with open(out_file2, 'w', encoding='utf-8') as f:
        f.write(html_text)

print(f"Generated HTML file successfully: {out_file1} ({os.path.getsize(out_file1)} bytes)")
if os.path.exists(out_folder):
    print(f"Copied to {out_file2} ({os.path.getsize(out_file2)} bytes)")
