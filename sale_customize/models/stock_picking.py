# -*- coding:utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        for rec in self:
            customer = rec.sale_id.partner_id
            email_customer = customer.email
            if rec.location_id.usage == 'internal':
                if rec.state == 'done':
                    mail_values = {
                        'subject': 'Thông báo quan trọng',
                        'body_html': '<p>Xin chào! This is your picking</p>',
                        'email_to': email_customer if email_customer else None,  # Địa chỉ người nhận
                        'email_from': 'email@example.com',  # Địa chỉ người gửi
                    }
                    # Tạo và gửi email
                    mail = self.env['mail.mail'].create(mail_values)
                    mail.send()
        return res

