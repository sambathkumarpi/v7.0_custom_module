from openerp.osv import orm, fields

class registration(orm.Model):
    _name = 'registration'
    _columns = {
                'name':fields.char('Name :',size=20),
                'mobile':fields.integer('Mobile No.:',size=14),
                'gender':fields.selection((('M','Male'),('F','Female')),string='Gender :'),
                'email':fields.char('E-mail :',size=25),
                'pass':fields.char('Password :',size=15)
    
    }
    
    
