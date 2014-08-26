# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class letter(osv.osv):
    """"""
    
    _name = 'coop.letter'
    _description = 'letter'

    _states_ = [
        # State machine: untitle
        ('draft','draft'),
        ('review','review'),
        ('cancel','cancel'),
        ('sent','sent'),
    ]


    _columns = {
        'name': fields.char(string='name'),
        'content': fields.char(string='content'),
        'state': fields.selection(_states_, "State"),
        'issuer_id': fields.many2one('res.partner', string='issuer_id', required=True), 
        'receiver_id': fields.many2one('res.partner', string='receiver_id', required=True), 
        'inquiri_id': fields.many2one('coop.letter', string='inquiri_id'), 
        'respond_id': fields.one2many('coop.letter', 'inquiri_id', string='respond_id'), 
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def action_wfk_set_cancel(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'cancel'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'coop.letter', obj_id, cr)
            wf_service.trg_create(uid, 'coop.letter', obj_id, cr)
        return True

    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'coop.letter', obj_id, cr)
            wf_service.trg_create(uid, 'coop.letter', obj_id, cr)
        return True



letter()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
