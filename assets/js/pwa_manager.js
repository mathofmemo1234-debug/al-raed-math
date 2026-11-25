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
  function openBarcodeModal() {
    let modal = document.getElementById('raed-barcode-modal');
    const currentUrl = window.location.href.split('#')[0];
    
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'raed-barcode-modal';
      modal.className = 'raed-modal-backdrop';
      modal.innerHTML = `
        <div class="raed-auth-dialog" style="max-width:420px; text-align:center;">
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
              <img src="assets/img/platform_qr.png" alt="باركود المنصة" style="width:230px; height:230px; display:block; object-fit:contain; border-radius:8px;">
            </div>
            <div style="margin-top:12px; font-weight:800; font-size:1rem; color:#1e3a8a;">
              منصة الرائد التعليمية الذكية
            </div>
            <div style="font-size:0.8rem; color:#64748b; margin-top:2px;">
              إعداد خبير الرياضيات: أ. محمد عبدالله جمعة
            </div>

            <div style="margin-top:18px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
              <button type="button" class="nav-btn primary" onclick="window.PWAManager.copyPlatformLink()">
                📋 <span>نسخ الرابط</span>
              </button>
              <button type="button" class="nav-btn" onclick="window.print()">
                🖨️ <span>طباعة الباركود</span>
              </button>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(modal);
    }
    modal.style.display = 'flex';
  }

  function copyPlatformLink() {
    const url = window.location.href.split('#')[0];
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        if (global.ArabicUtils && global.ArabicUtils.showToast) {
          global.ArabicUtils.showToast('✓ تم نسخ رابط المنصة إلى الحافظة بنجاح.');
        } else {
          alert('تم نسخ الرابط بنجاح.');
        }
      });
    } else {
      prompt('انسخ رابط المنصة:', url);
    }
  }

  global.PWAManager = {
    installPWA: installPWA,
    openBarcodeModal: openBarcodeModal,
    copyPlatformLink: copyPlatformLink
  };

})(typeof window !== 'undefined' ? window : globalThis);
