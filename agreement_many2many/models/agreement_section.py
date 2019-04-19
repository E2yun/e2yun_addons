# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AgreementSectionPad(models.Model):


    _inherit = ['agreement.section']

    clauses_ids = fields.Many2many(
        comodel_name='agreement.clause', relation='new_section_clauses_rel',
        string="Clauses", copy=True)

