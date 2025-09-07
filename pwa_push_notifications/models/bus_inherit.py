from odoo import models
import json
import logging

_logger = logging.getLogger(__name__)

try:
    import firebase_admin
    from firebase_admin import credentials, messaging
except ImportError:
    firebase_admin = None

class BusPushIntegration(models.Model):
    _inherit = 'bus.bus'

    def _sendone(self, user_id, channel, message):
        res = super()._sendone(user_id, channel, message)

        if not firebase_admin:
            return res

        user = self.env['res.users'].browse(user_id)
        tokens = user.device_ids.mapped('token')
        if not tokens:
            return res

        try:
            cred_path = self.env['ir.config_parameter'].sudo().get_param('pwa_push.service_account_path')
            if cred_path and not firebase_admin._apps:
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)

            body = message if isinstance(message, str) else json.dumps(message)
            notif = messaging.MulticastMessage(
                notification=messaging.Notification(
                    title="Odoo Notification",
                    body=body[:150]
                ),
                tokens=tokens
            )
            response = messaging.send_multicast(notif)
            _logger.info("Sent push to %s tokens, success=%s", len(tokens), response.success_count)
        except Exception as e:
            _logger.error("Push error: %s", e)

        return res