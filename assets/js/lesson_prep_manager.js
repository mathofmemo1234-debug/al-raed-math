/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات
 * وحدة التحضير الميداني الشامل المعتمد (Field Lesson Preparation Manager)
 * متوافقة مع معايير وزارة التعليم وهيئة تقويم التعليم والتدريب بالمملكة العربية السعودية
 * إعداد خبير الرياضيات: أ. محمد عبدالله جمعة | المدارس المتقدمة للتعلم الذكي بجدة
 * ==========================================================================
 */

(function (global) {
  'use strict';

  function getUtils() {
    return global.ArabicUtils || {
      toEasternDigits: function (n) { return String(n); },
      escapeHtml: function (s) { return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); },
      showToast: function (msg, type) { if (global.alert) alert(msg); }
    };
  }

  function esc(s) {
    return getUtils().escapeHtml(s);
  }

  function fmt(s, isG6) {
    if (s === undefined || s === null) return '';
    const utils = getUtils();
    return utils.formatMathText ? utils.formatMathText(s) : utils.toEasternDigits(s);
  }

  // Generate 2-3 tailored active learning strategies with teacher/student/outcome steps
  function buildPedagogicalStrategies(lesson, style) {
    const isG6 = !lesson.id || !lesson.id.startsWith('g1m');
    const title = lesson.title || 'الدرس';
    const vocab = (lesson.vocabulary && lesson.vocabulary.length) ? lesson.vocabulary.join('، ') : 'مفاهيم الدرس';

    if (style === 'inquiry') {
      return [
        {
          name: 'الاستقصاء الرياضي الموجّه (Guided Inquiry)',
          time: '٤ دقائق',
          teacherRole: `يطرح المعلم تحدياً استقصائياً مفتوحاً مرتبطاً بـ (${title})، ويوجه الطلاب بمجموعات للبحث عن النمط الرياضي الكامن دون إعطاء القاعدة الجاهزة فوراً.`,
          studentRole: `يجمع الطلاب الملاحظات، ويجربون فرضيات مختلفة لاكتشاف العلاقة الرياضية، ثم يسجلون النتائج في بطاقات الاستقصاء.`,
          expectedOutcome: `اكتشاف الطلاب للقاعدة الرياضية ذاتياً وتفسير مبرراتها المنطقية قبل الشرح الرسمي للمعلم.`
        },
        {
          name: 'فكر – زاوج – شارك (Think - Pair - Share)',
          time: '٣ دقائق',
          teacherRole: `يطرح مسألة تطبيقية متوسطة تتضمن (${vocab})، ويعطي دقيقة للتفكير الفردي، ثم يوجه لمناقشة ثنائية قبل الاستماع لآراء الصف.`,
          studentRole: `يفكر كل طالب منفرداً ويسجل فكرته، ثم يناقش زميله المجاور لتبادل طرق الحل وتصحيح المسار، ثم يشاركان استنتاجهما مع الصف.`,
          expectedOutcome: `مشاركة ١٠٠٪ من الطلاب في التفكير، وتطوير لغة الحوار الرياضي وتبرير خطوات الحل.`
        },
        {
          name: 'حل المشكلات الواقعية (Real-World Problem Solving)',
          time: '٣ دقائق',
          teacherRole: `يعرض مسألة حياتية تتطلب توظيف خطوات الحل الرياضي بدقة، ويتابع المجموعات موجهاً أسئلة سبرية تدعم التفكير العميق.`,
          studentRole: `يحلل الطلاب معطيات المسألة، ويميزون المطلوب، ويصوغون نموذجاً رياضياً للحل، ثم يتحققون من معقولية النتائج.`,
          expectedOutcome: `ربط الرياضيات بواقع الحياة اليومية وتنمية التفكير الناقد ومهارات التبرير الرياضي السليم.`
        }
      ];
    }

    if (style === 'visual') {
      return [
        {
          name: 'التمثيل البصري والنمذجة (Visual Representation & Modeling)',
          time: '٤ دقائق',
          teacherRole: `يوظف المعلم خط الأعداد، أو شبكات المربعات، أو النماذج الهندسية والمخططات الشجرية لتمثيل مفهوم (${title}) حسياً وبصرياً.`,
          studentRole: `يرسم الطلاب النموذج في دفاترهم أو على السبورة البيضاء المصغرة، ويترجمون المسألة اللفظية إلى رسم تخطيطي دقيق.`,
          expectedOutcome: `تحويل المفهوم المجرد إلى إدراك بصري ملموس يرسخ الفهم العميق ويمنع الأخطاء الشائعة.`
        },
        {
          name: 'التعلم التعاوني ذو الأدوار المحددة (Cooperative Learning)',
          time: '٣ دقائق',
          teacherRole: `يقسم الطلاب إلى مجموعات رباعية متجانسة جزئياً، ويوزع الأدوار: (الميسر، الكاتب، المتحدث، المقوم الزمني)، ويطرح مهمة تدريبية.`,
          studentRole: `تتعاون المجموعة في حل المسألة مع التزام كل طالب بدوره، والتأكد من فهم جميع أفراد المجموعة قبل إنهاء الحل.`,
          expectedOutcome: `تعزيز روح الفريق والمسؤولية الفردية والجماعية ورفع مستوى التحصيل لكافة فئات الطلاب.`
        },
        {
          name: 'الرؤوس المرقمة تتعاون (Numbered Heads Together)',
          time: '٣ دقائق',
          teacherRole: `يرقم أعضاء كل مجموعة من ١ إلى ٤، يطرح سؤال تحقق سريع، ثم ينادي رقماً عشوائياً للإجابة نيابة عن مجموعته.`,
          studentRole: `يتشاور أعضاء المجموعة للتأكد من أن صاحب كل رقم قادر تماماً على شرح خطوات الحل بالتفصيل.`,
          expectedOutcome: `جاهزية تامة ومسؤولية مشتركة، وإتاحة الفرصة للطلاب الخجولين للمشاركة بثقة.`
        }
      ];
    }

    if (style === 'differentiated') {
      return [
        {
          name: 'التدريس المتمايز بالمحطات (Differentiated Tiered Learning)',
          time: '٤ دقائق',
          teacherRole: `يعد المعلم ٣ مستويات للمهمة التدريبية (تأسيس مباشر، تدريب معياري، وتحدٍ إثرائي)، ويوجه الطلاب حسب جاهزيتهم مع تقديم الدعم المباشر للمتعثرين.`,
          studentRole: `يعمل كل طالب على المستوى المناسب لقدراته الرياضية، مع إمكانية الانتقال للمستوى الأعلى فور إتقان المستوى الحالي.`,
          expectedOutcome: `تلبية الاحتياجات الفردية للجميع، وضمان وصول المتعثر للإتقان ومنح الموهوب فرصة الإبحار والتوسع.`
        },
        {
          name: 'فكر – زاوج – شارك (Think - Pair - Share)',
          time: '٣ دقائق',
          teacherRole: `يطرح سؤالاً مفاهيمياً يمس الفكرة الجوهرية لـ (${title})، ويوجه الأقران لتقويم إجابات بعضهم البعض.`,
          studentRole: `يفكر الطالب مستقلاً، ثم يناقش زميله ويصححان لبعضهما بالرجوع للقاعدة الرياضية.`,
          expectedOutcome: `تفعيل التقويم التكويني بين الأقران وبناء الثقة بالنفس.`
        },
        {
          name: 'النمذجة الرياضية الموجهة (Explicit Teacher Modeling - I Do, We Do, You Do)',
          time: '٣ دقائق',
          teacherRole: `يطبق استراتيجية (أنا أحل بصوت عالٍ، ثم نحن نحل معاً، ثم أنتم تحلون بأنفسكم) لترسيخ خوارزمية الحل النظامية.`,
          studentRole: `يلاحظون تفكير المعلم الاستراتيجي، ثم يشاركون جزئياً في الخطوات، ثم يطبقون بأنفسهم باستقلالية كاملة.`,
          expectedOutcome: `انتقال تدريجي للمسؤولية المعرفية واكتساب الكفاية الرياضية بوضوح تام.`
        }
      ];
    }

    // Standard / Default pedagogical blend
    return [
      {
        name: 'فكر – زاوج – شارك (Think - Pair - Share)',
        time: '٣ دقائق',
        teacherRole: `يطرح المعلم السؤال التأسيسي المرتبط بـ (${title})، ويمنح الطلاب دقيقة للتفكير الفردي، ثم دقيقة للمناقشة الثنائية مع الزميل.`,
        studentRole: `يحلل الطالب السؤال ذاتياً ويسجل محاولته الأولى، ثم يقارن حله مع زميله الملتصق لتعديل التفكير وتبادل المبررات، ثم يعرضان النتيجة.`,
        expectedOutcome: `مشاركة نشطة وتفاعل ١٠٠٪ من الطلاب، واكتشاف الأخطاء وتصويبها ذاتياً قبل المناقشة الصفية العامة.`
      },
      {
        name: 'التمثيل البصري والنمذجة الرياضية (Visual Modeling)',
        time: '٤ دقائق',
        teacherRole: `يقدم المعلم نموذجاً بيانياً أو رسمياً يجسد مفهوم (${title}) ويوضح العلاقات الرياضية بشكل حسي وملموس على السبورة.`,
        studentRole: `يرسم الطلاب النموذج المماثل في كراساتهم، ويسجلون الترجمة الرمزية الرياضية المقابلة لكل عنصر من عناصر الشكل البصري.`,
        expectedOutcome: `ربط المفهوم النظري بالتمثيل البصري، وترسيخ الفكرة المحورية في الذاكرة طويلة المدى.`
      },
      {
        name: 'التعلم التعاوني ذو المهام المركبة (Cooperative Problem Solving)',
        time: '٣ دقائق',
        teacherRole: `يوزع بطاقات مسائل تطبيقية حياتية على مجموعات العمل، ويتابع التفاعل موفراً التغذية الراجعة الفورية للمتعثرين.`,
        studentRole: `يتعاون أعضاء المجموعة في تفكيك المسألة: فهم المعطيات، صياغة خطة الحل، تنفيذ العمليات الحسابية، ثم التحقق من صحة الناتج.`,
        expectedOutcome: `تنمية مهارات التفكير العليا، والعمل الجماعي، والتبرير الرياضي المقنع.`
      }
    ];
  }

  // Extract 3 tiered solved examples from lesson data
  function buildTieredSolvedExamples(lesson) {
    const isG6 = !lesson.id || !lesson.id.startsWith('g1m');
    const title = lesson.title || 'الدرس';
    const summary = lesson.summary || {};
    const worksheet = lesson.worksheet || { questions: [] };
    const quiz = lesson.quiz || { mcq: [], tf: [], essay: [] };

    // Example 1: Direct / Basic
    let ex1 = {
      level: 'المستوى الأول: تطبيق مباشر ومبسط (تأسيس المفهوم)',
      problem: '',
      solution: '',
      note: 'يركز على التطبيق المباشر لخوارزمية الدرس دون تعقيد لفظي أو خطوات متعددة.'
    };

    if (summary.solved_example) {
      ex1.problem = summary.solved_example.includes('الحل') ? summary.solved_example.split('الحل')[0].replace(/^(مثال|المسألة|تطبيق)[:\s]*/, '').trim() : summary.solved_example;
      ex1.solution = summary.solved_example.includes('الحل') ? summary.solved_example.split('الحل')[1].replace(/^[:\s]*/, '').trim() : 'تطبيق القاعدة الرياضية المباشرة للدرس والوصول للناتج النهائي بدقة.';
    } else if (worksheet.questions && worksheet.questions.length > 0) {
      ex1.problem = worksheet.questions[0].q;
      ex1.solution = worksheet.questions[0].answer || 'تطبيق القاعدة الرياضية المباشرة.';
    } else {
      ex1.problem = `احسب أو أوجد قيمة العبارة الرياضية المباشرة في درس (${title}).`;
      ex1.solution = `التعويض المباشر في القاعدة وتطبيق العمليات الحسابية بالترتيب الصحيح.`;
    }

    // Example 2: Medium / Multi-step
    let ex2 = {
      level: 'المستوى الثاني: تطبيق متوسط متعدد الخطوات (ربط المفاهيم)',
      problem: '',
      solution: '',
      note: 'يتطلب خطوتين متتابعتين، ويقيس قدرة الطالب على التمييز والتحقق من صحة الحل.'
    };

    if (worksheet.questions && worksheet.questions.length > 1) {
      ex2.problem = worksheet.questions[1].q;
      ex2.solution = worksheet.questions[1].answer || 'إجراء الخطوة الأولى للتحويل، ثم إتمام العملية الحسابية الأساسية والتحقق.';
    } else if (quiz.mcq && quiz.mcq.length > 0) {
      ex2.problem = quiz.mcq[0].q;
      ex2.solution = `الحل الصحيح: (${quiz.mcq[0].correct}) - التفسير: ${quiz.mcq[0].explanation || 'التحليل الرياضي المنهجي.'}`;
    } else {
      ex2.problem = `مسألة تطبيقية تتطلب توظيف مفهومين متصلين في درس (${title}).`;
      ex2.solution = `الخطوة ١: استخراج العلاقات الرياضية. الخطوة ٢: إجراء الحساب الدقيق والتحقق.`;
    }

    // Example 3: Complex / Higher-Order Thinking
    let ex3 = {
      level: 'المستوى الثالث: مسألة مركّبة / مهارات تفكير عليا (واقع الحياة والتبرير)',
      problem: '',
      solution: '',
      note: 'يقيس مهارات التحليل والاستنتاج والتبرير المنطقي وربط الرياضيات ببيئة الطالب.'
    };

    if (quiz.essay && quiz.essay.length > 0) {
      ex3.problem = quiz.essay[0].q;
      ex3.solution = quiz.essay[0].sample_answer || quiz.essay[0].answer || 'صياغة نموذج رياضي لحل المسألة اللفظية ومقارنة الحل بتقدير معقولية الإجابة.';
    } else if (worksheet.questions && worksheet.questions.length > 2) {
      ex3.problem = worksheet.questions[2].q;
      ex3.solution = worksheet.questions[2].answer || 'تحليل المسألة وصياغة معادلة رياضية وحلها بالخطوات التفصيلية.';
    } else {
      ex3.problem = `اكتشف الخطأ الرياضي أو برر صحة عبارة استقصائية في موضوع (${title}).`;
      ex3.solution = `تفنيد الفرضية الخاطئة، وتطبيق البرهان الرياضي الصحيح خطوة بخطوة.`;
    }

    return [ex1, ex2, ex3];
  }

  // Extract common misconceptions and remediation
  function buildCommonMisconceptions(lesson) {
    const socratic = lesson.socratic || {};
    if (socratic.misconception_buster) {
      return {
        fallacy: socratic.misconception_buster.fallacy || 'الخلط بين المفاهيم الرياضية الشائعة أو التسرع دون اتباع خطوات الحل.',
        truth: socratic.misconception_buster.truth || 'الالتزام بالقواعد والخصائص الرياضية الدقيقة والتحقق من النتيجة.',
        remediation: socratic.misconception_buster.proof || 'توجيه أسئلة سبرية واستخدام النماذج البصرية المضادة لإقناع الطالب بالتناقض المنطقي في تفكيره.'
      };
    }
    return {
      fallacy: `التسرع في تطبيق العمليات الحسابية دون مراعاة شروط وقوانين درس (${lesson.title}).`,
      truth: `تطبيق القوانين الرياضية بترتيبها المنطقي والتحقق من ملاءمة النتيجة لمعطيات المسألة.`,
      remediation: `استخدام تمثيلات بصرية ونماذج حسية وعكسية تكشف سبب الخطأ وتعزز البديل الصحيح فورياً.`
    };
  }

  // Construct the 6 Comprehensive Stations
  function buildFullPreparation(lesson, opts) {
    const isG6 = !lesson.id || !lesson.id.startsWith('g1m');
    const options = Object.assign({
      duration: 45,
      style: 'standard',
      focus: 'balanced'
    }, opts || {});

    const duration = options.duration || 45;
    const timeScale = duration / 45;

    // Time budget allocation
    const timeHook = Math.round(5 * timeScale);
    const timeStrategies = Math.round(10 * timeScale);
    const timeTeach = Math.round(15 * timeScale);
    const timeAssess = Math.round(10 * timeScale);
    const timeClosure = duration - (timeHook + timeStrategies + timeTeach + timeAssess);

    const title = lesson.title || 'الدرس';
    const grade = lesson.grade || (isG6 ? 'الصف السادس الابتدائي' : 'الصف الأول المتوسط');
    const stage = lesson.stage || (isG6 ? 'المرحلة الابتدائية' : 'المرحلة المتوسطة');
    const term = lesson.term || 'الفصل الدراسي الأول';
    const chapter = lesson.chapter || 'الفصل الدراسي';
    const pages = lesson.pages || 'الكتاب المدرسي';
    const objectives = lesson.objectives || [];
    const vocabulary = lesson.vocabulary || [];
    const lessonIdea = lesson.lesson_idea || (lesson.summary ? lesson.summary.concept : '');

    // Station 1: Data & Measurable Objectives
    const station1 = {
      number: '١',
      title: 'البيانات والأهداف التعليمية ونواتج التعلّم',
      metadata: {
        stage: stage,
        grade: grade,
        term: term,
        chapter: chapter,
        lessonTitle: title,
        pages: pages,
        durationMinutes: duration,
        supervision: 'أ. محمد عبدالله جمعة • المدارس المتقدمة للتعلم الذكي بجدة'
      },
      lessonIdea: lessonIdea,
      objectives: objectives.length ? objectives : [
        `أن يتعرف الطالب على المفهوم الرياضي الأساسي لدرس (${title}) بدقة.`,
        `أن يطبق الطالب خوارزمية الحل المنهجية على مسائل متنوعة بنسبة إتقان لا تقل عن ٨٥٪.`,
        `أن يحل مسائل وتطبيقات حياتية توظف مهارات التفكير العليا وتبرير خطوات الحل.`
      ],
      vocabulary: vocabulary.length ? vocabulary : [title, 'النمذجة الرياضية', 'التحقق والمعقولية']
    };

    // Station 2: Engaging Hook & Prior Knowledge Check
    const plan5 = lesson.plan_5es || {};
    const engageText = plan5.engage || `طرح موقف رياضي حياتي مشوق يرتبط باهتمامات الطلاب اليومية (كالنقود، الرياضة، أو التسوق) يبرز الحاجة لمفهوم (${title}).`;
    const station2 = {
      number: '٢',
      title: 'التمهيد والتهيئة المحفزة وكشف الجاهزية',
      timeMinutes: timeHook,
      hookDescription: engageText,
      priorKnowledgeCheck: `سؤال استثاري سريع يُعرض على السبورة لكشف المفاهيم السابقة المرتبطة بالدرس والتأكد من تمكن الطلاب من المتطلبات الأساسية قبل الانطلاق.`
    };

    // Station 3: Active Pedagogical Strategies
    const strategies = buildPedagogicalStrategies(lesson, options.style);
    const station3 = {
      number: '٣',
      title: 'استراتيجيات التدريس المتنوعة وتطبيقها الإجرائي في الدرس',
      timeMinutes: timeStrategies,
      items: strategies
    };

    // Station 4: Structured Teaching, Concepts & Tiered Solved Examples
    const tieredExamples = buildTieredSolvedExamples(lesson);
    const misconceptions = buildCommonMisconceptions(lesson);
    const conceptExplanation = (lesson.summary && lesson.summary.concept) ? lesson.summary.concept : (plan5.explain || `بناء مفهوم (${title}) من خلال التدرج من المحسوس إلى شبه المحسوس ثم إلى المجرد.`);
    const station4 = {
      number: '٤',
      title: 'عرض الدرس والشرح المتدرج والأمثلة المحلولة ومعالجة الأخطاء',
      timeMinutes: timeTeach,
      conceptBuild: conceptExplanation,
      goldenRule: (lesson.summary && lesson.summary.golden_rule) ? lesson.summary.golden_rule : `الدقة في قراءة المسألة وتحديد العمليات الحسابية المناسبة هو مفتاح الإتقان الرياضي.`,
      examples: tieredExamples,
      misconception: misconceptions
    };

    // Station 5: Comprehensive Assessment & Differentiation
    const worksheet = lesson.worksheet || { questions: [] };
    const quiz = lesson.quiz || { mcq: [], tf: [] };
    const diagQ = (worksheet.questions && worksheet.questions[0]) ? worksheet.questions[0].q : `ما المتطلب الرياضي الأساسي اللازم للبدء في حل مسائل (${title})؟`;
    const formQ = (quiz.tf && quiz.tf[0]) ? quiz.tf[0].q : (quiz.mcq && quiz.mcq[0] ? quiz.mcq[0].q : `طبق القاعدة في حساب قيمة المقدار المعطى وتحقق من صحة الناتج.`);
    const summQ = (quiz.mcq && quiz.mcq[1]) ? quiz.mcq[1].q : `اختر الإجابة الصحيحة لحل المسألة الختامية الشاملة لمخرجات الدرس.`;

    const station5 = {
      number: '٥',
      title: 'منظومة التقويم الشاملة ومراعاة الفروق الفردية (التمايز)',
      timeMinutes: timeAssess,
      diagnostic: {
        label: 'التقويم التشخيصي (القبلي):',
        task: diagQ,
        purpose: 'قياس تمكن الطلاب من المتطلبات الرياضية السابقة وفرز الفجوات المفاهيمية.'
      },
      formative: {
        label: 'التقويم التكويني (البنائي):',
        task: formQ,
        purpose: 'متابعة الفهم أثناء الشرح والتدريب الموجه، مع تقديم التغذية الراجعة الفورية وتصحيح المسار لحظياً.'
      },
      summative: {
        label: 'التقويم الختامي (البعدي):',
        task: summQ,
        purpose: 'مهمة فردية سريعة في نهاية الحصة لقياس تحقق نواتج التعلم المستهدفة.'
      },
      differentiation: {
        remedial: {
          target: 'إجراء داعم للطلاب المتعثرين:',
          plan: `استخدام تمثيلات ونماذج ملموسة، وتجزئة المهمة إلى خطوات مبسطة مرقمة مع جدول إرشادي داعم وإشراكهم مع أقران متعاونين.`
        },
        enrichment: {
          target: 'نشاط إثرائي للطلاب المتفوقين:',
          plan: `تكليفهم بحل مسألة مفتوحة من مهارات التفكير العليا أو ابتكار مسألة حياتية جديدة وصياغة خطوات حلها وشرحها لزملائهم.`
        }
      }
    };

    // Station 6: Closure & Homework
    const station6 = {
      number: '٦',
      title: 'الغلق والواجب المنزلي المتدرج',
      timeMinutes: timeClosure,
      closure: `غلق الدرس: تلخيص مركز يربط أجزاء الدرس في جملة ختامية مفتاحية يصوغها الطلاب، مع ربط الفكرة بالدرس القادم وتثبيت المفهوم في الذاكرة.`,
      homework: {
        pages: pages,
        exercises: `تمارين محددة ومتدرجة من فقرات (تأكد) و(تدرب وحل المسائل) في كتاب الطالب بصفحات (${pages}) دون إرهاق الطالب بما يعزز الاستيعاب المستدام.`
      }
    };

    return {
      lessonId: lesson.id,
      metadata: station1.metadata,
      stations: [station1, station2, station3, station4, station5, station6],
      options: options
    };
  }

  // ================= Render Preparation Tab Pane =================
  function renderPrepPaneHTML(lesson, currentMode, aiGeneratedData) {
    const isG6 = !lesson.id || !lesson.id.startsWith('g1m');
    const activeSubTab = currentMode || 'approved'; // 'approved' | 'ai-studio'
    const prepData = (activeSubTab === 'ai-studio' && aiGeneratedData) 
      ? aiGeneratedData 
      : buildFullPreparation(lesson, { style: 'standard', focus: 'balanced' });

    const m = prepData.metadata;

    return `
      <div class="field-prep-container">
        
        <!-- Prep Mode Switcher (Standard Official vs AI Studio) -->
        <div class="prep-mode-bar">
          <div class="prep-mode-tabs">
            <button type="button" class="prep-mode-btn ${activeSubTab === 'approved' ? 'active' : ''}" onclick="window.LessonPrepManager.switchMode('approved')">
              📘 التحضير الميداني المعتمد (النموذج الرسمي الشامل)
            </button>
            <button type="button" class="prep-mode-btn ${activeSubTab === 'ai-studio' ? 'active' : ''}" onclick="window.LessonPrepManager.switchMode('ai-studio')">
              ✨ توليد التحضير بالذكاء الاصطناعي (AI Lesson Studio)
            </button>
          </div>

          <div class="prep-actions-group">
            <button type="button" class="nav-btn primary" onclick="window.LessonPrepManager.copyPrepToWord('${lesson.id}', ${activeSubTab === 'ai-studio'})" title="نسخ التحضير بالكامل كجدول رسمي جاهز للصق في Word">
              📋 نسخ التحضير إلى Word
            </button>
            <button type="button" class="nav-btn" onclick="window.print()" title="طباعة التحضير الميداني">
              🖨️ طباعة التحضير
            </button>
          </div>
        </div>

        ${activeSubTab === 'ai-studio' ? renderAiStudioControls(lesson) : ''}

        <!-- Official Ministerial Preparation Document View -->
        <div class="prep-document-sheet" id="prep-doc-sheet">
          
          <!-- Official Ministry Header Table -->
          <div class="prep-official-header-table">
            <table class="prep-header-table-grid">
              <tr>
                <td style="width:28%; text-align:right;">
                  <strong>المملكة العربية السعودية</strong><br>
                  وزارة التعليم<br>
                  المدارس المتقدمة للتعلم الذكي بجدة
                </td>
                <td style="width:44%; text-align:center;">
                  <h3 class="prep-header-main-title">نموذج تحضير الدرس الميداني الشامل المعتمد</h3>
                  <div class="prep-header-subtitle">مادة الرياضيات • وفق الأدلة والمعايير الوزارية المطورة</div>
                  <div class="prep-header-author">إعداد خبير الرياضيات: <strong>أ. محمد عبدالله جمعة</strong></div>
                </td>
                <td style="width:28%; text-align:left;" dir="ltr">
                  <div><strong>الصف:</strong> ${esc(m.grade)}</div>
                  <div><strong>الفصل:</strong> ${esc(m.term)}</div>
                  <div><strong>مدة الحصة:</strong> ${fmt(m.durationMinutes, isG6)} دقيقة</div>
                </td>
              </tr>
            </table>

            <div class="prep-lesson-banner-strip">
              <div class="banner-col"><strong>عنوان الدرس:</strong> ${esc(m.lessonTitle)}</div>
              <div class="banner-col"><strong>الفصل:</strong> ${esc(m.chapter)}</div>
              <div class="banner-col"><strong>صفحات الكتاب:</strong> ${fmt(m.pages, isG6)}</div>
              <div class="banner-col"><strong>التوزيع الزمني:</strong> ٥ + ١٠ + ١٥ + ١٠ + ٥ = <strong>${fmt(m.durationMinutes, isG6)} دقيقة</strong></div>
            </div>
          </div>

          <!-- Station 1: Objectives & Concepts -->
          ${renderStation1(prepData.stations[0], isG6)}

          <!-- Station 2: Hook & Prior Knowledge -->
          ${renderStation2(prepData.stations[1], isG6)}

          <!-- Station 3: Active Teaching Strategies -->
          ${renderStation3(prepData.stations[2], isG6)}

          <!-- Station 4: Structured Teaching & Tiered Solved Examples -->
          ${renderStation4(prepData.stations[3], isG6)}

          <!-- Station 5: Comprehensive Assessment & Differentiation -->
          ${renderStation5(prepData.stations[4], isG6)}

          <!-- Station 6: Closure & Homework -->
          ${renderStation6(prepData.stations[5], isG6)}

          <!-- Footer Endorsement -->
          <div class="prep-doc-footer-endorsement">
            <div>✓ تم التحضير وفق المعايير المهنية الميدانية لمعلمي الرياضيات بالمملكة العربية السعودية.</div>
            <div>خبير تدريس الرياضيات ومطور المنصة: <strong>أ. محمد عبدالله جمعة</strong> • المدارس المتقدمة للتعلم الذكي بجدة</div>
          </div>

        </div>

      </div>
    `;
  }

  function renderStation1(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <h4>${esc(s.title)}</h4>
        </div>
        <div class="prep-station-content">
          ${s.lessonIdea ? `
            <div class="prep-sub-box highlight">
              <strong>💡 فكرة الدرس المحورية:</strong> ${fmt(s.lessonIdea, isG6)}
            </div>
          ` : ''}

          <div style="margin-top:12px;">
            <strong style="color:var(--primary); display:block; margin-bottom:8px;">🎯 نواتج التعلم والأهداف السلوكية والمعرفية (قابلة للقياس والتحقق):</strong>
            <ul class="prep-styled-list">
              ${s.objectives.map((obj, i) => `
                <li>
                  <span class="list-bullet-num">${fmt(i + 1, isG6)}</span>
                  <span>${fmt(obj, isG6)}</span>
                </li>
              `).join('')}
            </ul>
          </div>

          <div style="margin-top:14px;">
            <strong style="color:var(--primary); display:block; margin-bottom:6px;">🏷️ المفاهيم والمصطلحات الرياضية الأساسية:</strong>
            <div class="prep-tags-row">
              ${s.vocabulary.map(v => `<span class="prep-vocab-tag">${fmt(v, isG6)}</span>`).join('')}
            </div>
          </div>
        </div>
      </div>
    `;
  }

  function renderStation2(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
            <h4>${esc(s.title)}</h4>
            <span class="station-time-pill">⏱️ ${fmt(s.timeMinutes, isG6)} دقائق</span>
          </div>
        </div>
        <div class="prep-station-content">
          <div class="prep-sub-box">
            <strong style="color:#b45309; display:block; margin-bottom:6px;">🔥 التمهيد والتهيئة المحفزة (ربط الواقع بالخبرة السابقة):</strong>
            <p style="line-height:1.7;">${fmt(s.hookDescription, isG6)}</p>
          </div>

          <div class="prep-sub-box" style="margin-top:10px; border-right-color:#0284c7; background:#f0f9ff;">
            <strong style="color:#0369a1; display:block; margin-bottom:6px;">🔍 كشف الجاهزية والخبرات السابقة:</strong>
            <p style="line-height:1.7;">${fmt(s.priorKnowledgeCheck, isG6)}</p>
          </div>
        </div>
      </div>
    `;
  }

  function renderStation3(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
            <h4>${esc(s.title)}</h4>
            <span class="station-time-pill">⏱️ ${fmt(s.timeMinutes, isG6)} دقائق</span>
          </div>
        </div>
        <div class="prep-station-content">
          <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom:12px;">
            تطبيق إجرائي دقيق خطوة بخطوة يوضح دور المعلم والطلاب والناتج المتوقع في كل استراتيجية:
          </p>

          <div class="prep-strategies-grid">
            ${s.items.map((st, idx) => `
              <div class="prep-strategy-box">
                <div class="strategy-box-header">
                  <span class="strategy-name">${fmt(idx + 1, isG6)}. ${esc(st.name)}</span>
                  <span class="strategy-time">${fmt(st.time, isG6)}</span>
                </div>
                <div class="strategy-step-row">
                  <span class="role-tag teacher">👨‍🏫 دور المعلم:</span>
                  <p>${fmt(st.teacherRole, isG6)}</p>
                </div>
                <div class="strategy-step-row">
                  <span class="role-tag students">👨‍🎓 دور الطلاب:</span>
                  <p>${fmt(st.studentRole, isG6)}</p>
                </div>
                <div class="strategy-step-row">
                  <span class="role-tag outcome">🎯 الناتج المتوقع:</span>
                  <p>${fmt(st.expectedOutcome, isG6)}</p>
                </div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }

  function renderStation4(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
            <h4>${esc(s.title)}</h4>
            <span class="station-time-pill">⏱️ ${fmt(s.timeMinutes, isG6)} دقيقة</span>
          </div>
        </div>
        <div class="prep-station-content">
          
          <!-- Concept Building -->
          <div class="prep-sub-box highlight">
            <strong style="color:var(--primary); display:block; margin-bottom:6px;">💡 بناء المفهوم وشرح الفكرة بأسلوب مبسط:</strong>
            <p style="line-height:1.75;">${fmt(s.conceptBuild, isG6)}</p>
          </div>

          <!-- Golden Rule -->
          ${s.goldenRule ? `
            <div class="prep-golden-banner">
              <span style="font-size:1.4rem;">🌟</span>
              <div>
                <strong>القاعدة الذهبية المعتمدة:</strong>
                <div>${fmt(s.goldenRule, isG6)}</div>
              </div>
            </div>
          ` : ''}

          <!-- Tiered Solved Examples -->
          <div style="margin-top:18px;">
            <strong style="color:var(--primary); font-size:1.05rem; display:block; margin-bottom:12px;">✍️ أمثلة محلولة متدرجة خطوة بخطوة:</strong>
            
            <div class="prep-examples-stack">
              ${s.examples.map(ex => `
                <div class="prep-example-card">
                  <div class="example-card-header">
                    <span class="example-level-tag">${esc(ex.level)}</span>
                    <span class="example-pedagogical-note">${esc(ex.note)}</span>
                  </div>
                  <div class="example-body-text">
                    <div style="margin-bottom:8px;"><strong>المسألة:</strong> ${fmt(ex.problem, isG6)}</div>
                    <div class="example-solution-box">
                      <strong>خطوات الحل والتحقق:</strong>
                      <div style="margin-top:4px; line-height:1.7;">${fmt(ex.solution, isG6)}</div>
                    </div>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Common Misconceptions & Immediate Remediation -->
          <div class="prep-misconception-card">
            <div class="misconception-card-header">
              <span>⚠️ الأخطاء الشائعة المتوقعة وكيفية معالجتها فوراً</span>
            </div>
            <div class="misconception-grid">
              <div class="misconception-col fallacy">
                <span class="mis-col-title">❌ الخطأ الشائع المتوقع:</span>
                <p>${fmt(s.misconception.fallacy, isG6)}</p>
              </div>
              <div class="misconception-col truth">
                <span class="mis-col-title">✓ المفهوم الرياضي الصحيح:</span>
                <p>${fmt(s.misconception.truth, isG6)}</p>
              </div>
            </div>
            <div class="misconception-remedy">
              <strong>🩺 استراتيجية التدخل والعلاج الفوري:</strong>
              <p style="margin-top:4px;">${fmt(s.misconception.remediation, isG6)}</p>
            </div>
          </div>

        </div>
      </div>
    `;
  }

  function renderStation5(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
            <h4>${esc(s.title)}</h4>
            <span class="station-time-pill">⏱️ ${fmt(s.timeMinutes, isG6)} دقائق</span>
          </div>
        </div>
        <div class="prep-station-content">
          
          <div class="prep-assessment-grid">
            <div class="assessment-card diag">
              <div class="assessment-card-title">🔍 ١. ${esc(s.diagnostic.label)}</div>
              <div class="assessment-card-purpose">${esc(s.diagnostic.purpose)}</div>
              <div class="assessment-card-task"><strong>المهمة:</strong> ${fmt(s.diagnostic.task, isG6)}</div>
            </div>

            <div class="assessment-card form">
              <div class="assessment-card-title">⚡ ٢. ${esc(s.formative.label)}</div>
              <div class="assessment-card-purpose">${esc(s.formative.purpose)}</div>
              <div class="assessment-card-task"><strong>المهمة:</strong> ${fmt(s.formative.task, isG6)}</div>
            </div>

            <div class="assessment-card summ">
              <div class="assessment-card-title">🎯 ٣. ${esc(s.summative.label)}</div>
              <div class="assessment-card-purpose">${esc(s.summative.purpose)}</div>
              <div class="assessment-card-task"><strong>المهمة:</strong> ${fmt(s.summative.task, isG6)}</div>
            </div>
          </div>

          <!-- Differentiation / Individual Differences -->
          <div class="prep-differentiation-box">
            <h5 style="color:#1e3a8a; font-weight:800; margin-bottom:10px;">🌟 مراعاة الفروق الفردية والتعليم المتمايز:</h5>
            <div class="diff-grid">
              <div class="diff-col remedial">
                <span class="diff-title">🌱 ${esc(s.differentiation.remedial.target)}</span>
                <p>${fmt(s.differentiation.remedial.plan, isG6)}</p>
              </div>
              <div class="diff-col enrichment">
                <span class="diff-title">🚀 ${esc(s.differentiation.enrichment.target)}</span>
                <p>${fmt(s.differentiation.enrichment.plan, isG6)}</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    `;
  }

  function renderStation6(s, isG6) {
    return `
      <div class="prep-station-card">
        <div class="prep-station-badge-title">
          <span class="station-circle-num">${s.number}</span>
          <div style="display:flex; align-items:center; justify-content:space-between; width:100%;">
            <h4>${esc(s.title)}</h4>
            <span class="station-time-pill">⏱️ ${fmt(s.timeMinutes, isG6)} دقائق</span>
          </div>
        </div>
        <div class="prep-station-content">
          <div class="prep-sub-box highlight">
            <strong style="color:var(--primary); display:block; margin-bottom:6px;">🎯 غلق الدرس وتثبيت المفهوم المحوري:</strong>
            <p style="line-height:1.7;">${fmt(s.closure, isG6)}</p>
          </div>

          <div class="prep-sub-box" style="margin-top:10px; border-right-color:#16a34a; background:#f0fdf4;">
            <strong style="color:#15803d; display:block; margin-bottom:6px;">📝 الواجب المنزلي المتدرج:</strong>
            <p style="line-height:1.7;">${fmt(s.homework.exercises, isG6)}</p>
          </div>
        </div>
      </div>
    `;
  }

  // AI Studio Configuration Box
  function renderAiStudioControls(lesson) {
    return `
      <div class="ai-studio-config-card">
        <div class="ai-studio-header">
          <span style="font-size:1.8rem;">✨</span>
          <div>
            <h4 style="font-size:1.15rem; font-weight:800; color:#1e3a8a;">استوديو توليد التحضير الميداني بالذكاء الاصطناعي</h4>
            <p style="font-size:0.85rem; color:var(--text-muted);">قم بتخصيص معايير الحصة ليقوم محرك الذكاء الاصطناعي بتوليد تحضير ميداني فريد ومخصص للدرس</p>
          </div>
        </div>

        <div class="ai-controls-grid">
          <div class="ai-control-group">
            <label>⏱️ مدة الحصة المقررة:</label>
            <select id="ai-duration-select" class="ai-select">
              <option value="45" selected>٤٥ دقيقة (حصة اعتيادية قياسية)</option>
              <option value="90">٩٠ دقيقة (حصة مزدوجة / تدريب مكثف)</option>
            </select>
          </div>

          <div class="ai-control-group">
            <label>🎯 النمط التدريسي المفضل:</label>
            <select id="ai-style-select" class="ai-select">
              <option value="standard" selected>متوازن (فكر-زاوج-شارك + نمذجة بصرية + تعلم تعاوني)</option>
              <option value="inquiry">استقصائي موجّه (اكتشاف النمط وحل المشكلات الحياتية)</option>
              <option value="visual">بصري ونمذجة (الرؤوس المرقمة + خط الأعداد والنماذج)</option>
              <option value="differentiated">متمايز مكثف (محطات التعلم المتدرجة وسد الفجوات)</option>
            </select>
          </div>

          <div class="ai-control-group">
            <label>🌟 مستوى تركيز الأنشطة:</label>
            <select id="ai-focus-select" class="ai-select">
              <option value="balanced" selected>متوازن قياسي (شامل لكافة مستويات الصف)</option>
              <option value="remedial">تأسيسي وعلاجي (تركيز على سد الفجوات والمحسوس)</option>
              <option value="enrichment">إثرائي ومتقدم (تفكير ناقد ورعاية الموهوبين)</option>
            </select>
          </div>
        </div>

        <div style="margin-top:14px; display:flex; justify-content:flex-end; gap:10px;">
          <button type="button" class="nav-btn primary" onclick="window.LessonPrepManager.triggerAiGeneration('${lesson.id}')">
            🚀 توليد التحضير المخصص بالذكاء الاصطناعي
          </button>
        </div>
      </div>
    `;
  }

  // ================= State & Manager API =================
  let currentActiveMode = 'approved';
  let cachedAiPreparations = {};

  const LessonPrepManager = {
    buildFullPreparation: buildFullPreparation,

    renderPane(lesson) {
      const aiData = cachedAiPreparations[lesson.id] || null;
      return renderPrepPaneHTML(lesson, currentActiveMode, aiData);
    },

    switchMode(mode) {
      currentActiveMode = mode;
      if (global.Platform && global.Platform.renderCurrentView) {
        global.Platform.renderCurrentView();
      }
    },

    triggerAiGeneration(lessonId) {
      const lesson = (global.CURRICULUM_DATA && global.CURRICULUM_DATA.lessons) ? global.CURRICULUM_DATA.lessons[lessonId] : null;
      if (!lesson) return;

      const durEl = document.getElementById('ai-duration-select');
      const styEl = document.getElementById('ai-style-select');
      const focEl = document.getElementById('ai-focus-select');

      const duration = durEl ? parseInt(durEl.value, 10) : 45;
      const style = styEl ? styEl.value : 'standard';
      const focus = focEl ? focEl.value : 'balanced';

      const generated = buildFullPreparation(lesson, {
        duration: duration,
        style: style,
        focus: focus
      });

      cachedAiPreparations[lessonId] = generated;
      currentActiveMode = 'ai-studio';

      const utils = getUtils();
      if (utils.showToast) {
        utils.showToast('✓ تم توليد التحضير الميداني بنجاح وفق المعايير المختارة!', 'success');
      }

      if (global.Platform && global.Platform.renderCurrentView) {
        global.Platform.renderCurrentView();
      }
    },

    // Copy to Word as fully formatted HTML Table with Ministry Header
    copyPrepToWord(lessonId, isAi) {
      const lesson = (global.CURRICULUM_DATA && global.CURRICULUM_DATA.lessons) ? global.CURRICULUM_DATA.lessons[lessonId] : null;
      if (!lesson) return;

      // Access verification for visitors
      if (global.FirebaseAuthManager && global.Platform) {
        const path = global.Platform.findLessonPath ? global.Platform.findLessonPath(lessonId) : null;
        if (path) {
          const lIdx = (path.chapter.lessons || []).findIndex(l => l.id === lessonId);
          if (!global.FirebaseAuthManager.isLessonUnlocked(path.chapter, lIdx >= 0 ? lIdx : 0)) {
            global.FirebaseAuthManager.showToast('🔒 ميزة نسخ التحضير إلى Word مخصصة للأعضاء المعتمدين والمدير العام. يرجى تسجيل الدخول للحصول على الاعتماد.', 'warning');
            global.FirebaseAuthManager.openAuthModal();
            return;
          }
        }
      }

      const prepData = (isAi && cachedAiPreparations[lessonId]) 
        ? cachedAiPreparations[lessonId] 
        : buildFullPreparation(lesson, { style: 'standard', focus: 'balanced' });

      const isG6 = !lesson.id || !lesson.id.startsWith('g1m');
      const m = prepData.metadata;

      const htmlContent = `
        <html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">
        <head>
          <meta charset="utf-8">
          <title>تحضير درس: ${esc(m.lessonTitle)}</title>
          <style>
            body { font-family: 'Cairo', 'Arial', sans-serif; direction: rtl; text-align: right; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 16px; }
            th, td { border: 1px solid #1e3a8a; padding: 8px 12px; font-size: 11pt; }
            .header-cell { background-color: #1e3a8a; color: #ffffff; font-weight: bold; text-align: center; font-size: 13pt; }
            .sub-header-cell { background-color: #dbeafe; color: #1e3a8a; font-weight: bold; }
            .station-title { background-color: #1e3a8a; color: #ffffff; font-weight: bold; font-size: 12pt; }
            .badge { background-color: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
          </style>
        </head>
        <body>
          <table>
            <tr>
              <td style="width:30%; text-align:right;">
                <strong>المملكة العربية السعودية</strong><br>
                وزارة التعليم<br>
                المدارس المتقدمة للتعلم الذكي بجدة
              </td>
              <td style="width:40%; text-align:center;">
                <h2 style="margin:0; color:#1e3a8a;">تحضير الدرس الميداني الشامل المعتمد</h2>
                <div>مادة الرياضيات • نموذج الأداء الإشرافي المطور</div>
                <div style="font-weight:bold; margin-top:4px;">إعداد خبير الرياضيات: أ. محمد عبدالله جمعة</div>
              </td>
              <td style="width:30%; text-align:left;" dir="ltr">
                <div><strong>الصف:</strong> ${esc(m.grade)}</div>
                <div><strong>الفصل:</strong> ${esc(m.term)}</div>
                <div><strong>مدة الحصة:</strong> ${fmt(m.durationMinutes, isG6)} دقيقة</div>
              </td>
            </tr>
          </table>

          <table>
            <tr class="sub-header-cell">
              <td><strong>عنوان الدرس:</strong> ${esc(m.lessonTitle)}</td>
              <td><strong>الباب / الفصل:</strong> ${esc(m.chapter)}</td>
              <td><strong>صفحات الكتاب:</strong> ${fmt(m.pages, isG6)}</td>
            </tr>
          </table>

          <!-- Station 1 -->
          <table>
            <tr><td colspan="2" class="station-title">١. البيانات والأهداف التعليمية ونواتج التعلّم</td></tr>
            ${prepData.stations[0].lessonIdea ? `<tr><td style="width:25%;"><strong>فكرة الدرس:</strong></td><td>${fmt(prepData.stations[0].lessonIdea, isG6)}</td></tr>` : ''}
            <tr>
              <td style="width:25%;"><strong>نواتج التعلم (الأهداف السلوكية):</strong></td>
              <td>
                <ol style="margin:0; padding-right:20px;">
                  ${prepData.stations[0].objectives.map(o => `<li>${fmt(o, isG6)}</li>`).join('')}
                </ol>
              </td>
            </tr>
            <tr>
              <td><strong>المفاهيم والمصطلحات:</strong></td>
              <td>${prepData.stations[0].vocabulary.map(v => fmt(v, isG6)).join(' • ')}</td>
            </tr>
          </table>

          <!-- Station 2 -->
          <table>
            <tr><td colspan="2" class="station-title">٢. التمهيد والتهيئة المحفزة وكشف الجاهزية (٥ دقائق)</td></tr>
            <tr>
              <td style="width:25%;"><strong>التهيئة والموقف الحياتي:</strong></td>
              <td>${fmt(prepData.stations[1].hookDescription, isG6)}</td>
            </tr>
            <tr>
              <td><strong>كشف الجاهزية والخبرات السابقة:</strong></td>
              <td>${fmt(prepData.stations[1].priorKnowledgeCheck, isG6)}</td>
            </tr>
          </table>

          <!-- Station 3 -->
          <table>
            <tr><td colspan="4" class="station-title">٣. استراتيجيات التدريس المتنوعة وتطبيقها الإجرائي في الدرس (١٠ دقائق)</td></tr>
            <tr class="sub-header-cell">
              <td style="width:25%;">الاستراتيجية</td>
              <td style="width:25%;">دور المعلم</td>
              <td style="width:25%;">دور الطلاب</td>
              <td style="width:25%;">الناتج المتوقع</td>
            </tr>
            ${prepData.stations[2].items.map(st => `
              <tr>
                <td><strong>${esc(st.name)}</strong> (${fmt(st.time, isG6)})</td>
                <td>${fmt(st.teacherRole, isG6)}</td>
                <td>${fmt(st.studentRole, isG6)}</td>
                <td>${fmt(st.expectedOutcome, isG6)}</td>
              </tr>
            `).join('')}
          </table>

          <!-- Station 4 -->
          <table>
            <tr><td colspan="2" class="station-title">٤. عرض الدرس والشرح المتدرج والأمثلة المحلولة ومعالجة الأخطاء (١٥ دقيقة)</td></tr>
            <tr>
              <td style="width:25%;"><strong>بناء المفهوم وشرح الفكرة:</strong></td>
              <td>${fmt(prepData.stations[3].conceptBuild, isG6)}</td>
            </tr>
            ${prepData.stations[3].goldenRule ? `
              <tr>
                <td><strong>القاعدة الذهبية المعتمدة:</strong></td>
                <td><strong>${fmt(prepData.stations[3].goldenRule, isG6)}</strong></td>
              </tr>
            ` : ''}
            <tr>
              <td><strong>الأمثلة المحلولة المتدرجة:</strong></td>
              <td>
                ${prepData.stations[3].examples.map(ex => `
                  <div style="margin-bottom:8px; padding-bottom:6px; border-bottom:1px dashed #cbd5e1;">
                    <strong>[${esc(ex.level)}]:</strong> ${fmt(ex.problem, isG6)}<br>
                    <strong>الحل:</strong> ${fmt(ex.solution, isG6)}
                  </div>
                `).join('')}
              </td>
            </tr>
            <tr>
              <td><strong>معالجة الأخطاء الشائعة:</strong></td>
              <td>
                <strong>الخطأ الشائع:</strong> ${fmt(prepData.stations[3].misconception.fallacy, isG6)}<br>
                <strong>المفهوم الصحيح:</strong> ${fmt(prepData.stations[3].misconception.truth, isG6)}<br>
                <strong>العلاج الفوري:</strong> ${fmt(prepData.stations[3].misconception.remediation, isG6)}
              </td>
            </tr>
          </table>

          <!-- Station 5 -->
          <table>
            <tr><td colspan="2" class="station-title">٥. منظومة التقويم الشاملة والتعليم المتمايز (١٠ دقائق)</td></tr>
            <tr>
              <td style="width:25%;"><strong>التقويم التشخيصي:</strong></td>
              <td>${fmt(prepData.stations[4].diagnostic.task, isG6)}</td>
            </tr>
            <tr>
              <td><strong>التقويم التكويني:</strong></td>
              <td>${fmt(prepData.stations[4].formative.task, isG6)}</td>
            </tr>
            <tr>
              <td><strong>التقويم الختامي:</strong></td>
              <td>${fmt(prepData.stations[4].summative.task, isG6)}</td>
            </tr>
            <tr>
              <td><strong>مراعاة الفروق الفردية:</strong></td>
              <td>
                <strong>دعم المتعثرين:</strong> ${fmt(prepData.stations[4].differentiation.remedial.plan, isG6)}<br>
                <strong>إثراء المتفوقين:</strong> ${fmt(prepData.stations[4].differentiation.enrichment.plan, isG6)}
              </td>
            </tr>
          </table>

          <!-- Station 6 -->
          <table>
            <tr><td colspan="2" class="station-title">٦. الغلق والواجب المنزلي (٥ دقائق)</td></tr>
            <tr>
              <td style="width:25%;"><strong>غلق الدرس وتثبيت الفكرة:</strong></td>
              <td>${fmt(prepData.stations[5].closure, isG6)}</td>
            </tr>
            <tr>
              <td><strong>الواجب المنزلي المتدرج:</strong></td>
              <td>${fmt(prepData.stations[5].homework.exercises, isG6)}</td>
            </tr>
          </table>

          <div style="margin-top:20px; text-align:center; font-size:10pt; color:#64748b;">
            تم إعداد هذا التحضير الميداني وفق متطلبات المناهج المطورة بالمملكة العربية السعودية • إعداد خبير الرياضيات: أ. محمد عبدالله جمعة
          </div>
        </body>
        </html>
      `;

      // Copy using modern Clipboard API with text/html fallback
      if (navigator.clipboard && navigator.clipboard.write) {
        const textBlob = new Blob([htmlContent.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ')], { type: 'text/plain' });
        const htmlBlob = new Blob([htmlContent], { type: 'text/html' });
        const item = new ClipboardItem({
          'text/html': htmlBlob,
          'text/plain': textBlob
        });

        navigator.clipboard.write([item]).then(() => {
          const utils = getUtils();
          if (utils.showToast) {
            utils.showToast('✓ تم نسخ التحضير الميداني بالكامل كجدول رسمي منسق وجاهز للصق في Word!', 'success');
          }
        }).catch(() => fallbackClipboardCopy(htmlContent));
      } else {
        fallbackClipboardCopy(htmlContent);
      }
    }
  };

  function fallbackClipboardCopy(html) {
    const ta = document.createElement('div');
    ta.innerHTML = html;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    const range = document.createRange();
    range.selectNode(ta);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
    document.body.removeChild(ta);

    const utils = getUtils();
    if (utils.showToast) {
      utils.showToast('✓ تم نسخ التحضير الميداني كجدول رسمي جاهز للصق في Word!', 'success');
    }
  }

  global.LessonPrepManager = LessonPrepManager;

})(typeof window !== 'undefined' ? window : globalThis);
