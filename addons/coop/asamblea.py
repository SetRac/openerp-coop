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

class asamblea(osv.osv):
    """"""
    
    _name = 'coop.asamblea'
    _description = 'asamblea'



    _columns = {
        'name': 
        'number': fields.integer(string='number'),
        'apertura': fields.datetime(string='apertura'),
        'cierre': fields.datetime(string='cierre'),
        'reunion_ids': fields.one2many('coop.reunion_consejo_administracion', 'acta_asamblea_id', string='reunion_ids'), 
        'sequence_id': fields.many2one('ir.sequence', string='sequence_id', required=True), 
        'discusion_ids': fields.one2many('coop.orden', 'asamblea_id', string='discusion_ids'), 
        'asociado_ids': fields.many2many('res.partner', 'coop_asociado_ids_asamblea_ids_rel', 'asamblea_id', 'asociado_id', string='asociado_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




asamblea()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
