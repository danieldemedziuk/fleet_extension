# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import logging

_logger = logging.getLogger(__name__)


class FleetExtensionModel(models.Model):
    _inherit = 'fleet.vehicle'

    leasing_company = fields.Many2one('res.partner', string="Leasing company")
    leasing_date = fields.Date(string='Leasing expiration date')
    insurance_company = fields.Char(string='Insurance company', compute='set_default_contracts', readonly=True)
    insurance_date = fields.Date(string='End date of insurance', compute='set_default_contracts', readonly=True)
    insurance_number = fields.Char(string='Insurance policy number')
    wheel_size = fields.Char(string='Wheel size')
    fire_extinguisher_date = fields.Date(string='Expiration date of fire extinguisher', help='Does it exist in the car.')
    technical_review = fields.Date(string='Date of technical inspection')
    spare_wheel = fields.Boolean(string='Spare wheel', help='Does it exist in the car.')
    pin_card = fields.Integer(string='Card PIN', help="This is the pin code for the company's fleet card.")
    pressure_sensor = fields.Boolean(string='Pressure sensor', help='Does it exist in the car.')
    vignette = fields.Char(string='Vignette')
    vignette_date = fields.Date(string='Expiration date of the vignette')

    def set_default_contracts(self):
        companies = ['Insurance', 'Leasing', 'PKN Orlen', 'BP P.L.C.', 'Royal Dutch Shell', 'Total SE', 'Eni S.p.A.', 'Esso', 'Aral AG', 'LUKOIL']

        for item in companies:
            if not self.env['fleet.service.type'].search([('category', '=', 'contract'), ('name', '=', item)]):
                self.env['fleet.service.type'].create({
                    'name': item,
                    'category': 'contract'
                })

        for rec in self:
            veh_insurer = self.env['fleet.vehicle.log.contract'].search([('active', '=', True), ('cost_subtype_id', '=', 'Ubezpieczenie'), ('state', '=', 'open'), ('vehicle_id', '=', rec.name)])
            veh_leasing = self.env['fleet.vehicle.log.contract'].search([('active', '=', True), ('cost_subtype_id', '=', 'Leasing'), ('state', '=', 'open'), ('vehicle_id', '=', rec.name)])

            if len(veh_insurer) == 1:
                rec.insurance_date = veh_insurer['expiration_date']
                rec.insurance_company = veh_insurer['insurer_id']['name']

            if len(veh_leasing) == 1:
                rec.insurance_date = veh_leasing['expiration_date']
                rec.insurance_company = veh_leasing['insurer_id']['name']


class VehicleOdometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    driver = fields.Many2one('res.users', string='Driver', default=lambda self: self._uid, help='Driver of the vehicle', required=True)
    date_return = fields.Date(string='Date of return', help='Date of return and drop-off car')
    description = fields.Text(string='Description of the route', help='Description of the route traveled. Where stops were made. Where did you leave from and where did you get to.')
    destination = fields.Many2one('res.partner', string='Purpose of the trip', help='Enter the destination here. Name of customer, service, hotel, destination.', required=True)
    start_counter = fields.Float(string='Initial counter status', compute='set_counters', required=True)
    stop_counter = fields.Float(string='End counter status', required=True, store=True)
    num_km = fields.Float(string='Number of kilometers actually driven', compute='compute_km')

    def compute_km(self):
        for rec in self:
            if rec.start_counter and rec.stop_counter:
                rec.num_km = rec.stop_counter - rec.start_counter

            if rec.start_counter == 0.0:
                rec.num_km = rec.stop_counter

    def set_counters(self):
        for i, rec in enumerate(self):
            rec.stop_counter = rec.value

            if i+1 == len(self):
                break
            if self[i+1].stop_counter != 0.0:
                self[i].start_counter = self[i+1].stop_counter

