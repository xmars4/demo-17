# -*- coding:utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _name = 'res.partner.group'

    name = fields.Char(string='Name', required=True)
    discount = fields.Float(string='Discount', required=True)
    is_customizable = fields.Boolean(string='Is Customizable', default=False)