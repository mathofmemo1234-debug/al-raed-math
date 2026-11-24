/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات
 * مولد الصفحات التفاعلية المستقلة لكل درس بصيغة HTML (Interactive HTML Lesson Generator)
 * ينتج ملفات HTML قائمة بذاتها تعمل دون اتصال (Offline-first) مع محاورة سقراطية
 * واختبار ذاتي تفاعلي مصحح آلياً وبطاقات الشرح الميداني الشامل
 * إشراف خبير الرياضيات: أ. محمد عبدالله جمعة | المدارس المتقدمة للتعلم الذكي
 * ==========================================================================
 */

(function (global) {
  'use strict';

  // Helper: Convert English digits to Eastern Arabic digits if needed
  function toEasternArabicNumerals(str) {
    if (str === null || str === undefined) return '';
    const s = String(str);
    return s.replace(/[0-9]/g, function (w) {
      return String.fromCharCode(0x0660 + parseInt(w, 10));
    });
  }

  function toWesternNumerals(str) {
    if (str === null || str === undefined) return '';
    return String(str).replace(/[٠-٩]/g, function (w) {
      return String(w.charCodeAt(0) - 0x0660);
    });
  }

  // Format clean math expression (No carets ^, clean superscripts, LTR math for secondary)
  function formatMathDisplay(text, isArabicNumerals) {
    if (text === null || text === undefined || text === '') return '';
    let res = String(text);
    if (!isArabicNumerals) {
      if (global.ArabicUtils && typeof global.ArabicUtils.renderMathHtml === 'function') {
        return global.ArabicUtils.renderMathHtml(res, true);
      }
      res = toWesternNumerals(res);
      res = res.replace(/\^2/g, '²').replace(/\^3/g, '³').replace(/\^(\d+)/g, '($1)');
      return escapeHtml(res);
    }
    res = toEasternArabicNumerals(res);
    // Clean any accidental carets
    res = res.replace(/\^2/g, '²').replace(/\^3/g, '³').replace(/\^(\d+)/g, '($1)');
    return res;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Check whether lesson belongs to primary or intermediate (requires Eastern Arabic numerals)
  function isArabicStageLesson(lesson) {
    if (!lesson) return true;
    if (lesson.gradeId === 'g1s' || lesson.stageId === 'secondary') return false;
    if (global.ArabicUtils && typeof global.ArabicUtils.isSecondaryStage === 'function' && global.ArabicUtils.isSecondaryStage(lesson)) {
      return false;
    }
    const lid = (lesson.id || '').toLowerCase();
    if (lid.startsWith('g1s') || lid.startsWith('g2s') || lid.startsWith('g3s') || lid.includes('sec')) {
      return false;
    }
    return true;
  }

  /**
   * Main Generator Function: Produces a 100% self-contained interactive HTML string
   */
  function buildStandaloneLessonHtml(lesson) {
    if (!lesson) return '';

    const isArabicNum = isArabicStageLesson(lesson);
    const numFmt = (n) => isArabicNum ? toEasternArabicNumerals(n) : toWesternNumerals(n);

    // Get 6-station field lesson prep if LessonPrepManager is available
    let prep = null;
    if (global.LessonPrepManager && typeof global.LessonPrepManager.getLessonPrep === 'function') {
      prep = global.LessonPrepManager.getLessonPrep(lesson);
    }

    const quiz = lesson.quiz || { mcq: [], tf: [], essay: [] };
    const mcqs = quiz.mcq || [];
    const tfs = quiz.tf || [];
    const essays = quiz.essay || [];

    const summary = lesson.summary || { concept: '', methods: [], golden_rule: '', examples: [] };
    const socratic = lesson.socratic || { introduction: '', dialogue: [], conclusion: '' };
    const worksheet = lesson.worksheet || { exploratory: '', exercises: [], reflection: '' };

    // Format lesson metadata
    const lessonTitle = escapeHtml(numFmt(lesson.title || 'درس رياضيات'));
    const lessonNumber = numFmt(lesson.number || '1');
    const lessonPages = numFmt(lesson.pages || 'غير محدد');

    // Socratic steps JSON serialized for embedding
    const socraticSteps = (socratic.dialogue || []).map((step, idx) => ({
      stepNum: idx + 1,
      question: formatMathDisplay(step.question || '', isArabicNum),
      expectedAnswer: formatMathDisplay(step.expected_student_response || step.expectedAnswer || '', isArabicNum),
      socraticFeedback: formatMathDisplay(step.socratic_response || step.feedback || '', isArabicNum),
      pedagogicalGoal: formatMathDisplay(step.pedagogical_goal || step.goal || '', isArabicNum)
    }));

    // Quiz items JSON serialized for automated grading
    const quizItems = [
      ...mcqs.map((q, idx) => ({
        type: 'mcq',
        id: `mcq_${idx}`,
        question: formatMathDisplay(q.q || q.question || '', isArabicNum),
        options: (q.options || []).map(opt => formatMathDisplay(opt, isArabicNum)),
        answer: (q.correct !== undefined) ? q.correct : ((q.answer !== undefined) ? q.answer : 0),
        explanation: formatMathDisplay(q.explanation || '', isArabicNum)
      })),
      ...tfs.map((q, idx) => ({
        type: 'tf',
        id: `tf_${idx}`,
        question: formatMathDisplay(q.statement || q.q || q.question || '', isArabicNum),
        options: ['صواب', 'خطأ'],
        answer: (q.is_true === true || q.answer === true) ? 0 : 1,
        explanation: formatMathDisplay(q.explanation || '', isArabicNum)
      }))
    ];

    // Build the standalone HTML document
    return `<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>الدرس ${lessonNumber}: ${lessonTitle} | منصة الرائد التعليمية</title>
  <style>
    :root {
      --primary: #1d4ed8;
      --primary-hover: #1e40af;
      --primary-light: #eff6ff;
      --accent: #f59e0b;
      --success: #10b981;
      --success-light: #ecfdf5;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --card-shadow: 0 4px 18px rgba(15, 23, 42, 0.06);
      --font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Cairo", "Amiri", sans-serif;
    }

    [data-theme="dark"] {
      --primary: #3b82f6;
      --primary-hover: #60a5fa;
      --primary-light: #1e293b;
      --accent: #fbbf24;
      --success: #34d399;
      --success-light: #064e3b;
      --danger: #f87171;
      --danger-light: #7f1d1d;
      --bg-page: #0b0f19;
      --bg-card: #131c2e;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --border-color: #27354f;
      --card-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background: var(--bg-page);
      color: var(--text-main);
      font-family: var(--font-family);
      line-height: 1.7;
      direction: rtl;
      text-align: right;
      padding-bottom: 60px;
      transition: background 0.3s ease, color 0.3s ease;
    }

    /* Sticky Floating Interactive Action Bar */
    .top-action-bar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(19, 28, 46, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1.5px solid rgba(255, 255, 255, 0.12);
      color: #ffffff;
      padding: 10px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.25);
    }

    .top-bar-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 0.95rem;
    }

    .brand-badge {
      background: rgba(59, 130, 246, 0.3);
      border: 1px solid #60a5fa;
      color: #93c5fd;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 700;
    }

    .top-bar-tools {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .interactive-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid rgba(255, 255, 255, 0.2);
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      transition: all 0.2s ease;
      font-family: inherit;
      text-decoration: none;
    }

    .interactive-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      transform: translateY(-1px);
    }

    .interactive-btn.primary {
      background: #2563eb;
      border-color: #60a5fa;
    }
    .interactive-btn.primary:hover {
      background: #1d4ed8;
    }

    .interactive-btn.success {
      background: #059669;
      border-color: #34d399;
    }
    .interactive-btn.success:hover {
      background: #047857;
    }

    /* Container */
    .lesson-wrapper {
      max-width: 960px;
      margin: 24px auto;
      padding: 0 16px;
    }

    /* Header Card (Saudi Ministry Standard Style) */
    .header-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 24px 28px;
      margin-bottom: 24px;
      box-shadow: var(--card-shadow);
      position: relative;
      overflow: hidden;
      border-top: 5px solid var(--primary);
    }

    .header-top-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
      gap: 16px;
      flex-wrap: wrap;
    }

    .header-titles h1 {
      font-size: 1.65rem;
      font-weight: 900;
      color: var(--primary);
      margin-bottom: 6px;
      letter-spacing: -0.5px;
    }

    .header-meta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 10px;
    }

    .meta-chip {
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 14px;
      font-size: 0.8rem;
      font-weight: 700;
      border: 1px solid rgba(59, 130, 246, 0.2);
    }

    .meta-chip.teacher {
      background: #fef3c7;
      color: #b45309;
      border-color: #fde68a;
    }

    /* Quick Progress Roadmap */
    .lesson-roadmap-bar {
      display: flex;
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 6px;
      gap: 6px;
      margin-top: 18px;
      overflow-x: auto;
    }

    .roadmap-step-pill {
      flex: 1;
      text-align: center;
      padding: 8px 10px;
      font-size: 0.78rem;
      font-weight: 800;
      border-radius: 8px;
      background: var(--bg-card);
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .roadmap-step-pill:hover, .roadmap-step-pill.active {
      background: var(--primary);
      color: #ffffff;
      transform: translateY(-1px);
    }

    /* Section Cards */
    .section-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 22px 24px;
      margin-bottom: 22px;
      box-shadow: var(--card-shadow);
      transition: border-color 0.25s ease;
    }

    .section-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 12px;
      margin-bottom: 18px;
    }

    .section-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-time-badge {
      font-size: 0.75rem;
      background: var(--primary-light);
      color: var(--primary);
      padding: 3px 10px;
      border-radius: 12px;
      font-weight: 800;
    }

    /* Station 1: Objectives & Concepts */
    .obj-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    @media (max-width: 700px) {
      .obj-grid { grid-template-columns: 1fr; }
    }

    .obj-box {
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 14px 18px;
    }

    .obj-box-title {
      font-weight: 800;
      font-size: 0.92rem;
      color: var(--primary);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .obj-list {
      list-style-type: none;
      padding-right: 0;
    }

    .obj-list li {
      position: relative;
      padding-right: 20px;
      margin-bottom: 6px;
      font-size: 0.88rem;
      line-height: 1.6;
    }

    .obj-list li::before {
      content: "✓";
      position: absolute;
      right: 0;
      color: var(--success);
      font-weight: 900;
    }

    /* Station 2: Socratic Step-by-Step Interactive Engine */
    .socratic-container {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.04) 0%, rgba(16, 185, 129, 0.04) 100%);
      border: 1.5px solid rgba(59, 130, 246, 0.25);
      border-radius: 14px;
      padding: 20px;
    }

    .socratic-step-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 16px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.04);
      transition: all 0.25s ease;
    }

    .socratic-step-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }

    .socratic-step-badge {
      background: #3b82f6;
      color: #ffffff;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: 0.75rem;
      font-weight: 800;
    }

    .socratic-q-text {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 12px;
      line-height: 1.6;
    }

    .socratic-input-box {
      display: flex;
      gap: 8px;
      margin-top: 10px;
    }

    .socratic-student-input {
      flex: 1;
      height: 38px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-page);
      color: var(--text-main);
      padding: 0 12px;
      font-family: inherit;
      font-size: 0.88rem;
    }

    .socratic-reveal-btn {
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 0 16px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      font-family: inherit;
      white-space: nowrap;
      transition: background 0.2s ease;
    }

    .socratic-reveal-btn:hover {
      background: var(--primary-hover);
    }

    .socratic-feedback-reveal {
      display: none;
      margin-top: 14px;
      background: var(--success-light);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 10px;
      padding: 14px 16px;
      animation: fadeIn 0.3s ease;
    }

    .socratic-feedback-reveal.show {
      display: block;
    }

    .socratic-feedback-title {
      font-weight: 800;
      color: var(--success);
      font-size: 0.88rem;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Station 3: Graduated Examples with Collapsible Steps */
    .example-card {
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 14px;
    }

    .example-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .example-tier-tag {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 8px;
      background: #e0f2fe;
      color: #0369a1;
    }

    .example-tier-tag.tier-2 {
      background: #fef3c7;
      color: #b45309;
    }

    .example-tier-tag.tier-3 {
      background: #f3e8ff;
      color: #7e22ce;
    }

    .example-prompt {
      font-weight: 700;
      font-size: 0.98rem;
      margin-bottom: 10px;
      line-height: 1.6;
    }

    .solution-toggle-btn {
      background: transparent;
      border: 1px dashed var(--primary);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.82rem;
      padding: 6px 14px;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: inherit;
      transition: all 0.2s ease;
    }

    .solution-toggle-btn:hover {
      background: var(--primary-light);
    }

    .example-solution-box {
      display: none;
      margin-top: 12px;
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      border-radius: 10px;
      padding: 14px 18px;
      border-right: 4px solid var(--primary);
      font-size: 0.9rem;
      line-height: 1.7;
    }

    .example-solution-box.show {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    /* Station 4: Misconception Buster Cards */
    .pitfall-card {
      background: var(--danger-light);
      border: 1px solid rgba(239, 68, 68, 0.25);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 12px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    @media (max-width: 600px) {
      .pitfall-card { grid-template-columns: 1fr; }
    }

    .pitfall-side.wrong {
      color: #b91c1c;
      font-size: 0.88rem;
    }

    .pitfall-side.correct {
      color: #047857;
      font-size: 0.88rem;
      border-right: 2px solid rgba(16, 185, 129, 0.4);
      padding-right: 12px;
    }

    /* Station 5: Interactive Self-Grading Quiz */
    .quiz-container {
      background: var(--bg-card);
    }

    .quiz-score-banner {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #ffffff;
      border-radius: 12px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    }

    .quiz-item-card {
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 18px;
      margin-bottom: 16px;
      transition: all 0.25s ease;
    }

    .quiz-q-title {
      font-weight: 800;
      font-size: 0.98rem;
      margin-bottom: 12px;
      line-height: 1.6;
    }

    .quiz-opts-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }

    @media (max-width: 600px) {
      .quiz-opts-grid { grid-template-columns: 1fr; }
    }

    .quiz-opt-label {
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      border-radius: 10px;
      padding: 10px 14px;
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s ease;
      user-select: none;
    }

    .quiz-opt-label:hover {
      border-color: var(--primary);
      background: var(--primary-light);
    }

    .quiz-opt-label.selected-correct {
      background: #d1fae5 !important;
      border-color: #10b981 !important;
      color: #065f46 !important;
      font-weight: 800;
    }

    .quiz-opt-label.selected-wrong {
      background: #fee2e2 !important;
      border-color: #ef4444 !important;
      color: #991b1b !important;
    }

    .quiz-explanation-box {
      display: none;
      margin-top: 10px;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      line-height: 1.6;
      background: var(--bg-card);
      border-right: 4px solid var(--primary);
    }

    .quiz-explanation-box.show {
      display: block;
      animation: fadeIn 0.25s ease;
    }

    /* Homework & Closure Card */
    .homework-box {
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(217, 119, 6, 0.04) 100%);
      border: 1.5px solid rgba(245, 158, 11, 0.35);
      border-radius: 12px;
      padding: 16px 20px;
      margin-top: 16px;
    }

    .homework-title {
      font-weight: 800;
      color: #d97706;
      font-size: 0.95rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Print styling */
    @media print {
      .top-action-bar, .socratic-reveal-btn, .solution-toggle-btn, .quiz-score-banner {
        display: none !important;
      }
      .example-solution-box, .socratic-feedback-reveal, .quiz-explanation-box {
        display: block !important;
      }
      body { background: #fff !important; color: #000 !important; }
      .section-card, .header-card { box-shadow: none !important; border: 1px solid #ccc !important; }
    }

    .sec-math, .ltr-math, .sec-pow {
      direction: ltr !important;
      unicode-bidi: isolate !important;
      display: inline-block;
      font-family: 'Times New Roman', serif;
    }
    .sec-pow .sec-exp, .ar-pow .ar-exp {
      font-size: 0.72em;
      vertical-align: super;
      line-height: 0;
    }
  </style>
</head>
<body>

  <!-- Floating Sticky Action Bar -->
  <header class="top-action-bar">
    <div class="top-bar-brand">
      <span>📐 منصة الرائد التعليمية للرياضيات</span>
      <span class="brand-badge">صفحة تفاعلية مستقلة</span>
    </div>
    <div class="top-bar-tools">
      <button class="interactive-btn" onclick="togglePageTheme()" title="تبديل الوضع الليلي والنهاري">🌙 النمط</button>
      <button class="interactive-btn primary" onclick="window.print()" title="طباعة كامل الدرس أو تصدير PDF">🖨️ طباعة / PDF</button>
      <button class="interactive-btn success" onclick="copyShareableLink()" title="نسخ رابط الدرس للطالب">🔗 نسخ الرابط</button>
    </div>
  </header>

  <main class="lesson-wrapper">
    
    <!-- Header Card -->
    <div class="header-card">
      <div class="header-top-row">
        <div class="header-titles">
          <h1>الدرس ${lessonNumber}: ${lessonTitle}</h1>
          <p style="color:var(--text-muted); font-size:0.92rem;">
            صفحات الكتاب المدرسي: <strong>${lessonPages}</strong>
          </p>
        </div>
        <div>
          <span class="meta-chip teacher">🌟 إشراف خبير الرياضيات: أ. محمد عبدالله جمعة</span>
        </div>
      </div>

      <div class="header-meta-row">
        <span class="meta-chip">المملكة العربية السعودية • وزارة التعليم</span>
        <span class="meta-chip">المنهج السعودي المعتمد</span>
        <span class="meta-chip">منصة سقراط التوليدية</span>
        <span class="meta-chip">تقويم ذاتي تفاعلي فوري</span>
        <span class="meta-chip verified-member" style="background:rgba(16,185,129,0.12); color:#059669; border-color:rgba(16,185,129,0.3); font-weight:800;">🌟 نسخة العضوية المعتمدة (كامل الصلاحيات) ✓</span>
      </div>

      <!-- Quick Step Navigation -->
      <nav class="lesson-roadmap-bar">
        <a href="#sec-objectives" class="roadmap-step-pill">${numFmt(1)}. الأهداف والمفاهيم</a>
        <a href="#sec-socratic" class="roadmap-step-pill">${numFmt(2)}. محاورة سقراط التفاعلية</a>
        <a href="#sec-explanation" class="roadmap-step-pill">${numFmt(3)}. الشرح والأمثلة المحلولة</a>
        <a href="#sec-pitfalls" class="roadmap-step-pill">${numFmt(4)}. فخاخ التفكير</a>
        <a href="#sec-quiz" class="roadmap-step-pill">${numFmt(5)}. الاختبار الذاتي الفوري</a>
        <a href="#sec-closure" class="roadmap-step-pill">${numFmt(6)}. الغلق والواجب</a>
      </nav>
    </div>

    <!-- Section 1: Objectives & Key Concepts -->
    <section class="section-card" id="sec-objectives">
      <div class="section-header">
        <div class="section-title">
          <span>🎯 ${numFmt(1)}. نواتج التعلم والمفاهيم والمصطلحات الأساسية</span>
        </div>
        <span class="section-time-badge">محطة الانطلاق</span>
      </div>
      <div class="obj-grid">
        <div class="obj-box">
          <div class="obj-box-title">🎯 نواتج التعلم المستهدفة (مخرجات الأداء)</div>
          <ul class="obj-list">
            ${(prep && prep.station1 && prep.station1.learning_outcomes && prep.station1.learning_outcomes.length)
              ? prep.station1.learning_outcomes.map(o => `<li>${formatMathDisplay(o, isArabicNum)}</li>`).join('')
              : `<li>أن يتعرف الطالب المفهوم الرياضي الأساسي لـ (${lessonTitle}) بدقة.</li>
                 <li>أن يطبق الإجراء الرياضي السليم في حل التمارين المتدرجة.</li>
                 <li>أن يوظف المفهوم في حل مواقف ومسائل من واقع الحياة.</li>`
            }
          </ul>
        </div>
        <div class="obj-box">
          <div class="obj-box-title">💡 المفاهيم والمصطلحات الرياضية الأساسية</div>
          <p style="font-size:0.9rem; line-height:1.7; margin-bottom:8px;">
            <strong>📌 الفكرة المركزية:</strong> ${formatMathDisplay(summary.concept || 'بناء المفهوم الرياضي بأسلوب برهاني وتطبيقي دقيق.', isArabicNum)}
          </p>
          <div style="font-size:0.86rem; color:var(--text-muted);">
            <strong>المصطلحات المحورية:</strong>
            ${(prep && prep.station1 && prep.station1.key_concepts && prep.station1.key_concepts.length)
              ? prep.station1.key_concepts.join(' • ')
              : 'المصطلحات المعتمدة في كتاب الطالب'
            }
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Interactive Socratic Dialogue -->
    <section class="section-card" id="sec-socratic">
      <div class="section-header">
        <div class="section-title">
          <span>🏛️ ${numFmt(2)}. المحاورة السقراطية التفاعلية خطوة بخطوة (Socratic Dialogue)</span>
        </div>
        <span class="section-time-badge">تفكير استقصائي وتوليدي</span>
      </div>
      
      <p style="font-size:0.92rem; color:var(--text-muted); margin-bottom:16px;">
        ${formatMathDisplay(socratic.introduction || 'حاور الفكرة الرياضية عبر أسئلة سقراط المتتالية؛ فكر ملياً واكتب فكرتك ثم تحقق من توجيه سقراط:', isArabicNum)}
      </p>

      <div class="socratic-container">
        ${socraticSteps.length ? socraticSteps.map((step, idx) => `
          <div class="socratic-step-card" id="socratic-card-${idx}">
            <div class="socratic-step-header">
              <span class="socratic-step-badge">السؤال السقراطي رقم ${numFmt(idx + 1)}</span>
              <span style="font-size:0.75rem; color:var(--text-muted);">${step.pedagogicalGoal ? ('الهدف: ' + step.pedagogicalGoal) : ''}</span>
            </div>
            <div class="socratic-q-text">${step.question}</div>
            
            <div class="socratic-input-box">
              <input type="text" class="socratic-student-input" id="soc-in-${idx}" placeholder="اكتب استنتاجك أو إجابتك هنا...">
              <button class="socratic-reveal-btn" onclick="revealSocraticFeedback(${idx})">تحقق من تفكيرك 💡</button>
            </div>

            <div class="socratic-feedback-reveal" id="soc-box-${idx}">
              <div class="socratic-feedback-title">
                <span>🌟 تعليق وتوجيه سقراط الرياضي:</span>
              </div>
              <p style="font-size:0.92rem; line-height:1.7;">${step.socraticFeedback || step.expectedAnswer}</p>
            </div>
          </div>
        `).join('') : `
          <div style="padding:14px; text-align:center; color:var(--text-muted);">
            محاورة سقراطية استقصائية مباشرة لبناء المفهوم وقياس الجاهزية.
          </div>
        `}
      </div>
    </section>

    <!-- Section 3: Explanation and Graduated Solved Examples -->
    <section class="section-card" id="sec-explanation">
      <div class="section-header">
        <div class="section-title">
          <span>📖 ${numFmt(3)}. الشرح المتدرج والأمثلة المحلولة خطوة بخطوة</span>
        </div>
        <span class="section-time-badge">بناء المفهوم الرياضي</span>
      </div>

      <!-- Core Principle / Golden Rule -->
      ${summary.golden_rule ? `
        <div style="background:var(--primary-light); border:1px solid rgba(59, 130, 246, 0.3); border-radius:12px; padding:14px 18px; margin-bottom:18px;">
          <strong style="color:var(--primary); font-size:0.95rem;">🌟 القاعدة الذهبية / القانون المحوري:</strong>
          <p style="font-size:0.92rem; margin-top:4px;">${formatMathDisplay(summary.golden_rule, isArabicNum)}</p>
        </div>
      ` : ''}

      <!-- Graduated Examples -->
      ${(summary.examples && summary.examples.length) ? summary.examples.map((ex, idx) => `
        <div class="example-card">
          <div class="example-header">
            <span class="example-tier-tag ${idx === 1 ? 'tier-2' : (idx >= 2 ? 'tier-3' : '')}">
              ${idx === 0 ? ('المستوى ' + numFmt(1) + ': مثال مباشر وتطبيق أولي') : (idx === 1 ? ('المستوى ' + numFmt(2) + ': مسألة تطبيقية ومتوسطة') : ('المستوى ' + numFmt(3) + ': تفكير عليا وربط بالواقع'))}
            </span>
            <span style="font-size:0.75rem; color:var(--text-muted);">مثال محلول ${numFmt(idx + 1)}</span>
          </div>
          <div class="example-prompt">${formatMathDisplay(ex.problem || ex.title || 'مسألة تدريبية', isArabicNum)}</div>
          <button class="solution-toggle-btn" onclick="toggleExampleSolution(${idx})">
            <span>👁️ إظهار خطوات الحل والشرح الرياضي</span>
          </button>
          <div class="example-solution-box" id="ex-sol-${idx}">
            <strong>خطوات الحل المنظم:</strong>
            <p style="margin-top:6px;">${formatMathDisplay(ex.solution || ex.steps || 'يتم تطبيق القاعدة الرياضية بالتعويض المباشر والتبسيط.', isArabicNum)}</p>
          </div>
        </div>
      `).join('') : `
        <div class="example-card">
          <div class="example-prompt">أمثلة الكتاب المدرسي المتدرجة وفق المنهج السعودي.</div>
        </div>
      `}
    </section>

    <!-- Section 4: Misconceptions & Pitfalls -->
    <section class="section-card" id="sec-pitfalls">
      <div class="section-header">
        <div class="section-title">
          <span>⚠️ ${numFmt(4)}. فخاخ التفكير ومعالجة الأخطاء الشائعة</span>
        </div>
        <span class="section-time-badge">وقاية ومعالجة فورية</span>
      </div>

      ${(prep && prep.station4 && prep.station4.common_errors && prep.station4.common_errors.length) ? prep.station4.common_errors.map((err, idx) => `
        <div class="pitfall-card">
          <div class="pitfall-side wrong">
            <strong>❌ الخطأ الشائع المتوقع (${numFmt(idx + 1)}):</strong>
            <p style="margin-top:4px;">${formatMathDisplay(err.error || err, isArabicNum)}</p>
          </div>
          <div class="pitfall-side correct">
            <strong>✓ التصويب الرياضي الدقيق:</strong>
            <p style="margin-top:4px;">${formatMathDisplay(err.correction || 'التأكيد على خطوات التفكير السليم ومراجعة المعطيات قبل الحل.', isArabicNum)}</p>
          </div>
        </div>
      `).join('') : `
        <div class="pitfall-card">
          <div class="pitfall-side wrong">
            <strong>❌ الخطأ المتوقع:</strong>
            <p>التسرع في إجراء العمليات دون مراعاة ترتيب الأولويات أو الخصائص الأساسية.</p>
          </div>
          <div class="pitfall-side correct">
            <strong>✓ الإجراء السليم:</strong>
            <p>التحقق من صحة الناتج بالتعويض العكسي واستخدام النماذج البصرية.</p>
          </div>
        </div>
      `}
    </section>

    <!-- Section 5: Interactive Self-Grading Quiz -->
    <section class="section-card" id="sec-quiz">
      <div class="section-header">
        <div class="section-title">
          <span>📝 ${numFmt(5)}. التقييم الذاتي التفاعلي الفوري (الاختبار المقنن: ${numFmt(mcqs.length || 10)} اختيار + ${numFmt(tfs.length || 5)} صواب وخطأ + ${numFmt(essays.length || 3)} مقالي)</span>
        </div>
        <span class="section-time-badge">تصحيح إلكتروني لحظي</span>
      </div>

      <div class="quiz-score-banner" id="quiz-score-banner">
        <div>
          <div style="font-weight:900; font-size:1.1rem;">لوحة التقييم الفوري للطالب</div>
          <div style="font-size:0.85rem; opacity:0.9;">أجب عن الأسئلة الموضوعية وتعرف على درجتك فوراً، ثم أنجز المسائل المقالية التحليلية</div>
        </div>
        <div style="text-align:left;">
          <span style="font-size:1.6rem; font-weight:900;" id="user-score-display">${numFmt(0)} / ${numFmt(quizItems.length)}</span>
        </div>
      </div>

      <div class="quiz-container">
        ${quizItems.map((q, qIdx) => `
          <div class="quiz-item-card" id="q-card-${qIdx}">
            <div class="quiz-q-title">
              <span style="color:var(--primary); font-weight:900;">س ${numFmt(qIdx + 1)}:</span>
              ${q.question}
            </div>
            <div class="quiz-opts-grid">
              ${q.options.map((opt, oIdx) => `
                <div class="quiz-opt-label" id="opt-lbl-${qIdx}-${oIdx}" onclick="handleQuizAnswer(${qIdx}, ${oIdx})">
                  <span style="font-weight:800; font-size:0.8rem; color:var(--text-muted); width:20px;">(${q.type === 'mcq' ? (isArabicNum ? (['أ', 'ب', 'ج', 'د'][oIdx] || numFmt(oIdx + 1)) : (['A', 'B', 'C', 'D'][oIdx] || numFmt(oIdx + 1))) : numFmt(oIdx + 1)})</span>
                  <span>${opt}</span>
                </div>
              `).join('')}
            </div>
            <div class="quiz-explanation-box" id="q-exp-${qIdx}">
              <strong>💡 الشرح والتفسير الرياضي:</strong>
              <p style="margin-top:4px;">${q.explanation || 'الإجابة الصحيحة مبنية على التطبيق المباشر لقواعد الدرس.'}</p>
            </div>
          </div>
        `).join('')}
      </div>

      <!-- Part 3: Essay & Application Problems (المسائل المقالية التحليلية) -->
      ${essays.length ? `
        <div style="margin-top:28px; padding-top:20px; border-top:1px dashed var(--border-color);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
            <div style="font-weight:900; font-size:1.05rem; color:var(--primary);">
              <span>✍️ القسم الثاني: المسائل المقالية والتحليلية (${numFmt(essays.length)} مسائل)</span>
            </div>
            <span style="font-size:0.8rem; background:rgba(124,58,237,0.1); color:#7c3aed; padding:3px 10px; border-radius:12px; font-weight:700;">
              حل كتابي ونموذج إجابة
            </span>
          </div>

          <div style="display:flex; flex-direction:column; gap:14px;">
            ${essays.map((es, eIdx) => `
              <div class="quiz-item-card" style="border-right:4px solid #7c3aed;">
                <div class="quiz-q-title">
                  <span style="color:#7c3aed; font-weight:900;">مسألة ${numFmt(eIdx + 1)}:</span>
                  ${formatMathDisplay(es.q || es.question || '', isArabicNum)}
                </div>

                <div style="margin:12px 0 8px;">
                  <textarea class="socratic-student-input" style="width:100%; min-height:70px; resize:vertical; font-family:inherit; padding:10px 14px; border:1px solid var(--border-color); border-radius:8px; background:var(--bg-card); color:var(--text-main);" placeholder="اكتب خطوات الحل أو الناتج هنا للتفكير الذاتي..."></textarea>
                </div>

                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                  <button type="button" class="solution-toggle-btn" onclick="toggleEssaySolution(${eIdx})">
                    <span>👁️ إظهار نموذج الحل والتفسير الرياضي</span>
                  </button>
                  <span style="font-size:0.8rem; color:var(--text-muted); font-weight:700;">درجة السؤال: ${numFmt(es.marks || 2)} درجات</span>
                </div>

                <div class="socratic-feedback-reveal" id="essay-sol-${eIdx}">
                  <div class="socratic-feedback-title" style="color:#7c3aed;">
                    <span>✓ نموذج الحل والخطوات المعتمدة:</span>
                  </div>
                  <p style="font-size:0.92rem; line-height:1.7; margin-top:4px;">${formatMathDisplay(es.ans || es.answer || 'الحل مبني على تطبيق الخطوات الأربع وقواعد الدرس بدقة.', isArabicNum)}</p>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}
    </section>

    <!-- Section 6: Closure & Graduated Homework -->
    <section class="section-card" id="sec-closure">
      <div class="section-header">
        <div class="section-title">
          <span>🏁 ${numFmt(6)}. الغلق والواجب المنزلي وسؤال التحدي</span>
        </div>
        <span class="section-time-badge">تثبيت واستدامة التعلم</span>
      </div>

      <div style="background:var(--bg-page); border:1px solid var(--border-color); border-radius:12px; padding:16px 20px; margin-bottom:14px;">
        <strong style="color:var(--primary); font-size:0.95rem;">📌 ملخص الغلق المحوري:</strong>
        <p style="font-size:0.92rem; margin-top:6px; line-height:1.7;">
          ${(prep && prep.station6 && prep.station6.closure_activity) ? formatMathDisplay(prep.station6.closure_activity, isArabicNum) : 'يربط الطالب بين نواتج التعلم المستهدفة والتطبيقات الحياتية للدرس في جملة ختامية برهانية.'}
        </p>
      </div>

      <div class="homework-box">
        <div class="homework-title">
          <span>🏠 الواجب المنزلي ومهمة التمايز الرياضي:</span>
        </div>
        <div style="font-size:0.9rem; line-height:1.7;">
          ${(prep && prep.station6 && prep.station6.homework_exercises) ? `
            <div style="margin-bottom:6px;"><strong>المستوى الأساسي:</strong> ${formatMathDisplay(prep.station6.homework_exercises.basic || 'تمارين الكتاب المباشرة', isArabicNum)}</div>
            <div style="margin-bottom:6px;"><strong>المستوى المتوسط:</strong> ${formatMathDisplay(prep.station6.homework_exercises.intermediate || 'مسائل مهارات التفكير', isArabicNum)}</div>
            <div><strong>سؤال التحدي والإثراء:</strong> ${formatMathDisplay(prep.station6.homework_exercises.advanced || 'مسألة تفكير عليا مفتوحة', isArabicNum)}</div>
          ` : `
            <div>تمارين كتاب الطالب المقابلة لصفحات الدرس (${lessonPages}).</div>
          `}
        </div>
      </div>
    </section>

    <!-- Footer Credentials -->
    <footer style="text-align:center; padding:24px 10px; font-size:0.85rem; color:var(--text-muted); border-top:1px solid var(--border-color); margin-top:30px;">
      <p style="font-weight:700; color:var(--text-main); margin-bottom:4px;">منصة الرائد التعليمية الذكية للرياضيات • الإصدار ${numFmt('2.0')}</p>
      <p>إعداد وإشراف خبير الرياضيات: أ. محمد عبدالله جمعة | المدارس المتقدمة للتعلم الذكي</p>
      <p style="font-size:0.75rem; margin-top:4px;">صفحة تفاعلية مستقلة بصيغة HTML تعمل دون اتصال بالإنترنت</p>
    </footer>

  </main>

  <!-- Interactive Logic Engine -->
  <script>
    // Theme toggle
    function togglePageTheme() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('alraed_standalone_theme', next); } catch(e){}
    }

    // Restore theme preference
    try {
      const saved = localStorage.getItem('alraed_standalone_theme');
      if (saved) document.documentElement.setAttribute('data-theme', saved);
    } catch(e){}

    // Socratic step reveal
    function revealSocraticFeedback(stepIdx) {
      const box = document.getElementById('soc-box-' + stepIdx);
      if (box) {
        box.classList.toggle('show');
      }
    }

    // Example solution toggle
    function toggleExampleSolution(idx) {
      const box = document.getElementById('ex-sol-' + idx);
      if (box) {
        box.classList.toggle('show');
      }
    }

    // Essay solution toggle
    function toggleEssaySolution(idx) {
      const box = document.getElementById('essay-sol-' + idx);
      if (box) {
        box.classList.toggle('show');
      }
    }

    // Quiz automated grading data
    const QUIZ_ITEMS = ${JSON.stringify(quizItems)};
    const userAnswers = {};
    const IS_ARABIC_NUM = ${isArabicNum};

    function numToAr(n) {
      if (!IS_ARABIC_NUM) return String(n).replace(/[\\u0660-\\u0669]/g, w => String(w.charCodeAt(0) - 0x0660));
      return String(n).replace(/[0-9]/g, w => String.fromCharCode(0x0660 + parseInt(w, 10)));
    }

    function handleQuizAnswer(qIdx, optIdx) {
      if (userAnswers[qIdx] !== undefined) return; // already answered

      userAnswers[qIdx] = optIdx;
      const q = QUIZ_ITEMS[qIdx];
      const isCorrect = (optIdx === q.answer);

      // Highlight selected option
      const selectedLbl = document.getElementById('opt-lbl-' + qIdx + '-' + optIdx);
      if (selectedLbl) {
        selectedLbl.classList.add(isCorrect ? 'selected-correct' : 'selected-wrong');
      }

      // If wrong, highlight correct one
      if (!isCorrect) {
        const correctLbl = document.getElementById('opt-lbl-' + qIdx + '-' + q.answer);
        if (correctLbl) correctLbl.classList.add('selected-correct');
      }

      // Show explanation
      const exp = document.getElementById('q-exp-' + qIdx);
      if (exp) exp.classList.add('show');

      // Update score banner
      updateScoreBanner();
    }

    function updateScoreBanner() {
      let correct = 0;
      Object.keys(userAnswers).forEach(qIdx => {
        const q = QUIZ_ITEMS[qIdx];
        if (userAnswers[qIdx] === q.answer) correct++;
      });
      const display = document.getElementById('user-score-display');
      if (display) {
        display.textContent = numToAr(correct) + ' / ' + numToAr(QUIZ_ITEMS.length);
      }
    }

    // Shareable link copier
    function copyShareableLink() {
      const url = window.location.href;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(() => {
          alert('✓ تم نسخ رابط الدرس بنجاح!');
        }).catch(() => {
          prompt('انسخ رابط الدرس التالي:', url);
        });
      } else {
        prompt('انسخ رابط الدرس التالي:', url);
      }
    }
  </script>
</body>
</html>`;
  }

  /**
   * Download the generated HTML file directly to user device
   */
  function downloadLessonHtml(lessonId) {
    if (!global.CURRICULUM_DATA || !global.CURRICULUM_DATA.lessons) return;
    const lesson = global.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson) return;

    const htmlContent = buildStandaloneLessonHtml(lesson);
    const cleanTitle = (lesson.title || 'درس').replace(/[\\/:*?"<>|]/g, '_');
    const fileName = `الرائد_درس_${cleanTitle}.html`;

    const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    setTimeout(() => URL.revokeObjectURL(url), 2000);
  }

  /**
   * Open the generated HTML directly in a standalone new browser tab
   */
  function openLessonInNewTab(lessonId) {
    if (!global.CURRICULUM_DATA || !global.CURRICULUM_DATA.lessons) return;
    const lesson = global.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson) return;

    const htmlContent = buildStandaloneLessonHtml(lesson);
    const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    window.open(url, '_blank');
    setTimeout(() => URL.revokeObjectURL(url), 30000);
  }

  /**
   * Copy the raw HTML source code to clipboard
   */
  function copyLessonHtmlCode(lessonId) {
    if (!global.CURRICULUM_DATA || !global.CURRICULUM_DATA.lessons) return;
    const lesson = global.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson) return;

    const htmlContent = buildStandaloneLessonHtml(lesson);
    if (navigator.clipboard) {
      navigator.clipboard.writeText(htmlContent).then(() => {
        alert('✓ تم نسخ كود HTML الكامل للدرس بنجاح!\nيمكنك الآن لصقه في أي محرر أو موقع أو منصة تعليمية.');
      }).catch(() => {
        fallbackCopyText(htmlContent);
      });
    } else {
      fallbackCopyText(htmlContent);
    }
  }

  function fallbackCopyText(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      alert('✓ تم نسخ كود HTML الكامل للدرس!');
    } catch (e) {
      prompt('انسخ كود HTML يدوياً:', text.substring(0, 500) + '...');
    }
    document.body.removeChild(ta);
  }

  /**
   * Show Interactive HTML Generator Modal in the platform
   */
  function showGeneratorModal(lessonId) {
    if (!global.CURRICULUM_DATA || !global.CURRICULUM_DATA.lessons) return;
    const lesson = global.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson) return;

    // Remove existing modal if any
    const existing = document.getElementById('interactive-html-modal');
    if (existing) existing.remove();

    const isArabicNum = isArabicStageLesson(lesson);
    const numFmt = (n) => isArabicNum ? toEasternArabicNumerals(n) : toWesternNumerals(n);
    const lessonTitle = numFmt(lesson.title || 'الدرس');
    const lessonNumber = numFmt(lesson.number || '1');

    const htmlContent = buildStandaloneLessonHtml(lesson);
    const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
    const previewUrl = URL.createObjectURL(blob);

    const modal = document.createElement('div');
    modal.id = 'interactive-html-modal';
    modal.className = 'interactive-modal-overlay';
    modal.innerHTML = `
      <div class="interactive-modal-window">
        <div class="interactive-modal-header">
          <div class="modal-header-titles">
            <span class="modal-icon-badge">🌐</span>
            <div>
              <h3 style="font-size:1.15rem; font-weight:800; color:#ffffff; margin:0;">مولد الصفحات التفاعلية المستقلة (HTML)</h3>
              <p style="font-size:0.8rem; color:#93c5fd; margin-top:2px;">الدرس ${lessonNumber}: ${escapeHtml(lessonTitle)} • صفحة قائمة بذاتها تعمل دون إنترنت</p>
            </div>
          </div>
          <button type="button" class="modal-close-x" onclick="document.getElementById('interactive-html-modal').remove()">✕</button>
        </div>

        <div class="interactive-modal-toolbar">
          <div class="modal-toolbar-actions">
            <button class="nav-chip-btn primary" onclick="window.InteractiveHtmlGenerator.downloadLessonHtml('${lessonId}')" title="تحميل ملف HTML لجهازك مباشرة">
              <span>📥 تحميل ملف HTML المستقل</span>
            </button>
            <button class="nav-chip-btn" onclick="window.InteractiveHtmlGenerator.openLessonInNewTab('${lessonId}')" title="فتح الصفحة التفاعلية في نافذة جديدة بكامل الشاشة">
              <span>🚀 فتح في نافذة مستقلة</span>
            </button>
            <button class="nav-chip-btn" onclick="window.InteractiveHtmlGenerator.copyLessonHtmlCode('${lessonId}')" title="نسخ الكود البرمجي HTML">
              <span>📋 نسخ كود HTML</span>
            </button>
            <button class="nav-chip-btn" onclick="window.InteractiveHtmlGenerator.copyDirectStudentLink('${lessonId}')" title="نسخ رابط الطالب التفاعلي بالمنهج السقراطي">
              <span>🔗 رابط الطالب السقراطي</span>
            </button>
          </div>
          <div style="font-size:0.78rem; color:#64748b; font-weight:700;">
            ✓ صفحة متكاملة تشمل: محاورة سقراط + أمثلة تفاعلية + اختبار ذاتي مصحح + النمط الليلي
          </div>
        </div>

        <div class="interactive-modal-body">
          <iframe id="html-preview-frame" class="html-preview-frame" src="${previewUrl}"></iframe>
        </div>
      </div>
    `;

    document.body.appendChild(modal);
  }

  function copyDirectStudentLink(lessonId) {
    const origin = (typeof window !== 'undefined' && window.location) ? window.location.origin + window.location.pathname : '';
    const url = `${origin}?lesson=${encodeURIComponent(lessonId)}&view=socratic`;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(() => {
        alert(`✓ تم نسخ رابط الدرس التفاعلي بالمنهج السقراطي:\n\n${url}\n\nيمكنك إرساله مباشرة للطلاب عبر المنصة أو البريد أو وسائل التواصل.`);
      });
    } else {
      prompt('رابط الطالب التفاعلي المباشر بالمنهج السقراطي:', url);
    }
  }

  // Export to Global Scope
  global.InteractiveHtmlGenerator = {
    buildStandaloneLessonHtml,
    downloadLessonHtml,
    openLessonInNewTab,
    copyLessonHtmlCode,
    showGeneratorModal,
    copyDirectStudentLink
  };

})(typeof window !== 'undefined' ? window : this);
