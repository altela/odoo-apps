from odoo import models, fields, api


class TrackFieldsInventory(models.Model):
    _inherit = "product.template"

    name = fields.Char(string='Product Name', track_visibility='always')
    sale_ok = fields.Boolean(string='Can be Sold', track_visibility='always')
    purchase_ok = fields.Boolean(string='Can be Purchased', track_visibility='always')
    barcode = fields.Char(string='Barcode', track_visibility='always')

