# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class res_company(models.Model):
    _inherit = 'res.company'

    preparation_time_variable = fields.Integer(
        string='Preparation time variable',
        default=0
    )
    preparation_time_fixed = fields.Integer(
        string='Preparation time fixed',
        default=0
    )
