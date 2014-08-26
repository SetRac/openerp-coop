# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class meeting(osv.osv):
    """"""
    
    _name = 'coop.meeting'
    _description = 'meeting'



    _columns = {
        'name': fields.char(string='name'),
        'number': fields.char(string='number'),
        'begin': fields.datetime(string='begin'),
        'end': fields.datetime(string='end'),
        'topic_ids': fields.one2many('coop.topic', 'meeting_id', string='topic_ids'), 
        'associate_ids': fields.many2many('res.partner', 'coop_associate_ids_meeting_ids_rel', 'meeting_id', 'associate_id', string='associate_ids'), 
        'book_id': fields.many2one('coop.book', string='book_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




meeting()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
