from openerp.osv import orm, fields

class sale_order_change(orm.Model):
    _name = 'sale.order'
    _inherit = 'sale.order' 
    _columns = {
        'payment_type':fields.selection([('cash','CASH'),('check','CHECK'),('online','ONLINE TRANSCATION')],string='Payment mode'),
        'country_code': fields.related('partner_id', 'country_id', 'code', relation='res.country', type='char', string='Country code' ),
        'partner_email': fields.related('partner_id', 'email', type='char', string='Partner email', store=True),
    
    }
    def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
        res = super(sale_order_change, self).onchange_partner_id(cr, uid, ids, partner_id, context=context)
        if partner_id:
            result=self.pool.get('res.partner').browse(cr, uid,partner_id, context=context)

            res['value']['payment_type']= result.payment_type
        print res
        return res  