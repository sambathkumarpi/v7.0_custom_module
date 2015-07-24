from openerp.osv import orm, fields

class billing_inline(orm.Model):
    _name = 'billing.inline'
    _inherits = {  
                 'billing.order': 'customer_id',
                 'fruit.varieties': 'fruit_ids' 
    }
    _columns = {
        
        'customer_id':fields.many2one('billing.order','Customer Name',required=True,ondelete='cascade'),
        'total':fields.integer('total'),
       # 'fruit_ids':fields.many2one('fruit.varieties','Product',required=True,ondelete='cascade'),
        
        
    
    }