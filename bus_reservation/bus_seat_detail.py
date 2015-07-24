from openerp.osv import orm, fields

class seat(orm.Model):
    _name = 'seat.detail'
    _rec_name = 'date'
    _columns = {
        'date':fields.date('date'),
        'book_id':fields.one2many("bus.seat","bus_id",'Booking'),
    
        
    
    }