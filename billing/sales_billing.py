from openerp.osv import orm, fields

class new_sales(orm.Model):
    _name = 'new.sales'
    
    _columns = {
                
        'age':fields.integer("Age"),                     
    
    
    }