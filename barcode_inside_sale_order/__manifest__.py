# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Barcode Inside Sales Order',
    'author': 'Altela Softwares',
    'version': '15.0.1.0.0',
    'summary': 'Added barcode column inside sales order',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Added barcode column inside sales order""",
    'category': 'Extra Tools',
    'website': 'https://www.altela.net',
    'depends': [
        'sale_management',
    ],
    'images': [
        'static/description/assets/banner.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/barcode_inside_purchase.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': 'pre_init_check',
}
