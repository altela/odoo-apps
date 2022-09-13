from odoo import api, models, fields

class ClearPoWizard(models.TransientModel):
    _name = "clear.order.lines.po"

    def clear_order_lines_po(self):
        records = self.env['purchase.order'].browse(self._context.get('active_ids', []))
        for record in records:
            record.order_line = [(5, 0, 0)]

        msg_body = 'Has cleared order lines'
        records.message_post(body=msg_body, message_type='notification', subtype='mail.mt_comment')