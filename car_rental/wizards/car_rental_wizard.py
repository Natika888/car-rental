import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class CarRentalStatusWizard(models.TransientModel):
    """
        Wizard for changing the status of multiple car rentals.

        Allows the user to select a new status and apply it
        to selected rental records.
        """
    _name = 'car.rental.status.wizard'
    _description = 'Change Rental Status Wizard'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done')
    ], required=True)

    def action_apply(self):
        """
                Apply selected status to active rental records.

                Retrieves selected records from context (active_ids)
                and updates their state.
                """
        rentals = self.env['car.rental'].browse(self.env.context.get('active_ids'))
        rentals.write({'state': self.state})