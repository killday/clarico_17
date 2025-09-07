odoo.define('pwa_push_notifications.push_client', function (require) {
    "use strict";

    const ajax = require('web.ajax');

    async function initPush() {
        if (!("Notification" in window) || !("serviceWorker" in navigator)) {
            console.log("Push notifications not supported");
            return;
        }

        const perm = await Notification.requestPermission();
        if (perm !== 'granted') {
            console.log("Notification permission denied");
            return;
        }

        const config = await ajax.jsonRpc('/pwa_push/config', 'call', {});
        if (!config.apiKey) {
            console.error("No Firebase config set");
            return;
        }

        if (!firebase.apps.length) {
            firebase.initializeApp(config);
        }
        const messaging = firebase.messaging();

        navigator.serviceWorker.register('/firebase-messaging-sw.js').then(async (reg) => {
            messaging.useServiceWorker(reg);

            try {
                const token = await messaging.getToken({ vapidKey: config.vapidKey });
                if (token) {
                    await ajax.jsonRpc('/pwa_push/save_token', 'call', { token });
                    console.log("Token saved:", token);
                }
            } catch (err) {
                console.error("Error getting token:", err);
            }
        });
    }

    // Add floating button on frontend
    window.addEventListener('load', () => {
        const btn = document.createElement('button');
        btn.innerText = "Enable Notifications";
        btn.style.position = 'fixed';
        btn.style.bottom = '20px';
        btn.style.right = '20px';
        btn.style.zIndex = 9999;
        btn.style.padding = '10px 15px';
        btn.style.background = '#007bff';
        btn.style.color = '#fff';
        btn.style.border = 'none';
        btn.style.borderRadius = '5px';
        btn.onclick = initPush;
        document.body.appendChild(btn);
    });
});