/**
 * ==========================================================================
 * محرك التصدير المزدوج للاختبارات (Word .docx + PDF + معاينة A4 حية)
 * منصة الرائد التعليمية الذكية للرياضيات | الصف السادس الابتدائي
 * يدعم العمل مع السيرفر المحلي (/api/export/*) والعمل المباشر دون خادم (file:///)
 * ==========================================================================
 */

(function (global) {
  'use strict';

  function getUtils() {
    return global.ArabicUtils;
  }

  function escXml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
  }

  function groupQuestions(questions, groupByType) {
    const list = Array.isArray(questions) ? questions : [];
    if (!groupByType) {
      return [{ title: 'أسئلة الاختبار', items: list }];
    }
    const mcqs = list.filter(function (q) { return q.type === 'mcq'; });
    const tfs = list.filter(function (q) { return q.type === 'tf'; });
    const essays = list.filter(function (q) { return q.type !== 'mcq' && q.type !== 'tf'; });

    const ordinals = ['السؤال الأول', 'السؤال الثاني', 'السؤال الثالث'];
    const defs = [
      { desc: 'اختر الإجابة الصحيحة لكل فقرة مما يأتي:', items: mcqs },
      { desc: 'ضع علامة (✓) أمام العبارة الصحيحة وعلامة (✗) أمام العبارة الخاطئة:', items: tfs },
      { desc: 'أجب عن المسائل الآتية موضحاً خطوات الحل:', items: essays }
    ];
    const sections = [];
    let ordIdx = 0;
    defs.forEach(function (d) {
      if (d.items.length) {
        const prefix = ordinals[ordIdx] ? (ordinals[ordIdx] + ': ') : '';
        sections.push({ title: prefix + d.desc, items: d.items });
        ordIdx++;
      }
    });
    return sections;
  }

  function computeTotalMarks(questions) {
    const utils = getUtils();
    return (questions || []).reduce(function (sum, q) {
      return sum + utils.toWesternNumber(q.marks !== undefined ? q.marks : 1, 1);
    }, 0);
  }

  const WORD_CHOICE_LETTERS = ['أ', 'ب', 'جـ', 'د', 'هـ', 'و'];

  function splitTypeRuns(items) {
    const runs = [];
    (items || []).forEach(function (q) {
      const qt = (q.type === 'mcq' || q.type === 'tf' || q.type === 'essay')
        ? q.type
        : (q.options ? 'mcq' : (typeof q.is_true === 'boolean' ? 'tf' : 'essay'));
      if (!runs.length || runs[runs.length - 1].type !== qt) {
        runs.push({ type: qt, items: [q] });
      } else {
        runs[runs.length - 1].items.push(q);
      }
    });
    return runs;
  }

  /**
   * بناء HTML معاينة ورقة الاختبار A4 بنظام RTL وأرقام مشرقية
   * مطابق لترويسة وجداول وحدود النموذج الرسمي المعتمد
   */
  function buildExamPreviewHTML(examData, opts) {
    const utils = getUtils();
    const o = Object.assign({ forPrint: false }, opts || {});
    const header = examData.header || {};
    const questions = examData.questions || [];
    const options = examData.options || {};

    const isSec = !!(examData.isSecondary || (utils && utils.isSecondaryStage && utils.isSecondaryStage(header)) || (questions[0] && (questions[0].gradeId === 'g1s' || questions[0].gradeId === 'g2s')));
    const dNum = function (v) {
      const s = v === null || v === undefined ? '' : String(v);
      return isSec ? (utils && utils.toWesternDigits ? utils.toWesternDigits(s) : s) : (utils ? utils.toEasternDigits(s) : s);
    };
    const choiceLetters = (isSec && utils && utils.SECONDARY_CHOICE_LETTERS) ? utils.SECONDARY_CHOICE_LETTERS : WORD_CHOICE_LETTERS;

    const totalMarks = computeTotalMarks(questions);
    const totalStr = utils.formatMarkShort(totalMarks, isSec);
    const sections = groupQuestions(questions, options.groupByType !== false);
    const includeLogo = header.includeLogo !== false;
    const includeAnswerKey = options.includeAnswerKey !== false;

    function renderA4Figure(q, extraClass) {
      if (!q || !q.image) return '';
      const cap = q.imageCaption ? utils.escapeHtml(dNum(q.imageCaption)) : '';
      return (
        '<div class="a4-q-fig ' + (extraClass || '') + '">' +
        '<img src="' + utils.escapeHtml(q.image) + '" alt="' + (cap || 'شكل السؤال') + '" />' +
        (cap ? '<div class="a4-q-fig-cap">' + cap + '</div>' : '') +
        '</div>'
      );
    }

    function formatMathForDoc(text) {
      if (text === null || text === undefined) return '';
      if (utils && utils.renderMathHtml) {
        return utils.renderMathHtml(text, isSec);
      }
      let s = String(text);
      if (s.indexOf('&lt;') !== -1 && (s.indexOf('ar-pow') !== -1 || s.indexOf('span') !== -1)) {
        s = s.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
      }
      const powers = [];
      s = s.replace(/<span\s+class=["']ar-pow["']\s*>\s*<span\s+class=["']ar-base["']>([\s\S]*?)<\/span>\s*<sup\s+class=["']ar-exp["']>([\s\S]*?)<\/sup>\s*<\/span>/gi, function (_, base, exp) {
        const ph = '___ARPOW_' + powers.length + '___';
        powers.push({ base: dNum(base), exp: dNum(exp) });
        return ph;
      });
      s = utils.escapeHtml(dNum(s));
      powers.forEach(function (p, i) {
        const ph = '___ARPOW_' + i + '___';
        s = s.replace(ph, '<span class="ar-pow"><span class="ar-base">' + p.base + '</span><sup class="ar-exp">' + p.exp + '</sup></span>');
      });
      return s;
    }

    let globalQ = 0;
    const sectionsHtml = sections.map(function (sec) {
      const secMarks = computeTotalMarks(sec.items);
      const secMarksStr = utils.formatMarkShort(secMarks, isSec);
      const secHeader =
        '<div class="a4-doc-sec-bar">' +
        '<div class="a4-doc-sec-title">' + utils.escapeHtml(dNum(sec.title)) + '</div>' +
        '<table class="a4-doc-score-box" dir="rtl">' +
        '<tr><td class="a4-doc-score-top">الدرجة</td></tr>' +
        '<tr><td class="a4-doc-score-val"><span class="a4-doc-score-blank"></span> / ' + utils.escapeHtml(secMarksStr) + '</td></tr>' +
        '</table>' +
        '</div>';

      const runTables = splitTypeRuns(sec.items).map(function (runGrp) {
        const rtype = runGrp.type;
        const ritems = runGrp.items;

        if (rtype === 'mcq') {
          const tbodies = ritems.map(function (q) {
            globalQ++;
            const qText = formatMathForDoc(q.q || q.statement || '');
            const qOpts = (q.options || []).slice(0, 4);
            while (qOpts.length < 4) qOpts.push('');
            const optTds = qOpts.map(function (opt, idx) {
              const letCh = choiceLetters[idx] || (isSec ? 'A' : 'أ');
              return (
                '<td class="a4-doc-mcq-let">' + letCh + '</td>' +
                '<td class="a4-doc-mcq-opt">' + formatMathForDoc(opt) + '</td>'
              );
            }).join('');
            return (
              '<tbody class="a4-q-pair">' +
              '<tr>' +
              '<td rowspan="2" class="a4-doc-num">' + dNum(globalQ) + '</td>' +
              '<td colspan="8" class="a4-doc-prompt">' + qText + renderA4Figure(q) + '</td>' +
              '</tr>' +
              '<tr>' + optTds + '</tr>' +
              '</tbody>'
            );
          }).join('');
          return '<table class="a4-doc-mcq-tbl" dir="rtl">' + tbodies + '</table>';
        }

        if (rtype === 'tf') {
          const rows = ritems.map(function (q) {
            globalQ++;
            return (
              '<tr>' +
              '<td class="a4-doc-tf-num">' + dNum(globalQ) + '</td>' +
              '<td class="a4-doc-tf-stmt">' + formatMathForDoc(q.statement || q.q || '') + renderA4Figure(q, 'a4-q-fig-tf') + '</td>' +
              '<td class="a4-doc-tf-ans">( &nbsp;&nbsp;&nbsp;&nbsp; )</td>' +
              '</tr>'
            );
          }).join('');
          return (
            '<table class="a4-doc-tf-tbl" dir="rtl">' +
            '<thead><tr><th colspan="3">ضع علامة ( ✓ ) أمام العبارة الصحيحة وعلامة ( ✗ ) أمام العبارة الخاطئة:</th></tr></thead>' +
            '<tbody>' + rows + '</tbody>' +
            '</table>'
          );
        }

        const esBodies = ritems.map(function (q) {
          globalQ++;
          const qText = formatMathForDoc(q.q || q.statement || '');
          const lc = Math.max(2, Math.min(6, Math.round(utils.toWesternNumber(q.lines, 3))));
          let dotsHtml = '';
          for (let l = 0; l < lc; l++) {
            dotsHtml += '<div class="a4-doc-es-dot">' + (l === 0 ? '<strong>الحل / </strong>' : '') + '</div>';
          }
          return (
            '<tbody class="a4-q-pair">' +
            '<tr>' +
            '<td rowspan="2" class="a4-doc-es-num">' + dNum(globalQ) + '</td>' +
            '<td class="a4-doc-es-prompt">' + qText + renderA4Figure(q) + '</td>' +
            '</tr>' +
            '<tr>' +
            '<td class="a4-doc-es-sol">' + dotsHtml + '</td>' +
            '</tr>' +
            '</tbody>'
          );
        }).join('');
        return '<table class="a4-doc-es-tbl" dir="rtl">' + esBodies + '</table>';
      }).join('');

      return '<section class="a4-sec">' + secHeader + runTables + '</section>';
    }).join('');

    let answerKeyHtml = '';
    if (includeAnswerKey && questions.length) {
      const ordered = [];
      sections.forEach(function (s) {
        s.items.forEach(function (it) { ordered.push(it); });
      });
      const akRows = ordered.map(function (q, idx) {
        let tLbl = 'اختيار من متعدد';
        let ansTxt = '';
        if (q.type === 'mcq') {
          const cIdx = typeof q.correct === 'number' ? q.correct : 0;
          const letter = choiceLetters[cIdx] || (isSec ? 'A' : 'أ');
          const optVal = (q.options && q.options[cIdx]) ? q.options[cIdx] : '';
          ansTxt = letter + ') ' + optVal + (q.explanation ? (' — ' + q.explanation) : '');
        } else if (q.type === 'tf') {
          tLbl = 'صواب وخطأ';
          ansTxt = (q.is_true ? 'صواب (✓)' : 'خطأ (✗)') + (q.explanation ? (' — ' + q.explanation) : '');
        } else {
          tLbl = 'مسألة مقالية';
          ansTxt = q.ans || '';
        }
        return (
          '<tr>' +
          '<td class="a4-c-num">' + dNum(idx + 1) + '</td>' +
          '<td>' + tLbl + '</td>' +
          '<td class="a4-ak-ans">' + formatMathForDoc(ansTxt) + '</td>' +
          '<td class="a4-c-num">' + utils.escapeHtml(utils.formatMarkShort(q.marks !== undefined ? q.marks : 1, isSec)) + '</td>' +
          '</tr>'
        );
      }).join('');

      answerKeyHtml =
        '<div class="a4-page-break"></div>' +
        '<div class="a4-ak-header">نموذج الإجابة وتوزيع الدرجات — ' + utils.escapeHtml(dNum(header.examTitle || 'اختبار الرياضيات')) + '</div>' +
        '<table class="a4-ak-tbl" dir="rtl">' +
        '<thead><tr><th class="a4-c-num">س</th><th>النوع</th><th>الإجابة النموذجية والشرح</th><th class="a4-c-num">الدرجة</th></tr></thead>' +
        '<tbody>' + akRows + '</tbody>' +
        '</table>' +
        '<div class="a4-ak-total">المجموع الكلي للدرجات: ' + utils.escapeHtml(totalStr) + ' درجة</div>';
    }

    const instructions = (header.instructions || '').trim();
    const instHtml = instructions
      ? '<div class="a4-inst-box"><strong>تعليمات:</strong> ' + utils.escapeHtml(dNum(instructions)) + '</div>'
      : '';

    const logoSrc = (header.customLogoDataUrl || '').trim() || 'assets/img/my_logo.png';
    const logoHtml = includeLogo
      ? '<img src="' + utils.escapeHtml(logoSrc) + '" alt="شعار المدرسة" class="a4-doc-school-logo" onerror="this.style.display=\'none\'">'
      : '';

    const rightLinesHtml = [
      header.ministry || 'المملكة العربية السعودية',
      header.district || 'الإدارة العامة للتعليم بمحافظة جدة',
      header.schoolCompany || '',
      header.school || 'منصة الرائد التعليمية',
      header.stage || ''
    ].filter(function (v) { return (v || '').trim(); }).map(function (v) {
      return '<div>' + utils.escapeHtml(dNum(v)) + '</div>';
    }).join('');

    const teacherName = utils.escapeHtml(dNum(header.teacher || 'أ. محمد عبدالله جمعة'));
    const principalName = utils.escapeHtml(dNum(header.principal || ''));

    const docBodyContent = `
      <img src="assets/img/exam_top_ribbon.png" alt="" class="a4-doc-top-ribbon" onerror="this.style.display='none'">
      <table class="a4-doc-hdr-tbl" dir="rtl">
        <tr>
          <td class="a4-doc-hdr-right">${rightLinesHtml}</td>
          <td class="a4-doc-hdr-mid">
            <img src="assets/img/moe_logo.png" alt="وزارة التعليم" class="a4-doc-moe-logo" onerror="this.style.display='none'">
            <div class="a4-doc-title">${utils.escapeHtml(dNum(header.examTitle || 'اختبار مادة الرياضيات'))}</div>
            <div class="a4-doc-sub">المادة: ${utils.escapeHtml(dNum(header.subject || 'الرياضيات'))} &nbsp;|&nbsp; الصف: ${utils.escapeHtml(dNum(header.grade || ''))} &nbsp;|&nbsp; الفصل: ${utils.escapeHtml(dNum(header.term || 'الأول'))}</div>
            <div class="a4-doc-sub">العام الدراسي: ${utils.escapeHtml(dNum(header.year || (isSec ? '1448 هـ' : '١٤٤٨ هـ')))} &nbsp;|&nbsp; الزمن: ${utils.escapeHtml(dNum(header.duration || (isSec ? '45 دقيقة' : '٤٥ دقيقة')))}</div>
          </td>
          <td class="a4-doc-hdr-left">${logoHtml}</td>
        </tr>
      </table>

      <table class="a4-doc-stu-tbl" dir="rtl">
        <tr>
          <td class="a4-doc-stu-lbl">اسم الطالب</td>
          <td class="a4-doc-stu-fill">................................................................................</td>
          <td class="a4-doc-score-top">الدرجة الكلية</td>
        </tr>
        <tr>
          <td class="a4-doc-stu-lbl">الصف</td>
          <td class="a4-doc-stu-fill">${utils.escapeHtml(dNum(header.grade || ''))} &nbsp;/&nbsp; ( &nbsp;&nbsp;&nbsp;&nbsp; )</td>
          <td class="a4-doc-score-val">&nbsp;&nbsp;&nbsp;&nbsp; / ${utils.escapeHtml(totalStr)}</td>
        </tr>
      </table>

      ${instHtml}
      ${sectionsHtml || '<div style="text-align:center; padding:32px; color:#64748b;">لا توجد أسئلة مضافة للاختبار بعد.</div>'}

      <div class="a4-doc-closing">
        <div class="a4-doc-blessing">انتهت الأسئلة &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; مع خالص الدعوات بالتوفيق والنجاح</div>
        <table class="a4-doc-sig-tbl" dir="rtl">
          <tr>
            <td><div>معلم المادة</div><div>${teacherName}</div></td>
            <td><div>مدير المدرسة</div><div>${principalName}</div></td>
          </tr>
        </table>
        <img src="assets/img/exam_bottom_ribbon.png" alt="جيل ينتج المعرفة" class="a4-doc-bot-ribbon" onerror="this.style.display='none'">
      </div>
      ${answerKeyHtml}
    `;

    if (!o.forPrint) {
      return '<div class="a4-paper-sheet a4-doc-sheet" dir="rtl" lang="ar">' + docBodyContent + '</div>';
    }

    return `<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<title>${utils.escapeHtml(dNum(header.examTitle || 'اختبار الرياضيات'))}</title>
<link rel="stylesheet" href="assets/vendor/katex/katex.min.css">
<style>
  .katex, .sec-math .katex, .ltr-math .katex { direction: ltr !important; unicode-bidi: isolate !important; font-style: normal !important; font-weight: 400 !important; font-family: KaTeX_Main, 'Times New Roman', serif !important; vertical-align: middle !important; }
  .ar-frac { display: inline-flex !important; flex-direction: column !important; align-items: center !important; vertical-align: middle !important; line-height: 1.05 !important; margin: 0 3px !important; font-weight: 700 !important; font-size: 0.92em !important; }
  .ar-frac-num { display: block !important; padding: 0 3px 1.5px 3px !important; border-bottom: 1.4px solid #000 !important; text-align: center !important; }
  .ar-frac-den { display: block !important; padding: 1.5px 3px 0 3px !important; text-align: center !important; }
  .sec-exp { font-size: 0.72em !important; font-weight: 700 !important; font-style: normal !important; vertical-align: super !important; line-height: 0 !important; }
  .sec-matrix-container { display: inline-flex; align-items: stretch; vertical-align: middle; margin: 0 4px; direction: ltr !important; unicode-bidi: isolate; font-family: 'Cambria Math', 'Times New Roman', serif; line-height: 1.2; }
  .sec-det-container { border-left: 1.8px solid #000; border-right: 1.8px solid #000; padding: 2px 6px; }
  .sec-bracket-container { border-left: 1.8px solid #000; border-right: 1.8px solid #000; position: relative; padding: 2px 6px; }
  .sec-matrix-table { display: inline-flex; flex-direction: column; justify-content: center; gap: 3px; padding: 1px; }
  .sec-matrix-row { display: flex; justify-content: space-around; gap: 10px; }
  .sec-matrix-cell { min-width: 16px; text-align: center; font-size: 0.95em; white-space: nowrap; }
  @page { size: A4 portrait; margin: 8mm; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Cairo', 'Tajawal', 'Segoe UI', 'Arial', sans-serif; direction: rtl; text-align: right; background: #fff; color: #000; font-size: 11px; line-height: 1.4; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .page-frame-fixed { position: fixed; top: 0; right: 0; bottom: 0; left: 0; border: 2px solid #000; box-shadow: inset 0 0 0 2px #fff, inset 0 0 0 3.2px #000; pointer-events: none; z-index: 9999; }
  .print-shell-tbl { width: 100%; border-collapse: collapse; border: none; }
  .print-shell-tbl > thead > tr > td, .print-shell-tbl > tfoot > tr > td { height: 4mm; border: none; }
  .print-shell-tbl > tbody > tr > td { padding: 0 5mm; border: none; vertical-align: top; }
  .a4-doc-top-ribbon { width: 100%; max-height: 36px; display: block; object-fit: cover; margin-bottom: 3px; }
  .a4-doc-hdr-tbl { width: 100%; border-collapse: collapse; border-bottom: 3px solid #3F9E35; margin-bottom: 6px; }
  .a4-doc-hdr-tbl td { border: none; padding: 3px 6px 6px 6px; vertical-align: middle; }
  .a4-doc-hdr-right { width: 35%; text-align: center; font-weight: 700; font-size: 11.5px; line-height: 1.42; }
  .a4-doc-hdr-mid { width: 41%; text-align: center; }
  .a4-doc-hdr-left { width: 24%; text-align: center; }
  .a4-doc-moe-logo { max-height: 48px; width: auto; display: block; margin: 0 auto 3px auto; }
  .a4-doc-school-logo { max-width: 118px; max-height: 76px; width: auto; height: auto; display: block; margin: 0 auto; object-fit: contain; }
  .a4-doc-title { font-size: 14px; font-weight: 800; color: #000; }
  .a4-doc-sub { font-size: 11px; color: #1e293b; font-weight: 600; margin-top: 2px; }
  .a4-doc-stu-tbl { width: 100%; border-collapse: collapse; margin-bottom: 6px; }
  .a4-doc-stu-tbl td { border: 1px solid #000; padding: 4px 8px; font-size: 12px; }
  .a4-doc-stu-lbl { width: 14%; background: #F2F2F2; font-weight: 800; text-align: center; }
  .a4-doc-stu-fill { width: 67%; text-align: right; font-weight: 700; }
  .a4-doc-score-top { width: 19%; background: #F2F2F2; font-weight: 800; text-align: center; font-size: 11.5px; padding: 3px 6px; border: 1px solid #000; }
  .a4-doc-score-val { width: 19%; font-weight: 800; text-align: center; font-size: 13px; padding: 3px 6px; border: 1px solid #000; }
  .a4-inst-box { background: #fefce8; border: 1px solid #fde047; border-right: 3px solid #eab308; padding: 4px 8px; margin-bottom: 6px; font-size: 11px; }
  .a4-sec { margin-bottom: 8px; }
  .a4-doc-sec-bar { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin: 7px 0 4px 0; break-inside: avoid; page-break-inside: avoid; break-after: avoid; page-break-after: avoid; }
  .a4-doc-sec-title { flex: 1; text-align: right; font-weight: 800; font-size: 13.5px; color: #000; }
  .a4-doc-score-box { width: 19%; min-width: 110px; border-collapse: collapse; flex-shrink: 0; break-inside: avoid; page-break-inside: avoid; }
  .a4-doc-score-blank { display: inline-block; min-width: 28px; }
  .a4-doc-mcq-tbl, .a4-doc-tf-tbl, .a4-doc-es-tbl { width: 100%; border-collapse: collapse; margin-bottom: 6px; border: 1.2px solid #000; }
  tbody.a4-q-pair { break-inside: avoid; }
  .a4-doc-mcq-tbl td, .a4-doc-tf-tbl td, .a4-doc-tf-tbl th, .a4-doc-es-tbl td { border: 1px solid #000; padding: 3px 5px; font-size: 10.5px; vertical-align: middle; }
  .a4-doc-num { width: 5.5%; text-align: center; font-weight: 800; background: #fff; }
  .a4-doc-prompt { width: 94.5%; background: #F2F2F2; font-weight: 700; text-align: right; vertical-align: top; }
  .a4-doc-mcq-let { width: 4.5%; text-align: center; font-weight: 800; background: #fff; }
  .a4-doc-mcq-opt { width: 19.1%; text-align: right; background: #fff; }
  .a4-doc-tf-tbl th { background: #F2F2F2; font-weight: 800; text-align: center; }
  .a4-doc-tf-tbl tr { break-inside: avoid; }
  .a4-doc-tf-num { width: 8%; text-align: center; font-weight: 800; }
  .a4-doc-tf-stmt { width: 78%; text-align: right; font-weight: 600; }
  .a4-doc-tf-ans { width: 14%; text-align: center; font-weight: 700; white-space: nowrap; }
  .a4-doc-es-num { width: 8%; text-align: center; font-weight: 800; background: #fff; }
  .a4-doc-es-prompt { width: 92%; background: #F2F2F2; font-weight: 700; text-align: right; vertical-align: top; }
  .a4-doc-es-sol { width: 92%; background: #fff; vertical-align: top; padding: 5px 8px; }
  .a4-doc-es-dot { border-bottom: 1px dotted #64748b; height: 22px; margin-top: 2px; font-size: 11.5px; color: #334155; }
  .a4-q-fig { text-align: center; margin: 5px auto 3px auto; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; background: #fff; display: block; width: fit-content; max-width: 94%; }
  .a4-q-fig img { max-width: 280px; max-height: 145px; width: auto; height: auto; display: block; margin: 0 auto; object-fit: contain; }
  .a4-q-fig.a4-q-fig-tf img { max-width: 205px; max-height: 100px; }
  .a4-q-fig-cap { font-size: 10px; color: #475569; margin-top: 2px; }
  .a4-doc-closing { break-inside: avoid; margin-top: 10px; }
  .a4-doc-blessing { text-align: center; font-weight: 800; font-size: 13px; margin-bottom: 6px; }
  .a4-doc-sig-tbl { width: 100%; border-collapse: collapse; border: none; margin-bottom: 6px; }
  .a4-doc-sig-tbl td { width: 50%; border: none; text-align: center; font-weight: 700; font-size: 12px; padding: 2px 6px; }
  .a4-doc-bot-ribbon { width: 100%; max-height: 28px; display: block; object-fit: contain; }
  .a4-page-break { page-break-before: always; break-before: page; }
  .a4-ak-header { text-align: center; font-size: 15px; font-weight: 800; color: #047857; border: 2px solid #047857; background: #ecfdf5; padding: 7px; margin-bottom: 8px; }
  .a4-ak-tbl { width: 100%; border-collapse: collapse; }
  .a4-ak-tbl th, .a4-ak-tbl td { border: 1px solid #6ee7b7; padding: 4px 7px; font-size: 11.5px; }
  .a4-ak-tbl th { background: #d1fae5; color: #065f46; }
  .a4-c-num { width: 38px; text-align: center; font-weight: 800; color: #1e3a8a; }
  .a4-ak-ans { color: #065f46; font-weight: 600; }
  .a4-ak-total { margin-top: 8px; text-align: left; font-weight: 800; color: #1e3a8a; }
  /* صياغة الأسس والقوى الرياضية (الأس دائماً في أعلى يسار الأساس بالأرقام المشرقية) */
  .ar-pow {
    display: inline-flex !important;
    flex-direction: row !important;
    direction: rtl !important;
    align-items: flex-start !important;
    unicode-bidi: isolate !important;
    vertical-align: baseline !important;
    margin: 0 2px !important;
    line-height: 1 !important;
    position: relative !important;
  }
  .ar-base {
    display: inline-block !important;
    font-family: inherit !important;
    font-size: 1em !important;
    line-height: 1.15 !important;
  }
  .ar-exp {
    display: inline-block !important;
    font-size: 0.62em !important;
    font-weight: 800 !important;
    line-height: 1 !important;
    font-family: inherit !important;
    transform: translateY(-0.48em) !important;
    position: relative !important;
    top: -0.1em !important;
    margin-right: 2px !important;
    margin-left: 1px !important;
    color: inherit !important;
  }
  .sec-math, .ltr-math {
    direction: ltr !important;
    unicode-bidi: isolate !important;
    display: inline-block;
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-style: italic;
  }
  .sec-pow {
    display: inline-block !important;
    direction: ltr !important;
    unicode-bidi: isolate !important;
    vertical-align: baseline !important;
    margin: 0 !important;
    line-height: 1 !important;
  }
  .sec-pow .sec-base {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 1em;
  }
  .sec-pow .sec-exp {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 0.72em;
    font-weight: 700;
    font-style: normal;
    vertical-align: super;
    line-height: 0;
    margin-left: 1px;
  }
  .sec-sub {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 0.72em;
    font-style: normal;
    vertical-align: sub;
    line-height: 0;
  }
</style>
</head>
<body>
  <div class="page-frame-fixed"></div>
  <table class="print-shell-tbl" dir="rtl">
    <thead><tr><td></td></tr></thead>
    <tfoot><tr><td></td></tr></tfoot>
    <tbody><tr><td>${docBodyContent}</td></tr></tbody>
  </table>
</body>
</html>`;
  }

  // ========================================================================
  // Pure-JS Offline OOXML (.docx) ZIP (Store + CRC32) Builder
  // ========================================================================
  const CRC_TABLE = (function () {
    const table = new Uint32Array(256);
    for (let n = 0; n < 256; n++) {
      let c = n;
      for (let k = 0; k < 8; k++) {
        c = (c & 1) ? (0xedb88320 ^ (c >>> 1)) : (c >>> 1);
      }
      table[n] = c >>> 0;
    }
    return table;
  })();

  function crc32(bytes) {
    let c = 0xffffffff;
    for (let i = 0; i < bytes.length; i++) {
      c = CRC_TABLE[(c ^ bytes[i]) & 0xff] ^ (c >>> 8);
    }
    return (c ^ 0xffffffff) >>> 0;
  }

  function encodeUtf8(str) {
    if (typeof TextEncoder !== 'undefined') {
      return new TextEncoder().encode(str);
    }
    const buf = Buffer.from(str, 'utf8');
    return new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);
  }

  function createZipStore(files) {
    const localParts = [];
    const centralParts = [];
    let offset = 0;

    files.forEach(function (file) {
      const nameBytes = encodeUtf8(file.name);
      const dataBytes = typeof file.content === 'string' ? encodeUtf8(file.content) : file.content;
      const crc = crc32(dataBytes);

      const lh = new Uint8Array(30 + nameBytes.length);
      const lv = new DataView(lh.buffer);
      lv.setUint32(0, 0x04034b50, true);
      lv.setUint16(4, 20, true);
      lv.setUint16(6, 0x0800, true); // UTF-8
      lv.setUint16(8, 0, true); // Store
      lv.setUint16(10, 0, true);
      lv.setUint16(12, 0, true);
      lv.setUint32(14, crc, true);
      lv.setUint32(18, dataBytes.length, true);
      lv.setUint32(22, dataBytes.length, true);
      lv.setUint16(26, nameBytes.length, true);
      lv.setUint16(28, 0, true);
      lh.set(nameBytes, 30);

      localParts.push(lh, dataBytes);

      const cd = new Uint8Array(46 + nameBytes.length);
      const cv = new DataView(cd.buffer);
      cv.setUint32(0, 0x02014b50, true);
      cv.setUint16(4, 20, true);
      cv.setUint16(6, 20, true);
      cv.setUint16(8, 0x0800, true);
      cv.setUint16(10, 0, true);
      cv.setUint16(12, 0, true);
      cv.setUint16(14, 0, true);
      cv.setUint32(16, crc, true);
      cv.setUint32(20, dataBytes.length, true);
      cv.setUint32(24, dataBytes.length, true);
      cv.setUint16(28, nameBytes.length, true);
      cv.setUint16(30, 0, true);
      cv.setUint16(32, 0, true);
      cv.setUint16(34, 0, true);
      cv.setUint16(36, 0, true);
      cv.setUint32(38, 0, true);
      cv.setUint32(42, offset, true);
      cd.set(nameBytes, 46);
      centralParts.push(cd);

      offset += lh.length + dataBytes.length;
    });

    let cdSize = 0;
    centralParts.forEach(function (p) { cdSize += p.length; });

    const eocd = new Uint8Array(22);
    const ev = new DataView(eocd.buffer);
    ev.setUint32(0, 0x06054b50, true);
    ev.setUint16(4, 0, true);
    ev.setUint16(6, 0, true);
    ev.setUint16(8, files.length, true);
    ev.setUint16(10, files.length, true);
    ev.setUint32(12, cdSize, true);
    ev.setUint32(16, offset, true);
    ev.setUint16(20, 0, true);

    const totalLen = offset + cdSize + eocd.length;
    const out = new Uint8Array(totalLen);
    let pos = 0;
    localParts.forEach(function (p) { out.set(p, pos); pos += p.length; });
    centralParts.forEach(function (p) { out.set(p, pos); pos += p.length; });
    out.set(eocd, pos);
    return out;
  }

  function wRun(text, opts) {
    const utils = getUtils();
    const o = Object.assign({ sizePt: 14, bold: false, color: '0F172A', sup: false, isSecondary: false, ltr: false }, opts || {});
    let textStr = String(text || '');
    // Normalize LaTeX / legacy / bracket matrices cleanly before Word XML run serialization
    // so formatMathExponents never injects KaTeX HTML/MathML into DOCX XML runs
    const _cleanRowSpan = function (html) {
      return String(html || '')
        .replace(/<[^>]+>/g, '')
        .replace(/&nbsp;|\u00a0/g, '  ')
        .replace(/&minus;|−/g, '-')
        .trim();
    };
    textStr = textStr
      .replace(/\\begin\{(vmatrix|matrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
        const rows = body.trim().split('\\\\').map(function (r) {
          return r.split('&').map(function (c) { return c.trim(); }).join('  ');
        });
        return '| ' + rows.join(' ; ') + ' |';
      })
      .replace(/\\begin\{(bmatrix|pmatrix)\}([\s\S]*?)\\end\{\1\}/g, function (_, env, body) {
        const rows = body.trim().split('\\\\').map(function (r) {
          return r.split('&').map(function (c) { return c.trim(); }).join('  ');
        });
        return '[ ' + rows.join(' ; ') + ' ]';
      })
      .replace(/\|\s*(<span\s+class=["']sec-row["']>[\s\S]*?<\/span>(?:\s*,\s*<span\s+class=["']sec-row["']>[\s\S]*?<\/span>)*)\s*\|/gi, function (_, body) {
        const rows = (body.match(/<span\s+class=["']sec-row["']>[\s\S]*?<\/span>/gi) || []).map(_cleanRowSpan);
        return rows.length ? ('| ' + rows.join(' ; ') + ' |') : _;
      })
      .replace(/<span\s+class=["']sec-brack["']>\[<\/span>\s*([\s\S]*?)\s*<span\s+class=["']sec-brack["']>\]<\/span>/gi, function (_, body) {
        const rowSpans = body.match(/<span\s+class=["']sec-row["']>[\s\S]*?<\/span>/gi);
        if (rowSpans && rowSpans.length) {
          return '[ ' + rowSpans.map(_cleanRowSpan).join(' ; ') + ' ]';
        }
        return '[ ' + _cleanRowSpan(body) + ' ]';
      })
      .replace(/\|\s*\[(\[[^\[\]]+\](?:\s*,\s*\[[^\[\]]+\])*)\]\s*\|/g, function (_, body) {
        const rows = (body.match(/\[([^\[\]]+)\]/g) || []).map(function (r) { return r.slice(1, -1).split(',').map(function (c) { return c.trim(); }).join('  '); });
        return rows.length ? ('| ' + rows.join(' ; ') + ' |') : _;
      })
      .replace(/\[(\[[^\[\]]+\](?:\s*,\s*\[[^\[\]]+\])*)\]/g, function (_, body) {
        const rows = (body.match(/\[([^\[\]]+)\]/g) || []).map(function (r) { return r.slice(1, -1).split(',').map(function (c) { return c.trim(); }).join('  '); });
        return rows.length ? ('[ ' + rows.join(' ; ') + ' ]') : _;
      });
    if (utils && utils.formatMathExponents) {
      textStr = utils.formatMathExponents(textStr, !!o.isSecondary);
    }

    function _buildSingleRunXml(t, vAlignMode, isLtr) {
      const cleanText = String(t || '').replace(/<[^>]+>/g, '');
      const digitsNorm = o.isSecondary
        ? (utils && utils.toWesternDigits ? utils.toWesternDigits(cleanText) : cleanText)
        : utils.toEasternDigits(cleanText);
      const clean = escXml(digitsNorm);
      const isScript = (vAlignMode === 'sup' || vAlignMode === 'sub' || vAlignMode === true);
      const sizeVal = isScript ? Math.max(6.5, Math.round(o.sizePt * 0.68)) : o.sizePt;
      const sz = String(Math.round(sizeVal * 2));
      const useLtr = !!(isLtr || o.ltr);
      const fontXml = useLtr
        ? '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Traditional Arabic"/>'
        : '<w:rFonts w:ascii="Traditional Arabic" w:hAnsi="Traditional Arabic" w:cs="Traditional Arabic"/>';
      const vAlignXml = (vAlignMode === 'sup' || vAlignMode === true)
        ? '<w:vertAlign w:val="superscript"/>'
        : (vAlignMode === 'sub' ? '<w:vertAlign w:val="subscript"/>' : '');
      return (
        '<w:r>' +
        '<w:rPr>' +
        fontXml +
        (o.bold ? '<w:b/><w:bCs/>' : '') +
        '<w:color w:val="' + o.color + '"/>' +
        '<w:sz w:val="' + sz + '"/><w:szCs w:val="' + sz + '"/>' +
        vAlignXml +
        (useLtr ? '' : '<w:rtl/>') +
        '</w:rPr>' +
        '<w:t xml:space="preserve">' + clean + '</w:t>' +
        '</w:r>'
      );
    }

    function _emitInlineScripts(segText, baseLtr) {
      if (segText.indexOf('ar-pow') === -1 && segText.indexOf('sec-pow') === -1 && segText.indexOf('<sub') === -1) {
        return _buildSingleRunXml(segText, o.sup ? 'sup' : '', baseLtr);
      }
      const scriptPat = /<span\s+class=["'][^"']*(?:ar-pow|sec-pow)[^"']*["'][^>]*>\s*<span\s+class=["'][^"']*(?:ar-base|sec-base)[^"']*["'][^>]*>([\s\S]*?)<\/span>\s*<sup\s+class=["'][^"']*(?:ar-exp|sec-exp)[^"']*["'][^>]*>([\s\S]*?)<\/sup>\s*<\/span>|<sub\b[^>]*>([\s\S]*?)<\/sub>/gi;
      let xml = '';
      let idx = 0;
      let m;
      while ((m = scriptPat.exec(segText)) !== null) {
        if (m.index > idx) {
          xml += _emitInlineScripts(segText.substring(idx, m.index), baseLtr);
        }
        if (m[1] !== undefined) {
          const innerLtr = !!(baseLtr || o.isSecondary || m[0].indexOf('sec-pow') !== -1);
          xml += _emitInlineScripts(m[1], innerLtr);
          xml += _buildSingleRunXml(m[2], 'sup', innerLtr);
        } else if (m[3] !== undefined) {
          xml += _buildSingleRunXml(m[3], 'sub', !!(baseLtr || o.isSecondary));
        }
        idx = scriptPat.lastIndex;
      }
      if (idx < segText.length) {
        const tail = segText.substring(idx);
        if (tail) xml += _buildSingleRunXml(tail, o.sup ? 'sup' : '', baseLtr);
      }
      return xml;
    }

    if (textStr.indexOf('ar-pow') === -1 && textStr.indexOf('sec-pow') === -1 && textStr.indexOf('sec-math') === -1 && textStr.indexOf('ltr-math') === -1 && textStr.indexOf('<sub') === -1) {
      return _buildSingleRunXml(textStr, o.sup ? 'sup' : '', false);
    }

    // Unwrap outer sec-math/ltr-math containers cleanly while keeping nested sec-pow/sub intact
    const outerPat = /<span\s+class=["'][^"']*(?:sec-math|ltr-math)[^"']*["'][^>]*>/gi;
    if (textStr.indexOf('sec-math') === -1 && textStr.indexOf('ltr-math') === -1) {
      return _emitInlineScripts(textStr, false);
    }

    let outXml = '';
    let cursor = 0;
    let openMatch;
    while ((openMatch = outerPat.exec(textStr)) !== null) {
      if (openMatch.index < cursor) continue;
      if (openMatch.index > cursor) {
        outXml += _emitInlineScripts(textStr.substring(cursor, openMatch.index), false);
      }
      let depth = 1;
      let pos = outerPat.lastIndex;
      const tagScan = /<\/?span\b[^>]*>/gi;
      tagScan.lastIndex = pos;
      let tMatch;
      let closeStart = -1;
      let closeEnd = pos;
      while ((tMatch = tagScan.exec(textStr)) !== null) {
        if (tMatch[0].charAt(1) === '/') {
          depth--;
          if (depth === 0) {
            closeStart = tMatch.index;
            closeEnd = tagScan.lastIndex;
            break;
          }
        } else {
          depth++;
        }
      }
      if (closeStart !== -1) {
        const innerContent = textStr.substring(pos, closeStart);
        outXml += _emitInlineScripts(innerContent, true);
        cursor = closeEnd;
        outerPat.lastIndex = cursor;
      } else {
        outXml += _emitInlineScripts(textStr.substring(openMatch.index), true);
        cursor = textStr.length;
        break;
      }
    }
    if (cursor < textStr.length) {
      outXml += _emitInlineScripts(textStr.substring(cursor), false);
    }
    return outXml;
  }

  function wPara(runsXml, opts) {
    const o = Object.assign({ align: 'right', before: 40, after: 60, keepNext: false }, opts || {});
    return (
      '<w:p>' +
      '<w:pPr>' +
      (o.keepNext ? '<w:keepNext/>' : '') +
      '<w:bidi/>' +
      '<w:spacing w:before="' + o.before + '" w:after="' + o.after + '"/>' +
      '<w:jc w:val="' + o.align + '"/>' +
      '</w:pPr>' +
      runsXml +
      '</w:p>'
    );
  }

  function wCell(parasXml, widthDxa, opts) {
    const o = Object.assign({
      fill: '',
      borders: null,
      vMerge: '',
      gridSpan: 0,
      vAlign: 'center',
      marTop: 50,
      marBot: 50,
      marLeft: 75,
      marRight: 75
    }, opts || {});
    const shd = o.fill ? '<w:shd w:val="clear" w:color="auto" w:fill="' + o.fill + '"/>' : '';
    const gSpan = o.gridSpan > 1 ? '<w:gridSpan w:val="' + o.gridSpan + '"/>' : '';
    const vM = o.vMerge === 'restart'
      ? '<w:vMerge w:val="restart"/>'
      : (o.vMerge === 'continue' ? '<w:vMerge/>' : '');
    let bdrXml = '';
    if (o.borders && typeof o.borders === 'object') {
      const sideXml = ['top', 'left', 'bottom', 'right'].map(function (side) {
        const s = o.borders[side];
        if (!s) return '';
        if (s === 'none') return '<w:' + side + ' w:val="none"/>';
        return '<w:' + side + ' w:val="single" w:sz="' + (s.sz || 4) + '" w:space="0" w:color="' + (s.color || '000000') + '"/>';
      }).join('');
      if (sideXml) bdrXml = '<w:tcBorders>' + sideXml + '</w:tcBorders>';
    }
    return (
      '<w:tc>' +
      '<w:tcPr>' +
      '<w:tcW w:w="' + Math.round(widthDxa) + '" w:type="dxa"/>' +
      gSpan +
      vM +
      bdrXml +
      shd +
      '<w:tcMar><w:top w:w="' + o.marTop + '" w:type="dxa"/><w:bottom w:w="' + o.marBot + '" w:type="dxa"/><w:left w:w="' + o.marLeft + '" w:type="dxa"/><w:right w:w="' + o.marRight + '" w:type="dxa"/></w:tcMar>' +
      '<w:vAlign w:val="' + o.vAlign + '"/>' +
      '</w:tcPr>' +
      (parasXml || '<w:p><w:pPr><w:bidi/></w:pPr></w:p>') +
      '</w:tc>'
    );
  }

  function wTable(rowsXml, borders, borderColor, colWidthsDxa) {
    const bc = borderColor || '000000';
    const totalW = colWidthsDxa ? colWidthsDxa.reduce(function (a, b) { return a + Math.round(b); }, 0) : 10488;
    const gridXml = colWidthsDxa
      ? '<w:tblGrid>' + colWidthsDxa.map(function (w) { return '<w:gridCol w:w="' + Math.round(w) + '"/>'; }).join('') + '</w:tblGrid>'
      : '';
    const tblBorders = borders
      ? '<w:tblBorders>' +
        '<w:top w:val="single" w:sz="6" w:space="0" w:color="' + bc + '"/>' +
        '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="' + bc + '"/>' +
        '<w:left w:val="single" w:sz="6" w:space="0" w:color="' + bc + '"/>' +
        '<w:right w:val="single" w:sz="6" w:space="0" w:color="' + bc + '"/>' +
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="' + bc + '"/>' +
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="' + bc + '"/>' +
        '</w:tblBorders>'
      : '<w:tblBorders>' +
        '<w:top w:val="none"/><w:bottom w:val="none"/><w:left w:val="none"/><w:right w:val="none"/>' +
        '<w:insideH w:val="none"/><w:insideV w:val="none"/>' +
        '</w:tblBorders>';

    return (
      '<w:tbl>' +
      '<w:tblPr>' +
      '<w:bidiVisual/>' +
      '<w:tblW w:w="' + totalW + '" w:type="dxa"/>' +
      '<w:jc w:val="center"/>' +
      tblBorders +
      '<w:tblLayout w:type="fixed"/>' +
      '</w:tblPr>' +
      gridXml +
      rowsXml +
      '</w:tbl>'
    );
  }

  function parseImageDimensions(bytes) {
    try {
      if (!bytes || bytes.length < 24) return { width: 400, height: 240, ext: 'png' };
      // PNG header check
      if (bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4E && bytes[3] === 0x47) {
        const dv = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
        const w = dv.getUint32(16, false);
        const h = dv.getUint32(20, false);
        if (w > 0 && h > 0) return { width: w, height: h, ext: 'png' };
      }
      // JPEG SOF check
      if (bytes[0] === 0xFF && bytes[1] === 0xD8) {
        let i = 2;
        while (i + 9 < bytes.length) {
          if (bytes[i] !== 0xFF) break;
          const marker = bytes[i + 1];
          const segLen = (bytes[i + 2] << 8) | bytes[i + 3];
          if ((marker >= 0xC0 && marker <= 0xC3) || (marker >= 0xC5 && marker <= 0xC7)) {
            const h = (bytes[i + 5] << 8) | bytes[i + 6];
            const w = (bytes[i + 7] << 8) | bytes[i + 8];
            if (w > 0 && h > 0) return { width: w, height: h, ext: 'jpg' };
          }
          if (segLen < 2) break;
          i += 2 + segLen;
        }
        return { width: 400, height: 240, ext: 'jpg' };
      }
    } catch (e) { /* fallback */ }
    return { width: 400, height: 240, ext: 'png' };
  }

  function decodeDataUrlToBytes(dataUrl) {
    if (!dataUrl || typeof dataUrl !== 'string') return null;
    const m = dataUrl.match(/^\s*data:image\/(png|jpeg|jpg|webp|gif);base64,([A-Za-z0-9+/=\s]+)\s*$/i);
    if (!m) return null;
    const cleanB64 = m[2].replace(/\s+/g, '');
    try {
      let bytes;
      if (typeof atob === 'function') {
        const bin = atob(cleanB64);
        bytes = new Uint8Array(bin.length);
        for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      } else {
        const buf = Buffer.from(cleanB64, 'base64');
        bytes = new Uint8Array(buf.buffer, buf.byteOffset, buf.byteLength);
      }
      const dims = parseImageDimensions(bytes);
      return { bytes: bytes, width: dims.width, height: dims.height, ext: dims.ext };
    } catch (e) {
      return null;
    }
  }

  function buildInlineDrawingRun(rId, docPrId, name, wPx, hPx, maxWcm, maxHcm) {
    const emuPerPx = 9525; // 96 DPI
    const maxW = Math.round((maxWcm || 9.8) * 360000);
    const maxH = Math.round((maxHcm || 5.2) * 360000);
    const rawW = Math.max(1, wPx) * emuPerPx;
    const rawH = Math.max(1, hPx) * emuPerPx;
    const scale = Math.min(maxW / rawW, maxH / rawH, 1.0);
    const cx = Math.max(280000, Math.round(rawW * scale));
    const cy = Math.max(140000, Math.round(rawH * scale));
    const safeName = escXml(name || ('fig_' + docPrId + '.png'));
    return (
      '<w:r><w:drawing>' +
      '<wp:inline distT="0" distB="0" distL="0" distR="0">' +
      '<wp:extent cx="' + cx + '" cy="' + cy + '"/>' +
      '<wp:effectExtent l="0" t="0" r="0" b="0"/>' +
      '<wp:docPr id="' + docPrId + '" name="' + safeName + '"/>' +
      '<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>' +
      '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">' +
      '<pic:pic>' +
      '<pic:nvPicPr><pic:cNvPr id="' + docPrId + '" name="' + safeName + '"/><pic:cNvPicPr/></pic:nvPicPr>' +
      '<pic:blipFill><a:blip r:embed="' + rId + '"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>' +
      '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="' + cx + '" cy="' + cy + '"/></a:xfrm>' +
      '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>' +
      '</pic:pic>' +
      '</a:graphicData></a:graphic>' +
      '</wp:inline>' +
      '</w:drawing></w:r>'
    );
  }

  function buildDrawingParaXml(rId, docPrId, name, wPx, hPx, maxWcm, maxHcm, captionText, keepNext, isSecondary) {
    const utils = getUtils();
    const runXml = buildInlineDrawingRun(rId, docPrId, name, wPx, hPx, maxWcm, maxHcm);
    const drawingPara =
      '<w:p>' +
      '<w:pPr><w:bidi/><w:jc w:val="center"/><w:spacing w:before="40" w:after="20"/>' + (keepNext ? '<w:keepNext/>' : '') + '</w:pPr>' +
      runXml +
      '</w:p>';

    if (!captionText) return drawingPara;
    const capNorm = isSecondary
      ? (utils && utils.toWesternDigits ? utils.toWesternDigits(captionText) : String(captionText))
      : utils.toEasternDigits(captionText);
    return drawingPara + wPara(
      wRun(capNorm, { sizePt: 10, color: '475569', isSecondary: !!isSecondary }),
      { align: 'center', before: 0, after: 40 }
    );
  }

  function buildOfflineDocxBytes(examData) {
    const utils = getUtils();
    const header = examData.header || {};
    const questions = examData.questions || [];
    const options = examData.options || {};
    const isSec = !!(examData.isSecondary || (utils && utils.isSecondaryStage && utils.isSecondaryStage(header)) || (questions[0] && (questions[0].gradeId === 'g1s' || questions[0].gradeId === 'g2s')));
    const choiceLetters = (isSec && utils && utils.SECONDARY_CHOICE_LETTERS) ? utils.SECONDARY_CHOICE_LETTERS : WORD_CHOICE_LETTERS;
    const totalMarks = computeTotalMarks(questions);
    const totalStr = utils.formatMarkShort(totalMarks, isSec);
    const sections = groupQuestions(questions, options.groupByType !== false);
    const includeLogo = header.includeLogo !== false;
    const includeAnswerKey = options.includeAnswerKey !== false;

    const ed = function (v) {
      const s = v == null ? '' : String(v);
      return isSec ? (utils && utils.toWesternDigits ? utils.toWesternDigits(s) : s) : utils.toEasternDigits(s);
    };
    const secRun = function (txt, rOpts) {
      return wRun(txt, Object.assign({ isSecondary: isSec }, rOpts || {}));
    };

    const mediaFiles = [];
    const mediaRelList = [];
    const mediaByKey = {};
    const usedExts = { png: false, jpg: false };
    let nextImgNum = 1;
    let nextDocPrId = 1;

    function registerMedia(key, bytes, wPx, hPx, extHint) {
      if (!bytes || !bytes.length) return null;
      let reg = mediaByKey[key];
      if (!reg) {
        const b = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
        const dims = parseImageDimensions(b);
        const ext = (extHint === 'jpg' || dims.ext === 'jpg') ? 'jpg' : 'png';
        usedExts[ext] = true;
        const fname = 'img_' + nextImgNum + '.' + ext;
        const rId = 'rIdImg' + nextImgNum;
        nextImgNum++;
        reg = { fname: fname, rId: rId, wPx: wPx || dims.width, hPx: hPx || dims.height };
        mediaByKey[key] = reg;
        mediaFiles.push({ name: 'word/media/' + fname, content: b });
        mediaRelList.push({ rId: rId, target: 'media/' + fname });
      }
      return reg;
    }

    function assetParaXml(key, assetObj, maxWcm, maxHcm, captionText) {
      if (!assetObj || !assetObj.bytes || !assetObj.bytes.length) return '';
      const reg = registerMedia(key, assetObj.bytes, assetObj.width, assetObj.height, assetObj.ext);
      if (!reg) return '';
      const docId = nextDocPrId++;
      return buildDrawingParaXml(reg.rId, docId, reg.fname, reg.wPx, reg.hPx, maxWcm, maxHcm, captionText || '', false, isSec);
    }

    function maybeImageXml(q, maxWcm, maxHcm) {
      if (!q) return '';
      let b = q._imagePngBytes;
      let wPx = q._imageWidthPx;
      let hPx = q._imageHeightPx;
      let ext = 'png';
      if ((!b || !b.length) && q.image && /^data:image\//i.test(q.image)) {
        const decoded = decodeDataUrlToBytes(q.image);
        if (decoded) {
          b = decoded.bytes;
          wPx = decoded.width;
          hPx = decoded.height;
          ext = decoded.ext;
        }
      }
      if (!b || !b.length) return '';
      const key = q.image || ('inline_' + nextImgNum);
      const reg = registerMedia(key, b, wPx, hPx, ext);
      if (!reg) return '';
      const docId = nextDocPrId++;
      return buildDrawingParaXml(reg.rId, docId, reg.fname, reg.wPx, reg.hPx, maxWcm, maxHcm, q.imageCaption || '', false, isSec);
    }

    const bodyParts = [];

    // 1. Top Ribbon + Official 3-Column Header + Green Line (total 10488 dxa = 18.5 cm)
    const assetsMap = examData._offlineAssets || {};
    if (assetsMap.topRibbon) {
      const topPara = assetParaXml('__top_ribbon__', assetsMap.topRibbon, 18.4, 1.05);
      if (topPara) bodyParts.push(topPara);
    }

    const hdrWidths = [3742, 4082, 2664];
    const hdrBottomBdr = { bottom: { sz: 18, color: '3F9E35' }, top: 'none', left: 'none', right: 'none' };
    const rightLinesXml = [
      header.ministry || 'المملكة العربية السعودية',
      header.district || 'الإدارة العامة للتعليم بمحافظة جدة',
      header.schoolCompany || '',
      header.school || 'منصة الرائد التعليمية',
      header.stage || ''
    ].filter(function (v) { return (v || '').trim(); }).map(function (v, idx) {
      return wPara(secRun(ed(v), { sizePt: idx === 0 ? 12 : 11.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 15 });
    }).join('');

    const moeXml = assetsMap.moeLogo ? assetParaXml('__moe_logo__', assetsMap.moeLogo, 4.2, 1.45) : '';
    const midXml =
      moeXml +
      wPara(secRun(ed(header.examTitle || 'اختبار مادة الرياضيات'), { sizePt: 13.5, bold: true, color: '000000' }), { align: 'center', before: 15, after: 15 }) +
      wPara(secRun('المادة: ' + ed(header.subject || 'الرياضيات') + '  |  الصف: ' + ed(header.grade || '') + '  |  الفصل: ' + ed(header.term || 'الأول'), { sizePt: 11, bold: true, color: '0F172A' }), { align: 'center', before: 0, after: 15 }) +
      wPara(secRun('العام الدراسي: ' + ed(header.year || (isSec ? '1448 هـ' : '١٤٤٨ هـ')) + '  |  الزمن: ' + ed(header.duration || (isSec ? '45 دقيقة' : '٤٥ دقيقة')), { sizePt: 11, color: '475569' }), { align: 'center', before: 0, after: 15 });

    let schoolLogoAsset = assetsMap.schoolLogo || null;
    if (!schoolLogoAsset && includeLogo && header.customLogoDataUrl) {
      schoolLogoAsset = decodeDataUrlToBytes(header.customLogoDataUrl);
    }
    const leftXml = (includeLogo && schoolLogoAsset)
      ? assetParaXml('__school_logo__', schoolLogoAsset, 4.1, 2.2)
      : wPara('', { align: 'center', before: 0, after: 0 });

    const hdrRow =
      '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
      wCell(rightLinesXml, hdrWidths[0], { borders: hdrBottomBdr, marTop: 30, marBot: 55 }) +
      wCell(midXml, hdrWidths[1], { borders: hdrBottomBdr, marTop: 30, marBot: 55 }) +
      wCell(leftXml, hdrWidths[2], { borders: hdrBottomBdr, marTop: 30, marBot: 55 }) +
      '</w:tr>';
    bodyParts.push(wTable(hdrRow, false, '000000', hdrWidths));
    bodyParts.push(wPara('', { before: 15, after: 20 }));

    // 2. Student Info + Total Score Box (2 rows x 3 cols = 10488 dxa)
    const stuWidths = [1587, 6917, 1984];
    const stuRow0 =
      '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
      wCell(wPara(secRun('اسم الطالب', { sizePt: 12, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), stuWidths[0], { fill: 'F2F2F2' }) +
      wCell(wPara(secRun('..................................................................................', { sizePt: 11, color: '475569' }), { before: 0, after: 0 }), stuWidths[1]) +
      wCell(wPara(secRun('الدرجة الكلية', { sizePt: 11.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), stuWidths[2], { fill: 'F2F2F2' }) +
      '</w:tr>';
    const stuRow1 =
      '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
      wCell(wPara(secRun('الصف', { sizePt: 12, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), stuWidths[0], { fill: 'F2F2F2' }) +
      wCell(wPara(secRun(ed(header.grade || '') + '   /   (          )', { sizePt: 12, bold: true, color: '000000' }), { before: 0, after: 0 }), stuWidths[1]) +
      wCell(wPara(secRun('          /  ' + totalStr, { sizePt: 13, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), stuWidths[2]) +
      '</w:tr>';
    bodyParts.push(wTable(stuRow0 + stuRow1, true, '000000', stuWidths));

    if ((header.instructions || '').trim()) {
      bodyParts.push(wPara(
        secRun('تعليمات: ', { sizePt: 11.5, bold: true, color: '1E3A8A' }) +
        secRun(ed(header.instructions), { sizePt: 11.5, color: '475569' }),
        { before: 50, after: 40 }
      ));
    }

    // 3. Questions Sections (matching exact .doc tables for ANY count of questions)
    const boxBdr = {
      top: { sz: 6, color: '000000' },
      left: { sz: 6, color: '000000' },
      bottom: { sz: 6, color: '000000' },
      right: { sz: 6, color: '000000' }
    };
    const noBdr = { top: 'none', left: 'none', bottom: 'none', right: 'none' };

    let globalQ = 0;
    sections.forEach(function (sec) {
      const secMarks = computeTotalMarks(sec.items);
      const secMarksStr = utils.formatMarkShort(secMarks, isSec);
      const shWidths = [8504, 1984];
      const shRows =
        '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
        wCell(wPara(secRun(ed(sec.title), { sizePt: 13.5, bold: true, color: '000000' }), { before: 0, after: 0, keepNext: true }), shWidths[0], { vMerge: 'restart', borders: noBdr }) +
        wCell(wPara(secRun('الدرجة', { sizePt: 11, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), shWidths[1], { fill: 'F2F2F2', borders: boxBdr }) +
        '</w:tr>' +
        '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
        wCell('', shWidths[0], { vMerge: 'continue', borders: noBdr }) +
        wCell(wPara(secRun('          /  ' + secMarksStr, { sizePt: 12, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), shWidths[1], { borders: boxBdr }) +
        '</w:tr>';
      bodyParts.push(wPara('', { before: 35, after: 15 }));
      bodyParts.push(wTable(shRows, false, '000000', shWidths));
      bodyParts.push(wPara('', { before: 0, after: 20 }));

      splitTypeRuns(sec.items).forEach(function (runGrp) {
        const rtype = runGrp.type;
        const ritems = runGrp.items;

        if (rtype === 'mcq') {
          const mcqWidths = [567, 482, 1998, 482, 1998, 482, 1998, 482, 1999];
          const promptSpanW = mcqWidths.slice(1).reduce(function (a, b) { return a + b; }, 0);
          const rowsXml = ritems.map(function (q) {
            globalQ++;
            const qImgXml = maybeImageXml(q, 10.4, 4.6);
            const promptParas =
              wPara(secRun(ed(q.q || q.statement || ''), { sizePt: 10.5, bold: true, color: '000000' }), { before: 0, after: qImgXml ? 20 : 0, keepNext: true }) +
              qImgXml;
            const qOpts = (q.options || []).slice(0, 4);
            while (qOpts.length < 4) qOpts.push('');
            const optCells = qOpts.map(function (opt, oIdx) {
              return (
                wCell(wPara(secRun(choiceLetters[oIdx] || (isSec ? 'A' : 'أ'), { sizePt: 10, bold: true, color: '000000', ltr: isSec }), { align: 'center', before: 0, after: 0 }), mcqWidths[1 + 2 * oIdx], { marLeft: 30, marRight: 30 }) +
                wCell(wPara(secRun(ed(opt), { sizePt: 10 }), { before: 0, after: 0 }), mcqWidths[2 + 2 * oIdx], { marLeft: 55, marRight: 55 })
              );
            }).join('');

            return (
              '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
              wCell(wPara(secRun(ed(globalQ), { sizePt: 10.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0, keepNext: true }), mcqWidths[0], { vMerge: 'restart', marLeft: 30, marRight: 30 }) +
              wCell(promptParas, promptSpanW, { gridSpan: 8, fill: 'F2F2F2', vAlign: 'top' }) +
              '</w:tr>' +
              '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
              wCell('', mcqWidths[0], { vMerge: 'continue', marLeft: 30, marRight: 30 }) +
              optCells +
              '</w:tr>'
            );
          }).join('');
          bodyParts.push(wTable(rowsXml, true, '000000', mcqWidths));
        } else if (rtype === 'tf') {
          const tfWidths = [794, 8220, 1474];
          const tfHdr =
            '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
            wCell(
              wPara(wRun('ضع علامة ( ✓ ) أمام العبارة الصحيحة وعلامة ( ✗ ) أمام العبارة الخاطئة:', { sizePt: 10.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0, keepNext: true }),
              tfWidths[0] + tfWidths[1] + tfWidths[2],
              { gridSpan: 3, fill: 'F2F2F2' }
            ) +
            '</w:tr>';
          const tfRows = ritems.map(function (q) {
            globalQ++;
            const tfImg = maybeImageXml(q, 7.0, 3.5);
            return (
              '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
              wCell(wPara(secRun(ed(globalQ), { sizePt: 10.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), tfWidths[0]) +
              wCell(wPara(secRun(ed(q.statement || q.q || ''), { sizePt: 10.5, color: '000000' }), { before: 0, after: tfImg ? 20 : 0 }) + tfImg, tfWidths[1]) +
              wCell(wPara(secRun('(          )', { sizePt: 10.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0 }), tfWidths[2]) +
              '</w:tr>'
            );
          }).join('');
          bodyParts.push(wTable(tfHdr + tfRows, true, '000000', tfWidths));
        } else {
          const esWidths = [794, 9694];
          const esRows = ritems.map(function (q) {
            globalQ++;
            const qImgXml = maybeImageXml(q, 10.4, 4.6);
            const lc = Math.max(2, Math.min(6, Math.round(utils.toWesternNumber(q.lines, 3))));
            let solParas = '';
            for (let l = 0; l < lc; l++) {
              const prefix = l === 0 ? 'الحل /  ' : '';
              solParas += wPara(secRun(prefix + '....................................................................................................', { sizePt: 10, bold: l === 0, color: '475569' }), { before: 20, after: 25 });
            }
            return (
              '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
              wCell(wPara(secRun(ed(globalQ), { sizePt: 10.5, bold: true, color: '000000' }), { align: 'center', before: 0, after: 0, keepNext: true }), esWidths[0], { vMerge: 'restart' }) +
              wCell(wPara(secRun(ed(q.q || q.statement || ''), { sizePt: 10.5, bold: true, color: '000000' }), { before: 0, after: qImgXml ? 20 : 0, keepNext: true }) + qImgXml, esWidths[1], { fill: 'F2F2F2', vAlign: 'top' }) +
              '</w:tr>' +
              '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
              wCell('', esWidths[0], { vMerge: 'continue' }) +
              wCell(solParas, esWidths[1], { vAlign: 'top' }) +
              '</w:tr>'
            );
          }).join('');
          bodyParts.push(wTable(esRows, true, '000000', esWidths));
        }

        bodyParts.push(wPara('', { before: 0, after: 35 }));
      });
    });

    // 4. Closing Blessing + Teacher & Principal Signatures + Bottom Ribbon
    bodyParts.push(wPara(
      secRun('انتهت الأسئلة                   مع خالص الدعوات بالتوفيق والنجاح', { sizePt: 13, bold: true, color: '000000' }),
      { align: 'center', before: 100, after: 60, keepNext: true }
    ));

    const sigWidths = [5244, 5244];
    const teacherName = header.teacher || 'أ. محمد عبدالله جمعة';
    const principalName = header.principal || '';
    const sigRow =
      '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
      wCell(wPara(secRun('معلم المادة', { sizePt: 12, bold: true, color: '000000' }), { align: 'center', before: 0, after: 15 }) + wPara(secRun(ed(teacherName), { sizePt: 12, bold: true, color: '0F172A' }), { align: 'center', before: 0, after: 0 }), sigWidths[0], { borders: noBdr }) +
      wCell(wPara(secRun('مدير المدرسة', { sizePt: 12, bold: true, color: '000000' }), { align: 'center', before: 0, after: 15 }) + wPara(secRun(ed(principalName), { sizePt: 12, bold: true, color: '0F172A' }), { align: 'center', before: 0, after: 0 }), sigWidths[1], { borders: noBdr }) +
      '</w:tr>';
    bodyParts.push(wTable(sigRow, false, '000000', sigWidths));

    if (assetsMap.bottomRibbon) {
      const botPara = assetParaXml('__bot_ribbon__', assetsMap.bottomRibbon, 18.4, 0.9);
      if (botPara) bodyParts.push(botPara);
    }

    // 5. Optional Answer Key Page
    if (includeAnswerKey && questions.length) {
      bodyParts.push('<w:p><w:r><w:br w:type="page"/></w:r></w:p>');
      bodyParts.push(wPara(
        secRun('نموذج الإجابة وتوزيع الدرجات — ' + ed(header.examTitle || 'اختبار الرياضيات'), { sizePt: 14.5, bold: true, color: '1E3A8A' }),
        { align: 'center', before: 40, after: 100 }
      ));

      const ordered = [];
      sections.forEach(function (s) { s.items.forEach(function (it) { ordered.push(it); }); });
      const akWidths = [900, 1800, 6588, 1200];
      const akRows = [
        '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
        wCell(wPara(secRun('السؤال', { sizePt: 12, bold: true, color: '047857' }), { align: 'center', before: 0, after: 0 }), akWidths[0], { fill: 'D1FAE5' }) +
        wCell(wPara(secRun('النوع', { sizePt: 12, bold: true, color: '047857' }), { before: 0, after: 0 }), akWidths[1], { fill: 'D1FAE5' }) +
        wCell(wPara(secRun('الإجابة النموذجية والشرح', { sizePt: 12, bold: true, color: '047857' }), { before: 0, after: 0 }), akWidths[2], { fill: 'D1FAE5' }) +
        wCell(wPara(secRun('الدرجة', { sizePt: 12, bold: true, color: '047857' }), { align: 'center', before: 0, after: 0 }), akWidths[3], { fill: 'D1FAE5' }) +
        '</w:tr>'
      ];
      ordered.forEach(function (q, idx) {
        let tLbl = 'اختيار من متعدد';
        let ansTxt = '';
        if (q.type === 'mcq') {
          const c = typeof q.correct === 'number' ? q.correct : 0;
          const letter = choiceLetters[c] || (isSec ? 'A' : 'أ');
          ansTxt = letter + ') ' + ((q.options && q.options[c]) || '') + (q.explanation ? ' — ' + q.explanation : '');
        } else if (q.type === 'tf') {
          tLbl = 'صواب وخطأ';
          ansTxt = (q.is_true ? 'صواب (✓)' : 'خطأ (✗)') + (q.explanation ? ' — ' + q.explanation : '');
        } else {
          tLbl = 'مسألة مقالية';
          ansTxt = q.ans || '';
        }
        akRows.push(
          '<w:tr><w:trPr><w:cantSplit/></w:trPr>' +
          wCell(wPara(secRun(ed(idx + 1), { sizePt: 11.5, bold: true, color: '1E3A8A' }), { align: 'center', before: 0, after: 0 }), akWidths[0]) +
          wCell(wPara(secRun(tLbl, { sizePt: 11.5 }), { before: 0, after: 0 }), akWidths[1]) +
          wCell(wPara(secRun(ed(ansTxt), { sizePt: 11.5, color: '047857' }), { before: 0, after: 0 }), akWidths[2]) +
          wCell(wPara(secRun(utils.formatMarkShort(q.marks !== undefined ? q.marks : 1, isSec), { sizePt: 11.5, bold: true }), { align: 'center', before: 0, after: 0 }), akWidths[3]) +
          '</w:tr>'
        );
      });
      bodyParts.push(wTable(akRows.join(''), true, '047857', akWidths));
      bodyParts.push(wPara(secRun('المجموع الكلي للدرجات: ' + totalStr + ' درجة', { sizePt: 13, bold: true, color: '1E3A8A' }), { align: 'left', before: 100 }));
    }

    const pgBordersXml =
      '<w:pgBorders w:offsetFrom="page">' +
      '<w:top w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>' +
      '<w:left w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>' +
      '<w:bottom w:val="thickThinSmallGap" w:sz="24" w:space="18" w:color="000000"/>' +
      '<w:right w:val="thinThickSmallGap" w:sz="24" w:space="18" w:color="000000"/>' +
      '</w:pgBorders>';

    const documentXml =
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" ' +
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" ' +
      'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" ' +
      'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" ' +
      'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">' +
      '<w:body>' +
      bodyParts.join('') +
      '<w:sectPr>' +
      '<w:pgSz w:w="11906" w:h="16838"/>' +
      '<w:pgMar w:top="680" w:right="709" w:bottom="680" w:left="709" w:header="360" w:footer="360" w:gutter="0"/>' +
      pgBordersXml +
      '<w:bidi/>' +
      '</w:sectPr>' +
      '</w:body>' +
      '</w:document>';

    const contentTypesXml =
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' +
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>' +
      '<Default Extension="xml" ContentType="application/xml"/>' +
      (usedExts.png ? '<Default Extension="png" ContentType="image/png"/>' : '') +
      (usedExts.jpg ? '<Default Extension="jpg" ContentType="image/jpeg"/>' : '') +
      '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>' +
      '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>' +
      '</Types>';

    const relsXml =
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
      '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>' +
      '</Relationships>';

    const wordRelsXml =
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
      mediaRelList.map(function (rel) {
        return '<Relationship Id="' + rel.rId + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="' + escXml(rel.target) + '"/>';
      }).join('') +
      '</Relationships>';

    const stylesXml =
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">' +
      '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">' +
      '<w:name w:val="Normal"/>' +
      '<w:pPr><w:bidi/></w:pPr>' +
      '<w:rPr><w:rFonts w:ascii="Traditional Arabic" w:hAnsi="Traditional Arabic" w:cs="Traditional Arabic"/><w:sz w:val="28"/><w:szCs w:val="28"/><w:rtl/></w:rPr>' +
      '</w:style>' +
      '</w:styles>';

    const zipEntries = [
      { name: '[Content_Types].xml', content: contentTypesXml },
      { name: '_rels/.rels', content: relsXml },
      { name: 'word/_rels/document.xml.rels', content: wordRelsXml },
      { name: 'word/styles.xml', content: stylesXml },
      { name: 'word/document.xml', content: documentXml }
    ].concat(mediaFiles);

    return createZipStore(zipEntries);
  }

  async function isServerAvailable() {
    if (typeof window === 'undefined' || !window.location || window.location.protocol === 'file:') {
      return false;
    }
    try {
      const ctrl = new AbortController();
      const timer = setTimeout(function () { ctrl.abort(); }, 1500);
      const res = await fetch('/api/health', { signal: ctrl.signal });
      clearTimeout(timer);
      if (!res.ok) return false;
      const json = await res.json();
      return !!json.ok;
    } catch (e) {
      return false;
    }
  }

  function triggerDownload(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(function () {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 1000);
  }

  function defaultExportBaseName(examData) {
    const grade = (examData.header && examData.header.grade) || '';
    const fallback = grade.indexOf('ثانوي') !== -1
      ? 'اختبار_الرياضيات_أول_ثانوي'
      : (grade.indexOf('متوسط') !== -1 ? 'اختبار_الرياضيات_أول_متوسط' : 'اختبار_الرياضيات_سادس');
    return ((examData.header && examData.header.examTitle) || fallback).replace(/[\\/:*?"<>|]/g, '_');
  }

  async function fetchImageAsset(src) {
    if (!src) return null;
    if (/^data:image\//i.test(src)) return decodeDataUrlToBytes(src);
    if (typeof fetch !== 'function') return null;
    if (typeof window !== 'undefined' && window.location && !/^https?:/i.test(window.location.protocol)) {
      return null;
    }
    try {
      const resp = await fetch(src);
      if (!resp.ok) return null;
      const buf = await resp.arrayBuffer();
      const bytes = new Uint8Array(buf);
      const dims = parseImageDimensions(bytes);
      return { bytes: bytes, width: dims.width, height: dims.height, ext: dims.ext };
    } catch (e) {
      return null;
    }
  }

  async function hydrateOfflineQuestionImages(examData) {
    const questions = examData.questions || [];
    const header = examData.header || {};
    const cache = {};

    const clonedQuestions = await Promise.all(questions.map(async function (q) {
      if (!q || !q.image || q._imagePngBytes) return q;
      if (/^data:image\//i.test(q.image)) {
        const dec = decodeDataUrlToBytes(q.image);
        if (!dec) return q;
        return Object.assign({}, q, {
          _imagePngBytes: dec.bytes,
          _imageWidthPx: dec.width,
          _imageHeightPx: dec.height
        });
      }
      if (!cache[q.image]) cache[q.image] = fetchImageAsset(q.image);
      const res = await cache[q.image];
      if (!res) return q;
      return Object.assign({}, q, {
        _imagePngBytes: res.bytes,
        _imageWidthPx: res.width,
        _imageHeightPx: res.height
      });
    }));

    const existingAssets = Object.assign({}, examData._offlineAssets || {});
    const logoSrc = (header.customLogoDataUrl || '').trim() || 'assets/img/my_logo.png';
    const assetFetches = await Promise.all([
      existingAssets.topRibbon ? Promise.resolve(existingAssets.topRibbon) : fetchImageAsset('assets/img/exam_top_ribbon.png'),
      existingAssets.moeLogo ? Promise.resolve(existingAssets.moeLogo) : fetchImageAsset('assets/img/moe_logo.png'),
      existingAssets.bottomRibbon ? Promise.resolve(existingAssets.bottomRibbon) : fetchImageAsset('assets/img/exam_bottom_ribbon.png'),
      header.includeLogo === false
        ? Promise.resolve(null)
        : (existingAssets.schoolLogo ? Promise.resolve(existingAssets.schoolLogo) : fetchImageAsset(logoSrc))
    ]);

    return Object.assign({}, examData, {
      questions: clonedQuestions,
      _offlineAssets: {
        topRibbon: assetFetches[0] || null,
        moeLogo: assetFetches[1] || null,
        bottomRibbon: assetFetches[2] || null,
        schoolLogo: assetFetches[3] || null
      }
    });
  }

  async function exportDocx(examData) {
    const utils = getUtils();
    if (!examData.questions || !examData.questions.length) {
      utils.showToast('يرجى إضافة سؤال واحد على الأقل قبل التصدير.', 'warning');
      return;
    }
    const baseName = defaultExportBaseName(examData);

    if (await isServerAvailable()) {
      try {
        utils.showToast('جاري توليد ملف Word (.docx) بالصياغة المدرسية الرسمية...', 'info');
        const res = await fetch('/api/export/docx', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(examData)
        });
        if (res.ok) {
          const blob = await res.blob();
          triggerDownload(blob, baseName + '.docx');
          utils.showToast('✓ تم تنزيل ملف Word (.docx) جاهز للتعديل!', 'success');
          return;
        }
      } catch (e) {
        // المتابعة للمولد المحلي بدون خادم
      }
    }

    const hydrated = await hydrateOfflineQuestionImages(examData);
    const bytes = buildOfflineDocxBytes(hydrated);
    const blob = new Blob([bytes], {
      type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    });
    triggerDownload(blob, baseName + '.docx');
    utils.showToast('✓ تم إنشاء وتنزيل ملف Word (.docx) محلياً!', 'success');
  }

  async function exportPdf(examData) {
    const utils = getUtils();
    if (!examData.questions || !examData.questions.length) {
      utils.showToast('يرجى إضافة سؤال واحد على الأقل قبل التصدير.', 'warning');
      return;
    }
    const baseName = defaultExportBaseName(examData);

    if (await isServerAvailable()) {
      try {
        utils.showToast('جاري توليد ملف PDF للطباعة بجودة A4...', 'info');
        const res = await fetch('/api/export/pdf', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(examData)
        });
        if (res.ok) {
          const blob = await res.blob();
          triggerDownload(blob, baseName + '.pdf');
          utils.showToast('✓ تم تنزيل ملف PDF جاهز للطباعة!', 'success');
          return;
        }
      } catch (e) {
        // fallback below
      }
    }

    // Fallback: Dedicated A4 Print Window
    const html = buildExamPreviewHTML(examData, { forPrint: true });
    const win = window.open('', '_blank');
    if (win) {
      win.document.open();
      win.document.write(html);
      win.document.close();
      win.focus();
      setTimeout(function () { win.print(); }, 450);
      utils.showToast('تم فتح نافذة الطباعة؛ اختر «حفظ بتنسيق PDF».', 'info');
    } else {
      utils.showToast('يرجى السماح بالنوافذ المنبثقة أو تشغيل الخادم للتصدير المباشر.', 'warning');
    }
  }

  global.ExamExporter = {
    buildExamPreviewHTML: buildExamPreviewHTML,
    buildOfflineDocxBytes: buildOfflineDocxBytes,
    exportDocx: exportDocx,
    exportPdf: exportPdf,
    groupQuestions: groupQuestions,
    computeTotalMarks: computeTotalMarks
  };
})(typeof window !== 'undefined' ? window : globalThis);
