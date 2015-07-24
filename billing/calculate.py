from openerp.osv import orm, fields

class calculate(orm.Model):
    _name = 'billing.calculate'
    _rec_name = 'p_name'
    _inherits = {  'fruit.varieties': 'item_id'}
    
    def cal(self, cr, uid, ids, field_name, arg, context=None ):
        res={}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id]=record.price*record.quantity 
        return res
    
#     def _tax(self, cr, uid, ids, field_name, arg, context=None):
#         x={}
#         y={}
#         for record in self.browse(cr, uid, ids, context=None):
#             x[record.id]=record.price*record.quantity
#             y[record.id]=x*(4/100)
#         return y
#     def _search_fruit(self, cr, uid, ids, field_name, arg, context=None):
#         cr.execute('select billing_calculate.id from billing_calculate inner join fruit_varieties on billing_calculate.item_id = fruit_varieties.id where quantity * price  = 100')
#         res = cr.fetchall()
#         print res,arg
#         return [('id', 'in', [x[0] for x in res])]
#         
        
       
    
    def _cal_qual(self, cr, uid, id, name, value, arg, context=None ):
        record=self.browse(cr, uid, id, context=context)
        return self.write(cr, uid, [id], {'quantity':  value / record.price}, context=context)
#          
    
    
    _columns = {
                'item_id':fields.many2one('fruit.varieties','item reference', requierd=True , ondelete='casacde'),
                'quantity':fields.float('quantity'),
                'total':fields.function(cal,fnct_inv=_cal_qual,string='total',type="float"),
#                                         store={
#                                                'billing.calculate': (lambda self, cr, uid, ids, c={}: ids, ['quantity'], 20),
#                                                },),
            #    'tax':fields.function(_tax, method=True, type='float', string='Tax', store=True),fnct_search=_search_fruit  
                 
    }
    
    def dummy(self, cr, uid, ids, context=None):
        pass
    
  
