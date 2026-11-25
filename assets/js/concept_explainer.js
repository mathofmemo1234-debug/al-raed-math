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
  const CACHE_STORE_KEY = 'alraed_ce_cache_v1';
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
      return { problem: '', steps: [], finalAnswer: '', fig: '' };
    }
    return {
      problem: String(ex.problem || '').trim(),
      steps: Array.isArray(ex.steps) ? ex.steps.map(function (s) { return String(s || '').trim(); }).filter(Boolean) : [],
      finalAnswer: String(ex.finalAnswer || '').trim(),
      fig: String(ex.fig || ex.image || '').trim(),
      cap: String(ex.cap || ex.imageCaption || '').trim(),
      isSec: !!isSec
    };
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
      let concl = finalAnswer;
      if (!concl && solSteps.length > 1) {
        concl = solSteps[solSteps.length - 1];
      }
      pool.push(normalizeExampleObj({
        problem: p,
        steps: solSteps.length ? solSteps : (s ? [s] : []),
        finalAnswer: concl || '',
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
   * مطابقة محلية ذكية من نصوص الدرس وأمثلة الكتاب عند العمل بدون إنترنت أو بدون ضبط GEMINI_API_KEY
   */
  function buildSmartLocalMatch(lesson, query, level, extraNote) {
    const isSec = isSecondaryLesson(lesson);
    const tokens = tokenizeQuery(query);
    const builtins = buildBuiltInSubtopics(lesson);
    const prep = lesson.prep || {};
    const sum = lesson.summary || {};
    const quiz = lesson.quiz || {};

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
    const pool = collectExamplePool(lesson, isSec);
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

  function ensureLessonState(lessonId) {
    if (!state.lessonStates[lessonId]) {
      state.lessonStates[lessonId] = {
        selectedSubtopicId: '',
        customResult: null,
        altExOffset: 0,
        revealCheck: false,
        loading: false,
        showTeacherForm: false,
        queryDraft: '',
        level: 'متوسط منهجي'
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

    return `
      <div class="ce-card ${sub.source === 'ai' ? 'is-ai' : ''}">
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
            <span>✍️ المثال التوضيحي المحلول خطوة بخطوة</span>
          </div>
          <div class="ce-ex-problem"><strong>المثال:</strong> ${fmt(ex.problem, isSec)}</div>
          ${figHtml}
          ${exStepsHtml}
          ${ex.finalAnswer ? `<div class="ce-ex-final">✅ <strong>الخلاصة / الناتج النهائي:</strong> ${fmt(ex.finalAnswer, isSec)}</div>` : ''}
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
      ? 'اكتب أي جزئية تريد شرحها بمثال (مثال: المجال الجبري، عدم الاتصال القفزي، خطي التقارب...)'
      : 'اكتب أي جزئية تريد شرحها بمثال (مثال: تحليل العوامل، ترتيب العمليات، توحيد المقامات...)';

    return `
      <div class="ce-wrapper" id="ce-root-${escHtml(lesson.id)}">
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
    rerenderInDom(lessonId);
  }

  function nextExample(lessonId) {
    const st = ensureLessonState(lessonId);
    st.altExOffset = (st.altExOffset || 0) + 1;
    rerenderInDom(lessonId);
  }

  function toggleQuickCheck(lessonId) {
    const st = ensureLessonState(lessonId);
    st.revealCheck = !st.revealCheck;
    rerenderInDom(lessonId);
  }

  function updateDraft(lessonId, val) {
    const st = ensureLessonState(lessonId);
    st.queryDraft = String(val || '');
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
    if (cached) {
      st.customResult = cached;
      st.altExOffset = 0;
      st.revealCheck = false;
      rerenderInDom(lessonId);
      return cached;
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
                finalAnswer: fmtPlainNum(d.workedExample && d.workedExample.finalAnswer, isSec)
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
    setCachedExplanation(cacheKey, localEntry);
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

    const wFmt = function (txt) {
      return utils.formatMathForWordHtml ? utils.formatMathForWordHtml(String(txt || ''), isSec) : escHtml(String(txt || ''));
    };

    const htmlDoc =
      '<div dir="rtl" lang="ar" style="direction:rtl; text-align:right; font-family:\'Traditional Arabic\',\'Cairo\',serif; line-height:1.8; color:#0f172a;">' +
        '<div style="border:2px solid #1e3a8a; border-radius:6pt; padding:10pt; margin-bottom:10pt; background:#f8fafc;">' +
          '<h3 style="margin:0 0 6pt 0; color:#1e3a8a; font-size:16pt;">' + wFmt(lesson.title + ' — ' + sub.title) + '</h3>' +
          '<p style="margin:4pt 0; font-size:14pt;"><strong>📌 التوضيح المفاهيمي:</strong> ' + wFmt(sub.summary) + '</p>' +
          ((sub.steps && sub.steps.length)
            ? '<ol style="margin:4pt 18pt 6pt 0; font-size:13.5pt;">' + sub.steps.map(function (s) { return '<li>' + wFmt(s) + '</li>'; }).join('') + '</ol>'
            : '') +
          '<div style="background:#ecfdf5; border-right:3pt solid #059669; padding:8pt; margin-top:8pt;">' +
            '<p style="margin:0 0 4pt 0; font-size:14pt; color:#065f46;"><strong>✍️ مثال توضيحي محلول:</strong> ' + wFmt(ex.problem) + '</p>' +
            ((ex.steps && ex.steps.length)
              ? '<ol style="margin:4pt 18pt; font-size:13.5pt;">' + ex.steps.map(function (s) { return '<li>' + wFmt(s) + '</li>'; }).join('') + '</ol>'
              : '') +
            (ex.finalAnswer ? '<p style="margin:4pt 0 0 0; font-size:13.5pt;"><strong>✅ الخلاصة:</strong> ' + wFmt(ex.finalAnswer) + '</p>' : '') +
          '</div>' +
          (sub.commonMistake
            ? '<p style="margin:8pt 0 0 0; font-size:13pt; color:#92400e;"><strong>⚠️ تنبيه خطأ شائع:</strong> ' + wFmt(sub.commonMistake) + '</p>'
            : '') +
        '</div>' +
      '</div>';

    const plainText = [
      stripToPlain(lesson.title + ' — ' + sub.title, isSec),
      'التوضيح: ' + stripToPlain(sub.summary, isSec),
      (sub.steps || []).map(function (s, idx) { return (idx + 1) + ') ' + stripToPlain(s, isSec); }).join('\n'),
      'المثال التوضيحي: ' + stripToPlain(ex.problem, isSec),
      (ex.steps || []).map(function (s, idx) { return '  - ' + stripToPlain(s, isSec); }).join('\n'),
      ex.finalAnswer ? ('الناتج: ' + stripToPlain(ex.finalAnswer, isSec)) : ''
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
      '</head><body><h2 style="color:#1e3a8a;margin-bottom:12px;">' + fmt(lesson.title + ' (' + (lesson.grade || '') + ')', isSec) + '</h2>' +
      cardHtml + '<script>setTimeout(function(){window.print();},350);</script></body></html>'
    );
    win.document.close();
  }

  global.ConceptExplainer = {
    buildBuiltInSubtopics: buildBuiltInSubtopics,
    buildSmartLocalMatch: buildSmartLocalMatch,
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
