from openerp.osv import orm, fields

class Onemany(orm.Model):
    _name = 'billing.onemany'
    _columns = {
            'sample_id':fields.one2many('billing.product','onemany_id','sample id'),
            'date':fields.date('date')
    
    }