# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AgreementSectionPad(models.Model):

    _name = 'agreement.section'
    _inherit = ['pad.common', 'agreement.section','mail.thread', 'mail.activity.mixin']

    section_pad_url = fields.Char('Section Pad Url', pad_content_field='content')

