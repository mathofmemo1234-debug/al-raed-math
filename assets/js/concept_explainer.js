/**
 * ==========================================================================
 * محرك الشارح التفصيلي التفاعلي للجزئيات بالأمثلة التوضيحية (النظام الهجين)
 * يجمع بين:
 *  1) بطاقات شرح تفصيلية فورية مدمجة لكل جزئيات الدرس مع أمثلة محلولة (Offline)
 *  2) طلب شرح مخصص لأي جزئية يكتبها المستخدم عبر /api/explain (Gemini) مع التخزين المؤقت
 *  3) مطابقة محلية ذكية من قاعدة بيانات الكتاب عند العمل بدون إنترنت أو بدون API
 *  4) إضافة شروحات مخصصة من المعلم + نسخ إلى Word + طباعة احترافية
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * ==========================================================================
 */

(function (global) {
  'use strict';

  const TEACHER_STORE_KEY = 'alraed_teacher_subtopics_v1';
  const CACHE_STORE_KEY = 'alraed_ce_cache_v2';
  const CE_NAV_SESSION_KEY = 'alraed_ce_nav_v1';
  const STOP_WORDS = new Set(['في', 'من', 'على', 'إلى', 'عن', 'ما', 'هي', 'هو', 'هذا', 'هذه', 'كيف', 'متى', 'لماذا', 'أو', 'ثم', 'بين', 'مع', 'كل', 'أي', 'لي', 'لـ', 'الدرس', 'جزئية', 'شرح', 'مثال', 'توضيحي', 'تفصيلي', 'اريد', 'أريد', 'اشرح']);

  const state = {
    lessonStates: Object.create(null)
  };

  function getUtils() {
    return global.ArabicUtils || null;
  }

  function isSecondaryLesson(lesson) {
    const utils = getUtils();
    if (!lesson) return false;
    if (utils && typeof utils.isSecondaryStage === 'function' && utils.isSecondaryStage(lesson)) {
      return true;
    }
    const lid = String(lesson.id || '');
    return lid.startsWith('g1s') || lid.startsWith('g2s') || lid.startsWith('g3s') || lesson.stageId === 'secondary';
  }

  function escHtml(str) {
    const utils = getUtils();
    if (utils && typeof utils.escapeHtml === 'function') {
      return utils.escapeHtml(str == null ? '' : String(str));
    }
    return String(str == null ? '' : str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function fmt(text, isSec) {
    if (text === null || text === undefined) return '';
    const utils = getUtils();
    if (utils && typeof utils.renderMathHtml === 'function') {
      return utils.renderMathHtml(String(text), !!isSec);
    }
    return escHtml(String(text));
  }

  function fmtPlainNum(val, isSec) {
    const utils = getUtils();
    const s = val == null ? '' : String(val);
    if (!utils) return s;
    return isSec ? utils.toWesternDigits(s) : utils.toEasternDigits(s);
  }

  function stripToPlain(text, isSec) {
    const utils = getUtils();
    if (utils && typeof utils.stripMathToPlain === 'function') {
      return utils.stripMathToPlain(String(text || ''), !!isSec);
    }
    return String(text || '').replace(/<[^>]+>/g, '');
  }

  function isApprovedOrAdmin() {
    const auth = global.FirebaseAuthManager;
    if (!auth) return false;
    if (typeof auth.isAdmin === 'function' && auth.isAdmin()) return true;
    if (typeof auth.isApproved === 'function' && auth.isApproved()) return true;
    return false;
  }

  function isAdminUser() {
    const auth = global.FirebaseAuthManager;
    return !!(auth && typeof auth.isAdmin === 'function' && auth.isAdmin());
  }

  function asText(val, sep) {
    if (val === null || val === undefined) return '';
    if (typeof val === 'string') return val.trim();
    if (Array.isArray(val)) {
      return val.map(function (item) { return asText(item, ' — '); }).filter(Boolean).join(sep || ' • ');
    }
    if (typeof val === 'object') {
      return Object.keys(val).map(function (k) { return asText(val[k], ' '); }).filter(Boolean).join(' — ');
    }
    return String(val).trim();
  }

  function splitIntoSteps(rawText) {
    const clean = asText(rawText, '\n');
    if (!clean) return [];
    // Mask $...$ blocks so interval commas/digits like "(-2, 2) \cup" never trigger step splits
    const stash = [];
    const masked = clean.replace(/\$\$[\s\S]+?\$\$|\$[^\$]+?\$/g, function (m) {
      const ph = '__CELTX' + stash.length + '__';
      stash.push(m);
      return ph;
    });
    const unmask = function (s) {
      return s.replace(/__CELTX(\d+)__/g, function (_, idx) { return stash[Number(idx)] || ''; });
    };
    let lines = masked
      .split(/\s*(?:\n+|(?<=[.؟!:])\s+(?=[١-٩0-9]{1,2}\s*[)\-:.]|أولاً|ثانياً|ثالثاً|رابعاً))\s*/)
      .map(function (s) { return unmask(s).trim(); })
      .filter(Boolean);
    if (lines.length <= 1) {
      lines = masked
        .split(/\s+(?=[١-٩0-9]{1,2}\)\s+(?=[A-Za-z\u0600-\u06FF]))/)
        .map(function (s) { return unmask(s).trim(); })
        .filter(Boolean);
    }
    return lines.length > 1 ? lines : [clean];
  }

  function normalizeExampleObj(ex, isSec) {
    if (!ex || typeof ex !== 'object') {
      return { problem: '', steps: [], finalAnswer: '', fig: '', isExactUserSolution: false };
    }
    return {
      problem: String(ex.problem || '').trim(),
      steps: Array.isArray(ex.steps) ? ex.steps.map(function (s) { return String(s || '').trim(); }).filter(Boolean) : [],
      finalAnswer: String(ex.finalAnswer || '').trim(),
      fig: String(ex.fig || ex.image || '').trim(),
      cap: String(ex.cap || ex.imageCaption || '').trim(),
      isSec: !!isSec,
      isExactUserSolution: !!ex.isExactUserSolution
    };
  }

  function normCmpText(s) {
    return String(s || '')
      .replace(/[\s.،,:؛$()\[\]{}]/g, '')
      .toLowerCase();
  }

  function isRedundantFinalAnswer(steps, finalAnswer) {
    const fa = String(finalAnswer || '').trim();
    if (!fa) return true;
    if (!Array.isArray(steps) || !steps.length) return false;
    const last = String(steps[steps.length - 1] || '').trim();
    if (!last) return false;
    const nFa = normCmpText(fa);
    const nLast = normCmpText(last);
    if (!nFa || nFa === nLast) return true;
    // Also treat as redundant when finalAnswer literally contains the entire multi-step chain of last step
    if (nFa.length >= 10 && nLast.indexOf(nFa) !== -1 && fa.indexOf('=') !== -1 && fa.split('=').length >= 3) {
      return true;
    }
    return false;
  }

  function extractConciseFinalAnswer(lastStep) {
    const s = String(lastStep || '').replace(/[.\s]+$/, '').trim();
    if (!s) return '';
    // Look for explicit conclusion markers
    const arrowParts = s.split(/(?:←|⇐|إذن|ومنه|وبالتالي)/);
    if (arrowParts.length > 1) {
      const tail = arrowParts[arrowParts.length - 1].replace(/^[:\s،]+/, '').trim();
      if (tail && tail.length <= 55 && tail.length < s.length && (tail.match(/\$/g) || []).length % 2 === 0) {
        return tail;
      }
    }
    // Condense chained equalities like "د(٤) = -٣(٤) + ٧ = -١٢ + ٧ = -٥" -> "د(٤) = -٥"
    const eqParts = s.split('=');
    if (eqParts.length >= 3) {
      let lhs = eqParts[0].trim();
      const rhs = eqParts[eqParts.length - 1].trim();
      // Strip verbose Arabic prefix before math expression if there is a colon
      const colonIdx = lhs.lastIndexOf(':');
      if (colonIdx !== -1 && (lhs.match(/\$/g) || []).length % 2 === 0) {
        const afterColon = lhs.slice(colonIdx + 1).trim();
        if (afterColon) lhs = afterColon;
      }
      const combined = lhs + ' = ' + rhs;
      if (lhs && rhs && lhs.length <= 34 && rhs.length <= 40 && (combined.match(/\$/g) || []).length % 2 === 0 && combined.length < s.length) {
        return combined;
      }
    }
    return '';
  }

  /**
   * يستخرج مجمع الأمثلة المحلولة الموثقة من جميع أركان الدرس (الملخص، التوجيه، المقالي، ورقة العمل، والاختيار من متعدد)
   */
  function collectExamplePool(lesson, isSec) {
    const pool = [];
    const seen = new Set();
    const sum = lesson.summary || {};
    const prep = lesson.prep || {};
    const st4 = prep.station4 || {};
    const ws = lesson.worksheet || {};
    const quiz = lesson.quiz || {};

    function pushEx(problem, rawSolution, finalAnswer, fig, cap) {
      const p = String(problem || '').trim();
      const s = String(rawSolution || '').trim();
      if (!p && !s) return;
      const key = (p.slice(0, 60) + '|' + s.slice(0, 60));
      if (seen.has(key)) return;
      seen.add(key);
      const solSteps = splitIntoSteps(s);
      let concl = String(finalAnswer || '').trim();
      if (!concl && solSteps.length > 0) {
        concl = extractConciseFinalAnswer(solSteps[solSteps.length - 1]);
      }
      if (isRedundantFinalAnswer(solSteps, concl)) {
        concl = '';
      }
      pool.push(normalizeExampleObj({
        problem: p,
        steps: solSteps.length ? solSteps : (s ? [s] : []),
        finalAnswer: concl,
        fig: fig || '',
        cap: cap || ''
      }, isSec));
    }

    // 1. Summary solved_example
    if (sum.solved_example) {
      const txt = asText(sum.solved_example).replace(/^(?:تطبيق نموذجي محلول|مثال محلول|مسألة محلولة)\s*:\s*/i, '').trim();
      const splitM = txt.match(/^([\s\S]+?)(?:الحل\s*:|الخطوات\s*:|←|الإجابة\s*:)([\s\S]+)$/);
      if (splitM) {
        pushEx(splitM[1].trim(), splitM[2].trim(), '');
      } else {
        pushEx(txt, txt, '');
      }
    }

    // 2. Station 4 guided_practice
    if (st4.guided_practice) {
      const txt = asText(st4.guided_practice).replace(/^مثال محلول\s*:\s*|^مسألة محلولة\s*:\s*/i, '').trim();
      const splitM = txt.match(/^([\s\S]+?)(?:الحل\s*:|←)([\s\S]+)$/);
      if (splitM) {
        pushEx(splitM[1].trim(), splitM[2].trim(), '');
      } else {
        pushEx(txt, txt, '');
      }
    }

    // 3. Quiz essays (often have rich step-by-step solutions)
    (quiz.essay || []).forEach(function (eq) {
      pushEx(eq.q, eq.ans, '', eq.fig || eq.image || '', eq.imageCaption || '');
    });

    // 4. Worksheet questions
    (ws.questions || []).forEach(function (wq) {
      pushEx(wq.q, wq.ans, '', wq.image || wq.fig || '', wq.imageCaption || '');
    });

    // 5. Quiz MCQs with explanations (illustrated MCQs prioritized after essays or included neatly)
    (quiz.mcq || []).forEach(function (mq) {
      const cIdx = typeof mq.ans === 'number' ? mq.ans : (typeof mq.correct === 'number' ? mq.correct : 0);
      const ansText = (mq.options && mq.options[cIdx]) ? mq.options[cIdx] : '';
      const exp = mq.explanation || ansText;
      pushEx(mq.q, exp, ansText, mq.fig || mq.image || '', mq.imageCaption || '');
    });

    return pool;
  }

  function formatVocabItems(vocabList) {
    if (!Array.isArray(vocabList)) {
      return typeof vocabList === 'string' && vocabList.trim() ? [vocabList.trim()] : [];
    }
    return vocabList.map(function (v) {
      if (typeof v === 'string') return v.trim();
      if (v && typeof v === 'object') {
        const ar = v.ar || v.term || '';
        const en = v.en ? (' (' + v.en + ')') : '';
        const def = v.def || '';
        return (ar + en + (def ? ': ' + def : '')).trim();
      }
      return '';
    }).filter(Boolean);
  }

  /**
   * يبني بطاقات الجزئيات التوضيحية المدمجة لأي درس من الدروس الـ 166 عبر جميع المراحل الست
   */
  function buildBuiltInSubtopics(lesson) {
    if (!lesson || !lesson.id) return [];
    const isSec = isSecondaryLesson(lesson);
    const pool = collectExamplePool(lesson, isSec);
    const sum = lesson.summary || {};
    const prep = lesson.prep || {};
    const st1 = prep.station1 || {};
    const st2 = prep.station2 || {};
    const st3 = prep.station3 || {};
    const st4 = prep.station4 || {};
    const st5 = prep.station5 || {};
    const soc = lesson.socratic || {};
    const quiz = lesson.quiz || {};

    const pickExample = function (preferredIdx) {
      if (!pool.length) {
        return normalizeExampleObj({
          problem: 'تطبيق مباشر على مفهوم ' + (lesson.title || ''),
          steps: [sum.concept || lesson.lesson_idea || lesson.title || ''],
          finalAnswer: sum.golden_rule || ''
        }, isSec);
      }
      return pool[preferredIdx % pool.length];
    };

    const subtopics = [];

    // 1. Core Concept & Golden Rule
    const coreSummary = asText(sum.concept) || asText(lesson.lesson_idea) || asText(st2.key_concepts) || ('شرح المفهوم الرئيس لدرس ' + lesson.title);
    const coreSteps = [];
    const keyConceptsTxt = asText(st2.key_concepts);
    if (keyConceptsTxt && keyConceptsTxt !== coreSummary) {
      splitIntoSteps(keyConceptsTxt).forEach(function (s) {
        if (s && s !== coreSummary) coreSteps.push(s);
      });
    }
    const goldenTxt = asText(sum.golden_rule);
    if (goldenTxt && goldenTxt !== coreSummary) {
      coreSteps.push('القاعدة الذهبية: ' + goldenTxt);
    }
    if (Array.isArray(lesson.objectives)) {
      lesson.objectives.map(function (o) { return asText(o); }).filter(Boolean).slice(0, 3).forEach(function (o) {
        if (o !== coreSummary && o !== keyConceptsTxt && coreSteps.indexOf(o) === -1) coreSteps.push(o);
      });
    }
    if (st2.concept_map) {
      const cmap = asText(st2.concept_map);
      if (cmap && cmap !== coreSummary && coreSteps.indexOf(cmap) === -1) coreSteps.push(cmap);
    }
    const figFallback = (Array.isArray(lesson.figures) && lesson.figures[0])
      ? (typeof lesson.figures[0] === 'string' ? lesson.figures[0] : (lesson.figures[0].image || ''))
      : '';
    const ex0 = Object.assign({}, pickExample(0));
    if (!ex0.fig && figFallback) ex0.fig = figFallback;

    const miscRaw = asText(st3.misconceptions) || asText(soc.misconception_buster);
    subtopics.push({
      id: lesson.id + '-sub-core',
      title: 'المفهوم الأساسي والقاعدة المحورية',
      badge: '📚 جزئية أساسية (جاهزة)',
      source: 'builtin',
      summary: coreSummary,
      steps: coreSteps.slice(0, 5),
      workedExample: ex0,
      altExamples: pool.slice(1, 5),
      commonMistake: miscRaw,
      quickCheck: (quiz.mcq && quiz.mcq[0])
        ? {
            question: asText(quiz.mcq[0].q),
            answer: asText((quiz.mcq[0].options && quiz.mcq[0].options[typeof quiz.mcq[0].ans === 'number' ? quiz.mcq[0].ans : (quiz.mcq[0].correct || 0)]) || '') +
              (quiz.mcq[0].explanation ? (' — ' + asText(quiz.mcq[0].explanation)) : '')
          }
        : { question: 'لخّص القاعدة الأساسية لهذا الدرس بكلماتك مع مثال عددي بسيط.', answer: goldenTxt || asText(sum.concept) }
    });

    // 2. Procedural Methods & Strategies
    const methodsList = Array.isArray(sum.methods) ? sum.methods.map(function (m) { return asText(m); }).filter(Boolean) : [];
    const vocabSteps = formatVocabItems(st2.vocabulary || lesson.vocabulary);
    const procSteps = methodsList.concat(vocabSteps.slice(0, 3)).filter(Boolean);
    if (procSteps.length) {
      const ex1 = pickExample(1);
      const tfQ = (quiz.tf && quiz.tf[0]) ? quiz.tf[0] : null;
      subtopics.push({
        id: lesson.id + '-sub-methods',
        title: 'خطوات الحل والمفردات الأساسية',
        badge: '⚙️ مهارات إجرائية (جاهزة)',
        source: 'builtin',
        summary: asText(st2.concept_map) || asText(st3.teaching_strategies) || 'الخطوات المنهجية المتسلسلة لتنفيذ مسائل الدرس بدقة.',
        steps: procSteps.slice(0, 5),
        workedExample: ex1,
        altExamples: pool.slice(2, 6),
        commonMistake: miscRaw || 'تحقق دائماً من صحة الخطوات الوسيطة والوحدات أو الإشارات قبل اعتماد الناتج.',
        quickCheck: tfQ
          ? {
              question: 'صح أم خطأ: ' + asText(tfQ.q || tfQ.statement),
              answer: ((tfQ.ans === true || tfQ.is_true === true) ? 'صواب ✓' : 'خطأ ✗') + (tfQ.explanation ? (' — ' + asText(tfQ.explanation)) : '')
            }
          : { question: 'ما أول خطوة تبدأ بها عند حل مسائل هذه المهارة؟', answer: procSteps[0] }
      });
    }

    // 3. Common Misconceptions & Traps
    const falseTf = (quiz.tf || []).find(function (t) { return t.ans === false || t.is_true === false; }) || (quiz.tf && quiz.tf[1]);
    const miscText = miscRaw || 'انتبه للخلط بين الحالات الخاصة والشروط الأساسية عند التعويض المباشر.';
    subtopics.push({
      id: lesson.id + '-sub-traps',
      title: 'الأخطاء الشائعة وشروط التحقق',
      badge: '⚠️ تنبيهات حرجة (جاهزة)',
      source: 'builtin',
      summary: miscText,
      steps: [
        'اقرأ شروط المسألة والمجال أو الإشارة المطلوبة قبل البدء في الحساب.',
        asText(soc.inquiry_question) || 'تأكد من عدم التسرع في الاختصار أو إهمال الحالات الحدية.',
        'تحقق من معقولية الناتج النهائي بتعويضه في المعادلة أو الشرط الأصلي.'
      ],
      workedExample: pickExample(2),
      altExamples: pool.slice(3, 7),
      commonMistake: miscText,
      quickCheck: falseTf
        ? {
            question: 'تحقق من صحة العبارة التالية مع التبرير: ' + asText(falseTf.q || falseTf.statement),
            answer: ((falseTf.ans === true || falseTf.is_true === true) ? 'صواب ✓' : 'خطأ ✗') + (falseTf.explanation ? (' — ' + asText(falseTf.explanation)) : '')
          }
        : { question: 'ما السبب الذي قد يوقع الطالب في الخطأ عند تطبيق هذه القاعدة؟', answer: miscText }
    });

    // 4. Applications & Higher-Order Thinking (when rich content exists)
    const appText = asText(st4.life_applications);
    const hotText = asText(st5.higher_order_thinking);
    if (appText || hotText || pool.length >= 4) {
      const challengeQ = (quiz.essay && quiz.essay[quiz.essay.length - 1]) || (quiz.mcq && quiz.mcq[quiz.mcq.length - 1]);
      subtopics.push({
        id: lesson.id + '-sub-apps',
        title: 'التطبيقات الحياتية ومسائل التحدي',
        badge: '🚀 تطبيق وتفكير عليا (جاهزة)',
        source: 'builtin',
        summary: [appText, hotText].filter(Boolean).join(' • ') || 'توظيف مفاهيم الدرس في المواقف الحياتية ومسائل القدرات والتحصيلي.',
        steps: [
          asText(st1.real_world_intro) || appText || 'ترجمة المعطيات اللفظية إلى علاقة رياضية دقيقة.',
          asText(st4.independent_practice) || 'تنفيذ الحل الجبري أو الهندسي بخطوات مرتبة.',
          hotText || 'ربط الناتج بالسياق الحقيقي للمسألة والتحقق من القيود المنطقية.'
        ].filter(Boolean),
        workedExample: pickExample(3),
        altExamples: pool.slice(0, 4),
        commonMistake: 'لا تتوقف عند الرقم الحسابي المجرد في المسائل اللفظية؛ أرفق التفسير والوحدة وتأكد من منطقية الحل.',
        quickCheck: challengeQ
          ? {
              question: asText(challengeQ.q),
              answer: asText(challengeQ.ans) || asText(challengeQ.options && challengeQ.options[typeof challengeQ.ans === 'number' ? challengeQ.ans : (challengeQ.correct || 0)])
            }
          : { question: 'اذكر تطبيقاً حياتياً واحداً يعتمد على هذا الدرس.', answer: appText || asText(st1.real_world_intro) }
      });
    }

    return subtopics;
  }

  function loadStoreMap(storageKey) {
    try {
      if (typeof localStorage === 'undefined') return {};
      const raw = localStorage.getItem(storageKey);
      const parsed = raw ? JSON.parse(raw) : {};
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (e) {
      return {};
    }
  }

  function saveStoreMap(storageKey, data) {
    try {
      if (typeof localStorage === 'undefined') return;
      localStorage.setItem(storageKey, JSON.stringify(data));
    } catch (e) { /* ignore quota errors */ }
  }

  function getTeacherSubtopics(lessonId) {
    const map = loadStoreMap(TEACHER_STORE_KEY);
    return Array.isArray(map[lessonId]) ? map[lessonId] : [];
  }

  function saveTeacherSubtopic(lessonId, item) {
    const map = loadStoreMap(TEACHER_STORE_KEY);
    const list = Array.isArray(map[lessonId]) ? map[lessonId] : [];
    list.unshift(item);
    map[lessonId] = list;
    saveStoreMap(TEACHER_STORE_KEY, map);

    // Optional cloud sync if Firebase Firestore is active
    try {
      if (global.firebase && global.firebase.apps && global.firebase.apps.length && typeof global.firebase.firestore === 'function') {
        global.firebase.firestore().collection('teacher_subtopics').doc(item.id).set(Object.assign({ lessonId: lessonId, updatedAt: Date.now() }, item)).catch(function () {});
      }
    } catch (e) {}
  }

  function getCacheKey(lessonId, query, level) {
    const utils = getUtils();
    const normQ = utils && utils.normalizeSearchText ? utils.normalizeSearchText(query) : String(query || '').toLowerCase().trim();
    return lessonId + '|' + (level || 'متوسط منهجي') + '|' + normQ;
  }

  function getCachedExplanation(key) {
    const cache = loadStoreMap(CACHE_STORE_KEY);
    return cache[key] || null;
  }

  function setCachedExplanation(key, entry) {
    const cache = loadStoreMap(CACHE_STORE_KEY);
    const keys = Object.keys(cache);
    if (keys.length >= 60) {
      delete cache[keys[0]];
    }
    cache[key] = entry;
    saveStoreMap(CACHE_STORE_KEY, cache);
  }

  function tokenizeQuery(query) {
    const utils = getUtils();
    const norm = utils && utils.normalizeSearchText ? utils.normalizeSearchText(query) : String(query || '').toLowerCase();
    return norm
      .split(/[\s،,.;:!؟?()\[\]{}"'\/\\+\-*=<>]+/)
      .map(function (t) { return t.trim(); })
      .filter(function (t) { return t.length >= 2 && !STOP_WORDS.has(t); });
  }

  function scoreText(text, tokens) {
    if (!text || !tokens.length) return 0;
    const utils = getUtils();
    const hay = utils && utils.normalizeSearchText ? utils.normalizeSearchText(text) : String(text).toLowerCase();
    let score = 0;
    tokens.forEach(function (tok) {
      if (hay.indexOf(tok) !== -1) score += (tok.length >= 4 ? 3 : 2);
    });
    return score;
  }

  /**
   * محلّل وحلّال رياضي محلي دقيق وآمن (دون eval) يحل المسائل المدخلة خطوة بخطوة
   */
  const AR_TO_LAT_VAR = { 'س': 'x', 'ص': 'y', 'ع': 'z', 'ن': 'n', 'م': 'm', 'ك': 'k', 'ت': 't' };
  const LAT_TO_AR_VAR = { 'x': 'س', 'y': 'ص', 'z': 'ع', 'n': 'ن', 'm': 'م', 'k': 'ك', 't': 'ت' };
  const MATH_FUNCS = new Set(['sqrt', 'abs', 'sin', 'cos', 'tan', 'log', 'ln']);

  function replaceBraceCommand(str, cmd, replacer) {
    let out = String(str || '');
    let guard = 0;
    while (out.indexOf(cmd + '{') !== -1 && guard++ < 25) {
      const idx = out.indexOf(cmd + '{');
      const open1 = idx + cmd.length;
      let depth = 0;
      let close1 = -1;
      for (let i = open1; i < out.length; i++) {
        if (out[i] === '{') depth++;
        else if (out[i] === '}') {
          depth--;
          if (depth === 0) { close1 = i; break; }
        }
      }
      if (close1 === -1) break;
      const arg1 = out.slice(open1 + 1, close1);
      if (replacer.length === 1) {
        out = out.slice(0, idx) + replacer(arg1) + out.slice(close1 + 1);
      } else {
        let pos2 = close1 + 1;
        while (pos2 < out.length && /\s/.test(out[pos2])) pos2++;
        if (out[pos2] !== '{') break;
        let d2 = 0;
        let close2 = -1;
        for (let j = pos2; j < out.length; j++) {
          if (out[j] === '{') d2++;
          else if (out[j] === '}') {
            d2--;
            if (d2 === 0) { close2 = j; break; }
          }
        }
        if (close2 === -1) break;
        const arg2 = out.slice(pos2 + 1, close2);
        out = out.slice(0, idx) + replacer(arg1, arg2) + out.slice(close2 + 1);
      }
    }
    return out;
  }

  function normalizeMathExpr(raw) {
    if (!raw) return '';
    let s = String(raw);
    const utils = getUtils();
    if (utils && typeof utils.toWesternDigits === 'function') {
      s = utils.toWesternDigits(s);
    } else {
      s = s.replace(/[٠-٩]/g, function (d) { return String('٠١٢٣٤٥٦٧٨٩'.indexOf(d)); });
    }
    s = s
      .replace(/٫/g, '.')
      .replace(/،/g, ',')
      .replace(/[−–—]/g, '-')
      .replace(/[×·∗]/g, '*')
      .replace(/÷/g, '/')
      .replace(/\$/g, '')
      .replace(/\\left\b|\\right\b/g, '')
      .replace(/\\(?:times|cdot)\b/g, '*')
      .replace(/\\div\b/g, '/')
      .replace(/\\pi\b|π/g, 'pi');

    s = replaceBraceCommand(s, '\\dfrac', function (a, b) { return '((' + a + ')/(' + b + '))'; });
    s = replaceBraceCommand(s, '\\frac', function (a, b) { return '((' + a + ')/(' + b + '))'; });
    s = replaceBraceCommand(s, '\\sqrt', function (a) { return 'sqrt(' + a + ')'; });

    // Convert ^{exp} -> ^(exp)
    s = s.replace(/\^\s*\{([^}]+)\}/g, '^($1)');

    // Superscripts like ²³ -> ^23
    const supMap = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-' };
    s = s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+/g, function (m) {
      return '^(' + m.split('').map(function (c) { return supMap[c] || ''; }).join('') + ')';
    });

    // Arabic / Unicode square root
    s = s.replace(/(?:جذر|√)\s*\(/g, 'sqrt(');
    s = s.replace(/(?:جذر|√)\s*([0-9]+(?:\.[0-9]+)?|[a-zA-Zسصعنمكت])/g, 'sqrt($1)');

    // Absolute value bars |...|
    for (let k = 0; k < 2; k++) {
      s = s.replace(/\|([^|]+)\|/g, 'abs($1)');
    }

    // Isolated Arabic math variables -> Latin equivalents (ignore words like حساب / قيمة)
    s = s.replace(/(^|[^A-Za-z\u0621-\u064A])([سصعنمكت])(?![A-Za-z\u0621-\u064A])/g, function (_, pre, ch) {
      return pre + (AR_TO_LAT_VAR[ch] || ch);
    });

    return s.trim();
  }

  function tokenizeMath(normStr) {
    const tokens = [];
    const s = String(normStr || '');
    let i = 0;
    while (i < s.length) {
      const ch = s[i];
      if (/\s/.test(ch)) { i++; continue; }
      if (/[0-9.]/.test(ch)) {
        let j = i;
        while (j < s.length && /[0-9.]/.test(s[j])) j++;
        const numStr = s.slice(i, j);
        if (!/^\d*\.?\d+$/.test(numStr)) return null;
        tokens.push({ type: 'num', val: parseFloat(numStr) });
        i = j;
        continue;
      }
      if (/[A-Za-z]/.test(ch)) {
        // Match multi-char known functions/constants first, else single variable char (so xy -> x * y)
        const rest = s.slice(i);
        const fnM = rest.match(/^(sqrt|abs|sin|cos|tan|log|ln|pi)(?![A-Za-z])/i);
        if (fnM) {
          tokens.push({ type: 'id', val: fnM[1].toLowerCase() });
          i += fnM[1].length;
        } else {
          tokens.push({ type: 'id', val: ch });
          i++;
        }
        continue;
      }
      if ('+-*/^'.indexOf(ch) !== -1) {
        tokens.push({ type: 'op', val: ch });
        i++;
        continue;
      }
      if (ch === '(' || ch === '[') { tokens.push({ type: 'lp' }); i++; continue; }
      if (ch === ')' || ch === ']') { tokens.push({ type: 'rp' }); i++; continue; }
      return null;
    }

    // Insert implicit multiplication (e.g. 2x, -x -> -1*x via unary, 3(4), (x+1)(x-2), 2sqrt(9))
    const expanded = [];
    for (let t = 0; t < tokens.length; t++) {
      const curr = tokens[t];
      if (t > 0) {
        const prev = tokens[t - 1];
        const prevIsVal = prev.type === 'num' || prev.type === 'rp' || (prev.type === 'id' && !MATH_FUNCS.has(prev.val));
        const currStartsFactor = curr.type === 'num' || curr.type === 'lp' || curr.type === 'id';
        if (prevIsVal && currStartsFactor) {
          expanded.push({ type: 'op', val: '*' });
        }
      }
      expanded.push(curr);
    }
    return expanded;
  }

  function evalMathAst(exprStr, varsMap) {
    const norm = normalizeMathExpr(exprStr);
    const tokens = tokenizeMath(norm);
    if (!tokens || !tokens.length) return { ok: false, error: 'PARSE' };
    const vars = varsMap || {};
    let pos = 0;

    function peek() { return tokens[pos] || null; }
    function consume() { return tokens[pos++]; }

    function parseAddSub() {
      let left = parseMulDiv();
      while (peek() && peek().type === 'op' && (peek().val === '+' || peek().val === '-')) {
        const op = consume().val;
        const right = parseMulDiv();
        left = op === '+' ? left + right : left - right;
      }
      return left;
    }

    function parseMulDiv() {
      let left = parseUnary();
      while (peek() && peek().type === 'op' && (peek().val === '*' || peek().val === '/')) {
        const op = consume().val;
        const right = parseUnary();
        if (op === '/') {
          if (Math.abs(right) < 1e-12) throw new Error('DIV_ZERO');
          left = left / right;
        } else {
          left = left * right;
        }
      }
      return left;
    }

    // Unary has LOWER precedence than exponentiation so -x^2 === -(x^2)
    function parseUnary() {
      if (peek() && peek().type === 'op' && (peek().val === '+' || peek().val === '-')) {
        const op = consume().val;
        const inner = parseUnary();
        return op === '-' ? -inner : inner;
      }
      return parsePower();
    }

    function parsePower() {
      const base = parseAtom();
      if (peek() && peek().type === 'op' && peek().val === '^') {
        consume();
        const exp = parseUnary();
        const res = Math.pow(base, exp);
        if (!Number.isFinite(res)) throw new Error('DOMAIN');
        return res;
      }
      return base;
    }

    function parseAtom() {
      const tok = peek();
      if (!tok) throw new Error('UNEXPECTED_END');
      if (tok.type === 'num') {
        consume();
        return tok.val;
      }
      if (tok.type === 'lp') {
        consume();
        const val = parseAddSub();
        if (!peek() || peek().type !== 'rp') throw new Error('MISSING_PAREN');
        consume();
        return val;
      }
      if (tok.type === 'id') {
        consume();
        if (tok.val === 'pi') return Math.PI;
        if (tok.val === 'e' && !Object.prototype.hasOwnProperty.call(vars, 'e')) return Math.E;
        if (MATH_FUNCS.has(tok.val)) {
          const arg = peek() && peek().type === 'lp' ? parseAtom() : parseUnary();
          if (tok.val === 'sqrt') {
            if (arg < -1e-12) throw new Error('NEG_SQRT');
            return Math.sqrt(Math.max(0, arg));
          }
          if (tok.val === 'abs') return Math.abs(arg);
          if (tok.val === 'sin') return Math.sin(arg);
          if (tok.val === 'cos') return Math.cos(arg);
          if (tok.val === 'tan') return Math.tan(arg);
          if (tok.val === 'log') { if (arg <= 0) throw new Error('DOMAIN'); return Math.log10(arg); }
          if (tok.val === 'ln') { if (arg <= 0) throw new Error('DOMAIN'); return Math.log(arg); }
        }
        if (Object.prototype.hasOwnProperty.call(vars, tok.val)) {
          return Number(vars[tok.val]);
        }
        throw new Error('UNKNOWN_VAR:' + tok.val);
      }
      throw new Error('UNEXPECTED_TOKEN');
    }

    try {
      const value = parseAddSub();
      if (pos !== tokens.length || !Number.isFinite(value)) {
        return { ok: false, error: 'TRAILING' };
      }
      return { ok: true, value: Math.abs(value) < 1e-11 ? 0 : value };
    } catch (err) {
      return { ok: false, error: (err && err.message) || 'EVAL' };
    }
  }

  function gcdInt(a, b) {
    let x = Math.abs(Math.round(a));
    let y = Math.abs(Math.round(b));
    while (y) { const t = y; y = x % y; x = t; }
    return x || 1;
  }

  function toExactFraction(val, maxDen) {
    if (!Number.isFinite(val)) return null;
    if (Math.abs(val - Math.round(val)) < 1e-9) {
      return { num: Math.round(val), den: 1 };
    }
    const limit = maxDen || 36;
    for (let d = 2; d <= limit; d++) {
      const n = Math.round(val * d);
      if (Math.abs(val - n / d) < 1e-9) {
        const g = gcdInt(n, d);
        return { num: n / g, den: d / g };
      }
    }
    return null;
  }

  function formatExactNumber(val, isSec, forTex) {
    if (!Number.isFinite(val)) return 'غير معرّف';
    const clean = Math.abs(val) < 1e-10 ? 0 : val;
    const frac = toExactFraction(clean, 24);
    if (frac) {
      if (frac.den === 1) {
        return fmtPlainNum(String(frac.num), isSec);
      }
      const sign = frac.num < 0 ? '-' : '';
      const a = Math.abs(frac.num);
      const b = frac.den;
      if (isSec) {
        return forTex ? (sign + '\\dfrac{' + a + '}{' + b + '}') : (sign + a + '/' + b);
      }
      return fmtPlainNum(sign + a + '/' + b, false);
    }
    const rounded = Number(clean.toFixed(4)).toString();
    if (isSec) return rounded;
    return fmtPlainNum(rounded.replace('.', '٫'), false);
  }

  function wrapMathIfSec(texBody, isSec) {
    if (!isSec) return fmtPlainNum(texBody, false);
    return '$' + toWesternStr(texBody) + '$';
  }

  function toWesternStr(str) {
    const utils = getUtils();
    const s = String(str || '').replace(/٫/g, '.').replace(/،/g, ',').replace(/[−–—]/g, '-');
    return utils && typeof utils.toWesternDigits === 'function'
      ? utils.toWesternDigits(s)
      : s.replace(/[٠-٩]/g, function (d) { return String('٠١٢٣٤٥٦٧٨٩'.indexOf(d)); });
  }

  function formatDisplayExpr(rawExpr, isSec, preferredVar) {
    let s = String(rawExpr || '').trim();
    if (isSec) {
      s = toWesternStr(s)
        .replace(/×/g, '\\cdot ')
        .replace(/÷/g, '/')
        .replace(/√\s*\(([^)]+)\)/g, '\\sqrt{$1}')
        .replace(/√\s*([0-9a-zA-Z]+)/g, '\\sqrt{$1}')
        .replace(/\$/g, '');
      // Convert any Arabic variable letters to Latin
      s = s.replace(/(^|[^A-Za-z\u0621-\u064A])([سصعنمكت])(?![A-Za-z\u0621-\u064A])/g, function (_, pre, ch) {
        return pre + (AR_TO_LAT_VAR[ch] || preferredVar || ch);
      });
      return s.trim();
    }
    // Non-secondary: Eastern digits & Arabic symbols
    s = s.replace(/\*/g, '×').replace(/\$/g, '').replace(/[−–—]/g, '-');
    return fmtPlainNum(s, false);
  }

  function splitTopLevelTerms(normExpr) {
    const s = String(normExpr || '').replace(/\s+/g, '');
    if (!s) return null;
    const terms = [];
    let depth = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
      const ch = s[i];
      if (ch === '(') depth++;
      else if (ch === ')') depth--;
      else if (depth === 0 && i > start && (ch === '+' || ch === '-') && s[i - 1] !== '^' && s[i - 1] !== '*' && s[i - 1] !== '/') {
        terms.push(s.slice(start, i));
        start = i;
      }
    }
    terms.push(s.slice(start));
    return terms.length >= 2 ? terms : null;
  }

  function substituteVariableDisplay(dispExpr, varSym, subText, isSec) {
    let s = String(dispExpr || '');
    const wrapSub = '(' + subText + ')';
    if (/[\u0621-\u064A]/.test(varSym)) {
      const re = new RegExp('(^|[^A-Za-z\\u0621-\\u064A])' + varSym.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![A-Za-z\\u0621-\\u064A])', 'g');
      s = s.replace(re, '$1' + wrapSub);
    } else {
      const lat = AR_TO_LAT_VAR[varSym] || varSym;
      const re = new RegExp('(^|[^A-Za-z])' + lat.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?![A-Za-z])', 'g');
      s = s.replace(re, '$1' + wrapSub);
    }
    return isSec ? s : fmtPlainNum(s, false);
  }

  function buildSolvedEntry(lesson, query, level, cfg) {
    const isSec = isSecondaryLesson(lesson);
    const sum = (lesson && lesson.summary) || {};
    const ruleTail = sum.golden_rule ? (' (يرتبط بالقاعدة: ' + asText(sum.golden_rule) + ')') : '';
    return {
      id: (lesson ? lesson.id : 'math') + '-solved-' + Date.now(),
      title: query ? ('شرح جزئية: ' + fmtPlainNum(query, isSec)) : cfg.title,
      badge: '🧮 حل فوري دقيق لمسألتك خطوة بخطوة (' + (level || 'متوسط منهجي') + ')',
      source: 'local-solver',
      summary: fmtPlainNum(cfg.summary + ruleTail, isSec),
      steps: (cfg.steps || []).map(function (s) { return fmtPlainNum(s, isSec); }),
      workedExample: normalizeExampleObj({
        problem: fmtPlainNum(cfg.problem, isSec),
        steps: (cfg.exSteps || []).map(function (s) { return fmtPlainNum(s, isSec); }),
        finalAnswer: fmtPlainNum(cfg.finalAnswer, isSec),
        isExactUserSolution: true
      }, isSec),
      commonMistake: fmtPlainNum(cfg.commonMistake || (lesson && lesson.prep && lesson.prep.station3 && lesson.prep.station3.misconceptions) || 'تحقق من الإشارات وأولوية العمليات الحسابية والتعويض الصحيح.', isSec),
      quickCheck: cfg.quickCheck || { question: '', answer: '' }
    };
  }

  function detectFunctionEvaluation(query, isSec, lesson) {
    const cleanQ = String(query || '').trim();
    const fnMatch = cleanQ.match(/(?:^|[^A-Za-z\u0621-\u064A])(هـ|[دقتركمعلfghpqrFGHPQ])\s*\(\s*([سصعنمكتa-zA-Z])\s*\)\s*=\s*([\s\S]+)$/);
    if (!fnMatch) return null;

    const fnName = fnMatch[1];
    const varOrig = fnMatch[2];
    const varLat = AR_TO_LAT_VAR[varOrig] || varOrig;
    const tail = fnMatch[3].trim();

    // Split RHS from trailing question ("، فأوجد قيمة د(٣)", "أوجد ق(2)", "when x = 3", etc.)
    const sepRe = new RegExp(
      '[،,;?!؟]|\\s+(?:فأوجد|أوجد|فاحسب|احسب|فما|ما\\s*قيمة|قيمة|حيث|عندما|عند|find|evaluate|compute|calculate|then|where)(?=[\\s،,;?!؟]|$)|\\s+(?=' +
      fnName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*\\()',
      'i'
    );
    const sepMatch = sepRe.exec(tail);
    const rhsRaw = (sepMatch ? tail.slice(0, sepMatch.index) : tail).trim().replace(/[.=]+$/, '').trim();
    const rest = sepMatch ? tail.slice(sepMatch.index).trim() : '';
    if (!rhsRaw) return null;

    let argRaw = '';
    const escFn = fnName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const callRe = new RegExp(escFn + '\\s*\\(\\s*([^()]+(?:\\([^()]*\\)[^()]*)?)\\s*\\)');
    const callM = (rest || '').match(callRe);
    if (callM) {
      argRaw = callM[1].trim();
    } else {
      const escVar = varOrig.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const atRe = new RegExp('(?:عندما|عند|when|at)\\s*' + escVar + '\\s*=\\s*([^\\s،,;؟?!]+)', 'i');
      const atM = cleanQ.match(atRe);
      if (atM) argRaw = atM[1].trim();
    }
    if (!argRaw) return null;

    const argEval = evalMathAst(argRaw);
    if (!argEval.ok) return null;
    const argVal = argEval.value;
    const vars = {};
    vars[varLat] = argVal;
    const valRes = evalMathAst(rhsRaw, vars);

    const dispVar = isSec ? varLat : (LAT_TO_AR_VAR[varOrig] || varOrig);
    const dispFn = isSec ? (AR_TO_LAT_VAR[fnName] ? 'f' : fnName) : fnName;
    const dispArg = formatExactNumber(argVal, isSec, true);
    const dispArgPlain = formatExactNumber(argVal, isSec, false);
    const dispRhs = formatDisplayExpr(rhsRaw, isSec, dispVar);
    const subExpr = substituteVariableDisplay(dispRhs, dispVar, dispArg, isSec).replace(/(^|[(+=])\s*-\s+\(/g, '$1-(');
    const callLabel = dispFn + '(' + dispArg + ')';
    const defLabel = dispFn + '(' + dispVar + ') = ' + dispRhs;

    if (!valRes.ok && valRes.error === 'DIV_ZERO') {
      return buildSolvedEntry(lesson, query, null, {
        title: 'حساب قيمة الدالة',
        summary: 'لإيجاد قيمة الدالة عند عدد معطى، نعوض بهذا العدد مكان المتغير ونتأكد أولاً أن المقام لا يساوي الصفر.',
        steps: [
          'نعوّض بالعدد المعطى مكان المتغير في قاعدة الدالة.',
          'إذا أصبح المقام صفراً فإن الدالة تكون غير معرّفة عند هذه القيمة.'
        ],
        problem: query,
        exSteps: [
          'نكتب قاعدة الدالة: ' + wrapMathIfSec(defLabel, isSec),
          'نعوّض عن ' + wrapMathIfSec(dispVar + ' = ' + dispArg, isSec) + ' فنجد أن المقام يصبح مساوياً للصفر.',
          'القسمة على صفر غير معرّفة؛ إذن ' + wrapMathIfSec(callLabel, isSec) + ' غير معرّفة.'
        ],
        finalAnswer: wrapMathIfSec(callLabel, isSec) + ' غير معرّفة',
        commonMistake: 'القسمة على الصفر لا تساوي صفراً بل تجعل العبارة غير معرّفة.'
      });
    }
    if (!valRes.ok) return null;

    const finalNumTex = formatExactNumber(valRes.value, isSec, true);
    const finalEqTex = callLabel + ' = ' + finalNumTex;

    const exSteps = [
      'نكتب قاعدة الدالة المعطاة: ' + wrapMathIfSec(defLabel, isSec),
      'نعوض عن ' + (isSec ? ('$' + dispVar + '$') : dispVar) + ' بالعدد ' + wrapMathIfSec(dispArg, isSec) + ': ' + wrapMathIfSec(callLabel + ' = ' + subExpr, isSec)
    ];

    // Add intermediate term-by-term simplification step when there are >= 2 terms
    const normRhs = normalizeMathExpr(rhsRaw);
    const rawTerms = splitTopLevelTerms(normRhs);
    if (rawTerms && rawTerms.length >= 2) {
      let termStr = '';
      let allTermsOk = true;
      for (let i = 0; i < rawTerms.length; i++) {
        const tEval = evalMathAst(rawTerms[i], vars);
        if (!tEval.ok) { allTermsOk = false; break; }
        const tv = tEval.value;
        const tvFmt = formatExactNumber(Math.abs(tv), isSec, true);
        if (i === 0) {
          termStr += (tv < 0 ? '-' : '') + tvFmt;
        } else {
          termStr += (tv < 0 ? ' - ' : ' + ') + tvFmt;
        }
      }
      if (allTermsOk) {
        const fullCalc = termStr + ' = ' + finalNumTex;
        if (normCmpText(termStr) !== normCmpText(subExpr)) {
          exSteps.push('نبسّط القوى والضرب ثم نجمع/نطرح: ' + wrapMathIfSec(fullCalc, isSec));
        } else {
          exSteps.push('نحسب الناتج: ' + wrapMathIfSec(fullCalc, isSec));
        }
      } else {
        exSteps.push('نحسب الناتج النهائي: ' + wrapMathIfSec(finalEqTex, isSec));
      }
    } else {
      exSteps.push('نبسّط العبارة الحسابية فنحصل على: ' + wrapMathIfSec(finalEqTex, isSec));
    }

    // Generate a tied quickCheck for argVal + 1
    const nextArg = argVal + 1;
    const nextVars = {};
    nextVars[varLat] = nextArg;
    const nextRes = evalMathAst(rhsRaw, nextVars);
    const quickCheck = nextRes.ok ? {
      question: 'باستعمال الدالة نفسها ' + wrapMathIfSec(defLabel, isSec) + '، أوجد قيمة ' + wrapMathIfSec(dispFn + '(' + formatExactNumber(nextArg, isSec, true) + ')', isSec) + '.',
      answer: wrapMathIfSec(dispFn + '(' + formatExactNumber(nextArg, isSec, true) + ') = ' + formatExactNumber(nextRes.value, isSec, true), isSec)
    } : null;

    return buildSolvedEntry(lesson, query, null, {
      title: 'حساب قيمة الدالة',
      summary: 'لإيجاد قيمة الدالة ' + wrapMathIfSec(dispFn + '(' + dispVar + ')', isSec) + ' عند القيمة ' + wrapMathIfSec(dispArgPlain, isSec) + '، نستبدل كل ' + (isSec ? ('$' + dispVar + '$') : dispVar) + ' في قاعدة الدالة بالعدد (' + dispArgPlain + ') ثم نحسب الناتج وفق ترتيب العمليات.',
      steps: [
        'حدد قاعدة الدالة المعطاة في السؤال.',
        'ضع قيمة المتغير المعطاة بين قوسين مكان كل ظهور للمتغير (خاصة عند وجود إشارة سالبة).',
        'نفّذ الأسس أولاً، ثم الضرب والقسمة، وأخيراً الجمع والطرح.'
      ],
      problem: query,
      exSteps: exSteps,
      finalAnswer: wrapMathIfSec(finalEqTex, isSec),
      commonMistake: 'الخطأ الأكثر شيوعاً هو نسيان الأقواس حول العدد السالب أو الخلط بين الإشارة السالبة أمام المتغير ومعامل المتغير، مثل كتابة -(' + dispArgPlain + ') على أنها موجبة دون مبرر.',
      quickCheck: quickCheck
    });
  }

  function detectLinearOrQuadraticEquation(query, isSec, lesson) {
    const raw = String(query || '').trim();
    if (raw.indexOf('=') === -1) return null;
    // Skip function definitions like د(س) = ...
    if (/(?:^|[^A-Za-z\u0621-\u064A])(?:هـ|[دقتركمعلfghpqrFGHPQ])\s*\(\s*[سصعنمكتa-zA-Z]\s*\)\s*=/.test(raw)) {
      return null;
    }
    const stripped = raw
      .replace(/^(?:حل|أوجد\s*حل|أوجد\s*قيمة(?:\s*المتغير)?(?:\s*[سصعنمكتa-zA-Z])?(?:\s*في)?|ما\s*حل|solve(?:\s+for\s+[a-zA-Z])?|find\s+[a-zA-Z]\s*(?:if|for)?)(?:\s+(?:المعادلة|التالية|الآتية))*(?:\s*[:：])?\s*/i, '')
      .replace(/[؟?!.،,;]+$/g, '')
      .trim();
    const parts = stripped.split('=');
    if (parts.length !== 2) return null;
    const lhsRaw = parts[0].trim();
    const rhsRaw = parts[1].trim();
    if (!lhsRaw || !rhsRaw) return null;

    const lhsNorm = normalizeMathExpr(lhsRaw);
    const rhsNorm = normalizeMathExpr(rhsRaw);
    // Find distinct variables (exclude math function names & 'pi')
    const combinedNorm = lhsNorm + ' ' + rhsNorm;
    const cleanedIds = combinedNorm.replace(/\b(?:sqrt|abs|sin|cos|tan|log|ln|pi)\b/g, ' ');
    const varSet = new Set(cleanedIds.match(/[a-zA-Z]/g) || []);
    if (varSet.size !== 1) return null;

    const varLat = Array.from(varSet)[0];
    const origHadArabic = new RegExp('(^|[^\\u0621-\\u064A])' + (LAT_TO_AR_VAR[varLat] || '__') + '(?![\\u0621-\\u064A])').test(stripped);
    const dispVar = isSec ? varLat : (origHadArabic ? LAT_TO_AR_VAR[varLat] : varLat);

    function evalSide(sideExpr, v) {
      const m = {};
      m[varLat] = v;
      return evalMathAst(sideExpr, m);
    }

    const pts = [-2, -1, 0, 1, 2, 3];
    const F = {};
    const L = {};
    const R = {};
    for (let i = 0; i < pts.length; i++) {
      const v = pts[i];
      const lr = evalSide(lhsRaw, v);
      const rr = evalSide(rhsRaw, v);
      if (!lr.ok || !rr.ok) return null;
      L[v] = lr.value;
      R[v] = rr.value;
      F[v] = lr.value - rr.value;
    }

    const a2 = (F[2] - 2 * F[1] + F[0]) / 2;
    const c2 = F[0];
    const b2 = F[1] - a2 - c2;

    // Verify exact quadratic/linear fit at -2, -1, 3
    for (let i = 0; i < pts.length; i++) {
      const v = pts[i];
      const pred = a2 * v * v + b2 * v + c2;
      if (Math.abs(pred - F[v]) > 1e-7) return null;
    }

    const dispEq = formatDisplayExpr(lhsRaw, isSec, dispVar) + ' = ' + formatDisplayExpr(rhsRaw, isSec, dispVar);

    // Case A: Linear (a2 === 0)
    if (Math.abs(a2) < 1e-8) {
      const coef = b2;
      const constTerm = c2; // coef * x + constTerm = 0
      if (Math.abs(coef) < 1e-9) {
        const isIdentity = Math.abs(constTerm) < 1e-9;
        return buildSolvedEntry(lesson, query, null, {
          title: 'حل المعادلة الخطية',
          summary: isIdentity ? 'عند تساوي الطرفين في المعاملات والحدود الثابتة تكون المعادلة متطابقة ومجموعة حلها جميع الأعداد الحقيقية.' : 'عند تساوي معامل المتغير في الطرفين واختلاف الحد الثابت تستحيل المعادلة ولا يوجد لها حل.',
          steps: ['نجمع حدود المتغير في طرف والحدود الثابتة في الطرف الآخر.'],
          problem: query,
          exSteps: [
            'المعادلة المعطاة: ' + wrapMathIfSec(dispEq, isSec),
            isIdentity ? 'بطرح المتغير من الطرفين ينتج عبارة صحيحة دائماً (٠ = ٠).' : 'بطرح المتغير من الطرفين ينتج تناقض عددي؛ لذا لا يوجد حل.'
          ],
          finalAnswer: isIdentity ? 'مجموعة الحل: جميع الأعداد الحقيقية' : 'لا يوجد حل (مجموعة الحل: ∅)'
        });
      }

      const sol = -constTerm / coef;
      const solFmt = formatExactNumber(sol, isSec, true);
      const rhsConst = formatExactNumber(-constTerm, isSec, true);
      const coefFmt = formatExactNumber(coef, isSec, true);
      const coefTermStr = (coef === 1 ? '' : (coef === -1 ? '-' : coefFmt)) + dispVar;
      const lhsCheck = evalSide(lhsRaw, sol);

      const exSteps = ['نكتب المعادلة المعطاة: ' + wrapMathIfSec(dispEq, isSec)];
      if (Math.abs(coef - 1) > 1e-9 || Math.abs(R[0] - R[1]) > 1e-9 || Math.abs(L[0]) > 1e-9) {
        exSteps.push('ننقل حدود المتغير في طرف والحدود الثابتة في الطرف الآخر: ' + wrapMathIfSec(coefTermStr + ' = ' + rhsConst, isSec));
      }
      if (Math.abs(coef - 1) > 1e-9) {
        exSteps.push('نقسم الطرفين على المعامل (' + formatExactNumber(coef, isSec, false) + '): ' + wrapMathIfSec(dispVar + ' = ' + solFmt, isSec));
      }
      if (lhsCheck.ok) {
        exSteps.push('التحقق: عند تعويض ' + wrapMathIfSec(dispVar + ' = ' + solFmt, isSec) + ' يتساوى الطرفان عند القيمة ' + wrapMathIfSec(formatExactNumber(lhsCheck.value, isSec, true), isSec) + '.');
      }

      return buildSolvedEntry(lesson, query, null, {
        title: 'حل المعادلة الخطية في متغير واحد',
        summary: 'نحل المعادلة الخطية بجعل حدود المتغير ' + (isSec ? ('$' + dispVar + '$') : dispVar) + ' في طرف واحد والأعداد الثابتة في الطرف الآخر، ثم نقسم على معامل المتغير.',
        steps: [
          'انقل الحدود التي تحوي المتغير إلى طرف والحدود الثابتة إلى الطرف الآخر مع عكس الإشارة.',
          'بسط كل طرف بجمع الحدود المتشابهة.',
          'اقسم كلا الطرفين على معامل المتغير ثم تحقق بالتعويض.'
        ],
        problem: query,
        exSteps: exSteps,
        finalAnswer: wrapMathIfSec(dispVar + ' = ' + solFmt, isSec),
        commonMistake: 'نسيان عكس إشارة الحد عند نقله للطرف الآخر أو القسمة على إشارة سالبة دون الانتباه لإشارة الناتج.',
        quickCheck: {
          question: 'تحقق من فهمك: إذا استبدلنا ' + wrapMathIfSec(dispVar + ' = ' + solFmt, isSec) + ' في المعادلة ' + wrapMathIfSec(dispEq, isSec) + '، فما قيمة كل طرف؟',
          answer: lhsCheck.ok ? ('كلا الطرفين يساوي ' + wrapMathIfSec(formatExactNumber(lhsCheck.value, isSec, true), isSec)) : ''
        }
      });
    }

    // Case B: Quadratic (|a2| > 1e-8)
    let a = a2, b = b2, c = c2;
    if (a < 0) { a = -a; b = -b; c = -c; }
    const disc = b * b - 4 * a * c;
    const aStr = (Math.abs(a - 1) < 1e-9 ? '' : formatExactNumber(a, isSec, true)) + dispVar + '^2';
    const bStr = Math.abs(b) < 1e-9 ? '' : ((b > 0 ? ' + ' : ' - ') + (Math.abs(Math.abs(b) - 1) < 1e-9 ? '' : formatExactNumber(Math.abs(b), isSec, true)) + dispVar);
    const cStr = Math.abs(c) < 1e-9 ? '' : ((c > 0 ? ' + ' : ' - ') + formatExactNumber(Math.abs(c), isSec, true));
    const stdEq = aStr + bStr + cStr + ' = ' + (isSec ? '0' : '٠');

    const exSteps = [
      'نضع المعادلة في الصورة القياسية: ' + wrapMathIfSec(stdEq, isSec),
      'نحدد المعاملات: ' + wrapMathIfSec('a = ' + formatExactNumber(a, isSec, true), isSec).replace(/\ba\b/, isSec ? 'a' : 'أ') + '، و' + wrapMathIfSec('b = ' + formatExactNumber(b, isSec, true), isSec).replace(/\bb\b/, isSec ? 'b' : 'ب') + '، و' + wrapMathIfSec('c = ' + formatExactNumber(c, isSec, true), isSec).replace(/\bc\b/, isSec ? 'c' : 'جـ'),
      'نحسب المميز: ' + (isSec ? ('$\\Delta = b^2 - 4ac = ' + formatExactNumber(disc, true, true) + '$') : ('المميز = ب^٢ - ٤أجـ = ' + formatExactNumber(disc, false, false)))
    ];

    let finalAns = '';
    if (disc < -1e-9) {
      if (isSec) {
        const realPart = -b / (2 * a);
        const imagPart = Math.sqrt(-disc) / (2 * a);
        const rFmt = Math.abs(realPart) < 1e-9 ? '' : formatExactNumber(realPart, true, true);
        const iFmt = Math.abs(imagPart - 1) < 1e-9 ? 'i' : (formatExactNumber(imagPart, true, true) + 'i');
        const rootTex = dispVar + ' = ' + (rFmt ? (rFmt + ' \\pm ' + iFmt) : ('\\pm ' + iFmt));
        exSteps.push('بما أن المميز سالب توجد جذور مركبة مترافقة: $' + rootTex + '$');
        finalAns = '$' + rootTex + '$';
      } else {
        exSteps.push('بما أن المميز سالب (< ٠)، فلا توجد حلول حقيقية لهذه المعادلة.');
        finalAns = 'لا توجد حلول حقيقية (مجموعة الحل: ∅)';
      }
    } else if (Math.abs(disc) < 1e-9) {
      const r0 = formatExactNumber(-b / (2 * a), isSec, true);
      exSteps.push('المميز يساوي صفراً؛ إذن للمعادلة جذر حقيقي مكرر: ' + wrapMathIfSec(dispVar + ' = ' + r0, isSec));
      finalAns = wrapMathIfSec(dispVar + ' = ' + r0, isSec);
    } else {
      const sDisc = Math.sqrt(disc);
      const r1 = (-b + sDisc) / (2 * a);
      const r2 = (-b - sDisc) / (2 * a);
      const r1Fmt = formatExactNumber(r1, isSec, true);
      const r2Fmt = formatExactNumber(r2, isSec, true);
      if (toExactFraction(sDisc, 12)) {
        const rhs1 = isSec ? (dispVar + ' = ' + r1Fmt) : (dispVar + ' = ' + r1Fmt);
        const rhs2 = isSec ? (dispVar + ' = ' + r2Fmt) : (dispVar + ' = ' + r2Fmt);
        exSteps.push('بتطبيق القانون العام أو التحليل: ' + wrapMathIfSec(rhs1, isSec) + ' أو ' + wrapMathIfSec(rhs2, isSec));
        finalAns = wrapMathIfSec(dispVar + ' = ' + r1Fmt, isSec) + ' أو ' + wrapMathIfSec(dispVar + ' = ' + r2Fmt, isSec);
      } else {
        const negB = formatExactNumber(-b, isSec, true);
        const twoA = formatExactNumber(2 * a, isSec, true);
        const dFmt = formatExactNumber(disc, isSec, true);
        const formulaTex = isSec
          ? (dispVar + ' = \\dfrac{' + negB + ' \\pm \\sqrt{' + dFmt + '}}{' + twoA + '}')
          : (dispVar + ' = (' + negB + ' ± جذر(' + dFmt + ')) / ' + twoA);
        exSteps.push('بتطبيق القانون العام: ' + wrapMathIfSec(formulaTex, isSec) + ' (تقريباً ' + formatExactNumber(r1, isSec, false) + ' و ' + formatExactNumber(r2, isSec, false) + ')');
        finalAns = wrapMathIfSec(formulaTex, isSec);
      }
    }

    return buildSolvedEntry(lesson, query, null, {
      title: 'حل المعادلة التربيعية',
      summary: 'لحل المعادلة التربيعية نرتبها أولاً على الصورة القياسية ثم نستخدم التحليل أو القانون العام عبر حساب المميز.',
      steps: [
        'انقل جميع الحدود إلى طرف واحد لتصبح بصورة قياسية تساوي صفراً.',
        'احسب المميز لتحديد عدد الجذور ونوعها.',
        'أوجد قيم الجذور باستخدام القانون العام أو التحليل.'
      ],
      problem: query,
      exSteps: exSteps,
      finalAnswer: finalAns,
      commonMistake: 'إغفال الإشارة السالبة للمعامل عند حساب المميز أو نسيان علامة (±) عند أخذ الجذر التربيعي.'
    });
  }

  function detectTwoPointProblem(query, isSec, lesson) {
    const raw = String(query || '');
    const ptMatches = [];
    const re = /\(\s*([^()،,]+)\s*[،,]\s*([^()،,]+)\s*\)/g;
    let m;
    while ((m = re.exec(raw)) !== null) {
      const xEv = evalMathAst(m[1]);
      const yEv = evalMathAst(m[2]);
      if (xEv.ok && yEv.ok) {
        ptMatches.push({ x: xEv.value, y: yEv.value });
      }
    }
    if (ptMatches.length !== 2) return null;

    const p1 = ptMatches[0];
    const p2 = ptMatches[1];
    const p1Str = '(' + formatExactNumber(p1.x, isSec, true) + (isSec ? ', ' : '، ') + formatExactNumber(p1.y, isSec, true) + ')';
    const p2Str = '(' + formatExactNumber(p2.x, isSec, true) + (isSec ? ', ' : '، ') + formatExactNumber(p2.y, isSec, true) + ')';

    const ctx = raw + ' ' + ((lesson && lesson.title) || '');
    const isMid = /منتصف|midpoint/i.test(ctx);
    const isDist = /مسافة|طول|distance/i.test(ctx);
    const isSlope = /ميل|slope/i.test(ctx) || (!isMid && !isDist);

    if (isSlope) {
      const dy = p2.y - p1.y;
      const dx = p2.x - p1.x;
      const slopeUndef = Math.abs(dx) < 1e-10;
      const mTex = isSec ? 'm' : 'م';
      const formulaTex = isSec ? 'm = \\dfrac{y_2 - y_1}{x_2 - x_1}' : 'الميل = (ص٢ - ص١) / (س٢ - س١)';
      const subTex = isSec
        ? ('m = \\dfrac{' + formatExactNumber(p2.y, true, true) + ' - (' + formatExactNumber(p1.y, true, true) + ')}{' + formatExactNumber(p2.x, true, true) + ' - (' + formatExactNumber(p1.x, true, true) + ')}')
        : ('الميل = (' + formatExactNumber(p2.y, false, false) + ' - (' + formatExactNumber(p1.y, false, false) + ')) / (' + formatExactNumber(p2.x, false, false) + ' - (' + formatExactNumber(p1.x, false, false) + '))');
      const finalAns = slopeUndef
        ? 'الميل غير معرّف (مستقيم رأسي)'
        : wrapMathIfSec(mTex + ' = ' + formatExactNumber(dy / dx, isSec, true), isSec);

      return buildSolvedEntry(lesson, query, null, {
        title: 'إيجاد ميل المستقيم المار بنقطتين',
        summary: 'ميل المستقيم هو نسبة التغير الرأسي (فرق الإحداثيات الصادية) إلى التغير الأفقي (فرق الإحداثيات السينية).',
        steps: [
          'عيّن إحداثيات النقطتين الأولى والثانية.',
          'طبّق قانون الميل وابدأ بطرح الصادات في البسط ثم السينات في المقام بالترتيب نفسه.'
        ],
        problem: query,
        exSteps: [
          'النقطتان المعطاتان: ' + wrapMathIfSec(p1Str, isSec) + ' و ' + wrapMathIfSec(p2Str, isSec),
          'نكتب قانون الميل: ' + wrapMathIfSec(formulaTex, isSec),
          'نعوّض بالإحداثيات: ' + wrapMathIfSec(subTex, isSec) + (slopeUndef ? '' : (' = ' + wrapMathIfSec(formatExactNumber(dy, isSec, true) + ' / ' + formatExactNumber(dx, isSec, true), isSec))),
          slopeUndef ? 'المقام يساوي صفراً؛ إذن المستقيم رأسي وميله غير معرّف.' : ('نبسّط الكسر فنحصل على: ' + finalAns)
        ],
        finalAnswer: finalAns,
        commonMistake: 'عكس الترتيب بين البسط والمقام أو نسيان علامة السالب المزدوجة عند طرح عدد سالب.'
      });
    }

    if (isMid) {
      const mx = (p1.x + p2.x) / 2;
      const my = (p1.y + p2.y) / 2;
      const midStr = '(' + formatExactNumber(mx, isSec, true) + (isSec ? ', ' : '، ') + formatExactNumber(my, isSec, true) + ')';
      return buildSolvedEntry(lesson, query, null, {
        title: 'إيجاد إحداثيي نقطة المنتصف',
        summary: 'إحداثيا نقطة المنتصف هما المتوسط الحسابي للإحداثيات السينية والمتوسط الحسابي للإحداثيات الصادية.',
        steps: ['اجمع الإحداثيين السينيين واقسم على ٢، واجمع الإحداثيين الصاديين واقسم على ٢.'],
        problem: query,
        exSteps: [
          'النقطتان: ' + wrapMathIfSec(p1Str, isSec) + ' و ' + wrapMathIfSec(p2Str, isSec),
          'نحسب منتصف السينات ومنتصف الصادات: ' + wrapMathIfSec(midStr, isSec)
        ],
        finalAnswer: 'نقطة المنتصف = ' + wrapMathIfSec(midStr, isSec)
      });
    }

    const dx = p2.x - p1.x;
    const dy = p2.y - p1.y;
    const d2 = dx * dx + dy * dy;
    const dist = Math.sqrt(d2);
    const distFmt = formatExactNumber(dist, isSec, true);
    return buildSolvedEntry(lesson, query, null, {
      title: 'حساب المسافة بين نقطتين',
      summary: 'تُحسب المسافة بين نقطتين في المستوى الإحداثي باستعمال الجذر التربيعي لمجموع مربعي فرق السينات وفرق الصادات.',
      steps: ['أوجد فرق السينات وفرق الصادات، ثم ربّع كلاً منهما واجمعهما تحت الجذر التربيعي.'],
      problem: query,
      exSteps: [
        'نحسب مربع المسافة: ' + wrapMathIfSec('(' + formatExactNumber(dx, isSec, true) + ')^2 + (' + formatExactNumber(dy, isSec, true) + ')^2 = ' + formatExactNumber(d2, isSec, true), isSec),
        'نأخذ الجذر التربيعي: ' + (isSec ? ('$\\sqrt{' + formatExactNumber(d2, true, true) + '} \\approx ' + distFmt + '$') : ('جذر(' + formatExactNumber(d2, false, false) + ') ≈ ' + distFmt))
      ],
      finalAnswer: 'المسافة = ' + (toExactFraction(dist, 12) ? wrapMathIfSec(distFmt, isSec) : (isSec ? ('$\\sqrt{' + formatExactNumber(d2, true, true) + '}$') : ('جذر(' + formatExactNumber(d2, false, false) + ')')))
    });
  }

  function detectConicClassification(query, isSec, lesson) {
    const raw = String(query || '').trim();
    if (raw.indexOf('=') === -1) return null;
    const parts = raw.replace(/[؟?!.،,;]+$/g, '').split('=');
    if (parts.length !== 2) return null;
    const lhsRaw = parts[0].trim();
    const rhsRaw = parts[1].trim();
    if (!lhsRaw || !rhsRaw) return null;

    const lhsToks = tokenizeMath(normalizeMathExpr(lhsRaw)) || [];
    const rhsToks = tokenizeMath(normalizeMathExpr(rhsRaw)) || [];
    const allToks = lhsToks.concat(rhsToks);
    const hasX = allToks.some(function (t) { return t.type === 'id' && t.val === 'x'; });
    const hasY = allToks.some(function (t) { return t.type === 'id' && t.val === 'y'; });
    const hasDeg2 = allToks.some(function (t) { return t.type === 'op' && t.val === '^'; }) ||
      /x\s*\*?\s*y|y\s*\*?\s*x/.test(normalizeMathExpr(raw).replace(/\s+/g, ''));
    if (!hasX || !hasY || !hasDeg2) return null;

    function F(xv, yv) {
      const l = evalMathAst(lhsRaw, { x: xv, y: yv });
      const r = evalMathAst(rhsRaw, { x: xv, y: yv });
      if (!l.ok || !r.ok) return null;
      return l.value - r.value;
    }

    const f00 = F(0, 0), f10 = F(1, 0), fm10 = F(-1, 0), f01 = F(0, 1), f0m1 = F(0, -1), f11 = F(1, 1), f20 = F(2, 0), f02 = F(0, 2);
    if ([f00, f10, fm10, f01, f0m1, f11, f20, f02].some(function (v) { return v === null; })) return null;

    const A = (f10 + fm10 - 2 * f00) / 2;
    const C = (f01 + f0m1 - 2 * f00) / 2;
    const B = f11 - f10 - f01 + f00;
    const D = (f10 - fm10) / 2;
    const E = (f01 - f0m1) / 2;
    const K = f00;

    // Verify exact quadratic fit at (2,0) and (0,2)
    if (Math.abs((4 * A + 2 * D + K) - f20) > 1e-7 || Math.abs((4 * C + 2 * E + K) - f02) > 1e-7) return null;
    if (Math.abs(A) + Math.abs(B) + Math.abs(C) < 1e-9) return null;

    const disc = B * B - 4 * A * C;
    let kind = 'قطع ناقص';
    if (Math.abs(disc) < 1e-9) kind = 'قطع مكافئ';
    else if (disc > 0) kind = 'قطع زائد';
    else if (Math.abs(B) < 1e-9 && Math.abs(A - C) < 1e-9) kind = 'دائرة';

    return buildSolvedEntry(lesson, query, null, {
      title: 'تحديد نوع القطع المخروطي باستعمال المميز',
      summary: 'لتصنيف معادلة القطع المخروطي من الدرجة الثانية نحسب المميز $B^2 - 4AC$ بعد تعيين المعاملات $A, B, C$.',
      steps: [
        'استخرج معامل $x^2$ ($A$)، ومعامل $xy$ ($B$)، ومعامل $y^2$ ($C$).',
        'احسب قيمة المميز $\\Delta = B^2 - 4AC$ وقارنها بالصفر.'
      ],
      problem: query,
      exSteps: [
        'نحدد المعاملات: $A = ' + formatExactNumber(A, isSec, true) + ',\\; B = ' + formatExactNumber(B, isSec, true) + ',\\; C = ' + formatExactNumber(C, isSec, true) + '$',
        'نحسب المميز: $B^2 - 4AC = (' + formatExactNumber(B, isSec, true) + ')^2 - 4(' + formatExactNumber(A, isSec, true) + ')(' + formatExactNumber(C, isSec, true) + ') = ' + formatExactNumber(disc, isSec, true) + '$',
        Math.abs(disc) < 1e-9
          ? 'بما أن المميز يساوي $0$ فالمعادلة تمثل **قطعاً مكافئاً**.'
          : (disc > 0
              ? 'بما أن المميز أكبر من $0$ فالمعادلة تمثل **قطعاً زائداً**.'
              : ('بما أن المميز أصغر من $0$ ' + (kind === 'دائرة' ? 'مع $B=0$ و $A=C$ فالمعادلة تمثل **دائرة**.' : 'ولا تتحقق شروط الدائرة فالمعادلة تمثل **قطعاً ناقصاً**.')))
      ],
      finalAnswer: 'نوع القطع المخروطي: ' + kind
    });
  }

  function detectNumericExpression(query, isSec, lesson) {
    const raw = String(query || '').trim();
    if (!raw || raw.indexOf('=') !== -1) return null;
    const stripped = raw
      .replace(/^(?:احسب|أوجد\s*(?:قيمة|ناتج)?|ما\s*(?:قيمة|ناتج)|بسط|بسّط|ناتج|قيمة|evaluate|calculate|compute|simplify)\s*:?\s*/i, '')
      .replace(/[؟?!.،,;]+$/g, '')
      .trim();
    if (!stripped) return null;
    if (!/[0-9٠-٩]/.test(stripped)) return null;
    if (!/[+\-*×÷/^√()|]|جذر/.test(stripped)) return null;

    const ev = evalMathAst(stripped);
    if (!ev.ok) return null;

    const dispExpr = formatDisplayExpr(stripped, isSec, 'x');
    const ansFmt = formatExactNumber(ev.value, isSec, true);

    return buildSolvedEntry(lesson, query, null, {
      title: 'تبسيط وحساب العبارة العددية',
      summary: 'لحساب قيمة العبارة العددية بدقة نطبق ترتيب العمليات: الأقواس أولاً، ثم القوى والجذور، ثم الضرب والقسمة من اليمين إلى اليسار (أو اليسار لليمين بالرموز اللاتينية)، وأخيراً الجمع والطرح.',
      steps: [
        'احسب ما بداخل الأقواس والقيمة المطلقة أو الجذور أولاً.',
        'نفّذ القوى والأسس قبل الضرب والقسمة.',
        'أكمل بالجمع والطرح للوصول إلى الناتج النهائي.'
      ],
      problem: query,
      exSteps: [
        'العبارة المعطاة: ' + wrapMathIfSec(dispExpr, isSec),
        'بتطبيق أولوية العمليات الحسابية: ' + wrapMathIfSec(dispExpr + ' = ' + ansFmt, isSec)
      ],
      finalAnswer: wrapMathIfSec(ansFmt, isSec)
    });
  }

  function trySolveUserProblemLocally(query, isSec, lesson) {
    const q = String(query || '').trim();
    if (!q || q.length > 260) return null;
    try {
      return (
        detectFunctionEvaluation(q, isSec, lesson) ||
        detectTwoPointProblem(q, isSec, lesson) ||
        detectConicClassification(q, isSec, lesson) ||
        detectLinearOrQuadraticEquation(q, isSec, lesson) ||
        detectNumericExpression(q, isSec, lesson)
      );
    } catch (e) {
      return null;
    }
  }

  /**
   * مطابقة محلية ذكية من نصوص الدرس وأمثلة الكتاب عند العمل بدون إنترنت أو بدون ضبط GEMINI_API_KEY
   */
  function buildSmartLocalMatch(lesson, query, level, extraNote) {
    const isSec = isSecondaryLesson(lesson);
    const tokens = tokenizeQuery(query);
    const builtins = buildBuiltInSubtopics(lesson);
    const prep = lesson.prep || {};
    const sum = lesson.summary || {};
    const quiz = lesson.quiz || {};

    // Priority 0: Try exact deterministic algebraic/numeric problem solver first
    const directSolved = trySolveUserProblemLocally(query, isSec, lesson);
    const pool = collectExamplePool(lesson, isSec);

    if (directSolved) {
      return {
        id: directSolved.id,
        title: directSolved.title,
        badge: '🧮 حل فوري دقيق لمسألتك خطوة بخطوة (' + (level || 'متوسط منهجي') + ')',
        source: 'local-solver',
        summary: directSolved.summary,
        steps: directSolved.steps,
        workedExample: directSolved.workedExample,
        altExamples: pool.slice(0, 5),
        commonMistake: directSolved.commonMistake,
        quickCheck: (directSolved.quickCheck && directSolved.quickCheck.question) ? directSolved.quickCheck : (builtins[0] ? builtins[0].quickCheck : { question: '', answer: '' }),
        systemHint: ''
      };
    }

    // 1. Find best matching built-in sub-topic
    let bestSub = builtins[0] || null;
    let bestSubScore = -1;
    builtins.forEach(function (sub) {
      const s = scoreText([sub.title, sub.summary].concat(sub.steps || []).join(' '), tokens);
      if (s > bestSubScore) {
        bestSubScore = s;
        bestSub = sub;
      }
    });

    // 2. Find best matching sentence/snippet across stations + methods + vocab
    const snippets = [];
    for (let i = 1; i <= 6; i++) {
      const st = prep['station' + i];
      if (!st) continue;
      Object.keys(st).forEach(function (k) {
        if (k === 'title' || k === 'content') return;
        const val = st[k];
        if (typeof val === 'string' && val.trim()) snippets.push(val.trim());
        else if (Array.isArray(val)) formatVocabItems(val).forEach(function (vs) { snippets.push(vs); });
      });
    }
    (sum.methods || []).forEach(function (m) { if (m) snippets.push(m); });
    if (sum.concept) snippets.push(sum.concept);
    if (sum.golden_rule) snippets.push(sum.golden_rule);

    const scoredSnippets = snippets
      .map(function (txt) { return { txt: txt, score: scoreText(txt, tokens) }; })
      .sort(function (a, b) { return b.score - a.score; });

    const matchedSteps = [];
    const seenS = new Set();
    scoredSnippets.slice(0, 4).forEach(function (item) {
      if (item.score > 0 && !seenS.has(item.txt)) {
        seenS.add(item.txt);
        matchedSteps.push(item.txt);
      }
    });
    if (!matchedSteps.length && bestSub && Array.isArray(bestSub.steps)) {
      bestSub.steps.forEach(function (s) { matchedSteps.push(s); });
    }

    // 3. Find best matching worked example across full lesson pool + all MCQs/TFs/Essays
    let bestEx = pool[0] || (bestSub ? bestSub.workedExample : normalizeExampleObj({}, isSec));
    let bestExScore = -1;
    const altPool = [];
    pool.forEach(function (ex) {
      const s = scoreText([ex.problem].concat(ex.steps || []).concat([ex.finalAnswer]).join(' '), tokens);
      if (s > bestExScore) {
        bestExScore = s;
        bestEx = ex;
      } else {
        altPool.push(ex);
      }
    });
    bestEx = Object.assign({}, bestEx, { isExactUserSolution: false });

    // 4. Find best quick check from quiz questions matching query
    let qc = bestSub ? bestSub.quickCheck : { question: '', answer: '' };
    let bestQcScore = -1;
    (quiz.mcq || []).concat(quiz.essay || []).forEach(function (q) {
      const s = scoreText((q.q || '') + ' ' + (q.explanation || ''), tokens);
      if (s > bestQcScore && q !== null) {
        bestQcScore = s;
        const ansVal = q.options
          ? ((q.options[typeof q.ans === 'number' ? q.ans : (q.correct || 0)] || '') + (q.explanation ? (' — ' + q.explanation) : ''))
          : (q.ans || '');
        qc = { question: q.q, answer: ansVal };
      }
    });

    return {
      id: lesson.id + '-local-' + Date.now(),
      title: query ? ('شرح جزئية: ' + query) : (bestSub ? bestSub.title : lesson.title),
      badge: '⚡ شرح فوري من قاعدة بيانات المنهج المعتمد (' + (level || 'متوسط منهجي') + ')',
      source: 'local-smart',
      isSimilarOnly: !!query,
      summary: (scoredSnippets[0] && scoredSnippets[0].score > 0)
        ? scoredSnippets[0].txt
        : (bestSub ? bestSub.summary : (sum.concept || '')),
      steps: matchedSteps.slice(0, 5),
      workedExample: bestEx,
      altExamples: altPool.slice(0, 5),
      commonMistake: (bestSub && bestSub.commonMistake) || (prep.station3 && prep.station3.misconceptions) || '',
      quickCheck: qc,
      systemHint: extraNote || ''
    };
  }

  function getLessonById(lessonId) {
    if (global.CURRICULUM_DATA && global.CURRICULUM_DATA.lessons && global.CURRICULUM_DATA.lessons[lessonId]) {
      return global.CURRICULUM_DATA.lessons[lessonId];
    }
    const books = [global.GRADE3S_BOOK_DATA, global.GRADE2S_BOOK_DATA, global.GRADE1S_BOOK_DATA, global.GRADE3M_BOOK_DATA, global.GRADE1M_BOOK_DATA, global.GRADE6_BOOK_DATA];
    for (let i = 0; i < books.length; i++) {
      if (books[i] && books[i].lessons && books[i].lessons[lessonId]) {
        return books[i].lessons[lessonId];
      }
    }
    return null;
  }

  function loadSessionNavMap() {
    try {
      if (typeof sessionStorage === 'undefined') return {};
      const raw = sessionStorage.getItem(CE_NAV_SESSION_KEY);
      const parsed = raw ? JSON.parse(raw) : {};
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (e) {
      return {};
    }
  }

  function saveLessonNavState(lessonId) {
    try {
      if (typeof sessionStorage === 'undefined' || !state.lessonStates[lessonId]) return;
      const st = state.lessonStates[lessonId];
      const map = loadSessionNavMap();
      map[lessonId] = {
        selectedSubtopicId: st.selectedSubtopicId || '',
        altExOffset: st.altExOffset || 0,
        revealCheck: !!st.revealCheck,
        queryDraft: st.queryDraft || '',
        level: st.level || 'متوسط منهجي',
        hasCustom: !!st.customResult,
        customResult: st.customResult && st.customResult.source ? st.customResult : null
      };
      sessionStorage.setItem(CE_NAV_SESSION_KEY, JSON.stringify(map));
    } catch (e) {}
  }

  function ensureLessonState(lessonId) {
    if (!state.lessonStates[lessonId]) {
      const savedMap = loadSessionNavMap();
      const s = savedMap[lessonId] || {};
      state.lessonStates[lessonId] = {
        selectedSubtopicId: s.selectedSubtopicId || '',
        customResult: (s.hasCustom && s.customResult) ? s.customResult : null,
        altExOffset: s.altExOffset || 0,
        revealCheck: !!s.revealCheck,
        loading: false,
        showTeacherForm: false,
        queryDraft: s.queryDraft || '',
        level: s.level || 'متوسط منهجي'
      };
    }
    return state.lessonStates[lessonId];
  }

  function getAllSubtopics(lesson) {
    const builtins = buildBuiltInSubtopics(lesson);
    const teacherOnes = getTeacherSubtopics(lesson.id);
    return teacherOnes.concat(builtins);
  }

  function getActiveSubtopic(lesson) {
    const st = ensureLessonState(lesson.id);
    if (st.customResult) return st.customResult;
    const all = getAllSubtopics(lesson);
    if (st.selectedSubtopicId) {
      const found = all.find(function (item) { return item.id === st.selectedSubtopicId; });
      if (found) return found;
    }
    return all[0] || null;
  }

  function getDisplayedExample(sub, st) {
    if (!sub) return normalizeExampleObj({}, false);
    const list = [sub.workedExample].concat(sub.altExamples || []).filter(function (ex) {
      return ex && (ex.problem || (ex.steps && ex.steps.length));
    });
    if (!list.length) return normalizeExampleObj({}, false);
    return list[(st.altExOffset || 0) % list.length];
  }

  function renderActiveCardHtml(lesson) {
    const isSec = isSecondaryLesson(lesson);
    const st = ensureLessonState(lesson.id);
    const sub = getActiveSubtopic(lesson);
    if (!sub) {
      return '<div class="ce-empty">لا تتوفر بيانات شرح لهذا الدرس بعد.</div>';
    }
    const ex = getDisplayedExample(sub, st);
    const exListLen = [sub.workedExample].concat(sub.altExamples || []).filter(function (item) {
      return item && (item.problem || (item.steps && item.steps.length));
    }).length;

    const stepsHtml = (sub.steps && sub.steps.length)
      ? '<div class="ce-section"><h4 class="ce-sec-title">🔹 خطوات القاعدة والتفصيل:</h4><ol class="ce-steps-list">' +
        sub.steps.map(function (step) {
          return '<li>' + fmt(step, isSec) + '</li>';
        }).join('') +
        '</ol></div>'
      : '';

    const exStepsHtml = (ex.steps && ex.steps.length)
      ? '<ol class="ce-ex-steps">' + ex.steps.map(function (s) {
          return '<li>' + fmt(s, isSec) + '</li>';
        }).join('') + '</ol>'
      : '';

    const figHtml = ex.fig
      ? '<div class="ce-ex-fig"><img src="' + escHtml(ex.fig) + '" alt="شكل توضيحي للمثال" loading="lazy" ' +
        'onclick="window.Platform && window.Platform.openImageLightbox && window.Platform.openImageLightbox(this.getAttribute(\'src\'), \'\')" /></div>'
      : '';

    const mistakeHtml = sub.commonMistake
      ? '<div class="ce-mistake-box"><div class="ce-mistake-hdr">⚠️ تنبيه الخطأ الشائع وكيفية تجنبه:</div><div class="ce-mistake-body">' +
        fmt(sub.commonMistake, isSec) + '</div></div>'
      : '';

    const qc = sub.quickCheck || {};
    const checkHtml = qc.question
      ? '<div class="ce-check-box">' +
          '<div class="ce-check-hdr"><span>✍️ تحقق من فهمك (تدريب سريع):</span>' +
          '<button type="button" class="ce-mini-btn" onclick="window.ConceptExplainer.toggleQuickCheck(\'' + escHtml(lesson.id) + '\')">' +
            (st.revealCheck ? '🙈 إخفاء الإجابة' : '👁️ إظهار الحل') +
          '</button></div>' +
          '<div class="ce-check-q">' + fmt(qc.question, isSec) + '</div>' +
          (st.revealCheck
            ? '<div class="ce-check-ans"><strong>الإجابة النموذجية:</strong> ' + fmt(qc.answer || '', isSec) + '</div>'
            : '') +
        '</div>'
      : '';

    const hintHtml = (sub.systemHint && isAdminUser())
      ? '<div class="ce-admin-hint">💡 <strong>ملاحظة للمدير العام:</strong> لتفعيل التوليد الذكي الحر عبر Gemini لطلبات المستخدمين المفتوحة، أضف متغير <code>GEMINI_API_KEY</code> في إعدادات Vercel → Environment Variables.</div>'
      : '';

    const isShowingAlt = (st.altExOffset || 0) > 0;
    const isExactSol = !!ex.isExactUserSolution;
    const isSimilarFallback = !isExactSol && sub.source === 'local-smart' && sub.isSimilarOnly && !isShowingAlt;
    const exHeaderLabel = isExactSol
      ? '✍️ حل مسألتك خطوة بخطوة'
      : (isSimilarFallback ? '📖 أقرب مثال مشابه من المنهج المعتمد' : '✍️ المثال التوضيحي المحلول خطوة بخطوة');
    const exProbLabel = isExactSol ? 'المسألة:' : 'المثال:';
    const showFinalAnswer = !!(ex.finalAnswer && !isRedundantFinalAnswer(ex.steps, ex.finalAnswer));
    const similarNoteHtml = isSimilarFallback
      ? '<div class="ce-similar-note">ℹ️ تعذّر حل الصيغة الحرة محلياً دون خادم الذكاء الاصطناعي؛ فيما يلي أقرب مثال محلول من المنهج على نفس القاعدة:</div>'
      : '';

    return `
      <div class="ce-card ${sub.source === 'ai' ? 'is-ai' : ''} ${sub.source === 'local-solver' ? 'is-solved' : ''}">
        <div class="ce-card-header">
          <div>
            <span class="ce-source-badge">${escHtml(fmtPlainNum(sub.badge || '📚 شرح تفصيلي', isSec))}</span>
            <h3 class="ce-card-title">${fmt(sub.title, isSec)}</h3>
          </div>
          <div class="ce-card-actions">
            ${exListLen > 1 ? `
              <button type="button" class="ce-action-btn" onclick="window.ConceptExplainer.nextExample('${escHtml(lesson.id)}')" title="عرض مثال توضيحي بديل لنفس الجزئية">
                🔄 مثال آخر (${fmtPlainNum(((st.altExOffset || 0) % exListLen) + 1, isSec)}/${fmtPlainNum(exListLen, isSec)})
              </button>
            ` : ''}
            <button type="button" class="ce-action-btn primary" onclick="window.ConceptExplainer.copyToWord('${escHtml(lesson.id)}')" title="نسخ الشرح والمثال التوضيحي مباشرة إلى Microsoft Word">
              📋 نسخ إلى Word
            </button>
            <button type="button" class="ce-action-btn" onclick="window.ConceptExplainer.printCard('${escHtml(lesson.id)}')" title="طباعة بطاقة الشرح والمثال">
              🖨️ طباعة
            </button>
          </div>
        </div>

        <div class="ce-summary-box">
          <strong>📌 التوضيح المفاهيمي:</strong>
          <div class="ce-summary-text">${fmt(sub.summary, isSec)}</div>
        </div>

        ${stepsHtml}

        <div class="ce-example-box">
          <div class="ce-example-hdr">
            <span>${exHeaderLabel}</span>
          </div>
          ${similarNoteHtml}
          <div class="ce-ex-problem"><strong>${exProbLabel}</strong> ${fmt(ex.problem, isSec)}</div>
          ${figHtml}
          ${exStepsHtml}
          ${showFinalAnswer ? `<div class="ce-ex-final">✅ <strong>الخلاصة / الناتج النهائي:</strong> ${fmt(ex.finalAnswer, isSec)}</div>` : ''}
        </div>

        ${mistakeHtml}
        ${checkHtml}
        ${hintHtml}
      </div>
    `;
  }

  function renderTeacherModalHtml(lesson, isSec) {
    const st = ensureLessonState(lesson.id);
    if (!st.showTeacherForm) return '';
    return `
      <form class="ce-teacher-form" onsubmit="window.ConceptExplainer.submitTeacherSubtopic(event, '${escHtml(lesson.id)}')">
        <div class="ce-teacher-hdr">
          <strong>👨‍🏫 إضافة جزئية شرح ومثال توضيحي معتمد من المعلم لهذا الدرس</strong>
          <button type="button" class="ce-mini-btn" onclick="window.ConceptExplainer.toggleTeacherForm('${escHtml(lesson.id)}', false)">✖ إغلاق</button>
        </div>
        <div class="ce-teacher-grid">
          <input id="ce-t-title" type="text" required placeholder="عنوان الجزئية (مثال: إيجاد خطي التقارب للقطع الزائد)">
          <textarea id="ce-t-summary" rows="2" required placeholder="القاعدة أو الشرح التفصيلي... (${isSec ? 'أرقام 0-9 وصيغ $...$' : 'أرقام مشرقية ٠-٩'})"></textarea>
          <textarea id="ce-t-problem" rows="2" required placeholder="نص المثال التوضيحي..."></textarea>
          <textarea id="ce-t-steps" rows="2" required placeholder="خطوات الحل (كل خطوة في سطر أو مفصولة)..."></textarea>
          <input id="ce-t-mistake" type="text" placeholder="الخطأ الشائع المتوقع (اختياري)">
          <div style="display:flex; gap:8px; justify-content:flex-end;">
            <button type="submit" class="nav-btn primary">💾 حفظ الجزئية للدرس</button>
          </div>
        </div>
      </form>
    `;
  }

  function renderPane(lesson) {
    if (!lesson) return '';
    const isSec = isSecondaryLesson(lesson);
    const st = ensureLessonState(lesson.id);
    const allSubs = getAllSubtopics(lesson);
    const active = getActiveSubtopic(lesson);
    const canEditTeacher = isApprovedOrAdmin();
    const dTitle = fmt(lesson.title || '', isSec);

    const chipsHtml = allSubs.map(function (sub) {
      const isAct = active && active.id === sub.id && !st.customResult;
      return '<button type="button" class="ce-chip ' + (isAct ? 'active' : '') +
        '" onclick="window.ConceptExplainer.selectSubtopic(\'' + escHtml(lesson.id) + '\', \'' + escHtml(sub.id) + '\')">' +
        escHtml(sub.title) + '</button>';
    }).join('');

    const placeholderText = isSec
      ? 'اكتب أي جزئية أو مسألة تريد حلها وشرحها بمثال (مثال: f(x) = 2x^2 - 3x + 5 أوجد f(-3))'
      : 'اكتب أي جزئية أو مسألة تريد حلها وشرحها بمثال (مثال: د(س) = -س + ٧، فأوجد قيمة د(٣))';

    return `
      <div class="ce-wrapper ${isSec ? 'is-sec-stage' : 'is-ar-stage'}" id="ce-root-${escHtml(lesson.id)}">
        <div class="ce-hero">
          <div>
            <div class="ce-hero-title">🧠 الشارح التفصيلي للجزئيات بالأمثلة التوضيحية (النظام الهجين)</div>
            <div class="ce-hero-sub">اختر جزئية من جزئيات درس «${dTitle}» أو اكتب أي جزئية محددة للحصول على شرح تفصيلي بمثال محلول خطوة بخطوة.</div>
          </div>
          ${canEditTeacher ? `
            <button type="button" class="nav-btn" onclick="window.ConceptExplainer.toggleTeacherForm('${escHtml(lesson.id)}', true)">
              👨‍🏫 + إضافة شرح للمعلم
            </button>
          ` : ''}
        </div>

        ${renderTeacherModalHtml(lesson, isSec)}

        <form class="ce-query-bar" onsubmit="window.ConceptExplainer.handleCustomSubmit(event, '${escHtml(lesson.id)}')">
          <input type="text" id="ce-custom-query" class="ce-query-input" value="${escHtml(st.queryDraft || '')}"
            placeholder="${escHtml(placeholderText)}" oninput="window.ConceptExplainer.updateDraft('${escHtml(lesson.id)}', this.value)">
          <select id="ce-level-select" class="ce-level-select" aria-label="مستوى الشرح">
            <option value="مبسّط للطالب" ${st.level === 'مبسّط للطالب' ? 'selected' : ''}>مستوى مبسّط للطالب</option>
            <option value="متوسط منهجي" ${st.level === 'متوسط منهجي' ? 'selected' : ''}>مستوى متوسط منهجي</option>
            <option value="متقدم / قدرات وتحصيلي" ${st.level === 'متقدم / قدرات وتحصيلي' ? 'selected' : ''}>متقدم / قدرات وتحصيلي</option>
          </select>
          <button type="submit" class="nav-btn primary ce-submit-btn" ${st.loading ? 'disabled' : ''}>
            ${st.loading ? '⏳ جاري إعداد الشرح والمثال...' : '✨ اشرح بمثال توضيحي'}
          </button>
        </form>

        <div class="ce-chips-section">
          <div class="ce-chips-label">📌 جزئيات الدرس الجاهزة (انقر للعرض الفوري):</div>
          <div class="ce-chips-row">${chipsHtml}</div>
        </div>

        <div id="ce-active-card">${renderActiveCardHtml(lesson)}</div>
      </div>
    `;
  }

  function rerenderInDom(lessonId) {
    if (typeof document === 'undefined') return;
    const lesson = getLessonById(lessonId);
    const root = document.getElementById('ce-root-' + lessonId);
    if (lesson && root && root.parentNode) {
      root.outerHTML = renderPane(lesson);
    }
  }

  function selectSubtopic(lessonId, subtopicId) {
    const st = ensureLessonState(lessonId);
    st.selectedSubtopicId = subtopicId;
    st.customResult = null;
    st.altExOffset = 0;
    st.revealCheck = false;
    saveLessonNavState(lessonId);
    rerenderInDom(lessonId);
  }

  function nextExample(lessonId) {
    const st = ensureLessonState(lessonId);
    st.altExOffset = (st.altExOffset || 0) + 1;
    saveLessonNavState(lessonId);
    rerenderInDom(lessonId);
  }

  function toggleQuickCheck(lessonId) {
    const st = ensureLessonState(lessonId);
    st.revealCheck = !st.revealCheck;
    saveLessonNavState(lessonId);
    rerenderInDom(lessonId);
  }

  function updateDraft(lessonId, val) {
    const st = ensureLessonState(lessonId);
    st.queryDraft = String(val || '');
    saveLessonNavState(lessonId);
  }

  function toggleTeacherForm(lessonId, show) {
    const st = ensureLessonState(lessonId);
    st.showTeacherForm = !!show;
    rerenderInDom(lessonId);
  }

  function submitTeacherSubtopic(e, lessonId) {
    if (e && e.preventDefault) e.preventDefault();
    const lesson = getLessonById(lessonId);
    if (!lesson) return;
    const isSec = isSecondaryLesson(lesson);
    const titleEl = document.getElementById('ce-t-title');
    const sumEl = document.getElementById('ce-t-summary');
    const probEl = document.getElementById('ce-t-problem');
    const stepsEl = document.getElementById('ce-t-steps');
    const misEl = document.getElementById('ce-t-mistake');

    const title = fmtPlainNum((titleEl && titleEl.value) || '', isSec).trim();
    const summary = fmtPlainNum((sumEl && sumEl.value) || '', isSec).trim();
    const problem = fmtPlainNum((probEl && probEl.value) || '', isSec).trim();
    const rawSteps = fmtPlainNum((stepsEl && stepsEl.value) || '', isSec).trim();
    const mistake = fmtPlainNum((misEl && misEl.value) || '', isSec).trim();
    if (!title || !summary || !problem) return;

    const item = {
      id: lessonId + '-teacher-' + Date.now(),
      title: title,
      badge: '👨‍🏫 شرح معتمد من المعلم',
      source: 'teacher',
      summary: summary,
      steps: splitIntoSteps(summary),
      workedExample: normalizeExampleObj({
        problem: problem,
        steps: splitIntoSteps(rawSteps),
        finalAnswer: ''
      }, isSec),
      altExamples: [],
      commonMistake: mistake,
      quickCheck: { question: '', answer: '' }
    };
    saveTeacherSubtopic(lessonId, item);
    const st = ensureLessonState(lessonId);
    st.showTeacherForm = false;
    st.selectedSubtopicId = item.id;
    st.customResult = null;
    rerenderInDom(lessonId);
    const utils = getUtils();
    if (utils && utils.showToast) {
      utils.showToast('✓ تم حفظ جزئية الشرح والمثال التوضيحي للدرس بنجاح!', 'success', isSec);
    }
  }

  async function requestCustomExplanation(lessonId, queryInput, levelInput) {
    const lesson = getLessonById(lessonId);
    if (!lesson) return null;
    const isSec = isSecondaryLesson(lesson);
    const st = ensureLessonState(lessonId);
    const query = String(queryInput != null ? queryInput : st.queryDraft || '').trim();
    const level = String(levelInput != null ? levelInput : st.level || 'متوسط منهجي').trim();
    st.level = level;
    st.queryDraft = query;

    if (!query) {
      const utils = getUtils();
      if (utils && utils.showToast) utils.showToast('يرجى كتابة اسم الجزئية المراد شرحها أولاً.', 'warning', isSec);
      return null;
    }

    const cacheKey = getCacheKey(lessonId, query, level);
    const cached = getCachedExplanation(cacheKey);
    if (cached && cached.source === 'ai') {
      st.customResult = cached;
      st.altExOffset = 0;
      st.revealCheck = false;
      rerenderInDom(lessonId);
      return cached;
    }

    // Priority 1: Exact built-in mathematical problem solver (0ms, 100% deterministic accuracy)
    const directSolved = trySolveUserProblemLocally(query, isSec, lesson);
    if (directSolved) {
      const poolAlts = collectExamplePool(lesson, isSec).slice(0, 5);
      const builtins = buildBuiltInSubtopics(lesson);
      const solvedEntry = {
        id: directSolved.id,
        title: directSolved.title,
        badge: '🧮 حل فوري دقيق لمسألتك خطوة بخطوة (' + level + ')',
        source: 'local-solver',
        summary: directSolved.summary,
        steps: directSolved.steps,
        workedExample: directSolved.workedExample,
        altExamples: poolAlts,
        commonMistake: directSolved.commonMistake,
        quickCheck: (directSolved.quickCheck && directSolved.quickCheck.question) ? directSolved.quickCheck : (builtins[0] ? builtins[0].quickCheck : { question: '', answer: '' }),
        systemHint: ''
      };
      st.customResult = solvedEntry;
      st.altExOffset = 0;
      st.revealCheck = false;
      saveLessonNavState(lessonId);
      rerenderInDom(lessonId);
      return solvedEntry;
    }

    const canCallNetwork = typeof fetch === 'function' &&
      typeof window !== 'undefined' &&
      window.location &&
      /^https?:$/i.test(window.location.protocol);

    if (canCallNetwork) {
      st.loading = true;
      rerenderInDom(lessonId);
      try {
        const sum = lesson.summary || {};
        const prep = lesson.prep || {};
        const lessonContext = [
          sum.concept || '',
          prep.station2 && prep.station2.key_concepts ? prep.station2.key_concepts : '',
          sum.golden_rule || ''
        ].filter(Boolean).join(' | ').slice(0, 850);

        const resp = await fetch('/api/explain', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            lessonId: lesson.id,
            lessonTitle: lesson.title || '',
            chapterTitle: lesson.chapter || lesson.chapterTitle || '',
            grade: lesson.grade || '',
            isSecondary: isSec,
            topic: query,
            level: level,
            lessonContext: lessonContext
          })
        });

        if (resp && resp.ok) {
          const json = await resp.json();
          if (json && json.ok && json.data) {
            const d = json.data;
            const localAlts = collectExamplePool(lesson, isSec).slice(0, 3);
            const aiEntry = {
              id: lessonId + '-ai-' + Date.now(),
              title: fmtPlainNum(d.title || query, isSec),
              badge: '✨ شرح ذكي مولّد خصيصاً لجزئيتك (' + level + ')',
              source: 'ai',
              summary: fmtPlainNum(d.summary || '', isSec),
              steps: (d.steps || []).map(function (s) { return fmtPlainNum(s, isSec); }),
              workedExample: normalizeExampleObj({
                problem: fmtPlainNum(d.workedExample && d.workedExample.problem, isSec),
                steps: (d.workedExample && d.workedExample.steps || []).map(function (s) { return fmtPlainNum(s, isSec); }),
                finalAnswer: fmtPlainNum(d.workedExample && d.workedExample.finalAnswer, isSec),
                isExactUserSolution: true
              }, isSec),
              altExamples: localAlts,
              commonMistake: fmtPlainNum(d.commonMistake || '', isSec),
              quickCheck: {
                question: fmtPlainNum(d.quickCheck && d.quickCheck.question, isSec),
                answer: fmtPlainNum(d.quickCheck && d.quickCheck.answer, isSec)
              }
            };
            st.loading = false;
            st.customResult = aiEntry;
            st.altExOffset = 0;
            st.revealCheck = false;
            setCachedExplanation(cacheKey, aiEntry);
            saveLessonNavState(lessonId);
            rerenderInDom(lessonId);
            return aiEntry;
          }
        }
      } catch (e) {
        // Fall through silently to smart local textbook matcher
      }
      st.loading = false;
    }

    const localEntry = buildSmartLocalMatch(lesson, query, level, 'fallback');
    st.customResult = localEntry;
    st.altExOffset = 0;
    st.revealCheck = false;
    saveLessonNavState(lessonId);
    rerenderInDom(lessonId);
    return localEntry;
  }

  function handleCustomSubmit(e, lessonId) {
    if (e && e.preventDefault) e.preventDefault();
    const inp = document.getElementById('ce-custom-query');
    const lvl = document.getElementById('ce-level-select');
    requestCustomExplanation(lessonId, inp ? inp.value : '', lvl ? lvl.value : 'متوسط منهجي');
  }

  async function copyToWord(lessonId) {
    const lesson = getLessonById(lessonId);
    const utils = getUtils();
    if (!lesson || !utils) return false;
    const isSec = isSecondaryLesson(lesson);
    const st = ensureLessonState(lessonId);
    const sub = getActiveSubtopic(lesson);
    if (!sub) return false;
    const ex = getDisplayedExample(sub, st);
    const listStyle = isSec ? 'decimal' : 'arabic-indic';
    const showFinal = !!(ex.finalAnswer && !isRedundantFinalAnswer(ex.steps, ex.finalAnswer));

    const wFmt = function (txt) {
      return utils.formatMathForWordHtml ? utils.formatMathForWordHtml(String(txt || ''), isSec) : escHtml(String(txt || ''));
    };

    const htmlDoc =
      '<div dir="rtl" lang="ar" style="direction:rtl; text-align:right; font-family:\'Traditional Arabic\',\'Cairo\',serif; line-height:1.8; color:#0f172a;">' +
        '<div style="border:2px solid #1e3a8a; border-radius:6pt; padding:10pt; margin-bottom:10pt; background:#f8fafc;">' +
          '<h3 style="margin:0 0 6pt 0; color:#1e3a8a; font-size:16pt;">' + wFmt(lesson.title + ' — ' + sub.title) + '</h3>' +
          '<p style="margin:4pt 0; font-size:14pt;"><strong>📌 التوضيح المفاهيمي:</strong> ' + wFmt(sub.summary) + '</p>' +
          ((sub.steps && sub.steps.length)
            ? '<ol style="margin:4pt 18pt 6pt 0; font-size:13.5pt; list-style-type:' + listStyle + ';">' + sub.steps.map(function (s) { return '<li>' + wFmt(s) + '</li>'; }).join('') + '</ol>'
            : '') +
          '<div style="background:#ecfdf5; border-right:3pt solid #059669; padding:8pt; margin-top:8pt;">' +
            '<p style="margin:0 0 4pt 0; font-size:14pt; color:#065f46;"><strong>✍️ ' + (ex.isExactUserSolution ? 'المسألة:' : 'مثال توضيحي محلول:') + '</strong> ' + wFmt(ex.problem) + '</p>' +
            ((ex.steps && ex.steps.length)
              ? '<ol style="margin:4pt 18pt; font-size:13.5pt; list-style-type:' + listStyle + ';">' + ex.steps.map(function (s) { return '<li>' + wFmt(s) + '</li>'; }).join('') + '</ol>'
              : '') +
            (showFinal ? '<p style="margin:4pt 0 0 0; font-size:13.5pt;"><strong>✅ الخلاصة:</strong> ' + wFmt(ex.finalAnswer) + '</p>' : '') +
          '</div>' +
          (sub.commonMistake
            ? '<p style="margin:8pt 0 0 0; font-size:13pt; color:#92400e;"><strong>⚠️ تنبيه خطأ شائع:</strong> ' + wFmt(sub.commonMistake) + '</p>'
            : '') +
        '</div>' +
      '</div>';

    const plainText = [
      stripToPlain(lesson.title + ' — ' + sub.title, isSec),
      'التوضيح: ' + stripToPlain(sub.summary, isSec),
      (sub.steps || []).map(function (s, idx) { return fmtPlainNum(idx + 1, isSec) + ') ' + stripToPlain(s, isSec); }).join('\n'),
      (ex.isExactUserSolution ? 'المسألة: ' : 'المثال التوضيحي: ') + stripToPlain(ex.problem, isSec),
      (ex.steps || []).map(function (s) { return '  - ' + stripToPlain(s, isSec); }).join('\n'),
      showFinal ? ('الناتج: ' + stripToPlain(ex.finalAnswer, isSec)) : ''
    ].filter(Boolean).join('\n');

    try {
      if (navigator && navigator.clipboard && typeof navigator.clipboard.write === 'function' && typeof ClipboardItem === 'function') {
        await navigator.clipboard.write([
          new ClipboardItem({
            'text/html': new Blob([htmlDoc], { type: 'text/html' }),
            'text/plain': new Blob([plainText], { type: 'text/plain' })
          })
        ]);
        if (utils.showToast) utils.showToast('✓ تم نسخ الشرح والمثال التوضيحي بتنسيق Word!', 'success', isSec);
        return true;
      }
    } catch (e) {}

    try {
      if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(plainText);
        if (utils.showToast) utils.showToast('✓ تم نسخ الشرح والمثال إلى الحافظة!', 'success', isSec);
        return true;
      }
    } catch (e2) {}
    return false;
  }

  function printCard(lessonId) {
    const lesson = getLessonById(lessonId);
    if (!lesson || typeof window === 'undefined') return;
    const isSec = isSecondaryLesson(lesson);
    const win = window.open('', '_blank', 'width=900,height=750');
    if (!win) {
      if (typeof window.print === 'function') window.print();
      return;
    }
    const cardHtml = renderActiveCardHtml(lesson);
    win.document.write(
      '<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8">' +
      '<title>' + escHtml(lesson.title || 'شرح جزئية') + '</title>' +
      '<link rel="stylesheet" href="assets/vendor/katex/katex.min.css">' +
      '<link rel="stylesheet" href="assets/css/platform.css">' +
      '<style>body{background:#fff;padding:18px;font-family:\'Cairo\',\'Tajawal\',sans-serif;} .ce-card-actions,.ce-admin-hint,.ce-mini-btn{display:none!important;}</style>' +
      '</head><body><div class="ce-wrapper ' + (isSec ? 'is-sec-stage' : 'is-ar-stage') + '">' +
      '<h2 style="color:#1e3a8a;margin-bottom:12px;">' + fmt(lesson.title + ' (' + (lesson.grade || '') + ')', isSec) + '</h2>' +
      cardHtml + '</div><script>setTimeout(function(){window.print();},350);</script></body></html>'
    );
    win.document.close();
  }

  global.ConceptExplainer = {
    buildBuiltInSubtopics: buildBuiltInSubtopics,
    buildSmartLocalMatch: buildSmartLocalMatch,
    trySolveUserProblemLocally: trySolveUserProblemLocally,
    isRedundantFinalAnswer: isRedundantFinalAnswer,
    renderPane: renderPane,
    selectSubtopic: selectSubtopic,
    nextExample: nextExample,
    toggleQuickCheck: toggleQuickCheck,
    updateDraft: updateDraft,
    handleCustomSubmit: handleCustomSubmit,
    requestCustomExplanation: requestCustomExplanation,
    toggleTeacherForm: toggleTeacherForm,
    submitTeacherSubtopic: submitTeacherSubtopic,
    copyToWord: copyToWord,
    printCard: printCard
  };

})(typeof window !== 'undefined' ? window : globalThis);
