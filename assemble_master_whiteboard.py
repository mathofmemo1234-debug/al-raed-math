# -*- coding: utf-8 -*-
"""
Generator script for the Comprehensive Dynamic Student Whiteboard:
إثبات تطابق المثلثات (SSS, SAS) - العرض الشامل التفاعلي لكل مسائل وتمارين كتاب الطالب
"""

import os

# We will create the complete HTML string in sections to ensure zero truncation and maximum fidelity.
header_part = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>السبورة التفاعلية الشاملة: إثبات تطابق المثلثات (SSS, SAS)</title>
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
                        brandBlue: { 50: '#eff6ff', 100: '#dbeafe', 500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8' },
                        brandOrange: { 500: '#f97316', 600: '#ea580c' },
                        brandEmerald: { 500: '#10b981', 600: '#059669' },
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
        .whiteboard-card {
            background: #ffffff;
            border: 2px solid #e2e8f0;
            border-radius: 1.5rem;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .whiteboard-card:hover {
            border-color: #cbd5e1;
        }
        .tool-draggable {
            position: absolute;
            cursor: grab;
            user-select: none;
            z-index: 50;
            touch-action: none;
        }
        .tool-draggable:active {
            cursor: grabbing;
        }
        .nav-pill.active {
            background-color: #2563eb;
            color: #ffffff;
            box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3);
        }
        .grid-bg {
            background-image: linear-gradient(#f1f5f9 1px, transparent 1px), linear-gradient(90deg, #f1f5f9 1px, transparent 1px);
            background-size: 20px 20px;
        }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased selection:bg-blue-600 selection:text-white min-h-screen flex flex-col">

    <!-- Top Whiteboard Controls & Banner -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50 px-4 sm:px-6 py-3 shadow-xs">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            
            <!-- Branding -->
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white shadow-md shadow-blue-500/20 text-xl font-black">
                    <i class="fa-solid fa-shapes"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 text-[11px] font-black">رياضيات 1-2 • مسارات</span>
                        <span class="text-xs text-slate-500 font-bold">الدرس (3-4) كامل بمسائله ورسوماته</span>
                    </div>
                    <h1 class="text-lg sm:text-2xl font-black text-slate-900 leading-tight">السبورة التفاعلية الشاملة: إثبات تطابق المثلثات (SSS, SAS)</h1>
                </div>
            </div>

            <!-- Virtual Floating Tools Controls -->
            <div class="flex items-center gap-2">
                <!-- Protractor Button -->
                <button onclick="toggleTool('v-protractor')" class="px-3.5 py-2 rounded-xl border border-amber-200 bg-amber-50 hover:bg-amber-100 text-xs font-black text-amber-900 shadow-xs transition flex items-center gap-2">
                    <i class="fa-solid fa-compass-drafting text-amber-600 text-sm"></i>
                    <span>المنقلة 360°</span>
                </button>

                <!-- Ruler Button -->
                <button onclick="toggleTool('v-ruler')" class="px-3.5 py-2 rounded-xl border border-blue-200 bg-blue-50 hover:bg-blue-100 text-xs font-black text-blue-900 shadow-xs transition flex items-center gap-2">
                    <i class="fa-solid fa-ruler-combined text-blue-600 text-sm"></i>
                    <span>المسطرة الرقمية</span>
                </button>

                <!-- Timer -->
                <div class="bg-slate-100 border border-slate-200 px-3 py-1.5 rounded-xl flex items-center gap-2">
                    <i class="fa-regular fa-clock text-blue-600"></i>
                    <span id="board-timer" class="font-mono text-sm font-black text-slate-800">00:00</span>
                    <button onclick="toggleTimer()" id="timer-btn" class="text-xs bg-white border border-slate-300 hover:bg-slate-50 px-2 py-0.5 rounded font-bold text-slate-700">
                        <i class="fa-solid fa-play"></i>
                    </button>
                    <button onclick="resetTimer()" class="text-xs bg-white border border-slate-300 hover:bg-slate-50 px-2 py-0.5 rounded text-slate-700">
                        <i class="fa-solid fa-rotate-right"></i>
                    </button>
                </div>

                <!-- Fullscreen -->
                <button onclick="toggleFullScreen()" class="bg-blue-600 hover:bg-blue-700 text-white p-2.5 rounded-xl text-xs font-bold shadow-xs transition" title="ملء الشاشة">
                    <i class="fa-solid fa-expand"></i>
                </button>
            </div>
        </div>

        <!-- 6Es Navigation Ribbon -->
        <div class="max-w-7xl mx-auto mt-3 overflow-x-auto pb-1">
            <div class="flex items-center gap-2 min-w-max bg-slate-100 p-1.5 rounded-2xl border border-slate-200">
                <button onclick="switchTab('sec-engage')" id="btn-sec-engage" class="nav-pill active px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition flex items-center gap-2">
                    <span>⚡ 1. محاكاة المربع والمثلث والسبورة A (Engage)</span>
                </button>
                <button onclick="switchTab('sec-explore')" id="btn-sec-explore" class="nav-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-2">
                    <span>🔬 2. مختبر SSS و SAS وخديعة SSA (Explore)</span>
                </button>
                <button onclick="switchTab('sec-explain')" id="btn-sec-explain" class="nav-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-2">
                    <span>📐 3. براهين الكتاب ورسوماتها (Explain)</span>
                </button>
                <button onclick="switchTab('sec-engineer')" id="btn-sec-engineer" class="nav-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-2">
                    <span>🏗️ 4. السقالات وجسر الرياض المعلق (Engineer)</span>
                </button>
                <button onclick="switchTab('sec-elaborate')" id="btn-sec-elaborate" class="nav-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-2">
                    <span>⚔️ 5. شبكة الإحداثيات ومناظرة أحمد وخالد (Elaborate)</span>
                </button>
                <button onclick="switchTab('sec-evaluate')" id="btn-sec-evaluate" class="nav-pill px-4 py-2 rounded-xl text-xs sm:text-sm font-bold text-slate-600 hover:text-slate-900 transition flex items-center gap-2">
                    <span>🏆 6. تذكرة الخروج وشجرة القرار (Evaluate)</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Draggable Virtual Tools -->

    <!-- Virtual Protractor (منقلة رقمية نصف دائرية شفافة قابلة للسحب والتدوير التام) -->
    <div id="v-protractor" class="tool-draggable hidden" style="top: 140px; left: 80px;">
        <div class="relative group bg-amber-50/90 backdrop-blur border-2 border-amber-500 rounded-b-full p-2 shadow-2xl">
            <button onclick="toggleTool('v-protractor')" class="absolute -top-3 -right-3 w-6 h-6 bg-rose-600 text-white rounded-full flex items-center justify-center text-xs shadow-md z-50">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <div class="flex items-center justify-between text-[11px] font-black text-amber-900 px-3 pb-1 border-b border-amber-300">
                <span>المنقلة الشفافة</span>
                <button onclick="rotateProtractor()" class="bg-amber-500 hover:bg-amber-600 text-white px-2 py-0.5 rounded text-[10px]">
                    تدوير: <span id="prot-deg">0°</span>
                </button>
            </div>
            <svg id="prot-svg" class="w-80 h-40 transition-transform" viewBox="0 0 320 160" fill="none">
                <path d="M 10 150 A 150 150 0 0 1 310 150 Z" fill="rgba(254, 243, 199, 0.65)" stroke="#d97706" stroke-width="2.5"/>
                <circle cx="160" cy="150" r="5" fill="#b45309"/>
                <line x1="160" y1="135" x2="160" y2="150" stroke="#b45309" stroke-width="2"/>
                <line x1="10" y1="150" x2="310" y2="150" stroke="#b45309" stroke-width="2"/>
                <!-- Degree labels -->
                <text x="160" y="25" font-size="12" font-weight="900" fill="#92400e" text-anchor="middle">90°</text>
                <text x="55" y="125" font-size="11" font-weight="bold" fill="#92400e">30°</text>
                <text x="85" y="70" font-size="11" font-weight="bold" fill="#92400e">60°</text>
                <text x="235" y="70" font-size="11" font-weight="bold" fill="#92400e">120°</text>
                <text x="265" y="125" font-size="11" font-weight="bold" fill="#92400e">150°</text>
                <text x="25" y="145" font-size="11" font-weight="bold" fill="#92400e">0°</text>
                <text x="295" y="145" font-size="11" font-weight="bold" fill="#92400e">180°</text>
            </svg>
        </div>
    </div>

    <!-- Virtual Ruler (مسطرة رقمية قابلة للسحب) -->
    <div id="v-ruler" class="tool-draggable hidden" style="top: 260px; left: 120px;">
        <div class="relative bg-blue-50/90 backdrop-blur border-2 border-blue-400 rounded-xl p-2 shadow-2xl w-96">
            <button onclick="toggleTool('v-ruler')" class="absolute -top-3 -right-3 w-6 h-6 bg-rose-600 text-white rounded-full flex items-center justify-center text-xs shadow-md z-50">
                <i class="fa-solid fa-xmark"></i>
            </button>
            <div class="flex justify-between items-center text-[10px] font-mono text-blue-900 border-b border-blue-300 pb-1">
                <span class="font-sans font-bold">مسطرة القياس السنتيمترية الرقمية</span>
                <span class="text-blue-700 font-bold">12 cm</span>
            </div>
            <div class="flex justify-between items-start h-6 pt-1 font-mono text-[9px] text-blue-800">
                <span class="border-r border-blue-700 h-5 pl-0.5">0</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">2</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">4</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">6</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">8</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">10</span>
                <span class="border-r border-blue-400 h-2"></span>
                <span class="border-r border-blue-700 h-5 pl-0.5">12 cm</span>
            </div>
        </div>
    </div>

    <!-- Main Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-8">
'''

with open(r'c:\Users\TOSHIBA\.gemini\antigravity\scratch\تحضر\عرض_السبورة_التفاعلي_الشامل_المثلثات_SSS_SAS.html', 'w', encoding='utf-8') as f:
    f.write(header_part)

print("Wrote header part successfully.")
