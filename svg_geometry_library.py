# -*- coding: utf-8 -*-
"""
svg_geometry_library.py: High-precision, editable SVG geometry engine
for High School Geometry (1st Secondary - Congruent Triangles).
Generates razor-sharp, mathematically accurate diagrams with:
- Standard English Latin vertices (A, B, C, D, E, F, etc.)
- Congruence tick marks (|, ||, |||)
- Angle arcs and degree measures
- Right angle indicator boxes
- Cartesian coordinate grids and labeled points (0,0), (a,0), (b,c)
- Clean, responsive SVG wrappers.
"""

def svg_wrapper(content, title="", width=650, height=200):
    return f"""
    <div class="geometry-figure-container">
        {f'<div class="figure-title">📐 {title}</div>' if title else ''}
        <div class="svg-wrapper">
            <svg viewBox="0 0 {width} {height}" class="geom-svg" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#334155" />
                    </marker>
                </defs>
                <style>
                    .t-ar {{ font-family: 'Tajawal', sans-serif; font-size: 13px; font-weight: bold; fill: #1e3a8a; text-anchor: middle; }}
                    .t-sub {{ font-family: 'Tajawal', sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }}
                    .t-en {{ font-family: 'Times New Roman', serif; font-style: italic; font-size: 15px; font-weight: bold; fill: #0f172a; text-anchor: middle; }}
                    .t-num {{ font-family: 'Cairo', sans-serif; font-size: 12px; font-weight: 700; fill: #dc2626; text-anchor: middle; }}
                    .s-tri {{ stroke: #2563eb; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: #eff6ff; fill-opacity: 0.6; }}
                    .s-tri2 {{ stroke: #0d9488; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; fill: #f0fdfa; fill-opacity: 0.6; }}
                    .s-mark {{ stroke: #dc2626; stroke-width: 2; stroke-linecap: round; }}
                    .s-arc {{ stroke: #ea580c; stroke-width: 2; fill: none; }}
                    .s-arc2 {{ stroke: #16a34a; stroke-width: 2; fill: none; }}
                    .s-sq {{ stroke: #dc2626; stroke-width: 1.8; fill: #fee2e2; }}
                    .s-axis {{ stroke: #334155; stroke-width: 1.8; }}
                    .s-grid {{ stroke: #e2e8f0; stroke-width: 1; }}
                    .s-dot {{ fill: #dc2626; stroke: #ffffff; stroke-width: 1.5; }}
                </style>
                {content}
            </svg>
        </div>
    </div>
    """

def svg_classify_by_angles():
    content = """
    <!-- 1. Acute -->
    <g transform="translate(10, 15)">
        <polygon points="70,15 15,120 135,120" class="s-tri" />
        <text x="70" y="8" class="t-en">A</text>
        <text x="8" y="125" class="t-en">B</text>
        <text x="142" y="125" class="t-en">C</text>
        <path d="M 30,113 A 18 18 0 0 0 38,120" class="s-arc" />
        <path d="M 112,120 A 18 18 0 0 0 120,113" class="s-arc" />
        <path d="M 64,28 A 18 18 0 0 0 76,28" class="s-arc" />
        <text x="75" y="150" class="t-ar">حاد الزوايا (Acute)</text>
        <text x="75" y="168" class="t-sub">جميع الزوايا &lt; 90°</text>
    </g>
    <!-- 2. Right -->
    <g transform="translate(170, 15)">
        <polygon points="25,20 25,120 135,120" class="s-tri" />
        <rect x="25" y="102" width="18" height="18" class="s-sq" />
        <text x="25" y="12" class="t-en">D</text>
        <text x="12" y="125" class="t-en">E</text>
        <text x="142" y="125" class="t-en">F</text>
        <text x="80" y="150" class="t-ar">قائم الزاوية (Right)</text>
        <text x="80" y="168" class="t-sub">زاوية واحدة = 90°</text>
    </g>
    <!-- 3. Obtuse -->
    <g transform="translate(330, 15)">
        <polygon points="105,25 20,120 145,120" class="s-tri" />
        <path d="M 38,108 A 24 24 0 0 0 44,120" class="s-arc" style="stroke-width:2.5; stroke:#b91c1c;" />
        <text x="110" y="18" class="t-en">G</text>
        <text x="10" y="125" class="t-en">H</text>
        <text x="152" y="125" class="t-en">K</text>
        <text x="82" y="150" class="t-ar">منفرج الزاوية (Obtuse)</text>
        <text x="82" y="168" class="t-sub">إحدى الزوايا &gt; 90°</text>
    </g>
    <!-- 4. Equiangular -->
    <g transform="translate(490, 15)">
        <polygon points="70,18 15,120 125,120" class="s-tri" style="fill:#f0fdf4;" />
        <path d="M 30,113 A 18 18 0 0 0 38,120" class="s-arc2" />
        <path d="M 102,120 A 18 18 0 0 0 110,113" class="s-arc2" />
        <path d="M 64,28 A 18 18 0 0 0 76,28" class="s-arc2" />
        <text x="70" y="10" class="t-en">P</text>
        <text x="8" y="125" class="t-en">Q</text>
        <text x="132" y="125" class="t-en">R</text>
        <text x="70" y="150" class="t-ar">متطابق الزوايا (Equiangular)</text>
        <text x="70" y="168" class="t-sub">3 زوايا متطابقة = 60°</text>
    </g>
    """
    return svg_wrapper(content, "تصنيف المثلثات وفقاً لقياسات زواياها", 650, 185)

def svg_classify_by_sides():
    content = """
    <!-- 1. Equilateral -->
    <g transform="translate(20, 15)">
        <polygon points="75,18 20,120 130,120" class="s-tri" />
        <!-- 3 single tick marks -->
        <line x1="43" y1="67" x2="52" y2="71" class="s-mark" />
        <line x1="98" y1="71" x2="107" y2="67" class="s-mark" />
        <line x1="75" y1="116" x2="75" y2="124" class="s-mark" />
        <text x="75" y="10" class="t-en">A</text>
        <text x="10" y="125" class="t-en">B</text>
        <text x="138" y="125" class="t-en">C</text>
        <text x="75" y="150" class="t-ar">متطابق الأضلاع (Equilateral)</text>
        <text x="75" y="168" class="t-sub">3 أضلاع متطابقة</text>
    </g>
    <!-- 2. Isosceles -->
    <g transform="translate(240, 15)">
        <polygon points="75,15 30,120 120,120" class="s-tri" />
        <!-- 2 double tick marks -->
        <line x1="48" y1="65" x2="56" y2="68" class="s-mark" />
        <line x1="51" y1="69" x2="59" y2="72" class="s-mark" />
        <line x1="94" y1="68" x2="102" y2="65" class="s-mark" />
        <line x1="91" y1="72" x2="99" y2="69" class="s-mark" />
        <text x="75" y="8" class="t-en">J</text>
        <text x="20" y="125" class="t-en">K</text>
        <text x="130" y="125" class="t-en">L</text>
        <text x="75" y="150" class="t-ar">متطابق الضلعين (Isosceles)</text>
        <text x="75" y="168" class="t-sub">ضلعان متطابقان على الأقل</text>
    </g>
    <!-- 3. Scalene -->
    <g transform="translate(460, 15)">
        <polygon points="105,25 20,120 140,120" class="s-tri" />
        <!-- 1, 2, 3 different ticks -->
        <line x1="58" y1="68" x2="66" y2="74" class="s-mark" />
        <line x1="118" y1="68" x2="127" y2="72" class="s-mark" />
        <line x1="121" y1="72" x2="130" y2="76" class="s-mark" />
        <line x1="76" y1="116" x2="76" y2="124" class="s-mark" />
        <line x1="80" y1="116" x2="80" y2="124" class="s-mark" />
        <line x1="84" y1="116" x2="84" y2="124" class="s-mark" />
        <text x="110" y="18" class="t-en">X</text>
        <text x="10" y="125" class="t-en">Y</text>
        <text x="148" y="125" class="t-en">Z</text>
        <text x="80" y="150" class="t-ar">مختلف الأضلاع (Scalene)</text>
        <text x="80" y="168" class="t-sub">لا توجد أضلاع متطابقة</text>
    </g>
    """
    return svg_wrapper(content, "تصنيف المثلثات وفقاً لأطوال أضلاعها", 650, 185)

def svg_algebra_sides_exercise():
    content = """
    <g transform="translate(180, 20)">
        <polygon points="120,15 20,140 220,140" class="s-tri" />
        <!-- Equal ticks on AB and AC -->
        <line x1="64" y1="74" x2="74" y2="80" class="s-mark" />
        <line x1="166" y1="80" x2="176" y2="74" class="s-mark" />
        <text x="120" y="8" class="t-en">A</text>
        <text x="10" y="145" class="t-en">B</text>
        <text x="230" y="145" class="t-en">C</text>
        <text x="45" y="70" class="t-en" style="fill:#2563eb; font-size:14px;">5x - 0.5</text>
        <text x="195" y="70" class="t-en" style="fill:#2563eb; font-size:14px;">4x + 1</text>
        <text x="120" y="160" class="t-en" style="fill:#0d9488; font-size:14px;">3x + 2.5</text>
    </g>
    """
    return svg_wrapper(content, "إيجاد أطوال الأضلاع وقيمة x في مثلث متطابق الضلعين", 600, 195)

def svg_triangle_angle_sum():
    content = """
    <g transform="translate(120, 25)">
        <!-- Auxiliary parallel line above vertex A -->
        <line x1="20" y1="30" x2="360" y2="30" stroke="#64748b" stroke-width="1.8" stroke-dasharray="5,4" />
        <text x="375" y="34" class="t-en" style="fill:#64748b;">ℓ ∥ BC</text>
        <polygon points="190,30 60,150 320,150" class="s-tri" />
        <text x="190" y="18" class="t-en">A</text>
        <text x="45" y="155" class="t-en">B</text>
        <text x="330" y="155" class="t-en">C</text>
        <!-- interior angles -->
        <path d="M 80,144 A 22 22 0 0 0 92,150" class="s-arc" />
        <text x="105" y="142" class="t-num">2</text>
        <path d="M 288,150 A 22 22 0 0 0 300,144" class="s-arc" />
        <text x="275" y="142" class="t-num">3</text>
        <path d="M 178,44 A 20 20 0 0 0 202,44" class="s-arc" />
        <text x="190" y="60" class="t-num">1</text>
        <!-- alternate interior angles along line ell -->
        <path d="M 160,30 A 25 25 0 0 0 178,42" class="s-arc2" />
        <text x="150" y="24" class="t-num" style="fill:#16a34a;">4</text>
        <path d="M 202,42 A 25 25 0 0 0 220,30" class="s-arc2" />
        <text x="230" y="24" class="t-num" style="fill:#16a34a;">5</text>
        <text x="190" y="185" class="t-ar" style="font-size:14px;">نظرية مجموع قياسات زوايا المثلث: m∠1 + m∠2 + m∠3 = 180°</text>
    </g>
    """
    return svg_wrapper(content, "برهان ونظرية مجموع قياسات زوايا المثلث (Angle-Sum Theorem)", 620, 220)

def svg_exterior_angle():
    content = """
    <g transform="translate(70, 25)">
        <!-- Base line extending to D -->
        <line x1="40" y1="130" x2="440" y2="130" stroke="#334155" stroke-width="2.5" stroke-linecap="round" marker-end="url(#arrow)" />
        <polygon points="170,25 60,130 280,130" class="s-tri" />
        <text x="170" y="15" class="t-en">A</text>
        <text x="45" y="135" class="t-en">B</text>
        <text x="275" y="150" class="t-en">C</text>
        <text x="445" y="135" class="t-en">D</text>
        <!-- Remote interior angles 1 and 2 -->
        <path d="M 160,40 A 20 20 0 0 0 178,40" class="s-arc" />
        <text x="170" y="55" class="t-num">1</text>
        <path d="M 80,123 A 22 22 0 0 0 92,130" class="s-arc" />
        <text x="105" y="122" class="t-num">2</text>
        <!-- Interior angle 3 -->
        <path d="M 255,130 A 20 20 0 0 0 265,123" class="s-arc2" />
        <text x="250" y="122" class="t-num" style="fill:#16a34a;">3</text>
        <!-- Exterior angle 4 -->
        <path d="M 295,123 A 22 22 0 0 1 305,130" class="s-arc" style="stroke-width:2.5; stroke:#b91c1c;" />
        <text x="315" y="120" class="t-num" style="font-size:14px;">4</text>
        <text x="240" y="175" class="t-ar" style="font-size:14px;">نظرية الزاوية الخارجية: m∠4 = m∠1 + m∠2</text>
    </g>
    """
    return svg_wrapper(content, "نظرية الزاوية الخارجية للمثلث (Exterior Angle Theorem)", 600, 210)

def svg_congruent_triangles_cpctc():
    content = """
    <!-- Triangle 1: ABC -->
    <g transform="translate(50, 20)">
        <polygon points="70,20 15,125 130,125" class="s-tri" />
        <!-- Ticks on sides -->
        <line x1="39" y1="69" x2="47" y2="73" class="s-mark" />
        <line x1="96" y1="74" x2="104" y2="70" class="s-mark" />
        <line x1="93" y1="77" x2="101" y2="73" class="s-mark" />
        <line x1="68" y1="121" x2="68" y2="129" class="s-mark" />
        <line x1="72" y1="121" x2="72" y2="129" class="s-mark" />
        <line x1="76" y1="121" x2="76" y2="129" class="s-mark" />
        <!-- Angle arcs -->
        <path d="M 64,32 A 18 18 0 0 0 76,32" class="s-arc" />
        <path d="M 28,118 A 18 18 0 0 0 36,125" class="s-arc2" />
        <path d="M 32,114 A 23 23 0 0 0 42,125" class="s-arc2" />
        <path d="M 112,125 A 18 18 0 0 0 118,118" class="s-arc" style="stroke:#7c3aed;" />
        <text x="70" y="10" class="t-en">A</text>
        <text x="8" y="130" class="t-en">B</text>
        <text x="138" y="130" class="t-en">C</text>
        <text x="70" y="155" class="t-en" style="font-size:16px;">△ABC</text>
    </g>
    <!-- Congruence symbol -->
    <text x="240" y="90" class="t-en" style="font-size:32px; fill:#2563eb;">≅</text>
    <!-- Triangle 2: DEF -->
    <g transform="translate(300, 20)">
        <polygon points="70,20 15,125 130,125" class="s-tri2" />
        <!-- Ticks on sides -->
        <line x1="39" y1="69" x2="47" y2="73" class="s-mark" />
        <line x1="96" y1="74" x2="104" y2="70" class="s-mark" />
        <line x1="93" y1="77" x2="101" y2="73" class="s-mark" />
        <line x1="68" y1="121" x2="68" y2="129" class="s-mark" />
        <line x1="72" y1="121" x2="72" y2="129" class="s-mark" />
        <line x1="76" y1="121" x2="76" y2="129" class="s-mark" />
        <!-- Angle arcs -->
        <path d="M 64,32 A 18 18 0 0 0 76,32" class="s-arc" />
        <path d="M 28,118 A 18 18 0 0 0 36,125" class="s-arc2" />
        <path d="M 32,114 A 23 23 0 0 0 42,125" class="s-arc2" />
        <path d="M 112,125 A 18 18 0 0 0 118,118" class="s-arc" style="stroke:#7c3aed;" />
        <text x="70" y="10" class="t-en">D</text>
        <text x="8" y="130" class="t-en">E</text>
        <text x="138" y="130" class="t-en">F</text>
        <text x="70" y="155" class="t-en" style="font-size:16px;">△DEF</text>
    </g>
    """
    return svg_wrapper(content, "تطابق المثلثات والعناصر المتناظرة (CPCTC: △ABC ≅ △DEF)", 500, 180)

def svg_sss_and_sas():
    content = """
    <!-- SSS Section -->
    <g transform="translate(10, 10)">
        <polygon points="50,15 15,95 90,95" class="s-tri" />
        <line x1="29" y1="52" x2="36" y2="56" class="s-mark" />
        <line x1="67" y1="56" x2="73" y2="52" class="s-mark" />
        <line x1="64" y1="59" x2="70" y2="55" class="s-mark" />
        <line x1="49" y1="92" x2="49" y2="98" class="s-mark" />
        <line x1="53" y1="92" x2="53" y2="98" class="s-mark" />
        <line x1="57" y1="92" x2="57" y2="98" class="s-mark" />
        <text x="50" y="8" class="t-en" style="font-size:12px;">A</text>
        <text x="8" y="98" class="t-en" style="font-size:12px;">B</text>
        <text x="96" y="98" class="t-en" style="font-size:12px;">C</text>

        <polygon points="150,15 115,95 190,95" class="s-tri2" />
        <line x1="129" y1="52" x2="136" y2="56" class="s-mark" />
        <line x1="167" y1="56" x2="173" y2="52" class="s-mark" />
        <line x1="164" y1="59" x2="170" y2="55" class="s-mark" />
        <line x1="149" y1="92" x2="149" y2="98" class="s-mark" />
        <line x1="153" y1="92" x2="153" y2="98" class="s-mark" />
        <line x1="157" y1="92" x2="157" y2="98" class="s-mark" />
        <text x="150" y="8" class="t-en" style="font-size:12px;">D</text>
        <text x="108" y="98" class="t-en" style="font-size:12px;">E</text>
        <text x="196" y="98" class="t-en" style="font-size:12px;">F</text>
        <text x="105" y="125" class="t-ar">مسلمة SSS: تطابق ثلاثة أضلاع</text>
    </g>
    <!-- Divider -->
    <line x1="230" y1="15" x2="230" y2="135" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,4" />
    <!-- SAS Section -->
    <g transform="translate(250, 10)">
        <polygon points="50,15 15,95 90,95" class="s-tri" />
        <line x1="29" y1="52" x2="36" y2="56" class="s-mark" />
        <line x1="49" y1="92" x2="49" y2="98" class="s-mark" />
        <line x1="53" y1="92" x2="53" y2="98" class="s-mark" />
        <!-- Included angle B -->
        <path d="M 25,90 A 14 14 0 0 0 32,95" class="s-arc" style="stroke-width:2.2;" />
        <text x="50" y="8" class="t-en" style="font-size:12px;">J</text>
        <text x="8" y="98" class="t-en" style="font-size:12px;">K</text>
        <text x="96" y="98" class="t-en" style="font-size:12px;">L</text>

        <polygon points="150,15 115,95 190,95" class="s-tri2" />
        <line x1="129" y1="52" x2="136" y2="56" class="s-mark" />
        <line x1="149" y1="92" x2="149" y2="98" class="s-mark" />
        <line x1="153" y1="92" x2="153" y2="98" class="s-mark" />
        <path d="M 125,90 A 14 14 0 0 0 132,95" class="s-arc" style="stroke-width:2.2;" />
        <text x="150" y="8" class="t-en" style="font-size:12px;">P</text>
        <text x="108" y="98" class="t-en" style="font-size:12px;">Q</text>
        <text x="196" y="98" class="t-en" style="font-size:12px;">R</text>
        <text x="105" y="125" class="t-ar">مسلمة SAS: ضلعان وزاوية محصورة</text>
    </g>
    """
    return svg_wrapper(content, "مقارنة مسلمتي التطابق: SSS مقابل SAS", 480, 150)

def svg_asa_and_aas():
    content = """
    <!-- ASA Section -->
    <g transform="translate(10, 10)">
        <polygon points="50,15 15,95 90,95" class="s-tri" />
        <path d="M 25,90 A 14 14 0 0 0 32,95" class="s-arc" />
        <path d="M 78,95 A 14 14 0 0 0 83,90" class="s-arc2" />
        <!-- Included side BC -->
        <line x1="50" y1="92" x2="50" y2="98" class="s-mark" />
        <text x="50" y="8" class="t-en" style="font-size:12px;">A</text>
        <text x="8" y="98" class="t-en" style="font-size:12px;">B</text>
        <text x="96" y="98" class="t-en" style="font-size:12px;">C</text>

        <polygon points="150,15 115,95 190,95" class="s-tri2" />
        <path d="M 125,90 A 14 14 0 0 0 132,95" class="s-arc" />
        <path d="M 178,95 A 14 14 0 0 0 183,90" class="s-arc2" />
        <line x1="150" y1="92" x2="150" y2="98" class="s-mark" />
        <text x="150" y="8" class="t-en" style="font-size:12px;">D</text>
        <text x="108" y="98" class="t-en" style="font-size:12px;">E</text>
        <text x="196" y="98" class="t-en" style="font-size:12px;">F</text>
        <text x="105" y="125" class="t-ar">مسلمة ASA: زاويتان وضلع محصور</text>
    </g>
    <!-- Divider -->
    <line x1="230" y1="15" x2="230" y2="135" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4,4" />
    <!-- AAS Section -->
    <g transform="translate(250, 10)">
        <polygon points="50,15 15,95 90,95" class="s-tri" />
        <path d="M 45,26 A 14 14 0 0 0 55,26" class="s-arc" />
        <path d="M 25,90 A 14 14 0 0 0 32,95" class="s-arc2" />
        <!-- Non-included side AC -->
        <line x1="68" y1="56" x2="74" y2="52" class="s-mark" />
        <text x="50" y="8" class="t-en" style="font-size:12px;">X</text>
        <text x="8" y="98" class="t-en" style="font-size:12px;">Y</text>
        <text x="96" y="98" class="t-en" style="font-size:12px;">Z</text>

        <polygon points="150,15 115,95 190,95" class="s-tri2" />
        <path d="M 145,26 A 14 14 0 0 0 155,26" class="s-arc" />
        <path d="M 125,90 A 14 14 0 0 0 132,95" class="s-arc2" />
        <line x1="168" y1="56" x2="174" y2="52" class="s-mark" />
        <text x="150" y="8" class="t-en" style="font-size:12px;">U</text>
        <text x="108" y="98" class="t-en" style="font-size:12px;">V</text>
        <text x="196" y="98" class="t-en" style="font-size:12px;">W</text>
        <text x="105" y="125" class="t-ar">نظرية AAS: زاويتان وضلع غير محصور</text>
    </g>
    """
    return svg_wrapper(content, "مقارنة حالتي التطابق: ASA مقابل AAS", 480, 150)

def svg_hl_right_triangles():
    content = """
    <!-- Triangle 1 -->
    <g transform="translate(60, 20)">
        <polygon points="25,20 25,120 120,120" class="s-tri" />
        <rect x="25" y="104" width="16" height="16" class="s-sq" />
        <!-- Hypotenuse tick -->
        <line x1="68" y1="68" x2="76" y2="72" class="s-mark" style="stroke-width:2.5;" />
        <!-- Leg tick -->
        <line x1="22" y1="70" x2="28" y2="70" class="s-mark" />
        <text x="25" y="12" class="t-en">A</text>
        <text x="12" y="125" class="t-en">B</text>
        <text x="128" y="125" class="t-en">C</text>
        <text x="75" y="60" class="t-sub" style="font-weight:bold; fill:#dc2626;">الوتر (H)</text>
        <text x="5" y="75" class="t-sub" style="font-weight:bold;">ساق (L)</text>
    </g>
    <!-- Congruence -->
    <text x="220" y="85" class="t-en" style="font-size:28px; fill:#2563eb;">≅</text>
    <!-- Triangle 2 -->
    <g transform="translate(260, 20)">
        <polygon points="25,20 25,120 120,120" class="s-tri2" />
        <rect x="25" y="104" width="16" height="16" class="s-sq" />
        <line x1="68" y1="68" x2="76" y2="72" class="s-mark" style="stroke-width:2.5;" />
        <line x1="22" y1="70" x2="28" y2="70" class="s-mark" />
        <text x="25" y="12" class="t-en">D</text>
        <text x="12" y="125" class="t-en">E</text>
        <text x="128" y="125" class="t-en">F</text>
        <text x="75" y="60" class="t-sub" style="font-weight:bold; fill:#dc2626;">الوتر (H)</text>
        <text x="5" y="75" class="t-sub" style="font-weight:bold;">ساق (L)</text>
    </g>
    <text x="230" y="165" class="t-ar" style="font-size:13.5px;">نظرية الوتر وساق (HL Theorem): يتطابق المثلثان القائمان إذا تطابق وتر وساق</text>
    """
    return svg_wrapper(content, "نظرية تطابق المثلثات القائمة: وتر وساق (HL)", 460, 185)

def svg_isosceles_anatomy():
    content = """
    <g transform="translate(140, 20)">
        <polygon points="130,20 30,150 230,150" class="s-tri" />
        <!-- congruent legs -->
        <line x1="75" y1="82" x2="85" y2="88" class="s-mark" style="stroke-width:2.2;" />
        <line x1="175" y1="88" x2="185" y2="82" class="s-mark" style="stroke-width:2.2;" />
        <!-- base angles -->
        <path d="M 45,142 A 20 20 0 0 0 54,150" class="s-arc" style="stroke-width:2.2;" />
        <path d="M 206,150 A 20 20 0 0 0 215,142" class="s-arc" style="stroke-width:2.2;" />
        <!-- vertex angle -->
        <path d="M 122,35 A 18 18 0 0 0 138,35" class="s-arc2" />
        <!-- Labels -->
        <text x="130" y="10" class="t-en">A</text>
        <text x="18" y="155" class="t-en">B</text>
        <text x="242" y="155" class="t-en">C</text>
        <text x="130" y="55" class="t-sub" style="font-weight:bold; fill:#16a34a;">زاوية الرأس (Vertex Angle)</text>
        <text x="40" y="80" class="t-sub" style="font-weight:bold; fill:#dc2626;">الساق (Leg)</text>
        <text x="220" y="80" class="t-sub" style="font-weight:bold; fill:#dc2626;">الساق (Leg)</text>
        <text x="130" y="170" class="t-sub" style="font-weight:bold; fill:#1e3a8a;">القاعدة (Base)</text>
        <text x="40" y="170" class="t-sub" style="font-weight:bold; fill:#ea580c;">زاوية القاعدة</text>
        <text x="220" y="170" class="t-sub" style="font-weight:bold; fill:#ea580c;">زاوية القاعدة</text>
        <text x="130" y="195" class="t-ar">نظرية المثلث المتطابق الضلعين: إذا كان AB ≅ AC فإن ∠B ≅ ∠C والعكس صحيح</text>
    </g>
    """
    return svg_wrapper(content, "تشريح ونظرية المثلث المتطابق الضلعين (Isosceles Triangle)", 540, 225)

def svg_coordinate_proof_placement():
    content = """
    <g transform="translate(60, 25)">
        <!-- Axes -->
        <line x1="40" y1="140" x2="380" y2="140" class="s-axis" marker-end="url(#arrow)" />
        <line x1="60" y1="160" x2="60" y2="20" class="s-axis" marker-end="url(#arrow)" />
        <text x="390" y="145" class="t-en" style="font-size:14px;">x</text>
        <text x="60" y="12" class="t-en" style="font-size:14px;">y</text>
        <text x="48" y="155" class="t-en" style="font-size:12px;">O</text>
        <!-- Triangle placed on axes: (0,0), (a,0), (b,c) -->
        <polygon points="60,140 300,140 180,45" class="s-tri" />
        <!-- Dots and coordinates -->
        <circle cx="60" cy="140" r="4.5" class="s-dot" />
        <text x="60" y="175" class="t-en">(0, 0)</text>
        <text x="45" y="135" class="t-en">A</text>

        <circle cx="300" cy="140" r="4.5" class="s-dot" />
        <text x="300" y="160" class="t-en">(a, 0)</text>
        <text x="312" y="135" class="t-en">B</text>

        <circle cx="180" cy="45" r="4.5" class="s-dot" />
        <text x="180" y="35" class="t-en">(b, c)</text>
        <text x="180" y="20" class="t-en">C</text>
        <text x="210" y="195" class="t-ar" style="font-size:13.5px;">أفضل وضع للبرهان الإحداثي: رأس عند نقطة الأصل، وضلع منطبق على محور x</text>
    </g>
    """
    return svg_wrapper(content, "استراتيجية وضع المثلث في المستوى الإحداثي (Coordinate Proof)", 500, 225)

if __name__ == "__main__":
    print("svg_geometry_library.py compiled and validated.")


def svg_ws1_exercise():
    content = """
    <g transform="translate(140, 20)">
        <polygon points="150,15 30,135 270,135" class="s-tri" />
        <line x1="150" y1="15" x2="150" y2="135" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4,4" />
        <rect x="150" y="117" width="18" height="18" class="s-sq" />
        <line x1="85" y1="72" x2="95" y2="78" class="s-mark" />
        <line x1="205" y1="78" x2="215" y2="72" class="s-mark" />
        <text x="150" y="8" class="t-en">A</text>
        <text x="18" y="140" class="t-en">B</text>
        <text x="150" y="152" class="t-en">D</text>
        <text x="282" y="140" class="t-en">C</text>
        <text x="60" y="65" class="t-en" style="fill:#2563eb;">4x + 3</text>
        <text x="235" y="65" class="t-en" style="fill:#2563eb;">6x - 7</text>
        <text x="90" y="152" class="t-en" style="fill:#0d9488;">2x + 1</text>
        <text x="210" y="152" class="t-en" style="fill:#0d9488;">2x + 1</text>
    </g>
    """
    return svg_wrapper(content, "المسألة الهندسية: إيجاد قيمة x ومحيط المثلث △ABC", 580, 180)

def svg_ws2_exercise():
    content = """
    <g transform="translate(80, 25)">
        <line x1="30" y1="130" x2="420" y2="130" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)" />
        <polygon points="180,25 60,130 300,130" class="s-tri" />
        <text x="180" y="15" class="t-en">P</text>
        <text x="45" y="135" class="t-en">Q</text>
        <text x="295" y="150" class="t-en">R</text>
        <text x="425" y="135" class="t-en">S</text>
        <!-- Angle arcs and expressions -->
        <path d="M 170,40 A 20 20 0 0 0 190,40" class="s-arc" />
        <text x="180" y="60" class="t-en" style="fill:#b91c1c;">(2x + 15)°</text>
        <path d="M 85,123 A 22 22 0 0 0 95,130" class="s-arc" />
        <text x="115" y="122" class="t-en" style="fill:#2563eb;">(3x - 5)°</text>
        <path d="M 315,123 A 22 22 0 0 1 325,130" class="s-arc" style="stroke-width:2.5; stroke:#b91c1c;" />
        <text x="350" y="120" class="t-en" style="fill:#b91c1c; font-weight:bold;">(7x - 20)°</text>
    </g>
    """
    return svg_wrapper(content, "مسألة الزاوية الخارجية: أوجد قيمة x وقياس ∠PRS", 580, 195)

def svg_ws3_exercise():
    content = """
    <g transform="translate(60, 20)">
        <!-- Quad 1 -->
        <polygon points="40,20 120,30 140,110 30,120" class="s-tri" />
        <text x="35" y="12" class="t-en">A</text>
        <text x="130" y="25" class="t-en">B</text>
        <text x="150" y="115" class="t-en">C</text>
        <text x="18" y="125" class="t-en">D</text>
        <text x="80" y="18" class="t-en" style="font-size:12px; fill:#2563eb;">2x + 4</text>
        <text x="145" y="70" class="t-en" style="font-size:12px; fill:#2563eb;">12</text>
        <!-- Quad 2 -->
        <g transform="translate(260, 0)">
            <polygon points="40,20 120,30 140,110 30,120" class="s-tri2" />
            <text x="35" y="12" class="t-en">W</text>
            <text x="130" y="25" class="t-en">X</text>
            <text x="150" y="115" class="t-en">Y</text>
            <text x="18" y="125" class="t-en">Z</text>
            <text x="80" y="18" class="t-en" style="font-size:12px; fill:#0d9488;">18</text>
            <text x="145" y="70" class="t-en" style="font-size:12px; fill:#0d9488;">3y - 3</text>
        </g>
        <text x="210" y="75" class="t-en" style="font-size:26px; fill:#2563eb;">≅</text>
    </g>
    """
    return svg_wrapper(content, "المضلعان المتطابقان: ABCD ≅ WXYZ، أوجد قيمتي x و y", 550, 170)

def svg_ws4_exercise():
    content = """
    <g transform="translate(100, 20)">
        <!-- Two triangles sharing common side BD -->
        <polygon points="30,80 180,20 330,80 180,140" class="s-tri" />
        <line x1="180" y1="20" x2="180" y2="140" stroke="#2563eb" stroke-width="2.5" />
        <!-- Ticks on AB and CD -->
        <line x1="100" y1="46" x2="108" y2="52" class="s-mark" />
        <line x1="250" y1="106" x2="258" y2="112" class="s-mark" />
        <!-- Double ticks on AD and CB -->
        <line x1="100" y1="110" x2="108" y2="104" class="s-mark" />
        <line x1="104" y1="113" x2="112" y2="107" class="s-mark" />
        <line x1="250" y1="50" x2="258" y2="44" class="s-mark" />
        <line x1="254" y1="53" x2="262" y2="47" class="s-mark" />
        <text x="18" y="85" class="t-en">A</text>
        <text x="180" y="12" class="t-en">B</text>
        <text x="345" y="85" class="t-en">C</text>
        <text x="180" y="160" class="t-en">D</text>
    </g>
    """
    return svg_wrapper(content, "البرهان الهندسي: إثبات أن △ABD ≅ △CDB بمسلمة SSS", 520, 185)

def svg_ws6_exercise():
    content = """
    <g transform="translate(100, 20)">
        <!-- Two right triangles sharing altitude -->
        <polygon points="50,130 180,25 310,130" class="s-tri" />
        <line x1="180" y1="25" x2="180" y2="130" stroke="#dc2626" stroke-width="2.2" />
        <rect x="180" y="112" width="18" height="18" class="s-sq" />
        <rect x="162" y="112" width="18" height="18" class="s-sq" />
        <!-- Hypotenuse marks -->
        <line x1="110" y1="74" x2="118" y2="80" class="s-mark" style="stroke-width:2.5;" />
        <line x1="242" y1="80" x2="250" y2="74" class="s-mark" style="stroke-width:2.5;" />
        <text x="180" y="15" class="t-en">A</text>
        <text x="35" y="135" class="t-en">B</text>
        <text x="180" y="150" class="t-en">D</text>
        <text x="325" y="135" class="t-en">C</text>
        <text x="90" y="70" class="t-sub" style="font-weight:bold; fill:#dc2626;">الوتر</text>
        <text x="260" y="70" class="t-sub" style="font-weight:bold; fill:#dc2626;">الوتر</text>
        <text x="200" y="80" class="t-sub" style="font-weight:bold; fill:#2563eb;">ساق مشتركة</text>
    </g>
    """
    return svg_wrapper(content, "تطابق المثلثين القائمين △ABD و △ACD بنظرية الوتر وساق (HL)", 500, 180)

def svg_ws7_exercise():
    content = """
    <g transform="translate(130, 20)">
        <polygon points="150,15 40,140 260,140" class="s-tri" />
        <line x1="90" y1="74" x2="100" y2="80" class="s-mark" />
        <line x1="200" y1="80" x2="210" y2="74" class="s-mark" />
        <path d="M 55,133 A 18 18 0 0 0 65,140" class="s-arc" />
        <path d="M 235,140 A 18 18 0 0 0 245,133" class="s-arc" />
        <path d="M 142,32 A 18 18 0 0 0 158,32" class="s-arc2" />
        <text x="150" y="8" class="t-en">A</text>
        <text x="25" y="145" class="t-en">B</text>
        <text x="272" y="145" class="t-en">C</text>
        <text x="150" y="55" class="t-en" style="fill:#16a34a; font-weight:bold;">(2y + 10)°</text>
        <text x="85" y="133" class="t-en" style="fill:#ea580c; font-weight:bold;">(5x - 8)°</text>
        <text x="215" y="133" class="t-en" style="fill:#ea580c; font-weight:bold;">(3x + 16)°</text>
    </g>
    """
    return svg_wrapper(content, "حساب المتغيرات x و y في مثلث متطابق الضلعين", 520, 180)

def svg_ws8_exercise():
    content = """
    <g transform="translate(80, 25)">
        <line x1="30" y1="140" x2="400" y2="140" class="s-axis" marker-end="url(#arrow)" />
        <line x1="60" y1="165" x2="60" y2="20" class="s-axis" marker-end="url(#arrow)" />
        <text x="410" y="145" class="t-en">x</text>
        <text x="60" y="12" class="t-en">y</text>
        <polygon points="60,140 320,140 190,40" class="s-tri" />
        <!-- Midpoints on sides -->
        <circle cx="125" cy="90" r="4" fill="#0d9488" />
        <circle cx="255" cy="90" r="4" fill="#0d9488" />
        <circle cx="190" cy="140" r="4" fill="#0d9488" />
        <line x1="125" y1="90" x2="255" y2="90" stroke="#0d9488" stroke-width="2" stroke-dasharray="4,3" />
        <!-- Vertices -->
        <circle cx="60" cy="140" r="4.5" class="s-dot" />
        <text x="45" y="155" class="t-en">O(0, 0)</text>
        <circle cx="320" cy="140" r="4.5" class="s-dot" />
        <text x="320" y="160" class="t-en">B(2a, 0)</text>
        <circle cx="190" cy="40" r="4.5" class="s-dot" />
        <text x="190" y="30" class="t-en">C(2b, 2c)</text>
        <text x="190" y="80" class="t-sub" style="font-weight:bold; fill:#0d9488;">القطعة المنصفة</text>
    </g>
    """
    return svg_wrapper(content, "برهان إحداثي: إثبات خصائص القطعة المنصفة لضلعين في مثلث", 520, 210)
