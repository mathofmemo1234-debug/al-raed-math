/**
 * ==========================================================================
 * بنك الأسئلة الشامل (الأول المتوسط ١م • السادس الابتدائي ٦ب)
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * ==========================================================================
 */

(function (global) {
  'use strict';

  const PAGE_SIZE = 20;

  const BOOKS_CONFIG = {
    g3m: {
      id: 'g3m',
      label: 'الثالث المتوسط (٣ م)',
      heading: '🏦 بنك أسئلة الصف الثالث المتوسط (الفصل الدراسي الأول)',
      subtitle: 'مستخرج ومنقح بالكامل من كتاب الرياضيات «٣ م» • ٥ فصول • ٢٥ درساً • أرقام عربية مشرقية ١٠٠٪ وجاهز للنسخ المباشر إلى Word'
    },
    g1m: {
      id: 'g1m',
      label: 'الأول المتوسط (١ م)',
      heading: '🏦 بنك أسئلة الصف الأول المتوسط (الفصل الدراسي الأول)',
      subtitle: 'مستخرج ومنقح بالكامل من كتاب الرياضيات «١ م» • ٤ فصول • ٣١ درساً • مع ٣٨ شكلاً وصورة تعليمية وجاهز للنسخ المباشر إلى Word'
    },
    g6: {
      id: 'g6',
      label: 'السادس الابتدائي (٦ ب)',
      heading: '🏦 بنك أسئلة الصف السادس الابتدائي (الفصل الدراسي الأول)',
      subtitle: 'مستخرج ومنقح بالكامل من كتاب الرياضيات «٦ ب» • ٥ فصول • ٣٥ درساً • أرقام عربية مشرقية ١٠٠٪ وجاهز للنسخ المباشر إلى Word'
    }
  };

  const state = {
    bookId: global.GRADE3M_BOOK_DATA ? 'g3m' : (global.GRADE1M_BOOK_DATA ? 'g1m' : 'g6'),
    chapterId: 'all',
    lessonId: 'all',
    type: 'all', // 'all' | 'mcq' | 'tf' | 'essay'
    difficulty: 'all', // 'all' | 'سهل' | 'متوسط' | 'تحدٍّ'
    onlyImages: false,
    search: '',
    includeAnswersOnCopy: false,
    page: 1,
    selectedUids: new Set(),
    revealedAnswers: new Set(),
    container: null
  };

  function getUtils() {
    return global.ArabicUtils;
  }

  function isUserApproved() {
    return !!(global.FirebaseAuthManager && typeof global.FirebaseAuthManager.isApproved === 'function' && global.FirebaseAuthManager.isApproved());
  }

  function getBookData(bookId) {
    const id = bookId || state.bookId;
    if (id === 'g3m' && global.GRADE3M_BOOK_DATA) return global.GRADE3M_BOOK_DATA;
    if (id === 'g1m' && global.GRADE1M_BOOK_DATA) return global.GRADE1M_BOOK_DATA;
    if (global.GRADE6_BOOK_DATA) return global.GRADE6_BOOK_DATA;
    if (global.GRADE1M_BOOK_DATA) return global.GRADE1M_BOOK_DATA;
    if (global.GRADE3M_BOOK_DATA) return global.GRADE3M_BOOK_DATA;
    return { bookMeta: {}, chapters: [], lessons: {}, flatQuestionBank: [] };
  }

  function getFilteredQuestions() {
    const utils = getUtils();
    const bank = getBookData().flatQuestionBank || [];
    const searchNorm = utils.normalizeSearchText(state.search);
    const approved = isUserApproved();

    const typeCounters = { mcq: 0, tf: 0, essay: 0 };
    const maxPerType = approved ? Infinity : 5;

    return bank.filter(function (q) {
      if (state.chapterId !== 'all' && q.chapterId !== state.chapterId) return false;
      if (state.lessonId !== 'all' && q.lessonId !== state.lessonId) return false;
      if (state.type !== 'all' && q.type !== state.type) return false;
      if (state.difficulty !== 'all' && q.difficulty !== state.difficulty) return false;
      if (state.onlyImages && !q.image) return false;

      if (searchNorm) {
        const parts = [
          q.q,
          q.lessonTitle,
          q.chapterTitle,
          q.explanation || '',
          q.ans || '',
          q.imageCaption || '',
          Array.isArray(q.options) ? q.options.join(' ') : ''
        ].join(' ');
        if (!utils.normalizeSearchText(parts).includes(searchNorm)) return false;
      }

      if (!approved) {
        const t = q.type || 'mcq';
        if ((typeCounters[t] || 0) >= maxPerType) return false;
        typeCounters[t] = (typeCounters[t] || 0) + 1;
      }

      return true;
    });
  }

  function getSelectedQuestionObjects() {
    const bank = getBookData().flatQuestionBank || [];
    return bank.filter(function (q) {
      return state.selectedUids.has(q.uid);
    });
  }

  function getQuestionByUid(uid) {
    const bank = getBookData().flatQuestionBank || [];
    for (let i = 0; i < bank.length; i++) {
      if (bank[i].uid === uid) return bank[i];
    }
    return null;
  }

  function render(container) {
    if (container) state.container = container;
    if (!state.container) return;

    const utils = getUtils();
    const data = getBookData();
    const bank = data.flatQuestionBank || [];
    const chapters = data.chapters || [];

    const totalMcq = bank.filter(function (q) { return q.type === 'mcq'; }).length;
    const totalTf = bank.filter(function (q) { return q.type === 'tf'; }).length;
    const totalEssay = bank.filter(function (q) { return q.type === 'essay'; }).length;
    const totalIllustrated = bank.filter(function (q) { return !!q.image; }).length;
    const bookInfo = BOOKS_CONFIG[state.bookId] || BOOKS_CONFIG.g1m;

    const filtered = getFilteredQuestions();
    const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    if (state.page > totalPages) state.page = totalPages;
    if (state.page < 1) state.page = 1;

    const startIdx = (state.page - 1) * PAGE_SIZE;
    const pageItems = filtered.slice(startIdx, startIdx + PAGE_SIZE);

    // قائمة الدروس المتاحة حسب الفصل المختار
    let availableLessons = [];
    chapters.forEach(function (ch) {
      if (state.chapterId === 'all' || ch.id === state.chapterId) {
        (ch.lessons || []).forEach(function (ls) {
          availableLessons.push(ls);
        });
      }
    });

    const selectedCount = state.selectedUids.size;
    const examApi = global.ExamBuilder;

    const html = `
      <div class="qb-wrapper" dir="rtl">
        <!-- ترويسة بنك الأسئلة والإحصائيات -->
        <div class="qb-hero-banner">
          <div>
            <div class="qb-grade-switcher" role="group" aria-label="اختيار المرحلة الدراسية">
              ${['g3m', 'g1m', 'g6'].map(function (bid) {
                const cfg = BOOKS_CONFIG[bid];
                const hasData = bid === 'g3m' ? !!global.GRADE3M_BOOK_DATA : (bid === 'g1m' ? !!global.GRADE1M_BOOK_DATA : !!global.GRADE6_BOOK_DATA);
                if (!hasData) return '';
                return '<button type="button" class="qb-grade-btn ' + (state.bookId === bid ? 'active' : '') +
                  '" onclick="window.QuestionBank.setBook(\'' + bid + '\')">📘 ' + utils.escapeHtml(cfg.label) + '</button>';
              }).join('')}
            </div>
            <h2>${utils.escapeHtml(bookInfo.heading)}</h2>
            <p>${utils.escapeHtml(bookInfo.subtitle)}</p>
          </div>
          <div class="qb-stats-row">
            <div class="qb-stat-pill">
              <span class="qb-stat-num">${utils.toEasternDigits(bank.length)}</span>
              <span class="qb-stat-lbl">إجمالي الأسئلة</span>
            </div>
            <div class="qb-stat-pill">
              <span class="qb-stat-num">${utils.toEasternDigits(totalMcq)}</span>
              <span class="qb-stat-lbl">اختيار من متعدد</span>
            </div>
            <div class="qb-stat-pill">
              <span class="qb-stat-num">${utils.toEasternDigits(totalTf)}</span>
              <span class="qb-stat-lbl">صواب وخطأ</span>
            </div>
            <div class="qb-stat-pill">
              <span class="qb-stat-num">${utils.toEasternDigits(totalEssay)}</span>
              <span class="qb-stat-lbl">مسائل مقالية</span>
            </div>
            ${totalIllustrated ? `
              <div class="qb-stat-pill">
                <span class="qb-stat-num">${utils.toEasternDigits(totalIllustrated)}</span>
                <span class="qb-stat-lbl">أسئلة مصورة</span>
              </div>
            ` : ''}
            <div class="qb-stat-pill accent">
              <span class="qb-stat-num">${utils.toEasternDigits(selectedCount)}</span>
              <span class="qb-stat-lbl">محدد للنسخ</span>
            </div>
          </div>
        </div>

        <!-- شريط تمييز حالة العضوية في بنك الأسئلة -->
        ${isUserApproved() ? `
          <div class="qb-tier-banner approved">
            <div class="qb-tier-icon">🌟</div>
            <div class="qb-tier-info">
              <strong>عضوية معتمدة رسمياً (كامل الصلاحيات) ✓</strong>
              <span>وصول كامل وتصفح شامل لبنك الأسئلة مع إمكانية إضافة وتوليد الأسئلة وتصديرها بصيغة Word بلا أي قيود.</span>
            </div>
            <span class="qb-tier-tag approved">وصول غير محدود ∞</span>
          </div>
        ` : `
          <div class="qb-tier-banner preview">
            <div class="qb-tier-icon">🔒</div>
            <div class="qb-tier-info">
              <strong>نسخة المعاينة المجانية (محدد بـ ٥ أسئلة كحد أقصى لكل نوع)</strong>
              <span>يمكنك استعراض الأسئلة وإضافة حتى ٥ أسئلة فقط من كل نوع لمنشئ الاختبارات. لفتح البنك بالكامل، يُرجى طلب الاعتماد.</span>
            </div>
            <button type="button" class="qb-tier-btn" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()">
              طلب الاعتماد الكامل ↗
            </button>
          </div>
        `}

        <!-- شريط التصفية والبحث -->
        <div class="qb-filter-card">
          <div class="qb-filter-grid">
            <div class="qb-filter-field">
              <label for="qb-filter-chapter">الفصل (الوحدة):</label>
              <select id="qb-filter-chapter" onchange="window.QuestionBank.setFilter('chapterId', this.value)">
                <option value="all" ${state.chapterId === 'all' ? 'selected' : ''}>جميع الفصول (${utils.toEasternDigits(chapters.length)} فصول)</option>
                ${chapters.map(function (ch) {
                  return '<option value="' + utils.escapeHtml(ch.id) + '"' + (state.chapterId === ch.id ? ' selected' : '') + '>' +
                    utils.escapeHtml(utils.toEasternDigits(ch.number + ': ' + ch.title)) + '</option>';
                }).join('')}
              </select>
            </div>

            <div class="qb-filter-field">
              <label for="qb-filter-lesson">الدرس:</label>
              <select id="qb-filter-lesson" onchange="window.QuestionBank.setFilter('lessonId', this.value)">
                <option value="all" ${state.lessonId === 'all' ? 'selected' : ''}>جميع الدروس (${utils.toEasternDigits(availableLessons.length)})</option>
                ${availableLessons.map(function (ls) {
                  return '<option value="' + utils.escapeHtml(ls.id) + '"' + (state.lessonId === ls.id ? ' selected' : '') + '>' +
                    utils.escapeHtml(utils.toEasternDigits(ls.number + ' ' + ls.title)) + '</option>';
                }).join('')}
              </select>
            </div>

            <div class="qb-filter-field">
              <label for="qb-filter-type">نوع السؤال:</label>
              <select id="qb-filter-type" onchange="window.QuestionBank.setFilter('type', this.value)">
                <option value="all" ${state.type === 'all' ? 'selected' : ''}>جميع الأنواع</option>
                <option value="mcq" ${state.type === 'mcq' ? 'selected' : ''}>اختيار من متعدد</option>
                <option value="tf" ${state.type === 'tf' ? 'selected' : ''}>صواب وخطأ</option>
                <option value="essay" ${state.type === 'essay' ? 'selected' : ''}>مسألة مقالية</option>
              </select>
            </div>

            <div class="qb-filter-field">
              <label for="qb-filter-diff">مستوى الصعوبة:</label>
              <select id="qb-filter-diff" onchange="window.QuestionBank.setFilter('difficulty', this.value)">
                <option value="all" ${state.difficulty === 'all' ? 'selected' : ''}>جميع المستويات</option>
                <option value="سهل" ${state.difficulty === 'سهل' ? 'selected' : ''}>سهل</option>
                <option value="متوسط" ${state.difficulty === 'متوسط' ? 'selected' : ''}>متوسط</option>
                <option value="تحدٍّ" ${state.difficulty === 'تحدٍّ' ? 'selected' : ''}>تحدٍّ</option>
              </select>
            </div>

            <div class="qb-filter-field qb-search-field">
              <label for="qb-filter-search">بحث في نص السؤال أو الإجابة:</label>
              <input id="qb-filter-search" type="text" value="${utils.escapeHtml(state.search)}"
                placeholder="اكتب كلمة مفتاحية أو عدداً (مثال: القاسم، كسر، ٢٥)..."
                oninput="window.QuestionBank.setSearch(this.value)">
            </div>
          </div>

          <div class="qb-filter-footer">
            <span class="qb-result-count">
              ${isUserApproved() ? `
                عرض <strong>${utils.toEasternDigits(filtered.length)}</strong> سؤال من أصل <strong>${utils.toEasternDigits(bank.length)}</strong>
                • صفحة <strong>${utils.toEasternDigits(state.page)}</strong> من <strong>${utils.toEasternDigits(totalPages)}</strong>
              ` : `
                🔒 وضع المعاينة: تم حصر العرض في <strong>${utils.toEasternDigits(filtered.length)}</strong> أسئلة (٥ أسئلة للنوع كحد أقصى) • باقي بنك الأسئلة (${utils.toEasternDigits(bank.length)} سؤالاً) مخصص للأعضاء المعتمدين
              `}
            </span>
            <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
              ${totalIllustrated ? `
                <label class="qb-checkbox-toggle">
                  <input type="checkbox" ${state.onlyImages ? 'checked' : ''}
                    onchange="window.QuestionBank.toggleOnlyImages(this.checked)">
                  <span>📷 الأسئلة المصورة فقط (${utils.toEasternDigits(totalIllustrated)})</span>
                </label>
              ` : ''}
              <button class="nav-btn" type="button" onclick="window.QuestionBank.resetFilters()">🔄 إعادة ضبط التصفية</button>
            </div>
          </div>
        </div>

        <!-- شريط الإجراءات الجماعية والنسخ إلى Word -->
        <div class="qb-bulk-bar">
          <div class="qb-bulk-left">
            <button class="nav-btn" type="button" onclick="window.QuestionBank.selectAllOnPage()">☑️ تحديد الكل في هذه الصفحة</button>
            <button class="nav-btn" type="button" onclick="window.QuestionBank.clearSelection()">✖️ إلغاء التحديد (${utils.toEasternDigits(selectedCount)})</button>
            <label class="qb-checkbox-toggle">
              <input type="checkbox" ${state.includeAnswersOnCopy ? 'checked' : ''}
                onchange="window.QuestionBank.toggleIncludeAnswers(this.checked)">
              <span>تضمين الإجابة النموذجية عند النسخ لـ Word</span>
            </label>
          </div>
          <div class="qb-bulk-right">
            <button class="nav-btn primary" type="button" onclick="window.QuestionBank.copySelectedToWord()">
              📋 نسخ الأسئلة المحددة لـ Word (${utils.toEasternDigits(selectedCount)})
            </button>
            <button class="nav-btn success-btn" type="button" onclick="window.QuestionBank.addSelectedToExam()">
              ➕ إضافة المحددة لمنشئ الاختبارات
            </button>
          </div>
        </div>

        <!-- قائمة الأسئلة -->
        <div class="qb-questions-list">
          ${(() => {
            if (!pageItems.length) {
              return `
                <div class="objectives-card" style="text-align:center; padding:40px;">
                  <h3>لا توجد أسئلة مطابقة لمعايير التصفية الحالية</h3>
                  <p style="color:var(--text-muted); margin:8px 0 16px 0;">جرّب مسح نص البحث أو اختيار «جميع الفصول والدروس».</p>
                  <button class="nav-btn primary" type="button" onclick="window.QuestionBank.resetFilters()">عرض جميع الأسئلة</button>
                </div>
              `;
            }
            const approved = isUserApproved();
            const visitorTypeCounts = { mcq: 0, tf: 0, essay: 0 };

            return pageItems.map(function (q, i) {
              let displayNum;
              if (approved) {
                displayNum = utils.toEasternDigits(startIdx + i + 1);
              } else {
                const t = q.type || 'mcq';
                visitorTypeCounts[t] = (visitorTypeCounts[t] || 0) + 1;
                displayNum = utils.toEasternDigits(visitorTypeCounts[t]);
              }
              const isSelected = state.selectedUids.has(q.uid);
              const isRevealed = state.revealedAnswers.has(q.uid);
              const inExam = examApi && examApi.hasQuestion(q.uid);
              const typeBadgeClass = q.type === 'mcq' ? 'type-mcq' : (q.type === 'tf' ? 'type-tf' : 'type-essay');
              const diffBadgeClass = q.difficulty === 'سهل' ? 'diff-easy' : (q.difficulty === 'متوسط' ? 'diff-med' : 'diff-hard');

              let bodyHtml = '';
              let answerDetailHtml = '';

              if (q.type === 'mcq') {
                bodyHtml = '<div class="qb-mcq-options">' + q.options.map(function (opt, oIdx) {
                  const letter = utils.CHOICE_LETTERS[oIdx] || 'أ';
                  const isCorrectOpt = isRevealed && oIdx === q.correct;
                  return (
                    '<div class="qb-mcq-opt ' + (isCorrectOpt ? 'is-correct' : '') + '">' +
                    '<span class="opt-letter">' + letter + '</span>' +
                    '<span>' + utils.renderMathHtml(opt) + '</span>' +
                    '</div>'
                  );
                }).join('') + '</div>';

                const corrLetter = utils.CHOICE_LETTERS[q.correct] || 'أ';
                answerDetailHtml =
                  '<strong>الإجابة الصحيحة:</strong> ' + corrLetter + ') ' +
                  utils.renderMathHtml(q.options[q.correct] || '') +
                  (q.explanation ? '<br><strong>التفسير:</strong> ' + utils.renderMathHtml(q.explanation) : '');
              } else if (q.type === 'tf') {
                bodyHtml =
                  '<div class="qb-tf-preview">' +
                  '<span class="qb-tf-chip ' + (isRevealed && q.is_true ? 'is-correct' : '') + '">( &nbsp; ) صواب</span>' +
                  '<span class="qb-tf-chip ' + (isRevealed && !q.is_true ? 'is-correct' : '') + '">( &nbsp; ) خطأ</span>' +
                  '</div>';

                answerDetailHtml =
                  '<strong>الإجابة الصحيحة:</strong> ' + (q.is_true ? 'صواب (✓)' : 'خطأ (✗)') +
                  (q.explanation ? '<br><strong>التفسير:</strong> ' + utils.renderMathHtml(q.explanation) : '');
              } else {
                bodyHtml = '<div class="qb-essay-hint">✍️ مسألة تطبيقية مفتوحة (' + utils.toEasternDigits(q.lines || 3) + ' أسطر للإجابة)</div>';
                answerDetailHtml = '<strong>الحل النموذجي:</strong> ' + utils.renderMathHtml(q.ans || '');
              }

              return `
                <div class="qb-question-card ${isSelected ? 'selected' : ''}">
                  <div class="qb-q-top">
                    <label class="qb-q-select-label">
                      <input type="checkbox" ${isSelected ? 'checked' : ''}
                        onchange="window.QuestionBank.toggleSelect('${utils.escapeHtml(q.uid)}', this.checked)">
                      <span class="q-badge">س ${displayNum}</span>
                    </label>
                    <div class="qb-q-badges">
                      <span class="qb-pill chapter-pill">${utils.escapeHtml(utils.toEasternDigits(q.chapterNumber))} • ${utils.escapeHtml(utils.toEasternDigits(q.lessonNumber + ' ' + q.lessonTitle))}</span>
                      <span class="qb-pill ${typeBadgeClass}">${utils.escapeHtml(q.typeLabel)}</span>
                      ${q.image ? '<span class="qb-pill" style="background:#e0f2fe;color:#0369a1;">🖼️ مصور</span>' : ''}
                      <span class="qb-pill ${diffBadgeClass}">${utils.escapeHtml(q.difficulty)}</span>
                      <span class="qb-pill marks-pill">${utils.escapeHtml(utils.formatMark(q.marks))}</span>
                    </div>
                  </div>

                  <div class="qb-q-text">${utils.renderMathHtml(q.q)}</div>
                  ${q.image ? (
                    '<div class="q-figure-box">' +
                    '<img class="q-figure-img" src="' + utils.escapeHtml(q.image) + '" alt="' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption || 'شكل السؤال')) + '" loading="lazy" title="اضغط للتكبير" data-caption="' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption || '')) + '" onclick="if(window.Platform&&window.Platform.openImageLightbox){window.Platform.openImageLightbox(this.getAttribute(\'src\'),this.getAttribute(\'data-caption\'));}" />' +
                    (q.imageCaption ? '<div class="q-figure-caption">' + utils.escapeHtml(utils.toEasternDigits(q.imageCaption)) + '</div>' : '') +
                    '</div>'
                  ) : ''}
                  ${bodyHtml}

                  ${isRevealed ? '<div class="qb-answer-box">' + answerDetailHtml + '</div>' : ''}

                  <div class="qb-q-actions">
                    <button type="button" class="qb-act-btn" onclick="window.QuestionBank.toggleRevealAnswer('${utils.escapeHtml(q.uid)}')">
                      ${isRevealed ? '🙈 إخفاء الإجابة' : '💡 إظهار الإجابة النموذجية'}
                    </button>
                    <div class="qb-q-actions-left">
                      <button type="button" class="qb-act-btn copy-word-btn" onclick="window.QuestionBank.copySingleToWord('${utils.escapeHtml(q.uid)}')">
                        📋 نسخ السؤال لـ Word
                      </button>
                      <button type="button" class="qb-act-btn add-exam-btn ${inExam ? 'added' : ''}" onclick="window.QuestionBank.toggleExamQuestion('${utils.escapeHtml(q.uid)}')">
                        ${inExam ? '✓ مضاف للاختبار (إزالة)' : '➕ أضف للاختبار'}
                      </button>
                    </div>
                  </div>
                </div>
              `;
            }).join('');
          })()}
        </div>

        ${!isUserApproved() ? `
          <div class="qb-locked-gate-banner" style="margin:20px 0; background:linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%); border:2px dashed #f59e0b; border-radius:12px; padding:20px 24px; display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap;">
            <div style="display:flex; align-items:center; gap:14px;">
              <span style="font-size:2rem;">🔒</span>
              <div>
                <h4 style="margin:0 0 4px 0; font-size:1.05rem; font-weight:800; color:#92400e;">تم إيقاف العرض عند الحد المسموح به للمعاينة (٥ أسئلة لكل نوع)</h4>
                <p style="margin:0; font-size:0.88rem; color:#78350f;">
                  لبقية أسئلة بنك الأسئلة الشامل (أكثر من ٤٥٠ سؤالاً لكل صف دراسي) وميزات النسخ الكامل لـ Word والتوليد الشامل للاختبارات، سجّل دخولك واطلب اعتماد حسابك.
                </p>
              </div>
            </div>
            <button type="button" class="nav-btn primary" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()" style="font-weight:700;">
              🔑 تسجيل الدخول وطلب الاعتماد ↗
            </button>
          </div>
        ` : ''}

        <!-- الترقيم والتنقل بين الصفحات -->
        ${renderPagination(totalPages)}
      </div>
    `;

    state.container.innerHTML = html;

    // استعادة تركيز خانة البحث إذا كان المستخدم يكتب فيها
    const searchEl = document.getElementById('qb-filter-search');
    if (searchEl && state._keepSearchFocus) {
      searchEl.focus();
      const len = searchEl.value.length;
      searchEl.setSelectionRange(len, len);
      state._keepSearchFocus = false;
    }
  }

  function renderPagination(totalPages) {
    if (totalPages <= 1) return '';
    const utils = getUtils();
    let pagesHtml = '';
    const maxButtons = 7;
    let startP = Math.max(1, state.page - 3);
    let endP = Math.min(totalPages, startP + maxButtons - 1);
    if (endP - startP + 1 < maxButtons) {
      startP = Math.max(1, endP - maxButtons + 1);
    }

    for (let p = startP; p <= endP; p++) {
      pagesHtml += '<button type="button" class="qb-page-btn ' + (p === state.page ? 'active' : '') +
        '" onclick="window.QuestionBank.goToPage(' + p + ')">' + utils.toEasternDigits(p) + '</button>';
    }

    return `
      <div class="qb-pagination">
        <button type="button" class="qb-page-btn" ${state.page <= 1 ? 'disabled' : ''}
          onclick="window.QuestionBank.goToPage(${state.page - 1})">◀ السابق</button>
        ${pagesHtml}
        <button type="button" class="qb-page-btn" ${state.page >= totalPages ? 'disabled' : ''}
          onclick="window.QuestionBank.goToPage(${state.page + 1})">التالي ▶</button>
      </div>
    `;
  }

  function setBook(bookId) {
    if (!BOOKS_CONFIG[bookId] || state.bookId === bookId) return;
    state.bookId = bookId;
    state.chapterId = 'all';
    state.lessonId = 'all';
    state.onlyImages = false;
    state.page = 1;
    state.selectedUids.clear();
    render();
  }

  function toggleOnlyImages(checked) {
    state.onlyImages = !!checked;
    state.page = 1;
    render();
  }

  function setFilter(key, val) {
    state[key] = val;
    if (key === 'chapterId') {
      state.lessonId = 'all';
    }
    state.page = 1;
    render();
  }

  function setSearch(val) {
    state.search = val;
    state.page = 1;
    state._keepSearchFocus = true;
    render();
  }

  function resetFilters() {
    state.chapterId = 'all';
    state.lessonId = 'all';
    state.type = 'all';
    state.difficulty = 'all';
    state.onlyImages = false;
    state.search = '';
    state.page = 1;
    render();
  }

  function goToPage(p) {
    state.page = p;
    render();
    if (state.container) state.container.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function toggleSelect(uid, checked) {
    if (checked) state.selectedUids.add(uid);
    else state.selectedUids.delete(uid);
    render();
  }

  function selectAllOnPage() {
    const filtered = getFilteredQuestions();
    const startIdx = (state.page - 1) * PAGE_SIZE;
    const pageItems = filtered.slice(startIdx, startIdx + PAGE_SIZE);
    pageItems.forEach(function (q) {
      state.selectedUids.add(q.uid);
    });
    render();
  }

  function clearSelection() {
    state.selectedUids.clear();
    render();
  }

  function toggleIncludeAnswers(checked) {
    state.includeAnswersOnCopy = !!checked;
  }

  function toggleRevealAnswer(uid) {
    if (state.revealedAnswers.has(uid)) state.revealedAnswers.delete(uid);
    else state.revealedAnswers.add(uid);
    render();
  }

  function copySingleToWord(uid) {
    const q = getQuestionByUid(uid);
    if (!q) return;
    getUtils().copyQuestionsToWord([q], {
      includeAnswers: state.includeAnswersOnCopy,
      numbered: false
    });
  }

  function copySelectedToWord() {
    const selected = getSelectedQuestionObjects();
    if (!selected.length) {
      getUtils().showToast('يرجى تحديد سؤال واحد على الأقل للنسخ إلى Word.', 'warning');
      return;
    }
    const approved = isUserApproved();
    if (!approved) {
      const counts = { mcq: 0, tf: 0, essay: 0 };
      const safeList = [];
      let hadExcess = false;
      selected.forEach(function (q) {
        const t = q.type || 'mcq';
        if ((counts[t] || 0) < 5) {
          counts[t] = (counts[t] || 0) + 1;
          safeList.push(q);
        } else {
          hadExcess = true;
        }
      });
      if (hadExcess) {
        getUtils().showToast('🔒 تم تقييد النسخ إلى ٥ أسئلة كحد أقصى لكل نوع لغير الأعضاء المعتمدين.', 'warning');
      }
      getUtils().copyQuestionsToWord(safeList, {
        includeAnswers: state.includeAnswersOnCopy,
        numbered: true
      });
      return;
    }
    getUtils().copyQuestionsToWord(selected, {
      includeAnswers: state.includeAnswersOnCopy,
      numbered: true
    });
  }

  function toggleExamQuestion(uid) {
    const q = getQuestionByUid(uid);
    if (!q || !global.ExamBuilder) return;
    if (global.ExamBuilder.hasQuestion(uid)) {
      global.ExamBuilder.removeQuestion(uid);
      getUtils().showToast('تمت إزالة السؤال من منشئ الاختبارات.', 'info');
    } else {
      global.ExamBuilder.addQuestion(q);
    }
    render();
  }

  function addSelectedToExam() {
    const selected = getSelectedQuestionObjects();
    if (!selected.length) {
      getUtils().showToast('يرجى تحديد سؤال واحد على الأقل لإضافته للاختبار.', 'warning');
      return;
    }
    if (global.ExamBuilder) {
      global.ExamBuilder.addQuestions(selected);
      render();
    }
  }

  global.QuestionBank = {
    render: render,
    setBook: setBook,
    getBookData: getBookData,
    isUserApproved: isUserApproved,
    toggleOnlyImages: toggleOnlyImages,
    setFilter: setFilter,
    setSearch: setSearch,
    resetFilters: resetFilters,
    goToPage: goToPage,
    toggleSelect: toggleSelect,
    selectAllOnPage: selectAllOnPage,
    clearSelection: clearSelection,
    toggleIncludeAnswers: toggleIncludeAnswers,
    toggleRevealAnswer: toggleRevealAnswer,
    copySingleToWord: copySingleToWord,
    copySelectedToWord: copySelectedToWord,
    toggleExamQuestion: toggleExamQuestion,
    addSelectedToExam: addSelectedToExam
  };
})(typeof window !== 'undefined' ? window : globalThis);
