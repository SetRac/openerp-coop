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

class asociado(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]



    _columns = {
        'matricula': fields.integer(string='matricula'),
        'mocion_ids': fields.one2many('coop.mocion', 'asociado_id', string='mocion_ids'), 
        'discusion_id': fields.one2many('coop.orden', 'asociado_id', string='discusion_id'), 
        'asamblea_ids': fields.many2many('coop.asamblea', 'coop_asociado_ids_asamblea_ids_rel', 'partner_id', 'asamblea_id', string='asamblea_ids'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




asociado()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
