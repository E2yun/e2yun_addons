# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AgreementClausePad(models.Model):

    _name = 'agreement.clause'
    _inherit = ['pad.common', 'agreement.clause', 'mail.thread', 'mail.activity.mixin']

    clause_pad_url = fields.Char('Clause Pad Url', pad_content_field='content')

