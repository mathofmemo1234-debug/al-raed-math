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
    'قاعدة صارمة: إذا كتب المستخدم مسألة أو معادلة أو دالة محددة بأرقامها (مثل: د(س) = -س + ٧ فأوجد د(٣))، فيجب أن يكون workedExample.problem هو نفس مسألة المستخدم بالضبط وحلّها خطوة بخطوة حتى الناتج النهائي الصحيح، وممنوع تماماً استبدالها بمثال آخر مختلف الأرقام. كما يجب أن يكون finalAnswer مختصراً (الناتج النهائي فقط مثل: د(٣) = ٤) ولا يكرر الخطوة الأخيرة حرفياً.',
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
      maxOutputTokens: 3072
    }
  };

  const cleanKey = String(apiKey).trim();
  const baseModels = [
    'gemini-3.8-flash',
    'gemini-3.5-flash-lite',
    'gemini-3.1-flash-lite',
    'gemini-3-flash-preview',
    'gemini-2.5-flash',
    'gemini-2.5-flash-lite'
  ];
  const providers = [
    {
      label: 'aistudio',
      buildUrl: (model) => 'https://generativelanguage.googleapis.com/v1beta/models/' + model + ':generateContent'
    },
    {
      label: 'vertex',
      buildUrl: (model) => 'https://aiplatform.googleapis.com/v1/publishers/google/models/' + model + ':generateContent'
    }
  ];

  // Discover active flash models from AI Studio manifest when cached list is missing
  async function discoverAiStudioModels() {
    if (globalThis.__alraedCachedGeminiModels && Array.isArray(globalThis.__alraedCachedGeminiModels)) {
      return globalThis.__alraedCachedGeminiModels;
    }
    try {
      const listResp = await fetch('https://generativelanguage.googleapis.com/v1beta/models', {
        method: 'GET',
        headers: { 'x-goog-api-key': cleanKey }
      });
      if (!listResp.ok) return [];
      const listData = await listResp.json();
      const rawModels = Array.isArray(listData && listData.models) ? listData.models : [];
      const names = rawModels
        .filter(m => Array.isArray(m.supportedGenerationMethods) && m.supportedGenerationMethods.includes('generateContent'))
        .map(m => String(m.name || '').replace(/^models\//, ''))
        .filter(name => /gemini/i.test(name) && !/embedding|imagen|veo|tts|audio|robotics/i.test(name));
      names.sort((a, b) => {
        const score = (n) => (/flash/i.test(n) ? 10 : 0) + (/lite/i.test(n) ? 2 : 0) - (/pro|exp|preview/i.test(n) ? 1 : 0);
        return score(b) - score(a);
      });
      if (names.length) {
        globalThis.__alraedCachedGeminiModels = names.slice(0, 6);
      }
      return names.slice(0, 6);
    } catch (e) {
      return [];
    }
  }

  const attempts = [];

  function parseCandidateJson(text) {
    const cleaned = String(text || '')
      .replace(/^```json\s*/i, '')
      .replace(/^```\s*/i, '')
      .replace(/\s*```$/i, '')
      .trim();
    try {
      return JSON.parse(cleaned);
    } catch (e) {
      const start = cleaned.indexOf('{');
      const end = cleaned.lastIndexOf('}');
      if (start !== -1 && end > start) {
        return JSON.parse(cleaned.slice(start, end + 1));
      }
      throw e;
    }
  }

  const discovered = await discoverAiStudioModels();
  const models = Array.from(new Set(discovered.concat(baseModels)));

  for (let p = 0; p < providers.length; p++) {
    const provider = providers[p];
    for (let i = 0; i < models.length; i++) {
      const model = models[i];
      try {
        const url = provider.buildUrl(model);
        const upstream = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-goog-api-key': cleanKey
          },
          body: JSON.stringify(payload)
        });
        if (!upstream.ok) {
          let shortReason = '';
          try {
            const errBody = await upstream.text();
            const errJson = JSON.parse(errBody);
            shortReason = (errJson && errJson.error && errJson.error.message) ? String(errJson.error.message).slice(0, 80) : '';
          } catch (e2) {}
          shortReason = shortReason.split(cleanKey).join('[REDACTED]');
          attempts.push(provider.label + '/' + model + ':' + upstream.status + (shortReason ? ' (' + shortReason + ')' : ''));
          // Skip remaining models on same provider if project/auth is disabled (403/401)
          if (upstream.status === 401 || upstream.status === 403) break;
          continue;
        }
        const rawJson = await upstream.json();
        const parts = (rawJson && rawJson.candidates && rawJson.candidates[0] && rawJson.candidates[0].content && rawJson.candidates[0].content.parts) || [];
        const nonThought = parts.filter(part => part && !part.thought && typeof part.text === 'string').map(part => part.text).join('\n').trim();
        const textOut = nonThought || (parts.length && parts[parts.length - 1] && parts[parts.length - 1].text) || '';

        if (!textOut) {
          attempts.push(provider.label + '/' + model + ':empty');
          continue;
        }

        const parsed = parseCandidateJson(textOut);
        if (!parsed || typeof parsed !== 'object' || !parsed.summary || !parsed.workedExample) {
          attempts.push(provider.label + '/' + model + ':bad-schema');
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

        return res.status(200).json({ ok: true, source: 'ai', model: model, provider: provider.label, data: normalized });
      } catch (err) {
        const msg = String((err && err.message) || 'err').slice(0, 60).split(cleanKey).join('[REDACTED]');
        attempts.push(provider.label + '/' + model + ':' + msg);
      }
    }
  }

  return res.status(502).json({
    ok: false,
    code: 'AI_UPSTREAM_ERROR',
    message: 'تعذر توليد الشرح حالياً عبر الذكاء الاصطناعي (' + attempts.slice(0, 4).join(' | ') + ').'
  });
};
