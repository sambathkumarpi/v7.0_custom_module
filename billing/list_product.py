from openerp.osv import orm, fields

class fruit(orm.Model):
    _name = 'product.fruit'
    _rec_name = 'p_name'
    _columns = {
        "p_name":fields.char("P Name"),
        "quality":fields.selection([("I","First"),("II","Second"),("III","Third")],string="Quality"),
        "p_place":fields.char("P Place"),
        'color': fields.selection([('g','Green'),('r', 'Red'),('y',"yellow"),('d','default')], 'Color'),
        'in_date':fields.date("In Date"),
        'active':fields.boolean("Active")
    
    }
#     _sql_constraints = [     ('p_name', 'unique(p_name)', 'This product Name is allready present'), ]
    
class fruit_varieties(orm.Model):
    _name = 'fruit.varieties'
    _rec_name = 'p_name'
    _inherits = {'product.fruit': 'fruit_id'}    
    _columns = {
        'fruit_id': fields.many2one('product.fruit', 'Fruit reference', required=True, ondelete='casacde'),
        'price':fields.integer("price"),
        'p_names':fields.related('fruit_id','p_name', type='char',string='pro  id'),
        #'active':fields.boolean("Active", default=False, required=True )
    }
    
  #  def _get_name(self, cr, uid, ids, ):
    
    
