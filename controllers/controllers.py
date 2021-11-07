# -*- coding: utf-8 -*-
import logging
import pprint
import werkzeug
from werkzeug import urls
from odoo.addons.payment.models.payment_acquirer import ValidationError
#imported from 1card module
_logger = logging.getLogger(__name__)

from odoo import http
from odoo.http import Response
from odoo.http import json
from odoo.http import request


class InvoiceInfoApi(http.Controller):
    @http.route('/invoice-info-api/', methods=['GET'], type='http', csrf=False, auth="public")
    def index(self, invoice_no):
        invoice = http.request.env['account.move'].sudo().search([('name', '=', invoice_no)])
        if invoice:
            data = {"name": invoice['name'],
                    "amount_total": str(invoice['amount_total']),
                    "payment_state": invoice['payment_state'],
                    "invoice_date": str(invoice['invoice_date']),
                    "invoice_date_due": str(invoice['invoice_date_due']),
                    "invoice_partner_display_name": invoice['invoice_partner_display_name'],
                    "create_date": str(invoice['create_date']),
                    }
            response_data = {
                "status": True,
                "message": "success",
                "data": data
            }
            return Response(json.dumps(response_data),
                            content_type='application/json;charset=utf-8', status=200)
        else:
            response_data = {"status": False, "message": "fail", "data": ''}
            return Response(json.dumps(response_data),
                            content_type='application/json;charset=utf-8', status=200)

    @http.route('/invoice-info-api/payment-confirmation-with-status/', methods=['POST'], type='http', csrf=False, auth="public")
    def payment_confirmation(self, **post):
        invoice_no = post['invoice_no']
        paid_amount = post['paid_amount']

        data = {"invoice_no": invoice_no,
                "paid_amount": paid_amount,
                }
        response_data = {
            "status": True,
            "message": "success",
            "data": data
        }
        return Response(json.dumps(response_data),
                        content_type='application/json;charset=utf-8', status=200)

