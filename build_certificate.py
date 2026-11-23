import base64
import subprocess
import os
import shutil

with open('motaqadimah_logo_clean.png', 'rb') as f:
    motaqadimah_b64 = base64.b64encode(f.read()).decode('utf-8')

with open('moe_logo.svg', 'rb') as f:
    moe_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>شهادة شكر وتقدير - عبدالعزيز أحمد عبدالعزيز آل عسيس الغامدي</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 landscape;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    background-color: #0b1216;
    font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 0;
    margin: 0;
  }}

  /* Exact A4 Landscape Standard (1414 x 1000 px) */
  .certificate-canvas {{
    width: 1414px;
    height: 1000px;
    position: relative;
    background: #ffffff;
    background-image: 
      radial-gradient(circle at 50% 35%, #ffffff 0%, #fbf9f4 60%, #f4ede0 100%);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    padding: 20px;
    font-family: 'Cairo', sans-serif;
  }}

  /* Fine Guilloche Certificate Security Pattern */
  .security-pattern {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    opacity: 0.038;
    background-image: 
      radial-gradient(circle at 50% 50%, #035c6a 1.2px, transparent 1.2px),
      radial-gradient(circle at 0% 0%, #c59b27 1.2px, transparent 1.2px);
    background-size: 20px 20px, 40px 40px;
    z-index: 1;
  }}

  /* Watermark Rosette in Center */
  .watermark-rosette {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 620px;
    height: 620px;
    opacity: 0.032;
    pointer-events: none;
    z-index: 1;
  }}

  /* Outermost Golden Border */
  .outer-gold-border {{
    width: 100%;
    height: 100%;
    position: relative;
    border: 3.5px solid #c59b27;
    outline: 1.5px solid #dfbb6c;
    outline-offset: -7px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    z-index: 2;
    box-shadow: inset 0 0 35px rgba(197, 155, 39, 0.15);
  }}

  /* Geometric Middle Border */
  .geometric-frame {{
    width: 100%;
    height: 100%;
    position: relative;
    border: 1px dashed #d1a843;
    padding: 7px;
    display: flex;
    flex-direction: column;
  }}

  /* Main Inner Certificate Panel */
  .inner-panel {{
    width: 100%;
    height: 100%;
    position: relative;
    border: 2.5px solid #065b6b;
    padding: 24px 38px 24px 38px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 
      inset 0 0 0 3px #ffffff,
      inset 0 0 0 5px #e5c36d,
      0 4px 20px rgba(0, 0, 0, 0.04);
  }}

  /* Ornate Corner Elements */
  .corner-decor {{
    position: absolute;
    width: 82px;
    height: 82px;
    z-index: 5;
    pointer-events: none;
  }}
  .corner-tl {{ top: -2px; left: -2px; transform: scaleX(-1); }}
  .corner-tr {{ top: -2px; right: -2px; }}
  .corner-bl {{ bottom: -2px; left: -2px; transform: scale(-1); }}
  .corner-br {{ bottom: -2px; right: -2px; transform: scaleY(-1); }}

  /* ==================== HEADER ==================== */
  .cert-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding-bottom: 12px;
    border-bottom: 2px solid;
    border-image: linear-gradient(to right, transparent, #c59b27 18%, #055f6e 50%, #c59b27 82%, transparent) 1;
  }}

  .header-entity {{
    display: flex;
    align-items: center;
    gap: 15px;
    width: 360px;
  }}

  .header-entity.right-side {{
    justify-content: flex-start;
  }}

  .header-entity.left-side {{
    justify-content: flex-end;
  }}

  .entity-text {{
    display: flex;
    flex-direction: column;
    gap: 1px;
  }}

  .entity-main {{
    font-size: 16px;
    font-weight: 900;
    color: #083742;
    letter-spacing: 0.2px;
  }}

  .entity-sub {{
    font-size: 13.5px;
    color: #3f5960;
    font-weight: 700;
  }}

  .entity-dept {{
    font-size: 12.5px;
    color: #067283;
    font-weight: 800;
  }}

  .logo-moe {{
    height: 76px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.06));
  }}

  .logo-school {{
    height: 86px;
    width: 86px;
    object-fit: contain;
    filter: drop-shadow(0 3px 6px rgba(5, 102, 118, 0.2));
  }}

  .header-center {{
    text-align: center;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }}

  .basmala {{
    font-size: 23px;
    color: #8c6307;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-shadow: 0 1px 1px rgba(0,0,0,0.05);
  }}

  .nasmoo-badge-top {{
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    background: linear-gradient(135deg, #065b6b 0%, #0a4652 100%);
    color: #ffffff;
    padding: 4px 22px;
    border-radius: 20px;
    box-shadow: 0 2px 6px rgba(6, 91, 107, 0.2);
    border: 1px solid #d4af37;
  }}

  .nasmoo-title-ar {{
    font-size: 13.5px;
    font-weight: 800;
    letter-spacing: 0.2px;
  }}

  .nasmoo-title-en {{
    font-size: 9.5px;
    font-weight: 700;
    color: #e0f2f1;
    letter-spacing: 0.5px;
  }}

  /* ==================== TITLE SECTION ==================== */
  .title-section {{
    text-align: center;
    margin: 6px 0 2px 0;
  }}

  .grand-title {{
    font-size: 50px;
    font-weight: 900;
    line-height: 1.15;
    background: linear-gradient(180deg, #996e11 0%, #e0b443 38%, #8a6106 72%, #cf9e26 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 2px 3px rgba(138, 97, 6, 0.25));
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }}

  .title-divider {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 16px;
    margin: 2px 0 6px 0;
  }}

  .divider-line {{
    width: 180px;
    height: 2px;
    background: linear-gradient(to right, transparent, #c59b27, transparent);
  }}

  .divider-symbol {{
    color: #c59b27;
    font-size: 16px;
  }}

  .title-subtitle {{
    font-size: 17px;
    font-weight: 800;
    color: #06606f;
    letter-spacing: 0.3px;
  }}

  /* ==================== BODY SECTION (PERFECTLY DISTRIBUTED - NO GAPS) ==================== */
  .cert-body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    text-align: center;
    padding: 6px 15px;
    margin: 4px 0;
  }}

  .intro-text {{
    font-size: 20px;
    color: #2b3940;
    font-weight: 700;
    line-height: 1.4;
  }}

  /* Student Name Illuminated Cartouche */
  .student-cartouche {{
    position: relative;
    background: linear-gradient(135deg, #fdfbf7 0%, #f7f1e6 50%, #fdfbf7 100%);
    border: 2.5px solid #c99c32;
    border-radius: 14px;
    padding: 14px 80px;
    box-shadow: 
      inset 0 0 25px rgba(201, 156, 50, 0.18),
      0 6px 20px rgba(0, 0, 0, 0.06);
    display: inline-block;
    margin: 4px 0;
  }}

  .student-cartouche::before, .student-cartouche::after {{
    content: "❖";
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: #c59b27;
    font-size: 24px;
  }}
  .student-cartouche::before {{ left: 26px; }}
  .student-cartouche::after {{ right: 26px; }}

  .cartouche-title {{
    font-size: 14.5px;
    color: #8c650b;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 3px;
  }}

  .student-name {{
    font-size: 42px;
    font-weight: 900;
    color: #073844;
    letter-spacing: 0.5px;
    text-shadow: 0 1px 2px rgba(7, 56, 68, 0.12);
  }}

  /* Achievement Paragraph with Rich Cairo Typography */
  .achievement-box {{
    max-width: 1180px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 4px 0;
  }}

  .achievement-line {{
    font-size: 22px;
    color: #1a282f;
    font-weight: 700;
    line-height: 1.6;
  }}

  .highlight-term {{
    color: #045a68;
    font-weight: 900;
    background: rgba(6, 91, 107, 0.09);
    padding: 3px 16px;
    border-radius: 8px;
    border: 1.5px solid rgba(6, 91, 107, 0.25);
    font-size: 21px;
  }}

  .highlight-score {{
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, #065b6b 0%, #0a4753 100%);
    color: #ffffff;
    font-weight: 900;
    padding: 2px 20px;
    border-radius: 10px;
    font-size: 22px;
    box-shadow: 0 3px 8px rgba(6, 91, 107, 0.3);
    border: 1.5px solid #dfbb6c;
  }}

  .highlight-nasmoo {{
    color: #8c6307;
    font-weight: 900;
    background: rgba(212, 175, 55, 0.2);
    padding: 3px 18px;
    border-radius: 8px;
    border: 1.5px solid rgba(201, 156, 50, 0.5);
    font-size: 21px;
  }}

  /* Three Medallion Badges - Spacious & Prominent */
  .medallions-row {{
    display: flex;
    justify-content: center;
    gap: 28px;
    margin: 6px 0;
  }}

  .medallion-pill {{
    display: flex;
    align-items: center;
    gap: 14px;
    background: #ffffff;
    border: 2px solid #c59b27;
    border-radius: 35px;
    padding: 10px 28px;
    box-shadow: 0 4px 14px rgba(197, 155, 39, 0.15);
  }}

  .medallion-svg {{
    width: 30px;
    height: 30px;
    flex-shrink: 0;
  }}

  .medallion-label {{
    font-size: 16px;
    font-weight: 800;
    color: #074754;
  }}

  /* Closing Prayer - Framed & Elegant */
  .prayer-statement {{
    font-size: 18px;
    color: #3b5059;
    font-weight: 700;
    background: linear-gradient(135deg, rgba(255,255,255,0.7) 0%, rgba(247, 243, 232, 0.7) 100%);
    border: 1px solid #d4af37;
    border-radius: 20px;
    padding: 6px 36px;
    margin-top: 4px;
  }}

  /* ==================== SIGNATURES FOOTER ==================== */
  .signatures-section {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    width: 100%;
    padding: 0 24px;
    position: relative;
    border-top: 2px solid;
    border-image: linear-gradient(to right, transparent, #c59b27 15%, #dcd4c3 50%, #c59b27 85%, transparent) 1;
    padding-top: 16px;
    padding-bottom: 4px;
  }}

  .signature-column {{
    width: 290px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
  }}

  .col-title {{
    font-size: 16px;
    font-weight: 800;
    color: #055f6e;
    margin-bottom: 3px;
  }}

  .col-name {{
    font-size: 21px;
    font-weight: 900;
    color: #0c232b;
    margin-bottom: 16px;
  }}

  .clean-sig-box {{
    width: 200px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .signature-baseline {{
    width: 200px;
    height: 1.5px;
    background: linear-gradient(to right, transparent, #b8860b, transparent);
    margin-top: 2px;
  }}

  .col-caption {{
    font-size: 12.5px;
    color: #7b8e94;
    font-weight: 700;
    margin-top: 5px;
    letter-spacing: 0.5px;
  }}

  /* Official Certified Seal */
  .official-certified-seal {{
    position: absolute;
    left: 350px;
    bottom: -4px;
    width: 125px;
    height: 125px;
    border-radius: 50%;
    background: radial-gradient(circle, #fffdf5 0%, #ebd38e 55%, #c29528 100%);
    border: 3px double #8a650d;
    box-shadow: 
      0 6px 16px rgba(138, 101, 13, 0.28),
      inset 0 0 10px rgba(255, 255, 255, 0.85);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8px;
    z-index: 6;
    transform: rotate(-10deg);
  }}

  .seal-dashed-ring {{
    position: absolute;
    top: 5px; left: 5px; right: 5px; bottom: 5px;
    border: 1px dashed #8c6710;
    border-radius: 50%;
    pointer-events: none;
  }}

  .seal-txt-top {{
    font-size: 9.5px;
    font-weight: 900;
    color: #5c4205;
    line-height: 1.1;
  }}

  .seal-ribbon {{
    background: #065b6b;
    color: #ffffff;
    font-size: 10.5px;
    font-weight: 900;
    padding: 2px 10px;
    border-radius: 4px;
    margin: 3px 0 1px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.25);
    border: 1px solid #ffd700;
    letter-spacing: 0.5px;
  }}

  .seal-en {{
    font-size: 7.5px;
    font-weight: 800;
    color: #5c4205;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
  }}

  .seal-stars {{
    color: #8c6710;
    font-size: 9.5px;
    letter-spacing: 2px;
    line-height: 1;
  }}

  .seal-txt-bottom {{
    font-size: 9px;
    font-weight: 800;
    color: #5c4205;
    line-height: 1.1;
  }}

  /* Print Media */
  @media print {{
    body {{
      background: none !important;
      padding: 0 !important;
      margin: 0 !important;
    }}
    .certificate-canvas {{
      box-shadow: none !important;
      width: 100vw !important;
      height: 100vh !important;
      padding: 10mm 14mm !important;
      page-break-after: avoid !important;
      page-break-inside: avoid !important;
    }}
  }}
</style>
</head>
<body>

<div class="certificate-canvas">
  <!-- Guilloche Security Pattern -->
  <div class="security-pattern"></div>

  <!-- Central Watermark Rosette -->
  <svg class="watermark-rosette" viewBox="0 0 200 200">
    <circle cx="100" cy="100" r="92" fill="none" stroke="#065b6b" stroke-width="1.2"/>
    <circle cx="100" cy="100" r="84" fill="none" stroke="#c59b27" stroke-width="0.8" stroke-dasharray="3,3"/>
    <circle cx="100" cy="100" r="72" fill="none" stroke="#065b6b" stroke-width="0.8"/>
    <!-- 8-Point Star Guilloche -->
    <polygon points="100,20 122,68 174,68 132,100 152,150 100,120 48,150 68,100 26,68 78,68" fill="none" stroke="#065b6b" stroke-width="0.8"/>
    <polygon points="100,32 116,74 162,74 126,100 142,142 100,116 58,142 74,100 38,74 84,74" fill="none" stroke="#c59b27" stroke-width="0.7"/>
    <circle cx="100" cy="100" r="30" fill="none" stroke="#065b6b" stroke-width="0.6"/>
  </svg>

  <div class="outer-gold-border">
    <div class="geometric-frame">
      <div class="inner-panel">

        <!-- Corner Ornaments -->
        <!-- Top Right -->
        <svg class="corner-decor corner-tr" viewBox="0 0 100 100">
          <path d="M0,0 L100,0 L100,26 L34,26 Q26,26 26,34 L26,100 L0,100 Z" fill="url(#goldGradientTr)"/>
          <path d="M30,30 L94,30 L94,35 L40,35 Q35,35 35,40 L35,94 L30,94 Z" fill="#065b6b"/>
          <circle cx="58" cy="58" r="8" fill="url(#goldGradientTr)"/>
          <circle cx="58" cy="58" r="5" fill="#065b6b"/>
          <path d="M46,46 Q58,30 70,46 Q86,58 70,70 Q58,86 46,70 Q30,58 46,46 Z" fill="none" stroke="url(#goldGradientTr)" stroke-width="2"/>
          <defs>
            <linearGradient id="goldGradientTr" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d4af37"/>
              <stop offset="50%" stop-color="#fff0a8"/>
              <stop offset="100%" stop-color="#aa771c"/>
            </linearGradient>
          </defs>
        </svg>

        <!-- Top Left -->
        <svg class="corner-decor corner-tl" viewBox="0 0 100 100">
          <path d="M0,0 L100,0 L100,26 L34,26 Q26,26 26,34 L26,100 L0,100 Z" fill="url(#goldGradientTl)"/>
          <path d="M30,30 L94,30 L94,35 L40,35 Q35,35 35,40 L35,94 L30,94 Z" fill="#065b6b"/>
          <circle cx="58" cy="58" r="8" fill="url(#goldGradientTl)"/>
          <circle cx="58" cy="58" r="5" fill="#065b6b"/>
          <path d="M46,46 Q58,30 70,46 Q86,58 70,70 Q58,86 46,70 Q30,58 46,46 Z" fill="none" stroke="url(#goldGradientTl)" stroke-width="2"/>
          <defs>
            <linearGradient id="goldGradientTl" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d4af37"/>
              <stop offset="50%" stop-color="#fff0a8"/>
              <stop offset="100%" stop-color="#aa771c"/>
            </linearGradient>
          </defs>
        </svg>

        <!-- Bottom Left -->
        <svg class="corner-decor corner-bl" viewBox="0 0 100 100">
          <path d="M0,0 L100,0 L100,26 L34,26 Q26,26 26,34 L26,100 L0,100 Z" fill="url(#goldGradientBl)"/>
          <path d="M30,30 L94,30 L94,35 L40,35 Q35,35 35,40 L35,94 L30,94 Z" fill="#065b6b"/>
          <circle cx="58" cy="58" r="8" fill="url(#goldGradientBl)"/>
          <circle cx="58" cy="58" r="5" fill="#065b6b"/>
          <path d="M46,46 Q58,30 70,46 Q86,58 70,70 Q58,86 46,70 Q30,58 46,46 Z" fill="none" stroke="url(#goldGradientBl)" stroke-width="2"/>
          <defs>
            <linearGradient id="goldGradientBl" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d4af37"/>
              <stop offset="50%" stop-color="#fff0a8"/>
              <stop offset="100%" stop-color="#aa771c"/>
            </linearGradient>
          </defs>
        </svg>

        <!-- Bottom Right -->
        <svg class="corner-decor corner-br" viewBox="0 0 100 100">
          <path d="M0,0 L100,0 L100,26 L34,26 Q26,26 26,34 L26,100 L0,100 Z" fill="url(#goldGradientBr)"/>
          <path d="M30,30 L94,30 L94,35 L40,35 Q35,35 35,40 L35,94 L30,94 Z" fill="#065b6b"/>
          <circle cx="58" cy="58" r="8" fill="url(#goldGradientBr)"/>
          <circle cx="58" cy="58" r="5" fill="#065b6b"/>
          <path d="M46,46 Q58,30 70,46 Q86,58 70,70 Q58,86 46,70 Q30,58 46,46 Z" fill="none" stroke="url(#goldGradientBr)" stroke-width="2"/>
          <defs>
            <linearGradient id="goldGradientBr" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d4af37"/>
              <stop offset="50%" stop-color="#fff0a8"/>
              <stop offset="100%" stop-color="#aa771c"/>
            </linearGradient>
          </defs>
        </svg>

        <!-- HEADER -->
        <div class="cert-header">
          <!-- Right: Ministry of Education -->
          <div class="header-entity right-side">
            <img class="logo-moe" src="data:image/svg+xml;base64,{moe_b64}" alt="شعار وزارة التعليم">
            <div class="entity-text">
              <span class="entity-main">المملكة العربية السعودية</span>
              <span class="entity-sub">وزارة التعليم</span>
              <span class="entity-dept">إدارة التعليم الأهلي والأجنبي</span>
            </div>
          </div>

          <!-- Center: Basmala & Official Olympiad Title -->
          <div class="header-center">
            <div class="basmala">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
            <div class="nasmoo-badge-top">
              <span class="nasmoo-title-ar">أولمبياد العلوم والرياضيات الوطني «نَسْمُو»</span>
              <span class="nasmoo-title-en">National Science & Mathematics Olympiad 'NESMO'</span>
            </div>
          </div>

          <!-- Left: Al-Motaqadimah Schools -->
          <div class="header-entity left-side">
            <div class="entity-text" style="text-align: right;">
              <span class="entity-main">شركة المدارس المتقدمة</span>
              <span class="entity-sub">مدارس المتقدمة للتعلم الذكي</span>
              <span class="entity-dept">قسم الرياضيات</span>
            </div>
            <img class="logo-school" src="data:image/png;base64,{motaqadimah_b64}" alt="شعار شركة المدارس المتقدمة">
          </div>
        </div>

        <!-- TITLE AREA -->
        <div class="title-section">
          <h1 class="grand-title">شَهَادَةُ شُكْرٍ وَتَقْدِير</h1>
          <div class="title-divider">
            <div class="divider-line"></div>
            <div class="divider-symbol">✦ &nbsp; ❖ &nbsp; ✦</div>
            <div class="divider-line"></div>
          </div>
          <div class="title-subtitle">تَفَوُّقٌ فِي مَسَارِ الرِّيَاضِيَّاتِ وَتَأَهُّلٌ مُسْتَحَقٌّ فِي أولمبياد العلوم والرياضيات الوطني «نَسْمُو»</div>
        </div>

        <!-- BODY CONTENT (DISTRIBUTED EVENLY) -->
        <div class="cert-body">
          <p class="intro-text">
            تَسُرُّ إِدَارَةُ المَدَارِسِ وَقِسْمُ الرِّيَاضِيَّاتِ أَنْ تَمْنَحَ هَذِهِ الشَّهَادَةَ بِكُلِّ فَخْرٍ وَاعْتِزَازٍ لِلطَّالِبِ الْمُتَأَلِّقِ:
          </p>

          <!-- Student Name Illuminated Cartouche -->
          <div class="student-cartouche">
            <div class="cartouche-title">فَارِسُ الرِّيَاضِيَّاتِ وَالتَّمَيُّز</div>
            <div class="student-name">عبدالعزيز أحمد عبدالعزيز آل عسيس الغامدي</div>
          </div>

          <!-- Achievement Justification Paragraph -->
          <div class="achievement-box">
            <p class="achievement-line">
              نَظِيرَ اجْتِيَازِهِ مَرْحَلَةَ <span class="highlight-term">الرِّيَاضِيَّاتِ 2</span> بِتَمَيُّزٍ وَاقْتِدَارٍ،
            </p>
            <p class="achievement-line">
              وَحُصُولِهِ عَلَى <span class="highlight-score">74 دَرَجَةً</span> فِي <span class="highlight-nasmoo">أولمبياد العلوم والرياضيات الوطني «نَسْمُو»</span>، وَتَأَهُّلِهِ بِجَدَارَةٍ لِلْمَرْحَلَةِ التَّالِيَةِ.
            </p>
          </div>

          <!-- Three Medallion Badges -->
          <div class="medallions-row">
            <!-- Badge 1: Math 2 Pass -->
            <div class="medallion-pill">
              <svg class="medallion-svg" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" fill="#065b6b"/>
                <path d="M7 17L12 7L17 17H7Z" stroke="#ffd700" stroke-width="1.8" fill="none"/>
                <circle cx="12" cy="13" r="1.5" fill="#ffd700"/>
              </svg>
              <span class="medallion-label">اجتياز الرياضيات 2 بتفوق</span>
            </div>

            <!-- Badge 2: Score 74 -->
            <div class="medallion-pill">
              <svg class="medallion-svg" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" fill="#c59b27"/>
                <circle cx="12" cy="12" r="6" stroke="#ffffff" stroke-width="1.8" fill="none"/>
                <circle cx="12" cy="12" r="2.5" fill="#ffffff"/>
              </svg>
              <span class="medallion-label">الدرجة المكتسبة: 74 نقطة</span>
            </div>

            <!-- Badge 3: Qualified Next Stage -->
            <div class="medallion-pill">
              <svg class="medallion-svg" viewBox="0 0 24 24" fill="none">
                <circle cx="12" cy="12" r="10" fill="#065b6b"/>
                <path d="M8 8H16V12C16 14.2 14.2 16 12 16C9.8 16 8 14.2 8 12V8Z" fill="#ffd700"/>
                <path d="M6 9H8V11H6V9ZM16 9H18V11H16V9ZM10 16H14V18H10V16ZM9 18H15V19H9V18Z" fill="#ffd700"/>
              </svg>
              <span class="medallion-label">تأهل باقتدار - أولمبياد نَسْمُو (NESMO)</span>
            </div>
          </div>

          <div class="prayer-statement">
            سائلين المولى عز وجل له دوام التوفيق والارتقاء ومزيداً من التألق والنجاح في مسيرته العلمية المباركة.
          </div>
        </div>

        <!-- SIGNATURES FOOTER -->
        <div class="signatures-section">
          <!-- Right: Subject Teacher -->
          <div class="signature-column">
            <span class="col-title">معلم المادة</span>
            <span class="col-name">أ. محمد عبدالله</span>
            <div class="clean-sig-box"></div>
            <div class="signature-baseline"></div>
            <span class="col-caption">التوقيع والاعتماد</span>
          </div>

          <!-- Middle: Head of Departments -->
          <div class="signature-column">
            <span class="col-title">مدير الأقسام</span>
            <span class="col-name">أ. أنس الجهني</span>
            <div class="clean-sig-box"></div>
            <div class="signature-baseline"></div>
            <span class="col-caption">التوقيع والاعتماد</span>
          </div>

          <!-- Left: General Director -->
          <div class="signature-column">
            <span class="col-title">المدير العام</span>
            <span class="col-name">د. علي الزهراني</span>
            <div class="clean-sig-box"></div>
            <div class="signature-baseline"></div>
            <span class="col-caption">الختم والتوقيع</span>
          </div>

          <!-- Official School Certified Seal -->
          <div class="official-certified-seal">
            <div class="seal-dashed-ring"></div>
            <span class="seal-txt-top">شَرِكَةُ المَدَارِسِ المُتَقَدِّمَة</span>
            <div class="seal-ribbon">أولمبياد نَسْمُو</div>
            <span class="seal-en">NESMO OLYMPIAD</span>
            <span class="seal-stars">★★★★★</span>
            <span class="seal-txt-bottom">تَفَوُّقٌ وَاقْتِدَار</span>
          </div>
        </div>

      </div>
    </div>
  </div>
</div>

</body>
</html>
'''

with open('شهادة_شكر_عبدالعزيز_الغامدي.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated certificate layout to eliminate white space gap!')
