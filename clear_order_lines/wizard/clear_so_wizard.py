from odoo import api, models, fields

class ClearSoWizard(models.TransientModel):
    _name = "clear.order.lines.so"
    _description = "Clear Order Lines Button"

    order_line = fields.One2many('sale.order.line', 'order_id')

    def clear_order_lines(self):
        # records = self.env['sale.order'].browse(self._context.get('active_ids', []))
        for record in self.purchase_order_lines:
            record.order_line = [(5, 0, 0)]

        msg_body = 'Has cleared order lines'
        self.message_post(body=msg_body, message_type='notification')