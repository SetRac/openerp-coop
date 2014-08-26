# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class topic(osv.osv):
    """"""
    
    _name = 'coop.topic'
    _description = 'topic'



    _columns = {
        'name': fields.char(string='name'),
        'description': fields.text(string='description'),
        'sequence': fields.integer(string='sequence'),
        'begin': fields.datetime(string='begin'),
        'end': fields.datetime(string='end'),
        'mocion_ids': fields.one2many('coop.proposal', 'topic_id', string='mocion_ids'), 
        'associate_id': fields.many2one('res.partner', string='associate_id', required=True), 
        'meeting_id': fields.many2one('coop.meeting', string='meeting_id', ondelete='cascade', required=True), 
    }

    _defaults = {
        'meeting_id': lambda self, cr, uid, context=None: context and context.get('meeting_id', False),
    }


    _constraints = [
    ]




topic()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
