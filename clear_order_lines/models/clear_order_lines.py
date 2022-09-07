from odoo import fields, models


class ClearOrderLines(models.Model):
    _inherit = 'sale.order'

    def clear_order_lines(self):
        order_line = fields.One2many('sale.order.line', 'product_id')
        self.order_line = [(5, 0, 0)]


