from odoo import models, fields, api


class TrackFieldsInventory(models.Model):
    _inherit = "product.template"

    name = fields.Char(string='Product Name', track_visibility='always')
    sale_ok = fields.Boolean(string='Can be Sold', track_visibility='always')
    purchase_ok = fields.Boolean(string='Can be Purchased', track_visibility='always')

    # General Information
    type = fields.Selection(string='Product Type', track_visibility='always')
    categ_id = fields.Many2one(string='Product Category', track_visibility='always')
    default_code = fields.Char(string='Internal Reference', track_visibility='always')
    barcode = fields.Char(string='Barcode', track_visibility='always')
    list_price = fields.Float(string='Sales Price', track_visibility='always')
    standard_price = fields.Float(string='Cost', track_visibility='always')
    uom_id = fields.Many2one(string='Unit of Measure', track_visibility='always')
    uom_po_id = fields.Many2one(string='Unit of Measure', track_visibility='always')
    description = fields.Text(string='Description', track_visibility='always')




