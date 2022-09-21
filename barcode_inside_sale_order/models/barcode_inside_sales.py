from odoo import models, fields, api


class BarcodeInsidePurchase(models.Model):
    _inherit = 'sale.order.line'

    barcode = fields.Char('barcode', related='product_id.barcode')