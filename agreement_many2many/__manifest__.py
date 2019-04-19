# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Agreement Many2Many',
    'version': '0.1',
    'category': 'Partner',
    'description': """
This module changed relation with objects from One2many to Many2many
====================================================================

in agrrement can select or create recital,section,clause,

""",
    'website': 'https://www.odoo.com/page/notes',
    'summary': 'Sticky memos, Collaborative',
    'depends': [
        'agreement',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
