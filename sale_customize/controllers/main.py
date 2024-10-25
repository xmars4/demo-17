# -*- coding:utf-8 -*-

from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request, route


class InheritWebsitesale(WebsiteSale):
    def _get_shop_payment_values(self, order, **kwargs):
        values = super()._get_shop_payment_values(order, **kwargs)
        main_warehouse = request.env.ref('stock.warehouse0')
        stores = (request.env['stock.warehouse'].sudo().search([('company_id', '=', values['order'].company_id.id)])
                  .filtered(lambda x: x != main_warehouse)
                  .mapped(lambda x: {'store_id': x.id, 'store_name': x.name}))
        values['stores'] = stores
        return values
