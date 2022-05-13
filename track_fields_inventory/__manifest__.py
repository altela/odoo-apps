# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Edit History of Inventory',
    'author': 'Altela Eleviansyah Pramardhika',
    'version': '12.0.1.0.0',
    'summary': 'Create history into chatter after editing inventory',
    'license': 'LGPL-3',
    'sequence': 1,
    'description': """Create history into chatter after editing inventory""",
    'category': 'Extra Tools',
    'website': 'https://altela.my.id',
    'depends': [
        'stock',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': 'pre_init_check',
}
