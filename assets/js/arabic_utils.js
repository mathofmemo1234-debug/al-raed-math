/**
 * ==========================================================================
 * أدوات اللغة العربية، الأرقام العربية المشرقية (٠-٩)، والنسخ النظيف إلى Word
 * منصة الرائد التعليمية الذكية للرياضيات | الصف السادس الابتدائي
 * ==========================================================================
 */

(function (global) {
  'use strict';

  const EASTERN_DIGITS = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'];
  const EASTERN_TO_WESTERN_MAP = {
    '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
    '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9',
    '٫': '.'
  };
  const CHOICE_LETTERS = ['أ', 'ب', 'ج', 'د', 'هـ', 'و'];
  const WORD_CHOICE_LETTERS = ['أ', 'ب', 'جـ', 'د', 'هـ', 'و'];
  const SECONDARY_CHOICE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F'];
  const RLM = '\u200F';
  const LRM = '\u200E';
  const _clipboardImageCache = Object.create(null);

  /**
   * فحص ما إذا كان السياق أو الكتاب أو الدرس ينتمي إلى المرحلة الثانوية
   * حيث تعتمد المرحلة الثانوية الأرقام الإنجليزية حصراً واتجاه LTR للمعادلات
   */
  function isSecondaryStage(val) {
    if (!val) return false;
    if (typeof val === 'string') {
      return (
        val === 'g1s' || val === '1s' ||
        val === 'g2s' || val === '2s' ||
        val === 'secondary' || val === 'المرحلة الثانوية' ||
        val.startsWith('g1s') || val.startsWith('g2s')
      );
    }
    if (typeof val === 'object') {
      if (val.isSecondary || val.secondary) return true;
      if (val.id && (val.id === 'g1s' || val.id.startsWith('g1s') || val.id === 'g2s' || val.id.startsWith('g2s'))) return true;
      if (val.bookId && (val.bookId === 'g1s' || val.bookId === '1s' || val.bookId === 'g2s' || val.bookId === '2s')) return true;
      if (val.gradeId && (val.gradeId === 'g1s' || val.gradeId === '1s' || val.gradeId === 'g2s' || val.gradeId === '2s')) return true;
      if (val.lessonId && (val.lessonId.startsWith('g1s') || val.lessonId.startsWith('g2s'))) return true;
      if (val.stage && (val.stage === 'المرحلة الثانوية' || val.stage.includes('ثانوي'))) return true;
      if (val.grade && val.grade.includes('الثانوي')) return true;
    }
    return false;
  }

  /**
   * تحويل جميع الأرقام الإنجليزية (0-9) إلى أرقام عربية مشرقية (٠-٩)
   * وتحويل الفاصلة العشرية النقطية بين الأرقام إلى (٫)
   */
  function toEasternDigits(input) {
    if (input === null || input === undefined) return '';
    let str = String(input);
    // تحويل النقطة العشرية بين رقمين إلى فاصلة عربية مشرقية ٫
    str = str.replace(/(?<=[0-9٠-٩])\.(?=[0-9٠-٩])/g, '٫');
    return str.replace(/[0-9]/g, function (d) {
      return EASTERN_DIGITS[Number(d)];
    });
  }

  /**
   * تحويل جميع الأرقام العربية المشرقية (٠-٩) والفاصلة (٫) إلى أرقام إنجليزية (0-9)
   * معتمد حصراً في المرحلة الثانوية
   */
  function toWesternDigits(input) {
    if (input === null || input === undefined) return '';
    return String(input).replace(/[٠-٩٫]/g, function (ch) {
      return EASTERN_TO_WESTERN_MAP[ch] || ch;
    });
  }

  /**
   * تنسيق الأرقام وفق المرحلة الدراسية: إنجليزية للثانوية ومشرقية للابتدائية والمتوسطة
   */
  function formatStageDigits(input, isSecondary) {
    return isSecondary ? toWesternDigits(input) : toEasternDigits(input);
  }

  const UNICODE_SUP_TO_EASTERN_MAP = {
    '⁰': '٠', '¹': '١', '²': '٢', '³': '٣', '⁴': '٤',
    '⁵': '٥', '⁶': '٦', '⁷': '٧', '⁸': '٨', '⁹': '٩',
    '⁺': '+', '⁻': '-'
  };
  const UNICODE_SUP_TO_WESTERN_MAP = {
    '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
    '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
    '⁺': '+', '⁻': '-'
  };
  const PAT_BASE_SUP_JS = /(\((?:[^()<>]|\([^()<>]*\))+\)|[٠-٩0-9]+|[أ-ي]+)\s*([⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+)/g;
  const PAT_CARET_JS = /(\((?:[^()<>]|\([^()<>]*\))+\)|[٠-٩0-9]+|[أ-ي]+)\s*\^\s*([+\-]?[٠-٩0-9]+)/g;

  const WESTERN_TO_SUP_MAP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '٠': '⁰', '١': '¹', '٢': '²', '٣': '³', '٤': '⁴', '٥': '⁵', '٦': '⁶', '٧': '⁷', '٨': '⁸', '٩': '⁹',
    '+': '⁺', '-': '⁻', 'n': 'ⁿ'
  };
  const WESTERN_TO_SUBSCRIPT_MAP = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉'
  };

  /** تحويل الأس إلى رموز علوية مألوفة للنص العادي (x² بدلاً من x^2) */
  function toSuperscriptText(exp) {
    const e = String(exp || '').trim();
    const chars = Array.from(e);
    if (chars.length && chars.every(function (c) { return WESTERN_TO_SUP_MAP[c]; })) {
      return chars.map(function (c) { return WESTERN_TO_SUP_MAP[c]; }).join('');
    }
    return '^(' + e + ')';
  }

  /** تحويل المؤشر السفلي إلى رموز سفلية مألوفة للنص العادي (x₁ بدلاً من x_1) */
  function toSubscriptText(sub) {
    const s = String(sub || '').trim();
    const chars = Array.from(s);
    if (chars.length && chars.every(function (c) { return WESTERN_TO_SUBSCRIPT_MAP[c] || (EASTERN_TO_WESTERN_MAP[c] && WESTERN_TO_SUBSCRIPT_MAP[EASTERN_TO_WESTERN_MAP[c]]); })) {
      return chars.map(function (c) {
        const w = EASTERN_TO_WESTERN_MAP[c] || c;
        return WESTERN_TO_SUBSCRIPT_MAP[w] || c;
      }).join('');
    }
    return '_' + s;
  }

  /**
   * المؤشرات السفلية في المرحلتين الابتدائية والمتوسطة: (ص٢ - ص١) ÷ (س٢ - س١) ، م١ × م٢ ، م_العمودي
   * تُكتب الأرقام مصغرة أسفل المتغير كما في الكتاب المدرسي، ولا تُطبق إلا في سياق رياضي
   */
  const AR_SUB_CONTEXT = /[=÷×≠]|\(\s*[سص][٠-٩0-9]/;
  function markArabicSubscripts(s) {
    if (!s) return s;
    s = s.replace(/(^|[\s(،,{=\-+×÷])([سصمبعلن])_([\u0621-\u064A]+|[٠-٩0-9]+)/g, function (_, pre, v, sub) {
      return pre + v + '<sub class="ar-sub">' + toEasternDigits(sub) + '</sub>';
    });
    if (!AR_SUB_CONTEXT.test(s)) return s;
    return s.replace(/(^|[\s(،,{=\-+×÷])([سصمبعلن])([٠-٩0-9])(?=$|[\s)،,}=\-+×÷.:؛])/g, function (_, pre, v, d) {
      return pre + v + '<sub class="ar-sub">' + toEasternDigits(d) + '</sub>';
    });
  }

  /**
   * صياغة القوة والأس الرياضي باللغة العربية:
   * الأس دائماً على يسار الأساس وبالأرقام العربية المشرقية فقط (٠-٩)
   */
  function formatArabicExponent(base, exp) {
    const safeBase = toEasternDigits(String(base || '').trim());
    const safeExp = toEasternDigits(String(exp || '').trim());
    return '<span class="ar-pow"><span class="ar-base">' + safeBase + '</span><sup class="ar-exp">' + safeExp + '</sup></span>';
  }

  /**
   * صياغة القوة والأس للمرحلة الثانوية (LTR بالأرقام الإنجليزية 0-9)
   */
  function formatSecondaryExponent(base, exp) {
    const safeBase = toWesternDigits(String(base || '').trim());
    const safeExp = toWesternDigits(String(exp || '').trim());
    return '<span class="sec-pow" dir="ltr"><span class="sec-base">' + safeBase + '</span><sup class="sec-exp">' + safeExp + '</sup></span>';
  }

  /**
   * استدعاء مكتبة KaTeX سواء كانت محملة في المتصفح أو في بيئة Node.js
   */
  function getKatex() {
    if (typeof global !== 'undefined' && global.katex) return global.katex;
    if (typeof window !== 'undefined' && window.katex) return window.katex;
    try {
      if (typeof require === 'function') {
        return require('./assets/vendor/katex/katex.min.js');
      }
    } catch (e) {
      try {
        if (typeof require === 'function') {
          return require('../assets/vendor/katex/katex.min.js');
        }
      } catch (e2) {}
    }
    return null;
  }

  /**
   * صياغة وتصيير المصفوفات والمحددات ثنائية الأبعاد (2D) بدقة بصرية ورياضية فائقة
   */
  function parseLegacyMatrixRows(content) {
    if (!content) return null;
    const str = String(content);
    const rowMatches = str.match(/<span\s+class=["']sec-row["']>([\s\S]*?)<\/span>/gi);
    if (rowMatches && rowMatches.length > 0) {
      return rowMatches.map(function (rHtml) {
        const inner = rHtml.replace(/<\/?span\b[^>]*>/gi, '').replace(/&nbsp;/g, ' ').replace(/&minus;/g, '-').trim();
        return inner.split(/\s+/).filter(Boolean);
      });
    }
    const clean = str.replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&minus;/g, '-').trim();
    if (clean.indexOf(';') !== -1 || clean.indexOf(',') !== -1) {
      const sep = clean.indexOf(';') !== -1 ? ';' : ',';
      const rawRows = clean.split(sep);
      if (rawRows.length > 1) {
        return rawRows.map(function (r) {
          return r.trim().split(/\s+/).filter(Boolean);
        });
      }
    }
    return null;
  }

  function formatWordMatrixTable(rows, isDet, isSec) {
    if (!Array.isArray(rows) || !rows.length) return '';
    const cleanRows = rows.map(function (row) {
      return (Array.isArray(row) ? row : [row]).map(function (cell) {
        let c = String(cell != null ? cell : '').trim();
        return isSec !== false ? toWesternDigits(c) : toEasternDigits(c);
      });
    });
    const borderStyle = isDet
      ? 'border-left: 2pt solid #000; border-right: 2pt solid #000; border-top: none; border-bottom: none;'
      : 'border-left: 2pt solid #000; border-right: 2pt solid #000; border-top: none; border-bottom: none;';
    const rowsHtml = cleanRows.map(function (r) {
      const cellsHtml = r.map(function (c) {
        return '<td style="padding: 2pt 8pt; text-align: center; font-size: 11pt; font-family: \'Times New Roman\', serif; font-weight: bold; border: none;">' + c + '</td>';
      }).join('');
      return '<tr>' + cellsHtml + '</tr>';
    }).join('');
    return '<table dir="ltr" style="display: inline-table; vertical-align: middle; border-collapse: collapse; margin: 0 4pt; ' + borderStyle + '">' + rowsHtml + '</table>';
  }

  function format2DMatrixHtml(rows, isDet, isSec) {
    if (!Array.isArray(rows) || !rows.length) return '';
    const cleanRows = rows.map(function (row) {
      return (Array.isArray(row) ? row : [row]).map(function (cell) {
        let c = String(cell != null ? cell : '').trim();
        return isSec !== false ? toWesternDigits(c) : toEasternDigits(c);
      });
    });

    // 1. استخدام KaTeX في حال توفره للعرض المطبعي المثالي
    const katexLib = getKatex();
    if (katexLib && typeof katexLib.renderToString === 'function') {
      try {
        const env = isDet ? 'vmatrix' : 'bmatrix';
        const texBody = cleanRows.map(function (r) {
          return r.map(function (c) {
            return c.replace(/<[^>]+>/g, '').trim();
          }).join(' & ');
        }).join(' \\\\ ');
        const tex = '\\begin{' + env + '} ' + texBody + ' \\end{' + env + '}';
        return katexLib.renderToString(tex, { throwOnError: false, displayMode: false });
      } catch (e) {}
    }

    // 2. محرك العرض النقي Pure CSS كنسخة احتياطية مطابقة بنسبة 100%
    const containerClass = isDet ? 'sec-matrix-container sec-det-container' : 'sec-matrix-container sec-bracket-container';
    const borderLeft = isDet ? '<span class="sec-matrix-bar-left"></span>' : '<span class="sec-matrix-bracket-left"></span>';
    const borderRight = isDet ? '<span class="sec-matrix-bar-right"></span>' : '<span class="sec-matrix-bracket-right"><span class="m-r-hook-top"></span><span class="m-r-hook-bot"></span></span>';

    const rowsHtml = cleanRows.map(function (r) {
      const cellsHtml = r.map(function (c) {
        return '<span class="sec-matrix-cell">' + c + '</span>';
      }).join('');
      return '<span class="sec-matrix-row">' + cellsHtml + '</span>';
    }).join('');

    return '<span class="' + containerClass + '" dir="ltr">' +
      borderLeft +
      '<span class="sec-matrix-table">' + rowsHtml + '</span>' +
      borderRight +
      '</span>';
  }

  /**
   * تصيير صيغ وتعبيرات LaTeX الرياضية بدقة متقدمة
   */
  function renderLatexFormula(tex, isDisplay, isSec) {
    if (!tex) return '';
    let cleanTex = String(tex).trim();
    if (isSec !== false) {
      cleanTex = toWesternDigits(cleanTex);
    }
    const k = getKatex();
    if (k && typeof k.renderToString === 'function') {
      try {
        return k.renderToString(cleanTex, { throwOnError: false, displayMode: !!isDisplay });
      } catch (e) {}
    }
    // معالجة المصفوفات والمحددات بدون KaTeX
    const matMatch = cleanTex.match(/\\begin\{(vmatrix|bmatrix|pmatrix|matrix)\}([\s\S]*?)\\end\{\1\}/);
    if (matMatch) {
      const env = matMatch[1];
      const isDet = env === 'vmatrix';
      const rows = matMatch[2].trim().split('\\\\').map(function (r) {
        return r.split('&').map(function (c) { return c.trim(); });
      });
      return format2DMatrixHtml(rows, isDet, isSec !== false);
    }
    return '<span class="sec-math ltr-math" dir="ltr">' + cleanTex + '</span>';
  }

  function convertSecInnerMath(fragment) {
    if (fragment === null || fragment === undefined) return '';
    let s = toWesternDigits(String(fragment));
    // المؤشرات المكتوبة بشكل مسطح (x1, y2, m1) أو برموز يونيكود (x₁) تُوحّد إلى صيغة المؤشر السفلي
    s = s.replace(/([A-Za-z])([₀₁₂₃₄₅₆₇₈₉]+)/g, function (_, v, subs) {
      return v + '_' + Array.from(subs).map(function (c) { return String(c.charCodeAt(0) - 0x2080); }).join('');
    });
    s = s.replace(/(^|[^A-Za-z0-9_\-<\/"'=])([xym])([0-9])(?![A-Za-z0-9])/g, '$1$2_$3');
    const innerSaved = [];
    s = s.replace(/<span\s+class=["'][^"']*sec-pow[^"']*["'][^>]*>[\s\S]*?<\/span>|<sub\b[^>]*>[\s\S]*?<\/sub>/gi, function (tag) {
      const ph = '___SECINNER' + numToAlpha(innerSaved.length) + '___';
      innerSaved.push(tag);
      return ph;
    });

    // 1. تصيير بيئات LaTeX (المصفوفات والمحددات) وحفظها
    s = s.replace(/\\begin\{(vmatrix|bmatrix|pmatrix|matrix)\}[\s\S]*?\\end\{\1\}/g, function (m) {
      const ph = '___SECINNER' + numToAlpha(innerSaved.length) + '___';
      innerSaved.push(renderLatexFormula(m, false, true));
      return ph;
    });

    // 2. تصيير المحددات في التنسيق الموروث | <span class="sec-row">...</span> | وحفظها
    s = s.replace(/\|\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*\|/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      if (rows) {
        const ph = '___SECINNER' + numToAlpha(innerSaved.length) + '___';
        innerSaved.push(format2DMatrixHtml(rows, true, true));
        return ph;
      }
      return _;
    });

    // 3. تصيير المصفوفات في التنسيق الموروث وحفظها
    s = s.replace(/(?:<span\s+class=["']sec-brack["']>\[<\/span>|\[)\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*(?:<span\s+class=["']sec-brack["']>\]<\/span>|\])/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      if (rows) {
        const ph = '___SECINNER' + numToAlpha(innerSaved.length) + '___';
        innerSaved.push(format2DMatrixHtml(rows, false, true));
        return ph;
      }
      return _;
    });

    const escTextOnly = function (t) {
      return String(t)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    };

    const parts = [];
    const subAndPowStasher = function (htmlTag) {
      const ph = '___SECINBUILT' + numToAlpha(parts.length) + '___';
      parts.push(htmlTag);
      return ph;
    };

    s = s.replace(/(\((?:[^()<>]|\([^()<>]*\))+\)|[a-zA-Z₁₂₃₄₅₆₇₈₉₀]+|[0-9]+)\s*\^\s*([+\-]?[0-9a-zA-Z]+)/g, function (_, base, exp) {
      let b = base;
      if (/^\(/.test(b)) {
        b = b.replace(/(?<![A-Za-z_])([A-Za-z])_([A-Za-z0-9]+)(?![A-Za-z0-9_])/g, function (__, v, sub) {
          return v + subAndPowStasher('<sub class="sec-sub">' + escTextOnly(sub) + '</sub>');
        });
      }
      return subAndPowStasher(formatSecondaryExponent(b, exp));
    });

    s = s.replace(/(\((?:[^()<>]|\([^()<>]*\))+\)|[a-zA-Z₁₂₃₄₅₆₇₈₉₀]+|[0-9]+)\s*([⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+)/g, function (_, base, sups) {
      const expWestern = Array.from(sups).map(function (c) { return UNICODE_SUP_TO_WESTERN_MAP[c] || c; }).join('');
      let b = base;
      if (/^\(/.test(b)) {
        b = b.replace(/(?<![A-Za-z_])([A-Za-z])_([A-Za-z0-9]+)(?![A-Za-z0-9_])/g, function (__, v, sub) {
          return v + subAndPowStasher('<sub class="sec-sub">' + escTextOnly(sub) + '</sub>');
        });
      }
      return subAndPowStasher(formatSecondaryExponent(b, expWestern));
    });

    s = s.replace(/(?<![A-Za-z_])([A-Za-z])_([A-Za-z0-9]+)(?![A-Za-z0-9_])/g, function (_, v, sub) {
      return v + subAndPowStasher('<sub class="sec-sub">' + escTextOnly(sub) + '</sub>');
    });

    for (let i = parts.length - 1; i >= 0; i--) {
      const ph = '___SECINBUILT' + numToAlpha(i) + '___';
      s = s.split(ph).join(parts[i]);
    }
    for (let i = innerSaved.length - 1; i >= 0; i--) {
      const ph = '___SECINNER' + numToAlpha(i) + '___';
      s = s.split(ph).join(innerSaved[i]);
    }
    return s;
  }

  function formatMathExponents(input, isSecondary) {
    if (input === null || input === undefined) return '';
    let str = String(input);
    const sec = (isSecondary === true) || isSecondaryStage(isSecondary) || str.indexOf('sec-math') !== -1 || str.indexOf('ltr-math') !== -1 || str.indexOf('sec-pow') !== -1;
    if (sec) {
      return convertSecInnerMath(str);
    }
    str = str.replace(PAT_CARET_JS, function (_, base, exp) {
      return formatArabicExponent(base, exp);
    });
    str = str.replace(PAT_BASE_SUP_JS, function (_, base, sups) {
      const expEastern = Array.from(sups).map(function (c) { return UNICODE_SUP_TO_EASTERN_MAP[c] || c; }).join('');
      return formatArabicExponent(base, expEastern);
    });
    return str;
  }

  function numToAlpha(n) {
    let s = '';
    let num = n;
    do {
      s = String.fromCharCode(65 + (num % 26)) + s;
      num = Math.floor(num / 26) - 1;
    } while (num >= 0);
    return s;
  }

  function formatMathForWordHtml(input, opts) {
    if (input === null || input === undefined) return '';
    let s = String(input);
    const sec = (opts === true) || isSecondaryStage(opts) || s.indexOf('class="sec-math"') !== -1 || s.indexOf('class="ltr-math"') !== -1 || s.indexOf('class="sec-pow"') !== -1;

    if (s.indexOf('&lt;') !== -1 && (s.indexOf('ar-pow') !== -1 || s.indexOf('sec-pow') !== -1 || s.indexOf('span') !== -1 || s.indexOf('sup') !== -1 || s.indexOf('vmatrix') !== -1 || s.indexOf('bmatrix') !== -1)) {
      s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
    }

    // استبدال المحددات والمصفوفات بجداول Word المتوافقة
    s = s.replace(/\\begin\{(vmatrix|bmatrix|pmatrix|matrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
      const isDet = env === 'vmatrix';
      const rows = body.trim().split('\\\\').map(function (r) {
        return r.split('&').map(function (c) { return c.trim(); });
      });
      return formatWordMatrixTable(rows, isDet, sec);
    });

    s = s.replace(/\|\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*\|/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? formatWordMatrixTable(rows, true, sec) : _;
    });

    s = s.replace(/(?:<span\s+class=["']sec-brack["']>\[<\/span>|\[)\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*(?:<span\s+class=["']sec-brack["']>\]<\/span>|\])/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? formatWordMatrixTable(rows, false, sec) : _;
    });

    if (sec) {
      s = toWesternDigits(s);
      s = s.replace(/<span\s+class=["'][^"']*(?:sec-math|ltr-math)[^"']*["'][^>]*>([\s\S]*?)<\/span>/gi, function (_, inner) {
        const formatted = convertSecInnerMath(inner);
        return '<span dir="ltr" style="direction:ltr; unicode-bidi:isolate; font-family:\'Times New Roman\',serif; font-style:italic; font-weight:bold;">' + formatted + '</span>';
      });
      s = convertSecInnerMath(s);
      // الأسس والصيغ الإنجليزية للثانوي في Word
      s = s.replace(/<span\s+class=["'][^"']*(?:sec-pow|ar-pow)[^"']*["'][^>]*>\s*<span\s+class=["'][^"']*(?:sec-base|ar-base)[^"']*["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["'][^"']*(?:sec-exp|ar-exp)[^"']*["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        return '<span dir="ltr" style="direction:ltr; unicode-bidi:isolate; font-weight:bold;">' + base + '<sup style="font-size:75%; vertical-align:super;">' + exp + '</sup></span>';
      });
      s = s.replace(/<sub\b[^>]*>([\s\S]*?)<\/sub>/gi, function (_, subTxt) {
        return '<sub style="font-size:75%; vertical-align:sub;">' + subTxt + '</sub>';
      });
      return s;
    }

    const powers = [];
    s = formatMathExponents(s);
    s = s.replace(/<span\s+class=["']ar-pow["'][^>]*>\s*<span\s+class=["']ar-base["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const ph = '___ARPOW' + numToAlpha(powers.length) + '___';
      powers.push({ base: toEasternDigits(base), exp: toEasternDigits(exp) });
      return ph;
    });
    s = escapeHtml(toEasternDigits(s));
    powers.forEach(function (p, i) {
      const ph = '___ARPOW' + numToAlpha(i) + '___';
      s = s.split(ph).join('<span dir="rtl" style="direction:rtl; unicode-bidi:isolate;">' + p.base + '<sup style="font-size:75%; vertical-align:super; font-weight:bold;">' + p.exp + '</sup></span>');
    });
    return s;
  }

  /**
   * تحويل النص الرقمي (مشرقي أو غربي) إلى رقم برمجي للعمليات الحسابية
   */
  function toWesternNumber(input, fallback) {
    if (typeof input === 'number') return Number.isFinite(input) ? input : (fallback || 0);
    if (input === null || input === undefined) return fallback || 0;
    const cleaned = String(input)
      .replace(/[٠-٩٫]/g, function (ch) { return EASTERN_TO_WESTERN_MAP[ch] || ch; })
      .replace(/,/g, '.')
      .trim();
    const num = parseFloat(cleaned);
    return Number.isFinite(num) ? num : (fallback || 0);
  }

  /**
   * تنسيق الدرجة بصيغة دقيقة (مشرقية للابتدائي والمتوسط، وإنجليزية للثانوي)
   */
  function formatMark(num, isSecondary) {
    const val = toWesternNumber(num, 1);
    const rounded = Math.round(val * 100) / 100;
    if (isSecondary) {
      if (rounded === 1) return '1 درجة';
      if (rounded === 2) return '2 درجتان';
      if (rounded >= 3 && rounded <= 10 && Number.isInteger(rounded)) {
        return rounded + ' درجات';
      }
      return rounded + ' درجة';
    }
    if (rounded === 1) return '١ درجة';
    if (rounded === 2) return 'درجتان';
    const numStr = toEasternDigits(String(rounded));
    if (rounded >= 3 && rounded <= 10 && Number.isInteger(rounded)) {
      return numStr + ' درجات';
    }
    return numStr + ' درجة';
  }

  function formatMarkShort(num, isSecondary) {
    const val = toWesternNumber(num, 0);
    const rounded = Math.round(val * 100) / 100;
    if (isSecondary) {
      return String(rounded);
    }
    return toEasternDigits(String(rounded));
  }

  function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    let s = String(str);
    if (s.indexOf('ar-pow') === -1 && s.indexOf('sec-pow') === -1 && s.indexOf('sec-sub') === -1) {
      return s
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }
    const preserved = [];
    s = s.replace(/<span\s+class=["'][^"']*(?:ar-pow|sec-pow)[^"']*["'][^>]*>\s*<span\s+class=["'][^"']*(?:ar-base|sec-base)[^"']*["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["'][^"']*(?:ar-exp|sec-exp)[^"']*["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>|<sub\b[^>]*>[\s\S]*?<\/sub>/gi, function (fullTag) {
      const ph = '___ESCPOW' + numToAlpha(preserved.length) + '___';
      preserved.push(fullTag);
      return ph;
    });
    s = s
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
    preserved.forEach(function (fullTag, i) {
      const ph = '___ESCPOW' + numToAlpha(i) + '___';
      s = s.split(ph).join(fullTag);
    });
    return s;
  }

  /**
   * صياغة وعرض نصوص الأسئلة والخيارات والحلول بصيغة HTML آمنة
   * تضمن في المرحلة الابتدائية والمتوسطة: الأرقام العربية المشرقية والأسس RTL
   * وفي المرحلة الثانوية: الأرقام الإنجليزية حصراً والمعادلات LTR والشرح RTL المتوازن
   */
  function renderMathHtml(input, opts) {
    if (input === null || input === undefined) return '';
    let s = String(input);
    const sec = (opts === true) || isSecondaryStage(opts) || s.indexOf('class="sec-math"') !== -1 || s.indexOf('class="ltr-math"') !== -1 || s.indexOf('class="sec-pow"') !== -1;

    if (s.indexOf('&lt;') !== -1 && (s.indexOf('ar-pow') !== -1 || s.indexOf('sec-pow') !== -1 || s.indexOf('span') !== -1 || s.indexOf('sup') !== -1 || s.indexOf('sub') !== -1 || s.indexOf('vmatrix') !== -1 || s.indexOf('bmatrix') !== -1)) {
      s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
    }

    const ktxBlocks = [];
    const stashKtx = function (renderedHtml) {
      const ph = '___KTXPH' + numToAlpha(ktxBlocks.length) + '___';
      ktxBlocks.push(renderedHtml);
      return ph;
    };

    // حماية أي عناصر KaTeX أو حاويات مصفوفات 2D موجودة مسبقاً
    s = s.replace(/<span\s+class=["'][^"']*(?:katex|sec-matrix-container)[^"']*["'][\s\S]*?<\/span>\s*<\/span>\s*<\/span>|<span\s+class=["'][^"']*(?:katex|sec-matrix-container)[^"']*["'][\s\S]*?<\/span>/gi, function (m) {
      return stashKtx(m);
    });

    // 1. استخراج وتصيير بيئات المصفوفات والمحددات في LaTeX
    s = s.replace(/\\begin\{(vmatrix|bmatrix|pmatrix|matrix)\}[\s\S]*?\\end\{\1\}/g, function (m) {
      return stashKtx(renderLatexFormula(m, false, sec));
    });

    // 2. تصيير المحددات في التنسيق الموروث | <span class="sec-row">...</span> |
    s = s.replace(/\|\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*\|/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? stashKtx(format2DMatrixHtml(rows, true, sec)) : _;
    });

    // 3. تصيير المصفوفات في التنسيق الموروث [ <span class="sec-row">...</span> ]
    s = s.replace(/(?:<span\s+class=["']sec-brack["']>\[<\/span>|\[)\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*(?:<span\s+class=["']sec-brack["']>\]<\/span>|\])/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? stashKtx(format2DMatrixHtml(rows, false, sec)) : _;
    });

    // 4. تصيير صيغ LaTeX المحصورة بين علامات $ أو \( \) أو $$ أو \[ \]
    s = s.replace(/\$\$([\s\S]+?)\$\$/g, function (_, tex) {
      return stashKtx(renderLatexFormula(tex, true, sec));
    });
    s = s.replace(/\\\[([\s\S]+?)\\\]/g, function (_, tex) {
      return stashKtx(renderLatexFormula(tex, true, sec));
    });
    s = s.replace(/\\\(([\s\S]+?)\\\)/g, function (_, tex) {
      return stashKtx(renderLatexFormula(tex, false, sec));
    });
    s = s.replace(/(^|[^\\])\$([^\$]+?)\$/g, function (_, pre, tex) {
      return pre + stashKtx(renderLatexFormula(tex, false, sec));
    });

    if (sec) {
      // المرحلة الثانوية: أرقام إنجليزية (0-9) حصراً + تحويل الأسس والمؤشرات السفلية داخل وسوم LTR وخارجها بأمان تام
      s = toWesternDigits(s);
      const secTags = [];
      const stashTag = function (fullTag) {
        const ph = '___SECTAG' + numToAlpha(secTags.length) + '___';
        secTags.push(fullTag);
        return ph;
      };

      // استخراج وسوم <span> المتوازنة (مع دعم التداخل) وتحويل الأسس والمؤشرات داخلها
      let rebuilt = '';
      let cursor = 0;
      const openSpanPat = /<span\b([^>]*)>/gi;
      let om;
      while ((om = openSpanPat.exec(s)) !== null) {
        if (om.index < cursor) continue;
        if (om.index > cursor) {
          rebuilt += s.substring(cursor, om.index);
        }
        let depth = 1;
        const innerStart = openSpanPat.lastIndex;
        const tagScanner = /<\/?span\b[^>]*>/gi;
        tagScanner.lastIndex = innerStart;
        let tm;
        let closeStart = -1;
        let closeEnd = innerStart;
        while ((tm = tagScanner.exec(s)) !== null) {
          if (tm[0].charAt(1) === '/') {
            depth--;
            if (depth === 0) {
              closeStart = tm.index;
              closeEnd = tagScanner.lastIndex;
              break;
            }
          } else {
            depth++;
          }
        }
        if (closeStart !== -1) {
          const attrs = om[1] || '';
          const inner = s.substring(innerStart, closeStart);
          if (/sec-math|ltr-math/.test(attrs)) {
            rebuilt += stashTag('<span class="sec-math ltr-math" dir="ltr">' + convertSecInnerMath(inner) + '</span>');
          } else {
            rebuilt += stashTag(s.substring(om.index, closeEnd));
          }
          cursor = closeEnd;
          openSpanPat.lastIndex = cursor;
        } else {
          rebuilt += s.substring(om.index);
          cursor = s.length;
          break;
        }
      }
      if (cursor < s.length) {
        rebuilt += s.substring(cursor);
      }

      // معالجة النصوص خارج الوسوم فقط
      const segs = rebuilt.split(/(___SECTAG[A-Z]+___)/);
      s = segs.map(function (seg) {
        if (!seg || /^___SECTAG[A-Z]+___$/.test(seg)) return seg;
        let chunk = convertSecInnerMath(seg);
        // حفظ sec-pow / sec-sub الناتجة عن التحويل حتى لا تمسها تعبيرات المقارنة التالية
        const innerTags = [];
        chunk = chunk.replace(/<span\s+class=["']sec-pow["'][^>]*>\s*<span\s+class=["']sec-base["'][^>]*>[\s\S]*?<\/span>\s*<sup\s+class=["']sec-exp["'][^>]*>[\s\S]*?<\/sup>\s*<\/span>|<sub\b[^>]*>[\s\S]*?<\/sub>/gi, function (t) {
          const ph = '___CHKTAG' + numToAlpha(innerTags.length) + '___';
          innerTags.push(t);
          return ph;
        });
        chunk = chunk.replace(/(?<![\w\>])([A-Za-z][a-zA-Z0-9_\'\^\*\+\-\/\s\=∠≅△°~><]{2,}[A-Za-z0-9°])(?![\w\<])/g, function (match) {
          if (match.indexOf('___CHKTAG') !== -1) return match;
          if (/[=\+\-∠≅△°~><^]/.test(match) && !/[أ-ي]/.test(match)) {
            return '<span class="sec-math ltr-math" dir="ltr">' + match + '</span>';
          }
          return match;
        });
        for (let i = innerTags.length - 1; i >= 0; i--) {
          const ph = '___CHKTAG' + numToAlpha(i) + '___';
          chunk = chunk.split(ph).join(innerTags[i]);
        }
        return chunk;
      }).join('');

      for (let i = secTags.length - 1; i >= 0; i--) {
        const ph = '___SECTAG' + numToAlpha(i) + '___';
        s = s.split(ph).join(secTags[i]);
      }

      for (let i = ktxBlocks.length - 1; i >= 0; i--) {
        const ph = '___KTXPH' + numToAlpha(i) + '___';
        s = s.split(ph).join(ktxBlocks[i]);
      }

      return s;
    }

    // المرحلة الابتدائية والمتوسطة: الأرقام العربية المشرقية والأسس على يسار الأساس
    const powers = [];
    s = s.replace(/<span\s+class=["']ar-pow["'][^>]*>\s*<span\s+class=["']ar-base["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const ph = '___ARPOW' + numToAlpha(powers.length) + '___';
      powers.push({
        base: toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim()),
        exp: toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim())
      });
      return ph;
    });

    s = formatMathExponents(s);
    s = s.replace(/<span\s+class=["']ar-pow["'][^>]*>\s*<span\s+class=["']ar-base["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const ph = '___ARPOW' + numToAlpha(powers.length) + '___';
      powers.push({
        base: toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim()),
        exp: toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim())
      });
      return ph;
    });

    s = escapeHtml(toEasternDigits(s));

    powers.forEach(function (p, i) {
      const ph = '___ARPOW' + numToAlpha(i) + '___';
      s = s.split(ph).join('<span class="ar-pow"><span class="ar-base">' + p.base + '</span><sup class="ar-exp">' + p.exp + '</sup></span>');
    });

    for (let i = ktxBlocks.length - 1; i >= 0; i--) {
      const ph = '___KTXPH' + numToAlpha(i) + '___';
      s = s.split(ph).join(ktxBlocks[i]);
    }

    return s;
  }

  /**
   * تحويل وسوم الأسس إلى نص عادي آمن للحافظة النصية والمحررات العادية
   * يمنع تسريب أي وسوم HTML نهائياً
   */
  function stripMathToPlain(input, opts) {
    if (input === null || input === undefined) return '';
    let s = String(input);
    const sec = (opts === true) || isSecondaryStage(opts) || s.indexOf('class="sec-math"') !== -1 || s.indexOf('class="ltr-math"') !== -1 || s.indexOf('class="sec-pow"') !== -1;

    // تحويل بيئات المصفوفات والمحددات في LaTeX إلى صيغة نصية مقروءة ونظيفة
    s = s.replace(/\\begin\{(vmatrix|matrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
      const rows = body.trim().split('\\\\').map(function (r) {
        return r.split('&').map(function (c) { return c.trim(); }).join('  ');
      });
      return '| ' + rows.join(' ; ') + ' |';
    });
    s = s.replace(/\\begin\{(bmatrix|pmatrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
      const rows = body.trim().split('\\\\').map(function (r) {
        return r.split('&').map(function (c) { return c.trim(); }).join('  ');
      });
      return '[ ' + rows.join(' ; ') + ' ]';
    });
    s = s.replace(/\|\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*\|/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? ('| ' + rows.map(function (r) { return r.join('  '); }).join(' ; ') + ' |') : _;
    });
    s = s.replace(/(?:<span\s+class=["']sec-brack["']>\[<\/span>|\[)\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)+)\s*(?:<span\s+class=["']sec-brack["']>\]<\/span>|\])/gi, function (_, body) {
      const rows = parseLegacyMatrixRows(body);
      return rows ? ('[ ' + rows.map(function (r) { return r.join('  '); }).join(' ; ') + ' ]') : _;
    });
    s = s.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1/$2)');
    s = s.replace(/\\sqrt\{([^{}]+)\}/g, '√($1)');
    s = s.replace(/\\times/g, '×').replace(/\\pm/g, '±').replace(/\\cdot/g, '·').replace(/\\le/g, '≤').replace(/\\ge/g, '≥').replace(/\\ne/g, '≠').replace(/\\approx/g, '≈');

    if (sec) {
      s = s.replace(/<sub\b[^>]*>([\s\S]*?)<\/sub>/gi, function (_, sub) {
        const subDigits = toWesternDigits(String(sub || '').replace(/<[^>]+>/g, '').trim());
        return toSubscriptText(subDigits);
      });
      s = s.replace(/<span\s+class=["'][^"']*(?:sec-pow|ar-pow)[^"']*["'][^>]*>\s*<span\s+class=["'][^"']*(?:sec-base|ar-base)[^"']*["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["'][^"']*(?:sec-exp|ar-exp)[^"']*["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        const b = toWesternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
        const e = toWesternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
        return b + toSuperscriptText(e);
      });
      return toWesternDigits(s.replace(/<[^>]+>/g, '').trim());
    }
    s = s.replace(/<sub\b[^>]*>([\s\S]*?)<\/sub>/gi, function (_, sub) {
      const subClean = toEasternDigits(String(sub || '').replace(/<[^>]+>/g, '').trim());
      return toSubscriptText(subClean);
    });
    s = s.replace(/<span\s+class=["']ar-pow["'][^>]*>\s*<span\s+class=["']ar-base["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const b = toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
      const e = toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
      return b + toSuperscriptText(e);
    });
    return toEasternDigits(s.replace(/<[^>]+>/g, '').trim());
  }

  /**
   * تحويل السؤال إلى صيغة قابلة للتحرير المريح داخل حقل التعديل (textarea)
   * بحيث يرى المعلم كلم^٢ أو ٥^٢ بدلاً من وسوم HTML المعقدة (أو صيغ إنجليزية للثانوي)
   */
  function stripMathToInputText(input, opts) {
    if (input === null || input === undefined) return '';
    let s = String(input);
    const sec = (opts === true) || isSecondaryStage(opts) || s.indexOf('class="sec-math"') !== -1 || s.indexOf('class="ltr-math"') !== -1 || s.indexOf('class="sec-pow"') !== -1;
    if (sec) {
      s = s.replace(/<sub\b[^>]*>([\s\S]*?)<\/sub>/gi, function (_, sub) {
        return '_' + toWesternDigits(String(sub || '').replace(/<[^>]+>/g, '').trim());
      });
      s = s.replace(/<span\s+class=["'][^"']*(?:sec-pow|ar-pow)[^"']*["'][^>]*>\s*<span\s+class=["'][^"']*(?:sec-base|ar-base)[^"']*["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["'][^"']*(?:sec-exp|ar-exp)[^"']*["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        const b = toWesternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
        const e = toWesternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
        return b + '^' + e;
      });
      return toWesternDigits(s.replace(/<[^>]+>/g, '').trim());
    }
    s = s.replace(/<span\s+class=["']ar-pow["'][^>]*>\s*<span\s+class=["']ar-base["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const b = toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
      const e = toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
      return b + '^' + e;
    });
    return toEasternDigits(s.replace(/<[^>]+>/g, '').trim());
  }

  function normalizeSearchText(str) {
    if (!str) return '';
    return String(str)
      .replace(/[٠-٩٫]/g, function (ch) { return EASTERN_TO_WESTERN_MAP[ch] || ch; })
      .replace(/[أإآ]/g, 'ا')
      .replace(/ى/g, 'ي')
      .replace(/ة/g, 'ه')
      .replace(/[\u064B-\u065F\u0670]/g, '')
      .toLowerCase()
      .trim();
  }

  function toClipboardUrl(src) {
    if (!src) return '';
    const s = String(src).trim();
    if (!s || /^data:/i.test(s) || /^https?:/i.test(s)) return s;
    if (typeof window !== 'undefined' && window.location && /^https?:$/i.test(window.location.protocol)) {
      try {
        return new URL(s.replace(/^\/+/, ''), window.location.href).href;
      } catch (e) {
        return window.location.origin + '/' + s.replace(/^\/+/, '');
      }
    }
    return s;
  }

  function measureAndScaleDataUrl(dataUrl, fallbackUrl, maxW, maxH) {
    return new Promise(function (resolve) {
      if (typeof Image === 'undefined') {
        resolve({ dataUrl: dataUrl || fallbackUrl || '', width: 0, height: 0 });
        return;
      }
      const img = new Image();
      img.onload = function () {
        const nw = img.naturalWidth || img.width || 240;
        const nh = img.naturalHeight || img.height || 140;
        const ratio = Math.min(1, (maxW || 290) / nw, (maxH || 175) / nh);
        const w = Math.max(1, Math.round(nw * ratio));
        const h = Math.max(1, Math.round(nh * ratio));
        let outUrl = dataUrl;
        if (!outUrl && typeof document !== 'undefined') {
          try {
            const canvas = document.createElement('canvas');
            canvas.width = nw;
            canvas.height = nh;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, nw, nh);
            outUrl = canvas.toDataURL('image/png');
          } catch (e) {
            outUrl = fallbackUrl || '';
          }
        }
        resolve({ dataUrl: outUrl || fallbackUrl || '', width: w, height: h });
      };
      img.onerror = function () {
        resolve({ dataUrl: dataUrl || fallbackUrl || '', width: 0, height: 0 });
      };
      img.src = dataUrl || fallbackUrl || '';
    });
  }

  async function resolveImageForClipboard(src, maxW, maxH) {
    const clean = src ? String(src).trim() : '';
    if (!clean) return { dataUrl: '', width: 0, height: 0 };
    const cacheKey = clean + '|' + (maxW || 290) + 'x' + (maxH || 175);
    if (_clipboardImageCache[cacheKey]) return _clipboardImageCache[cacheKey];

    const absUrl = toClipboardUrl(clean);
    let result;
    if (/^data:image\//i.test(clean)) {
      result = await measureAndScaleDataUrl(clean, clean, maxW || 290, maxH || 175);
    } else if (typeof fetch === 'function' && typeof FileReader !== 'undefined') {
      try {
        const resp = await fetch(absUrl);
        if (resp && resp.ok) {
          const blob = await resp.blob();
          const b64 = await new Promise(function (resolve) {
            const r = new FileReader();
            r.onload = function () { resolve(String(r.result || '')); };
            r.onerror = function () { resolve(''); };
            r.readAsDataURL(blob);
          });
          result = await measureAndScaleDataUrl(b64, absUrl, maxW || 290, maxH || 175);
        } else {
          result = await measureAndScaleDataUrl('', absUrl, maxW || 290, maxH || 175);
        }
      } catch (e) {
        result = await measureAndScaleDataUrl('', absUrl, maxW || 290, maxH || 175);
      }
    } else {
      result = await measureAndScaleDataUrl('', absUrl, maxW || 290, maxH || 175);
    }
    _clipboardImageCache[cacheKey] = result;
    return result;
  }

  function buildWordFigHtml(q, imageMap, isSecondary) {
    if (!q || !q.image) return '';
    const mapped = imageMap && imageMap[q.image];
    const srcUrl = mapped && mapped.dataUrl ? mapped.dataUrl : toClipboardUrl(q.image);
    if (!srcUrl) return '';
    const dimAttrs = (mapped && mapped.width && mapped.height)
      ? (' width="' + mapped.width + '" height="' + mapped.height + '"')
      : '';
    const isSec = !!isSecondary || isSecondaryStage(q);
    const fmtCap = formatStageDigits(q.imageCaption || '', isSec);
    const cap = q.imageCaption
      ? ('<div style="font-size:10pt; color:#475569; margin-top:2pt;">' + escapeHtml(fmtCap) + '</div>')
      : '';
    const altText = formatStageDigits(q.imageCaption || 'شكل السؤال', isSec);
    return (
      '<div style="text-align:center; margin:4pt 0 2pt 0;">' +
      '<img src="' + escapeHtml(srcUrl) + '" alt="' + escapeHtml(altText) + '"' +
      dimAttrs + ' style="max-width:290px; max-height:175px; height:auto; border:1px solid #cbd5e1;" />' +
      cap +
      '</div>'
    );
  }

  function buildWordAnswerLine(q, qType, opts) {
    const isSec = !!(opts && opts.isSecondary);
    if (qType === 'mcq' && typeof q.correct === 'number') {
      const letters = isSec ? SECONDARY_CHOICE_LETTERS : WORD_CHOICE_LETTERS;
      const corrLetter = letters[q.correct] || (isSec ? 'A' : 'أ');
      const corrText = formatMathForWordHtml((q.options && q.options[q.correct]) || '', opts);
      const expText = q.explanation ? (' — ' + formatMathForWordHtml(q.explanation, opts)) : '';
      return '<strong>الإجابة النموذجية:</strong> ' + corrLetter + ') ' + corrText + expText;
    }
    if (qType === 'tf') {
      const tfAns = q.is_true ? 'صواب (✓)' : 'خطأ (✗)';
      const expText = q.explanation ? (' — ' + formatMathForWordHtml(q.explanation, opts)) : '';
      return '<strong>الإجابة النموذجية:</strong> ' + tfAns + expText;
    }
    if (q.ans) {
      return '<strong>الحل النموذجي:</strong> ' + formatMathForWordHtml(q.ans, opts);
    }
    return '';
  }

  function buildClipboardHeaderHtml(header, totalMarks, imageMap, isSecondary) {
    if (!header) return '';
    const h = header;
    const isSec = !!isSecondary || isSecondaryStage(h);
    const fmtD = function (v) { return formatStageDigits(v || '', isSec); };
    const includeLogo = h.includeLogo !== false;
    const rawLogo = h.customLogoDataUrl || 'assets/img/logo.png';
    const logoObj = includeLogo ? ((imageMap && imageMap[rawLogo]) || { dataUrl: toClipboardUrl(rawLogo), width: 72, height: 72 }) : null;
    const moeObj = (imageMap && imageMap['assets/img/moe_logo.png']) || { dataUrl: toClipboardUrl('assets/img/moe_logo.png'), width: 96, height: 48 };
    const topRib = (imageMap && imageMap['assets/img/exam_top_ribbon.png']) || { dataUrl: toClipboardUrl('assets/img/exam_top_ribbon.png'), width: 640, height: 34 };

    const fontStyle = "font-family:'Cairo','Traditional Arabic','Arial',sans-serif;";
    return (
      '<div dir="rtl" style="margin-bottom:8pt;">' +
      (topRib.dataUrl ? '<div style="text-align:center; margin-bottom:4pt;"><img src="' + escapeHtml(topRib.dataUrl) + '" width="640" style="width:100%; max-height:36px; object-fit:cover; display:block;" /></div>' : '') +
      '<table dir="rtl" cellspacing="0" cellpadding="4" style="width:100%; border-collapse:collapse; border-bottom:3px solid #3F9E35; margin-bottom:6pt; ' + fontStyle + '">' +
      '<tr>' +
      '<td style="width:36%; text-align:center; vertical-align:middle; border:none; font-size:11pt; font-weight:bold; line-height:1.45;">' +
      '<div>' + escapeHtml(fmtD(h.ministry || 'المملكة العربية السعودية')) + '</div>' +
      '<div>' + escapeHtml(fmtD(h.district || '')) + '</div>' +
      (h.schoolCompany ? '<div>' + escapeHtml(fmtD(h.schoolCompany)) + '</div>' : '') +
      '<div>' + escapeHtml(fmtD(h.school || '')) + '</div>' +
      (h.stage ? '<div>' + escapeHtml(fmtD(h.stage)) + '</div>' : '') +
      '</td>' +
      '<td style="width:40%; text-align:center; vertical-align:middle; border:none;">' +
      (moeObj.dataUrl ? '<div style="margin-bottom:4pt;"><img src="' + escapeHtml(moeObj.dataUrl) + '" width="' + (moeObj.width || 92) + '" style="max-height:52px; width:auto;" /></div>' : '') +
      '<div style="font-size:13pt; font-weight:bold;">' + escapeHtml(fmtD(h.examTitle || '')) + '</div>' +
      '<div style="font-size:10.5pt;">المادة: ' + escapeHtml(fmtD(h.subject || 'الرياضيات')) + ' • الصف: ' + escapeHtml(fmtD(h.grade || '')) + ' • الفصل: ' + escapeHtml(fmtD(h.term || '')) + '</div>' +
      '<div style="font-size:10.5pt;">العام الدراسي: ' + escapeHtml(fmtD(h.year || '')) + ' • الزمن: ' + escapeHtml(fmtD(h.duration || '')) + '</div>' +
      '</td>' +
      '<td style="width:24%; text-align:center; vertical-align:middle; border:none;">' +
      (logoObj && logoObj.dataUrl ? '<img src="' + escapeHtml(logoObj.dataUrl) + '" width="' + Math.min(82, logoObj.width || 72) + '" style="max-width:82px; max-height:76px; width:auto; height:auto;" />' : '') +
      '</td>' +
      '</tr></table>' +
      '<table dir="rtl" cellspacing="0" cellpadding="4" style="width:100%; border-collapse:collapse; margin-bottom:8pt; ' + fontStyle + '">' +
      '<tr>' +
      '<td style="width:16%; border:1px solid #000; background:#F2F2F2; font-weight:bold; text-align:center; font-size:11pt;">اسم الطالب</td>' +
      '<td style="width:66%; border:1px solid #000; text-align:right; font-size:11pt;">....................................................................................</td>' +
      '<td rowspan="2" style="width:18%; border:1px solid #000; padding:0; vertical-align:middle;">' +
      '<table dir="rtl" cellspacing="0" cellpadding="2" style="width:100%; border-collapse:collapse;">' +
      '<tr><td style="border-bottom:1px solid #000; background:#F2F2F2; text-align:center; font-size:10pt; font-weight:bold;">الدرجة</td></tr>' +
      '<tr><td style="text-align:center; font-size:13pt; font-weight:bold;">&nbsp;&nbsp;&nbsp; / ' + escapeHtml(formatMarkShort(totalMarks, isSec)) + '</td></tr>' +
      '</table></td></tr>' +
      '<tr>' +
      '<td style="border:1px solid #000; background:#F2F2F2; font-weight:bold; text-align:center; font-size:11pt;">الصف</td>' +
      '<td style="border:1px solid #000; text-align:right; font-size:11pt;">' + escapeHtml(fmtD(h.grade || '')) + ' / ( &nbsp;&nbsp; )</td>' +
      '</tr></table>' +
      '</div>'
    );
  }

  function renderClipboardQuestionTableGroup(qType, items, opts, imageMap, startNum) {
    const isSec = !!(opts && opts.isSecondary);
    const cellFont = "font-family:'Cairo','Traditional Arabic','Arial',sans-serif; font-size:12pt; color:#000000;";
    const choiceLetters = isSec ? SECONDARY_CHOICE_LETTERS : WORD_CHOICE_LETTERS;
    if (qType === 'mcq') {
      const rows = items.map(function (q, i) {
        const qNum = opts.numbered ? (isSec ? String(startNum + i) : toEasternDigits(startNum + i)) : (isSec ? '1' : '١');
        const qText = formatMathForWordHtml(q.q || q.statement || '', opts);
        const figHtml = buildWordFigHtml(q, imageMap, isSec);
        const optArr = Array.isArray(q.options) ? q.options.slice(0, 4) : ['', '', '', ''];
        while (optArr.length < 4) optArr.push('');
        const optCells = optArr.map(function (opt, oIdx) {
          return (
            '<td style="width:4.5%; border:1px solid #000; text-align:center; vertical-align:middle; font-weight:bold; padding:4pt 2pt; ' + cellFont + '">' +
            (choiceLetters[oIdx] || (isSec ? 'A' : 'أ')) +
            '</td>' +
            '<td style="width:19.25%; border:1px solid #000; text-align:right; vertical-align:middle; padding:4pt 6pt; ' + cellFont + '">' +
            formatMathForWordHtml(opt, opts) +
            '</td>'
          );
        }).join('');
        return (
          '<tr>' +
          '<td rowspan="2" style="width:5%; border:1px solid #000; text-align:center; vertical-align:middle; font-weight:bold; background:#ffffff; padding:4pt; ' + cellFont + '">' + qNum + '</td>' +
          '<td colspan="8" style="width:95%; border:1px solid #000; background:#F2F2F2; text-align:right; vertical-align:top; padding:5pt 8pt; font-weight:bold; ' + cellFont + '">' + qText + figHtml + '</td>' +
          '</tr>' +
          '<tr>' + optCells + '</tr>'
        );
      }).join('');
      return (
        '<table dir="rtl" cellspacing="0" cellpadding="0" style="width:100%; border-collapse:collapse; border:1px solid #000; margin-bottom:8pt; direction:rtl;">' +
        rows +
        '</table>'
      );
    }

    if (qType === 'tf') {
      const headerRow =
        '<tr><td colspan="3" style="border:1px solid #000; background:#F2F2F2; text-align:center; font-weight:bold; padding:5pt 8pt; ' + cellFont + '">' +
        'ضع علامة ( ✓ ) أمام العبارة الصحيحة وعلامة ( ✗ ) أمام العبارة الخاطئة:' +
        '</td></tr>';
      const rows = items.map(function (q, i) {
        const qNum = opts.numbered ? (isSec ? String(startNum + i) : toEasternDigits(startNum + i)) : (isSec ? '1' : '١');
        const qText = formatMathForWordHtml(q.statement || q.q || '', opts);
        const figHtml = buildWordFigHtml(q, imageMap, isSec);
        return (
          '<tr>' +
          '<td style="width:9%; border:1px solid #000; text-align:center; vertical-align:middle; font-weight:bold; padding:5pt; ' + cellFont + '">' + qNum + '</td>' +
          '<td style="width:79%; border:1px solid #000; text-align:right; vertical-align:middle; padding:5pt 8pt; ' + cellFont + '">' + qText + figHtml + '</td>' +
          '<td style="width:12%; border:1px solid #000; text-align:center; vertical-align:middle; padding:5pt; white-space:nowrap; ' + cellFont + '">( &nbsp;&nbsp;&nbsp; )</td>' +
          '</tr>'
        );
      }).join('');
      return (
        '<table dir="rtl" cellspacing="0" cellpadding="0" style="width:100%; border-collapse:collapse; border:1px solid #000; margin-bottom:8pt; direction:rtl;">' +
        headerRow + rows +
        '</table>'
      );
    }

    const rows = items.map(function (q, i) {
      const qNum = opts.numbered ? (isSec ? String(startNum + i) : toEasternDigits(startNum + i)) : (isSec ? '1' : '١');
      const qText = formatMathForWordHtml(q.q || q.statement || '', opts);
      const figHtml = buildWordFigHtml(q, imageMap, isSec);
      const lineCount = Math.max(2, Math.min(6, toWesternNumber(q.lines, 3)));
      let linesHtml = '';
      for (let l = 0; l < lineCount; l++) {
        linesHtml += (l === 0 ? 'الحل / ' : '') + '..............................................................................................' + (l < lineCount - 1 ? '<br/>' : '');
      }
      return (
        '<tr>' +
        '<td rowspan="2" style="width:9%; border:1px solid #000; text-align:center; vertical-align:middle; font-weight:bold; background:#ffffff; padding:5pt; ' + cellFont + '">' + qNum + '</td>' +
        '<td style="width:91%; border:1px solid #000; background:#F2F2F2; text-align:right; vertical-align:top; padding:5pt 8pt; font-weight:bold; ' + cellFont + '">' + qText + figHtml + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td style="width:91%; border:1px solid #000; background:#ffffff; text-align:right; vertical-align:top; padding:6pt 8pt; color:#475569; ' + cellFont + '">' + linesHtml + '</td>' +
        '</tr>'
      );
    }).join('');
    return (
      '<table dir="rtl" cellspacing="0" cellpadding="0" style="width:100%; border-collapse:collapse; border:1px solid #000; margin-bottom:8pt; direction:rtl;">' +
      rows +
      '</table>'
    );
  }

  /**
   * بناء HTML متوافق تماماً مع Microsoft Word بنظام RTL
   * يدعم الأرقام المشرقية للابتدائي والمتوسط، والأرقام الإنجليزية ومعادلات LTR للثانوي
   * مع تضمين الجداول الرسمية والصيغ والصور المضمنة Base64
   */
  function buildWordClipboardHTML(questions, options) {
    const opts = Object.assign({ includeAnswers: false, numbered: true, asTable: true }, options || {});
    const list = Array.isArray(questions) ? questions : [questions];
    const imageMap = opts.imageMap || null;

    if (!opts.isSecondary && list.some(isSecondaryStage)) {
      opts.isSecondary = true;
    }
    const isSec = !!opts.isSecondary;

    let totalMarks = 0;
    list.forEach(function (q) {
      totalMarks += toWesternNumber(q.marks !== undefined ? q.marks : 1, 1);
    });

    const parts = [];
    if (opts.header) {
      parts.push(buildClipboardHeaderHtml(opts.header, totalMarks, imageMap, isSec));
    }

    if (Array.isArray(opts.sections) && opts.sections.length) {
      opts.sections.forEach(function (sec) {
        const items = sec.items || [];
        if (!items.length) return;
        let secMarks = 0;
        items.forEach(function (q) { secMarks += toWesternNumber(q.marks !== undefined ? q.marks : 1, 1); });
        const secTitle = isSec ? escapeHtml(toWesternDigits(sec.title || 'القسم')) : escapeHtml(toEasternDigits(sec.title || 'القسم'));
        const markText = escapeHtml(formatMarkShort(secMarks, isSec));
        parts.push(
          '<table dir="rtl" cellspacing="0" cellpadding="4" style="width:100%; border-collapse:collapse; margin:6pt 0 4pt 0; border:none;">' +
          '<tr>' +
          '<td style="width:82%; text-align:right; font-weight:bold; font-size:12.5pt; border:none;">' + secTitle + '</td>' +
          '<td style="width:18%; border:none; padding:0;">' +
          '<table dir="rtl" cellspacing="0" cellpadding="2" style="width:100%; border-collapse:collapse;">' +
          '<tr><td style="border:1px solid #000; text-align:center; font-weight:bold; font-size:11pt;">&nbsp;&nbsp;&nbsp; / ' + markText + '</td></tr>' +
          '</table></td></tr></table>'
        );
        let runStart = 1;
        let idx = 0;
        while (idx < items.length) {
          const curType = items[idx].type || (items[idx].options ? 'mcq' : (typeof items[idx].is_true === 'boolean' ? 'tf' : 'essay'));
          const batch = [items[idx]];
          idx++;
          while (idx < items.length) {
            const nextType = items[idx].type || (items[idx].options ? 'mcq' : (typeof items[idx].is_true === 'boolean' ? 'tf' : 'essay'));
            if (nextType !== curType) break;
            batch.push(items[idx]);
            idx++;
          }
          parts.push(renderClipboardQuestionTableGroup(curType, batch, opts, imageMap, runStart));
          runStart += batch.length;
        }
      });
    } else {
      let runStart = 1;
      let idx = 0;
      while (idx < list.length) {
        const curType = list[idx].type || (list[idx].options ? 'mcq' : (typeof list[idx].is_true === 'boolean' ? 'tf' : 'essay'));
        const batch = [list[idx]];
        idx++;
        while (idx < list.length) {
          const nextType = list[idx].type || (list[idx].options ? 'mcq' : (typeof list[idx].is_true === 'boolean' ? 'tf' : 'essay'));
          if (nextType !== curType) break;
          batch.push(list[idx]);
          idx++;
        }
        parts.push(renderClipboardQuestionTableGroup(curType, batch, opts, imageMap, runStart));
        runStart += batch.length;
      }
    }

    if (opts.includeAnswers) {
      const ansLines = list.map(function (q, i) {
        const qType = q.type || (q.options ? 'mcq' : (typeof q.is_true === 'boolean' ? 'tf' : 'essay'));
        const line = buildWordAnswerLine(q, qType, opts);
        if (!line) return '';
        const lbl = opts.numbered ? ('س ' + (isSec ? String(i + 1) : toEasternDigits(i + 1)) + ': ') : '';
        return '<p dir="rtl" style="direction:rtl; text-align:right; margin:2pt 0; color:#047857; font-size:11.5pt;"><strong>' + lbl + '</strong>' + line + '</p>';
      }).filter(Boolean).join('');
      if (ansLines) {
        parts.push('<div dir="rtl" style="margin-top:8pt; padding-top:6pt; border-top:1px dashed #94a3b8;">' + ansLines + '</div>');
      }
    }

    if (opts.header) {
      const botRib = (imageMap && imageMap['assets/img/exam_bottom_ribbon.png']) || { dataUrl: toClipboardUrl('assets/img/exam_bottom_ribbon.png'), width: 640 };
      const teacherName = isSec ? escapeHtml(opts.header.teacher || '') : escapeHtml(toEasternDigits(opts.header.teacher || ''));
      const principalName = isSec ? escapeHtml(opts.header.principal || '') : escapeHtml(toEasternDigits(opts.header.principal || ''));
      parts.push(
        '<div dir="rtl" style="text-align:center; font-weight:bold; font-size:12pt; margin-top:10pt;">انتهت الأسئلة — مع خالص الدعوات بالتوفيق والنجاح</div>' +
        '<table dir="rtl" cellspacing="0" cellpadding="4" style="width:100%; border-collapse:collapse; border:none; margin-top:6pt;">' +
        '<tr>' +
        '<td style="width:50%; text-align:center; border:none; font-weight:bold; font-size:11.5pt;">معلم المادة<br/>' + teacherName + '</td>' +
        '<td style="width:50%; text-align:center; border:none; font-weight:bold; font-size:11.5pt;">مدير المدرسة<br/>' + principalName + '</td>' +
        '</tr></table>' +
        (botRib.dataUrl ? '<div style="text-align:center; margin-top:6pt;"><img src="' + escapeHtml(botRib.dataUrl) + '" width="640" style="width:100%; max-height:28px; object-fit:contain;" /></div>' : '')
      );
    }

    return (
      '<div dir="rtl" lang="ar" style="direction:rtl; text-align:right; font-family:\'Cairo\',\'Traditional Arabic\',\'Arial\',sans-serif; font-size:12.5pt; line-height:1.5; color:#000000;">' +
      parts.join('') +
      '</div>'
    );
  }

  /**
   * بناء نص عادي RTL محمي بمحارف التحكم بالاتجاه RLM للّصق الآمن
   */
  function buildWordClipboardPlain(questions, options) {
    const opts = Object.assign({ includeAnswers: false, numbered: true }, options || {});
    const list = Array.isArray(questions) ? questions : [questions];
    const isSec = !!(opts.isSecondary || list.some(isSecondaryStage));
    const letters = isSec ? SECONDARY_CHOICE_LETTERS : CHOICE_LETTERS;

    return list.map(function (q, idx) {
      const qNum = opts.numbered ? ('س ' + (isSec ? String(idx + 1) : toEasternDigits(idx + 1)) + ': ') : '';
      const qText = stripMathToPlain(q.q || q.statement || '', isSec);
      const markText = '(' + formatMark(q.marks !== undefined ? q.marks : 1, isSec) + ')';
      const qType = q.type || (q.options ? 'mcq' : (typeof q.is_true === 'boolean' ? 'tf' : 'essay'));

      const lines = [RLM + qNum + qText + ' ' + markText];

      if (qType === 'mcq' && Array.isArray(q.options)) {
        const optsLine = q.options.slice(0, 4).map(function (opt, i) {
          return (letters[i] || (isSec ? 'A' : 'أ')) + ') ' + stripMathToPlain(opt, isSec);
        }).join('    ');
        lines.push(RLM + optsLine);
        if (opts.includeAnswers && typeof q.correct === 'number') {
          const corrLetter = letters[q.correct] || (isSec ? 'A' : 'أ');
          const corrText = stripMathToPlain(q.options[q.correct] || '', isSec);
          const exp = q.explanation ? (' — ' + stripMathToPlain(q.explanation, isSec)) : '';
          lines.push(RLM + 'الإجابة النموذجية: ' + corrLetter + ') ' + corrText + exp);
        }
      } else if (qType === 'tf') {
        lines.push(RLM + '(   ) صواب        (   ) خطأ');
        if (opts.includeAnswers) {
          const exp = q.explanation ? (' — ' + stripMathToPlain(q.explanation, isSec)) : '';
          lines.push(RLM + 'الإجابة النموذجية: ' + (q.is_true ? 'صواب' : 'خطأ') + exp);
        }
      } else {
        const lineCount = Math.max(2, Math.min(6, toWesternNumber(q.lines, 3)));
        for (let l = 0; l < lineCount; l++) {
          lines.push(RLM + '...........................................................................');
        }
        if (opts.includeAnswers && q.ans) {
          lines.push(RLM + 'الحل النموذجي: ' + stripMathToPlain(q.ans, isSec));
        }
      }
      return lines.join('\n');
    }).join('\n\n');
  }

  /**
   * إشعار عائم غير معطل للمستخدم
   */
  function showToast(message, type, isSecondary) {
    if (typeof document === 'undefined' || !document.body) return;
    const toastType = type || 'success';
    let container = document.getElementById('raed-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'raed-toast-container';
      container.className = 'raed-toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'raed-toast raed-toast-' + toastType;
    toast.setAttribute('dir', 'rtl');
    toast.textContent = isSecondary ? toWesternDigits(message) : toEasternDigits(message);
    container.appendChild(toast);

    setTimeout(function () {
      toast.classList.add('show');
    }, 10);

    setTimeout(function () {
      toast.classList.remove('show');
      setTimeout(function () {
        if (toast.parentNode) toast.parentNode.removeChild(toast);
      }, 300);
    }, 3200);
  }

  /**
   * نسخ سؤال أو مجموعة أسئلة بتنسيق مزدوج (HTML نظيف لبرنامج Word + نص RTL)
   */
  async function copyQuestionsToWord(questions, options) {
    const list = Array.isArray(questions) ? questions : [questions];
    if (!list.length) {
      showToast('لم يتم تحديد أي أسئلة للنسخ.', 'warning');
      return false;
    }

    const imageKeys = [];
    list.forEach(function (q) {
      if (q && q.image && imageKeys.indexOf(q.image) === -1) imageKeys.push(q.image);
    });
    const optsObj = Object.assign({}, options || {});
    if (optsObj.header) {
      const h = optsObj.header;
      if (h.includeLogo !== false) {
        const logoKey = h.customLogoDataUrl || 'assets/img/logo.png';
        if (imageKeys.indexOf(logoKey) === -1) imageKeys.push(logoKey);
      }
      ['assets/img/moe_logo.png', 'assets/img/exam_top_ribbon.png', 'assets/img/exam_bottom_ribbon.png'].forEach(function (aKey) {
        if (imageKeys.indexOf(aKey) === -1) imageKeys.push(aKey);
      });
    }

    const imageMap = Object.create(null);
    if (imageKeys.length) {
      const entries = await Promise.all(imageKeys.map(function (key) {
        const isRibbon = key.indexOf('ribbon') !== -1;
        return resolveImageForClipboard(key, isRibbon ? 640 : 290, isRibbon ? 60 : 175).then(function (res) {
          return [key, res];
        });
      }));
      entries.forEach(function (pair) { imageMap[pair[0]] = pair[1]; });
    }
    optsObj.imageMap = imageMap;

    const isSec = !!(optsObj.isSecondary || list.some(isSecondaryStage));
    optsObj.isSecondary = isSec;

    const html = buildWordClipboardHTML(list, optsObj);
    const plain = buildWordClipboardPlain(list, optsObj);
    const countStr = isSec ? toWesternDigits(list.length) : toEasternDigits(list.length);

    // المحاولة الأولى: Clipboard API الحديثة مع صيغتي HTML و Plain Text
    try {
      if (typeof navigator !== 'undefined' && navigator.clipboard && typeof window.ClipboardItem === 'function') {
        const htmlBlob = new Blob(['\ufeff' + html], { type: 'text/html' });
        const plainBlob = new Blob([plain], { type: 'text/plain' });
        await navigator.clipboard.write([
          new window.ClipboardItem({
            'text/html': htmlBlob,
            'text/plain': plainBlob
          })
        ]);
        showToast(
          list.length === 1
            ? '✓ تم نسخ السؤال بتنسيق Microsoft Word بنجاح!'
            : '✓ تم نسخ ' + countStr + ' أسئلة بتنسيق Microsoft Word بنجاح!',
          'success',
          isSec
        );
        return true;
      }
    } catch (err) {
      // المتابعة للنسخ الاحتياطي عبر contenteditable
    }

    // المحاولة الثانية: عنصر contenteditable مخفي مع execCommand('copy') (يعمل حتى مع file:///)
    try {
      const div = document.createElement('div');
      div.setAttribute('contenteditable', 'true');
      div.setAttribute('dir', 'rtl');
      div.style.position = 'fixed';
      div.style.left = '-9999px';
      div.style.top = '0';
      div.style.opacity = '0';
      div.innerHTML = html;
      document.body.appendChild(div);

      const range = document.createRange();
      range.selectNodeContents(div);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);

      const ok = document.execCommand('copy');
      sel.removeAllRanges();
      document.body.removeChild(div);

      if (ok) {
        showToast(
          list.length === 1
            ? '✓ تم نسخ السؤال بتنسيق Microsoft Word بنجاح!'
            : '✓ تم نسخ ' + countStr + ' أسئلة بتنسيق Microsoft Word بنجاح!',
          'success',
          isSec
        );
        return true;
      }
    } catch (err2) {
      // المتابعة للنسخ النصي الصرف
    }

    try {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        await navigator.clipboard.writeText(plain);
        showToast('✓ تم نسخ النص بصيغة RTL.', 'success', isSec);
        return true;
      }
    } catch (err3) {
      showToast('تعذر النسخ التلقائي؛ يرجى التأكد من أذونات الحافظة.', 'error', isSec);
    }
    return false;
  }

  global.ArabicUtils = {
    EASTERN_DIGITS: EASTERN_DIGITS,
    CHOICE_LETTERS: CHOICE_LETTERS,
    WORD_CHOICE_LETTERS: WORD_CHOICE_LETTERS,
    SECONDARY_CHOICE_LETTERS: SECONDARY_CHOICE_LETTERS,
    isSecondaryStage: isSecondaryStage,
    RLM: RLM,
    LRM: LRM,
    toEasternDigits: toEasternDigits,
    toWesternDigits: toWesternDigits,
    formatStageDigits: formatStageDigits,
    toWesternNumber: toWesternNumber,
    formatMark: formatMark,
    formatMarkShort: formatMarkShort,
    escapeHtml: escapeHtml,
    getKatex: getKatex,
    format2DMatrixHtml: format2DMatrixHtml,
    renderLatexFormula: renderLatexFormula,
    renderMathHtml: renderMathHtml,
    stripMathToPlain: stripMathToPlain,
    stripMathToInputText: stripMathToInputText,
    formatArabicExponent: formatArabicExponent,
    formatMathExponents: formatMathExponents,
    formatMathForWordHtml: formatMathForWordHtml,
    normalizeSearchText: normalizeSearchText,
    resolveImageForClipboard: resolveImageForClipboard,
    buildWordClipboardHTML: buildWordClipboardHTML,
    buildWordClipboardPlain: buildWordClipboardPlain,
    copyQuestionsToWord: copyQuestionsToWord,
    showToast: showToast
  };
})(typeof window !== 'undefined' ? window : globalThis);
