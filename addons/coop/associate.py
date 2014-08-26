# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class associate(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]



    _columns = {
        'associate_id': fields.integer(string='associate_id'),
        'is_asociate': fields.boolean(string='is_asociate'),
        'mocion_ids': fields.one2many('coop.proposal', 'associate_id', string='mocion_ids'), 
        'discusion_ids': fields.one2many('coop.topic', 'associate_id', string='discusion_ids'), 
        'meeting_ids': fields.many2many('coop.meeting', 'coop_associate_ids_meeting_ids_rel', 'partner_id', 'meeting_id', string='meeting_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




associate()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
