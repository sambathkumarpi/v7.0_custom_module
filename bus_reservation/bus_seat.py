from openerp.osv import orm, fields

class bus_seat(orm.Model):
    _name = 'bus.seat'
    _rec_name = 'seatno'
    _columns = {
                'seatno':fields.integer("Seat No:"),
                'booked':fields.boolean('Select',default=False),
                'bus_id':fields.many2one("seat.detail","Seat Detail")
    
    }