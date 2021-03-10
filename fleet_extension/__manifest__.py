# -*- coding: utf-8 -*-
{
    'name': 'Fleet extension',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'sequence': 110,
    'summary': 'Fleet, Insurance, Leasing, Odometer, Equipment',
    'description': """
Fleet Module Extension
==================================
This addition to the Fleet module extends the basic module with additional data such as:
- date of registration inspection
- car equipment
- tire type
- vignette
- insurance
and others.

Additionally, it creates potential contracts with selected brands in order to facilitate work organization.

The odometer system was extended by additional fields. The purpose of this extension is to more precisely determine kilometers driven on a given trip, day or month.

Updates to the module's current status are planned. In the future the module is to provide more beneficial services to the user.

""",
    'website': 'website',
    'category': 'Tool',
    'depends': ['base', 'mail', 'fleet'],
    'data': [
        'views/fleet_extension_view.xml',
        'views/vehicle_odometer_view.xml',
        ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
