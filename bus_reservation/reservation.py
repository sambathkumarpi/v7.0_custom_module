from openerp.osv import orm, fields

class reservation(orm.Model):
    _name = 'buss.reservation'
    _columns = {
                'movie_name':fields.char("MOVIE"),
                "date":fields.date('Date'),
                'n_o_seat':fields.char('No. of seat')
    
    }