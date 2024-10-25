# -*- coding: utf-8 -*-
{
    'name': "sale-customize",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_stock', 'sale_management', 'website_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/product_pricelist_data.xml',
        'data/res_partner_group_data.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_group_views.xml',
        'views/product_pricelist.xml',
        'views/delivery_carrier_views.xml',
        'views/delivery_templates.xml',
    ],
}
