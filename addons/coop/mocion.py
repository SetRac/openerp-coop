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

class mocion(osv.osv):
    """"""
    
    _name = 'coop.mocion'
    _description = 'mocion'

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
        'name': 
        'propuesta': 
        'presented': fields.datetime(string='presented'),
        'votos_pos': fields.integer(string='votos_pos'),
        'votos_neg': fields.integer(string='votos_neg'),
        'votos_neu': fields.integer(string='votos_neu'),
        'state': fields.selection(_states_, "State"),
        'discusion_id': fields.many2one('coop.orden', string='discusion_id', required=True), 
        'asociado_id': fields.many2one('res.partner', string='asociado_id', required=True), 
    }

    _defaults = {
        'state': 'draft',
    }


    _constraints = [
    ]


    def action_wfk_set_draft(self, cr, uid, ids, *args):
        self.write(cr, uid, ids, {'state':'draft'})
        wf_service = netsvc.LocalService("workflow")
        for obj_id in ids:
            wf_service.trg_delete(uid, 'coop.mocion', obj_id, cr)
            wf_service.trg_create(uid, 'coop.mocion', obj_id, cr)
        return True



mocion()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
