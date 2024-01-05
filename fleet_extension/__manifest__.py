# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    # App information

    'name': 'Fleet extension',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'summary': 'Fleet, Insurance, Leasing, Odometer, Equipment',
    'license': 'OPL-1',
    'price':   9,
    'currency':   'EUR',
    'description': """
Fleet Module Extension
==================================
This addition to the Fleet module extends the basic module with additional data such as:

Main Features
-------------
* date of registration inspection
* car equipment
* tire type
* vignette
* insurance
and others.

Depends
---------
* fleet

Additionally, it creates potential contracts with selected brands in order to facilitate work organization.
The odometer system was extended by additional fields. The purpose of this extension is to more precisely determine kilometers driven on a given trip, day or month.
Updates to the module's current status are planned. In the future the module is to provide more beneficial services to the user.

""",
    'category': 'Fleet, Tool',
    'depends': ['base', 'mail', 'fleet'],
    'data': [
        'views/fleet_extension_view.xml',
        'views/vehicle_odometer_view.xml',
        ],
    'images': ['static/description/f_extension.jpg'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
