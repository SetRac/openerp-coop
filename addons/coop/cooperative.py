# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class cooperative(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]



    _columns = {
        'is_cooperative': fields.boolean(string='Is Cooperative?'),
        'coop_code': fields.char(string='Cooperative Id'),
    }

    _defaults = {
    }


    _constraints = [
    ]




cooperative()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
