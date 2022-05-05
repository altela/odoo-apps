# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inventory : Track Changes of Field Value',
    'author': 'Altela Eleviansyah Pramardhika',
    'version': '12.0.1.0.0',
    'summary': 'Tracking Changes of Odoo Inventory Fields into Chatter or Logs',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Tracking Changes of Odoo Fields into Chatter or Logs""",
    'category': 'Extra Tools',
    'website': 'https://altela.my.id',
    'depends': [
        'stock',
    ],
    # 'data': [
    #     'views/stock_adjustment_rename.xml'
    # ],
    # 'images': [
    #     'static/description/banner.jpg',
    # ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': 'pre_init_check',
}
