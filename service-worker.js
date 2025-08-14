const CACHE_NAME = 'ficha-treino-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/favicon.ico',
  '/logo.jpeg',
  '/icon-192x192.png',
  '/icon-512x512.png',
  'https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.72/pdfmake.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.72/vfs_fonts.js'
];

// Instalar o service worker e fazer cache dos recursos
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Cache aberto');
        return cache.addAll(urlsToCache);
      })
  );
});

// Interceptar requisições e servir do cache quando possível
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - retorna a resposta do cache
        if (response) {
          return response;
        }

        return fetch(event.request).then(
          function(response) {
            // Verifica se recebemos uma resposta válida
            if(!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }

            // IMPORTANTE: Clone a resposta. Uma resposta é um stream
            // e porque queremos que o navegador consuma a resposta
            // assim como o cache consumindo a resposta, precisamos
            // cloná-la para que tenhamos dois streams.
            var responseToCache = response.clone();

            caches.open(CACHE_NAME)
              .then(function(cache) {
                cache.put(event.request, responseToCache);
              });

            return response;
          }
        );
      })
    );
});

// Atualizar o service worker
self.addEventListener('activate', function(event) {
  var cacheWhitelist = [CACHE_NAME];

  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Lidar com mensagens do cliente
self.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Notificação de instalação bem-sucedida
self.addEventListener('install', function(event) {
  console.log('Service Worker instalado com sucesso');
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  console.log('Service Worker ativado com sucesso');
  event.waitUntil(self.clients.claim());
});

