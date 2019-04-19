# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AgreementRecitalPad(models.Model):

    _name = 'agreement.recital'
    _inherit = ['pad.common', 'agreement.recital', 'mail.thread', 'mail.activity.mixin']

    recital_pad_url = fields.Char('Recital Pad Url', pad_content_field='content')

