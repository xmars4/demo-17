# -*- coding:utf-8 -*-

from odoo import models, fields, api


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    is_pickup_store = fields.Boolean(string='Is Pickup at Store')