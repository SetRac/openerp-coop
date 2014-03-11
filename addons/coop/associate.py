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
