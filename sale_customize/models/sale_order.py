# -*- coding:utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    shipping_type = fields.Selection([('freeship', 'Freeship'), ('pickup', 'Pickup')], string='Shipping Type', default='freeship')

    def action_open_discount_wizard(self):
        self.ensure_one()
        partner_group = self.partner_id.group_id
        if partner_group == self.env.ref('sale_customize.group_3'):
            discount = self.partner_id.customize_discount or partner_group.discount
        else:
            discount = partner_group.discount
        return {
            'name': ("Discount"),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.discount',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_discount_percentage': discount}
        }



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_id', 'product_uom', 'product_uom_qty', 'order_id.partner_id.group_id')
    def _compute_discount(self):
        super()._compute_discount()
        for rec in self:
            if rec.order_id.partner_id.group_id == self.env.ref('sale_customize.group_2') and rec.product_template_id.product_tag_ids.filtered(lambda t: t.name == 'Clearance'):
                rec.discount = 10
