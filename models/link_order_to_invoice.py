# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class sale_order_account_invoice_link(models.Model): 
    _inherit = "account.invoice"
    
    order_id = fields.Many2one('sale.order', string='Orderigerniger', store=True, readonly=True)
    confirmation_date = fields.Datetime(string='Confirmation Date', related='order_id.confirmation_date', store=True)


    