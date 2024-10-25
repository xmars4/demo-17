# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    group_id = fields.Many2one('res.partner.group', string='Customer Group')
