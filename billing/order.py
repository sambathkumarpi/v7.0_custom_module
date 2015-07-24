from openerp.osv import orm, fields
import re


class billing_order(orm.Model):
    _name = 'billing.order'
    _rec_name = 'customer'
    
    def _has_image(self, cr, uid, ids, name, args, context=None):
        result = {}
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = obj.image != False
        return result
    def  validateemail(self, cr, uid, ids, email, context=None):
        print 'check'
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
        else:
            raise orm.except_orm('Invalid Email', 'Please enter a valid email address')
 
    _columns = {
        'customer':fields.char('Customer', required=True, help='the name'),
        'email':fields.char('Email'),
        'phone':fields.char('Phone'),
        'age':fields.float('Age'),
        'gender':fields.selection([('m', 'Male'), ('f', 'Female')], 'Gender'),
        'join_date':fields.date('Join'),
        'left_date':fields.date('left'),
        'image':fields.binary('image'),
        'street':fields.char('street'),
        'street2':fields.char('street2'),
        'city':fields.char('city'),
        'state':fields.char('state'),
        'zip':fields.char('zip'),
        'country':fields.char('country'),
        'reg_no':fields.char('Reg', readonly=True),
        'has_image': fields.function(_has_image, type="boolean"),
    }
    
#     _sql_constraints = [    
#                          ('name_uniq', 'unique (customer,email,phone)', 'Name and email ID is already reg. !'),      
#                          ('date_check', 'CHECK (age > 18)', 'your can\'t reg. your age is not satified '),
#                          
#                          ]
#     
    _defaults = {'reg_no': '/', }

    def create(self, cr, uid, vals, context=None):
        if not vals:
            vals = {}
        if context is None:
            context = {}
        vals['reg_no'] = self.pool.get('ir.sequence').get(cr, uid, 'UR_module')
        return super(billing_order, self).create(cr, uid, vals, context=context)
    
#     def _get_image(self, cr, uid, ids, name, args, context=None):
#         result = dict.fromkeys(ids, False)
#         for obj in self.browse(cr, uid, ids, context=context):
#             result[obj.id] = tools.image_get_resized_images(obj.image)
#         return result
