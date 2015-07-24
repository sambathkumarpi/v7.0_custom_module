from openerp.osv import orm, fields

class bus_reservation_wizard(orm.TransientModel):
    _name = 'bus.reservation.wizard'
    
    _columns = {
        'name': fields.char()
    }