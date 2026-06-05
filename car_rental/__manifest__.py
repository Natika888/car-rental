{
    'name': 'Car Rental',
    'version': '19.0.1.0.0',
    'summary': 'Car Rental Management System',
    'description': 'Module for managing car rentals, locations and vehicles',

    'author': 'Natika',
    'category': 'Services',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'product',
    ],

    'data': [
        # security
        'security/car_rental_groups.xml',
        'security/ir.model.access.csv',
        'security/car_rental_rules.xml',

        # views

        'views/car_category_views.xml',
        'views/rental_location_views.xml',
        'views/product_views.xml',
        'views/car_rental_views.xml',

        'views/menu.xml',

        'wizards/car_rental_wizard_views.xml',

        'data/car_data.xml',

        'report/car_rental_report.xml',
        'report/car_rental_report_action.xml',
    ],

    'demo': [
        'demo/car_demo.xml',
    ],

    'installable': True,
    'application': True,

    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
}
