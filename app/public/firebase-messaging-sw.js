importScripts('https://www.gstatic.com/firebasejs/8.2.5/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.2.5/firebase-messaging.js');

firebase.initializeApp({
    apiKey: "AIzaSyDqDesb79-FWz7mMJnz07stjiC-3WiMiYE",
    authDomain: "pushleopard.firebaseapp.com",
    projectId: "pushleopard",
    storageBucket: "pushleopard.appspot.com",
    messagingSenderId: "1006554054487",
    appId: "1:1006554054487:web:262ed1a4313f895f7d0812",
    measurementId: "G-17NKGTNE86"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.

const messaging = firebase.messaging();   
messaging.setBackgroundMessageHandler(function(payload) {
    const promiseChain = clients
      .matchAll({
        type: "window",
        includeUncontrolled: true
      })
      .then(windowClients => {
        for (let i = 0; i < windowClients.length; i++) {
          const windowClient = windowClients[i];
          windowClient.postMessage(payload);
        }
      })
      .then(() => {
        return registration.showNotification("my notification title");
      });
    return promiseChain;
  });
  
  self.addEventListener('notificationclick', function(event) {
    // do what you want
    // ...
  });