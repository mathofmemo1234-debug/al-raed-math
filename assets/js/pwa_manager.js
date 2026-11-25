/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * PWA Install Manager & Dynamic QR Code / Barcode Controller
 * ==========================================================================
 */

(function (global) {
  'use strict';

  let deferredPrompt = null;
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  const isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;

  // 1. Register Service Worker
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('./sw.js')
        .then((reg) => {
          console.log('✓ تم تسجيل Service Worker لمنصة الرائد بنجاح:', reg.scope);
        })
        .catch((err) => {
          console.warn('تعذر تسجيل Service Worker:', err);
        });
    });
  }

  // 2. Listen to BeforeInstallPrompt
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    updateInstallButtons(true);
  });

  window.addEventListener('appinstalled', () => {
    deferredPrompt = null;
    updateInstallButtons(false);
    if (global.ArabicUtils && global.ArabicUtils.showToast) {
      global.ArabicUtils.showToast('🎉 تهانينا! تم تثبيت منصة الرائد كتطبيق رسمي بنجاح.');
    }
  });

  function updateInstallButtons(available) {
    const btns = document.querySelectorAll('.pwa-install-btn');
    btns.forEach(b => {
      b.style.display = 'inline-flex';
      if (available) {
        b.classList.add('pulse');
      }
    });
  }

  // 3. Trigger Installation
  async function installPWA() {
    if (isStandalone) {
      if (global.ArabicUtils && global.ArabicUtils.showToast) {
        global.ArabicUtils.showToast('✓ التطبيق مثبت مسبقاً وتعمل حالياً بالنسخة المستقلة الكاملة.', 'info');
      } else {
        alert('التطبيق مثبت بالفعل على جهازك.');
      }
      return;
    }

    if (deferredPrompt) {
      deferredPrompt.prompt();
      const choice = await deferredPrompt.userChoice;
      if (choice.outcome === 'accepted') {
        deferredPrompt = null;
        updateInstallButtons(false);
      }
      return;
    }

    if (isIOS) {
      openIOSInstallModal();
      return;
    }

    // Default Guidance for Chrome / Edge / Android
    openDesktopInstallModal();
  }

  function openIOSInstallModal() {
    let modal = document.getElementById('raed-ios-install-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'raed-ios-install-modal';
      modal.className = 'raed-modal-backdrop';
      modal.innerHTML = `
        <div class="raed-auth-dialog" style="max-width:440px; text-align:center;">
          <div class="raed-auth-header">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:1.6rem;">📱</span>
              <h3 style="font-size:1.15rem; font-weight:800; color:#1e3a8a; margin:0;">تثبيت المنصة على آيفون / آيباد</h3>
            </div>
            <button type="button" class="raed-modal-close" onclick="document.getElementById('raed-ios-install-modal').style.display='none'">✖</button>
          </div>
          <div class="raed-auth-body" style="padding:20px; line-height:1.7;">
            <p style="font-size:0.92rem; color:#334155; margin-bottom:16px;">
              لتثبيت <strong>منصة الرائد التعليمية</strong> كتطبيق رسمي كامل على شاشتك الرئيسية:
            </p>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px; text-align:right; font-size:0.9rem;">
              <div style="margin-bottom:10px;">1️⃣ اضغط على زر <strong>المشاركة</strong> <span style="font-size:1.2rem;">⎋</span> في شريط المتصفح السفلي (Safari).</div>
              <div style="margin-bottom:10px;">2️⃣ مرر قائمة الخيارات لأسفل واختر <strong>«إضافة إلى الشاشة الرئيسية»</strong> ➕.</div>
              <div>3️⃣ اضغط على <strong>«إضافة» (Add)</strong> في أعلى اليمين.</div>
            </div>
            <div style="margin-top:16px;">
              <button type="button" class="nav-btn primary" style="width:100%; justify-content:center;" onclick="document.getElementById('raed-ios-install-modal').style.display='none'">فهمت ذلك ✓</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
    }
    modal.style.display = 'flex';
  }

  function openDesktopInstallModal() {
    let modal = document.getElementById('raed-desktop-install-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'raed-desktop-install-modal';
      modal.className = 'raed-modal-backdrop';
      modal.innerHTML = `
        <div class="raed-auth-dialog" style="max-width:440px; text-align:center;">
          <div class="raed-auth-header">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:1.6rem;">📥</span>
              <h3 style="font-size:1.15rem; font-weight:800; color:#1e3a8a; margin:0;">تثبيت المنصة على جهازك</h3>
            </div>
            <button type="button" class="raed-modal-close" onclick="document.getElementById('raed-desktop-install-modal').style.display='none'">✖</button>
          </div>
          <div class="raed-auth-body" style="padding:20px; line-height:1.7;">
            <p style="font-size:0.92rem; color:#334155; margin-bottom:16px;">
              يمكنك تثبيت المنصة مباشرة عبر متصفحك (Chrome / Edge / Safari):
            </p>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:14px; text-align:right; font-size:0.9rem;">
              <div style="margin-bottom:10px;">• اضغط على أيقونة <strong>تثبيت التطبيق</strong> 🖥️ الموجودة في شريط العنوان أعلى المتصفح.</div>
              <div>• أو اضغط على قائمة المتصفح (⋮) ثم اختر <strong>«تثبيت منصة الرائد التعليمية»</strong>.</div>
            </div>
            <div style="margin-top:16px;">
              <button type="button" class="nav-btn primary" style="width:100%; justify-content:center;" onclick="document.getElementById('raed-desktop-install-modal').style.display='none'">حسناً ✓</button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
    }
    modal.style.display = 'flex';
  }

  // 4. Barcode / QR Code Modal
  const PLATFORM_PUBLIC_URL = 'https://mjumaa-math.vercel.app/';

  function getShareUrl() {
    if (window.location && /^https?:\/\//i.test(window.location.href) && !/localhost|127\.0\.0\.1/i.test(window.location.hostname)) {
      return window.location.origin + '/';
    }
    return PLATFORM_PUBLIC_URL;
  }

  function openBarcodeModal() {
    let modal = document.getElementById('raed-barcode-modal');
    const shareUrl = PLATFORM_PUBLIC_URL;

    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'raed-barcode-modal';
      modal.className = 'raed-modal-backdrop';
      modal.innerHTML = `
        <div class="raed-auth-dialog" style="max-width:440px; text-align:center;">
          <div class="raed-auth-header">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:1.6rem;">📱</span>
              <h3 style="font-size:1.15rem; font-weight:800; color:#1e3a8a; margin:0;">باركود منصة الرائد التعليمية</h3>
            </div>
            <button type="button" class="raed-modal-close" onclick="document.getElementById('raed-barcode-modal').style.display='none'">✖</button>
          </div>
          <div class="raed-auth-body" style="padding:20px;">
            <p style="font-size:0.88rem; color:#475569; margin-bottom:14px;">
              امسح الباركود بكاميرا الجوال للدخول الفوري والمباشر إلى المنصة:
            </p>
            <div style="background:#ffffff; border:2px solid #e2e8f0; border-radius:16px; padding:16px; display:inline-block; box-shadow:0 6px 20px rgba(0,0,0,0.06);">
              <img src="assets/img/platform_qr.png?v=20261125_v6" alt="باركود منصة الرائد التعليمية" style="width:240px; height:240px; display:block; object-fit:contain; border-radius:8px;">
            </div>
            <div style="margin-top:12px; font-weight:800; font-size:1.05rem; color:#1e3a8a;">
              منصة الرائد التعليمية الذكية
            </div>
            <div style="font-size:0.82rem; color:#64748b; margin-top:2px;">
              إعداد خبير الرياضيات: أ. محمد عبدالله جمعة
            </div>
            <div style="margin-top:10px; background:#f1f5f9; border:1px solid #cbd5e1; border-radius:10px; padding:7px 12px; display:inline-block; direction:ltr;">
              <a href="${shareUrl}" target="_blank" rel="noopener noreferrer" style="color:#1d4ed8; font-weight:700; font-size:0.9rem; text-decoration:none; font-family:monospace;">${shareUrl}</a>
            </div>

            <div style="margin-top:18px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
              <button type="button" class="nav-btn primary" onclick="window.PWAManager.copyPlatformLink()">
                📋 <span>نسخ الرابط</span>
              </button>
              <button type="button" class="nav-btn" onclick="window.PWAManager.printBarcodeCard()">
                🖨️ <span>طباعة بطاقة الباركود</span>
              </button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
    }
    modal.style.display = 'flex';
  }

  function printBarcodeCard() {
    const shareUrl = PLATFORM_PUBLIC_URL;
    const win = window.open('', '_blank', 'width=640,height=820');
    if (!win) {
      window.print();
      return;
    }
    const baseHref = window.location.href.replace(/[^/]*$/, '');
    win.document.open();
    win.document.write(`<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex, nofollow">
  <base href="${baseHref}">
  <title>باركود منصة الرائد التعليمية</title>
  <style>
    @page { size: A4 portrait; margin: 18mm; }
    body { font-family: 'Cairo', 'Tajawal', 'Segoe UI', Arial, sans-serif; display:flex; justify-content:center; align-items:center; min-height:92vh; margin:0; background:#fff; color:#0f172a; }
    .card { border: 3px solid #1e3a8a; border-radius: 24px; padding: 36px 40px; text-align: center; max-width: 480px; width: 100%; box-shadow: 0 10px 30px rgba(30,58,138,0.08); }
    .logo { width: 72px; height: 72px; object-fit: contain; margin-bottom: 10px; }
    h1 { font-size: 26px; color: #1e3a8a; margin: 0 0 6px; font-weight: 900; }
    .sub { font-size: 16px; color: #475569; margin-bottom: 22px; font-weight: 600; }
    .qr-box { border: 2px solid #cbd5e1; border-radius: 18px; padding: 18px; display: inline-block; background: #fff; }
    .qr-box img { width: 290px; height: 290px; display: block; }
    .url { margin-top: 18px; font-family: monospace; font-size: 17px; font-weight: 700; color: #1d4ed8; direction: ltr; background: #eff6ff; padding: 8px 16px; border-radius: 10px; display: inline-block; }
    .hint { margin-top: 16px; font-size: 15px; color: #334155; font-weight: 700; }
  </style>
</head>
<body>
  <div class="card">
    <img class="logo" src="assets/img/my_logo.png" alt="شعار المنصة">
    <h1>منصة الرائد التعليمية الذكية</h1>
    <div class="sub">إعداد خبير الرياضيات: أ. محمد عبدالله جمعة</div>
    <div class="qr-box">
      <img src="assets/img/platform_qr.png?v=20261125_v6" alt="باركود المنصة">
    </div>
    <div><span class="url">${shareUrl}</span></div>
    <div class="hint">📱 امسح الباركود بكاميرا الجوال للدخول المباشر إلى المنصة</div>
  </div>
  <script>window.onload = function(){ setTimeout(function(){ window.print(); }, 350); };<\/script>
</body>
</html>`);
    win.document.close();
  }

  function copyPlatformLink() {
    const url = PLATFORM_PUBLIC_URL;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        if (global.ArabicUtils && global.ArabicUtils.showToast) {
          global.ArabicUtils.showToast('✓ تم نسخ رابط المنصة (' + url + ') بنجاح.');
        } else {
          alert('تم نسخ الرابط بنجاح: ' + url);
        }
      });
    } else {
      prompt('انسخ رابط المنصة:', url);
    }
  }

  global.PWAManager = {
    PLATFORM_URL: PLATFORM_PUBLIC_URL,
    installPWA: installPWA,
    openBarcodeModal: openBarcodeModal,
    printBarcodeCard: printBarcodeCard,
    copyPlatformLink: copyPlatformLink
  };

})(typeof window !== 'undefined' ? window : globalThis);
