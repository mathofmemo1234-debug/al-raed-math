# -*- coding: utf-8 -*-
"""
Generator for the Comprehensive 5Es Student Worksheet:
ورقة عمل الاستقصاء الخماسي (5Es): إثبات تطابق المثلثات (SSS, SAS)
Based on: اثبات تطابق المثلثات SSS, SAS.pdf (كتاب الرياضيات 1-2 أول ثانوي مسارات ص 170-177)
"""

import os

WORKSHEET_HTML = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ورقة عمل استقصائية (5Es): إثبات تطابق المثلثات (SSS, SAS)</title>
    <!-- Fonts: Cairo -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <!-- FontAwesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: { cairo: ['Cairo', 'sans-serif'] },
                    colors: {
                        brand: { 50: '#eff6ff', 100: '#dbeafe', 500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8' }
                    }
                }
            }
        }
    </script>
    <!-- MathJax -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']]
            },
            svg: { fontCache: 'global' }
        };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
    <style>
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #f8fafc;
            color: #0f172a;
        }
        .write-line {
            border-bottom: 1.5px dotted #94a3b8;
            height: 1.75rem;
            display: inline-block;
            width: 100%;
        }
        .box-fill {
            border: 1.5px dashed #94a3b8;
            background-color: #ffffff;
            border-radius: 0.5rem;
            min-height: 2.2rem;
        }
        @media print {
            body {
                background: white !important;
                color: black !important;
                font-size: 10pt;
            }
            .no-print { display: none !important; }
            .page-break { page-break-before: always; }
            .worksheet-card {
                box-shadow: none !important;
                border: 1px solid #94a3b8 !important;
                break-inside: avoid;
            }
            .print-tight { padding: 0.5rem !important; margin-bottom: 0.5rem !important; }
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-blue-600 selection:text-white min-h-screen py-6 px-3 sm:px-6">

    <!-- Action Bar (Digital toolbar, hidden on print) -->
    <div class="max-w-5xl mx-auto mb-6 flex flex-wrap items-center justify-between gap-3 bg-white p-4 rounded-2xl border border-slate-200 shadow-sm no-print">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-lg">
                <i class="fa-solid fa-file-pen"></i>
            </div>
            <div>
                <h1 class="text-base sm:text-lg font-black text-slate-900">ورقة عمل استقصائية وفق نموذج (5Es)</h1>
                <p class="text-xs text-slate-500">إثبات تطابق المثلثات (SSS, SAS) — الرياضيات 1-2 مسارات (ص 170 – 177)</p>
            </div>
        </div>

        <div class="flex items-center gap-2">
            <button onclick="toggleAnswerKey()" class="px-3.5 py-2 rounded-xl border border-amber-300 bg-amber-50 hover:bg-amber-100 text-xs font-black text-amber-900 transition flex items-center gap-1.5">
                <i class="fa-solid fa-key text-amber-600"></i>
                <span id="key-btn-txt">إظهار مفتاح الحل النموذجي</span>
            </button>
            <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-black shadow transition flex items-center gap-1.5">
                <i class="fa-solid fa-print"></i>
                <span>طباعة الورقة (A4)</span>
            </button>
        </div>
    </div>

    <!-- Main Printable Worksheet Sheet Container -->
    <div class="max-w-5xl mx-auto bg-white border-2 border-slate-300 rounded-3xl p-6 sm:p-8 shadow-md space-y-6">

        <!-- Header: Official School & Student Meta Data -->
        <header class="border-b-2 border-slate-800 pb-4">
            <div class="flex justify-between items-center text-xs sm:text-sm font-bold text-slate-700 border-b border-slate-200 pb-3 mb-3">
                <div class="text-right space-y-0.5">
                    <div>المملكة العربية السعودية</div>
                    <div>وزارة التعليم</div>
                    <div>الإدارة العامة للتعليم</div>
                    <div>المرحلة الثانوية — مسارات</div>
                </div>

                <div class="text-center space-y-1">
                    <div class="inline-block px-4 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-900 font-black text-sm sm:text-base">
                        ورقة عمل الاستقصاء الخماسي (5Es)
                    </div>
                    <div class="text-xs text-slate-600 font-bold">مادة الرياضيات 1-2 | الفصل 3: المثلثات المتطابقة (الدرس 3-4)</div>
                </div>

                <div class="text-left space-y-0.5">
                    <div>الصف: الأول الثانوي</div>
                    <div>الدرجة الكلية: / 15</div>
                    <div>زمن النشاط: حصة دراسية</div>
                </div>
            </div>

            <!-- Student Fillable Meta Box -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 p-3 rounded-xl border border-slate-200 text-xs sm:text-sm font-bold">
                <div><span class="text-slate-500">اسم الطالب:</span> <span class="write-line w-28"></span></div>
                <div><span class="text-slate-500">الفصل:</span> <span class="write-line w-20"></span></div>
                <div><span class="text-slate-500">المجموعة:</span> <span class="write-line w-20"></span></div>
                <div><span class="text-slate-500">التاريخ:</span> <span class="write-line w-24"></span></div>
            </div>
        </header>


        <!-- ============================================================== -->
        <!-- المحطة 1: التهيئة والاستثارة (ENGAGE) - [درجتان] -->
        <!-- ============================================================== -->
        <section class="worksheet-card p-5 rounded-2xl border border-amber-300 bg-amber-50/20 space-y-3">
            <div class="flex items-center justify-between border-b border-amber-200 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-amber-500 text-white font-black text-xs flex items-center justify-center">1</span>
                    <h2 class="text-sm sm:text-base font-black text-amber-950">المحطة الأولى: التهيئة والاستثارة (Engage) — لغز ثبات الهياكل الهندسية</h2>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800 text-xs font-black">2 درجات</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center">
                <div class="sm:col-span-8 text-xs sm:text-sm text-slate-800 space-y-2">
                    <p class="leading-relaxed">
                        <strong>سياق المسألة (كتاب الطالب ص 170):</strong> تُعد السبورة المزدوجة على شكل الحرف A ثابتة تماماً عند تثبيت الذراعين الجانبيين $\overline{BC}$ على أبعاد متساوية من القمة، لتشكل مثلثين متطابقين هما $\triangle ABC, \triangle XYZ$.
                    </p>
                    <p class="font-bold text-amber-900">
                        س 1: إذا قمنا بدفع رأس إطار خشبي رباعي (مربع)، يتشوه شكله وتتغير زواياه، بينما يستحيل تشويه المثلث؛ فسّر رياضياً لماذا تكفي أطوال الأضلاع الثلاثة لتثبيت المثلث تماماً؟
                    </p>
                    <div class="space-y-1.5 pt-1">
                        <div class="write-line"></div>
                        <div class="write-line"></div>
                    </div>

                    <!-- Hidden Solution -->
                    <div class="ans-key hidden p-2.5 bg-emerald-50 border border-emerald-300 rounded-lg text-emerald-900 font-bold text-xs mt-2">
                        <strong>الإجابة النموذجية:</strong> لأن المثلث شكل هندسي صلب (Rigid)؛ فتثبيت أطوال أضلاعه الثلاثة يقيد قياسات زواياه بالكامل ويولد مثلثاً وحيداً غير قابل للحركة، وهو جوهر مسلمة التطابق بثلاثة أضلاع ($SSS$).
                    </div>
                </div>

                <!-- SVG A-Frame Illustration -->
                <div class="sm:col-span-4 bg-white p-2.5 rounded-xl border border-amber-200 flex flex-col items-center justify-center">
                    <svg class="w-40 h-28" viewBox="0 0 200 140" fill="none">
                        <line x1="20" y1="130" x2="180" y2="130" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3 3"/>
                        <line x1="100" y1="15" x2="40" y2="130" stroke="#ea580c" stroke-width="3.5" stroke-linecap="round"/>
                        <line x1="100" y1="15" x2="160" y2="130" stroke="#ea580c" stroke-width="3.5" stroke-linecap="round"/>
                        <line x1="63" y1="85" x2="137" y2="85" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
                        <circle cx="100" cy="15" r="4" fill="#0f172a"/>
                        <text x="100" y="10" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">A (Z)</text>
                        <text x="50" y="90" font-size="9" font-weight="bold" fill="#0284c7">B (X)</text>
                        <text x="150" y="90" font-size="9" font-weight="bold" fill="#0284c7">C (Y)</text>
                        <text x="100" y="105" font-size="8" font-weight="bold" fill="#0369a1" text-anchor="middle">الذراع الثابت BC</text>
                    </svg>
                    <span class="text-[10px] text-slate-500 font-bold">السبورة المزدوجة شكل A (ص 170)</span>
                </div>
            </div>
        </section>


        <!-- ============================================================== -->
        <!-- المحطة 2: الاستكشاف والملاحظة (EXPLORE) - [درجتان] -->
        <!-- ============================================================== -->
        <section class="worksheet-card p-5 rounded-2xl border border-teal-300 bg-teal-50/20 space-y-3">
            <div class="flex items-center justify-between border-b border-teal-200 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-teal-600 text-white font-black text-xs flex items-center justify-center">2</span>
                    <h2 class="text-sm sm:text-base font-black text-teal-950">المحطة الثانية: الاستكشاف والتجريب (Explore) — مفهوم الزاوية المحصورة</h2>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-teal-100 text-teal-800 text-xs font-black">2 درجات</span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center">
                <div class="sm:col-span-8 text-xs sm:text-sm text-slate-800 space-y-2">
                    <p class="leading-relaxed">
                        <strong>استكشاف عقارب الساعة (كتاب الطالب ص 172):</strong> كلما دار عقربا الساعة وشكلا زاوية لها القياس نفسه، فإن المسافة المستقيمة بين طرفي العقربين تكون متساوية تماماً.
                    </p>
                    <p class="font-bold text-teal-950">
                        س 2: أ) عرّف "الزاوية المحصورة" (Included Angle) بأسلوبك الرياضي:
                    </p>
                    <div class="write-line"></div>

                    <p class="font-bold text-teal-950 pt-1">
                        ب) في $\triangle DEF$، ما هي الزاوية المحصورة بين الضلعين $\overline{DE}$ و $\overline{EF}$؟
                    </p>
                    <div class="flex gap-4 items-center">
                        <span class="text-slate-600">الزاوية المحصورة هي:</span>
                        <div class="box-fill w-32 flex items-center justify-center font-bold font-mono text-teal-900">
                            <span class="ans-key hidden text-emerald-700">$\angle E$</span>
                        </div>
                    </div>

                    <!-- Hidden Solution -->
                    <div class="ans-key hidden p-2 bg-emerald-50 border border-emerald-300 rounded-lg text-emerald-900 font-bold text-xs mt-2">
                        <strong>الإجابة النموذجية:</strong> الزاوية المحصورة هي الزاوية المتكونة من التقاء ضلعين متجاورين في المضلع (ورأسها هو الحرف المشترك بين الضلعين وهو $E$).
                    </div>
                </div>

                <!-- SVG Clocks -->
                <div class="sm:col-span-4 bg-white p-2.5 rounded-xl border border-teal-200 flex flex-col items-center justify-center">
                    <svg class="w-36 h-24" viewBox="0 0 140 90" fill="none">
                        <circle cx="70" cy="45" r="38" stroke="#059669" stroke-width="2" fill="#f8fafc"/>
                        <line x1="70" y1="45" x2="70" y2="18" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>
                        <line x1="70" y1="45" x2="95" y2="45" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
                        <path d="M 70 32 A 13 13 0 0 1 83 45" stroke="#dc2626" stroke-width="2" fill="none"/>
                        <line x1="70" y1="18" x2="95" y2="45" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="2 2"/>
                        <text x="70" y="80" font-size="8" font-weight="bold" fill="#047857" text-anchor="middle">المسافة بين الرأسين</text>
                    </svg>
                    <span class="text-[10px] text-slate-500 font-bold">الزاوية المحصورة وعقارب الساعة (ص 172)</span>
                </div>
            </div>
        </section>


        <!-- ============================================================== -->
        <!-- المحطة 3: الشرح والتفسير والتطبيق البرهاني (EXPLAIN) - [4 درجات] -->
        <!-- ============================================================== -->
        <section class="worksheet-card p-5 rounded-2xl border border-blue-300 bg-blue-50/20 space-y-4">
            <div class="flex items-center justify-between border-b border-blue-200 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-blue-600 text-white font-black text-xs flex items-center justify-center">3</span>
                    <h2 class="text-sm sm:text-base font-black text-blue-950">المحطة الثالثة: الشرح والتطبيق البرهاني (Explain) — كتابة البراهين</h2>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 text-xs font-black">4 درجات</span>
            </div>

            <!-- Task 3.1: Flow Proof SSS (Example 1, p. 170) -->
            <div class="space-y-2">
                <div class="flex justify-between items-center text-xs sm:text-sm font-bold">
                    <span class="text-blue-900">س 3 (أ): أكمل مخطط البرهان التسلسلي الآتي لإثبات أن $\triangle GHL \cong \triangle KJL$ (كتاب الطالب ص 170):</span>
                    <span class="text-slate-500 font-normal">[درجتان]</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-12 gap-3 items-center">
                    <div class="sm:col-span-8 bg-white p-3 rounded-xl border border-slate-300 overflow-x-auto">
                        <div class="flex items-center justify-between gap-1 text-center min-w-[380px]">
                            <div class="flex-1 p-2 bg-slate-50 border border-slate-300 rounded-lg text-xs">
                                <div class="font-bold text-blue-700">$\overline{GH} \cong \overline{KJ}$</div>
                                <div class="text-[10px] text-slate-500 border-t border-slate-200 mt-1">معطى</div>
                            </div>
                            <span class="text-slate-400 font-bold">➔</span>
                            <div class="flex-1 space-y-1">
                                <div class="p-1.5 bg-slate-50 border border-slate-300 rounded text-[11px] text-slate-700 font-semibold">$L$ منتصف $\overline{GK}$ (معطى)</div>
                                <div class="text-[10px] text-slate-400">▼</div>
                                <div class="box-fill p-1 flex flex-col justify-center text-xs font-bold text-emerald-800">
                                    <span class="text-[10px] text-slate-400 font-normal">اكتب العبارة والمبرر:</span>
                                    <span class="ans-key hidden text-emerald-700 font-mono">$\overline{GL} \cong \overline{KL}$ (تعريف المنتصف)</span>
                                </div>
                            </div>
                            <span class="text-slate-400 font-bold">➔</span>
                            <div class="flex-1 p-2 bg-slate-50 border border-slate-300 rounded-lg text-xs">
                                <div class="font-bold text-blue-700">$\overline{HL} \cong \overline{JL}$</div>
                                <div class="text-[10px] text-slate-500 border-t border-slate-200 mt-1">معطى</div>
                            </div>
                            <span class="text-blue-600 font-bold">➔</span>
                            <div class="flex-1 p-2 bg-blue-600 text-white rounded-xl text-xs font-black shadow-xs">
                                <div>$\triangle GHL \cong \triangle KJL$</div>
                                <div class="text-[10px] text-blue-100 border-t border-blue-400 mt-1">مسلمة SSS</div>
                            </div>
                        </div>
                    </div>

                    <!-- SVG Example 1 -->
                    <div class="sm:col-span-4 bg-white p-2 rounded-xl border border-slate-200 flex items-center justify-center">
                        <svg class="w-36 h-20" viewBox="0 0 200 110" fill="none">
                            <line x1="20" y1="90" x2="180" y2="90" stroke="#0f172a" stroke-width="2"/>
                            <polygon points="20,90 100,90 50,20" fill="rgba(37, 99, 235, 0.08)" stroke="#2563eb" stroke-width="2"/>
                            <polygon points="100,90 180,90 150,20" fill="rgba(16, 185, 129, 0.08)" stroke="#059669" stroke-width="2"/>
                            <text x="12" y="100" font-size="9" font-weight="bold">G</text>
                            <text x="100" y="105" font-size="9" font-weight="bold" text-anchor="middle">L</text>
                            <text x="185" y="100" font-size="9" font-weight="bold">K</text>
                            <text x="45" y="15" font-size="9" font-weight="bold" fill="#2563eb">H</text>
                            <text x="155" y="15" font-size="9" font-weight="bold" fill="#059669">J</text>
                        </svg>
                    </div>
                </div>
            </div>

            <!-- Task 3.2: Two-Column Proof SAS (Scaffold Lights, p. 173) -->
            <div class="space-y-2 pt-2 border-t border-blue-100">
                <div class="flex justify-between items-center text-xs sm:text-sm font-bold">
                    <span class="text-blue-900">س 3 (ب): أكمل البرهان ذي العمودين لإثبات تطابق دعامات السقالة حاملة المصابيح (ص 173):</span>
                    <span class="text-slate-500 font-normal">[درجتان]</span>
                </div>
                <div class="text-xs text-slate-600 mb-1">
                    <strong>المعطيات:</strong> $\overline{WX} \cong \overline{ZY}$ ، $\overline{WX} \parallel \overline{ZY}$. <strong>المطلوب:</strong> $\triangle WXZ \cong \triangle YZX$.
                </div>

                <div class="overflow-x-auto rounded-xl border border-slate-300">
                    <table class="w-full text-right text-xs">
                        <thead class="bg-slate-100 font-bold text-slate-700">
                            <tr>
                                <th class="p-2 w-10 text-center">#</th>
                                <th class="p-2 w-1/2">العبارات (Statements)</th>
                                <th class="p-2 w-1/2">المبررات (Reasons)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 bg-white">
                            <tr>
                                <td class="p-2 text-center font-bold text-slate-500">1</td>
                                <td class="p-2">$\overline{WX} \cong \overline{ZY} \quad , \quad \overline{WX} \parallel \overline{ZY}$</td>
                                <td class="p-2 text-slate-600">معطيات (Given)</td>
                            </tr>
                            <tr>
                                <td class="p-2 text-center font-bold text-slate-500">2</td>
                                <td class="p-2 font-mono font-bold text-amber-800">
                                    <span class="ans-key hidden text-emerald-700">$\angle WXZ \cong \angle XZY$</span>
                                    <span class="write-line w-40 inline-block"></span>
                                </td>
                                <td class="p-2 text-slate-600">نظرية الزوايا الداخلية المتبادلة</td>
                            </tr>
                            <tr>
                                <td class="p-2 text-center font-bold text-slate-500">3</td>
                                <td class="p-2">$\overline{XZ} \cong \overline{ZX}$</td>
                                <td class="p-2 font-bold text-blue-800">
                                    <span class="ans-key hidden text-emerald-700">خاصية الانعكاس للتطابق</span>
                                    <span class="write-line w-44 inline-block"></span>
                                </td>
                            </tr>
                            <tr class="bg-blue-50/50">
                                <td class="p-2 text-center font-bold text-blue-700">4</td>
                                <td class="p-2 font-black text-blue-900">$\triangle WXZ \cong \triangle YZX$</td>
                                <td class="p-2 font-black text-blue-900">
                                    <span class="ans-key hidden text-emerald-700">مسلمة SAS</span>
                                    <span class="write-line w-36 inline-block"></span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>


        <!-- ============================================================== -->
        <!-- المحطة 4: الإثراء والتوسع والتفكير الناقد (ELABORATE) - [4 درجات] -->
        <!-- ============================================================== -->
        <section class="worksheet-card p-5 rounded-2xl border border-purple-300 bg-purple-50/20 space-y-4">
            <div class="flex items-center justify-between border-b border-purple-200 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-purple-600 text-white font-black text-xs flex items-center justify-center">4</span>
                    <h2 class="text-sm sm:text-base font-black text-purple-950">المحطة الرابعة: الإثراء والتوسع والتفكير الناقد (Elaborate)</h2>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-800 text-xs font-black">4 درجات</span>
            </div>

            <!-- Task 4.1: Error Detection (p. 177) -->
            <div class="p-3.5 bg-white rounded-xl border border-rose-200 space-y-2">
                <div class="flex justify-between items-center text-xs sm:text-sm font-bold">
                    <span class="text-rose-900"><i class="fa-solid fa-bug ml-1"></i>س 4 (أ): اكتشف الخطأ (مسألة 24 ص 177 في كتاب الطالب):</span>
                    <span class="text-slate-500 font-normal">[درجتان]</span>
                </div>
                <p class="text-xs text-slate-700 leading-relaxed">
                    قال <strong>أحمد</strong>: "إن المثلثين في الشكل أدناه متطابقان بحسب مسلمة SAS؛ لوجود ضلعين متطابقين وزاوية قياسها $59^\circ$". فاعترض <strong>خالد</strong> وقال: "المعلومات غير كافية!". <strong>من منهما إجابته صحيحة؟ وضح السبب الرياضي بدقة:</strong>
                </p>
                <div class="space-y-1">
                    <div class="write-line"></div>
                    <div class="write-line"></div>
                </div>

                <!-- Hidden Solution -->
                <div class="ans-key hidden p-2 bg-emerald-50 border border-emerald-300 rounded-lg text-emerald-900 font-bold text-xs">
                    <strong>الإجابة:</strong> إجابة <strong>خالد</strong> صحيحة؛ لأن الزاوية المعطاة ($59^\circ$) ليست محصورة بين الضلعين المتطابقين (هذه حالة $SSA$ الخاطئة)، وحالة $SSA$ تسمح للضلع الحر بالتأرجح وتكوين أكثر من مثلث فلا يتحقق التطابق.
                </div>
            </div>

            <!-- Task 4.2: Coordinate & Algebra (p. 171 & 176) -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
                <!-- Algebra -->
                <div class="p-3 bg-white rounded-xl border border-slate-200 space-y-2">
                    <span class="font-bold text-purple-900 block">س 4 (ب) مسألة جبرية (ص 176):</span>
                    <p class="text-slate-700 text-xs">إذا كان $\triangle WXY \cong \triangle WXZ$، وكان طولا الضلعين المتناظرين $3y+7$ و $19$. أوجد قيمة $y$:</p>
                    <div class="box-fill p-2 font-mono text-center font-bold text-purple-900">
                        <span class="ans-key hidden text-emerald-700">$3y + 7 = 19 \implies 3y = 12 \implies \mathbf{y = 4}$</span>
                    </div>
                </div>

                <!-- Coordinate Distance Check -->
                <div class="p-3 bg-white rounded-xl border border-slate-200 space-y-2">
                    <span class="font-bold text-purple-900 block">س 4 (ج) قانون المسافة (ص 171):</span>
                    <p class="text-slate-700 text-xs">احسب المسافة بين النقطتين $J(2, 5)$ و $K(1, 1)$ باستخدام قانون المسافة $d$:</p>
                    <div class="box-fill p-2 font-mono text-center font-bold text-purple-900">
                        <span class="ans-key hidden text-emerald-700">$JK = \sqrt{(1-2)^2 + (1-5)^2} = \sqrt{1+16} = \mathbf{\sqrt{17}}$</span>
                    </div>
                </div>
            </div>
        </section>


        <!-- ============================================================== -->
        <!-- المحطة 5: التقويم وتذكرة الخروج (EVALUATE) - [3 درجات] -->
        <!-- ============================================================== -->
        <section class="worksheet-card p-5 rounded-2xl border border-rose-300 bg-rose-50/20 space-y-4">
            <div class="flex items-center justify-between border-b border-rose-200 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-rose-600 text-white font-black text-xs flex items-center justify-center">5</span>
                    <h2 class="text-sm sm:text-base font-black text-rose-950">المحطة الخامسة: تذكرة الخروج والتقويم الختامي (Evaluate)</h2>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-rose-100 text-rose-800 text-xs font-black">3 درجات</span>
            </div>

            <!-- Exit Ticket from Book Question 26, p. 177 -->
            <div class="p-3.5 bg-white rounded-xl border border-rose-200 space-y-3">
                <div class="flex justify-between items-center text-xs sm:text-sm font-bold">
                    <span class="text-slate-900">س 5: تدريب على اختبار معياري (مسألة 26 ص 177 في كتاب الطالب):</span>
                    <span class="text-rose-600 font-bold">[درجة ونصف]</span>
                </div>
                <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
                    في الشكلين أدناه، إذا كان $\overline{AC} \cong \overline{XZ}$ و $\angle C \cong \angle Z$. ما المعلومة الإضافية التي يمكن استعمالها لإثبات أن $\triangle ABC \cong \triangle XYZ$ بمسلمة $SAS$؟
                </p>

                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 text-xs font-mono font-bold">
                    <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 hover:bg-slate-50 cursor-pointer">
                        <input type="radio" name="ws_mcq" class="w-4 h-4 text-rose-600">
                        <span>(A) $\overline{BC} \cong \overline{YZ}$</span>
                    </label>
                    <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 hover:bg-slate-50 cursor-pointer">
                        <input type="radio" name="ws_mcq" class="w-4 h-4 text-rose-600">
                        <span>(B) $\overline{AB} \cong \overline{XY}$</span>
                    </label>
                    <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 hover:bg-slate-50 cursor-pointer">
                        <input type="radio" name="ws_mcq" class="w-4 h-4 text-rose-600">
                        <span>(C) $\overline{BC} \cong \overline{XZ}$</span>
                    </label>
                    <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 hover:bg-slate-50 cursor-pointer">
                        <input type="radio" name="ws_mcq" class="w-4 h-4 text-rose-600">
                        <span>(D) $\overline{XZ} \cong \overline{XY}$</span>
                    </label>
                </div>

                <div class="ans-key hidden p-2 bg-emerald-50 border border-emerald-300 rounded-lg text-emerald-900 font-bold text-xs">
                    <strong>الإجابة الصحيحة: (A) $\overline{BC} \cong \overline{YZ}$</strong>؛ لأن الزاوية $\angle C$ تكون محصورة بين $\overline{AC}$ و $\overline{BC}$، والزاوية $\angle Z$ تكون محصورة بين $\overline{XZ}$ و $\overline{YZ}$.
                </div>
            </div>

            <!-- True / False Fast Check -->
            <div class="p-3 bg-white rounded-xl border border-slate-200 text-xs sm:text-sm space-y-2">
                <span class="font-bold text-slate-800 block">ضع علامة (✓) أو (✗) أمام العبارات الآتية: [درجة ونصف]</span>
                <div class="space-y-1.5 text-xs text-slate-700">
                    <div class="flex items-center justify-between p-1.5 rounded bg-slate-50">
                        <span>1. إذا طابقت أضلاع مثلث الأضلاع المناظرة في مثلث آخر، فإن المثلثين متطابقان (SSS).</span>
                        <span class="font-bold text-blue-600">( &nbsp; <span class="ans-key hidden text-emerald-700 font-black">✓</span> &nbsp; )</span>
                    </div>
                    <div class="flex items-center justify-between p-1.5 rounded bg-slate-50">
                        <span>2. تطابق ضلعين وزاوية غير محصورة (SSA) يكفي دائماً لإثبات تطابق أي مثلثين.</span>
                        <span class="font-bold text-blue-600">( &nbsp; <span class="ans-key hidden text-rose-700 font-black">✗</span> &nbsp; )</span>
                    </div>
                </div>
            </div>
        </section>


        <!-- Student Self-Assessment Rubric & Teacher Feedback Footer -->
        <footer class="pt-2 border-t-2 border-slate-200 grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-1.5">
                <span class="font-bold text-slate-800 flex items-center gap-1.5">
                    <i class="fa-solid fa-star text-amber-500"></i>سلم التقييم الذاتي للطالب:
                </span>
                <div class="grid grid-cols-3 gap-1.5 text-center text-[11px] font-semibold">
                    <div class="p-1 rounded border border-slate-300 bg-white">
                        <input type="checkbox" class="ml-1"> أتقنت تماماً (3/3)
                    </div>
                    <div class="p-1 rounded border border-slate-300 bg-white">
                        <input type="checkbox" class="ml-1"> أحتاج تدريباً بسيطاً
                    </div>
                    <div class="p-1 rounded border border-slate-300 bg-white">
                        <input type="checkbox" class="ml-1"> أطلب مساعدة المعلم
                    </div>
                </div>
            </div>

            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 flex flex-col justify-between">
                <div class="flex justify-between items-center font-bold text-slate-700">
                    <span>توقيع المعلم: ..............................</span>
                    <span>الدرجة المستحقة: &nbsp;&nbsp;&nbsp;&nbsp; / 15</span>
                </div>
                <div class="text-[10px] text-slate-400 text-left pt-1 font-mono">
                    STEM-5Es Curriculum • Mathematics 1-2 (Saudi Pathways)
                </div>
            </div>
        </footer>

    </div>

    <!-- JavaScript for Interactive Worksheet Features -->
    <script>
        let keyVisible = false;
        function toggleAnswerKey() {
            keyVisible = !keyVisible;
            const elements = document.querySelectorAll('.ans-key');
            elements.forEach(el => {
                if (keyVisible) el.classList.remove('hidden');
                else el.classList.add('hidden');
            });
            const btnTxt = document.getElementById('key-btn-txt');
            if (btnTxt) {
                btnTxt.innerText = keyVisible ? 'إخفاء مفتاح الحل النموذجي' : 'إظهار مفتاح الحل النموذجي';
            }
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        }
    </script>
</body>
</html>
'''

output_path = r'c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\ورقة_عمل_إثبات_تطابق_المثلثات_SSS_SAS_5Es.html'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(WORKSHEET_HTML)

print(f"Generated 5Es worksheet at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
