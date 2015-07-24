from openerp.osv import orm, fields

class booking(orm.Model):
    _name = 'bus.booking'
    _columns = {
        'name':fields.many2one('registration','Person Name',select=True),
        'root':fields.selection((('c2P','Chennai to Pondicherry'),('p2c','Pondicherry to chennai')),string='Select Root'),
        'date':fields.many2one('seat.detail','dates',select=True),
        'seat_no':fields.many2one('bus.seat','seat no',select=True),
       # 'seat':fields.selection((('s1','S1'),('s2','S2'),('s3','S3'),('s4','S4'),('s5','S5'),('s6','S6'),('s7','S7'),('s8','S8'),('s9','S9'),('s10','S10')),string='seat No')


                }
    
    
