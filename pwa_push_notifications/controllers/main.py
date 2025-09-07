from odoo import http
from odoo.http import request

class PwaPushController(http.Controller):

    @http.route('/pwa_push/config', type='json', auth='user')
    def get_config(self):
        """Return Firebase web config to the frontend"""
        params = request.env['ir.config_parameter'].sudo()
        return {
            'apiKey': params.get_param('pwa_push.apiKey'),
            'authDomain': params.get_param('pwa_push.authDomain'),
            'projectId': params.get_param('pwa_push.projectId'),
            'storageBucket': params.get_param('pwa_push.storageBucket'),
            'messagingSenderId': params.get_param('pwa_push.messagingSenderId'),
            'appId': params.get_param('pwa_push.appId'),
            'vapidKey': params.get_param('pwa_push.vapidKey'),
        }

    @http.route('/pwa_push/save_token', type='json', auth='user')
    def save_token(self, token):
        """Save the FCM token for the current user"""
        user = request.env.user
        Device = request.env['fcm.device'].sudo()
        if token:
            existing = Device.search([('token', '=', token)])
            if not existing:
                Device.create({'user_id': user.id, 'token': token})
        return {'status': 'ok'}

    @http.route('/firebase-messaging-sw.js', type='http', auth='public')
    def service_worker(self):
        """Serve Firebase service worker file"""
        content = """
importScripts('https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js');

self.addEventListener('install', function(event) {
    console.log('Firebase SW installed');
});

self.addEventListener('activate', function(event) {
    console.log('Firebase SW activated');
});

firebase.initializeApp(%s);

const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    const notificationTitle = payload.notification.title;
    const notificationOptions = {
        body: payload.notification.body,
        icon: '/web/static/img/favicon.ico'
    };
    self.registration.showNotification(notificationTitle, notificationOptions);
});
""" % request.env['ir.config_parameter'].sudo().get_param('pwa_push.firebase_web_config', '{}')
        return request.make_response(content, [('Content-Type', 'application/javascript')])