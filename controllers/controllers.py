# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
from odoo.http import json


class InvoiceInfoApi(http.Controller):
    @http.route('/invoice-info-api/', methods=['GET'], type='http', csrf=False, auth="public")
    def index(self, **kw):
        invoice = http.request.env['account.move'].search([('name', '=', 'INV/2021/10/0004')])
        # return str(invoice['amount_total'])
        return Response(json.dumps({"name": invoice['name'],
                                    "amount_total": str(invoice['amount_total']),
                                    "invoice_date": str(invoice['invoice_date']),
                                    "invoice_date_due": str(invoice['invoice_date_due']),
                                    "invoice_partner_display_name": invoice['invoice_partner_display_name'],
                                    "create_date": str(invoice['create_date']),
                                    }),
                        content_type='application/json;charset=utf-8', status=200)

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
