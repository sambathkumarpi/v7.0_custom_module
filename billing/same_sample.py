from openerp.osv import orm, fields

class same_sample(orm.Model):
    _name = 'sample'
    _inherit = 'sample'
    _columns = {
                "mobile":fields.integer("mobile"),
                "customer":fields.integer("Customer")
    }
    def on_change_name(self, cr, uid, ids, age, context=None):
#         y = {}
#         
#         if age == 23:
#             y = {
#                'customer':12
#                }
#         return  {'value':y}
        res = super(same_sample, self).on_change_name(cr, uid, ids, age, context=context)
        print "super"
        res['value']['customer']=22
        print res['value']
        return  res
