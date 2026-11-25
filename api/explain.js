/**
 * Vercel Serverless Function: /api/explain
 * Generates a detailed, curriculum-aligned Arabic mathematical explanation
 * with a step-by-step worked example for a specific sub-topic chosen by the user.
 * Reads GEMINI_API_KEY strictly from server environment variables.
 */

module.exports = async function handler(req, res) {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');

  if (req.method === 'OPTIONS') {
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ ok: false, code: 'METHOD_NOT_ALLOWED', message: 'يُسمح بطلبات POST فقط.' });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try {
      body = JSON.parse(body);
    } catch (e) {
      return res.status(400).json({ ok: false, code: 'INVALID_JSON', message: 'صيغة البيانات المرسلة غير صالحة.' });
    }
  }
  body = body && typeof body === 'object' ? body : {};

  const topic = String(body.topic || '').trim();
  if (!topic) {
    return res.status(400).json({ ok: false, code: 'MISSING_TOPIC', message: 'يرجى كتابة أو تحديد الجزئية المراد شرحها.' });
  }
  if (topic.length > 300) {
    return res.status(400).json({ ok: false, code: 'TOPIC_TOO_LONG', message: 'نص الجزئية طويل جداً (الحد الأقصى 300 حرف).' });
  }

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey || !String(apiKey).trim()) {
    return res.status(503).json({
      ok: false,
      code: 'API_KEY_NOT_CONFIGURED',
      message: 'لم يتم ضبط مفتاح Gemini API في إعدادات Vercel بعد.'
    });
  }

  const lessonTitle = String(body.lessonTitle || '').trim().slice(0, 160);
  const chapterTitle = String(body.chapterTitle || '').trim().slice(0, 160);
  const grade = String(body.grade || '').trim().slice(0, 100);
  const isSecondary = !!body.isSecondary;
  const level = String(body.level || 'متوسط منهجي').trim().slice(0, 80);
  const lessonContext = String(body.lessonContext || '').trim().slice(0, 900);

  const numeracyRules = isSecondary
    ? [
        'المرحلة الثانوية (التزام صارم):',
        '- استعمل الأرقام الإنجليزية (0-9) حصراً في كل الشرح والأمثلة والخطوات ولا تستعمل الأرقام المشرقية نهائياً.',
        '- استعمل المتغيرات اللاتينية (x, y, z, θ, a, b, c) واكتب جميع الصيغ والكسور والجذور والمعادلات بين علامتي دولار لـ KaTeX مثل $x^2 + 3x - 4 = 0$ أو $\\dfrac{x}{2}$.',
        '- ممنوع كتابة أي حروف عربية داخل علامتي $...$ نهائياً؛ اكتب الكلمات العربية خارج $...$.'
      ].join('\n')
    : [
        'المرحلة الابتدائية / المتوسطة (التزام صارم):',
        '- استعمل الأرقام العربية المشرقية (٠-٩) والفاصلة العشرية (٫) حصراً في كل النصوص والأمثلة والخطوات ولا تضع أرقاماً إنجليزية.',
        '- استعمل الرموز العربية المعتمدة في المنهج السعودي (س، ص، ÷، ×، ±) واكتب القوى بصيغة بسيطة مثل س^٢ أو ٢^٣ والكسور مثل ٣/٤ دون علامات $ أو أوامر LaTeX.'
      ].join('\n');

  const systemPrompt = [
    'أنت خبير تربوي في تدريس الرياضيات بالمنهج السعودي في منصة الرائد التعليمية.',
    'مهمتك تقديم شرح تفصيلي واضح ومباشر لجزئية محددة يطلبها المستخدم داخل الدرس مع مثال توضيحي محلول خطوة بخطوة وتدريب تحقق سريع.',
    numeracyRules,
    'مستوى الشرح المطلوب: ' + level + '.',
    'أجب بكائن JSON صالح فقط يطابق تماماً البنية الآتية دون أي نص خارجي أو علامات Markdown:',
    '{',
    '  "title": "عنوان مركز للجزئية",',
    '  "summary": "شرح تفصيلي واضح للمفهوم أو القاعدة الأساسية",',
    '  "steps": ["الخطوة الأولى...", "الخطوة الثانية..."],',
    '  "workedExample": {',
    '    "problem": "نص المثال التوضيحي الكامل",',
    '    "steps": ["خطوة الحل 1...", "خطوة الحل 2..."],',
    '    "finalAnswer": "الناتج النهائي المختصر"',
    '  },',
    '  "commonMistake": "تنبيه لأبرز خطأ شائع وكيفية تجنبه",',
    '  "quickCheck": {',
    '    "question": "سؤال تحقق قصير للطالب",',
    '    "answer": "الإجابة النموذجية المختصرة"',
    '  }',
    '}'
  ].join('\n');

  const userPrompt = [
    grade ? ('الصف الدراسي: ' + grade) : '',
    chapterTitle ? ('الفصل: ' + chapterTitle) : '',
    lessonTitle ? ('الدرس: ' + lessonTitle) : '',
    lessonContext ? ('سياق المنهج المعتمد: ' + lessonContext) : '',
    'الجزئية المطلوب شرحها بمثال توضيحي: ' + topic
  ].filter(Boolean).join('\n');

  const payload = {
    contents: [
      {
        role: 'user',
        parts: [{ text: systemPrompt + '\n\n' + userPrompt }]
      }
    ],
    generationConfig: {
      responseMimeType: 'application/json',
      temperature: 0.35,
      maxOutputTokens: 1600
    }
  };

  const models = ['gemini-2.5-flash', 'gemini-2.0-flash'];
  let lastErrMsg = 'تعذر الاتصال بخدمة التوليد الذكي.';

  for (let i = 0; i < models.length; i++) {
    const model = models[i];
    try {
      const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + model + ':generateContent?key=' + encodeURIComponent(apiKey);
      const upstream = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!upstream.ok) {
        lastErrMsg = 'HTTP ' + upstream.status + ' from ' + model;
        continue;
      }
      const rawJson = await upstream.json();
      const textOut =
        rawJson &&
        rawJson.candidates &&
        rawJson.candidates[0] &&
        rawJson.candidates[0].content &&
        rawJson.candidates[0].content.parts &&
        rawJson.candidates[0].content.parts[0] &&
        rawJson.candidates[0].content.parts[0].text;

      if (!textOut) {
        lastErrMsg = 'Empty candidate from ' + model;
        continue;
      }

      const cleaned = String(textOut)
        .replace(/^```json\s*/i, '')
        .replace(/^```\s*/i, '')
        .replace(/\s*```$/i, '')
        .trim();

      const parsed = JSON.parse(cleaned);
      if (!parsed || typeof parsed !== 'object' || !parsed.summary || !parsed.workedExample) {
        lastErrMsg = 'Invalid JSON structure from ' + model;
        continue;
      }

      const normalized = {
        title: String(parsed.title || topic).trim(),
        summary: String(parsed.summary || '').trim(),
        steps: Array.isArray(parsed.steps) ? parsed.steps.map(s => String(s || '').trim()).filter(Boolean) : [],
        workedExample: {
          problem: String((parsed.workedExample && parsed.workedExample.problem) || '').trim(),
          steps: Array.isArray(parsed.workedExample && parsed.workedExample.steps)
            ? parsed.workedExample.steps.map(s => String(s || '').trim()).filter(Boolean)
            : [],
          finalAnswer: String((parsed.workedExample && parsed.workedExample.finalAnswer) || '').trim()
        },
        commonMistake: String(parsed.commonMistake || '').trim(),
        quickCheck: {
          question: String((parsed.quickCheck && parsed.quickCheck.question) || '').trim(),
          answer: String((parsed.quickCheck && parsed.quickCheck.answer) || '').trim()
        }
      };

      return res.status(200).json({ ok: true, source: 'ai', model: model, data: normalized });
    } catch (err) {
      lastErrMsg = (err && err.message) || lastErrMsg;
    }
  }

  return res.status(502).json({
    ok: false,
    code: 'AI_UPSTREAM_ERROR',
    message: 'تعذر توليد الشرح حالياً عبر الذكاء الاصطناعي (' + lastErrMsg + ').'
  });
};
