# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class partner(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]



    _columns = {
        'sent_letter_ids': fields.one2many('coop.letter', 'issuer_id', string='sent_letter_ids'), 
        'received_letter_ids': fields.one2many('coop.letter', 'receiver_id', string='received_letter_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
