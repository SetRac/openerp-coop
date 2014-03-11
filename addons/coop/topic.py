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
