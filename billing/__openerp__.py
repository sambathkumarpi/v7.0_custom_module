{
    "name": "billing",
    "version": "1.0",
    "depends": ["base","sale","web"],
    "author": "open source",
    "category": "Test",
    "description": """
    This module provide :
    cr
    """,
    "data" : [
              'wizard/wizard_customer_view.xml',
              'order.xml',
              #'sales_billing.xml',
              'inh_sample.xml',
              'same_sample.xml',
              'billing_product.xml',
              'list_product.xml',
              'calculate.xml',
              'sale_cash_change.xml',
              'sale_order_change.xml',
              'onemany.xml',
              'billing_inline.xml',
            
              ],
    'installable': True,
    'active': True,
}