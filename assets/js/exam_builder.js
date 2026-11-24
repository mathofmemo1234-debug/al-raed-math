/**
 * ==========================================================================
 * منشئ الاختبارات التفاعلي (اختبار فترة / اختبار نهائي) — (الأول المتوسط ١م • السادس الابتدائي ٦ب)
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * ==========================================================================
 */

(function (global) {
  'use strict';

  const STORAGE_KEY_PREFIX = 'raed_exam_draft_v2_';
  const LEGACY_G6_STORAGE_KEY = 'raed_g6_exam_draft_v1';
  const ACTIVE_BOOK_STORAGE_KEY = 'raed_exam_active_book_v2';
  const PROFILE_STORAGE_KEY = 'raed_exam_profile_v1';
  const CUSTOM_LOGO_STORAGE_KEY = 'raed_exam_custom_logo_v1';
  const PROFILE_KEYS = ['ministry', 'district', 'schoolCompany', 'school', 'teacher', 'principal', 'includeLogo'];

  const BOOK_PRESETS = {
    g1m: {
      id: 'g1m',
      label: 'الأول المتوسط (١ م)',
      heroTitle: '📝 منشئ الاختبارات التفاعلي (اختبار فترة / اختبار نهائي) — الصف الأول المتوسط',
      autogenTitle: '⚡ التوليد المتوازن التلقائي من فصول كتاب «١ م»',
      grade: 'الأول المتوسط',
      stage: 'المرحلة المتوسطة',
      periodTitle: 'اختبار الفترة الأولى — رياضيات الأول المتوسط',
      finalTitle: 'الاختبار النهائي للفصل الدراسي الأول — رياضيات الأول المتوسط',
      periodChapters: ['g1m-t1-c1', 'g1m-t1-c2'],
      finalChapters: ['g1m-t1-c1', 'g1m-t1-c2', 'g1m-t1-c3', 'g1m-t1-c4']
    },
    g6: {
      id: 'g6',
      label: 'السادس الابتدائي (٦ ب)',
      heroTitle: '📝 منشئ الاختبارات التفاعلي (اختبار فترة / اختبار نهائي) — الصف السادس الابتدائي',
      autogenTitle: '⚡ التوليد المتوازن التلقائي من فصول كتاب «٦ ب»',
      grade: 'السادس الابتدائي',
      stage: 'المرحلة الابتدائية',
      periodTitle: 'اختبار الفترة الأولى — مادة الرياضيات',
      finalTitle: 'الاختبار النهائي للفصل الدراسي الأول — مادة الرياضيات',
      periodChapters: ['g6-t1-c1', 'g6-t1-c2'],
      finalChapters: ['g6-t1-c1', 'g6-t1-c2', 'g6-t1-c3', 'g6-t1-c4', 'g6-t1-c5']
    }
  };

  function getPreset(bookId) {
    return BOOK_PRESETS[bookId] || BOOK_PRESETS.g1m;
  }

  function loadSavedProfile() {
    const out = {};
    try {
      if (typeof localStorage === 'undefined') return out;
      const raw = localStorage.getItem(PROFILE_STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === 'object') {
          PROFILE_KEYS.forEach(function (k) {
            if (parsed[k] !== undefined) out[k] = parsed[k];
          });
        }
      }
      const logoRaw = localStorage.getItem(CUSTOM_LOGO_STORAGE_KEY);
      if (logoRaw && /^data:image\//i.test(logoRaw)) {
        out.customLogoDataUrl = logoRaw;
      }
    } catch (e) { /* ignore storage errors */ }
    return out;
  }

  function saveProfile(headerObj) {
    try {
      if (typeof localStorage === 'undefined' || !headerObj) return;
      const prof = {};
      PROFILE_KEYS.forEach(function (k) {
        if (headerObj[k] !== undefined) prof[k] = headerObj[k];
      });
      localStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(prof));
      if (headerObj.customLogoDataUrl && /^data:image\//i.test(headerObj.customLogoDataUrl)) {
        localStorage.setItem(CUSTOM_LOGO_STORAGE_KEY, headerObj.customLogoDataUrl);
      } else {
        localStorage.removeItem(CUSTOM_LOGO_STORAGE_KEY);
      }
    } catch (e) { /* ignore storage quota errors */ }
  }

  function resizeImageFile(file, maxDim, cb) {
    if (!file || typeof FileReader === 'undefined') return;
    const utils = getUtils();
    if (file.size > 8 * 1024 * 1024) {
      if (utils) utils.showToast('حجم الصورة كبير جداً (الحد الأقصى ٨ ميجابايت).', 'warning');
      return;
    }
    const reader = new FileReader();
    reader.onload = function () {
      const rawUrl = String(reader.result || '');
      if (typeof Image === 'undefined' || typeof document === 'undefined') {
        cb(rawUrl);
        return;
      }
      const img = new Image();
      img.onload = function () {
        try {
          const w = img.naturalWidth || img.width || maxDim;
          const h = img.naturalHeight || img.height || maxDim;
          const scale = Math.min(1, maxDim / Math.max(w, h));
          const tw = Math.max(1, Math.round(w * scale));
          const th = Math.max(1, Math.round(h * scale));
          const canvas = document.createElement('canvas');
          canvas.width = tw;
          canvas.height = th;
          const ctx = canvas.getContext('2d');
          ctx.clearRect(0, 0, tw, th);
          ctx.drawImage(img, 0, 0, tw, th);
          cb(canvas.toDataURL('image/png'));
        } catch (e) {
          cb(rawUrl);
        }
      };
      img.onerror = function () { cb(rawUrl); };
      img.src = rawUrl;
    };
    reader.readAsDataURL(file);
  }

  function makeDefaultHeader(bookId, examType) {
    const preset = getPreset(bookId);
    const isFinal = examType === 'final';
    const base = {
      ministry: 'المملكة العربية السعودية',
      district: 'الإدارة العامة للتعليم بمحافظة جدة',
      schoolCompany: 'شركة المدارس المتقدمة',
      school: 'مدارس المتقدمة – للتعلم الذكي (جدة)',
      stage: preset.stage || 'المرحلة المتوسطة',
      examTitle: isFinal ? preset.finalTitle : preset.periodTitle,
      subject: 'الرياضيات',
      grade: preset.grade,
      term: 'الأول',
      year: '١٤٤٨ هـ',
      teacher: 'أ. محمد عبدالله جمعة',
      principal: 'حسين عبد الله أزيبي',
      duration: isFinal ? 'ساعتان' : '٤٥ دقيقة',
      instructions: 'أجب عن جميع الأسئلة التالية مستعملاً الأرقام العربية المشرقية، وتأكد من مراجعة إجاباتك قبل التسليم.',
      includeLogo: true,
      customLogoDataUrl: ''
    };
    return Object.assign(base, loadSavedProfile());
  }

  const initialBookId = (function () {
    try {
      if (typeof localStorage !== 'undefined') {
        const savedBook = localStorage.getItem(ACTIVE_BOOK_STORAGE_KEY);
        if (savedBook && BOOK_PRESETS[savedBook]) {
          if (savedBook === 'g1m' && global.GRADE1M_BOOK_DATA) return 'g1m';
          if (savedBook === 'g6' && global.GRADE6_BOOK_DATA) return 'g6';
        }
      }
    } catch (e) { /* ignore */ }
    return global.GRADE1M_BOOK_DATA ? 'g1m' : 'g6';
  })();

  const state = {
    bookId: initialBookId,
    examType: 'period', // 'period' | 'final'
    header: makeDefaultHeader(initialBookId, 'period'),
    options: {
      includeAnswerKey: true,
      groupByType: true
    },
    autoGen: {
      chapters: getPreset(initialBookId).periodChapters.slice(),
      mcqCount: 10,
      tfCount: 5,
      essayCount: 3
    },
    questions: [],
    editingIndex: -1,
    showPreview: false,
    showCustomModal: false,
    customType: 'mcq',
    customDraftImage: '',
    customDraftCaption: '',
    dragIndex: -1,
    container: null
  };

  function getUtils() {
    return global.ArabicUtils;
  }

  function getBookData(bookId) {
    const bid = bookId || state.bookId;
    if (bid === 'g1m' && global.GRADE1M_BOOK_DATA) return global.GRADE1M_BOOK_DATA;
    if (global.GRADE6_BOOK_DATA) return global.GRADE6_BOOK_DATA;
    if (global.GRADE1M_BOOK_DATA) return global.GRADE1M_BOOK_DATA;
    return { chapters: [], flatQuestionBank: [] };
  }

  function inferQuestionBookId(q) {
    if (!q) return state.bookId;
    if (q.gradeId === 'g1m' || (q.lessonId && q.lessonId.indexOf('g1m') === 0) || (q.chapterId && q.chapterId.indexOf('g1m') === 0)) {
      return 'g1m';
    }
    if (q.gradeId === 'g6' || (q.lessonId && q.lessonId.indexOf('g6') === 0) || (q.chapterId && q.chapterId.indexOf('g6') === 0)) {
      return 'g6';
    }
    return state.bookId;
  }

  function isUserApproved() {
    return !!(window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isApproved === 'function' && window.FirebaseAuthManager.isApproved());
  }

  function getQuestionTypeName(type) {
    if (type === 'mcq') return 'الاختيار من متعدد';
    if (type === 'tf') return 'الصواب والخطأ';
    if (type === 'essay') return 'المسائل والمقالي';
    return 'الأسئلة';
  }

  function applyBookDefaults(bookId, examType) {
    const preset = getPreset(bookId);
    const mode = examType || state.examType || 'period';
    const approved = isUserApproved();
    state.bookId = preset.id;
    state.examType = mode;
    state.header = makeDefaultHeader(preset.id, mode);
    let mcq = mode === 'final' ? 20 : 10;
    let tf = mode === 'final' ? 10 : 5;
    let essay = mode === 'final' ? 5 : 3;
    if (!approved) {
      mcq = Math.min(5, mcq);
      tf = Math.min(5, tf);
      essay = Math.min(5, essay);
    }
    state.autoGen = {
      chapters: (mode === 'final' ? preset.finalChapters : preset.periodChapters).slice(),
      mcqCount: mcq,
      tfCount: tf,
      essayCount: essay
    };
  }

  function loadDraft(targetBookId) {
    const bid = targetBookId || state.bookId;
    applyBookDefaults(bid, 'period');
    state.questions = [];
    state.editingIndex = -1;
    try {
      if (typeof localStorage === 'undefined') return;
      let raw = localStorage.getItem(STORAGE_KEY_PREFIX + bid);
      if (!raw && bid === 'g6') {
        raw = localStorage.getItem(LEGACY_G6_STORAGE_KEY);
      }
      if (!raw) return;
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === 'object') {
        const mode = parsed.examType || 'period';
        state.examType = mode;
        const baseHeader = makeDefaultHeader(bid, mode);
        const savedProf = loadSavedProfile();
        if (parsed.header) {
          state.header = Object.assign({}, baseHeader, parsed.header, savedProf);
        } else {
          state.header = baseHeader;
        }
        if (parsed.options) state.options = Object.assign({ includeAnswerKey: true, groupByType: true }, parsed.options);
        if (parsed.autoGen) state.autoGen = Object.assign({}, state.autoGen, parsed.autoGen);
        if (Array.isArray(parsed.questions)) state.questions = parsed.questions;
      }
    } catch (e) {
      // ignore storage errors
    }
  }

  function saveDraft() {
    try {
      if (typeof localStorage === 'undefined') return;
      saveProfile(state.header);
      const draftHeader = Object.assign({}, state.header);
      delete draftHeader.customLogoDataUrl;
      localStorage.setItem(ACTIVE_BOOK_STORAGE_KEY, state.bookId);
      localStorage.setItem(STORAGE_KEY_PREFIX + state.bookId, JSON.stringify({
        bookId: state.bookId,
        examType: state.examType,
        header: draftHeader,
        options: state.options,
        autoGen: state.autoGen,
        questions: state.questions
      }));
    } catch (e) {
      // ignore storage errors
    }
    updateBadge();
  }

  function setBook(bookId) {
    if (!BOOK_PRESETS[bookId] || state.bookId === bookId) return;
    saveDraft();
    loadDraft(bookId);
    saveDraft();
    render();
    const utils = getUtils();
    if (utils) utils.showToast('تم التحويل إلى اختبارات ' + getPreset(bookId).label, 'info');
  }

  function updateBadge() {
    if (typeof document === 'undefined') return;
    const utils = getUtils();
    const text = utils ? utils.toEasternDigits(state.questions.length) : String(state.questions.length);
    const badge = document.getElementById('exam-count-badge');
    if (badge) badge.textContent = text;
    const navBadge = document.getElementById('nav-exam-count-badge');
    if (navBadge) navBadge.textContent = text;
  }

  function cloneQuestionForExam(q) {
    const copy = JSON.parse(JSON.stringify(q));
    if (!copy.uid) copy.uid = 'custom-' + Date.now() + '-' + Math.random().toString(36).slice(2, 6);
    if (!copy.type) copy.type = copy.options ? 'mcq' : (typeof copy.is_true === 'boolean' ? 'tf' : 'essay');
    if (!copy.typeLabel) {
      copy.typeLabel = copy.type === 'mcq' ? 'اختيار من متعدد' : (copy.type === 'tf' ? 'صواب وخطأ' : 'مسألة مقالية');
    }
    if (copy.marks === undefined) copy.marks = copy.type === 'essay' ? 2 : 1;
    if (!copy.q && copy.statement) copy.q = copy.statement;
    if (copy.image === undefined) copy.image = '';
    if (copy.imageCaption === undefined) copy.imageCaption = '';
    if (!copy.gradeId) copy.gradeId = inferQuestionBookId(copy);
    return copy;
  }

  function hasQuestion(uid) {
    return state.questions.some(function (q) { return q.uid === uid; });
  }

  function addQuestion(q, silent) {
    if (!q) return false;
    const utils = getUtils();
    const approved = isUserApproved();

    // قيد الأعضاء غير المعتمدين: ٥ أسئلة كحد أقصى من كل نوع
    if (!approved) {
      const qType = q.type || 'mcq';
      const countOfType = state.questions.filter(function (item) { return (item.type || 'mcq') === qType; }).length;
      if (countOfType >= 5) {
        if (!silent) {
          utils.showToast('🔒 لغير الأعضاء المعتمدين: تم بلوغ الحد الأقصى (٥ أسئلة) من نوع (' + getQuestionTypeName(qType) + '). اطلب الاعتماد لإضافة غير محدودة.', 'warning');
        }
        return false;
      }
    }

    const targetBook = inferQuestionBookId(q);
    if (targetBook && BOOK_PRESETS[targetBook] && targetBook !== state.bookId && state.questions.length === 0) {
      saveDraft();
      loadDraft(targetBook);
    }
    if (q.uid && hasQuestion(q.uid)) {
      if (!silent) utils.showToast('هذا السؤال مضاف بالفعل في قائمة الاختبار.', 'info');
      return false;
    }
    state.questions.push(cloneQuestionForExam(q));
    saveDraft();
    if (!silent) utils.showToast('✓ تمت إضافة السؤال إلى منشئ الاختبارات.', 'success');
    if (state.container && isActiveInViewport()) render();
    return true;
  }

  function addQuestions(qs) {
    const utils = getUtils();
    const approved = isUserApproved();
    let added = 0;
    let hitCapCount = 0;

    (qs || []).forEach(function (q) {
      const qType = (q && q.type) || 'mcq';
      if (!approved) {
        const countOfType = state.questions.filter(function (item) { return (item.type || 'mcq') === qType; }).length;
        if (countOfType >= 5) {
          hitCapCount++;
          return;
        }
      }
      if (addQuestion(q, true)) added++;
    });

    if (added > 0) {
      if (hitCapCount > 0) {
        utils.showToast('✓ تمت إضافة ' + utils.toEasternDigits(added) + ' أسئلة. تم إيقاف البقية لبلوغ الحد الأقصى (٥ أسئلة لكل نوع لغير المعتمدين).', 'warning');
      } else {
        utils.showToast('✓ تمت إضافة ' + utils.toEasternDigits(added) + ' أسئلة إلى منشئ الاختبارات.', 'success');
      }
    } else if (hitCapCount > 0) {
      utils.showToast('🔒 تعذر إضافة الأسئلة: تم الوصول للحد الأقصى المسموح لغير المعتمدين (٥ أسئلة من كل نوع). اطلب الاعتماد للفتح الكامل.', 'warning');
    } else {
      utils.showToast('جميع الأسئلة المحددة مضافة مسبقاً في الاختبار.', 'info');
    }
    if (state.container && isActiveInViewport()) render();
  }

  function removeQuestion(uid) {
    state.questions = state.questions.filter(function (q) { return q.uid !== uid; });
    saveDraft();
    if (state.container && isActiveInViewport()) render();
  }

  function isActiveInViewport() {
    return state.container && state.container.querySelector('.eb-wrapper') !== null;
  }

  function getCount() {
    return state.questions.length;
  }

  function setExamType(mode) {
    const utils = getUtils();
    const preset = getPreset(state.bookId);
    const defaults = makeDefaultHeader(state.bookId, mode);
    const approved = isUserApproved();
    state.examType = mode;
    state.header.examTitle = defaults.examTitle;
    state.header.duration = defaults.duration;
    state.header.grade = defaults.grade;
    if (mode === 'period') {
      state.autoGen.chapters = preset.periodChapters.slice();
      state.autoGen.mcqCount = approved ? 10 : 5;
      state.autoGen.tfCount = approved ? 5 : 5;
      state.autoGen.essayCount = approved ? 3 : 3;
      utils.showToast('تم ضبط إعدادات «اختبار الفترة»' + (!approved ? ' (معاينة: ٥ أسئلة للنوع)' : ' (١٠ اختيار + ٥ صواب/خطأ + ٣ مقالي)') + '.', 'info');
    } else {
      state.autoGen.chapters = preset.finalChapters.slice();
      state.autoGen.mcqCount = approved ? 20 : 5;
      state.autoGen.tfCount = approved ? 10 : 5;
      state.autoGen.essayCount = approved ? 5 : 5;
      utils.showToast('تم ضبط إعدادات «الاختبار النهائي» الشامل' + (!approved ? ' (معاينة: ٥ أسئلة لكل نوع)' : ' (٤٠ درجة افتراضياً)') + '.', 'info');
    }
    saveDraft();
    render();
  }

  function toggleAutoChapter(chId, checked) {
    const set = new Set(state.autoGen.chapters || []);
    if (checked) set.add(chId);
    else set.delete(chId);
    state.autoGen.chapters = Array.from(set);
    saveDraft();
  }

  function setAutoCount(key, val) {
    const utils = getUtils();
    const approved = isUserApproved();
    let num = Math.max(0, Math.min(50, Math.round(utils.toWesternNumber(val, 0))));
    if (!approved && num > 5) {
      num = 5;
      utils.showToast('🔒 لغير الأعضاء المعتمدين: الحد الأقصى هو ٥ أسئلة من كل نوع. يرجى تسجيل الدخول واعتماد الحساب للتوليد غير المحدود.', 'warning');
    }
    state.autoGen[key] = num;
    saveDraft();
  }

  /**
   * التوليد التلقائي المتوازن للأسئلة عبر الفصول والدروس المحددة دون تكرار
   */
  function pickBalancedQuestions(pool, count, chapters) {
    if (count <= 0 || !pool.length) return [];
    const byChapter = {};
    chapters.forEach(function (cid) { byChapter[cid] = []; });
    pool.forEach(function (q) {
      if (byChapter[q.chapterId]) byChapter[q.chapterId].push(q);
    });

    // خلط عشوائي خفيف داخل كل فصل مع مراعاة التوزيع عبر الدروس
    Object.keys(byChapter).forEach(function (cid) {
      const arr = byChapter[cid];
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
      }
    });

    const picked = [];
    const usedUids = new Set();
    let round = 0;
    while (picked.length < count && round < 200) {
      let progressed = false;
      for (let c = 0; c < chapters.length && picked.length < count; c++) {
        const list = byChapter[chapters[c]] || [];
        if (round < list.length) {
          const candidate = list[round];
          if (!usedUids.has(candidate.uid)) {
            usedUids.add(candidate.uid);
            picked.push(cloneQuestionForExam(candidate));
            progressed = true;
          }
        }
      }
      if (!progressed) break;
      round++;
    }
    return picked;
  }

  function generateBalancedExam() {
    const utils = getUtils();
    const approved = isUserApproved();
    const chapters = state.autoGen.chapters || [];
    if (!chapters.length) {
      utils.showToast('يرجى تحديد فصل واحد على الأقل للتوليد التلقائي.', 'warning');
      return;
    }

    const bank = getBookData().flatQuestionBank || [];
    const mcqPool = bank.filter(function (q) { return q.type === 'mcq' && chapters.indexOf(q.chapterId) !== -1; });
    const tfPool = bank.filter(function (q) { return q.type === 'tf' && chapters.indexOf(q.chapterId) !== -1; });
    const essayPool = bank.filter(function (q) { return q.type === 'essay' && chapters.indexOf(q.chapterId) !== -1; });

    let targetMcq = state.autoGen.mcqCount;
    let targetTf = state.autoGen.tfCount;
    let targetEssay = state.autoGen.essayCount;

    if (!approved) {
      let clamped = false;
      if (targetMcq > 5) { targetMcq = 5; clamped = true; }
      if (targetTf > 5) { targetTf = 5; clamped = true; }
      if (targetEssay > 5) { targetEssay = 5; clamped = true; }
      if (clamped) {
        state.autoGen.mcqCount = targetMcq;
        state.autoGen.tfCount = targetTf;
        state.autoGen.essayCount = targetEssay;
        utils.showToast('🔒 تم ضبط الأعداد إلى ٥ أسئلة لكل نوع (الحد الأقصى لغير الأعضاء المعتمدين).', 'warning');
      }
    }

    const mcqs = pickBalancedQuestions(mcqPool, targetMcq, chapters);
    const tfs = pickBalancedQuestions(tfPool, targetTf, chapters);
    const essays = pickBalancedQuestions(essayPool, targetEssay, chapters);

    state.questions = mcqs.concat(tfs, essays);
    state.editingIndex = -1;
    saveDraft();
    render();
    utils.showToast(
      '⚡ تم توليد اختبار متوازن من ' + utils.toEasternDigits(state.questions.length) +
      ' سؤالاً بمجموع ' + utils.formatMark(getTotalMarks()) + '!' +
      (!approved ? ' (معاينة: ٥ أسئلة لكل نوع)' : ' (عضو معتمد: توليد كامل غير محدود ✓)'),
      'success'
    );
  }

  function getTotalMarks() {
    return global.ExamExporter ? global.ExamExporter.computeTotalMarks(state.questions) : state.questions.length;
  }

  function updateHeaderField(key, val) {
    const utils = getUtils();
    if (key === 'includeLogo') {
      state.header.includeLogo = !!val;
    } else if (key === 'customLogoDataUrl') {
      state.header.customLogoDataUrl = val ? String(val) : '';
    } else {
      state.header[key] = utils.toEasternDigits(val);
    }
    saveDraft();
    if (state.showPreview) renderPreviewOnly();
  }

  function uploadSchoolLogo(input) {
    const file = input && input.files && input.files[0];
    if (!file) return;
    resizeImageFile(file, 320, function (dataUrl) {
      state.header.customLogoDataUrl = dataUrl;
      state.header.includeLogo = true;
      saveDraft();
      render();
      const utils = getUtils();
      if (utils) utils.showToast('✓ تم تحديث شعار المدرسة وحفظه تلقائياً.', 'success');
    });
  }

  function resetSchoolLogo() {
    state.header.customLogoDataUrl = '';
    saveDraft();
    render();
    const utils = getUtils();
    if (utils) utils.showToast('تمت استعادة الشعار الافتراضي للمنصة.', 'info');
  }

  function uploadEditQuestionImage(idx, input) {
    const q = state.questions[idx];
    const file = input && input.files && input.files[0];
    if (!q || !file) return;
    resizeImageFile(file, 680, function (dataUrl) {
      q.image = dataUrl;
      saveDraft();
      render();
      const utils = getUtils();
      if (utils) utils.showToast('✓ تم إرفاق الصورة بالسؤال.', 'success');
    });
  }

  function removeEditQuestionImage(idx) {
    const q = state.questions[idx];
    if (!q) return;
    q.image = '';
    q.imageCaption = '';
    saveDraft();
    render();
  }

  function uploadCustomQuestionImage(input) {
    const file = input && input.files && input.files[0];
    if (!file) return;
    resizeImageFile(file, 680, function (dataUrl) {
      state.customDraftImage = dataUrl;
      const previewEl = document.getElementById('eb-cust-img-preview');
      if (previewEl) {
        previewEl.innerHTML =
          '<img src="' + dataUrl + '" alt="معاينة صورة السؤال" style="max-height:90px;border-radius:6px;border:1px solid #cbd5e1;" />' +
          '<button type="button" class="qb-act-btn" style="color:#dc2626;" onclick="window.ExamBuilder.clearCustomQuestionImage()">✖️ إزالة الصورة</button>';
      }
      const utils = getUtils();
      if (utils) utils.showToast('✓ تم تجهيز الصورة للسؤال المخصص.', 'success');
    });
  }

  function clearCustomQuestionImage() {
    state.customDraftImage = '';
    state.customDraftCaption = '';
    const previewEl = document.getElementById('eb-cust-img-preview');
    if (previewEl) previewEl.innerHTML = '';
    const fileEl = document.getElementById('eb-cust-img-file');
    if (fileEl) fileEl.value = '';
  }

  function updateOptionField(key, val) {
    state.options[key] = !!val;
    saveDraft();
    if (state.showPreview) renderPreviewOnly();
  }

  function updateQuestionMark(idx, rawVal) {
    const utils = getUtils();
    if (!state.questions[idx]) return;
    const num = Math.max(0.5, Math.min(20, utils.toWesternNumber(rawVal, 1)));
    state.questions[idx].marks = num;
    saveDraft();
    render();
  }

  function moveQuestion(idx, dir) {
    const target = idx + dir;
    if (target < 0 || target >= state.questions.length) return;
    const tmp = state.questions[idx];
    state.questions[idx] = state.questions[target];
    state.questions[target] = tmp;
    if (state.editingIndex === idx) state.editingIndex = target;
    else if (state.editingIndex === target) state.editingIndex = idx;
    saveDraft();
    render();
  }

  function onDragStart(idx) {
    state.dragIndex = idx;
  }

  function onDragOver(e) {
    e.preventDefault();
  }

  function onDrop(targetIdx) {
    if (state.dragIndex < 0 || state.dragIndex === targetIdx) return;
    const moved = state.questions.splice(state.dragIndex, 1)[0];
    state.questions.splice(targetIdx, 0, moved);
    state.dragIndex = -1;
    state.editingIndex = -1;
    saveDraft();
    render();
  }

  function duplicateQuestion(idx) {
    const orig = state.questions[idx];
    if (!orig) return;
    const dup = JSON.parse(JSON.stringify(orig));
    dup.uid = orig.uid + '-copy-' + Date.now().toString().slice(-4);
    state.questions.splice(idx + 1, 0, dup);
    saveDraft();
    render();
    getUtils().showToast('✓ تم تكرار السؤال.', 'success');
  }

  function deleteQuestionAt(idx) {
    state.questions.splice(idx, 1);
    if (state.editingIndex === idx) state.editingIndex = -1;
    else if (state.editingIndex > idx) state.editingIndex--;
    saveDraft();
    render();
  }

  function toggleEdit(idx) {
    state.editingIndex = (state.editingIndex === idx) ? -1 : idx;
    render();
  }

  function saveInlineEdit(idx, e) {
    e.preventDefault();
    const utils = getUtils();
    const q = state.questions[idx];
    if (!q) return;

    const textEl = document.getElementById('eb-edit-text-' + idx);
    const marksEl = document.getElementById('eb-edit-marks-' + idx);
    const expEl = document.getElementById('eb-edit-exp-' + idx);
    const capEl = document.getElementById('eb-edit-img-cap-' + idx);

    q.q = utils.formatMathExponents(utils.toEasternDigits((textEl && textEl.value) || q.q));
    if (q.type === 'tf') q.statement = q.q;
    q.marks = Math.max(0.5, Math.min(20, utils.toWesternNumber(marksEl && marksEl.value, q.marks || 1)));
    if (capEl) q.imageCaption = utils.toEasternDigits(capEl.value.trim());

    if (q.type === 'mcq') {
      q.options = [0, 1, 2, 3].map(function (i) {
        const el = document.getElementById('eb-edit-opt-' + idx + '-' + i);
        return utils.formatMathExponents(utils.toEasternDigits((el && el.value) || ''));
      });
      const radio = document.querySelector('input[name="eb-edit-correct-' + idx + '"]:checked');
      if (radio) q.correct = Number(radio.value);
      q.explanation = utils.formatMathExponents(utils.toEasternDigits((expEl && expEl.value) || ''));
    } else if (q.type === 'tf') {
      const tfRadio = document.querySelector('input[name="eb-edit-tf-' + idx + '"]:checked');
      if (tfRadio) q.is_true = (tfRadio.value === 'true');
      q.explanation = utils.formatMathExponents(utils.toEasternDigits((expEl && expEl.value) || ''));
    } else {
      const ansEl = document.getElementById('eb-edit-ans-' + idx);
      const linesEl = document.getElementById('eb-edit-lines-' + idx);
      q.ans = utils.formatMathExponents(utils.toEasternDigits((ansEl && ansEl.value) || ''));
      q.lines = Math.max(2, Math.min(6, Math.round(utils.toWesternNumber(linesEl && linesEl.value, 3))));
    }

    state.editingIndex = -1;
    saveDraft();
    render();
    utils.showToast('✓ تم حفظ تعديلات السؤال بنجاح!', 'success');
  }

  function toggleCustomModal(open) {
    state.showCustomModal = !!open;
    if (!open) {
      state.customDraftImage = '';
      state.customDraftCaption = '';
    }
    render();
  }

  function setCustomType(t) {
    state.customType = t;
    render();
  }

  function saveCustomQuestion(e) {
    e.preventDefault();
    const utils = getUtils();
    const t = state.customType;
    const text = utils.formatMathExponents(utils.toEasternDigits(document.getElementById('eb-cust-q').value.trim()));
    const marks = Math.max(0.5, Math.min(20, utils.toWesternNumber(document.getElementById('eb-cust-marks').value, t === 'essay' ? 2 : 1)));
    const capEl = document.getElementById('eb-cust-img-cap');
    const customCap = capEl ? utils.toEasternDigits(capEl.value.trim()) : '';
    if (!text) return;

    const newQ = {
      uid: 'custom-' + Date.now(),
      type: t,
      typeLabel: t === 'mcq' ? 'اختيار من متعدد' : (t === 'tf' ? 'صواب وخطأ' : 'مسألة مقالية'),
      chapterId: 'custom',
      chapterNumber: 'مخصص',
      chapterTitle: 'سؤال مضاف يدوياً',
      lessonId: 'custom',
      lessonNumber: 'مخصص',
      lessonTitle: 'إضافة المعلم',
      difficulty: 'متوسط',
      marks: marks,
      q: text,
      image: state.customDraftImage || '',
      imageCaption: customCap || ''
    };

    if (t === 'mcq') {
      newQ.options = [0, 1, 2, 3].map(function (i) {
        return utils.formatMathExponents(utils.toEasternDigits(document.getElementById('eb-cust-opt-' + i).value.trim() || ('خيار ' + utils.CHOICE_LETTERS[i])));
      });
      const r = document.querySelector('input[name="eb-cust-correct"]:checked');
      newQ.correct = r ? Number(r.value) : 0;
      newQ.explanation = utils.formatMathExponents(utils.toEasternDigits(document.getElementById('eb-cust-exp').value.trim()));
    } else if (t === 'tf') {
      newQ.statement = text;
      const r = document.querySelector('input[name="eb-cust-tf"]:checked');
      newQ.is_true = r ? (r.value === 'true') : true;
      newQ.explanation = utils.formatMathExponents(utils.toEasternDigits(document.getElementById('eb-cust-exp').value.trim()));
    } else {
      newQ.ans = utils.formatMathExponents(utils.toEasternDigits(document.getElementById('eb-cust-ans').value.trim()));
      newQ.lines = Math.max(2, Math.min(6, Math.round(utils.toWesternNumber(document.getElementById('eb-cust-lines').value, 3))));
    }

    state.questions.push(newQ);
    state.showCustomModal = false;
    state.customDraftImage = '';
    state.customDraftCaption = '';
    saveDraft();
    render();
    utils.showToast('✓ تمت إضافة السؤال المخصص إلى الاختبار!', 'success');
  }

  function clearExam() {
    if (!state.questions.length) return;
    if (!global.confirm || global.confirm('هل تريد تفريغ جميع أسئلة الاختبار الحالي؟')) {
      state.questions = [];
      state.editingIndex = -1;
      saveDraft();
      render();
      getUtils().showToast('تم تفريغ قائمة الاختبار.', 'info');
    }
  }

  function togglePreview() {
    state.showPreview = !state.showPreview;
    render();
  }

  function getExamPayload() {
    return {
      examType: state.examType,
      header: state.header,
      options: state.options,
      questions: state.questions
    };
  }

  function renderPreviewOnly() {
    const el = document.getElementById('eb-live-preview-box');
    if (el && global.ExamExporter) {
      el.innerHTML = global.ExamExporter.buildExamPreviewHTML(getExamPayload(), { forPrint: false });
    }
  }

  function copyFullExamToWord() {
    if (!state.questions.length) {
      getUtils().showToast('يرجى إضافة أسئلة أولاً قبل النسخ إلى Word.', 'warning');
      return;
    }
    const sections = global.ExamExporter
      ? global.ExamExporter.groupQuestions(state.questions, state.options.groupByType)
      : [{ title: 'أسئلة الاختبار', type: 'mixed', items: state.questions }];
    const ordered = [];
    sections.forEach(function (s) {
      s.items.forEach(function (it) { ordered.push(it); });
    });
    getUtils().copyQuestionsToWord(ordered, {
      includeAnswers: state.options.includeAnswerKey,
      numbered: true,
      asTable: true,
      header: state.header,
      sections: sections
    });
  }

  function copyOneToWord(idx) {
    const q = state.questions[idx];
    if (!q) return;
    getUtils().copyQuestionsToWord([q], {
      includeAnswers: false,
      numbered: false,
      asTable: true
    });
  }

  function exportDocx() {
    if (global.ExamExporter) global.ExamExporter.exportDocx(getExamPayload());
  }

  function exportPdf() {
    if (global.ExamExporter) global.ExamExporter.exportPdf(getExamPayload());
  }

  function render(container) {
    if (container) state.container = container;
    if (!state.container) return;

    const utils = getUtils();
    const chapters = getBookData().chapters || [];
    const totalMarks = getTotalMarks();
    const mcqCount = state.questions.filter(function (q) { return q.type === 'mcq'; }).length;
    const tfCount = state.questions.filter(function (q) { return q.type === 'tf'; }).length;
    const essayCount = state.questions.filter(function (q) { return q.type === 'essay'; }).length;

    const preset = getPreset(state.bookId);

    const previewHtml = (state.showPreview && global.ExamExporter)
      ? global.ExamExporter.buildExamPreviewHTML(getExamPayload(), { forPrint: false })
      : '';

    const html = `
      <div class="eb-wrapper" dir="rtl">
        <!-- ترويسة منشئ الاختبارات واختيار النمط -->
        <div class="eb-hero-banner">
          <div>
            <div class="qb-grade-switcher" role="group" aria-label="اختيار الصف الدراسي للاختبار">
              ${['g1m', 'g6'].map(function (bid) {
                const cfg = BOOK_PRESETS[bid];
                const hasData = bid === 'g1m' ? !!global.GRADE1M_BOOK_DATA : !!global.GRADE6_BOOK_DATA;
                if (!hasData) return '';
                return '<button type="button" class="qb-grade-btn ' + (state.bookId === bid ? 'active' : '') +
                  '" onclick="window.ExamBuilder.setBook(\'' + bid + '\')">📘 ' + utils.escapeHtml(cfg.label) + '</button>';
              }).join('')}
            </div>
            <h2>${utils.escapeHtml(preset.heroTitle)}</h2>
            <p>تحرير كامل للأسئلة والصور المرفقة والترويسة والدرجات والترتيب مع التصدير الفوري بصيغتي Word (.docx) و PDF بنظام RTL والأرقام العربية المشرقية</p>
          </div>
          <div class="eb-mode-cards">
            <button type="button" class="eb-mode-btn ${state.examType === 'period' ? 'active' : ''}" onclick="window.ExamBuilder.setExamType('period')">
              <span class="eb-mode-title">📋 اختبار فترة</span>
              <span class="eb-mode-sub">٤٥ دقيقة • ٢٠ درجة افتراضياً</span>
            </button>
            <button type="button" class="eb-mode-btn ${state.examType === 'final' ? 'active' : ''}" onclick="window.ExamBuilder.setExamType('final')">
              <span class="eb-mode-title">🎓 اختبار نهائي</span>
              <span class="eb-mode-sub">ساعتان • ٤٠ درجة شاملة</span>
            </button>
          </div>
        </div>

        <!-- شريط حالة العضوية وترخيص الاختبارات -->
        ${isUserApproved() ? `
          <div class="eb-tier-banner approved">
            <div class="eb-tier-icon">🌟</div>
            <div class="eb-tier-content">
              <div class="eb-tier-title">ترخيص العضوية المعتمدة (كامل الصلاحيات) ✓</div>
              <div class="eb-tier-desc">متاح لك توليد عدد غير محدود من الأسئلة من كافة الفصول والمراحل وتصدير Word ونماذج الإجابة كاملة دون أي قيود.</div>
            </div>
            <span class="eb-tier-badge approved">توليد غير محدود ∞</span>
          </div>
        ` : `
          <div class="eb-tier-banner preview">
            <div class="eb-tier-icon">🔒</div>
            <div class="eb-tier-content">
              <div class="eb-tier-title">نسخة المعاينة المجانية (محدد بـ ٥ أسئلة كحد أقصى لكل نوع)</div>
              <div class="eb-tier-desc">يُسمح بتوليد وإضافة حتى ٥ أسئلة فقط من كل نوع (اختيار، صواب وخطأ، مقالي). لرفع كافة القيود والتوليد الشامل، يُرجى طلب الاعتماد من المدير العام.</div>
            </div>
            <button type="button" class="eb-tier-btn" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()">
              طلب الاعتماد الكامل ↗
            </button>
          </div>
        `}

        <!-- المولد الذكي المتوازن للاختبار -->
        <div class="eb-card">
          <div class="eb-card-header">
            <h3>${utils.escapeHtml(preset.autogenTitle)}</h3>
            <span class="eb-hint">يوزع الأسئلة بعدالة بين الفصول والدروس المختارة دون تكرار</span>
          </div>
          <div class="eb-autogen-grid">
            <div class="eb-autogen-chapters">
              <div class="eb-sublabel">اختر الفصول المشمولة في الاختبار:</div>
              <div class="eb-chapter-checks">
                ${chapters.map(function (ch) {
                  const checked = (state.autoGen.chapters || []).indexOf(ch.id) !== -1;
                  return (
                    '<label class="eb-chap-chip ' + (checked ? 'checked' : '') + '">' +
                    '<input type="checkbox" ' + (checked ? 'checked' : '') +
                    ' onchange="window.ExamBuilder.toggleAutoChapter(\'' + utils.escapeHtml(ch.id) + '\', this.checked)">' +
                    '<span>' + utils.escapeHtml(utils.toEasternDigits(ch.number + ': ' + ch.title)) + '</span>' +
                    '</label>'
                  );
                }).join('')}
              </div>
            </div>

            <div class="eb-autogen-counts">
              <div class="eb-count-box">
                <label>اختيار من متعدد (١ درجة):</label>
                <input type="text" value="${utils.toEasternDigits(state.autoGen.mcqCount)}"
                  onchange="window.ExamBuilder.setAutoCount('mcqCount', this.value); this.value = window.ArabicUtils.toEasternDigits(Math.max(0, window.ArabicUtils.toWesternNumber(this.value, 0)))">
                ${!isUserApproved() ? '<span class="eb-cap-hint">🔒 حد المعاينة: ٥ أسئلة</span>' : '<span class="eb-unlimited-hint">🌟 غير محدود</span>'}
              </div>
              <div class="eb-count-box">
                <label>صواب وخطأ (١ درجة):</label>
                <input type="text" value="${utils.toEasternDigits(state.autoGen.tfCount)}"
                  onchange="window.ExamBuilder.setAutoCount('tfCount', this.value); this.value = window.ArabicUtils.toEasternDigits(Math.max(0, window.ArabicUtils.toWesternNumber(this.value, 0)))">
                ${!isUserApproved() ? '<span class="eb-cap-hint">🔒 حد المعاينة: ٥ أسئلة</span>' : '<span class="eb-unlimited-hint">🌟 غير محدود</span>'}
              </div>
              <div class="eb-count-box">
                <label>مسائل مقالية (درجتان):</label>
                <input type="text" value="${utils.toEasternDigits(state.autoGen.essayCount)}"
                  onchange="window.ExamBuilder.setAutoCount('essayCount', this.value); this.value = window.ArabicUtils.toEasternDigits(Math.max(0, window.ArabicUtils.toWesternNumber(this.value, 0)))">
                ${!isUserApproved() ? '<span class="eb-cap-hint">🔒 حد المعاينة: ٥ أسئلة</span>' : '<span class="eb-unlimited-hint">🌟 غير محدود</span>'}
              </div>
              <button type="button" class="nav-btn primary eb-gen-btn" onclick="window.ExamBuilder.generateBalancedExam()">
                ⚡ توليد الاختبار تلقائياً
              </button>
            </div>
          </div>
        </div>

        <!-- تحرير الترويسة الرسمية وخيارات الورقة -->
        <div class="eb-card">
          <div class="eb-card-header">
            <h3>🏛️ إعدادات الترويسة الرسمية وبيانات ورقة الاختبار</h3>
            <span class="eb-hint">جميع الأرقام تحوّل تلقائياً إلى الأرقام العربية المشرقية (٠-٩)</span>
          </div>
          <div class="eb-header-form">
            <div class="eb-field">
              <label>الدولة / الوزارة:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.ministry))}" onchange="window.ExamBuilder.updateHeaderField('ministry', this.value)">
            </div>
            <div class="eb-field">
              <label>إدارة التعليم:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.district))}" onchange="window.ExamBuilder.updateHeaderField('district', this.value)">
            </div>
            <div class="eb-field">
              <label>الشركة / المؤسسة التعليمية:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.schoolCompany || ''))}" onchange="window.ExamBuilder.updateHeaderField('schoolCompany', this.value)">
            </div>
            <div class="eb-field">
              <label>اسم المدرسة:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.school))}" onchange="window.ExamBuilder.updateHeaderField('school', this.value)">
            </div>
            <div class="eb-field">
              <label>المرحلة الدراسية:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.stage || ''))}" onchange="window.ExamBuilder.updateHeaderField('stage', this.value)">
            </div>
            <div class="eb-field">
              <label>عنوان الاختبار:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.examTitle))}" onchange="window.ExamBuilder.updateHeaderField('examTitle', this.value)">
            </div>
            <div class="eb-field">
              <label>المادة الدراسية:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.subject || 'الرياضيات'))}" onchange="window.ExamBuilder.updateHeaderField('subject', this.value)">
            </div>
            <div class="eb-field">
              <label>العام الدراسي:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.year))}" onchange="window.ExamBuilder.updateHeaderField('year', this.value)">
            </div>
            <div class="eb-field">
              <label>الصف الدراسي:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.grade))}" onchange="window.ExamBuilder.updateHeaderField('grade', this.value)">
            </div>
            <div class="eb-field">
              <label>الفصل الدراسي:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.term))}" onchange="window.ExamBuilder.updateHeaderField('term', this.value)">
            </div>
            <div class="eb-field">
              <label>زمن الاختبار:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.duration))}" onchange="window.ExamBuilder.updateHeaderField('duration', this.value)">
            </div>
            <div class="eb-field">
              <label>اسم المعلم:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.teacher))}" onchange="window.ExamBuilder.updateHeaderField('teacher', this.value)">
            </div>
            <div class="eb-field">
              <label>اسم مدير المدرسة:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.principal || ''))}" onchange="window.ExamBuilder.updateHeaderField('principal', this.value)">
            </div>
            <div class="eb-field eb-col-span-2">
              <label>تعليمات الاختبار للطلاب:</label>
              <input type="text" value="${utils.escapeHtml(utils.toEasternDigits(state.header.instructions))}" onchange="window.ExamBuilder.updateHeaderField('instructions', this.value)">
            </div>
          </div>

          <div class="eb-logo-picker">
            <img class="eb-logo-preview" src="${utils.escapeHtml(state.header.customLogoDataUrl || 'assets/img/logo.png')}" alt="شعار المدرسة المعتمد">
            <div class="eb-logo-picker-info">
              <strong>شعار المدرسة في الترويسة الرسمية:</strong>
              <span>${state.header.customLogoDataUrl ? 'شعار مخصص مرفوع من المستخدم (محفوظ تلقائياً)' : 'الشعار الافتراضي للمنصة — يمكنك رفع شعار مدرستك الخاص'}</span>
              <div class="eb-logo-picker-actions">
                <label class="qb-act-btn" style="cursor:pointer;">
                  🖼️ رفع / تغيير شعار المدرسة
                  <input type="file" accept="image/*" style="display:none;" onchange="window.ExamBuilder.uploadSchoolLogo(this)">
                </label>
                ${state.header.customLogoDataUrl ? '<button type="button" class="qb-act-btn" onclick="window.ExamBuilder.resetSchoolLogo()">🔄 استعادة الشعار الافتراضي</button>' : ''}
              </div>
            </div>
          </div>

          <div class="eb-options-row">
            <label class="qb-checkbox-toggle">
              <input type="checkbox" ${state.header.includeLogo !== false ? 'checked' : ''} onchange="window.ExamBuilder.updateHeaderField('includeLogo', this.checked)">
              <span>تضمين شعار المدرسة في الترويسة</span>
            </label>
            <label class="qb-checkbox-toggle">
              <input type="checkbox" ${state.options.includeAnswerKey !== false ? 'checked' : ''} onchange="window.ExamBuilder.updateOptionField('includeAnswerKey', this.checked)">
              <span>إرفاق نموذج الإجابة وتوزيع الدرجات في صفحة مستقلة</span>
            </label>
            <label class="qb-checkbox-toggle">
              <input type="checkbox" ${state.options.groupByType !== false ? 'checked' : ''} onchange="window.ExamBuilder.updateOptionField('groupByType', this.checked)">
              <span>تجميع الأسئلة تلقائياً حسب النوع (الأول/الثاني/الثالث)</span>
            </label>
          </div>
        </div>

        <!-- شريط التصدير والمجموع الثابت -->
        <div class="eb-export-bar">
          <div class="eb-summary-pills">
            <span class="eb-sum-pill">إجمالي الأسئلة: <strong>${utils.toEasternDigits(state.questions.length)}</strong></span>
            <span class="eb-sum-pill">اختيارات: <strong>${utils.toEasternDigits(mcqCount)}</strong> • صواب/خطأ: <strong>${utils.toEasternDigits(tfCount)}</strong> • مقالي: <strong>${utils.toEasternDigits(essayCount)}</strong></span>
            <span class="eb-sum-pill total">الدرجة الكلية: <strong>${utils.escapeHtml(utils.formatMark(totalMarks))}</strong></span>
          </div>
          <div class="eb-export-actions">
            <button type="button" class="nav-btn" onclick="window.ExamBuilder.togglePreview()">
              ${state.showPreview ? '🔼 إخفاء معاينة A4' : '👁️ معاينة ورقة الاختبار (A4)'}
            </button>
            <button type="button" class="nav-btn" onclick="window.ExamBuilder.copyFullExamToWord()">
              📋 نسخ الاختبار لـ Word
            </button>
            <button type="button" class="nav-btn primary" onclick="window.ExamBuilder.exportDocx()">
              📄 تصدير Word (.docx)
            </button>
            <button type="button" class="nav-btn danger-btn" onclick="window.ExamBuilder.exportPdf()">
              📕 تصدير PDF للطباعة
            </button>
          </div>
        </div>

        <!-- معاينة ورقة الاختبار A4 الحية -->
        ${state.showPreview ? '<div class="eb-preview-shell"><div class="eb-preview-title">👁️ معاينة حية لورقة الاختبار (حجم A4 — اتجاه RTL)</div><div id="eb-live-preview-box" class="exam-a4-preview">' + previewHtml + '</div></div>' : ''}

        <!-- قائمة تحرير وترتيب أسئلة الاختبار -->
        <div class="eb-card">
          <div class="eb-card-header">
            <h3>🛠️ تحرير وترتيب أسئلة الاختبار المختارة (${utils.toEasternDigits(state.questions.length)})</h3>
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <button type="button" class="nav-btn primary" onclick="window.ExamBuilder.toggleCustomModal(true)">✏️ إضافة سؤال مخصص جديد</button>
              <button type="button" class="nav-btn" onclick="window.Platform && window.Platform.switchView('question-bank')">🏦 استعراض بنك الأسئلة</button>
              <button type="button" class="nav-btn" style="color:#dc2626;" onclick="window.ExamBuilder.clearExam()">🗑️ تفريغ الاختبار</button>
            </div>
          </div>

          ${state.showCustomModal ? renderCustomQuestionForm() : ''}

          <div class="eb-questions-editor">
            ${state.questions.length ? state.questions.map(function (q, idx) {
              return renderQuestionEditorCard(q, idx);
            }).join('') : `
              <div style="text-align:center; padding:36px 20px; color:var(--text-muted);">
                <div style="font-size:2.4rem; margin-bottom:10px;">📝</div>
                <h4 style="color:var(--text-main); margin-bottom:6px;">سلة الاختبار فارغة حالياً</h4>
                <p style="margin-bottom:16px;">اضغط على <strong>«⚡ توليد الاختبار تلقائياً»</strong> أعلاه لبناء اختبار متوازن بضغطة زر، أو أضف أسئلة محددة من بنك الأسئلة والدروس.</p>
                <button type="button" class="nav-btn primary" onclick="window.ExamBuilder.generateBalancedExam()">⚡ توليد اختبار الآن</button>
              </div>
            `}
          </div>
        </div>
      </div>
    `;

    state.container.innerHTML = html;
  }

  function renderQuestionEditorCard(q, idx) {
    const utils = getUtils();
    const isEditing = state.editingIndex === idx;
    const typeLabel = q.type === 'mcq' ? 'اختيار من متعدد' : (q.type === 'tf' ? 'صواب وخطأ' : 'مسألة مقالية');

    let previewSnippet = '';
    if (q.type === 'mcq' && Array.isArray(q.options)) {
      previewSnippet = '<div class="eb-q-opts-preview">' + q.options.slice(0, 4).map(function (opt, oIdx) {
        const isCorr = oIdx === q.correct;
        return '<span class="' + (isCorr ? 'is-corr' : '') + '"><strong>' + utils.CHOICE_LETTERS[oIdx] + ')</strong> ' +
          utils.renderMathHtml(opt) + (isCorr ? ' ✓' : '') + '</span>';
      }).join('') + '</div>';
    } else if (q.type === 'tf') {
      previewSnippet = '<div class="eb-q-tf-preview">الإجابة الصحيحة: <strong>' + (q.is_true ? 'صواب (✓)' : 'خطأ (✗)') + '</strong></div>';
    } else {
      previewSnippet = '<div class="eb-q-essay-preview"><strong>الحل النموذجي:</strong> ' + utils.renderMathHtml(q.ans || '') + '</div>';
    }

    let editFormHtml = '';
    if (isEditing) {
      let typeFields = '';
      if (q.type === 'mcq') {
        typeFields =
          '<div class="eb-edit-opts-grid">' +
          [0, 1, 2, 3].map(function (oIdx) {
            const val = (q.options && q.options[oIdx]) || '';
            return (
              '<div class="eb-edit-opt-row">' +
              '<label class="eb-radio-lbl"><input type="radio" name="eb-edit-correct-' + idx + '" value="' + oIdx + '" ' + (q.correct === oIdx ? 'checked' : '') + '> <span>الخيار ' + utils.CHOICE_LETTERS[oIdx] + ' (صحيح)</span></label>' +
              '<input id="eb-edit-opt-' + idx + '-' + oIdx + '" type="text" value="' + utils.escapeHtml(utils.stripMathToInputText(val)) + '" required>' +
              '</div>'
            );
          }).join('') +
          '</div>' +
          '<div class="eb-field"><label>التفسير الرياضي:</label><input id="eb-edit-exp-' + idx + '" type="text" value="' + utils.escapeHtml(utils.stripMathToInputText(q.explanation || '')) + '"></div>';
      } else if (q.type === 'tf') {
        typeFields =
          '<div class="eb-tf-edit-radios">' +
          '<label class="eb-radio-lbl"><input type="radio" name="eb-edit-tf-' + idx + '" value="true" ' + (q.is_true ? 'checked' : '') + '> <span>صواب (✓)</span></label>' +
          '<label class="eb-radio-lbl"><input type="radio" name="eb-edit-tf-' + idx + '" value="false" ' + (!q.is_true ? 'checked' : '') + '> <span>خطأ (✗)</span></label>' +
          '</div>' +
          '<div class="eb-field"><label>التفسير الرياضي:</label><input id="eb-edit-exp-' + idx + '" type="text" value="' + utils.escapeHtml(utils.stripMathToInputText(q.explanation || '')) + '"></div>';
      } else {
        typeFields =
          '<div class="eb-field"><label>الحل النموذجي:</label><textarea id="eb-edit-ans-' + idx + '" rows="2">' + utils.escapeHtml(utils.stripMathToInputText(q.ans || '')) + '</textarea></div>' +
          '<div class="eb-field" style="max-width:180px;"><label>عدد أسطر الإجابة:</label><input id="eb-edit-lines-' + idx + '" type="text" value="' + utils.toEasternDigits(q.lines || 3) + '"></div>';
      }

      editFormHtml = `
        <form class="eb-inline-edit-form" onsubmit="window.ExamBuilder.saveInlineEdit(${idx}, event)">
          <div class="eb-field">
            <label>نص السؤال:</label>
            <textarea id="eb-edit-text-${idx}" rows="2" required>${utils.escapeHtml(utils.stripMathToInputText(q.q || q.statement || ''))}</textarea>
          </div>
          <div class="eb-field" style="max-width:180px;">
            <label>الدرجة:</label>
            <input id="eb-edit-marks-${idx}" type="text" value="${utils.escapeHtml(utils.formatMarkShort(q.marks !== undefined ? q.marks : 1))}" required>
          </div>
          ${typeFields}
          <div class="eb-edit-image-row">
            <label style="font-weight:700;font-size:0.86rem;">🖼️ صورة توضيحية للسؤال:</label>
            <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:4px;">
              ${q.image ? '<img src="' + utils.escapeHtml(q.image) + '" alt="صورة السؤال" style="max-height:68px;border-radius:6px;border:1px solid #cbd5e1;">' : '<span class="eb-hint">لا توجد صورة مرفقة حالياً</span>'}
              <label class="qb-act-btn" style="cursor:pointer;">
                ${q.image ? '🔄 تغيير الصورة' : '➕ إرفاق صورة'}
                <input type="file" accept="image/*" style="display:none;" onchange="window.ExamBuilder.uploadEditQuestionImage(${idx}, this)">
              </label>
              ${q.image ? '<button type="button" class="qb-act-btn" style="color:#dc2626;" onclick="window.ExamBuilder.removeEditQuestionImage(' + idx + ')">🗑️ إزالة الصورة</button>' : ''}
              <input id="eb-edit-img-cap-${idx}" type="text" placeholder="وصف الصورة (اختياري)..." value="${utils.escapeHtml(utils.toEasternDigits(q.imageCaption || ''))}" style="flex:1;min-width:180px;">
            </div>
          </div>
          <div style="display:flex; gap:8px; margin-top:10px;">
            <button type="submit" class="nav-btn primary">💾 حفظ التعديل</button>
            <button type="button" class="nav-btn" onclick="window.ExamBuilder.toggleEdit(${idx})">إلغاء</button>
          </div>
        </form>
      `;
    }

    return `
      <div class="eb-q-card" draggable="true"
           ondragstart="window.ExamBuilder.onDragStart(${idx})"
           ondragover="window.ExamBuilder.onDragOver(event)"
           ondrop="window.ExamBuilder.onDrop(${idx})">
        <div class="eb-q-card-top">
          <div class="eb-q-card-meta">
            <span class="eb-drag-handle" title="اسحب لإعادة الترتيب">⠿</span>
            <span class="q-badge">س ${utils.toEasternDigits(idx + 1)}</span>
            <span class="qb-pill chapter-pill">${utils.escapeHtml(utils.toEasternDigits((q.chapterNumber || '') + ' • ' + (q.lessonTitle || '')))}</span>
            <span class="qb-pill">${utils.escapeHtml(typeLabel)}</span>
          </div>
          <div class="eb-q-card-controls">
            <label class="eb-inline-mark">
              <span>الدرجة:</span>
              <input type="text" value="${utils.escapeHtml(utils.formatMarkShort(q.marks !== undefined ? q.marks : 1))}"
                onchange="window.ExamBuilder.updateQuestionMark(${idx}, this.value)">
            </label>
            <button type="button" class="qb-act-btn" title="تحريك لأعلى" onclick="window.ExamBuilder.moveQuestion(${idx}, -1)" ${idx === 0 ? 'disabled' : ''}>⬆️</button>
            <button type="button" class="qb-act-btn" title="تحريك لأسفل" onclick="window.ExamBuilder.moveQuestion(${idx}, 1)" ${idx === state.questions.length - 1 ? 'disabled' : ''}>⬇️</button>
            <button type="button" class="qb-act-btn" onclick="window.ExamBuilder.toggleEdit(${idx})">${isEditing ? '🔼 إغلاق' : '✏️ تعديل'}</button>
            <button type="button" class="qb-act-btn" title="تكرار السؤال" onclick="window.ExamBuilder.duplicateQuestion(${idx})">📄 تكرار</button>
            <button type="button" class="qb-act-btn copy-word-btn" title="نسخ لـ Word" onclick="window.ExamBuilder.copyOneToWord(${idx})">📋</button>
            <button type="button" class="qb-act-btn" style="color:#dc2626;" title="حذف" onclick="window.ExamBuilder.deleteQuestionAt(${idx})">🗑️</button>
          </div>
        </div>
        <div class="eb-q-card-prompt">${utils.renderMathHtml(q.q || q.statement || '')}</div>
        ${q.image ? (
          '<div class="eb-q-fig">' +
          '<img src="' + utils.escapeHtml(q.image) + '" alt="' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption || 'شكل السؤال')) + '" loading="lazy" data-caption="' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption || '')) + '" onclick="if(window.Platform&&window.Platform.openImageLightbox){window.Platform.openImageLightbox(this.getAttribute(\'src\'),this.getAttribute(\'data-caption\'));}" />' +
          (q.imageCaption ? '<div class="eb-q-fig-cap">' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption)) + '</div>' : '') +
          '</div>'
        ) : ''}
        ${previewSnippet}
        ${editFormHtml}
      </div>
    `;
  }

  function renderCustomQuestionForm() {
    const utils = getUtils();
    const t = state.customType;
    return `
      <form class="eb-custom-form" onsubmit="window.ExamBuilder.saveCustomQuestion(event)">
        <div class="eb-card-header" style="margin-bottom:10px;">
          <h4>✏️ إضافة سؤال مخصص جديد</h4>
          <button type="button" class="qb-act-btn" onclick="window.ExamBuilder.toggleCustomModal(false)">✖️ إغلاق</button>
        </div>
        <div class="eb-custom-type-tabs">
          <button type="button" class="qb-act-btn ${t === 'mcq' ? 'active-type' : ''}" onclick="window.ExamBuilder.setCustomType('mcq')">اختيار من متعدد</button>
          <button type="button" class="qb-act-btn ${t === 'tf' ? 'active-type' : ''}" onclick="window.ExamBuilder.setCustomType('tf')">صواب وخطأ</button>
          <button type="button" class="qb-act-btn ${t === 'essay' ? 'active-type' : ''}" onclick="window.ExamBuilder.setCustomType('essay')">مسألة مقالية</button>
        </div>
        <div class="eb-field">
          <label>نص السؤال:</label>
          <textarea id="eb-cust-q" rows="2" placeholder="اكتب نص السؤال هنا..." required></textarea>
        </div>
        <div class="eb-field" style="max-width:180px;">
          <label>الدرجة:</label>
          <input id="eb-cust-marks" type="text" value="${t === 'essay' ? '٢' : '١'}" required>
        </div>
        ${t === 'mcq' ? (
          '<div class="eb-edit-opts-grid">' +
          [0, 1, 2, 3].map(function (i) {
            return (
              '<div class="eb-edit-opt-row">' +
              '<label class="eb-radio-lbl"><input type="radio" name="eb-cust-correct" value="' + i + '" ' + (i === 0 ? 'checked' : '') + '> <span>الخيار ' + utils.CHOICE_LETTERS[i] + ' (صحيح)</span></label>' +
              '<input id="eb-cust-opt-' + i + '" type="text" placeholder="الخيار ' + utils.CHOICE_LETTERS[i] + '..." required>' +
              '</div>'
            );
          }).join('') +
          '</div>' +
          '<div class="eb-field"><label>التفسير الرياضي (اختياري):</label><input id="eb-cust-exp" type="text" placeholder="شرح الإجابة..."></div>'
        ) : t === 'tf' ? (
          '<div class="eb-tf-edit-radios">' +
          '<label class="eb-radio-lbl"><input type="radio" name="eb-cust-tf" value="true" checked> <span>صواب (✓)</span></label>' +
          '<label class="eb-radio-lbl"><input type="radio" name="eb-cust-tf" value="false"> <span>خطأ (✗)</span></label>' +
          '</div>' +
          '<div class="eb-field"><label>التفسير الرياضي (اختياري):</label><input id="eb-cust-exp" type="text" placeholder="التعليل..."></div>'
        ) : (
          '<div class="eb-field"><label>الحل النموذجي:</label><textarea id="eb-cust-ans" rows="2" placeholder="خطوات الحل النموذجية..."></textarea></div>' +
          '<div class="eb-field" style="max-width:180px;"><label>عدد أسطر الكتابة:</label><input id="eb-cust-lines" type="text" value="٣"></div>'
        )}
        <div class="eb-edit-image-row" style="margin-top:10px;">
          <label style="font-weight:700;font-size:0.86rem;">🖼️ إرفاق صورة بالسؤال المخصص (اختياري):</label>
          <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:4px;">
            <label class="qb-act-btn" style="cursor:pointer;">
              📷 اختيار صورة
              <input id="eb-cust-img-file" type="file" accept="image/*" style="display:none;" onchange="window.ExamBuilder.uploadCustomQuestionImage(this)">
            </label>
            <input id="eb-cust-img-cap" type="text" placeholder="وصف الصورة (اختياري)..." style="flex:1;min-width:180px;">
          </div>
          <div id="eb-cust-img-preview" style="display:flex;align-items:center;gap:8px;margin-top:6px;">
            ${state.customDraftImage ? '<img src="' + utils.escapeHtml(state.customDraftImage) + '" alt="معاينة صورة السؤال" style="max-height:90px;border-radius:6px;border:1px solid #cbd5e1;"><button type="button" class="qb-act-btn" style="color:#dc2626;" onclick="window.ExamBuilder.clearCustomQuestionImage()">✖️ إزالة الصورة</button>' : ''}
          </div>
        </div>
        <div style="margin-top:12px;">
          <button type="submit" class="nav-btn primary">➕ إضافة السؤال للاختبار</button>
        </div>
      </form>
    `;
  }

  loadDraft(state.bookId);

  global.ExamBuilder = {
    render: render,
    setBook: setBook,
    updateBadge: updateBadge,
    hasQuestion: hasQuestion,
    addQuestion: addQuestion,
    addQuestions: addQuestions,
    removeQuestion: removeQuestion,
    getCount: getCount,
    setExamType: setExamType,
    toggleAutoChapter: toggleAutoChapter,
    setAutoCount: setAutoCount,
    generateBalancedExam: generateBalancedExam,
    updateHeaderField: updateHeaderField,
    uploadSchoolLogo: uploadSchoolLogo,
    resetSchoolLogo: resetSchoolLogo,
    uploadEditQuestionImage: uploadEditQuestionImage,
    removeEditQuestionImage: removeEditQuestionImage,
    uploadCustomQuestionImage: uploadCustomQuestionImage,
    clearCustomQuestionImage: clearCustomQuestionImage,
    updateOptionField: updateOptionField,
    updateQuestionMark: updateQuestionMark,
    moveQuestion: moveQuestion,
    onDragStart: onDragStart,
    onDragOver: onDragOver,
    onDrop: onDrop,
    duplicateQuestion: duplicateQuestion,
    deleteQuestionAt: deleteQuestionAt,
    toggleEdit: toggleEdit,
    saveInlineEdit: saveInlineEdit,
    toggleCustomModal: toggleCustomModal,
    setCustomType: setCustomType,
    saveCustomQuestion: saveCustomQuestion,
    clearExam: clearExam,
    togglePreview: togglePreview,
    copyFullExamToWord: copyFullExamToWord,
    copyOneToWord: copyOneToWord,
    exportDocx: exportDocx,
    exportPdf: exportPdf
  };
})(typeof window !== 'undefined' ? window : globalThis);
