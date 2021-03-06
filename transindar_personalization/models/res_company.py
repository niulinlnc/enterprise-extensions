##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class ResCompany(models.Model):

    _inherit = 'res.company'

    preparation_time_variable = fields.Integer(
        default=0,
    )

    preparation_time_fixed = fields.Integer(
        default=0,
    )
