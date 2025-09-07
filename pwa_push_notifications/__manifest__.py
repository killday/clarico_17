{
    'name': 'PWA Push Notifications (FCM)',
    'version': '16.0.1.0.0',
    'summary': 'Forward Odoo notifications to Firebase Push (PWA)',
    'description': """
This module integrates Odoo notifications with Firebase Cloud Messaging (FCM)
to allow Progressive Web Apps (PWAs) on Android to receive push notifications.
""",
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'category': 'Tools',
    'depends': ['base', 'bus', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'pwa_push_notifications/static/src/js/push_client.js',
        ],
    },
    'installable': True,
    'application': False,
}