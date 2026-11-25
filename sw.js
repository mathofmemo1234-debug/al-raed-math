/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * Service Worker (Network-First Freshness + Offline PWA Fallback)
 * ==========================================================================
 */

const CACHE_NAME = 'alraed-platform-v3';
const CORE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './assets/css/platform.css',
  './assets/js/arabic_utils.js',
  './assets/js/pwa_manager.js',
  './assets/js/platform.js',
  './assets/js/lesson_prep_manager.js',
  './assets/js/question_bank.js',
  './assets/js/exam_builder.js',
  './assets/js/exam_exporter.js',
  './assets/vendor/katex/katex.min.css',
  './assets/vendor/katex/katex.min.js',
  './assets/vendor/katex/auto-render.min.js',
  './assets/img/my_logo.png',
  './assets/img/icon-192.png',
  './assets/img/icon-512.png',
  './assets/img/platform_qr.png',
  './assets/img/moe_logo.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(CORE_ASSETS).catch((err) => {
        console.warn('PWA Pre-cache skipped some optional assets:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) {
    return;
  }

  // Network-First strategy: ensures users ALWAYS get latest updates immediately,
  // with seamless offline cache fallback when disconnected.
  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
        }
        return networkResponse;
      })
      .catch(() => {
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
            return caches.match('./index.html');
          }
        });
      })
  );
});
