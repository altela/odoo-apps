from odoo import models, fields, api


class TrackFieldsInventory(models.Model):
    _inherit = "product.template"

    name = fields.Char(string='Product Name', track_visibility='always')
