# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Barcode Inside Purchase',
    'author': 'Altela Software',
    'version': '14.0.1.0.0',
    'summary': 'Added barcode column inside purchase order',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Create history into chatter after editing inventory""",
    'category': 'Extra Tools',
    'website': 'https://www.altelasoftware.com',
    'depends': [
        'purchase',
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
