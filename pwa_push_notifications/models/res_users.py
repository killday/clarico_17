from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    device_ids = fields.One2many('fcm.device', 'user_id', string='FCM Devices')