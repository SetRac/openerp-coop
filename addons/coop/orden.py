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

class orden(osv.osv):
    """"""
    
    _name = 'coop.orden'
    _description = 'orden'



    _columns = {
        'name': 
        'description': 
        'sequence': fields.integer(string='sequence'),
        'begin': fields.datetime(string='begin'),
        'end': fields.datetime(string='end'),
        'mocion_ids': fields.one2many('coop.mocion', 'discusion_id', string='mocion_ids'), 
        'asociado_id': fields.many2one('res.partner', string='asociado_id', required=True), 
        'asamblea_id': fields.many2one('coop.asamblea', string='asamblea_id'), 
        'reunion_id': fields.many2one('coop.reunion_consejo_administracion', string='reunion_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




orden()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
