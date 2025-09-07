from odoo import models, fields

class FCMDevice(models.Model):
    _name = 'fcm.device'
    _description = 'Firebase Device Token'

    user_id = fields.Many2one('res.users', string="User", required=True, ondelete="cascade")
    token = fields.Char('FCM Token', required=True, index=True, unique=True)