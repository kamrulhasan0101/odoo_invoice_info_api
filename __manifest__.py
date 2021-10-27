# -*- coding: utf-8 -*-
{
    'name': "Invoice Info Api",

    'summary': """This module is used to retrieve invoice information against invoice id provided by client""",

    'description': """
        This module is used to retrieve invoice information against invoice id provided by client. 
        It can be used in bkash ,nagad or any other mobile payment service to acquire payments.
    """,

    'author': "Md. Kamrul Hasan",
    'website': "http://www.daffodil-bd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
