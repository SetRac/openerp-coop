# -*- coding: utf-8 -*-

import re
from openerp import netsvc
from openerp.osv import osv, fields

class proposal(osv.osv):
    """"""
    
    _name = 'coop.proposal'
    _description = 'proposal'

    _states_ = [
        # State machine: untitle
        ('draft','draft'),
        ('waiting_for_referendum','waiting_for_referendum'),
        ('in_referendum','in_referendum'),
        ('canceled','canceled'),
        ('accepted','accepted'),
        ('rejected','rejected'),
    ]


    _columns = {
        'name': fields.char(string='name'),
        'description': fields.text(string='description'),
        'presented': fields.datetime(string='presented'),
        'affirmative_votes': fields.integer(string='affirmative_votes'),
        'negative_votes': fields.integer(string='negative_votes'),
        'other_votes': fields.integer(string='other_votes'),
        'state': fields.selection(_states_, "State"),
        'topic_id': fields.many2one('coop.topic', string='topic_id', ondelete='cascade', required=True), 
        'associate_id': fields.many2one('res.partner', string='associate_id', required=True), 
    }

    _defaults = {
        'state': 'draft',
        'topic_id': lambda self, cr, uid, context=None: context and context.get('topic_id', False),
    }


    _constraints = [
    ]


    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'coop.proposal', obj_id, cr)
            wf_service.trg_create(uid, 'coop.proposal', obj_id, cr)
        return True



proposal()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
