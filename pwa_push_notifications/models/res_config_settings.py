from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    apiKey = fields.Char("Firebase API Key", config_parameter='pwa_push.apiKey')
    authDomain = fields.Char("Firebase Auth Domain", config_parameter='pwa_push.authDomain')
    projectId = fields.Char("Firebase Project ID", config_parameter='pwa_push.projectId')
    storageBucket = fields.Char("Firebase Storage Bucket", config_parameter='pwa_push.storageBucket')
    messagingSenderId = fields.Char("Firebase Messaging Sender ID", config_parameter='pwa_push.messagingSenderId')
    appId = fields.Char("Firebase App ID", config_parameter='pwa_push.appId')
    vapidKey = fields.Char("Web Push VAPID Key", config_parameter='pwa_push.vapidKey')
    service_account_path = fields.Char("Service Account JSON Path", config_parameter='pwa_push.service_account_path')