import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CarCategory(models.Model):
    """
        Model representing car categories.

        Used to classify cars into groups
        """
    _name = 'car.category'
    _description = 'Car Category'

    name = fields.Char(required=True)
    description = fields.Text()