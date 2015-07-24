from openerp.osv import orm, fields

class wizard_customer(orm.TransientModel):
    
    _name = 'wizard.customer'
    
    _columns = {
            'cust':fields.many2one('billing.order','Customer Name',required=True),
            'age_selection':fields.selection([(24,24),(25,25),(26,26)], string='age selection' ),
                    }
    
    def wiz(self, cr, uid, ids, context):
        wiz_rec = self.browse(cr, uid, ids, context=None)
        chang_wiz=self.pool.get('billing.product')
        for x in wiz_rec:
            print type("cust")
            chang_wiz.write(cr, uid,context.get('active_ids', []),{'customer': x.cust.customer,'age': x.age_selection   } )
        