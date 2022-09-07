# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Clear Order Lines',
    'author': 'Altela Softwares',
    'version': '12.0.1.0.0',
    'summary': 'Clear Order Lines inside The Sales and Purchase Order',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Clear Order Lines inside The Sales and Purchase Order""",
    'category': 'Extra Tools',
    'website': 'https://www.altela.net',
    'depends': [
        'sale_management',
        'purchase',
        'stock',
    ],
    # 'images': [
    #     'static/description/assets/banner.gif',
    # ],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/clear_order_lines.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': 'pre_init_check',
}
