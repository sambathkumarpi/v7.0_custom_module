from openerp.osv import orm, fields

class inh_sample(orm.Model):
    _name = 'inh.sample'
    _inherit ='sample'
    _columns = {
                "mobile":fields.integer("mobile")
    }
