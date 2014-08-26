# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class book(osv.osv):
    """"""
    
    _name = 'coop.book'
    _description = 'book'



    _columns = {
        'name': fields.char(string='name'),
        'sequence_id': fields.many2one('ir.sequence', string='sequence_id', required=True), 
        'meeting_ids': fields.one2many('coop.meeting', 'book_id', string='meeting_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




book()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
