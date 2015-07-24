from openerp.osv import orm, fields

class sale_cash_change(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner' 
    _columns = {
        'payment_type':fields.selection([('cash','CASH'),('check','CHECK'),('online','ONLINE TRANSCATION')],string='Payment Type')
    
    }
    
    
# def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
#     res = super(sale_cash_change, self).onchange_partner_id(cr, uid, ids, partner_id, context=context)
#     return res