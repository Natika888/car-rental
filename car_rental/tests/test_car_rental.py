from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class TestCarRental(TransactionCase):

    def setUp(self):
        super().setUp()

        self.customer = self.env['res.partner'].create({
            'name': 'Test Customer'
        })

        self.location = self.env['rental.location'].create({
            'name': 'Test Location'
        })

        self.category = self.env['car.category'].create({
            'name': 'Test Category'
        })

        self.car = self.env['product.template'].create({
            'name': 'Test Car',
            'is_car': True,
            'status': 'available'
        })

    # car.category
    def test_create_category(self):
        category = self.env['car.category'].create({
            'name': 'SUV'
        })
        self.assertTrue(category.id)

    # rental.location
    def test_create_location(self):
        location = self.env['rental.location'].create({
            'name': 'Kyiv'
        })
        self.assertTrue(location.id)

    # product.template (car)
    def test_create_car(self):
        car = self.env['product.template'].create({
            'name': 'BMW',
            'is_car': True,
            'status': 'available'
        })
        self.assertEqual(car.status, 'available')

    # car.rental
    def test_create_rental(self):
        rental = self.env['car.rental'].create({
            'customer_id': self.customer.id,
            'car_id': self.car.id,
            'pickup_location_id': self.location.id,
            'return_location_id': self.location.id,
            'state': 'draft'
        })
        self.assertEqual(rental.state, 'draft')

    # wizard
    def test_wizard_change_state(self):
        rental = self.env['car.rental'].create({
            'customer_id': self.customer.id,
            'car_id': self.car.id,
            'pickup_location_id': self.location.id,
            'return_location_id': self.location.id,
            'state': 'draft'
        })

        wizard = self.env['car.rental.status.wizard'].create({
            'state': 'done'
        })

        wizard = wizard.with_context(active_ids=rental.ids)
        wizard.action_apply()

        self.assertEqual(rental.state, 'done')