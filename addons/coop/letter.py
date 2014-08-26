# -*- coding: utf-8 -*-
##############################################################################
#
#    coop
#    Copyright (C) 2014 No author.
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


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
