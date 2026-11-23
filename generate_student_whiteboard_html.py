# -*- coding: utf-8 -*-
"""
Generator script for Student-Facing Interactive Whiteboard Display:
إثبات تطابق المثلثات (SSS, SAS) وفق نموذج 6Es الاستقصائي
"""

import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>عرض السبورة التفاعلي: إثبات تطابق المثلثات (SSS, SAS)</title>
    <!-- Google Fonts: Cairo -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <!-- FontAwesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        cairo: ['Cairo', 'sans-serif'],
                    },
                    colors: {
                        chall: {
                            50: '#fff7ed',
                            100: '#ffedd5',
                            500: '#f97316',
                            600: '#ea580c',
                            700: '#c2410c',
                        },
                        math: {
                            blue: '#2563eb',
                            indigo: '#4f46e5',
                            emerald: '#059669',
                            rose: '#e11d48',
                            amber: '#d97706',
                            cyan: '#0891b2',
                        }
                    }
                }
            }
        }
    </script>
    <!-- MathJax for rendering math formulas -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true
            },
            svg: { fontCache: 'global' }
        };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
    <style>
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
        }
        .glow-chall {
            box-shadow: 0 0 25px rgba(249, 115, 22, 0.25);
        }
        .glow-blue {
            box-shadow: 0 0 25px rgba(37, 99, 235, 0.25);
        }
        .glow-emerald {
            box-shadow: 0 0 25px rgba(5, 150, 105, 0.25);
        }
        .tab-btn.active {
            background: linear-gradient(135deg, #ea580c, #c2410c);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(234, 88, 12, 0.35);
        }
        @media print {
            body { background: white !important; color: black !important; }
            .no-print { display: none !important; }
            .tab-pane { display: block !important; margin-bottom: 2rem !important; }
        }
    </style>
</head>
<body class="min-h-screen bg-slate-950 text-slate-100 flex flex-col antialiased selection:bg-orange-500 selection:text-white">

    <!-- Top Smartboard Header Bar -->
    <header class="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-50 px-4 py-3 shadow-lg no-print">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            
            <!-- Lesson Main Badge -->
            <div class="flex items-center gap-3">
                <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-orange-500 to-amber-500 flex items-center justify-center text-white shadow-lg shadow-orange-500/20 text-xl font-black">
                    <i class="fa-solid fa-shapes"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded-full bg-orange-500/20 text-orange-400 text-[11px] font-black border border-orange-500/30">رياضيات 1-2 • مسارات</span>
                        <span class="text-xs text-slate-400 font-bold">الدرس 3-4 (ص 170 – 177)</span>
                    </div>
                    <h1 class="text-lg sm:text-2xl font-black text-white tracking-wide">إثبات تطابق المثلثات: رحلة التحديات الستة (6Es)</h1>
                </div>
            </div>

            <!-- Smartboard Controls (Timer & Fullscreen) -->
            <div class="flex items-center gap-2 sm:gap-3">
                <!-- Interactive Challenge Timer -->
                <div class="bg-slate-800/90 border border-slate-700 px-3.5 py-1.5 rounded-xl flex items-center gap-2">
                    <i class="fa-regular fa-clock text-orange-400 animate-pulse"></i>
                    <span id="timer-display" class="font-mono text-base font-black text-orange-400">00:00</span>
                    <button onclick="toggleTimer()" id="timer-btn" class="text-xs bg-slate-700 hover:bg-slate-600 px-2 py-1 rounded text-slate-200 transition font-bold" title="تشغيل/إيقاف مؤقت التحدي">
                        <i class="fa-solid fa-play"></i>
                    </button>
                    <button onclick="resetTimer()" class="text-xs bg-slate-700 hover:bg-slate-600 px-2 py-1 rounded text-slate-200 transition" title="إعادة تعيين المؤقت">
                        <i class="fa-solid fa-rotate-right"></i>
                    </button>
                </div>

                <!-- Fullscreen Toggle -->
                <button onclick="toggleFullScreen()" class="bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 px-3 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5" title="ملء الشاشة للسبورة الذكية">
                    <i class="fa-solid fa-expand text-slate-400"></i>
                    <span class="hidden md:inline">ملء الشاشة</span>
                </button>
            </div>
        </div>

        <!-- 6Es Navigation Ribbon for the Smartboard -->
        <div class="max-w-7xl mx-auto mt-3 overflow-x-auto pb-1">
            <div class="flex items-center gap-1.5 min-w-max bg-slate-950/60 p-1.5 rounded-2xl border border-slate-800/80">
                <button onclick="showTab('tab-engage')" id="btn-engage" class="tab-btn active px-4 py-2 rounded-xl text-xs sm:text-sm font-bold transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/20 text-white flex items-center justify-center text-[10px]">1</span>
                    <span>⚡ 1. إشعال الشرارة (Engage)</span>
                </button>
                <button onclick="showTab('tab-explore')" id="btn-explore" class="tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-400 hover:text-white transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px]">2</span>
                    <span>🔬 2. مختبر الاستكشاف (Explore)</span>
                </button>
                <button onclick="showTab('tab-explain')" id="btn-explain" class="tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-400 hover:text-white transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px]">3</span>
                    <span>📐 3. شفرة البرهان (Explain)</span>
                </button>
                <button onclick="showTab('tab-engineer')" id="btn-engineer" class="tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-400 hover:text-white transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px]">4</span>
                    <span>🏗️ 4. التحدي الهندسي (Engineer)</span>
                </button>
                <button onclick="showTab('tab-elaborate')" id="btn-elaborate" class="tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-400 hover:text-white transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px]">5</span>
                    <span>⚔️ 5. تحدي الفرسان (Elaborate)</span>
                </button>
                <button onclick="showTab('tab-evaluate')" id="btn-evaluate" class="tab-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-400 hover:text-white transition flex items-center gap-2">
                    <span class="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center text-[10px]">6</span>
                    <span>🏆 6. تذكرة النصر (Evaluate)</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Interactive Display Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

        <!-- ============================================================= -->
        <!-- المحطة 1: ENGAGE - إشعال الشرارة والتحدي الاستهلالي -->
        <!-- ============================================================= -->
        <section id="tab-engage" class="tab-pane space-y-6">
            <!-- Stage Header Banner -->
            <div class="bg-gradient-to-l from-orange-600 via-amber-600 to-yellow-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white relative overflow-hidden">
                <div class="relative z-10 space-y-2">
                    <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-orange-200">
                        <i class="fa-solid fa-fire"></i> المحطة الأولى: التحدي الاستهلالي (Engage)
                    </div>
                    <h2 class="text-2xl sm:text-4xl font-black">لغز صلابة المثلث وثبات السبورة حرف A</h2>
                    <p class="text-sm sm:text-base text-orange-100 max-w-3xl">
                        تأمل الأشياء من حولك: الرافعات العملاقة، أبراج الضغط العالي، الجسور المعلقة، وسقالات الإنارة... لماذا تعتمد جميعها على "المثلث" دون غيره من الأشكال؟
                    </p>
                </div>
            </div>

            <!-- The Big Challenge Card -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                <!-- Challenge Text & Prompt -->
                <div class="lg:col-span-7 bg-slate-900 border-2 border-orange-500/40 rounded-3xl p-6 sm:p-8 space-y-5 glow-chall">
                    <div class="flex items-center gap-3">
                        <span class="px-3.5 py-1.5 rounded-xl bg-orange-500/20 text-orange-400 font-black text-sm border border-orange-500/30">
                            🔥 تحدي التفكير السريع (دقيقتان)
                        </span>
                    </div>

                    <h3 class="text-xl sm:text-2xl font-black text-white leading-snug">
                        إذا قمنا بصنع إطار مربع من 4 قطع خشبية، وإطار مثلث من 3 قطع خشبية:
                    </h3>

                    <div class="space-y-3 text-slate-300 text-sm sm:text-base leading-relaxed">
                        <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-start gap-3">
                            <span class="w-7 h-7 rounded-lg bg-orange-500/20 text-orange-400 flex items-center justify-center font-bold text-sm shrink-0">1</span>
                            <span>لو دفعت أحد رؤوس المربع بيدك... ماذا يحدث لشكله؟ <strong>(يتشوه ليصبح متوازي أضلاع!)</strong></span>
                        </div>
                        <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 flex items-start gap-3">
                            <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm shrink-0">2</span>
                            <span>لو دفعت أحد رؤوس المثلث بأقصى قوتك... هل يتغير شكله؟ <strong>(مستحيل! ثابت تماماً!)</strong></span>
                        </div>
                    </div>

                    <div class="p-4 rounded-2xl bg-gradient-to-r from-orange-500/10 to-amber-500/10 border border-orange-500/30 text-orange-200 text-sm">
                        <strong class="text-orange-400 font-bold block mb-1">السؤال الذي يحير المهندسين:</strong>
                        لماذا تكفي معرفة أطوال أضلاع المثلث الثلاثة ($SSS$) لتثبيت زواياه ومنع أي تشوه بالكامل دون الحاجة لأي منقلة؟
                    </div>

                    <!-- Interactive Reveal Button -->
                    <button onclick="toggleAnswer('reveal-engage')" class="w-full py-3.5 px-6 rounded-2xl bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 text-white font-black text-sm sm:text-base shadow-lg shadow-orange-500/30 transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-key"></i>
                        <span>اكشف سر اللغز الهندسي</span>
                    </button>

                    <!-- Hidden Insight Card -->
                    <div id="reveal-engage" class="hidden p-5 rounded-2xl bg-slate-800 border-2 border-emerald-500 text-slate-200 space-y-2 text-sm sm:text-base">
                        <div class="flex items-center gap-2 font-black text-emerald-400">
                            <i class="fa-solid fa-certificate text-lg"></i>
                            <span>السر الرياضي الكامن (مسلمة SSS):</span>
                        </div>
                        <p class="leading-relaxed">
                            الأضلاع الثلاثة في المثلث تقيد حركات الزوايا تماماً! عند تثبيت أطوال الأضلاع الثلاثة لا يمكن تشكيل إلا <strong>مثلث وحيد في الفراغ</strong>. هذا المبدأ هو أساس صمود الجسور المعلقة وهو سر مسلمة التطابق بثلاثة أضلاع $SSS$.
                        </p>
                    </div>
                </div>

                <!-- Visual Board SVG Display -->
                <div class="lg:col-span-5 bg-slate-900 border border-slate-800 rounded-3xl p-6 flex flex-col items-center justify-center text-center space-y-4">
                    <svg class="w-full max-w-[280px] h-64" viewBox="0 0 240 220" fill="none">
                        <!-- Glow Backing -->
                        <circle cx="120" cy="110" r="90" fill="#f97316" fill-opacity="0.05"/>
                        <!-- Ground line -->
                        <line x1="20" y1="195" x2="220" y2="195" stroke="#475569" stroke-width="2" stroke-dasharray="4 4"/>
                        <!-- Left Board Leg -->
                        <line x1="120" y1="35" x2="45" y2="195" stroke="#f97316" stroke-width="5" stroke-linecap="round"/>
                        <!-- Right Board Leg -->
                        <line x1="120" y1="35" x2="195" y2="195" stroke="#f97316" stroke-width="5" stroke-linecap="round"/>
                        <!-- Fixed Cross Brace -->
                        <line x1="75" y1="130" x2="165" y2="130" stroke="#0ea5e9" stroke-width="4.5" stroke-linecap="round"/>
                        <!-- Top Hinge -->
                        <circle cx="120" cy="35" r="6" fill="#f8fafc" stroke="#f97316" stroke-width="2"/>
                        <!-- Labels -->
                        <text x="120" y="24" fill="#f8fafc" font-size="14" font-weight="900" text-anchor="middle">القمة A (Z)</text>
                        <text x="60" y="125" fill="#38bdf8" font-size="12" font-weight="bold">B (X)</text>
                        <text x="180" y="125" fill="#38bdf8" font-size="12" font-weight="bold">C (Y)</text>
                        <!-- Congruent Ticks -->
                        <line x1="93" y1="78" x2="102" y2="85" stroke="#ef4444" stroke-width="2.5"/>
                        <line x1="138" y1="85" x2="147" y2="78" stroke="#ef4444" stroke-width="2.5"/>
                        <line x1="117" y1="125" x2="117" y2="135" stroke="#ef4444" stroke-width="2.5"/>
                        <line x1="123" y1="125" x2="123" y2="135" stroke="#ef4444" stroke-width="2.5"/>
                        <text x="120" y="160" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">الذراع المثبت (Crossbar)</text>
                        <text x="120" y="212" fill="#94a3b8" font-size="11" text-anchor="middle">نموذج السبورة المزدوجة (ص 170)</text>
                    </svg>
                    <div class="text-xs text-slate-400 font-bold">
                        $\triangle ABC \cong \triangle XYZ$ (تطابق الأضلاع الثلاثة يضمن ثباتاً مطلقاً)
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================= -->
        <!-- المحطة 2: EXPLORE - مختبر الاستكشاف الرياضي -->
        <!-- ============================================================= -->
        <section id="tab-explore" class="tab-pane hidden space-y-6">
            <div class="bg-gradient-to-l from-teal-600 via-emerald-600 to-green-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
                <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-emerald-200 mb-2">
                    <i class="fa-solid fa-flask-vial"></i> المحطة الثانية: مختبر الاستكشاف (Explore)
                </div>
                <h2 class="text-2xl sm:text-4xl font-black">مختبر التحقق الذاتي: هل تكفي المعطيات لتوليد مثلث وحيد؟</h2>
                <p class="text-sm sm:text-base text-emerald-100 max-w-3xl">
                    ادخل مع فريقك في تجربة عملية لفحص شروط التطابق واكتشاف أهمية "الزاوية المحصورة".
                </p>
            </div>

            <!-- Two Lab Challenges -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

                <!-- Lab Challenge 1: The SSS Rigidity -->
                <div class="bg-slate-900 border-2 border-teal-500/40 rounded-3xl p-6 space-y-4 glow-emerald flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-3 py-1 rounded-full bg-teal-500/20 text-teal-400 text-xs font-black border border-teal-500/30">
                                🧪 التجربة رقم 1
                            </span>
                            <span class="text-xs text-slate-400 font-bold">أطوال محددة: 6cm, 8cm, 10cm</span>
                        </div>
                        <h3 class="text-lg sm:text-xl font-black text-white">تحدي بناء المثلث الفريد (SSS)</h3>
                        <p class="text-sm text-slate-300 leading-relaxed mt-2">
                            إذا أعطيناك 3 أضلاع بأطوال محددة تماماً، ورسم كل طالب في الفصل مثلثه الخاص... هل يمكن أن يختلف قياس أي زاوية بين رسم وآخر؟
                        </p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-3">
                        <div class="flex items-center justify-between text-xs sm:text-sm font-bold">
                            <span class="text-slate-300">نسبة التطابق بين جميع الرسومات:</span>
                            <span class="text-teal-400 font-mono text-base">100% تطابق تام!</span>
                        </div>
                        <div class="w-full bg-slate-700 h-2.5 rounded-full overflow-hidden">
                            <div class="bg-teal-500 h-full rounded-full w-full"></div>
                        </div>
                        <p class="text-xs text-slate-400">
                            <strong>الاستنتاج العملي:</strong> تطابق الأضلاع الثلاثة في مثلث مع نظائرها في مثلث آخر ($SSS$) يُلغي أي احتمال للاختلاف.
                        </p>
                    </div>

                    <button onclick="toggleAnswer('reveal-exp1')" class="w-full py-2.5 px-4 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-magnifying-glass"></i>
                        <span>عرض قاعدة SSS الرسمية</span>
                    </button>
                    <div id="reveal-exp1" class="hidden p-3.5 bg-slate-800 rounded-xl border border-teal-500/50 text-xs sm:text-sm text-teal-200 font-bold">
                        إذا طابقت أضلاع مثلث الأضلاع المناظرة في مثلث آخر، فإن المثلثين متطابقان حتماً ($\triangle ABC \cong \triangle DEF$).
                    </div>
                </div>

                <!-- Lab Challenge 2: The Included Angle Dilemma -->
                <div class="bg-slate-900 border-2 border-emerald-500/40 rounded-3xl p-6 space-y-4 glow-emerald flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 text-xs font-black border border-emerald-500/30">
                                ⏱️ التجربة رقم 2
                            </span>
                            <span class="text-xs text-slate-400 font-bold">عقارب الساعة ص 172</span>
                        </div>
                        <h3 class="text-lg sm:text-xl font-black text-white">تحدي لغز عقارب الساعة والزاوية المحصورة</h3>
                        <p class="text-sm text-slate-300 leading-relaxed mt-2">
                            طول عقرب الساعات ثابت، وطول عقرب الدقائق ثابت. ما العامل الوحيد الذي يتحكم في المسافة المستقيمة بين طرفي العقربين؟
                        </p>
                    </div>

                    <!-- Visual Clocks SVG -->
                    <div class="bg-slate-800/80 p-3 rounded-2xl border border-slate-700 flex items-center justify-around">
                        <svg class="w-36 h-28" viewBox="0 0 140 110" fill="none">
                            <circle cx="50" cy="55" r="42" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                            <line x1="50" y1="55" x2="50" y2="25" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
                            <line x1="50" y1="55" x2="78" y2="55" stroke="#10b981" stroke-width="3.5" stroke-linecap="round"/>
                            <path d="M 50 38 A 17 17 0 0 1 67 55" stroke="#f43f5e" stroke-width="2.5" fill="none"/>
                            <line x1="50" y1="25" x2="78" y2="55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>
                            <text x="50" y="106" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">الزاوية المحصورة (3:00)</text>
                        </svg>
                        <svg class="w-36 h-28" viewBox="0 0 140 110" fill="none">
                            <circle cx="50" cy="55" r="42" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
                            <line x1="50" y1="55" x2="50" y2="25" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
                            <line x1="50" y1="55" x2="22" y2="55" stroke="#10b981" stroke-width="3.5" stroke-linecap="round"/>
                            <path d="M 33 55 A 17 17 0 0 1 50 38" stroke="#f43f5e" stroke-width="2.5" fill="none"/>
                            <line x1="50" y1="25" x2="22" y2="55" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3 3"/>
                            <text x="50" y="106" font-size="10" font-weight="bold" fill="#34d399" text-anchor="middle">الزاوية المحصورة (9:00)</text>
                        </svg>
                    </div>

                    <button onclick="toggleAnswer('reveal-exp2')" class="w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs sm:text-sm transition flex items-center justify-center gap-2">
                        <i class="fa-solid fa-lightbulb"></i>
                        <span>ماذا تعني "الزاوية المحصورة"؟</span>
                    </button>
                    <div id="reveal-exp2" class="hidden p-3.5 bg-slate-800 rounded-xl border border-emerald-500/50 text-xs sm:text-sm text-emerald-200 font-bold">
                        الزاوية المحصورة هي الزاوية المتكونة من التقاء الضلعين نفسيهما. إذا تساوت الزاوية المحصورة وطولا الضلعين، تتطابق المسافة بين الطرفين حتماً ($SAS$).
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================= -->
        <!-- المحطة 3: EXPLAIN - شفرة البرهان والمسلمات -->
        <!-- ============================================================= -->
        <section id="tab-explain" class="tab-pane hidden space-y-6">
            <div class="bg-gradient-to-l from-blue-600 via-indigo-600 to-violet-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
                <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-blue-200 mb-2">
                    <i class="fa-solid fa-code-compare"></i> المحطة الثالثة: شفرة البرهان (Explain)
                </div>
                <h2 class="text-2xl sm:text-4xl font-black">القواعد الذهبية لكتابة البرهان الهندسي</h2>
                <p class="text-sm sm:text-base text-blue-100 max-w-3xl">
                    تعرف على مسلّمتي الدرس، ومارس خطة البرهان خطوة بخطوة بالمنطق والرموز الصارمة.
                </p>
            </div>

            <!-- Golden Rules Cards (SSS & SAS) -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- SSS Card -->
                <div class="bg-slate-900 border-2 border-blue-500/40 rounded-3xl p-6 space-y-4 glow-blue">
                    <div class="flex items-center justify-between">
                        <span class="px-3 py-1 rounded-lg bg-blue-600 text-white text-xs font-black">مسلمة 3.1 ص 170</span>
                        <span class="text-xs font-mono text-blue-400 font-bold">Side-Side-Side (SSS)</span>
                    </div>
                    <h3 class="text-xl font-black text-white">مسلمة التطابق بثلاثة أضلاع (SSS)</h3>
                    <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 text-slate-300 text-sm leading-relaxed">
                        "إذا تطابقت أضلاع مثلث مع الأضلاع المناظرة لها في مثلث آخر، فإن المثلثين متطابقان."
                    </div>
                    <div class="p-3 rounded-xl bg-blue-950/60 border border-blue-500/30 text-center font-mono text-sm text-blue-300">
                        $\overline{AB} \cong \overline{DE} \quad , \quad \overline{BC} \cong \overline{EF} \quad , \quad \overline{AC} \cong \overline{DF}$<br>
                        $\Downarrow$<br>
                        <strong class="text-white text-base">$\triangle ABC \cong \triangle DEF$</strong>
                    </div>
                </div>

                <!-- SAS Card -->
                <div class="bg-slate-900 border-2 border-indigo-500/40 rounded-3xl p-6 space-y-4 glow-blue">
                    <div class="flex items-center justify-between">
                        <span class="px-3 py-1 rounded-lg bg-indigo-600 text-white text-xs font-black">مسلمة 3.2 ص 172</span>
                        <span class="text-xs font-mono text-indigo-400 font-bold">Side-Angle-Side (SAS)</span>
                    </div>
                    <h3 class="text-xl font-black text-white">مسلمة التطابق بضلعين وزاوية محصورة (SAS)</h3>
                    <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 text-slate-300 text-sm leading-relaxed">
                        "إذا طابق ضلعان وزاوية محصورة بينهما في مثلث نظائرها في مثلث آخر، فإن المثلثين متطابقان."
                    </div>
                    <div class="p-3 rounded-xl bg-indigo-950/60 border border-indigo-500/30 text-center font-mono text-sm text-indigo-300">
                        $\overline{AB} \cong \overline{DE} \quad , \quad \angle B \cong \angle E \quad , \quad \overline{BC} \cong \overline{EF}$<br>
                        $\Downarrow$<br>
                        <strong class="text-white text-base">$\triangle ABC \cong \triangle DEF$</strong>
                    </div>
                </div>
            </div>

            <!-- Interactive Proof Challenge: Flow Proof (Example 1 from Book) -->
            <div class="bg-slate-900 border-2 border-slate-700 rounded-3xl p-6 sm:p-8 space-y-5">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                    <div>
                        <span class="text-xs font-bold text-orange-400 uppercase tracking-wider">تحدي كتابة البرهان الصفي</span>
                        <h3 class="text-lg sm:text-xl font-black text-white">المهمة 1: إثبات تطابق المثلثين بالبرهان التسلسلي (مثال 1 ص 170)</h3>
                    </div>
                    <span class="px-3 py-1 rounded-full bg-slate-800 text-slate-300 text-xs font-bold border border-slate-700">برهان تسلسلي (Flow Proof)</span>
                </div>

                <div class="bg-slate-800/60 p-4 rounded-2xl border border-slate-700 text-sm space-y-2">
                    <p><strong>المعطيات:</strong> $\overline{GH} \cong \overline{KJ}$ ، $\overline{HL} \cong \overline{JL}$ ، والنقطة $L$ هي منتصف القطعة $\overline{GK}$.</p>
                    <p><strong>المطلوب:</strong> إثبات أن $\triangle GHL \cong \triangle KJL$.</p>
                </div>

                <!-- Interactive Flow Chart on Whiteboard -->
                <div class="overflow-x-auto p-4 bg-slate-950 rounded-2xl border border-slate-800">
                    <div class="min-w-[500px] flex items-center justify-between gap-3 text-center">
                        <!-- Box 1 -->
                        <div class="flex-1 bg-slate-900 p-3 rounded-xl border border-slate-700 shadow-md">
                            <span class="text-xs text-slate-400 block mb-1">الضلع الأول</span>
                            <div class="text-sm font-black text-blue-400 font-mono">$\overline{GH} \cong \overline{KJ}$</div>
                            <span class="text-[11px] text-slate-500 mt-1 block">معطى</span>
                        </div>

                        <span class="text-slate-600 font-bold text-lg">➔</span>

                        <!-- Box 2 Midpoint -->
                        <div class="flex-1 space-y-2">
                            <div class="bg-slate-900 p-2 rounded-xl border border-slate-700">
                                <span class="text-[11px] text-slate-400 block">$L$ منتصف $\overline{GK}$ (معطى)</span>
                            </div>
                            <div class="text-slate-500 text-xs">▼</div>
                            <div class="bg-slate-800 p-2.5 rounded-xl border-2 border-orange-500/60">
                                <span class="text-xs text-orange-400 font-bold block mb-0.5">الضلع الثاني</span>
                                <div class="text-sm font-black text-white font-mono">$\overline{GL} \cong \overline{KL}$</div>
                                <span class="text-[10px] text-orange-300">تعريف نقطة المنتصف</span>
                            </div>
                        </div>

                        <span class="text-slate-600 font-bold text-lg">➔</span>

                        <!-- Box 3 -->
                        <div class="flex-1 bg-slate-900 p-3 rounded-xl border border-slate-700 shadow-md">
                            <span class="text-xs text-slate-400 block mb-1">الضلع الثالث</span>
                            <div class="text-sm font-black text-blue-400 font-mono">$\overline{HL} \cong \overline{JL}$</div>
                            <span class="text-[11px] text-slate-500 mt-1 block">معطى</span>
                        </div>

                        <span class="text-orange-500 font-bold text-xl">➔</span>

                        <!-- Final Box -->
                        <div class="flex-1 bg-gradient-to-tr from-orange-500 to-amber-600 p-4 rounded-2xl text-white shadow-xl">
                            <span class="text-xs text-orange-100 font-bold block mb-1">الاستنتاج النهائي</span>
                            <div class="text-sm sm:text-base font-black font-mono">$\triangle GHL \cong \triangle KJL$</div>
                            <span class="text-[11px] font-black text-white/90 border-t border-white/20 mt-1.5 pt-1 block">مسلمة SSS</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================= -->
        <!-- المحطة 4: ENGINEER - التحدي الهندسي والتطبيق الإنشائي -->
        <!-- ============================================================= -->
        <section id="tab-engineer" class="tab-pane hidden space-y-6">
            <div class="bg-gradient-to-l from-amber-600 via-orange-600 to-red-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
                <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-amber-200 mb-2">
                    <i class="fa-solid fa-helmet-safety"></i> المحطة الرابعة: التحدي الهندسي (Engineer)
                </div>
                <h2 class="text-2xl sm:text-4xl font-black">هندسة الواقع: متانة السقالات وعظمة الجسور المعلقة</h2>
                <p class="text-sm sm:text-base text-amber-100 max-w-3xl">
                    تطبيق مباشر على البرهان ذي العمودين في مشاريع رؤية 2030 وتجهيزات الإنتاج العالمية.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                <!-- Two Column Proof Scaffold Display -->
                <div class="lg:col-span-8 bg-slate-900 border-2 border-orange-500/40 rounded-3xl p-6 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <h3 class="text-lg font-black text-white">تحدي برهان دعامات السقالة حاملة المصابيح (مثال 3 ص 173)</h3>
                        <span class="px-3 py-1 rounded-full bg-orange-500/20 text-orange-400 text-xs font-bold">برهان ذو عمودين</span>
                    </div>

                    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                        <strong>المعطيات:</strong> $\overline{WX} \cong \overline{ZY}$ ، $\overline{WX} \parallel \overline{ZY}$.<br>
                        <strong>المطلوب:</strong> إثبات أن $\triangle WXZ \cong \triangle YZX$.
                    </p>

                    <!-- Interactive Table -->
                    <div class="overflow-x-auto rounded-2xl border border-slate-800">
                        <table class="w-full text-right text-xs sm:text-sm">
                            <thead class="bg-slate-800 text-slate-300 font-bold">
                                <tr>
                                    <th class="p-3 w-12 text-center text-orange-400">#</th>
                                    <th class="p-3 w-1/2">العبارات (Statements)</th>
                                    <th class="p-3 w-1/2">المبررات (Reasons)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 bg-slate-950 font-mono text-slate-200">
                                <tr>
                                    <td class="p-3 text-center text-slate-500 font-sans">1</td>
                                    <td class="p-3">$\overline{WX} \cong \overline{ZY}$</td>
                                    <td class="p-3 text-slate-400 font-sans">معطى</td>
                                </tr>
                                <tr>
                                    <td class="p-3 text-center text-slate-500 font-sans">2</td>
                                    <td class="p-3">$\overline{WX} \parallel \overline{ZY}$</td>
                                    <td class="p-3 text-slate-400 font-sans">معطى</td>
                                </tr>
                                <tr class="bg-orange-500/5">
                                    <td class="p-3 text-center text-orange-400 font-sans">3</td>
                                    <td class="p-3 text-orange-400 font-bold">$\angle WXZ \cong \angle XZY$</td>
                                    <td class="p-3 text-slate-300 font-sans">نظرية الزوايا الداخلية المتبادلة</td>
                                </tr>
                                <tr class="bg-blue-500/5">
                                    <td class="p-3 text-center text-blue-400 font-sans">4</td>
                                    <td class="p-3 text-blue-400 font-bold">$\overline{XZ} \cong \overline{ZX}$</td>
                                    <td class="p-3 text-slate-300 font-sans">خاصية الانعكاس للتطابق (ضلع مشترك)</td>
                                </tr>
                                <tr class="bg-gradient-to-r from-orange-500/20 to-amber-500/20">
                                    <td class="p-3 text-center text-emerald-400 font-black font-sans">5</td>
                                    <td class="p-3 text-emerald-400 font-black">$\triangle WXZ \cong \triangle YZX$</td>
                                    <td class="p-3 text-emerald-300 font-black font-sans">مسلمة التطابق بضلعين وزاوية محصورة (SAS)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Riyadh Suspension Bridge Challenge (Exercise 7, p. 175) -->
                <div class="lg:col-span-4 bg-slate-900 border border-slate-800 rounded-3xl p-6 space-y-4 text-center">
                    <div class="w-12 h-12 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl mx-auto">
                        <i class="fa-solid fa-bridge"></i>
                    </div>
                    <h4 class="text-base font-black text-white">تحدي جسر الرياض المعلق (ص 175)</h4>
                    <p class="text-xs text-slate-300 leading-relaxed text-justify">
                        طول الجسر $763\text{ m}$ مثبت بكابلات تلتقي عند منتصف المسافة بين الدعامتين الخرسانيتين في النقطة $C$.
                    </p>
                    <div class="p-3 bg-slate-800 rounded-xl text-xs text-amber-300 border border-amber-500/30 text-right space-y-1">
                        <div>• المعطيات: $AB = ED$ ، $C$ منتصف $BD$.</div>
                        <div>• الزاوية: قائمتان عند طرفي البرجين.</div>
                        <div class="font-bold text-white pt-1">النتيجة: المثلثان متطابقان بحسب مسلمة SAS.</div>
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================= -->
        <!-- المحطة 5: ELABORATE - تحدي الفرسان والتفكير الناقد -->
        <!-- ============================================================= -->
        <section id="tab-elaborate" class="tab-pane hidden space-y-6">
            <div class="bg-gradient-to-l from-purple-600 via-fuchsia-600 to-pink-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
                <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-purple-200 mb-2">
                    <i class="fa-solid fa-chess"></i> المحطة الخامسة: تحدي الفرسان (Elaborate)
                </div>
                <h2 class="text-2xl sm:text-4xl font-black">ميدان محاكمة الأخطاء وتحديات الهندسة الإحداثية</h2>
                <p class="text-sm sm:text-base text-purple-100 max-w-3xl">
                    هل تستطيع كشف الفخاخ الرياضية وإثبات التطابق في المستوى الديكارتي؟
                </p>
            </div>

            <!-- Error Hunt Debate Card (Question 24, p. 177) -->
            <div class="bg-slate-900 border-2 border-rose-500/40 rounded-3xl p-6 sm:p-8 space-y-5 glow-chall">
                <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-8 h-8 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold">
                            <i class="fa-solid fa-triangle-exclamation"></i>
                        </span>
                        <h3 class="text-lg sm:text-xl font-black text-white">تحدي اكتشف الخطأ: مناظرة أحمد ضد خالد (ص 177)</h3>
                    </div>
                    <span class="px-3 py-1 rounded-full bg-rose-500/20 text-rose-400 text-xs font-bold border border-rose-500/30">عمق معرفي DOK 4</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2">
                        <div class="font-bold text-amber-400 flex items-center gap-2">
                            <i class="fa-solid fa-user"></i> ادعاء أحمد:
                        </div>
                        <p class="text-slate-300">
                            "المثلثان $\triangle PRQ \cong \triangle XYZ$ متطابقان بحسب مسلمة SAS؛ لأن لدينا ضلعين متطابقين وزاوية متطابقة!"
                        </p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2">
                        <div class="font-bold text-emerald-400 flex items-center gap-2">
                            <i class="fa-solid fa-user-shield"></i> اعتراض خالد:
                        </div>
                        <p class="text-slate-300">
                            "كلا يا أحمد! لا توجد معلومات كافية لإثبات التطابق؛ إجابتك غير صحيحة!"
                        </p>
                    </div>
                </div>

                <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 text-center">
                    <span class="text-xs text-slate-400 block mb-2">من المحق منهما ولماذا؟</span>
                    <button onclick="toggleAnswer('reveal-debate')" class="py-2.5 px-6 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs sm:text-sm transition inline-flex items-center gap-2">
                        <i class="fa-solid fa-gavel"></i>
                        <span>حكم المحكمة الرياضية</span>
                    </button>
                    <div id="reveal-debate" class="hidden mt-3 p-4 bg-slate-800 text-slate-200 text-xs sm:text-sm rounded-xl border border-rose-500 text-right space-y-2">
                        <strong class="text-emerald-400 text-sm block">الحكم: خالد هو المحق بنسبة 100%!</strong>
                        <p>
                            الزاوية المعطاة في الشكل <strong>ليست محصورة</strong> بين الضلعين المتطابقين. هذه الحالة تُسمى حالة <strong>(SSA)</strong>، وتطابق ضلعين وزاوية غير محصورة لا يضمن تطابق المثلثين لأن الضلع الحر يمكن أن يتأرجح منتجاً مثلثين مختلفين تماماً!
                        </p>
                    </div>
                </div>
            </div>

            <!-- Coordinate Challenge (Check 2, p. 171) -->
            <div class="bg-slate-900 border-2 border-purple-500/40 rounded-3xl p-6 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <h3 class="text-base sm:text-lg font-black text-white">تحدي الهندسة الإحداثية بقانون المسافة: $d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$</h3>
                    <span class="text-xs text-purple-400 font-bold">ص 171 تحقق 2</span>
                </div>
                <p class="text-xs sm:text-sm text-slate-300">
                    هل المثلث $\triangle JKL$ ذو الرؤوس $J(2, 5), K(1, 1), L(5, 2)$ يطابق المثلث $\triangle NPQ$ ذو الرؤوس $N(-3, 0), P(-7, 1), Q(-4, 4)$؟
                </p>
                <button onclick="toggleAnswer('reveal-coord-chall')" class="py-2 px-4 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs transition flex items-center gap-2">
                    <i class="fa-solid fa-calculator"></i>
                    <span>اكشف حسابات المسافة</span>
                </button>
                <div id="reveal-coord-chall" class="hidden p-4 rounded-2xl bg-slate-950 font-mono text-xs sm:text-sm space-y-2 text-slate-200 border border-purple-500/40">
                    <div class="text-emerald-400 font-bold font-sans">حسابات الأضلاع المتناظرة:</div>
                    <div>• $JK = \sqrt{(1-2)^2 + (1-5)^2} = \sqrt{1+16} = \mathbf{\sqrt{17}} = NP$</div>
                    <div>• $KL = \sqrt{(5-1)^2 + (2-1)^2} = \sqrt{16+1} = \mathbf{\sqrt{17}} = NQ$</div>
                    <div>• $JL = \sqrt{(5-2)^2 + (2-5)^2} = \sqrt{9+9} = \mathbf{\sqrt{18}} = 3\sqrt{2} = PQ$</div>
                    <div class="text-purple-300 font-bold font-sans pt-1 border-t border-slate-800">
                        النتيجة: جميع الأضلاع المتناظرة متطابقة، إذن $\triangle JKL \cong \triangle NPQ$ بموجب (SSS).
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================= -->
        <!-- المحطة 6: EVALUATE - تذكرة النصر والتقييم الختامي -->
        <!-- ============================================================= -->
        <section id="tab-evaluate" class="tab-pane hidden space-y-6">
            <div class="bg-gradient-to-l from-rose-600 via-pink-600 to-red-600 rounded-3xl p-6 sm:p-8 shadow-xl text-white">
                <div class="inline-flex items-center gap-2 bg-black/20 backdrop-blur px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider text-rose-200 mb-2">
                    <i class="fa-solid fa-trophy"></i> المحطة السادسة: تذكرة النصر (Evaluate)
                </div>
                <h2 class="text-2xl sm:text-4xl font-black">تذكرة الخروج: هل أنت مستعد لاختبار القدرات والمعايير؟</h2>
                <p class="text-sm sm:text-base text-rose-100 max-w-3xl">
                    أجب عن سؤال الاختبار المعياري المباشر من كتابك لتتأهل لوسام إتقان تطابق المثلثات.
                </p>
            </div>

            <!-- Big Exit Ticket Card -->
            <div class="bg-slate-900 border-2 border-rose-500 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="px-3.5 py-1 rounded-full bg-rose-500 text-white text-xs font-black">
                            سؤال 26 ص 177
                        </span>
                        <h3 class="text-lg sm:text-xl font-black text-white">تدريب على اختبار معياري</h3>
                    </div>
                    <span class="text-xs text-rose-400 font-bold">تحديد المعلومة الناقصة لـ SAS</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                    <div class="lg:col-span-8 space-y-4">
                        <p class="text-base sm:text-lg font-bold text-slate-100 leading-relaxed">
                            في الشكلين أدناه، إذا كان $\overline{AC} \cong \overline{XZ}$ و $\angle C \cong \angle Z$.<br>
                            ما المعلومة الإضافية التي يمكن استعمالها لإثبات أن $\triangle ABC \cong \triangle XYZ$ بمسلمة $SAS$؟
                        </p>

                        <!-- Options -->
                        <div class="space-y-2.5 pt-2" id="exit-ticket-board-options">
                            <label class="flex items-center gap-3 p-3.5 rounded-2xl border border-slate-700 bg-slate-800/80 hover:bg-slate-800 cursor-pointer transition">
                                <input type="radio" name="board_opt" value="A" class="w-5 h-5 text-rose-500 focus:ring-rose-500">
                                <span class="text-sm sm:text-base font-black text-slate-200 font-mono">(A) $\overline{BC} \cong \overline{YZ}$</span>
                            </label>
                            <label class="flex items-center gap-3 p-3.5 rounded-2xl border border-slate-700 bg-slate-800/80 hover:bg-slate-800 cursor-pointer transition">
                                <input type="radio" name="board_opt" value="B" class="w-5 h-5 text-rose-500 focus:ring-rose-500">
                                <span class="text-sm sm:text-base font-black text-slate-200 font-mono">(B) $\overline{AB} \cong \overline{XY}$</span>
                            </label>
                            <label class="flex items-center gap-3 p-3.5 rounded-2xl border border-slate-700 bg-slate-800/80 hover:bg-slate-800 cursor-pointer transition">
                                <input type="radio" name="board_opt" value="C" class="w-5 h-5 text-rose-500 focus:ring-rose-500">
                                <span class="text-sm sm:text-base font-black text-slate-200 font-mono">(C) $\overline{BC} \cong \overline{XZ}$</span>
                            </label>
                            <label class="flex items-center gap-3 p-3.5 rounded-2xl border border-slate-700 bg-slate-800/80 hover:bg-slate-800 cursor-pointer transition">
                                <input type="radio" name="board_opt" value="D" class="w-5 h-5 text-rose-500 focus:ring-rose-500">
                                <span class="text-sm sm:text-base font-black text-slate-200 font-mono">(D) $\overline{XZ} \cong \overline{XY}$</span>
                            </label>
                        </div>

                        <!-- Check Action -->
                        <button onclick="checkBoardExit()" class="px-6 py-3 rounded-2xl bg-gradient-to-r from-rose-600 to-pink-600 hover:from-rose-700 hover:to-pink-700 text-white font-black text-sm sm:text-base shadow-lg transition flex items-center gap-2">
                            <i class="fa-solid fa-paper-plane"></i>
                            <span>تسجيل الإجابة والتصحيح المباشر</span>
                        </button>

                        <!-- Live Feedback -->
                        <div id="board-exit-feedback" class="hidden p-4 rounded-2xl text-sm leading-relaxed"></div>
                    </div>

                    <!-- Visual Question 26 SVG -->
                    <div class="lg:col-span-4 bg-slate-950 p-4 rounded-3xl border border-slate-800 flex flex-col items-center justify-center">
                        <svg class="w-full max-w-[240px] h-40" viewBox="0 0 240 140" fill="none">
                            <!-- Triangle 1 (ABC) -->
                            <polygon points="25,120 90,120 55,30" fill="#1e1b4b" stroke="#6366f1" stroke-width="2.5"/>
                            <text x="15" y="125" font-size="12" font-weight="900" fill="#f8fafc">B</text>
                            <text x="96" y="125" font-size="12" font-weight="900" fill="#f8fafc">C</text>
                            <text x="55" y="20" font-size="12" font-weight="900" fill="#f8fafc">A</text>
                            <!-- Angle C arc -->
                            <path d="M 78 120 A 14 14 0 0 1 83 107" stroke="#10b981" stroke-width="3" fill="none"/>
                            <!-- AC tick -->
                            <line x1="68" y1="70" x2="77" y2="77" stroke="#ef4444" stroke-width="2.5"/>

                            <!-- Triangle 2 (XYZ) -->
                            <polygon points="145,120 210,120 175,30" fill="#1e1b4b" stroke="#6366f1" stroke-width="2.5"/>
                            <text x="135" y="125" font-size="12" font-weight="900" fill="#f8fafc">Y</text>
                            <text x="216" y="125" font-size="12" font-weight="900" fill="#f8fafc">Z</text>
                            <text x="175" y="20" font-size="12" font-weight="900" fill="#f8fafc">X</text>
                            <!-- Angle Z arc -->
                            <path d="M 198 120 A 14 14 0 0 1 203 107" stroke="#10b981" stroke-width="3" fill="none"/>
                            <!-- XZ tick -->
                            <line x1="188" y1="70" x2="197" y2="77" stroke="#ef4444" stroke-width="2.5"/>
                        </svg>
                        <span class="text-xs text-slate-400 font-bold mt-2">المعطى: $\overline{AC} \cong \overline{XZ}$ و $\angle C \cong \angle Z$</span>
                    </div>
                </div>
            </div>

            <!-- Decision Tree Summary on Board -->
            <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 text-center space-y-4">
                <h4 class="text-base font-black text-white flex items-center justify-center gap-2">
                    <i class="fa-solid fa-route text-orange-400"></i>
                    <span>شجرة القرار السريعة: كيف تحدد مسار إثباتك في 5 ثوانٍ؟</span>
                </h4>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
                    <div class="p-4 rounded-2xl bg-slate-800 border border-blue-500/40 text-blue-200">
                        <strong class="text-white block text-sm mb-1">هل كل المعطيات أضلاع فقط (3 أضلاع)؟</strong>
                        استخدم فوراً مسلمة <strong class="text-orange-400 text-base">SSS</strong> (ابحث عن ضلع مشترك أو منتصف قطعة).
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-800 border border-emerald-500/40 text-emerald-200">
                        <strong class="text-white block text-sm mb-1">هل لديك ضلعان وزاوية؟</strong>
                        تأكد أن الزاوية <strong>محصورة</strong> بينهما ➔ استخدم <strong class="text-emerald-400 text-base">SAS</strong>! لو لم تكن محصورة ➔ توقف (المعلومات غير كافية).
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Interactive Scripts for Whiteboard Operations -->
    <script>
        // 6Es Navigation Tab Switcher
        function showTab(tabId) {
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.add('hidden'));
            const target = document.getElementById(tabId);
            if (target) target.classList.remove('hidden');

            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('active');
                btn.classList.add('text-slate-400');
            });

            const activeBtn = document.getElementById('btn-' + tabId.replace('tab-', ''));
            if (activeBtn) {
                activeBtn.classList.add('active');
                activeBtn.classList.remove('text-slate-400');
            }

            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        }

        // Toggle Specific Answer or Hidden Challenge
        function toggleAnswer(id) {
            const el = document.getElementById(id);
            if (!el) return;
            el.classList.toggle('hidden');
            if (window.MathJax && !el.classList.contains('hidden')) {
                MathJax.typesetPromise([el]);
            }
        }

        // Interactive Live Timer Widget
        let timerSeconds = 0;
        let timerInterval = null;
        let timerRunning = false;

        function updateTimerDisplay() {
            const mins = Math.floor(timerSeconds / 60);
            const secs = timerSeconds % 60;
            const formatted = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            const display = document.getElementById('timer-display');
            if (display) display.innerText = formatted;
        }

        function toggleTimer() {
            const btn = document.getElementById('timer-btn');
            if (!timerRunning) {
                timerRunning = true;
                timerInterval = setInterval(() => {
                    timerSeconds++;
                    updateTimerDisplay();
                }, 1000);
                if (btn) btn.innerHTML = '<i class="fa-solid fa-pause"></i>';
            } else {
                timerRunning = false;
                clearInterval(timerInterval);
                if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
            }
        }

        function resetTimer() {
            timerRunning = false;
            clearInterval(timerInterval);
            timerSeconds = 0;
            updateTimerDisplay();
            const btn = document.getElementById('timer-btn');
            if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
        }

        // Fullscreen Toggle
        function toggleFullScreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(() => {});
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen().catch(() => {});
                }
            }
        }

        // Board Exit Ticket Validation
        function checkBoardExit() {
            const selected = document.querySelector('input[name="board_opt"]:checked');
            const feedback = document.getElementById('board-exit-feedback');
            if (!feedback) return;

            if (!selected) {
                feedback.className = 'p-4 rounded-2xl bg-amber-950/80 border border-amber-500 text-amber-200 block font-bold text-center';
                feedback.innerHTML = '<i class="fa-solid fa-hand text-lg ml-1"></i> اختر أحد البدائل الأربعة أولاً على السبورة!';
                return;
            }

            feedback.classList.remove('hidden');

            if (selected.value === 'A') {
                feedback.className = 'p-5 rounded-2xl bg-emerald-950/90 border-2 border-emerald-400 text-emerald-100 block space-y-2';
                feedback.innerHTML = `
                    <div class="font-black text-emerald-300 text-base flex items-center gap-2">
                        <i class="fa-solid fa-circle-check text-xl"></i>
                        <span>إجابة عبقرية وصحيحة! (A) $\\overline{BC} \\cong \\overline{YZ}$</span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300">
                        <strong>التبرير الرياضي:</strong> الزاوية $\\angle C$ محصورة تماماً بين الضلعين $\\overline{AC}$ و $\\overline{BC}$. والزاوية $\\angle Z$ محصورة بين $\\overline{XZ}$ و $\\overline{YZ}$. بتطابق الضلع $\\overline{BC} \\cong \\overline{YZ}$ يكتمل شرط ضلعين والزاوية المحصورة بينهما ($SAS$).
                    </p>
                `;
            } else {
                feedback.className = 'p-5 rounded-2xl bg-rose-950/90 border-2 border-rose-400 text-rose-100 block space-y-2';
                feedback.innerHTML = `
                    <div class="font-black text-rose-300 text-base flex items-center gap-2">
                        <i class="fa-solid fa-circle-xmark text-xl"></i>
                        <span>إجابة خاطئة! فكر في موقع الزاوية المحصورة</span>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-300">
                        <strong>تنبيه:</strong> إذا اخترت ضلعاً آخر فستصبح الزاوية غير محصورة (حالة $SSA$ الخاطئة). البديل الصحيح الذي يجعل $\\angle C$ محصورة هو <strong>(A) $\\overline{BC} \\cong \\overline{YZ}$</strong>.
                    </p>
                `;
            }

            if (window.MathJax) {
                MathJax.typesetPromise([feedback]);
            }
        }
    </script>
</body>
</html>
'''

output_path = r'c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\عرض_السبورة_تطابق_المثلثات_SSS_SAS_6Es.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully generated student whiteboard HTML at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
