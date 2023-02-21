from odoo import models


class ClearSoWizard(models.TransientModel):
    _name = "clear.order.lines.so"

    def clear_order_lines_so(self):
        records = self.env['sale.order'].browse(self._context.get('active_ids', []))
        for record in records.order_line:
            record.unlink()

        msg_body = 'Has cleared order lines'
        records.message_post(body=msg_body, message_type='notification')