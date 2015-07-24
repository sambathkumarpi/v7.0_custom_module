from openerp.osv import orm, fields
from datetime import datetime

class billing_product(orm.Model):
    _name = 'billing.product'
    _rec_name = 'customer'
    _inherits = {  'billing.order': 'billing_order_id'  }
    
    def py_wizard_change(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        view_id = mod_obj.get_object_reference(cr, uid, 'billing', 'wizard_customer_form_view')
        return {
            'name': "wizard customer" ,
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id and view_id[1] or False,
            'res_model': 'wizard.customer',
            'src_model': 'billing.product',
            'type': 'ir.actions.act_window',
            'context': context,
            'target': 'new',
            }
        
        
    _columns = {
            "product_name":fields.char("Product name",),
            "quandity":fields.integer("Quantity"),
            "quality":fields.selection((("I","First"),("II","Second"),("III","Third")),string="Quality"),
            "in_date":fields.date("In Date"),
            "manufacture_date":fields.date("Manuf Date"),
            "expire_date":fields.date("Expire Date"),
            "cost":fields.integer("Cost"),
            "description":fields.text("description"),
            "billing_order_id":fields.many2one("billing.order", required=True, ondelete='cascade'),
            "onemany_id":fields.many2one('billing.onemany', "Referance"),
    
    }
    
    _defaults = {  
        'in_date': lambda *a: datetime.today().strftime('%Y-%m-%d'),
        }
    def _product_check(self, cr, uid, ids): 
        res = {} 
        for res in self.browse(cr, uid, ids, context=None):
            if res.quandity > 10:
                return True
            return False

    _constraints = [(_product_check, 'NO AREA', ['quandity']), ]
    
    #_sql_constraints = [     ('name_app', 'CHECK (product_name ilike app)', 'The Name of the OpenERPModel must be unique !'),      ]
    
    
    
    
    
    