/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * Core Web Platform Controller & Interactive Logic
 * ==========================================================================
 */

(function () {
  'use strict';

  // Global State
  const state = {
    currentLessonId: 'g6-t1-c1-l1',
    activeView: 'cockpit', // 'cockpit' | 'question-bank' | 'exam-builder' | 'visual-tree' | 'suites' | 'vault' | 'builder'
    activeLessonTab: 'prep', // 'prep' | 'summary' | 'worksheet' | 'socratic' | 'tools' | 'quiz' | 'downloads'
    termFilter: 'all',
    searchQuery: '',
    quizScores: {}, // lessonId -> { answeredCount, correctCount, userAnswers: {} }
    expandedNodes: new Set(['elementary', 'g6', 'g6-term1', 'g6-t1-c1', 'intermediate', 'g1m', 'g1m-term1', 'g1m-t1-c1', 'g3m', 'g3m-term1', 'secondary', 'g1s', 'g1s-term1', 'g2s', 'g2s-term1', 'g3s', 'g3s-term1'])
  };

  function isCurrentSecondary() {
    if (state.currentLessonId && (state.currentLessonId.startsWith('g1s') || state.currentLessonId.startsWith('g2s') || state.currentLessonId.startsWith('g3s'))) return true;
    if (window.QuestionBank && window.QuestionBank.getCurrentBookId && (window.QuestionBank.getCurrentBookId() === 'g1s' || window.QuestionBank.getCurrentBookId() === 'g2s' || window.QuestionBank.getCurrentBookId() === 'g3s')) return true;
    if (window.ExamBuilder && window.ExamBuilder.getCurrentBookId && (window.ExamBuilder.getCurrentBookId() === 'g1s' || window.ExamBuilder.getCurrentBookId() === 'g2s' || window.ExamBuilder.getCurrentBookId() === 'g3s')) return true;
    return false;
  }

  function fmtNum(val, forceEastern) {
    if (window.ArabicUtils) {
      if (isCurrentSecondary()) {
        if (typeof val === 'string' && (val.indexOf('$') !== -1 || val.indexOf('sec-math') !== -1 || val.indexOf('ltr-math') !== -1 || val.indexOf('sec-pow') !== -1 || val.indexOf('^') !== -1)) {
          return window.ArabicUtils.renderMathHtml(val, true);
        }
        return window.ArabicUtils.toWesternDigits ? window.ArabicUtils.toWesternDigits(val) : String(val);
      }
      if (typeof val === 'string' && (val.indexOf('ar-pow') !== -1 || val.indexOf('^') !== -1 || val.indexOf('sec-pow') !== -1)) {
        return window.ArabicUtils.renderMathHtml(val, false);
      }
      if (forceEastern !== false) {
        return window.ArabicUtils.toEasternDigits(val);
      }
    }
    return String(val);
  }

  function escHtml(str) {
    if (window.ArabicUtils && window.ArabicUtils.escapeHtml) {
      return window.ArabicUtils.escapeHtml(str || '');
    }
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function isFullBookLesson(lesson) {
    return !!(lesson && lesson.id && (lesson.id.startsWith('g6') || lesson.id.startsWith('g1m') || lesson.id.startsWith('g3m') || lesson.id.startsWith('g1s') || lesson.id.startsWith('g2s') || lesson.id.startsWith('g3s')));
  }

  function mergeBookData() {
    if (!window.CURRICULUM_DATA || !window.CURRICULUM_DATA.lessons) return;
    if (window.GRADE6_BOOK_DATA && window.GRADE6_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE6_BOOK_DATA.lessons);
    }
    if (window.GRADE1M_BOOK_DATA && window.GRADE1M_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE1M_BOOK_DATA.lessons);
    }
    if (window.GRADE3M_BOOK_DATA && window.GRADE3M_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE3M_BOOK_DATA.lessons);
    }
    if (window.GRADE1S_BOOK_DATA && window.GRADE1S_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE1S_BOOK_DATA.lessons);

      // Dynamically sync and rebuild the Secondary tree structure in stages from GRADE1S_BOOK_DATA
      if (window.CURRICULUM_DATA.stages && window.GRADE1S_BOOK_DATA.chapters) {
        const secStage = window.CURRICULUM_DATA.stages.find(s => s.id === 'secondary');
        if (secStage && secStage.grades) {
          const g1s = secStage.grades.find(g => g.id === 'g1s');
          if (g1s && g1s.terms) {
            g1s.badge = window.GRADE1S_BOOK_DATA.bookMeta ? window.GRADE1S_BOOK_DATA.bookMeta.badge : 'مكتمل 100% (4 فصول • 27 درساً)';
            const t1 = g1s.terms.find(t => t.id === 'term1');
            if (t1) {
              t1.chapters = window.GRADE1S_BOOK_DATA.chapters.map(ch => ({
                id: ch.id,
                number: ch.number,
                title: ch.title,
                pages: ch.pages || '',
                lessons_count: (ch.lessons || []).length,
                status: 'completed',
                badge: ch.badge || 'مكتمل بالكامل',
                lessons: (ch.lessons || []).map(l => {
                  const fullL = (window.GRADE1S_BOOK_DATA.lessons && window.GRADE1S_BOOK_DATA.lessons[l.id]) || {};
                  return {
                    id: l.id,
                    number: l.number || fullL.number || '',
                    title: fullL.title || l.title || '',
                    pages: fullL.pages || l.pages || '',
                    status: 'completed'
                  };
                })
              }));
            }
          }
        }
      }
    }
    if (window.GRADE2S_BOOK_DATA && window.GRADE2S_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE2S_BOOK_DATA.lessons);

      // Dynamically sync and rebuild the Secondary tree structure in stages from GRADE2S_BOOK_DATA
      if (window.CURRICULUM_DATA.stages && window.GRADE2S_BOOK_DATA.chapters) {
        const secStage = window.CURRICULUM_DATA.stages.find(s => s.id === 'secondary');
        if (secStage && secStage.grades) {
          const g2s = secStage.grades.find(g => g.id === 'g2s');
          if (g2s && g2s.terms) {
            g2s.badge = window.GRADE2S_BOOK_DATA.bookMeta ? window.GRADE2S_BOOK_DATA.bookMeta.badge : 'مكتمل 100% (4 فصول • 26 درساً)';
            const t1 = g2s.terms.find(t => t.id === 'term1');
            if (t1) {
              t1.chapters = window.GRADE2S_BOOK_DATA.chapters.map(ch => ({
                id: ch.id,
                number: ch.number,
                title: ch.title,
                pages: ch.pages || '',
                lessons_count: (ch.lessons || []).length,
                status: 'completed',
                badge: ch.badge || 'مكتمل بالكامل',
                lessons: (ch.lessons || []).map(l => {
                  const fullL = (window.GRADE2S_BOOK_DATA.lessons && window.GRADE2S_BOOK_DATA.lessons[l.id]) || {};
                  return {
                    id: l.id,
                    number: l.number || fullL.number || '',
                    title: fullL.title || l.title || '',
                    pages: fullL.pages || l.pages || '',
                    status: 'completed'
                  };
                })
              }));
            }
          }
        }
      }
    }
    if (window.GRADE3S_BOOK_DATA && window.GRADE3S_BOOK_DATA.lessons) {
      Object.assign(window.CURRICULUM_DATA.lessons, window.GRADE3S_BOOK_DATA.lessons);

      // Dynamically sync and rebuild the Secondary tree structure in stages from GRADE3S_BOOK_DATA
      if (window.CURRICULUM_DATA.stages && window.GRADE3S_BOOK_DATA.chapters) {
        const secStage = window.CURRICULUM_DATA.stages.find(s => s.id === 'secondary');
        if (secStage && secStage.grades) {
          const g3s = secStage.grades.find(g => g.id === 'g3s');
          if (g3s && g3s.terms) {
            g3s.badge = window.GRADE3S_BOOK_DATA.bookMeta ? window.GRADE3S_BOOK_DATA.bookMeta.badge : 'مكتمل 100% (4 فصول • 22 درساً)';
            const t1 = g3s.terms.find(t => t.id === 'term1');
            if (t1) {
              t1.chapters = window.GRADE3S_BOOK_DATA.chapters.map(ch => ({
                id: ch.id,
                number: ch.number,
                title: ch.title,
                pages: ch.pages || '',
                lessons_count: (ch.lessons || []).length,
                status: 'completed',
                badge: ch.badge || 'مكتمل بالكامل',
                lessons: (ch.lessons || []).map(l => {
                  const fullL = (window.GRADE3S_BOOK_DATA.lessons && window.GRADE3S_BOOK_DATA.lessons[l.id]) || {};
                  return {
                    id: l.id,
                    number: l.number || fullL.number || '',
                    title: fullL.title || l.title || '',
                    pages: fullL.pages || l.pages || '',
                    status: 'completed'
                  };
                })
              }));
            }
          }
        }
      }
    }
  }

  function openImageLightbox(src, caption) {
    if (!src) return;
    let lb = document.getElementById('raed-lightbox');
    if (!lb) {
      lb = document.createElement('div');
      lb.id = 'raed-lightbox';
      lb.className = 'raed-lightbox';
      lb.innerHTML =
        '<div class="raed-lightbox-dialog" onclick="event.stopPropagation()">' +
          '<button type="button" class="raed-lightbox-close" onclick="window.Platform.closeImageLightbox()" aria-label="إغلاق">✖️</button>' +
          '<img id="raed-lightbox-img" src="" alt="شكل تعليمي" />' +
          '<div id="raed-lightbox-cap" class="raed-lightbox-cap"></div>' +
        '</div>';
      lb.addEventListener('click', closeImageLightbox);
      document.body.appendChild(lb);
    }
    const imgEl = document.getElementById('raed-lightbox-img');
    const capEl = document.getElementById('raed-lightbox-cap');
    if (imgEl) imgEl.src = src;
    if (capEl) {
      capEl.textContent = caption ? fmtNum(caption, true) : '';
      capEl.style.display = caption ? 'block' : 'none';
    }
    lb.classList.add('open');
  }

  function closeImageLightbox() {
    const lb = document.getElementById('raed-lightbox');
    if (lb) lb.classList.remove('open');
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeImageLightbox();
    });
  }

  function renderQuestionFigure(item) {
    const imgSrc = item && (item.image || item.fig);
    if (!imgSrc) return '';
    const cap = item.imageCaption ? fmtNum(item.imageCaption, true) : '';
    const altText = cap || 'شكل توضيحي للسؤال';
    return `
      <div class="q-figure-box">
        <img
          class="q-figure-img"
          src="${escHtml(imgSrc)}"
          alt="${escHtml(altText)}"
          loading="lazy"
          title="اضغط للتكبير"
          onclick="window.Platform.openImageLightbox(this.getAttribute('src'), this.getAttribute('data-caption'))"
          data-caption="${escHtml(cap)}"
        />
        ${cap ? `<div class="q-figure-caption">${escHtml(cap)}</div>` : ''}
      </div>
    `;
  }

  // DOM Elements
  let sidebarTreeContainer;
  let viewportArea;
  let searchInput;

  // Initialize
  window.addEventListener('DOMContentLoaded', () => {
    sidebarTreeContainer = document.getElementById('sidebar-tree');
    viewportArea = document.getElementById('app-viewport');
    searchInput = document.getElementById('nav-search');

    function startPlatform() {
      if (!window.CURRICULUM_DATA) {
        setTimeout(startPlatform, 50);
        return;
      }
      mergeBookData();
      if (window.ExamBuilder && window.ExamBuilder.updateBadge) {
        window.ExamBuilder.updateBadge();
      }

      if (window.FirebaseAuthManager) {
        window.FirebaseAuthManager.onAuthStateChanged(() => {
          renderTree();
          renderCurrentView();
        });
      }

      setupEventListeners();
      renderTree();
      renderCurrentView();
    }

    startPlatform();
  });

  // Event Listeners
  function setupEventListeners() {
    // Term filter tabs
    document.querySelectorAll('.term-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.term-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.termFilter = btn.dataset.term;
        renderTree();
        if (state.activeView === 'visual-tree') renderVisualTree();
      });
    });

    // Search input & Ctrl+K shortcut
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value.trim().toLowerCase();
        renderTree();
      });
    }

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (searchInput) {
          searchInput.focus();
          searchInput.select();
        }
      }
    });

    // View switcher tabs
    document.querySelectorAll('.view-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.view-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.activeView = btn.dataset.view;
        renderCurrentView();
      });
    });

    // Dark Mode Toggle
    const themeBtn = document.getElementById('btn-theme-toggle');
    function updateThemeBtn(isDark) {
      if (!themeBtn) return;
      if (isDark) {
        themeBtn.innerHTML = `
          <span class="nav-chip-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="5"></circle>
              <line x1="12" y1="1" x2="12" y2="3"></line>
              <line x1="12" y1="21" x2="12" y2="23"></line>
              <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
              <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
              <line x1="1" y1="12" x2="3" y2="12"></line>
              <line x1="21" y1="12" x2="23" y2="12"></line>
              <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
              <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
            </svg>
          </span>
          <span class="nav-chip-label">الوضع النهاري</span>
        `;
      } else {
        themeBtn.innerHTML = `
          <span class="nav-chip-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
            </svg>
          </span>
          <span class="nav-chip-label">الوضع الليلي</span>
        `;
      }
    }
    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {
          document.body.removeAttribute('data-theme');
          updateThemeBtn(false);
        } else {
          document.body.setAttribute('data-theme', 'dark');
          updateThemeBtn(true);
        }
      });
    }

    // Close crumb dropdowns when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.tree-crumb-item')) {
        document.querySelectorAll('.crumb-dropdown.open').forEach(el => el.classList.remove('open'));
        document.querySelectorAll('.tree-crumb-item.active-menu').forEach(el => el.classList.remove('active-menu'));
      }
    });
  }

  // Find ancestor IDs for a lesson: [stage, grade, term, termKey, chapter, lesson]
  function findLessonPath(lessonId) {
    if (!window.CURRICULUM_DATA || !window.CURRICULUM_DATA.stages) return null;
    for (const stage of window.CURRICULUM_DATA.stages) {
      for (const grade of stage.grades) {
        for (const term of grade.terms) {
          const termKey = grade.id + '-' + term.id;
          for (const chapter of (term.chapters || [])) {
            for (const l of (chapter.lessons || [])) {
              if (l.id === lessonId) {
                return {
                  stage,
                  grade,
                  term,
                  termKey,
                  chapter,
                  lesson: l
                };
              }
            }
          }
        }
      }
    }
    return null;
  }

  function getAllLessonsList() {
    const list = [];
    if (!window.CURRICULUM_DATA || !window.CURRICULUM_DATA.stages) return list;
    window.CURRICULUM_DATA.stages.forEach(stage => {
      stage.grades.forEach(grade => {
        grade.terms.forEach(term => {
          (term.chapters || []).forEach(ch => {
            (ch.lessons || []).forEach(l => {
              list.push({
                id: l.id,
                title: l.title,
                number: l.number,
                chapterId: ch.id,
                chapterTitle: ch.title,
                chapterNumber: ch.number,
                termId: term.id,
                gradeId: grade.id,
                stageId: stage.id
              });
            });
          });
        });
      });
    });
    return list;
  }

  function goToPrevLesson() {
    const list = getAllLessonsList();
    const idx = list.findIndex(item => item.id === state.currentLessonId);
    if (idx > 0) {
      selectLesson(list[idx - 1].id);
    }
  }

  function goToNextLesson() {
    const list = getAllLessonsList();
    const idx = list.findIndex(item => item.id === state.currentLessonId);
    if (idx >= 0 && idx < list.length - 1) {
      selectLesson(list[idx + 1].id);
    }
  }

  function selectFirstLessonOfStage(stageId) {
    const stages = (window.CURRICULUM_DATA && window.CURRICULUM_DATA.stages) || [];
    const stage = stages.find(s => s.id === stageId);
    if (stage) {
      for (const grade of stage.grades) {
        for (const term of grade.terms) {
          for (const ch of (term.chapters || [])) {
            if (ch.lessons && ch.lessons.length) {
              selectLesson(ch.lessons[0].id);
              return;
            }
          }
        }
      }
    }
  }

  function selectFirstLessonOfGrade(gradeId) {
    const stages = (window.CURRICULUM_DATA && window.CURRICULUM_DATA.stages) || [];
    for (const stage of stages) {
      const grade = stage.grades.find(g => g.id === gradeId);
      if (grade) {
        for (const term of grade.terms) {
          for (const ch of (term.chapters || [])) {
            if (ch.lessons && ch.lessons.length) {
              selectLesson(ch.lessons[0].id);
              return;
            }
          }
        }
      }
    }
  }

  function selectFirstLessonOfTerm(gradeId, termId) {
    const stages = (window.CURRICULUM_DATA && window.CURRICULUM_DATA.stages) || [];
    for (const stage of stages) {
      const grade = stage.grades.find(g => g.id === gradeId);
      if (grade) {
        const term = grade.terms.find(t => t.id === termId);
        if (term) {
          for (const ch of (term.chapters || [])) {
            if (ch.lessons && ch.lessons.length) {
              selectLesson(ch.lessons[0].id);
              return;
            }
          }
        }
      }
    }
  }

  function selectFirstLessonOfChapter(chapterId) {
    const stages = (window.CURRICULUM_DATA && window.CURRICULUM_DATA.stages) || [];
    for (const stage of stages) {
      for (const grade of stage.grades) {
        for (const term of grade.terms) {
          const ch = (term.chapters || []).find(c => c.id === chapterId);
          if (ch && ch.lessons && ch.lessons.length) {
            selectLesson(ch.lessons[0].id);
            return;
          }
        }
      }
    }
  }

  function expandAll() {
    if (!window.CURRICULUM_DATA || !window.CURRICULUM_DATA.stages) return;
    state.expandedNodes.clear();
    window.CURRICULUM_DATA.stages.forEach(stage => {
      state.expandedNodes.add(stage.id);
      (stage.grades || []).forEach(grade => {
        state.expandedNodes.add(grade.id);
        (grade.terms || []).forEach(term => {
          state.expandedNodes.add(grade.id + '-' + term.id);
          (term.chapters || []).forEach(ch => {
            state.expandedNodes.add(ch.id);
          });
        });
      });
    });
    renderTree();
  }

  function collapseAll() {
    state.expandedNodes.clear();
    renderTree();
  }

  function toggleSidebar() {
    const sidebar = document.getElementById('app-sidebar');
    const openPill = document.getElementById('sidebar-open-pill');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (!sidebar) return;

    // Check if mobile viewport
    if (typeof window !== 'undefined' && window.innerWidth <= 860) {
      const isMobileOpen = sidebar.classList.contains('mobile-open');
      if (isMobileOpen) {
        sidebar.classList.remove('mobile-open');
        if (backdrop) backdrop.classList.remove('show');
      } else {
        sidebar.classList.add('mobile-open');
        if (backdrop) backdrop.classList.add('show');
      }
      return;
    }

    sidebar.classList.toggle('collapsed');
    const isCollapsed = sidebar.classList.contains('collapsed');
    if (openPill) {
      openPill.style.display = isCollapsed ? 'inline-flex' : 'none';
    }
  }

  function closeSidebarMobile() {
    const sidebar = document.getElementById('app-sidebar');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (sidebar) sidebar.classList.remove('mobile-open');
    if (backdrop) backdrop.classList.remove('show');
  }

  function toggleMobileNav() {
    const drawer = document.getElementById('mobile-nav-drawer');
    if (drawer) drawer.classList.toggle('open');
  }

  function closeMobileNav() {
    const drawer = document.getElementById('mobile-nav-drawer');
    if (drawer) drawer.classList.remove('open');
  }

  function openCurrentLessonHtmlGenerator() {
    if (window.InteractiveHtmlGenerator) {
      window.InteractiveHtmlGenerator.showGeneratorModal(state.currentLessonId);
    }
  }

  function toggleCrumbDropdown(event, menuId) {
    if (event) event.stopPropagation();
    const targetMenu = document.getElementById(menuId);
    if (!targetMenu) return;
    const isOpen = targetMenu.classList.contains('open');
    document.querySelectorAll('.crumb-dropdown.open').forEach(el => el.classList.remove('open'));
    document.querySelectorAll('.tree-crumb-item.active-menu').forEach(el => el.classList.remove('active-menu'));
    if (!isOpen) {
      targetMenu.classList.add('open');
      const parentCrumb = targetMenu.closest('.tree-crumb-item');
      if (parentCrumb) parentCrumb.classList.add('active-menu');
    }
  }

  // ================= Hierarchical Navigation Rendering =================
  function renderTree() {
    try {
      if (!sidebarTreeContainer) sidebarTreeContainer = document.getElementById('sidebar-tree');
      if (!sidebarTreeContainer) return;
      if (!window.CURRICULUM_DATA) {
        sidebarTreeContainer.innerHTML = `
          <div style="padding:20px 14px; text-align:center; color:#94a3b8; font-size:0.85rem;">
            ⏳ جاري تحميل دليل المناهج...
          </div>
        `;
        setTimeout(() => {
          if (window.CURRICULUM_DATA) renderTree();
        }, 200);
        return;
      }
      const stages = window.CURRICULUM_DATA.stages || [];
      let html = '';

    const isApproved = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isApproved === 'function' && window.FirebaseAuthManager.isApproved();
    const isAdmin = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isAdmin === 'function' && window.FirebaseAuthManager.isAdmin();
    const isPending = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isPending === 'function' && window.FirebaseAuthManager.isPending();
    const currentUser = window.FirebaseAuthManager && (window.FirebaseAuthManager.getCurrentUser ? window.FirebaseAuthManager.getCurrentUser() : (window.FirebaseAuthManager.getUser ? window.FirebaseAuthManager.getUser() : null));

    let membershipCardHtml = '';
    if (isAdmin) {
      membershipCardHtml = `
        <div class="sidebar-member-card admin">
          <div class="smc-header">
            <span class="smc-icon">👑</span>
            <div class="smc-title">المدير العام والمسؤول</div>
            <span class="smc-badge admin">إدارة عليا ✓</span>
          </div>
          <div class="smc-desc">أ. محمد عبدالله جمعة • كامل الصلاحيات وإدارة الحسابات النشطة.</div>
        </div>
      `;
    } else if (isApproved) {
      membershipCardHtml = `
        <div class="sidebar-member-card approved">
          <div class="smc-header">
            <span class="smc-icon">🌟</span>
            <div class="smc-title">عضوية معتمدة رسمياً</div>
            <span class="smc-badge approved">وصول كامل ✓</span>
          </div>
          <div class="smc-desc">مرحباً بك (${escHtml((currentUser && currentUser.displayName) || 'أستاذ')}) • كافة الدروس والتحضيرات وبنك الأسئلة وتصدير Word متاحة بالكامل.</div>
        </div>
      `;
    } else if (isPending) {
      membershipCardHtml = `
        <div class="sidebar-member-card pending">
          <div class="smc-header">
            <span class="smc-icon">⏳</span>
            <div class="smc-title">حساب قيد المراجعة</div>
            <span class="smc-badge pending">بانتظار الاعتماد</span>
          </div>
          <div class="smc-desc">طلبك قيد المراجعة لدى المدير العام. متاح لك أول درسين من كل فصل كمعاينة وتوليد حتى ${fmtNum(5, true)} أسئلة لكل نوع.</div>
        </div>
      `;
    } else {
      membershipCardHtml = `
        <div class="sidebar-member-card visitor" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()" title="انقر لتسجيل الدخول وطلب الاعتماد">
          <div class="smc-header">
            <span class="smc-icon">🔒</span>
            <div class="smc-title">نسخة المعاينة المجانية</div>
            <span class="smc-badge visitor">طلب العضوية ↗</span>
          </div>
          <div class="smc-desc">متاح أول درسين من كل فصل كمعاينة وتوليد حتى ${fmtNum(5, true)} أسئلة للنوع. سجّل واطلب تفعيل العضوية لفتح جميع المناهج المتاحة (ابتدائي، متوسط، ثانوي) وبنك الأسئلة الشامل.</div>
        </div>
      `;
    }

    html += membershipCardHtml;

    stages.forEach(stage => {
      let stageMatches = false;
      let gradesHtml = '';

      stage.grades.forEach(grade => {
        let gradeMatches = false;
        let termsHtml = '';

        grade.terms.forEach(term => {
          if (state.termFilter !== 'all' && term.id !== state.termFilter) return;

          let termMatches = false;
          let chaptersHtml = '';

          (term.chapters || []).forEach(chapter => {
            let chapterMatches = false;
            let lessonsHtml = '';

            (chapter.lessons || []).forEach((lesson, lIdx) => {
              const fullLesson = window.CURRICULUM_DATA.lessons[lesson.id];
              const title = fullLesson ? fullLesson.title : lesson.title;
              const matchesSearch = !state.searchQuery || 
                title.toLowerCase().includes(state.searchQuery) || 
                (fullLesson && fullLesson.objectives && fullLesson.objectives.some(o => o.toLowerCase().includes(state.searchQuery)));

              if (matchesSearch) {
                chapterMatches = true;
                termMatches = true;
                gradeMatches = true;
                stageMatches = true;

                const isCompleted = lesson.status === 'completed' || (fullLesson && fullLesson.status === 'completed');
                const isActive = state.currentLessonId === lesson.id;
                const isUnlocked = window.FirebaseAuthManager ? window.FirebaseAuthManager.isLessonUnlocked(chapter, lIdx) : true;
                const lessonNum = lesson.number || (fullLesson && fullLesson.number) || '';

                lessonsHtml += `
                  <div class="tree-lesson-item ${isActive ? 'active' : ''} ${!isUnlocked ? 'locked-lesson' : ''}" onclick="window.Platform.selectLesson('${lesson.id}')" title="${escHtml(title)}${!isUnlocked ? ' (مخصص للأعضاء المعتمدين - المعاينة لدرسين)' : ''}">
                    <span style="display:flex; align-items:center; gap:5px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                      <span class="lesson-status-dot ${isCompleted ? 'completed' : 'roadmap'}"></span>
                      ${lessonNum ? `<span style="font-weight:700; color:${isActive ? '#ffffff' : (isCompleted ? '#e2e8f0' : '#cbd5e1')}">${escHtml(lessonNum)}</span>` : ''}
                      <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${escHtml(title || '')}</span>
                    </span>
                    <span style="display:flex; align-items:center; gap:4px; flex-shrink:0;">
                      ${isUnlocked ? (isApproved ? '<span class="tree-unlocked-star" title="عضو معتمد: وصول كامل ومفتوح">🌟</span>' : '') : '<span class="tree-lock-badge" title="هذا الدرس متاح للأعضاء المعتمدين والمدير">🔒</span>'}
                      <span style="font-size:0.62rem; color:${isActive ? '#ffffff' : (isCompleted ? '#86efac' : '#fcd34d')};">
                        ${isCompleted ? '✓' : 'قيد الإدراج'}
                      </span>
                    </span>
                  </div>
                `;
              }
            });

            if (chapterMatches || !state.searchQuery) {
              const isChapterOpen = state.expandedNodes.has(chapter.id) || !!state.searchQuery;
              const lessonCount = (chapter.lessons || []).length;
              chaptersHtml += `
                <div class="tree-chapter-node">
                  <div class="tree-chapter-header" onclick="window.Platform.toggleNode('${chapter.id}')">
                    <span style="display:flex; align-items:center; gap:5px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                      <span>📖</span>
                      <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${chapter.number}: ${chapter.title}</span>
                    </span>
                    <div style="display:flex; align-items:center; gap:4px; flex-shrink:0;">
                      <span style="font-size:0.6rem; color:#94a3b8;">(${lessonCount})</span>
                      <span class="node-arrow ${isChapterOpen ? 'open' : ''}">◀</span>
                    </div>
                  </div>
                  <div class="tree-chapter-children" style="display:${isChapterOpen ? 'block' : 'none'};">
                    ${lessonsHtml || '<div style="padding:4px 8px; font-size:0.7rem; color:#64748b;">قيد الإدراج</div>'}
                  </div>
                </div>
              `;
            }
          });

          if (termMatches || !state.searchQuery) {
            const termKey = grade.id + '-' + term.id;
            const isTermOpen = state.expandedNodes.has(termKey) || !!state.searchQuery;
            termsHtml += `
              <div class="tree-term-node">
                <div class="tree-term-header" onclick="window.Platform.toggleNode('${termKey}')">
                  <span>${term.icon || '📅'} ${term.name}</span>
                  <span class="node-arrow ${isTermOpen ? 'open' : ''}">◀</span>
                </div>
                <div class="tree-term-children" style="display:${isTermOpen ? 'block' : 'none'};">
                  ${chaptersHtml}
                </div>
              </div>
            `;
          }
        });

        if (gradeMatches || !state.searchQuery) {
          const isGradeOpen = state.expandedNodes.has(grade.id) || !!state.searchQuery;
          gradesHtml += `
            <div class="tree-grade-node">
              <div class="tree-grade-header" onclick="window.Platform.toggleNode('${grade.id}')">
                <div class="tree-grade-title">
                  <span>${isGradeOpen ? '📂' : '📁'}</span>
                  <span>${grade.name}</span>
                </div>
                <div style="display:flex; align-items:center; gap:5px;">
                  <span class="grade-badge">${grade.badge ? grade.badge.split('(')[0].trim() : ''}</span>
                  <span class="node-arrow ${isGradeOpen ? 'open' : ''}">◀</span>
                </div>
              </div>
              <div class="tree-grade-children" style="display:${isGradeOpen ? 'block' : 'none'};">
                ${termsHtml}
              </div>
            </div>
          `;
        }
      });

      if (stageMatches || !state.searchQuery) {
        const isStageOpen = state.expandedNodes.has(stage.id) || !!state.searchQuery;
        html += `
          <div class="tree-stage-group">
            <div class="tree-stage-header" onclick="window.Platform.toggleNode('${stage.id}')">
              <span>${stage.icon} ${stage.name}</span>
              <span class="node-arrow ${isStageOpen ? 'open' : ''}">◀</span>
            </div>
            <div class="tree-stage-children" style="display:${isStageOpen ? 'block' : 'none'};">
              ${gradesHtml}
            </div>
          </div>
        `;
      }
    });

    sidebarTreeContainer.innerHTML = html || '<div style="padding:20px; color:#94a3b8; text-align:center;">لا توجد نتائج مطابقة لبحثك</div>';
    } catch (err) {
      console.error('Critical error in renderTree:', err);
    }
  }

  // Toggle tree node collapse/expand
  function toggleNode(nodeId) {
    if (state.expandedNodes.has(nodeId)) {
      state.expandedNodes.delete(nodeId);
    } else {
      state.expandedNodes.add(nodeId);
    }
    renderTree();
  }

  // Select Lesson
  function selectLesson(lessonId) {
    state.currentLessonId = lessonId;
    state.activeView = 'cockpit';
    
    // Auto-expand all parent ancestors so current lesson is visible in tree
    const p = findLessonPath(lessonId);
    if (p) {
      state.expandedNodes.add(p.stage.id);
      state.expandedNodes.add(p.grade.id);
      state.expandedNodes.add(p.termKey);
      state.expandedNodes.add(p.chapter.id);
    }

    // update tabs
    document.querySelectorAll('.view-tab-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.view === 'cockpit');
    });

    renderTree();
    triggerFlashTransition();
    renderCurrentView();

    // Auto-scroll active item in sidebar smoothly
    setTimeout(() => {
      const activeEl = document.querySelector('.tree-lesson-item.active');
      if (activeEl) {
        activeEl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }, 50);

    // Scroll viewport to top smoothly
    if (viewportArea && typeof viewportArea.scrollTo === 'function') viewportArea.scrollTo({ top: 0, behavior: 'smooth' });
    closeSidebarMobile();
  }

  // ================= View Switcher Handler =================
  function renderCurrentView() {
    if (!viewportArea) return;

    if (state.activeView === 'cockpit') {
      renderLessonCockpit();
    } else if (state.activeView === 'question-bank') {
      if (window.QuestionBank) window.QuestionBank.render(viewportArea);
    } else if (state.activeView === 'exam-builder') {
      if (window.ExamBuilder) window.ExamBuilder.render(viewportArea);
    } else if (state.activeView === 'visual-tree') {
      renderVisualTree();
    } else if (state.activeView === 'suites') {
      renderSuitesView();
    } else if (state.activeView === 'vault') {
      renderVaultView();
    } else if (state.activeView === 'builder') {
      renderBuilderView();
    }
  }

  function buildLessonQuestionPayload(lesson, type, idx) {
    const utils = window.ArabicUtils;
    if (!lesson) return null;
    const inferredGradeId = lesson.gradeId || (lesson.id && lesson.id.startsWith('g3s') ? 'g3s' : (lesson.id && lesson.id.startsWith('g2s') ? 'g2s' : (lesson.id && lesson.id.startsWith('g1s') ? 'g1s' : (lesson.id && lesson.id.startsWith('g3m') ? 'g3m' : (lesson.id && lesson.id.startsWith('g1m') ? 'g1m' : 'g6')))));
    if (type === 'mcq') {
      const m = lesson.quiz.mcq[idx];
      if (!m) return null;
      return {
        uid: lesson.id + '-mcq-' + (idx + 1),
        type: 'mcq',
        typeLabel: 'اختيار من متعدد',
        gradeId: inferredGradeId,
        chapterId: lesson.chapter_id || '',
        chapterNumber: (lesson.chapter || '').split(':')[0] || '',
        chapterTitle: lesson.chapter || '',
        lessonId: lesson.id,
        lessonNumber: lesson.number,
        lessonTitle: lesson.title,
        q: m.q,
        options: m.options.slice(),
        correct: m.correct,
        explanation: m.explanation,
        difficulty: m.difficulty || 'متوسط',
        marks: m.marks || 1,
        image: m.image || m.fig || '',
        imageCaption: m.imageCaption || ''
      };
    } else if (type === 'tf') {
      const t = lesson.quiz.tf[idx];
      if (!t) return null;
      return {
        uid: lesson.id + '-tf-' + (idx + 1),
        type: 'tf',
        typeLabel: 'صواب وخطأ',
        gradeId: inferredGradeId,
        chapterId: lesson.chapter_id || '',
        chapterNumber: (lesson.chapter || '').split(':')[0] || '',
        chapterTitle: lesson.chapter || '',
        lessonId: lesson.id,
        lessonNumber: lesson.number,
        lessonTitle: lesson.title,
        q: t.statement,
        statement: t.statement,
        is_true: t.is_true,
        explanation: t.explanation,
        difficulty: t.difficulty || 'سهل',
        marks: t.marks || 1,
        image: t.image || t.fig || '',
        imageCaption: t.imageCaption || ''
      };
    } else if (type === 'essay') {
      const e = (lesson.quiz.essay || [])[idx];
      if (!e) return null;
      return {
        uid: lesson.id + '-essay-' + (idx + 1),
        type: 'essay',
        typeLabel: 'مسألة مقالية',
        gradeId: inferredGradeId,
        chapterId: lesson.chapter_id || '',
        chapterNumber: (lesson.chapter || '').split(':')[0] || '',
        chapterTitle: lesson.chapter || '',
        lessonId: lesson.id,
        lessonNumber: lesson.number,
        lessonTitle: lesson.title,
        q: e.q,
        ans: e.ans,
        difficulty: e.difficulty || 'متوسط',
        marks: e.marks || 2,
        lines: e.lines || 3,
        image: e.image || e.fig || '',
        imageCaption: e.imageCaption || ''
      };
    } else if (type === 'ws') {
      const w = (lesson.worksheet && lesson.worksheet.questions || [])[idx];
      if (!w) return null;
      return {
        uid: lesson.id + '-ws-' + (idx + 1),
        type: 'essay',
        typeLabel: 'مسألة استقصائية',
        gradeId: inferredGradeId,
        chapterId: lesson.chapter_id || '',
        chapterNumber: (lesson.chapter || '').split(':')[0] || '',
        chapterTitle: lesson.chapter || '',
        lessonId: lesson.id,
        lessonNumber: lesson.number,
        lessonTitle: lesson.title,
        q: w.q,
        ans: w.ans,
        difficulty: 'متوسط',
        marks: 2,
        lines: 3,
        image: w.image || w.fig || '',
        imageCaption: w.imageCaption || ''
      };
    }
    return null;
  }

  function copyLessonQuestionToWord(lessonId, type, idx) {
    const path = findLessonPath(lessonId);
    if (path && window.FirebaseAuthManager) {
      const lIdx = (path.chapter.lessons || []).findIndex(l => l.id === lessonId);
      if (!window.FirebaseAuthManager.isLessonUnlocked(path.chapter, lIdx >= 0 ? lIdx : 0)) {
        window.FirebaseAuthManager.showToast('🔒 ميزة نسخ الأسئلة إلى Word مخصصة للأعضاء المعتمدين والمدير العام. يرجى تسجيل الدخول للحصول على الاعتماد.', 'warning');
        window.FirebaseAuthManager.openAuthModal();
        return;
      }
    }
    const lesson = window.CURRICULUM_DATA.lessons[lessonId];
    const qObj = buildLessonQuestionPayload(lesson, type, idx);
    if (qObj && window.ArabicUtils) {
      window.ArabicUtils.copyQuestionsToWord([qObj], {
        includeAnswers: false,
        numbered: false,
        isSecondary: !!(lessonId && (lessonId.startsWith('g1s') || lessonId.startsWith('g2s') || lessonId.startsWith('g3s')))
      });
    }
  }

  function copySocraticStudentLink(lessonId) {
    const base = window.location.href.split('?')[0].split('#')[0].replace(/index\.html$/, '');
    const cleanBase = base.endsWith('/') ? base : (base + '/');
    const fullUrl = cleanBase + 'socratic_session.html?lesson=' + encodeURIComponent(lessonId);

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(fullUrl).then(() => {
        if (window.ArabicUtils && window.ArabicUtils.showToast) {
          window.ArabicUtils.showToast('✓ تم نسخ رابط الجلسة السقراطية التفاعلية للطالب بنجاح!', 'success');
        }
      }).catch(() => fallbackCopyText(fullUrl));
    } else {
      fallbackCopyText(fullUrl);
    }
  }

  function fallbackCopyText(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    if (window.ArabicUtils && window.ArabicUtils.showToast) {
      window.ArabicUtils.showToast('✓ تم نسخ رابط الجلسة السقراطية التفاعلية للطالب بنجاح!', 'success');
    }
  }

  function toggleLessonQuestionInExam(lessonId, type, idx) {
    const lesson = window.CURRICULUM_DATA.lessons[lessonId];
    const qObj = buildLessonQuestionPayload(lesson, type, idx);
    if (!qObj || !window.ExamBuilder) return;
    if (window.ExamBuilder.hasQuestion(qObj.uid)) {
      window.ExamBuilder.removeQuestion(qObj.uid);
      if (window.ArabicUtils) window.ArabicUtils.showToast('تمت إزالة السؤال من منشئ الاختبارات.', 'info');
    } else {
      window.ExamBuilder.addQuestion(qObj);
    }
    renderLessonCockpit();
  }

  function addAllLessonQuestionsToExam(lessonId) {
    const path = findLessonPath(lessonId);
    if (path && window.FirebaseAuthManager) {
      const lIdx = (path.chapter.lessons || []).findIndex(l => l.id === lessonId);
      if (!window.FirebaseAuthManager.isLessonUnlocked(path.chapter, lIdx >= 0 ? lIdx : 0)) {
        window.FirebaseAuthManager.showToast('🔒 ميزة إضافة الأسئلة لمنشئ الاختبارات مخصصة للأعضاء المعتمدين والمدير العام.', 'warning');
        window.FirebaseAuthManager.openAuthModal();
        return;
      }
    }
    const lesson = window.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson || !window.ExamBuilder) return;
    const all = [];
    (lesson.quiz.mcq || []).forEach((_, i) => all.push(buildLessonQuestionPayload(lesson, 'mcq', i)));
    (lesson.quiz.tf || []).forEach((_, i) => all.push(buildLessonQuestionPayload(lesson, 'tf', i)));
    (lesson.quiz.essay || []).forEach((_, i) => all.push(buildLessonQuestionPayload(lesson, 'essay', i)));
    window.ExamBuilder.addQuestions(all.filter(Boolean));
    renderLessonCockpit();
  }

  function buildBreadcrumbsHtml(pathInfo, lesson) {
    if (pathInfo) {
      const { stage, grade, term, chapter } = pathInfo;
      const allLessons = getAllLessonsList();
      const currentIdx = allLessons.findIndex(item => item.id === lesson.id);
      const hasPrev = currentIdx > 0;
      const hasNext = currentIdx >= 0 && currentIdx < allLessons.length - 1;

      const stagesDropHtml = (window.CURRICULUM_DATA.stages || []).map(s => `
        <div class="crumb-dropdown-item ${s.id === stage.id ? 'active' : ''}" onclick="window.Platform.selectFirstLessonOfStage('${s.id}')">
          <span>${s.icon} ${s.name}</span>
          ${s.id === stage.id ? '<span>✓</span>' : ''}
        </div>
      `).join('');

      const gradesDropHtml = (stage.grades || []).map(g => `
        <div class="crumb-dropdown-item ${g.id === grade.id ? 'active' : ''}" onclick="window.Platform.selectFirstLessonOfGrade('${g.id}')">
          <span>🎓 ${g.name}</span>
          ${g.id === grade.id ? '<span>✓</span>' : ''}
        </div>
      `).join('');

      const termsDropHtml = (grade.terms || []).map(t => `
        <div class="crumb-dropdown-item ${t.id === term.id ? 'active' : ''}" onclick="window.Platform.selectFirstLessonOfTerm('${grade.id}', '${t.id}')">
          <span>${t.icon || '📅'} ${t.name}</span>
          ${t.id === term.id ? '<span>✓</span>' : ''}
        </div>
      `).join('');

      const chaptersDropHtml = (term.chapters || []).map(ch => `
        <div class="crumb-dropdown-item ${ch.id === chapter.id ? 'active' : ''}" onclick="window.Platform.selectFirstLessonOfChapter('${ch.id}')">
          <span>📖 ${ch.number}: ${ch.title}</span>
          ${ch.id === chapter.id ? '<span>✓</span>' : ''}
        </div>
      `).join('');

      const lessonsDropHtml = (chapter.lessons || []).map(l => `
        <div class="crumb-dropdown-item ${l.id === lesson.id ? 'active' : ''}" onclick="window.Platform.selectLesson('${l.id}')">
          <span style="display:flex; align-items:center; gap:6px;">
            <span class="lesson-status-dot ${l.status === 'completed' ? 'completed' : 'roadmap'}"></span>
            ${l.number} ${l.title}
          </span>
          ${l.id === lesson.id ? '<span>✓</span>' : ''}
        </div>
      `).join('');

      return `
        <nav class="tree-breadcrumb-nav" aria-label="المسار التعليمي الهرمي">
          <div class="tree-crumb-root-label">
            <span>🧭 المسار التعليمي:</span>
          </div>

          <div class="tree-crumb-item" onclick="window.Platform.toggleCrumbDropdown(event, 'crumb-drop-stage')" title="المرحلة التعليمية">
            <span>${stage.icon} ${stage.name}</span>
            <span class="crumb-arrow">▾</span>
            <div class="crumb-dropdown" id="crumb-drop-stage">
              ${stagesDropHtml}
            </div>
          </div>

          <span class="crumb-sep">/</span>

          <div class="tree-crumb-item" onclick="window.Platform.toggleCrumbDropdown(event, 'crumb-drop-grade')" title="الصف الدراسي">
            <span>🎓 ${grade.name}</span>
            <span class="crumb-arrow">▾</span>
            <div class="crumb-dropdown" id="crumb-drop-grade">
              ${gradesDropHtml}
            </div>
          </div>

          <span class="crumb-sep">/</span>

          <div class="tree-crumb-item" onclick="window.Platform.toggleCrumbDropdown(event, 'crumb-drop-term')" title="الفصل الدراسي">
            <span>${term.icon || '📅'} ${term.name}</span>
            <span class="crumb-arrow">▾</span>
            <div class="crumb-dropdown" id="crumb-drop-term">
              ${termsDropHtml}
            </div>
          </div>

          <span class="crumb-sep">/</span>

          <div class="tree-crumb-item" onclick="window.Platform.toggleCrumbDropdown(event, 'crumb-drop-chapter')" title="الباب أو الفصل">
            <span>📖 ${chapter.number}: ${chapter.title}</span>
            <span class="crumb-arrow">▾</span>
            <div class="crumb-dropdown" id="crumb-drop-chapter">
              ${chaptersDropHtml}
            </div>
          </div>

          <span class="crumb-sep">/</span>

          <div class="tree-crumb-item current-lesson" onclick="window.Platform.toggleCrumbDropdown(event, 'crumb-drop-lesson')" title="الدرس الحالي">
            <span class="lesson-status-dot completed" style="margin-left:4px;"></span>
            <span>🎯 ${lesson.number}: ${lesson.title}</span>
            <span class="crumb-arrow">▾</span>
            <div class="crumb-dropdown" id="crumb-drop-lesson">
              ${lessonsDropHtml}
            </div>
          </div>

          <div class="tree-crumb-nav-steppers">
            <button type="button" class="crumb-stepper-btn" onclick="window.Platform.goToPrevLesson()" ${hasPrev ? '' : 'disabled'} title="الانتقال للدرس السابق">
              ▶ السابق
            </button>
            <button type="button" class="crumb-stepper-btn" onclick="window.Platform.goToNextLesson()" ${hasNext ? '' : 'disabled'} title="الانتقال للدرس التالي">
              التالي ◀
            </button>
          </div>
        </nav>
      `;
    }
    return `
      <div class="breadcrumb-trail">
        <span>🏫 ${lesson.stage || ''}</span>
        <span>/</span>
        <span>🎓 ${lesson.grade || ''}</span>
        <span>/</span>
        <span>📅 ${lesson.term || ''}</span>
        <span>/</span>
        <span>📖 ${lesson.chapter || ''}</span>
      </div>
    `;
  }

  function renderVisitorLockedLessonGate(lesson, pathInfo) {
    if (!viewportArea) return;
    const isG6 = isFullBookLesson(lesson);
    const topTreeBreadcrumbsHtml = buildBreadcrumbsHtml(pathInfo, lesson);

    const currentUser = window.FirebaseAuthManager ? window.FirebaseAuthManager.getCurrentUser() : null;
    const isPending = currentUser && currentUser.role === 'pending';

    viewportArea.innerHTML = `
      <div class="lesson-cockpit-header">
        ${topTreeBreadcrumbsHtml}
        <div class="lesson-header-main">
          <div class="lesson-title-area">
            <h2>الدرس ${fmtNum(lesson.number, isG6)}: ${lesson.title}</h2>
            <div class="lesson-subtitle">${lesson.english_title ? (lesson.english_title + ' • ') : ''}صفحات الكتاب المدرسي: ${fmtNum(lesson.pages, isG6)}</div>
            <div class="lesson-meta-badges">
              <span class="meta-badge red">🔒 محتوى مخصص للأعضاء المعتمدين</span>
              <span class="meta-badge">📖 ${lesson.chapter || ''}</span>
              <span class="meta-badge">💡 إشراف: أ. محمد عبدالله جمعة</span>
            </div>
          </div>
        </div>
      </div>

      <div class="locked-lesson-container">
        <div class="locked-shield-card">
          <div class="locked-shield-icon">🔒</div>
          <h3 class="locked-shield-title">هذا الدرس مخصص للأعضاء المعتمدين</h3>
          
          <div class="locked-shield-notice">
            <strong>📢 سياسة وصول الزوار والمعاينة النموذجية:</strong>
            <p style="margin-top:6px; line-height:1.7;">
              يُتاح لزوار المنصة الكرام استعراض <strong>أول درسين مجاناً من كل فصل دراسي</strong> كعينة معاينة شاملة لكافة المحتويات والأنشطة والتحضير الميداني والاختبارات.
            </p>
            <p style="margin-top:6px; line-height:1.7;">
              للوصول إلى هذا الدرس (<strong>${lesson.number}: ${lesson.title}</strong>) وبقية دروس المنهج، يرجى تسجيل الدخول بحساب Google أو رقم الجوال ليتم اعتماد حسابك من قبل المدير العام (أ. محمد عبدالله جمعة).
            </p>
          </div>

          ${isPending ? `
            <div class="pending-approval-banner">
              <span style="font-size:2rem;">⏳</span>
              <div>
                <strong style="color:#b45309; font-size:1.05rem;">حسابك قيد المراجعة والاعتماد من قبل المدير العام:</strong>
                <p style="margin-top:4px; color:#475569; line-height:1.6;">مرحباً بك (${escHtml(currentUser.displayName)}). تم تسجيل طلب اعتمادك بنجاح وهو قيد المراجعة حالياً من قبل خبير الرياضيات والمدير العام (أ. محمد عبدالله جمعة). ستتاح لك كافة المناهج المتاحة والخصائص فور الاعتماد.</p>
              </div>
            </div>
          ` : `
            <div class="locked-action-btns">
              <button type="button" class="nav-btn primary large" onclick="window.FirebaseAuthManager.openAuthModal()">
                🔑 <span>تسجيل الدخول / طلب اعتماد العضوية</span>
              </button>
              <button type="button" class="nav-btn large director" onclick="window.FirebaseAuthManager.signInAsDirector()">
                👑 <span>دخول المدير العام (أ. محمد عبدالله جمعة)</span>
              </button>
            </div>
          `}

          <!-- بطاقة التواصل المباشر وطلب العضوية عبر واتساب وهاتف -->
          <div class="membership-direct-contact-card" style="margin:20px 0; background:linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%); border:2px solid #86efac; border-radius:14px; padding:18px 20px; text-align:center; box-shadow:0 4px 14px rgba(16, 185, 129, 0.08);">
            <div style="display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:8px;">
              <span style="font-size:1.7rem;">💬</span>
              <h4 style="font-size:1.15rem; font-weight:800; color:#065f46; margin:0;">طلب تفعيل العضوية والتواصل المباشر</h4>
            </div>
            <p style="font-size:0.92rem; color:#047857; margin-bottom:12px; line-height:1.6;">
              لطلب اعتماد العضوية وفتح الوصول الكامل لجميع المناهج الدراسية وبنك الأسئلة، تواصل مباشرة مع <strong>أ. محمد عبدالله جمعة</strong>:
            </p>
            <div style="display:inline-flex; align-items:center; justify-content:center; gap:10px; background:#ffffff; border:1.5px dashed #10b981; border-radius:10px; padding:8px 18px; margin-bottom:14px; font-size:1.18rem; font-weight:800; color:#065f46; direction:ltr;">
              <span>📱 0545841974</span>
              <span style="color:#cbd5e1; font-weight:normal;">|</span>
              <span style="color:#047857;">+966545841974</span>
            </div>
            <div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
              <a href="https://wa.me/966545841974?text=${encodeURIComponent('السلام عليكم ورحمة الله وبركاته، أستاذ محمد عبدالله جمعة، أود طلب تفعيل واعتماد العضوية الكاملة لجميع المناهج المتاحة في منصة الرائد التعليمية للرياضيات.')}"
                 target="_blank" 
                 rel="noopener noreferrer"
                 style="display:inline-flex; align-items:center; justify-content:center; gap:8px; background:#25D366; color:#ffffff; font-weight:800; font-size:0.95rem; padding:10px 22px; border-radius:10px; text-decoration:none; box-shadow:0 3px 12px rgba(37, 211, 102, 0.35);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.04 14.69 2 12.04 2M12.04 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.81 13.47 3.81 11.91C3.81 7.37 7.5 3.67 12.04 3.67M9.53 7.35C9.34 7.35 9.04 7.42 8.78 7.7C8.53 7.97 7.82 8.63 7.82 10C7.82 11.37 8.82 12.69 8.96 12.87C9.1 13.06 10.93 15.87 13.73 17.08C14.4 17.36 14.92 17.54 15.33 17.67C16 17.88 16.63 17.85 17.12 17.78C17.67 17.7 18.8 17.09 19.04 16.42C19.28 15.75 19.28 15.17 19.21 15.06C19.14 14.94 18.95 14.87 18.66 14.73C18.38 14.59 17.01 13.91 16.75 13.82C16.5 13.72 16.31 13.68 16.12 13.96C15.93 14.24 15.39 14.87 15.22 15.06C15.06 15.25 14.89 15.27 14.61 15.13C14.33 14.99 13.42 14.69 12.35 13.74C11.51 13 10.95 12.08 10.78 11.8C10.62 11.52 10.76 11.37 10.9 11.23C11.03 11.1 11.19 10.89 11.33 10.73C11.47 10.56 11.52 10.45 11.61 10.26C11.71 10.07 11.66 9.91 11.59 9.77C11.52 9.63 10.95 8.24 10.72 7.68C10.49 7.13 10.26 7.21 10.09 7.2C9.93 7.2 9.74 7.2 9.55 7.2L9.53 7.35Z"/>
                </svg>
                <span>تواصل عبر واتساب لطلب العضوية</span>
              </a>
              <a href="tel:+966545841974" 
                 style="display:inline-flex; align-items:center; justify-content:center; gap:6px; background:#ffffff; color:#065f46; border:1.5px solid #10b981; font-weight:700; font-size:0.92rem; padding:10px 18px; border-radius:10px; text-decoration:none;">
                <span>📞 اتصال هاتفي</span>
              </a>
            </div>
          </div>

          <div class="locked-features-list">
            <h4 style="color:#1e3a8a; font-weight:800; margin-bottom:12px;">مزايا الحساب المعتمد والوصول الإداري:</h4>
            <div class="features-check-grid">
              <div class="feat-item">✓ وصول غير محدود لكافة دروس ومناهج الرياضيات المتاحة (المرحلة الابتدائية، المتوسطة، والثانوية) بجميع فصولها الدراسية.</div>
              <div class="feat-item">✓ التحضير الميداني الشامل المعتمد بـ ${fmtNum(6, true)} محطات متكاملة وتوزيع زمني واقعي (${fmtNum(45, true)} دقيقة).</div>
              <div class="feat-item">✓ استوديو توليد التحضير بالذكاء الاصطناعي مع تخصيص زمن الحصة والأنماط التدريسية.</div>
              <div class="feat-item">✓ نسخ التحضير الميداني والأسئلة بضغطة زر إلى Word بصيغة جداول رسمية جاهزة للطباعة.</div>
              <div class="feat-item">✓ بنك الأسئلة الشامل ومنشئ الاختبارات مع نماذج الإجابة وسلم الدرجات لكافة الصفوف.</div>
              <div class="feat-item">✓ حماية فائقة للحساب من المشاركة عبر تقنية الجلسة النشطة الواحدة (Single Active Session).</div>
            </div>
          </div>

          <div style="margin-top:22px; text-align:center;">
            <button type="button" class="nav-btn" onclick="window.Platform.goToPrevLesson()">
              ◀ الانتقال للدرس السابق (أحد الدروس المفتوحة للمعاينة)
            </button>
          </div>
        </div>
      </div>
    `;
  }

  // ================= Render Lesson Cockpit =================
  function renderLessonCockpit() {
    try {
      if (!viewportArea) viewportArea = document.getElementById('app-viewport');
      if (!viewportArea) return;
      if (!window.CURRICULUM_DATA || !window.CURRICULUM_DATA.lessons) {
        viewportArea.innerHTML = `
          <div style="padding:40px 20px; text-align:center; background:#ffffff; border-radius:16px; margin:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06);">
            <div style="font-size:2.5rem; margin-bottom:12px;">⏳</div>
            <h3 style="font-weight:800; color:#1e3a8a; margin-bottom:8px;">جاري تحميل محتوى الدرس وبيانات المنهج...</h3>
            <p style="color:#64748b; font-size:0.9rem;">يُرجى الانتظار بضع ثوانٍ بينما تكتمل مزامنة الدروس السحابية.</p>
          </div>
        `;
        setTimeout(() => {
          if (window.CURRICULUM_DATA && window.CURRICULUM_DATA.lessons) renderLessonCockpit();
        }, 200);
        return;
      }
      const lesson = window.CURRICULUM_DATA.lessons[state.currentLessonId];
      if (!lesson) {
        renderUnfinishedLessonPlaceholder(state.currentLessonId);
        return;
      }

    const pathInfo = findLessonPath(lesson.id);
    let isLessonUnlocked = true;
    if (pathInfo && window.FirebaseAuthManager) {
      const lIdx = (pathInfo.chapter.lessons || []).findIndex(l => l.id === lesson.id);
      isLessonUnlocked = window.FirebaseAuthManager.isLessonUnlocked(pathInfo.chapter, lIdx >= 0 ? lIdx : 0);
    }

    if (!isLessonUnlocked) {
      renderVisitorLockedLessonGate(lesson, pathInfo);
      return;
    }

    const isG6 = isFullBookLesson(lesson);
    const quiz = lesson.quiz || { mcq: [], tf: [], essay: [] };
    const essays = quiz.essay || [];
    const quizStats = state.quizScores[lesson.id] || { answeredCount: 0, correctCount: 0, userAnswers: {} };
    const totalAutoQ = (quiz.mcq || []).length + (quiz.tf || []).length;
    const examApi = window.ExamBuilder;
    const isApproved = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isApproved === 'function' && window.FirebaseAuthManager.isApproved();
    const isAdmin = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isAdmin === 'function' && window.FirebaseAuthManager.isAdmin();
    const isPending = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isPending === 'function' && window.FirebaseAuthManager.isPending();

    const topTreeBreadcrumbsHtml = buildBreadcrumbsHtml(pathInfo, lesson);

    let html = `
      <!-- Cockpit Header Banner -->
      <div class="lesson-cockpit-header">
        ${topTreeBreadcrumbsHtml}
        <div class="lesson-header-main">
          <div class="lesson-title-area">
            <h2>الدرس ${fmtNum(lesson.number, isG6)}: ${lesson.title}</h2>
            <div class="lesson-subtitle">${lesson.english_title ? (lesson.english_title + ' • ') : ''}صفحات الكتاب المدرسي: ${fmtNum(lesson.pages, isG6)}</div>
            <div class="lesson-meta-badges">
              ${isAdmin ? `
                <span class="meta-badge admin-member" title="حساب المدير العام">👑 الحساب: المدير العام (أ. محمد عبدالله جمعة)</span>
              ` : (isApproved ? `
                <span class="meta-badge verified-member" title="عضوية معتمدة رسمياً">🌟 العضوية: معتمد رسمي (وصول كامل للمحتوى، التحضير، الطباعة، وبنك الأسئلة) ✓</span>
              ` : (isPending ? `
                <span class="meta-badge pending-member" title="الحساب قيد مراجعة واعتماد المدير العام">⏳ العضوية: قيد المراجعة (معاينة أول درسين • الحد الأقصى ${fmtNum(5, true)} أسئلة للنوع)</span>
              ` : `
                <span class="meta-badge visitor-member" onclick="window.FirebaseAuthManager.openAuthModal()" style="cursor:pointer;" title="انقر لتسجيل الدخول وطلب الاعتماد">🔒 العضوية: نسخة تجريبية (الحد الأقصى ${fmtNum(5, true)} أسئلة للنوع • اطلب الاعتماد) ↗</span>
              `))}
              <span class="meta-badge green">✓ ${lesson.badge || 'مكتمل وشامل'}</span>
              <span class="meta-badge" onclick="window.Platform.switchLessonTab('prep')" style="cursor:pointer;" title="الانتقال إلى التحضير الميداني الشامل">📋 التحضير الميداني المعتمد</span>
              <span class="meta-badge" onclick="window.Platform.switchLessonTab('explain')" style="cursor:pointer; background:#eff6ff; color:#1d4ed8; border-color:#bfdbfe;" title="شرح تفصيلي بالأمثلة التوضيحية لأي جزئية في الدرس">🧠 الشارح التفصيلي بالأمثلة</span>
              <span class="meta-badge" onclick="window.Platform.switchLessonTab('socratic')" style="cursor:pointer;" title="الانتقال إلى منصة سقراط التوليدية">🏛️ منصة سقراط الحوارية</span>
              <span class="meta-badge" onclick="window.Platform.switchLessonTab('tools')" style="cursor:pointer;" title="الانتقال إلى الأدوات والمختبر التفاعلي">🛠️ ${(lesson.lesson_tools && lesson.lesson_tools.title) ? lesson.lesson_tools.title.split('(')[0].trim() : 'أدوات الدرس الذكية'}</span>
              <span class="meta-badge orange" onclick="window.Platform.switchLessonTab('quiz')" style="cursor:pointer;" title="انقر للانتقال المباشر وحل الاختبار المقنن">📝 الاختبار المقنن: ${fmtNum(quiz.mcq.length, true)} اختيار + ${fmtNum(quiz.tf.length, true)} صواب وخطأ${essays.length ? (' + ' + fmtNum(essays.length, true) + ' مقالي') : ''}</span>
              <span class="meta-badge" onclick="window.Platform.openCurrentLessonHtmlGenerator()" style="cursor:pointer; background:#ecfdf5; color:#065f46; border-color:#a7f3d0;" title="توليد صفحة تفاعلية مستقلة بصيغة HTML">🌐 مولد HTML التفاعلي</span>
              <span class="meta-badge">💡 إشراف: أ. محمد عبدالله جمعة</span>
            </div>
          </div>
          <div class="lesson-header-actions">
            <button class="nav-btn success" onclick="window.Platform.openCurrentLessonHtmlGenerator()" title="توليد وتصدير صفحة تفاعلية مستقلة بصيغة HTML للدرس تعمل دون إنترنت">🌐 صفحة تفاعلية (HTML)</button>
            ${isG6 ? `<button class="nav-btn" onclick="window.Platform.addAllLessonQuestionsToExam('${lesson.id}')">➕ أضف أسئلة الدرس للاختبار</button>` : ''}
            <button class="nav-btn primary" onclick="window.print()">🖨️ طباعة كامل الدرس</button>
          </div>
        </div>
      </div>

      <!-- Navigation Tabs for the Lesson -->
      <div class="lesson-nav-tabs">
        <button class="lesson-tab-button ${state.activeLessonTab === 'prep' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('prep')">
          📋 التحضير الميداني الشامل المعتمد
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'summary' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('summary')">
          📚 الملخص ومطوية المفاهيم
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'explain' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('explain')">
          🧠 الشارح التفصيلي بالأمثلة
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'worksheet' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('worksheet')">
          📄 ورقة العمل الاستقصائية
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'socratic' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('socratic')">
          🏛️ منصة سقراط التوليدية (الحوار والاستقصاء)
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'tools' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('tools')">
          🖥️ المختبر والأدوات التفاعلية
        </button>
        <button class="lesson-tab-button ${state.activeLessonTab === 'quiz' ? 'active' : ''}" onclick="window.Platform.switchLessonTab('quiz')">
          📝 الاختبار المقنن (${fmtNum(quiz.mcq.length, true)} اختيارات + ${fmtNum(quiz.tf.length, true)} صواب وخطأ${essays.length ? (' + ' + fmtNum(essays.length, true) + ' مقالي') : ''})
        </button>
      </div>

      <!-- Tab 1: Comprehensive Field Lesson Preparation (Master Unified Standard) -->
      <div class="tab-pane-content ${state.activeLessonTab === 'prep' ? 'active' : ''}" id="tab-prep">
        ${window.LessonPrepManager ? window.LessonPrepManager.renderPane(lesson) : ''}
      </div>

      <!-- Tab 3: Summary & Concept Guide -->
      <div class="tab-pane-content ${state.activeLessonTab === 'summary' ? 'active' : ''}" id="tab-summary">
        <div class="summary-container">
          <div class="card-section-title">
            <span>📚 الخلاصة المعرفية ومطوية المفاهيم والقوانين</span>
          </div>
          <div style="font-size:1.05rem; line-height:1.7; margin-bottom:16px;">
            <strong>📌 المفهوم الأساسي:</strong> ${fmtNum(lesson.summary.concept, isG6)}
          </div>
          <div style="margin-bottom:16px;">
            <strong style="color:var(--primary);">الطرق والخصائص الإجرائية:</strong>
            <ul style="margin-right:24px; margin-top:8px; line-height:1.8;">
              ${lesson.summary.methods.map(m => `<li>${fmtNum(m, isG6)}</li>`).join('')}
            </ul>
          </div>
          <div class="golden-rule-box">
            <span class="golden-rule-icon">🌟</span>
            <div>
              <strong>القاعدة الذهبية للمعلم والطالب:</strong>
              <div>${fmtNum(lesson.summary.golden_rule, isG6)}</div>
            </div>
          </div>
          <div class="solved-example-box">
            <div class="solved-example-title">
              <span>✍️ مثال محلول تطبيقي شامل:</span>
            </div>
            <div class="solved-example-body">${fmtNum(lesson.summary.solved_example, isG6)}</div>
          </div>
          ${(lesson.figures && lesson.figures.length) ? `
            <div style="margin-top:20px;">
              <strong style="color:var(--primary); display:block; margin-bottom:10px;">🖼️ الأشكال والتمثيلات المعتمدة في الدرس (اضغط للتكبير):</strong>
              <div class="lesson-figures-grid">
                ${lesson.figures.map(fig => {
                  const imgSrc = typeof fig === 'string' ? fig : ((fig && fig.image) || '');
                  if (!imgSrc) return '';
                  const rawCap = (typeof fig === 'object' && fig && fig.caption) ? fig.caption : '';
                  const cap = fmtNum(rawCap, true);
                  return `
                    <div class="lesson-figure-card">
                      <img src="${escHtml(imgSrc)}" alt="${escHtml(cap || 'شكل تعليمي')}" loading="lazy"
                        onclick="window.Platform.openImageLightbox(this.getAttribute('src'), this.getAttribute('data-caption'))"
                        data-caption="${escHtml(cap)}" />
                      ${cap ? `<div class="lesson-figure-caption">${escHtml(cap)}</div>` : ''}
                    </div>
                  `;
                }).join('')}
              </div>
            </div>
          ` : ''}
        </div>
      </div>

      <!-- Tab 2b: Hybrid Concept Explainer with Worked Examples -->
      <div class="tab-pane-content ${state.activeLessonTab === 'explain' ? 'active' : ''}" id="tab-explain">
        ${window.ConceptExplainer ? window.ConceptExplainer.renderPane(lesson) : ''}
      </div>

      <!-- Tab 4: Inquiry Worksheet -->
      <div class="tab-pane-content ${state.activeLessonTab === 'worksheet' ? 'active' : ''}" id="tab-worksheet">
        <div class="worksheet-container">
          <div class="card-section-title" style="justify-content:space-between;">
            <span>📄 ${fmtNum(lesson.worksheet.title, isG6)}</span>
            <button class="nav-btn" onclick="window.Platform.toggleAllSolutions()">إظهار / إخفاء جميع الحلول</button>
          </div>
          ${lesson.worksheet.questions.map((q, idx) => `
            <div class="ws-item">
              <div class="ws-question-text">${fmtNum(q.q, isG6)}</div>
              ${renderQuestionFigure(q)}
              <div style="display:flex; gap:8px; flex-wrap:wrap; align-items:center;">
                <button class="ws-toggle-btn" onclick="window.Platform.toggleWsSolution('ws-sol-${idx}')">
                  <span>💡 إظهار الحل النموذجي</span>
                </button>
                <button class="qb-act-btn copy-word-btn" type="button" onclick="window.Platform.copyLessonQuestionToWord('${lesson.id}', 'ws', ${idx})">
                  📋 نسخ لـ Word
                </button>
              </div>
              <div class="ws-solution-box" id="ws-sol-${idx}">
                <strong>الحل النموذجي:</strong> ${fmtNum(q.ans, isG6)}
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <!-- Tab 5: Socratic Inquiry Platform (منصة سقراط التوليدية المخصصة للدرس) -->
      <div class="tab-pane-content ${state.activeLessonTab === 'socratic' ? 'active' : ''}" id="tab-socratic">
        ${renderSocraticPane(lesson, isG6)}
      </div>

      <!-- Tab 6: Interactive Tools & Smart Boards (المختبر والأدوات التفاعلية المخصصة) -->
      <div class="tab-pane-content ${state.activeLessonTab === 'tools' ? 'active' : ''}" id="tab-tools">
        ${renderLessonToolsPane(lesson, isG6)}
      </div>

      <!-- Tab 6: STANDARDIZED QUIZ (10 MCQs + 5 TF + Essay) -->
      <div class="tab-pane-content ${state.activeLessonTab === 'quiz' ? 'active' : ''}" id="tab-quiz">
        <div class="quiz-cockpit">
          ${(() => {
            const isUserFullyAuthorized = isApproved || isAdmin;
            const displayedMcqs = isUserFullyAuthorized ? quiz.mcq : (quiz.mcq || []).slice(0, 5);
            const hasLockedMcqs = !isUserFullyAuthorized && (quiz.mcq || []).length > 5;
            const displayedTfs = isUserFullyAuthorized ? quiz.tf : (quiz.tf || []).slice(0, 5);
            const hasLockedTfs = !isUserFullyAuthorized && (quiz.tf || []).length > 5;
            const displayedEssays = isUserFullyAuthorized ? essays : (essays || []).slice(0, 5);
            const hasLockedEssays = !isUserFullyAuthorized && (essays || []).length > 5;
            const totalPreviewCount = displayedMcqs.length + displayedTfs.length;

            return `
              <div class="quiz-header-banner">
                <div>
                  <h3 style="font-size:1.25rem; font-weight:800; margin-bottom:4px;">📝 الاختبار المقنن والتقييم الإلكتروني الفوري</h3>
                  <p style="font-size:0.88rem; opacity:0.9;">مكون من ${fmtNum(quiz.mcq.length, true)} فقرات اختيار من متعدد بأربع خيارات أفقية + ${fmtNum(quiz.tf.length, true)} فقرات صواب وخطأ${essays.length ? (' + ' + fmtNum(essays.length, true) + ' مسائل مقالية') : ''}</p>
                </div>
                <div class="quiz-score-badge" id="quiz-live-score">
                  ${isUserFullyAuthorized 
                    ? `الدرجة: ${fmtNum(quizStats.correctCount, true)} / ${fmtNum(totalAutoQ, true)}`
                    : `الدرجة: ${fmtNum(quizStats.correctCount, true)} / ${fmtNum(totalPreviewCount, true)} (معاينة ${fmtNum(5, true)} أسئلة)`
                  }
                </div>
              </div>

              <!-- Part 1: 10 MCQs with 4 Horizontal Options -->
              <div class="quiz-part-title">
                <span>🔹 القسم الأول: أسئلة الاختيار من متعدد (${fmtNum(quiz.mcq.length, true)} فقرات - ${fmtNum(4, true)} خيارات أفقية)${!isUserFullyAuthorized ? ` [معاينة ${fmtNum(5, true)} أسئلة]` : ''}</span>
                <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">(لكل فقرة خيار واحد فقط صحيح)</span>
              </div>

              <div class="mcq-list">
                ${displayedMcqs.map((mcq, qIdx) => {
                  const userAns = quizStats.userAnswers['mcq-' + qIdx];
                  const isAnswered = userAns !== undefined;
                  const uid = lesson.id + '-mcq-' + (qIdx + 1);
                  const inExam = examApi && examApi.hasQuestion(uid);
                  const isSecQuiz = isCurrentSecondary();
                  const letters = isSecQuiz ? ['A', 'B', 'C', 'D'] : ['أ', 'ب', 'ج', 'د'];
                  return `
                    <div class="question-card" id="card-mcq-${qIdx}">
                      <div class="question-header" style="justify-content:space-between; width:100%;">
                        <div style="display:flex; align-items:flex-start; gap:10px; flex:1;">
                          <span class="q-badge">س ${fmtNum(qIdx + 1, true)}</span>
                          <span class="q-text">${fmtNum(mcq.q, isG6)}</span>
                        </div>
                        <div class="q-inline-tools">
                          ${mcq.difficulty ? `<span class="qb-pill">${mcq.difficulty}</span>` : ''}
                          <button type="button" class="qb-act-btn copy-word-btn" onclick="window.Platform.copyLessonQuestionToWord('${lesson.id}', 'mcq', ${qIdx})">📋 نسخ لـ Word</button>
                          <button type="button" class="qb-act-btn add-exam-btn ${inExam ? 'added' : ''}" onclick="window.Platform.toggleLessonQuestionInExam('${lesson.id}', 'mcq', ${qIdx})">${inExam ? '✓ مضاف' : '➕ للاختبار'}</button>
                        </div>
                      </div>
                      ${renderQuestionFigure(mcq)}
                      <div class="mcq-options-horizontal">
                        ${mcq.options.map((opt, optIdx) => {
                          let btnClass = 'opt-btn';
                          if (isAnswered) {
                            if (optIdx === mcq.correct) btnClass += ' correct';
                            else if (optIdx === userAns) btnClass += ' wrong';
                          }
                          return `
                            <button class="${btnClass}" ${isAnswered ? 'disabled' : ''} onclick="window.Platform.answerMCQ(${qIdx}, ${optIdx})">
                              <span class="opt-letter">${letters[optIdx]}</span>
                              <span class="opt-text">${fmtNum(opt, isG6)}</span>
                            </button>
                          `;
                        }).join('')}
                      </div>
                      <div class="q-explanation-box ${isAnswered ? 'show' : ''}" id="exp-mcq-${qIdx}">
                        <strong>💡 التفسير الرياضي:</strong> ${fmtNum(mcq.explanation, isG6)}
                      </div>
                    </div>
                  `;
                }).join('')}
                ${hasLockedMcqs ? `
                  <div class="quiz-locked-gate">
                    <div class="qlg-shield-icon">🔒</div>
                    <div class="qlg-info">
                      <div class="qlg-title">الأسئلة المقننة المتبقية (من س ${fmtNum(6, true)} إلى س ${fmtNum(10, true)}) مخصصة للأعضاء المعتمدين والمدير العام</div>
                      <div class="qlg-desc">
                        وفق ضوابط المنصة، يُسمح لغير الأعضاء المعتمدين بمعاينة ${fmtNum(5, true)} أسئلة فقط لكل نوع. سجّل دخولك واطلب اعتماد العضوية فوراً لفتح كافة أسئلة الاختبار المقنن بالكامل (${fmtNum(10, true)} اختيار من متعدد + ${fmtNum(5, true)} صواب وخطأ + ${fmtNum(3, true)} مقالي) مع التفسيرات الرياضية، وإتاحة تصديرها لـ Word وبنك الأسئلة الشامل.
                      </div>
                    </div>
                    <button type="button" class="qlg-action-btn" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()">
                      🔑 تسجيل الدخول / طلب اعتماد العضوية ↗
                    </button>
                  </div>
                ` : ''}
              </div>

              <!-- Part 2: 5 True / False Questions -->
              <div class="quiz-part-title">
                <span>🔹 القسم الثاني: أسئلة الصواب والخطأ (${fmtNum(quiz.tf.length, true)} فقرات)${!isUserFullyAuthorized && hasLockedTfs ? ` [معاينة ${fmtNum(5, true)} أسئلة]` : ''}</span>
                <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">(حدد صواب أو خطأ مع التبرير)</span>
              </div>

              <div class="tf-list">
                ${displayedTfs.map((tf, qIdx) => {
                  const userAns = quizStats.userAnswers['tf-' + qIdx];
                  const isAnswered = userAns !== undefined;
                  const uid = lesson.id + '-tf-' + (qIdx + 1);
                  const inExam = examApi && examApi.hasQuestion(uid);
                  let trueClass = 'tf-btn opt-true';
                  let falseClass = 'tf-btn opt-false';

                  if (isAnswered) {
                    if (tf.is_true) {
                      trueClass += ' correct';
                      if (userAns === false) falseClass += ' wrong';
                    } else {
                      falseClass += ' correct';
                      if (userAns === true) trueClass += ' wrong';
                    }
                  }

                  return `
                    <div class="question-card" id="card-tf-${qIdx}">
                      <div class="question-header" style="justify-content:space-between; width:100%;">
                        <div style="display:flex; align-items:flex-start; gap:10px; flex:1;">
                          <span class="q-badge" style="background:#059669;">س ${fmtNum(qIdx + quiz.mcq.length + 1, true)}</span>
                          <span class="q-text">${fmtNum(tf.statement, isG6)}</span>
                        </div>
                        <div class="q-inline-tools">
                          ${tf.difficulty ? `<span class="qb-pill">${tf.difficulty}</span>` : ''}
                          <button type="button" class="qb-act-btn copy-word-btn" onclick="window.Platform.copyLessonQuestionToWord('${lesson.id}', 'tf', ${qIdx})">📋 نسخ لـ Word</button>
                          <button type="button" class="qb-act-btn add-exam-btn ${inExam ? 'added' : ''}" onclick="window.Platform.toggleLessonQuestionInExam('${lesson.id}', 'tf', ${qIdx})">${inExam ? '✓ مضاف' : '➕ للاختبار'}</button>
                        </div>
                      </div>
                      ${renderQuestionFigure(tf)}
                      <div class="tf-options-horizontal">
                        <button class="${trueClass}" ${isAnswered ? 'disabled' : ''} onclick="window.Platform.answerTF(${qIdx}, true)">
                          <span>✓ صواب</span>
                        </button>
                        <button class="${falseClass}" ${isAnswered ? 'disabled' : ''} onclick="window.Platform.answerTF(${qIdx}, false)">
                          <span>✗ خطأ</span>
                        </button>
                      </div>
                      <div class="q-explanation-box ${isAnswered ? 'show' : ''}" id="exp-tf-${qIdx}">
                        <strong>💡 التفسير الرياضي:</strong> ${fmtNum(tf.explanation, isG6)}
                      </div>
                    </div>
                  `;
                }).join('')}
                ${hasLockedTfs ? `
                  <div class="quiz-locked-gate">
                    <div class="qlg-shield-icon">🔒</div>
                    <div class="qlg-info">
                      <div class="qlg-title">بقية أسئلة الصواب والخطأ مخصصة للأعضاء المعتمدين</div>
                      <div class="qlg-desc">سجّل دخولك واطلب الاعتماد لفتح كامل الأسئلة.</div>
                    </div>
                    <button type="button" class="qlg-action-btn" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()">🔑 طلب الاعتماد ↗</button>
                  </div>
                ` : ''}
              </div>

              ${displayedEssays.length ? `
                <!-- Part 3: Essay & Application Problems -->
                <div class="quiz-part-title">
                  <span>🔹 القسم الثالث: المسائل المقالية والتطبيقية (${fmtNum(essays.length, true)} مسائل)${!isUserFullyAuthorized && hasLockedEssays ? ` [معاينة ${fmtNum(5, true)} مسائل]` : ''}</span>
                  <span style="font-size:0.85rem; color:var(--text-muted); font-weight:600;">(تُستخدم في الاختبارات الكتابية والنسخ لـ Word)</span>
                </div>
                <div class="tf-list">
                  ${displayedEssays.map((es, eIdx) => {
                    const uid = lesson.id + '-essay-' + (eIdx + 1);
                    const inExam = examApi && examApi.hasQuestion(uid);
                    return `
                      <div class="question-card" id="card-essay-${eIdx}">
                        <div class="question-header" style="justify-content:space-between; width:100%;">
                          <div style="display:flex; align-items:flex-start; gap:10px; flex:1;">
                            <span class="q-badge" style="background:#7c3aed;">س ${fmtNum(eIdx + quiz.mcq.length + quiz.tf.length + 1, true)}</span>
                            <span class="q-text">${fmtNum(es.q, isG6)}</span>
                          </div>
                          <div class="q-inline-tools">
                            <span class="qb-pill marks-pill">${window.ArabicUtils ? window.ArabicUtils.formatMark(es.marks || 2, isCurrentSecondary()) : fmtNum(2, true) + ' درجة'}</span>
                            <button type="button" class="qb-act-btn copy-word-btn" onclick="window.Platform.copyLessonQuestionToWord('${lesson.id}', 'essay', ${eIdx})">📋 نسخ لـ Word</button>
                            <button type="button" class="qb-act-btn add-exam-btn ${inExam ? 'added' : ''}" onclick="window.Platform.toggleLessonQuestionInExam('${lesson.id}', 'essay', ${eIdx})">${inExam ? '✓ مضاف' : '➕ للاختبار'}</button>
                          </div>
                        </div>
                        ${renderQuestionFigure(es)}
                        <div style="display:flex; gap:8px; margin-top:8px;">
                          <button type="button" class="ws-toggle-btn" onclick="window.Platform.toggleWsSolution('essay-sol-${eIdx}')">💡 إظهار الحل النموذجي</button>
                        </div>
                        <div class="ws-solution-box" id="essay-sol-${eIdx}">
                          <strong>الحل النموذجي:</strong> ${fmtNum(es.ans, isG6)}
                        </div>
                      </div>
                    `;
                  }).join('')}
                  ${hasLockedEssays ? `
                    <div class="quiz-locked-gate">
                      <div class="qlg-shield-icon">🔒</div>
                      <div class="qlg-info">
                        <div class="qlg-title">بقية المسائل المقالية مخصصة للأعضاء المعتمدين</div>
                        <div class="qlg-desc">سجّل دخولك واطلب الاعتماد للوصول غير المحدود.</div>
                      </div>
                      <button type="button" class="qlg-action-btn" onclick="window.FirebaseAuthManager && window.FirebaseAuthManager.openAuthModal()">🔑 طلب الاعتماد ↗</button>
                    </div>
                  ` : ''}
                </div>
              ` : ''}
            `;
          })()}

          <!-- Bottom Actions & Reset -->
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:24px; padding-top:16px; border-top:1px solid var(--border-light); flex-wrap:wrap; gap:10px;">
            <button class="nav-btn" onclick="window.Platform.resetQuiz('${lesson.id}')">🔄 إعادة الاختبار</button>
            <div style="display:flex; gap:8px;">
              ${isG6 ? `<button class="nav-btn" onclick="window.Platform.addAllLessonQuestionsToExam('${lesson.id}')">➕ إضافة كل أسئلة الدرس للاختبار</button>` : ''}
              <button class="nav-btn primary" onclick="window.print()">🖨️ طباعة تقرير النتيجة</button>
            </div>
          </div>
        </div>
      </div>
    `;

    viewportArea.innerHTML = html;
    } catch (err) {
      console.error('Critical error in renderLessonCockpit:', err);
      if (viewportArea) {
        viewportArea.innerHTML = `
          <div style="padding:40px 20px; text-align:center; background:#ffffff; border-radius:16px; margin:20px; box-shadow:0 4px 20px rgba(0,0,0,0.06);">
            <div style="font-size:2.5rem; margin-bottom:12px;">⚠️</div>
            <h3 style="font-weight:800; color:#dc2626; margin-bottom:8px;">تنبيه: حدث تعذر في تحميل الدرس</h3>
            <p style="color:#64748b; font-size:0.9rem; margin-bottom:16px;">يرجى النقر على زر إعادة التهيئة لتحديث العرض فوراً.</p>
            <button type="button" class="nav-btn primary" onclick="window.Platform.selectLesson('g6-t1-c1-l1')">🔄 إعادة تحميل الدرس</button>
          </div>
        `;
      }
    }
  }

  // Fallback for roadmap lessons
  function renderUnfinishedLessonPlaceholder(lessonId) {
    viewportArea.innerHTML = `
      <div class="objectives-card" style="text-align:center; padding:48px 24px;">
        <span style="font-size:3.5rem;">🏗️</span>
        <h2 style="font-size:1.6rem; font-weight:800; margin:16px 0 8px 0;">هذا الدرس مدرج في الخطة التعليمية وجاهز للتوسعة</h2>
        <p style="color:var(--text-muted); max-width:600px; margin:0 auto 24px auto;">
          تم تسجيل هذا الدرس بكافة معاييره وتصنيفه الهيكلي حسب الفصلين الدراسيين (الأول والثاني). يمكنك استخدام "استوديو إضافة المناهج" لإدراج محتوى هذا الدرس أو اختباراته مباشرة!
        </p>
        <div style="display:flex; gap:10px; justify-content:center;">
          <button class="nav-btn primary" onclick="window.Platform.switchView('builder')">➕ إضافة محتوى الدرس الآن</button>
          <button class="nav-btn" onclick="window.Platform.selectLesson('g6-t1-c4-l1')">الرجوع للدروس المكتملة</button>
        </div>
      </div>
    `;
  }

  // ================= Socratic Platform & Interactive Tools Panes =================
  function renderSocraticPane(lesson, isG6) {
    const s = lesson.socratic || {};
    const dialogue = s.dialogue || [];
    const probing = s.probing_questions || [];
    const mb = s.misconception_buster || {};

    return `
      <div class="socratic-container">
        <!-- Header Banner -->
        <div class="socratic-header-card">
          <div class="socratic-badge-pill">🏛️ منصة سقراط التوليدية • الحوار والاستقصاء المعرفي</div>
          <h3 class="socratic-main-title">الدرس ${fmtNum(lesson.number, isG6)}: ${lesson.title}</h3>
          <p class="socratic-lead">حوار فلسفي استقصائي يقود المتعلم لاكتشاف المفهوم وتصحيح التصورات البديلة عبر التفكير الناقد والبرهان المنطقي.</p>
        </div>

        <!-- Generating Inquiry Question -->
        <div class="socratic-card inquiry-box">
          <div class="socratic-card-header">
            <span class="socratic-icon">❓</span>
            <h4>السؤال التوليدي الاستقصائي للدرس</h4>
          </div>
          <div class="socratic-card-body inquiry-text">
            ${fmtNum(s.inquiry_question || 'كيف يمثل هذا الدرس مدخلاً لفهم النماذج الرياضية في واقع الحياة؟', isG6)}
          </div>
        </div>

        <!-- Conceptual Dilemma -->
        ${s.conceptual_dilemma ? `
          <div class="socratic-card dilemma-box">
            <div class="socratic-card-header">
              <span class="socratic-icon">⚡</span>
              <h4>المأزق المفاهيمي (Cognitive Dissonance)</h4>
            </div>
            <div class="socratic-card-body dilemma-text">
              ${fmtNum(s.conceptual_dilemma, isG6)}
            </div>
          </div>
        ` : ''}

        <!-- Multi-Turn Socratic Dialogue -->
        <div class="socratic-card dialogue-box">
          <div class="socratic-card-header">
            <span class="socratic-icon">💬</span>
            <h4>الحوار السقراطي المعياري الموجه</h4>
          </div>
          <div class="socratic-dialogue-list">
            ${dialogue.map(turn => `
              <div class="dialogue-turn ${turn.role || 'teacher'}">
                <div class="turn-avatar">${turn.avatar || (turn.role === 'teacher' ? '🏛️' : '🎓')}</div>
                <div class="turn-bubble">
                  <div class="turn-speaker">${turn.speaker}</div>
                  <div class="turn-content">${fmtNum(turn.text, isG6)}</div>
                </div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Probing Questions -->
        ${probing.length ? `
          <div class="socratic-card probing-box">
            <div class="socratic-card-header">
              <span class="socratic-icon">🔍</span>
              <h4>أسئلة السبر والتعميق المعرفي للحوار الصفي</h4>
            </div>
            <div class="socratic-probing-list">
              ${probing.map((q, idx) => `
                <div class="probing-item">
                  <span class="probing-num">${fmtNum(idx + 1, true)}</span>
                  <span>${fmtNum(q, isG6)}</span>
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        <!-- Misconception Buster -->
        ${mb.misconception ? `
          <div class="socratic-card buster-box">
            <div class="socratic-card-header">
              <span class="socratic-icon">🛡️</span>
              <h4>مفكك المفاهيم الخاطئة (Misconception Buster)</h4>
            </div>
            <div class="socratic-card-body buster-grid">
              <div class="buster-side wrong">
                <div class="buster-title">❌ الفهم الخاطئ الشائع:</div>
                <div>${fmtNum(mb.misconception, isG6)}</div>
              </div>
              <div class="buster-side right">
                <div class="buster-title">✓ التصحيح والبرهان الرياضي:</div>
                <div>${fmtNum(mb.correction, isG6)}</div>
              </div>
            </div>
          </div>
        ` : ''}

        <!-- Standalone Interactive Socratic Session Link for Students -->
        <div class="socratic-card socratic-student-share-card">
          <div class="socratic-card-header" style="align-items:flex-start;">
            <span class="socratic-icon" style="background:#eff6ff; font-size:1.8rem; padding:8px; border-radius:10px; border:1px solid #bfdbfe;">🚀</span>
            <div style="flex:1;">
              <h4 style="font-size:1.15rem; font-weight:800; color:#1e3a8a; margin-bottom:4px;">رابط جلسة التعلّم السقراطي التفاعلية للطالب</h4>
              <p style="font-size:0.86rem; color:var(--text-muted); line-height:1.6;">رابط تفاعلي مستقل وخاص بهذا الدرس يمكن نسخه وإرساله للطالب (عبر واتساب / كلاس روم / تيمز / منصة مدرستي) لدراسة الدرس ذاتياً عبر الحوار السقراطي وتفكيك المفاهيم الخاطئة والحصول على بطاقة إتقان معتمدة.</p>
            </div>
          </div>
          <div class="socratic-share-actions-row">
            <div class="socratic-url-display" title="رابط جلسة الطالب التفاعلية">
              <span>socratic_session.html?lesson=${encodeURIComponent(lesson.id)}</span>
            </div>
            <div class="socratic-share-btns">
              <button type="button" class="nav-btn primary" onclick="window.Platform.copySocraticStudentLink('${lesson.id}')">
                📋 <span>نسخ رابط الطالب للمشاركة</span>
              </button>
              <button type="button" class="nav-btn success" onclick="window.Platform.openCurrentLessonHtmlGenerator()">
                🌐 <span>مولد صفحة HTML التفاعلية</span>
              </button>
              <a href="socratic_session.html?lesson=${encodeURIComponent(lesson.id)}" target="_blank" class="nav-btn" style="background:#ffffff; border:1.5px solid #cbd5e1; color:#0f172a; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
                🔗 <span>فتح الجلسة التفاعلية ↗</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  function renderLessonToolsPane(lesson, isG6) {
    const tools = lesson.lesson_tools || {};
    const features = tools.features || [];
    const actions = tools.quick_actions || [];
    const toolUrl = getRelevantToolFile(lesson.id);

    return `
      <div class="lesson-tools-container">
        <!-- Tools Header Banner -->
        <div class="tools-header-card" style="background:var(--bg-card); border:1px solid var(--border-light); border-radius:12px; padding:18px 20px; margin-bottom:16px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px;">
            <div>
              <div class="socratic-badge-pill" style="background:#eff6ff; color:#1e40af; border:1px solid #bfdbfe;">🛠️ ${tools.widget_badge || 'بيئة التعلم الرقمية والمختبر النشط'}</div>
              <h3 style="font-size:1.25rem; font-weight:800; margin:6px 0; color:var(--text-main);">${tools.title || ('مختبر ' + lesson.title)}</h3>
              <p style="color:var(--text-muted); font-size:0.92rem; max-width:700px;">${tools.description || 'أداة تفاعلية مخصصة تدمج النمذجة البصرية بالاستقصاء الرياضي النشط.'}</p>
            </div>
            <div>
              <a href="${toolUrl}" target="_blank" class="nav-btn primary">
                ↗️ فتح الأداة في شاشة كاملة
              </a>
            </div>
          </div>

          <!-- Quick Action Buttons -->
          ${actions.length ? `
            <div class="tools-actions-bar" style="display:flex; gap:8px; flex-wrap:wrap; margin-top:14px; border-top:1px solid var(--border-light); padding-top:12px;">
              ${actions.map(act => `
                <button class="nav-btn" type="button" onclick="window.Platform.runToolAction('${act.id}', '${lesson.id}')">
                  <span>${act.icon}</span>
                  <span>${act.label}</span>
                </button>
              `).join('')}
            </div>
          ` : ''}
        </div>

        <!-- Features Grid -->
        ${features.length ? `
          <div class="tools-features-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:10px; margin-bottom:16px;">
            ${features.map(f => `
              <div style="background:var(--bg-card); border:1px solid var(--border-light); border-radius:8px; padding:10px 14px; font-size:0.88rem; display:flex; align-items:center; gap:8px;">
                <span style="color:var(--primary); font-weight:bold;">✦</span>
                <span>${f}</span>
              </div>
            `).join('')}
          </div>
        ` : ''}

        <!-- Interactive Whiteboard & Tool IFrame -->
        <div class="tool-embed-container">
          <iframe class="tool-embed-iframe" src="${toolUrl}" title="${tools.title || 'المختبر التفاعلي'}"></iframe>
        </div>
      </div>
    `;
  }

  function runToolAction(actionId, lessonId) {
    const lesson = window.CURRICULUM_DATA.lessons[lessonId];
    if (!lesson) return;
    const tools = lesson.lesson_tools || {};
    if (actionId === 'whiteboard') {
      window.open('عرض_السبورة_التفاعلي_الشامل_المثلثات_SSS_SAS.html', '_blank');
    } else if (actionId === 'simulate') {
      const url = getRelevantToolFile(lessonId);
      window.open(url, '_blank');
    } else if (actionId === 'generate') {
      alert(`🎯 تم توليد مسألة استقصائية جديدة لدرس: ${lesson.title}!\nيمكنك الآن استكشاف الحل ومناقشته في منصة سقراط.`);
    } else {
      const url = getRelevantToolFile(lessonId);
      window.open(url, '_blank');
    }
  }

  // Determine relevant micro-app file based on lesson ID
  function getRelevantToolFile(lessonId) {
    if (lessonId.startsWith('g6')) return 'منصة_سقراط_للرياضيات_سادس_ابتدائي.html';
    if (lessonId.startsWith('g1s')) return 'عرض_السبورة_التفاعلي_الشامل_المثلثات_SSS_SAS.html';
    if (lessonId.startsWith('g3m')) return 'صيغ_معادلة_المستقيم_حقيبة_تفاعلية.html';
    return 'منصة_سقراط_للرياضيات_سادس_ابتدائي.html';
  }

  // ================= Quiz Logic =================
  function answerMCQ(qIdx, optIdx) {
    const isApproved = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isApproved === 'function' && window.FirebaseAuthManager.isApproved();
    const isAdmin = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isAdmin === 'function' && window.FirebaseAuthManager.isAdmin();
    if (!isApproved && !isAdmin && qIdx >= 5) {
      if (window.FirebaseAuthManager && window.FirebaseAuthManager.showToast) {
        window.FirebaseAuthManager.showToast(`عفواً، الأسئلة من س ${fmtNum(6, true)} إلى س ${fmtNum(10, true)} وبقية الاختبار المقنن متاحة حصرياً للأعضاء المعتمدين والمدير العام.`, 'warning');
      }
      return;
    }

    const lesson = window.CURRICULUM_DATA.lessons[state.currentLessonId];
    if (!lesson) return;
    const mcq = lesson.quiz.mcq[qIdx];
    if (!mcq) return;

    if (!state.quizScores[lesson.id]) {
      state.quizScores[lesson.id] = { answeredCount: 0, correctCount: 0, userAnswers: {} };
    }
    const qState = state.quizScores[lesson.id];
    if (qState.userAnswers['mcq-' + qIdx] !== undefined) return; // already answered

    qState.userAnswers['mcq-' + qIdx] = optIdx;
    qState.answeredCount++;
    if (optIdx === mcq.correct) {
      qState.correctCount++;
    }

    renderLessonCockpit();
  }

  function answerTF(qIdx, boolAns) {
    const isApproved = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isApproved === 'function' && window.FirebaseAuthManager.isApproved();
    const isAdmin = window.FirebaseAuthManager && typeof window.FirebaseAuthManager.isAdmin === 'function' && window.FirebaseAuthManager.isAdmin();
    if (!isApproved && !isAdmin && qIdx >= 5) {
      if (window.FirebaseAuthManager && window.FirebaseAuthManager.showToast) {
        window.FirebaseAuthManager.showToast('عفواً، الأسئلة بعد السؤال الخامس متاحة حصرياً للأعضاء المعتمدين والمدير العام.', 'warning');
      }
      return;
    }

    const lesson = window.CURRICULUM_DATA.lessons[state.currentLessonId];
    if (!lesson) return;
    const tf = lesson.quiz.tf[qIdx];
    if (!tf) return;

    if (!state.quizScores[lesson.id]) {
      state.quizScores[lesson.id] = { answeredCount: 0, correctCount: 0, userAnswers: {} };
    }
    const qState = state.quizScores[lesson.id];
    if (qState.userAnswers['tf-' + qIdx] !== undefined) return;

    qState.userAnswers['tf-' + qIdx] = boolAns;
    qState.answeredCount++;
    if (boolAns === tf.is_true) {
      qState.correctCount++;
    }

    renderLessonCockpit();
  }

  function resetQuiz(lessonId) {
    if (state.quizScores[lessonId]) {
      delete state.quizScores[lessonId];
    }
    renderLessonCockpit();
  }

  // Toggle Worksheet Solution
  function toggleWsSolution(id) {
    const el = document.getElementById(id);
    if (el) el.classList.toggle('open');
  }

  function toggleAllSolutions() {
    document.querySelectorAll('.ws-solution-box').forEach(box => {
      box.classList.toggle('open');
    });
  }

  function triggerFlashTransition() {
    const flashBar = document.getElementById('nav-flash-bar');
    if (flashBar) {
      flashBar.classList.remove('flash-active');
      void flashBar.offsetWidth;
      flashBar.classList.add('flash-active');
    }
    const container = document.getElementById('view-container');
    if (container) {
      container.classList.remove('flash-enter');
      void container.offsetWidth;
      container.classList.add('flash-enter');
    }
  }

  function switchLessonTab(tabName) {
    state.activeLessonTab = tabName;
    triggerFlashTransition();
    renderLessonCockpit();
    setTimeout(() => {
      const targetPane = document.getElementById('tab-' + tabName) || document.querySelector('.lesson-nav-tabs');
      if (targetPane && typeof targetPane.scrollIntoView === 'function') {
        targetPane.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 40);
  }

  function switchView(viewName) {
    state.activeView = viewName;
    document.querySelectorAll('.view-tab-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.view === viewName);
    });
    triggerFlashTransition();
    renderCurrentView();
  }

  // ================= Visual Tree View =================
  function renderVisualTree() {
    const stages = window.CURRICULUM_DATA.stages || [];
    let html = `
      <div class="visual-tree-container">
        <div class="tree-canvas-header">
          <div>
            <h2 style="font-size:1.4rem; font-weight:800; color:var(--text-main);">🗺️ خريطة المناهج الدراسية التفاعلية الكاملة</h2>
            <p style="color:var(--text-muted); font-size:0.9rem;">استعراض هيكلي شامل لكافة المراحل والصفوف الدراسية والفصول الثلاثة والأبواب والدروس:</p>
          </div>
          <button class="nav-btn primary" onclick="window.print()">🖨️ طباعة المخطط الهيكلي</button>
        </div>
        <div class="tree-chart-wrapper">
    `;

    stages.forEach(stage => {
      html += `
        <div style="margin-bottom:32px; background:var(--bg-page); border:1px solid var(--border-light); border-radius:var(--radius-lg); padding:20px;">
          <h3 style="font-size:1.2rem; font-weight:800; color:#1e3a8a; margin-bottom:16px;">${stage.icon} ${stage.name}</h3>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
      `;

      stage.grades.forEach(grade => {
        html += `
          <div class="tree-node-card">
            <h4 style="font-size:1.05rem; font-weight:800; color:var(--text-main); margin-bottom:8px;">🎓 ${grade.name}</h4>
            <div style="display:flex; flex-direction:column; gap:6px;">
        `;

        grade.terms.forEach(term => {
          if (state.termFilter !== 'all' && term.id !== state.termFilter) return;
          const chapters = term.chapters || [];
          html += `
            <div style="background:var(--bg-card); border-right:3px solid #3b82f6; padding:8px 12px; border-radius:6px;">
              <div style="font-weight:700; font-size:0.85rem; color:#1e40af; margin-bottom:4px;">${term.icon || '📅'} ${term.name}</div>
              <div style="font-size:0.78rem; color:var(--text-muted);">
                ${chapters.map(ch => `<span style="display:block; padding:2px 0;">• ${ch.number}: ${ch.title}</span>`).join('')}
              </div>
            </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      html += `
          </div>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;

    viewportArea.innerHTML = html;
  }

  // ================= Specialized Suites View =================
  function renderSuitesView() {
    const tools = window.CURRICULUM_DATA.tools || [];
    let html = `
      <div class="visual-tree-container">
        <div class="tree-canvas-header">
          <div>
            <h2 style="font-size:1.4rem; font-weight:800; color:var(--text-main);">🌟 الأجنحة والأدوات التفاعلية المدمجة</h2>
            <p style="color:var(--text-muted); font-size:0.9rem;">مختبرات الذكاء الاصطناعي والسبورات الذكية وميادين المسابقات وسجلات المتابعة:</p>
          </div>
        </div>
        <div class="vault-grid">
          ${tools.map(tool => `
            <div class="vault-item-card">
              <div>
                <div style="font-size:2.2rem; margin-bottom:10px;">${tool.icon}</div>
                <h3 style="font-size:1.15rem; font-weight:800; color:var(--text-main); margin-bottom:6px;">${tool.title}</h3>
                <span class="meta-badge" style="margin-bottom:10px;">${tool.target}</span>
                <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.6;">${tool.desc}</p>
              </div>
              <div style="display:flex; gap:8px;">
                <a href="${tool.file}" target="_blank" class="nav-btn primary" style="flex:1; justify-content:center;">
                  🚀 تشغيل الأداة
                </a>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    viewportArea.innerHTML = html;
  }

  // ================= Vault & PDF Downloads View =================
  function renderVaultView() {
    const downloads = window.CURRICULUM_DATA.vault_downloads || [];
    let html = `
      <div class="visual-tree-container">
        <div class="tree-canvas-header">
          <div>
            <h2 style="font-size:1.4rem; font-weight:800; color:var(--text-main);">📥 مركز التحميل والطباعة (PDF Vault)</h2>
            <p style="color:var(--text-muted); font-size:0.9rem;">تحميل وتصفح الحقائب الشاملة وسجلات المتابعة والشهادات الرسمية بجودة طباعة كاملة:</p>
          </div>
        </div>
        <div class="vault-grid">
          ${downloads.map(item => `
            <div class="vault-item-card">
              <div>
                <span class="meta-badge green" style="margin-bottom:8px;">${item.badge}</span>
                <h3 style="font-size:1.05rem; font-weight:800; color:var(--text-main); line-height:1.5;">${item.title}</h3>
              </div>
              <div style="display:flex; gap:8px;">
                <a href="${item.pdf}" download class="nav-btn primary" style="flex:1; justify-content:center;">
                  📥 تحميل PDF
                </a>
                <a href="${item.html}" target="_blank" class="nav-btn" style="flex:1; justify-content:center;">
                  🌐 معاينة الويب
                </a>
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;
    viewportArea.innerHTML = html;
  }

  // ================= Builder View =================
  function renderBuilderView() {
    let html = `
      <div class="objectives-card">
        <div class="card-section-title">
          <span>➕ استوديو توسيع المناهج وإدراج الدروس الجديدة</span>
        </div>
        <p style="color:var(--text-muted); font-size:0.92rem; margin-bottom:20px;">
          يتيح هذا الاستوديو للمعلم (أ. محمد عبدالله جمعة) إدراج وحدات ودروس جديدة في الخطة الدراسية مع خططها وأسئلتها وحفظها محلياً:
        </p>
        <form onsubmit="window.Platform.saveNewLesson(event)" style="display:flex; flex-direction:column; gap:16px; max-width:700px;">
          <div>
            <label style="display:block; font-weight:700; font-size:0.88rem; margin-bottom:6px;">الصف والمرحلة الدراسية:</label>
            <select id="new-lesson-grade" style="width:100%; padding:10px; border-radius:8px; border:1px solid var(--border-light);">
              <option value="g6">الصف السادس الابتدائي</option>
              <option value="g1m">الصف الأول المتوسط</option>
              <option value="g2m">الصف الثاني المتوسط</option>
              <option value="g3m">الصف الثالث المتوسط</option>
              <option value="g1s">الصف الأول الثانوي (مسارات)</option>
              <option value="g2s">الصف الثاني الثانوي (مسارات)</option>
              <option value="g3s">الصف الثالث الثانوي (مسارات)</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:0.88rem; margin-bottom:6px;">الفصل الدراسي:</label>
            <select id="new-lesson-term" style="width:100%; padding:10px; border-radius:8px; border:1px solid var(--border-light);">
              <option value="term1">الفصل الدراسي الأول</option>
              <option value="term2">الفصل الدراسي الثاني</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:0.88rem; margin-bottom:6px;">عنوان الدرس الجديد:</label>
            <input id="new-lesson-title" type="text" placeholder="مثال: الدرس ٥-١: مساحة المثلث" required style="width:100%; padding:10px; border-radius:8px; border:1px solid var(--border-light);">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:0.88rem; margin-bottom:6px;">أهداف الدرس (كل هدف في سطر):</label>
            <textarea id="new-lesson-objectives" rows="4" placeholder="الهدف الأول...&#10;الهدف الثاني..." style="width:100%; padding:10px; border-radius:8px; border:1px solid var(--border-light);"></textarea>
          </div>
          <button type="submit" class="nav-btn primary" style="padding:12px; font-size:1rem; justify-content:center;">
            💾 حفظ الدرس وإدراجه في الخطة
          </button>
        </form>
      </div>
    `;
    viewportArea.innerHTML = html;
  }

  function saveNewLesson(e) {
    e.preventDefault();
    const title = document.getElementById('new-lesson-title').value.trim();
    const grade = document.getElementById('new-lesson-grade').value;
    const term = document.getElementById('new-lesson-term').value;
    const objsText = document.getElementById('new-lesson-objectives').value.trim();
    const objs = objsText.split('\n').filter(o => o.trim());

    const newId = `custom-${Date.now()}`;
    const newLessonObj = {
      id: newId,
      number: 'جديد',
      title: title,
      grade: grade,
      term: term,
      chapter: 'وحدة مضافة حديثاً',
      pages: 'ص مخصصة',
      status: 'completed',
      badge: 'مضاف حديثاً',
      objectives: objs.length ? objs : ['تحقيق إتقان المفاهيم الرياضية المستهدفة.'],
      plan_5es: {
        engage: 'تهيئة جاذبة لربط المفاهيم.',
        explore: 'استقصاء تعاوني.',
        explain: 'تفسير القوانين.',
        elaborate: 'ربط حياتي وتطبيقات.',
        evaluate: 'تقويم ختامي.'
      },
      summary: {
        concept: title,
        methods: ['مراجعة القوانين والتمارين'],
        golden_rule: 'الدقة والتدريب المستمر يصنعان التميز الرياضي.',
        solved_example: 'تطبيق تدريبي مباشر.'
      },
      worksheet: {
        title: `ورقة عمل: ${title}`,
        questions: [{"q": "مسألة تدريبية أولى", "ans": "إجابة المسألة الأولى"}]
      },
      quiz: {
        mcq: [
          {
            "q": `السؤال الأول حول ${title}:`,
            "options": ["خيار أ", "خيار ب", "خيار ج", "خيار د"],
            "correct": 0,
            "explanation": "الشرح والتفسير الرياضي."
          }
        ],
        tf: [
          {
            "statement": "هذه العبارة الرياضية صحيحة.",
            "is_true": true,
            "explanation": "تفسير الصواب والخطأ."
          }
        ]
      }
    };

    window.CURRICULUM_DATA.lessons[newId] = newLessonObj;
    alert('تم حفظ وإدراج الدرس الجديد بنجاح في الخطة الدراسية!');
    selectLesson(newId);
  }

  function toggleTheme() {
    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) themeBtn.click();
  }

  // Export Platform API
  window.Platform = {
    selectLesson,
    toggleNode,
    expandAll,
    collapseAll,
    toggleSidebar,
    closeSidebarMobile,
    toggleMobileNav,
    closeMobileNav,
    openCurrentLessonHtmlGenerator,
    toggleTheme,
    goToPrevLesson,
    goToNextLesson,
    toggleCrumbDropdown,
    selectFirstLessonOfStage,
    selectFirstLessonOfGrade,
    selectFirstLessonOfTerm,
    selectFirstLessonOfChapter,
    switchLessonTab,
    switchView,
    answerMCQ,
    answerTF,
    resetQuiz,
    toggleWsSolution,
    toggleAllSolutions,
    saveNewLesson,
    copyLessonQuestionToWord,
    copySocraticStudentLink,
    toggleLessonQuestionInExam,
    addAllLessonQuestionsToExam,
    openImageLightbox,
    closeImageLightbox,
    runToolAction,
    findLessonPath,
    renderCurrentView
  };

})();
