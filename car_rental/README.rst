# Car Rental Module

## Overview

This module provides a simple car rental management system in Odoo.

## Features

* Manage car categories
* Manage rental locations
* Manage cars (based on products)
* Create and manage rentals
* Track rental status
* Restrict access: users see only their own rentals
* Wizard for mass changing status
* PDF report for rentals
* Demo data included
* Unit tests implemented

## Models

* car.category
* rental.location
* car.rental
* res.partner (extended)
* product.template (extended)

## Security

* Two user roles: User and Admin
* Record rules restrict access to own rentals

## Usage

1. Create a rental
2. System automatically assigns current user as customer
3. Track rental status in Kanban view

## Author

Natika888
