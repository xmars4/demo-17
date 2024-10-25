# -*- coding:utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    group_id = fields.Many2one('res.partner.group', string='Customer Group')
    is_customizable_discount = fields.Boolean(string='Is Customizable', related='group_id.is_customizable', store=True)
    customize_discount = fields.Float(string='Customize Discount')
