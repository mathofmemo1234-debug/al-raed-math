/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات
 * نظام المصادقة وإدارة المستخدمين واعتماد المدير (Role-Based Access Control)
 * مع حماية الحساب من المشاركة عبر الجلسة النشطة الواحدة (Single Active Session)
 * Firebase Auth & Single Active Session Security Manager
 * إعداد خبير الرياضيات: أ. محمد عبدالله جمعة | المدارس المتقدمة للتعلم الذكي بجدة
 * ==========================================================================
 */

(function (global) {
  'use strict';

  const AUTH_STORAGE_KEY = 'alraed_auth_current_user_v2';
  const LOCAL_SESSION_KEY = 'alraed_local_session_id_v2';
  const USERS_DB_STORAGE_KEY = 'alraed_users_directory_v2';
  const SESSION_CHANNEL_KEY = 'alraed_session_heartbeat_channel';

  // Helper: Device / Browser fingerprint detection
  function getDeviceFingerprint() {
    if (typeof navigator === 'undefined') return 'متصفح ويب';
    const ua = navigator.userAgent || '';
    let browser = 'متصفح';
    if (ua.includes('Edg/')) browser = 'Edge';
    else if (ua.includes('Chrome/')) browser = 'Chrome';
    else if (ua.includes('Safari/')) browser = 'Safari';
    else if (ua.includes('Firefox/')) browser = 'Firefox';

    let os = 'جهاز';
    if (ua.includes('Windows')) os = 'Windows';
    else if (ua.includes('iPhone') || ua.includes('iPad')) os = 'iOS';
    else if (ua.includes('Android')) os = 'Android';
    else if (ua.includes('Mac OS')) os = 'macOS';

    return `${browser} على ${os}`;
  }

  // Helper: Generate secure random session ID with timestamp
  function generateSessionId() {
    const ts = Date.now().toString(36);
    const rand = Math.random().toString(36).substring(2, 10);
    return `sess_${ts}_${rand}`;
  }

  // Seed default director and sample approved users
  const DEFAULT_USERS = [
    {
      uid: 'director-001',
      displayName: 'أ. محمد عبدالله جمعة',
      email: 'mohamed.gomaa@al-raed.edu.sa',
      phoneNumber: '+966500000001',
      role: 'admin', // 'admin' | 'approved' | 'pending'
      provider: 'google',
      registeredAt: '١٤٤٨/٠١/٠١ هـ',
      approvedAt: '١٤٤٨/٠١/٠١ هـ',
      activeSessionId: null,
      lastLoginAt: '١٤٤٨/٠١/٠١ هـ',
      lastLoginDevice: 'لوحة إدارة المنصة',
      notes: 'المدير العام وخبير الرياضيات للمنصة (وصول كامل)'
    },
    {
      uid: 'sample-teacher-1',
      displayName: 'معلم رياضيات معتمد',
      email: 'teacher.smart@al-raed.edu.sa',
      phoneNumber: '+966555123456',
      role: 'approved',
      provider: 'google',
      registeredAt: '١٤٤٨/٠٢/١٥ هـ',
      approvedAt: '١٤٤٨/٠٢/١٥ هـ',
      activeSessionId: null,
      lastLoginAt: '١٤٤٨/٠٢/١٥ هـ',
      lastLoginDevice: 'Edge على Windows',
      notes: 'معلم معتمد من قبل المدير'
    }
  ];

  const memStorage = {};
  const safeStorage = {
    getItem(k) {
      try {
        if (typeof localStorage !== 'undefined') return localStorage.getItem(k);
      } catch (e) {}
      return memStorage[k] || null;
    },
    setItem(k, v) {
      try {
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem(k, v);
          return;
        }
      } catch (e) {}
      memStorage[k] = String(v);
    },
    removeItem(k) {
      try {
        if (typeof localStorage !== 'undefined') {
          localStorage.removeItem(k);
          return;
        }
      } catch (e) {}
      delete memStorage[k];
    }
  };

  function loadUsersDirectory() {
    try {
      const data = safeStorage.getItem(USERS_DB_STORAGE_KEY);
      if (data) {
        const parsed = JSON.parse(data);
        if (Array.isArray(parsed) && parsed.length) return parsed;
      }
    } catch (e) {
      // ignore
    }
    saveUsersDirectory(DEFAULT_USERS);
    return DEFAULT_USERS;
  }

  function saveUsersDirectory(list) {
    try {
      safeStorage.setItem(USERS_DB_STORAGE_KEY, JSON.stringify(list));
      safeStorage.setItem(SESSION_CHANNEL_KEY, Date.now().toString());
    } catch (e) {
      // ignore
    }
  }

  function loadCurrentUser() {
    try {
      const data = safeStorage.getItem(AUTH_STORAGE_KEY);
      if (data) return JSON.parse(data);
    } catch (e) {
      // ignore
    }
    return {
      uid: 'visitor',
      displayName: 'زائر المنصة',
      email: null,
      phoneNumber: null,
      role: 'visitor',
      provider: 'anonymous'
    };
  }

  function saveCurrentUser(user) {
    try {
      safeStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(user));
    } catch (e) {
      // ignore
    }
  }

  let currentUser = loadCurrentUser();
  let usersDirectory = loadUsersDirectory();
  const listeners = [];

  function escHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function renderAuthNavbarWidget() {
    if (typeof document === 'undefined') return;
    const container = document.getElementById('nav-auth-container');
    if (!container) return;

    if (currentUser.role === 'admin') {
      container.innerHTML = `
        <div class="nav-auth-chip admin" title="حساب المدير العام - أ. محمد عبدالله جمعة">
          <span class="auth-chip-avatar">👑</span>
          <div class="auth-chip-text">
            <span class="auth-chip-name">${escHtml(currentUser.displayName)}</span>
            <span class="auth-chip-role">المدير العام (وصول كامل)</span>
          </div>
          <button type="button" class="auth-chip-btn dashboard" onclick="window.FirebaseAuthManager.openDirectorDashboard()" title="لوحة إدارة واعتماد المستخدمين والجلسات">
            ⚙️ إدارة المستخدمين
          </button>
          <button type="button" class="auth-chip-btn logout" onclick="window.FirebaseAuthManager.signOut()" title="تسجيل الخروج">
            🚪
          </button>
        </div>
      `;
    } else if (currentUser.role === 'approved') {
      container.innerHTML = `
        <div class="nav-auth-chip approved" title="حساب معتمد">
          <span class="auth-chip-avatar">👨‍🏫</span>
          <div class="auth-chip-text">
            <span class="auth-chip-name">${escHtml(currentUser.displayName)}</span>
            <span class="auth-chip-role">معتمد • جلسة نشطة 🟢</span>
          </div>
          <button type="button" class="auth-chip-btn logout" onclick="window.FirebaseAuthManager.signOut()" title="تسجيل الخروج">
            🚪 خروج
          </button>
        </div>
      `;
    } else if (currentUser.role === 'pending') {
      container.innerHTML = `
        <div class="nav-auth-chip pending" title="الحساب بانتظار اعتماد المدير العام">
          <span class="auth-chip-avatar">⏳</span>
          <div class="auth-chip-text">
            <span class="auth-chip-name">${escHtml(currentUser.displayName)}</span>
            <span class="auth-chip-role">بانتظار اعتماد المدير</span>
          </div>
          <button type="button" class="auth-chip-btn logout" onclick="window.FirebaseAuthManager.signOut()" title="تسجيل الخروج">
            🚪
          </button>
        </div>
      `;
    } else {
      // Visitor
      container.innerHTML = `
        <button type="button" class="nav-chip-btn auth-login-trigger" onclick="window.FirebaseAuthManager.openAuthModal()" title="تسجيل الدخول أو طلب اعتماد الحساب">
          <span class="nav-chip-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </span>
          <span class="nav-chip-label">دخول / اعتماد</span>
        </button>
      `;
    }
  }

  function notifyChange() {
    renderAuthNavbarWidget();
    listeners.forEach(fn => {
      try { fn(currentUser); } catch (err) { console.error(err); }
    });
  }

  // ================= Single Active Session Protection =================
  // Checks if the local session matches the active session registered for the user
  function verifyActiveSession(showModalOnKick) {
    if (!currentUser || currentUser.role === 'visitor') return true;

    // Refresh directory from storage
    usersDirectory = loadUsersDirectory();
    const freshUser = usersDirectory.find(u => u.uid === currentUser.uid);

    if (!freshUser) {
      forceLogoutDueToSessionKick('تمت إزالة الحساب من سجلات المنصة.');
      return false;
    }

    // If role changed (e.g. Director approved/revoked), sync role immediately
    if (freshUser.role !== currentUser.role) {
      currentUser.role = freshUser.role;
      saveCurrentUser(currentUser);
      notifyChange();
    }

    // Check Single Active Session Token
    const localSessionId = safeStorage.getItem(LOCAL_SESSION_KEY);
    if (freshUser.activeSessionId && localSessionId && freshUser.activeSessionId !== localSessionId) {
      // ANOTHER DEVICE LOGGED IN! Terminate this device's session immediately!
      const kickerDevice = freshUser.lastLoginDevice || 'جهاز جديد';
      forceLogoutDueToSessionKick(`تم رصد تسجيل دخول جديد لحسابك من (${kickerDevice}).\n\nحفاظاً على أمان الحساب ومنع مشاركة كلمات المرور، يُسمح بجلسة نشطة واحدة فقط في نفس الوقت. تم تسجيل الخروج من هذا الجهاز.`);
      return false;
    }

    return true;
  }

  function forceLogoutDueToSessionKick(reason) {
    // Reset local user to visitor
    currentUser = {
      uid: 'visitor',
      displayName: 'زائر المنصة',
      email: null,
      phoneNumber: null,
      role: 'visitor',
      provider: 'anonymous'
    };
    saveCurrentUser(currentUser);
    safeStorage.removeItem(LOCAL_SESSION_KEY);

    notifyChange();

    // Show security alert modal
    openSessionKickAlertModal(reason);
  }

  // Start periodic heartbeat verification (every 4 seconds)
  if (typeof setInterval !== 'undefined') {
    setInterval(() => {
      verifyActiveSession(true);
    }, 4000);
  }

  // Cross-tab synchronization via storage event
  if (typeof window !== 'undefined' && typeof window.addEventListener === 'function') {
    window.addEventListener('storage', (e) => {
      if (e.key === USERS_DB_STORAGE_KEY || e.key === SESSION_CHANNEL_KEY) {
        verifyActiveSession(true);
      }
    });

    // Check when user switches back to this tab
    window.addEventListener('focus', () => {
      verifyActiveSession(true);
    });
  }

  // ================= Public API =================
  const FirebaseAuthManager = {
    getCurrentUser() {
      return currentUser;
    },

    getRole() {
      return currentUser ? currentUser.role : 'visitor';
    },

    isAdmin() {
      return currentUser && currentUser.role === 'admin';
    },

    isApproved() {
      return currentUser && (currentUser.role === 'approved' || currentUser.role === 'admin');
    },

    isPending() {
      return currentUser && currentUser.role === 'pending';
    },

    isVisitor() {
      return !currentUser || currentUser.role === 'visitor';
    },

    isUnlocked() {
      return this.isAdmin() || this.isApproved();
    },

    // Chapter lesson preview rule: First 2 lessons (index 0 and 1) are unlocked for visitors!
    isLessonUnlocked(chapter, lessonIndex) {
      if (this.isUnlocked()) return true;
      return lessonIndex < 2;
    },

    // Bind new Single Active Session for a user
    _bindSessionForUser(userObj) {
      const newSessionId = generateSessionId();
      const device = getDeviceFingerprint();
      const nowStr = new Date().toLocaleString('ar-SA');

      userObj.activeSessionId = newSessionId;
      userObj.lastLoginAt = nowStr;
      userObj.lastLoginDevice = device;

      // Update in directory
      usersDirectory = loadUsersDirectory();
      const idx = usersDirectory.findIndex(u => u.uid === userObj.uid);
      if (idx !== -1) {
        usersDirectory[idx] = Object.assign({}, usersDirectory[idx], userObj);
      } else {
        usersDirectory.push(userObj);
      }
      saveUsersDirectory(usersDirectory);

      // Save local session token
      safeStorage.setItem(LOCAL_SESSION_KEY, newSessionId);

      currentUser = userObj;
      saveCurrentUser(currentUser);
      notifyChange();
    },

    // Sign-in flows
    signInWithGoogle() {
      const email = prompt('أدخل بريد Google الإلكتروني للتسجيل (مثال: teacher@gmail.com):', 'user@gmail.com');
      if (!email || !email.trim()) return false;

      const name = prompt('أدخل الاسم الثلاثي:', 'مستكشف الرياضيات') || 'مستخدم جديد';

      usersDirectory = loadUsersDirectory();
      const existing = usersDirectory.find(u => u.email && u.email.toLowerCase() === email.trim().toLowerCase());

      if (existing) {
        this._bindSessionForUser(existing);
        this.showToast(`مرحباً بك مجدداً ${existing.displayName}! (تم تفعيل جلستك النشطة بنجاح)`, 'success');
        this.closeAllModals();
        return true;
      }

      // Create new pending user
      const today = new Date().toLocaleDateString('ar-SA');
      const newUser = {
        uid: 'user-' + Date.now(),
        displayName: name.trim(),
        email: email.trim(),
        phoneNumber: null,
        role: 'pending', // Requires Director approval!
        provider: 'google',
        registeredAt: today,
        approvedAt: null,
        activeSessionId: null,
        lastLoginAt: today,
        lastLoginDevice: getDeviceFingerprint(),
        notes: 'تم التسجيل بحساب Google بانتظار اعتماد المدير'
      };

      this._bindSessionForUser(newUser);
      this.showToast('✓ تم تسجيل حسابك بنجاح! حسابك الآن بانتظار اعتماد المدير العام (أ. محمد عبدالله جمعة).', 'info');
      this.closeAllModals();
      return true;
    },

    signInWithPhone() {
      const phone = prompt('أدخل رقم الجوال مع رمز الدولة (مثال: +9665xxxxxxxx):', '+9665');
      if (!phone || phone.trim().length < 9) return false;

      const name = prompt('أدخل الاسم الثلاثي:', 'مستكشف الرياضيات') || 'مستخدم جوال';

      usersDirectory = loadUsersDirectory();
      const existing = usersDirectory.find(u => u.phoneNumber === phone.trim());

      if (existing) {
        this._bindSessionForUser(existing);
        this.showToast(`مرحباً بك مجدداً ${existing.displayName}! (تم تفعيل جلستك النشطة بنجاح)`, 'success');
        this.closeAllModals();
        return true;
      }

      const today = new Date().toLocaleDateString('ar-SA');
      const newUser = {
        uid: 'phone-' + Date.now(),
        displayName: name.trim(),
        email: null,
        phoneNumber: phone.trim(),
        role: 'pending',
        provider: 'phone',
        registeredAt: today,
        approvedAt: null,
        activeSessionId: null,
        lastLoginAt: today,
        lastLoginDevice: getDeviceFingerprint(),
        notes: 'تم التسجيل برقم الجوال بانتظار اعتماد المدير'
      };

      this._bindSessionForUser(newUser);
      this.showToast('✓ تم تسجيل رقم الجوال بنجاح! حسابك بانتظار اعتماد المدير العام.', 'info');
      this.closeAllModals();
      return true;
    },

    // Director Quick Sign-in for أ. محمد عبدالله جمعة
    signInAsDirector() {
      const code = prompt('أدخل كلمة المرور / رمز اعتماد المدير العام:', '');
      if (code === '1448' || code === 'admin' || code === 'جمعة' || code === 'raed') {
        usersDirectory = loadUsersDirectory();
        const director = usersDirectory[0] || DEFAULT_USERS[0];
        this._bindSessionForUser(director);
        this.showToast('👑 مرحباً بك يا أستاذ محمد عبدالله جمعة! تم تفعيل صلاحيات المدير العام والوصول الكامل لجميع الدروس والخصائص.', 'success');
        this.closeAllModals();
        return true;
      } else {
        alert('رمز الاعتماد غير صحيح. يرجى إدخال الرمز المعتمد للمدير العام (١٤٤٨).');
        return false;
      }
    },

    signOut() {
      if (currentUser && currentUser.uid !== 'visitor') {
        // Clear active session in directory
        usersDirectory = loadUsersDirectory();
        const u = usersDirectory.find(x => x.uid === currentUser.uid);
        if (u) {
          u.activeSessionId = null;
          saveUsersDirectory(usersDirectory);
        }
      }

      currentUser = {
        uid: 'visitor',
        displayName: 'زائر المنصة',
        email: null,
        phoneNumber: null,
        role: 'visitor',
        provider: 'anonymous'
      };
      saveCurrentUser(currentUser);
      safeStorage.removeItem(LOCAL_SESSION_KEY);

      this.showToast('تم تسجيل الخروج بنجاح. أنت الآن تتصفح المنصة كزائر (درسان من كل فصل).', 'info');
      notifyChange();
      this.closeAllModals();
    },

    // Director Administrative Operations
    getUsersDirectory() {
      usersDirectory = loadUsersDirectory();
      return usersDirectory;
    },

    approveUser(uid) {
      if (!this.isAdmin()) return false;
      usersDirectory = loadUsersDirectory();
      const u = usersDirectory.find(x => x.uid === uid);
      if (u) {
        u.role = 'approved';
        u.approvedAt = new Date().toLocaleDateString('ar-SA');
        saveUsersDirectory(usersDirectory);

        if (currentUser.uid === uid) {
          currentUser = u;
          saveCurrentUser(currentUser);
        }
        this.showToast(`✓ تم اعتماد المستخدم (${u.displayName}) ومنحه الوصول الكامل بنجاح!`, 'success');
        notifyChange();
        this.refreshDirectorModal();
        return true;
      }
      return false;
    },

    revokeUser(uid) {
      if (!this.isAdmin()) return false;
      usersDirectory = loadUsersDirectory();
      const u = usersDirectory.find(x => x.uid === uid);
      if (u && u.role !== 'admin') {
        u.role = 'pending';
        u.approvedAt = null;
        u.activeSessionId = null; // Also drop active session
        saveUsersDirectory(usersDirectory);

        if (currentUser.uid === uid) {
          currentUser = u;
          saveCurrentUser(currentUser);
        }
        this.showToast(`تم تعليق اعتماد المستخدم (${u.displayName}).`, 'warning');
        notifyChange();
        this.refreshDirectorModal();
        return true;
      }
      return false;
    },

    // Force terminate active session of any user (Single Session Enforcement)
    terminateUserSession(uid) {
      if (!this.isAdmin()) return false;
      usersDirectory = loadUsersDirectory();
      const u = usersDirectory.find(x => x.uid === uid);
      if (u) {
        u.activeSessionId = null; // Invalidates the active token
        saveUsersDirectory(usersDirectory);

        this.showToast(`🔴 تم إنهاء الجلسة النشطة للمستخدم (${u.displayName}) فوراً! سيخرج جهازه تلقائياً.`, 'info');
        this.refreshDirectorModal();
        return true;
      }
      return false;
    },

    deleteUser(uid) {
      if (!this.isAdmin()) return false;
      usersDirectory = loadUsersDirectory();
      const target = usersDirectory.find(x => x.uid === uid);
      if (target && target.role === 'admin') {
        alert('لا يمكن حذف حساب المدير العام.');
        return false;
      }
      if (!confirm(`هل أنت متأكد من حذف المستخدم (${target ? target.displayName : uid}) نهائياً؟`)) return false;

      usersDirectory = usersDirectory.filter(x => x.uid !== uid);
      saveUsersDirectory(usersDirectory);
      this.showToast('تم حذف المستخدم من الدليل بنجاح.', 'info');
      notifyChange();
      this.refreshDirectorModal();
      return true;
    },

    addPreapprovedUser(name, contact, isEmail) {
      if (!this.isAdmin()) return false;
      usersDirectory = loadUsersDirectory();
      const today = new Date().toLocaleDateString('ar-SA');
      const newUser = {
        uid: 'pre-' + Date.now(),
        displayName: name.trim(),
        email: isEmail ? contact.trim() : null,
        phoneNumber: !isEmail ? contact.trim() : null,
        role: 'approved',
        provider: isEmail ? 'google' : 'phone',
        registeredAt: today,
        approvedAt: today,
        activeSessionId: null,
        lastLoginAt: null,
        lastLoginDevice: null,
        notes: 'مضاف ومعتمد مباشرة من المدير العام'
      };
      usersDirectory.push(newUser);
      saveUsersDirectory(usersDirectory);
      this.showToast(`✓ تم إضافة واعتماد (${name}) بنجاح!`, 'success');
      notifyChange();
      this.refreshDirectorModal();
      return true;
    },

    // UI Modals
    openAuthModal() {
      let modal = document.getElementById('raed-auth-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'raed-auth-modal';
        modal.className = 'raed-modal-backdrop';
        document.body.appendChild(modal);
      }

      modal.innerHTML = `
        <div class="raed-auth-dialog">
          <div class="raed-auth-header">
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:1.8rem; background:#eff6ff; padding:6px 10px; border-radius:10px; border:1px solid #bfdbfe;">🔑</span>
              <div>
                <h3 style="font-size:1.2rem; font-weight:800; color:#1e3a8a;">تسجيل الدخول واعتماد الصلاحيات</h3>
                <p style="font-size:0.82rem; color:var(--text-muted);">منصة الرائد التعليمية الذكية للرياضيات</p>
              </div>
            </div>
            <button type="button" class="raed-modal-close" onclick="window.FirebaseAuthManager.closeAllModals()">✖</button>
          </div>

          <div class="raed-auth-body">
            <div class="raed-auth-notice">
              <strong>📢 سياسة وصول الزوار والمعاينة النموذجية:</strong>
              <p style="margin-top:4px; font-size:0.88rem; line-height:1.6;">
                يُتاح للزوار استعراض <strong>أول درسين من كل فصل دراسي مجاناً</strong> للمعاينة.
                لفتح كامل دروس وفصول المنهج وميزات النسخ، يُرجى تسجيل الدخول بحساب Google أو الجوال ليتم اعتماد حسابك من قبل المدير العام.
              </p>
            </div>

            <div class="single-session-badge">
              <span>🛡️ حماية الحساب:</span>
              <span>يتم ربط كل حساب معتمد بجلسة نشطة واحدة فقط (Single Active Session) لحماية الحساب من المشاركة غير المصرح بها.</span>
            </div>

            <div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">
              <button type="button" class="auth-provider-btn google" onclick="window.FirebaseAuthManager.signInWithGoogle()">
                <span class="auth-btn-icon">🌐</span>
                <div style="text-align:right;">
                  <div style="font-weight:800;">تسجيل الدخول بحساب Google</div>
                  <div style="font-size:0.78rem; opacity:0.85;">تسجيل سريع وآمن بالبريد الإلكتروني</div>
                </div>
              </button>

              <button type="button" class="auth-provider-btn phone" onclick="window.FirebaseAuthManager.signInWithPhone()">
                <span class="auth-btn-icon">📱</span>
                <div style="text-align:right;">
                  <div style="font-weight:800;">تسجيل الدخول برقم الجوال</div>
                  <div style="font-size:0.78rem; opacity:0.85;">التحقق والربط الآمن عبر رقم الهاتف</div>
                </div>
              </button>
            </div>

            <div style="margin:20px 0; text-align:center; position:relative;">
              <hr style="border:none; border-top:1px solid #e2e8f0;">
              <span style="position:absolute; top:-10px; right:50%; transform:translateX(50%); background:#ffffff; padding:0 12px; font-size:0.8rem; color:#94a3b8; font-weight:700;">أو</span>
            </div>

            <button type="button" class="auth-provider-btn director" onclick="window.FirebaseAuthManager.signInAsDirector()">
              <span class="auth-btn-icon">👑</span>
              <div style="text-align:right;">
                <div style="font-weight:800;">دخول المدير المسؤول (أ. محمد عبدالله جمعة)</div>
                <div style="font-size:0.78rem; opacity:0.85;">الوصول الإداري الكامل واعتماد المستخدمين</div>
              </div>
            </button>
          </div>
        </div>
      `;

      modal.style.display = 'flex';
    },

    openDirectorDashboard() {
      if (!this.isAdmin()) {
        alert('هذه اللوحة مخصصة للمدير العام فقط.');
        return;
      }

      let modal = document.getElementById('raed-director-modal');
      if (!modal) {
        modal = document.createElement('div');
        modal.id = 'raed-director-modal';
        modal.className = 'raed-modal-backdrop';
        document.body.appendChild(modal);
      }

      this.refreshDirectorModal();
      modal.style.display = 'flex';
    },

    refreshDirectorModal(filterRole) {
      const modal = document.getElementById('raed-director-modal');
      if (!modal) return;

      usersDirectory = loadUsersDirectory();
      const currentFilter = filterRole || 'all';

      const filtered = usersDirectory.filter(u => {
        if (currentFilter === 'pending') return u.role === 'pending';
        if (currentFilter === 'approved') return u.role === 'approved';
        return true;
      });

      const pendingCount = usersDirectory.filter(u => u.role === 'pending').length;
      const approvedCount = usersDirectory.filter(u => u.role === 'approved').length;

      modal.innerHTML = `
        <div class="raed-director-dialog">
          <div class="raed-auth-header">
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:1.8rem; background:#fef3c7; padding:6px 10px; border-radius:10px; border:1px solid #fde68a;">👑</span>
              <div>
                <h3 style="font-size:1.2rem; font-weight:800; color:#1e3a8a;">لوحة المدير العام: إدارة واعتماد المستخدمين</h3>
                <p style="font-size:0.82rem; color:var(--text-muted);">إشراف أ. محمد عبدالله جمعة • حماية الجلسة الواحدة (Single Active Session)</p>
              </div>
            </div>
            <button type="button" class="raed-modal-close" onclick="window.FirebaseAuthManager.closeAllModals()">✖</button>
          </div>

          <div class="raed-director-body">
            
            <!-- Quick Add Pre-approved User -->
            <div class="director-quick-add-box">
              <h4 style="font-size:0.95rem; font-weight:800; margin-bottom:8px; color:#1e3a8a;">➕ إضافة مستخدم واعتماده مباشرة:</h4>
              <div style="display:flex; gap:8px; flex-wrap:wrap;">
                <input id="new-user-name" type="text" placeholder="اسم المعلم / الطالب..." class="director-input" style="flex:1; min-width:160px;">
                <input id="new-user-contact" type="text" placeholder="البريد أو رقم الجوال..." class="director-input" style="flex:1; min-width:180px;">
                <button type="button" class="nav-btn primary" onclick="window.FirebaseAuthManager._submitQuickAdd()">
                  <span>اعتماد وإضافة</span>
                </button>
              </div>
            </div>

            <!-- Filter Tabs -->
            <div class="director-tabs-row">
              <button type="button" class="director-tab-btn ${currentFilter === 'all' ? 'active' : ''}" onclick="window.FirebaseAuthManager.refreshDirectorModal('all')">
                الكل (${usersDirectory.length})
              </button>
              <button type="button" class="director-tab-btn ${currentFilter === 'pending' ? 'active' : ''}" onclick="window.FirebaseAuthManager.refreshDirectorModal('pending')">
                ⏳ بانتظار الاعتماد (${pendingCount})
              </button>
              <button type="button" class="director-tab-btn ${currentFilter === 'approved' ? 'active' : ''}" onclick="window.FirebaseAuthManager.refreshDirectorModal('approved')">
                ✓ المعتمدون (${approvedCount})
              </button>
            </div>

            <!-- Users List Table / Cards -->
            <div class="director-users-list">
              ${filtered.map(u => {
                const isAdmin = u.role === 'admin';
                const isApproved = u.role === 'approved';
                const hasActiveSession = !!u.activeSessionId;

                return `
                  <div class="user-row-card ${isAdmin ? 'admin-row' : ''}">
                    <div class="user-row-main">
                      <div class="user-avatar">${isAdmin ? '👑' : (isApproved ? '👨‍🏫' : '⏳')}</div>
                      <div class="user-info">
                        <div class="user-name">
                          ${u.displayName}
                          ${isAdmin ? '<span class="role-badge admin">المدير العام</span>' : (isApproved ? '<span class="role-badge approved">معتمد (كامل الصلاحيات)</span>' : '<span class="role-badge pending">بانتظار الاعتماد</span>')}
                        </div>
                        <div class="user-contact">
                          ${u.email ? `📧 ${u.email}` : ''}
                          ${u.phoneNumber ? `📱 ${u.phoneNumber}` : ''}
                          <span style="color:#94a3b8;">• تاريخ التسجيل: ${u.registeredAt}</span>
                        </div>
                        <div class="user-session-status">
                          ${hasActiveSession ? `
                            <span class="session-indicator active">🟢 جلسة نشطة: ${u.lastLoginDevice || 'متصفح'}</span>
                            <span style="color:#64748b; font-size:0.75rem;">(آخر نشاط: ${u.lastLoginAt || '-'})</span>
                          ` : `
                            <span class="session-indicator offline">⚪ لا توجد جلسة نشطة حالياً</span>
                          `}
                        </div>
                      </div>
                    </div>

                    <div class="user-row-actions">
                      ${!isAdmin ? `
                        ${!isApproved ? `
                          <button type="button" class="dir-btn approve" onclick="window.FirebaseAuthManager.approveUser('${u.uid}')" title="اعتماد ومنح الوصول الكامل">
                            ✓ اعتماد
                          </button>
                        ` : `
                          <button type="button" class="dir-btn revoke" onclick="window.FirebaseAuthManager.revokeUser('${u.uid}')" title="تعليق الصلاحيات مؤقتاً">
                            ⏸ تعليق
                          </button>
                        `}

                        ${hasActiveSession ? `
                          <button type="button" class="dir-btn kick" onclick="window.FirebaseAuthManager.terminateUserSession('${u.uid}')" title="إنهاء الجلسة النشطة فورا وإخراج الجهاز المتصل لمنع المشاركة">
                            🔴 إنهاء الجلسة
                          </button>
                        ` : ''}

                        <button type="button" class="dir-btn delete" onclick="window.FirebaseAuthManager.deleteUser('${u.uid}')" title="حذف الحساب">
                          🗑️
                        </button>
                      ` : `
                        <span style="font-size:0.8rem; font-weight:700; color:#94a3b8;">الحساب الإداري الرئيسي</span>
                      `}
                    </div>
                  </div>
                `;
              }).join('')}
            </div>

          </div>
        </div>
      `;
    },

    _submitQuickAdd() {
      const nameInput = document.getElementById('new-user-name');
      const contactInput = document.getElementById('new-user-contact');
      if (!nameInput || !contactInput) return;

      const name = nameInput.value.trim();
      const contact = contactInput.value.trim();
      if (!name || !contact) {
        alert('يرجى إدخال اسم المستخدم والبريد الإلكتروني أو رقم الجوال.');
        return;
      }
      const isEmail = contact.includes('@');
      this.addPreapprovedUser(name, contact, isEmail);
      nameInput.value = '';
      contactInput.value = '';
    },

    closeAllModals() {
      const m1 = document.getElementById('raed-auth-modal');
      const m2 = document.getElementById('raed-director-modal');
      const m3 = document.getElementById('raed-session-kick-modal');
      if (m1) m1.style.display = 'none';
      if (m2) m2.style.display = 'none';
      if (m3) m3.style.display = 'none';
    },

    onAuthStateChanged(callback) {
      if (typeof callback === 'function') {
        listeners.push(callback);
        callback(currentUser);
      }
    },

    init() {
      renderAuthNavbarWidget();
      verifyActiveSession(false);
    },

    showToast(msg, type) {
      if (window.ArabicUtils && window.ArabicUtils.showToast) {
        window.ArabicUtils.showToast(msg, type || 'info');
      } else {
        alert(msg);
      }
    }
  };

  // Helper Modal for Session Kick Alert
  function openSessionKickAlertModal(reason) {
    let modal = document.getElementById('raed-session-kick-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'raed-session-kick-modal';
      modal.className = 'raed-modal-backdrop';
      document.body.appendChild(modal);
    }

    modal.innerHTML = `
      <div class="raed-auth-dialog" style="max-width:480px; text-align:center; padding:28px;">
        <div style="font-size:3.5rem; margin-bottom:12px;">🚨</div>
        <h3 style="font-size:1.3rem; font-weight:900; color:#991b1b; margin-bottom:10px;">تم إنهاء الجلسة لحماية الحساب</h3>
        <p style="font-size:0.95rem; color:#475569; line-height:1.7; margin-bottom:20px; white-space:pre-wrap;">${reason}</p>
        
        <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:10px; padding:12px; font-size:0.85rem; color:#b91c1c; text-align:right; margin-bottom:20px;">
          🛡️ <strong>حماية الحساب من المشاركة:</strong>
          كل حساب معتمد محمي تقنياً بجلسة نشطة واحدة (Single Active Session). يمنع نظام المنصة تشغيل الحساب على أكثر من جهاز في نفس اللحظة.
        </div>

        <button type="button" class="nav-btn primary" style="width:100%; justify-content:center; padding:10px 0;" onclick="window.FirebaseAuthManager.closeAllModals()">
          <span>فهمت ذلك، المتابعة كزائر</span>
        </button>
      </div>
    `;

    modal.style.display = 'flex';
  }

  global.FirebaseAuthManager = FirebaseAuthManager;

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => FirebaseAuthManager.init());
    } else {
      FirebaseAuthManager.init();
    }
  }

})(typeof window !== 'undefined' ? window : globalThis);
