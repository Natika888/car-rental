import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class RentalLocation(models.Model):
    """
        Model representing rental locations.

        Stores information about pickup and return points,
        including name and address.
        """
    _name = 'rental.location'
    _description = 'Rental Location'

    name = fields.Char(required=True)
    address = fields.Char(string="Address")