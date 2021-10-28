# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
from odoo.http import json
from odoo.http import request


class InvoiceInfoApi(http.Controller):
    @http.route('/invoice-info-api/', methods=['GET'], type='http', csrf=False, auth="public")
    def index(self, invoice_no):
        invoice = http.request.env['account.move'].search([('name', '=', invoice_no)])
        if invoice:
            data = {"status": True,
                    "name": invoice['name'],
                    "amount_total": str(invoice['amount_total']),
                    "payment_state": invoice['payment_state'],
                    "invoice_date": str(invoice['invoice_date']),
                    "invoice_date_due": str(invoice['invoice_date_due']),
                    "invoice_partner_display_name": invoice['invoice_partner_display_name'],
                    "create_date": str(invoice['create_date']),
                    }
            return Response(json.dumps(data),
                            content_type='application/json;charset=utf-8', status=200)
        else:
            data = {"status": False, "message": "No Data Found"}
            return Response(json.dumps(data),
                            content_type='application/json;charset=utf-8', status=200)

    @http.route('/invoice-info-api/payment-confirmation-with-status/', methods=['POST'], type='http', csrf=False, auth="public")
    def payment_confirmation(self, **kw):
        payment_status = kw['payment_status']
        data = {"status": True,
                "message": "Success",
                "payment_status": payment_status,
                }
        return Response(json.dumps(data),
                        content_type='application/json;charset=utf-8', status=200)

    # @http.route('/invoice_info_api/invoice_info_api/objects/<model("invoice_info_api.invoice_info_api"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('invoice_info_api.object', {
    #         'object': obj
    #     })
