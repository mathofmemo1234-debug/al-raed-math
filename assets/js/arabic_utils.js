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
      return val === 'g1s' || val === '1s' || val === 'secondary' || val === 'المرحلة الثانوية' || val.startsWith('g1s');
    }
    if (typeof val === 'object') {
      if (val.isSecondary || val.secondary) return true;
      if (val.id && (val.id === 'g1s' || val.id.startsWith('g1s'))) return true;
      if (val.bookId && (val.bookId === 'g1s' || val.bookId === '1s')) return true;
      if (val.gradeId && (val.gradeId === 'g1s' || val.gradeId === '1s')) return true;
      if (val.lessonId && val.lessonId.startsWith('g1s')) return true;
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
  const PAT_BASE_SUP_JS = /(\(-?[٠-٩0-9\w\s\+\-\*×÷\.]+\)|[٠-٩0-9]+|[أ-ي]+)\s*([⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+)/g;
  const PAT_CARET_JS = /(\(-?[٠-٩0-9\w\s\+\-\*×÷\.]+\)|[٠-٩0-9]+|[أ-ي]+)\s*\^\s*([٠-٩0-9]+)/g;

  /**
   * صياغة القوة والأس الرياضي باللغة العربية:
   * الأس دائماً على يسار الأساس وبالأرقام العربية المشرقية فقط (٠-٩)
   */
  function formatArabicExponent(base, exp) {
    const safeBase = toEasternDigits(String(base || '').trim());
    const safeExp = toEasternDigits(String(exp || '').trim());
    return '<span class="ar-pow"><span class="ar-base">' + safeBase + '</span><sup class="ar-exp">' + safeExp + '</sup></span>';
  }

  function formatMathExponents(input) {
    if (input === null || input === undefined) return '';
    let str = String(input);
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

    if (s.indexOf('&lt;') !== -1 && (s.indexOf('ar-pow') !== -1 || s.indexOf('sec-pow') !== -1 || s.indexOf('span') !== -1 || s.indexOf('sup') !== -1)) {
      s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
    }

    if (sec) {
      s = toWesternDigits(s);
      // الأسس والصيغ الإنجليزية للثانوي في Word
      s = s.replace(/<span\s+class=["'](?:sec-pow|ar-pow)["']\s*>\s*<span\s+class=["'](?:sec-base|ar-base)["']>([\s\S]*?)<\/span>\s*<sup\s+class=["'](?:sec-exp|ar-exp)["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        return '<span dir="ltr" style="direction:ltr; unicode-bidi:isolate; font-weight:bold;">' + base + '<sup style="font-size:75%; vertical-align:super;">' + exp + '</sup></span>';
      });
      // العبارات المحددة كـ sec-math
      s = s.replace(/<span\s+class=["'][^"']*sec-math[^"']*["'][^>]*>([\s\S]*?)<\/span>/gi, function (_, inner) {
        return '<span dir="ltr" style="direction:ltr; unicode-bidi:isolate; font-family:\'Times New Roman\',serif; font-style:italic; font-weight:bold;">' + inner + '</span>';
      });
      return s;
    }

    const powers = [];
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
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
    if (s.indexOf('ar-pow') === -1) {
      return s
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
    }
    const powers = [];
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const ph = '___ARPOW' + numToAlpha(powers.length) + '___';
      powers.push({ base: base, exp: exp });
      return ph;
    });
    s = s
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
    powers.forEach(function (p, i) {
      const ph = '___ARPOW' + numToAlpha(i) + '___';
      s = s.split(ph).join('<span class="ar-pow"><span class="ar-base">' + p.base + '</span><sup class="ar-exp">' + p.exp + '</sup></span>');
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

    if (s.indexOf('&lt;') !== -1 && (s.indexOf('ar-pow') !== -1 || s.indexOf('sec-pow') !== -1 || s.indexOf('span') !== -1 || s.indexOf('sup') !== -1)) {
      s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
    }

    if (sec) {
      // المرحلة الثانوية: أرقام إنجليزية (0-9) حصراً + اتجاه LTR للمعادلات والرموز الجبرية
      s = toWesternDigits(s);
      const secTags = [];
      s = s.replace(/<span\s+[^>]*>[\s\S]*?<\/span>/gi, function (fullTag) {
        const ph = '___SECTAG' + numToAlpha(secTags.length) + '___';
        secTags.push(fullTag);
        return ph;
      });

      // صياغة الأسس الإنجليزية مثل x^2 أو (x+3)^2
      s = s.replace(/(\(-?[0-9a-zA-Z\s\+\-\*\/=]+\)|[0-9a-zA-Z]+)\s*\^\s*([0-9a-zA-Z]+)/g, function (_, base, exp) {
        return '<span class="sec-pow" dir="ltr"><span class="sec-base">' + escapeHtml(base) + '</span><sup class="sec-exp">' + escapeHtml(exp) + '</sup></span>';
      });

      // صياغة العبارات والمعادلات الإنجليزية المباشرة مثل y = 2x + 1 أو DE = 8x - 3 أو m∠A + m∠B = 90° إذا لم تكن مضمنة في وسم
      s = s.replace(/(?<![\w\>])([A-Z][a-zA-Z0-9_\'\^\*\+\-\/\s\=∠≅△°~><]{2,}[A-Za-z0-9°])(?![\w\<])/g, function (match) {
        if (match.indexOf('___SECTAG') !== -1 || match.indexOf('sec-pow') !== -1) return match;
        // إذا كان تعبيراً رياضياً يحتوي على رمز رياضي أو مساواة
        if (/[=\+\-∠≅△°~><^]/.test(match) && !/[أ-ي]/.test(match)) {
          return '<span class="sec-math ltr-math" dir="ltr">' + match + '</span>';
        }
        return match;
      });

      secTags.forEach(function (tag, i) {
        const ph = '___SECTAG' + numToAlpha(i) + '___';
        s = s.split(ph).join(tag);
      });

      return s;
    }

    // المرحلة الابتدائية والمتوسطة: الأرقام العربية المشرقية والأسس على يسار الأساس
    const powers = [];
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const ph = '___ARPOW' + numToAlpha(powers.length) + '___';
      powers.push({
        base: toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim()),
        exp: toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim())
      });
      return ph;
    });

    s = formatMathExponents(s);
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
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
    if (sec) {
      s = s.replace(/<span\s+class=["'](?:sec-pow|ar-pow)["']\s*>\s*<span\s+class=["'](?:sec-base|ar-base)["']>([\s\S]*?)<\/span>\s*<sup\s+class=["'](?:sec-exp|ar-exp)["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        const b = toWesternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
        const e = toWesternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
        return b + '^' + e;
      });
      return toWesternDigits(s.replace(/<[^>]+>/g, '').trim());
    }
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
      const b = toEasternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
      const e = toEasternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
      if (/^(كلم|سم|م|ملم|دسم)$/.test(b) && e === '٢') {
        return b + '²';
      }
      if (/^(كلم|سم|م|ملم|دسم)$/.test(b) && e === '٣') {
        return b + '³';
      }
      return b + ' (أس ' + e + ')';
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
      s = s.replace(/<span\s+class=["'](?:sec-pow|ar-pow)["']\s*>\s*<span\s+class=["'](?:sec-base|ar-base)["']>([\s\S]*?)<\/span>\s*<sup\s+class=["'](?:sec-exp|ar-exp)["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        const b = toWesternDigits(String(base || '').replace(/<[^>]+>/g, '').trim());
        const e = toWesternDigits(String(exp || '').replace(/<[^>]+>/g, '').trim());
        return b + '^' + e;
      });
      return toWesternDigits(s.replace(/<[^>]+>/g, '').trim());
    }
    s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
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
