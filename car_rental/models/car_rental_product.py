import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    """
       Extension of product.template for car rental functionality.

       Adds fields specific to cars such as:
       - rental price
       - license plate
       - current location
       - availability status
       """
    _inherit = 'product.template'

    is_car = fields.Boolean()
    category_id = fields.Many2one('car.category')

    rent_price = fields.Float(string="Rent Price", help="Price for renting car")

    license_plate = fields.Char()
    location_id = fields.Many2one('rental.location')
    status = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('service', 'In Service')
    ], default='available')
