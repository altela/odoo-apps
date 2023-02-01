from odoo import api, models, fields

class ClearPoWizard(models.TransientModel):
    _name = "clear.order.lines.po"
    _description = "Clear Order Lines Button"

    order_line = fields.One2many('purchase.order.line','product_id')
    name = fields.Text(required=False)
    product_qty = fields.Text(required=False)
    date_planned = fields.Datetime(required=False)
    product_uom = fields.Many2one(required=False)
    product_id = fields.Many2one(required=False)
    price_unit = fields.Float(required=False)
    order_id = fields.Many2one(required=False)

    def clear_order_lines_po(self):
        # records = self.env['purchase.order'].browse(self._context.get('active_ids', []))
        for record in self.purchase_order_lines:
            record.order_line = [(5, 0, 0)]

        msg_body = 'Has cleared order lines'
        self.message_post(body=msg_body, message_type='notification')