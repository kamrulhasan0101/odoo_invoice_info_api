# -*- coding: utf-8 -*-
from odoo import http


class InvoiceInfoApi(http.Controller):
    @http.route('/invoice-info-api/', auth='public')
    def index(self, **kw):
        invoice = http.request.env['account.move'].search([('name', '=', 'INV/2021/10/0004')])
        return str(invoice['amount_total'])

    # @http.route('/invoice_info_api/invoice_info_api/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('invoice_info_api.listing', {
    #         'root': '/invoice_info_api/invoice_info_api',
    #         'objects': http.request.env['invoice_info_api.invoice_info_api'].search([]),
    #     })

    # @http.route('/invoice_info_api/invoice_info_api/objects/<model("invoice_info_api.invoice_info_api"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('invoice_info_api.object', {
    #         'object': obj
    #     })
