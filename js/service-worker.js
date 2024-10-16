const CACHE_NAME = 'riu-palace-cache-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/css/style.css',
    '/images/riu192x192.png',
    '/images/riu512x512.png',
    '/js/custom.js'
    // Incluye aquí otros recursos que desees cachear
];

// Instalación del Service Worker
self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

// Activación del Service Worker
self.addEventListener('activate', function(event) {
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

// Intercepta peticiones y responde desde la caché si es posible
self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});
