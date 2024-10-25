# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    group_id = fields.Many2one('res.partner.group', string='Customer Group')
    base_product_pricelist_id = fields.Many2one('product.pricelist', string='Base Pricelist')
    child_pricelist_ids = fields.One2many('product.pricelist', 'base_product_pricelist_id', string='Child Pricelists')

