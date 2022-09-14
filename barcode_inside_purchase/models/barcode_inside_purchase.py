from odoo import models, fields, api


class BarcodeInsidePurchase(models.Model):
    _inherit = 'purchase.order.line'

    # product_id = fields.Many2one('product.template', 'product_id')
    barcode = fields.Text(string='Barcode')

    # barcode = fields.Many2one('product.template', 'barcode')
    @api.onchange('product_id')
    def pull_barcode(self):
        self.barcode = self.product_id.barcode
