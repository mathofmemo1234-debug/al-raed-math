/**
 * ==========================================================================
 * منصة الرائد التعليمية الذكية للرياضيات | أ. محمد عبدالله جمعة
 * Service Worker (Offline First Caching & PWA Support)
 * ==========================================================================
 */

const CACHE_NAME = 'alraed-platform-v1';
const CORE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './assets/css/platform.css',
  './assets/js/arabic_utils.js',
  './assets/js/platform.js',
  './assets/js/lesson_prep_manager.js',
  './assets/js/question_bank.js',
  './assets/js/exam_builder.js',
  './assets/js/exam_exporter.js',
  './assets/js/curriculum_tree.js',
  './assets/vendor/katex/katex.min.css',
  './assets/vendor/katex/katex.min.js',
  './assets/vendor/katex/auto-render.min.js',
  './assets/img/my_logo.png',
  './assets/img/icon-192.png',
  './assets/img/icon-512.png',
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
  // Pass through non-GET and external API / Firebase requests
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin && !url.hostname.includes('fonts.googleapis.com') && !url.hostname.includes('fonts.gstatic.com')) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        // Stale-while-revalidate in background
        fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, networkResponse));
          }
        }).catch(() => {});
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      }).catch(() => {
        if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
