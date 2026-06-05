import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """
        Extension of res.partner model for car rental module.

        Adds a flag to identify customers who use car rental services.
        """
    _inherit = 'res.partner'

    is_car_customer = fields.Boolean(string='Is Car Customer')

