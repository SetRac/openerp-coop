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

class meeting(osv.osv):
    """"""
    
    _name = 'coop.meeting'
    _description = 'meeting'



    _columns = {
        'name': fields.char(string='name'),
        'number': fields.char(string='number'),
        'begin': fields.datetime(string='begin'),
        'end': fields.datetime(string='end'),
        'topic_ids': fields.one2many('coop.topic', 'meeting_id', string='topic_ids'), 
        'associate_ids': fields.many2many('res.partner', 'coop_associate_ids_meeting_ids_rel', 'meeting_id', 'associate_id', string='associate_ids'), 
        'book_id': fields.many2one('coop.book', string='book_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




meeting()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
