import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CarRental(models.Model):
    """
        Model for managing car rental records.

        Stores information about rental periods, customer,
        selected car, locations, and rental status.
        """
    _name = 'car.rental'
    _description = 'Car Rental'

    # customer_id = fields.Many2one('res.partner', required=True)
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        default=lambda self: self.env.user.partner_id
    )
    car_id = fields.Many2one('product.template', required=True)
    rent_price = fields.Float(
        related='car_id.rent_price',
        string="Rent Price",
        store=True
    )

    pickup_location_id = fields.Many2one('rental.location')
    return_location_id = fields.Many2one('rental.location')

    date_start = fields.Datetime()
    date_end = fields.Datetime()

    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done')
    ], default='draft')
