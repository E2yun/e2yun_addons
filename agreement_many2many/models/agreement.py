# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Agreement(models.Model):


    _inherit = ['agreement']

    recital_ids = fields.Many2many(
        comodel_name='agreement.recital', relation='new_agreement_recital_rel',
        string="Recitals", copy=True)

    sections_ids = fields.Many2many(
        comodel_name='agreement.section', relation='new_agreement_sections_rel',
        string="Sections", copy=True)

    clauses_ids = fields.Many2many(
        comodel_name='agreement.clause', relation='new_agreement_clauses_rel',
        string="Clauses", copy=True)

    appendix_ids = fields.Many2many(
        comodel_name='agreement.appendix', relation='new_agreement_cappendix_rel',
        string="Appendices", copy=True)

