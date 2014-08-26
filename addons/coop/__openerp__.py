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


{   'active': False,
    'author': 'No author.',
    'category': 'base.module_category_hidden',
    'demo_xml': [],
    'depends': [u'account'],
    'description': 'No documented',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': 'coop',
    'test': [],
    'update_xml': [   u'security/coop_group.xml',
                      u'view/cooperative_view.xml',
                      u'view/associate_view.xml',
                      u'view/topic_view.xml',
                      u'view/book_view.xml',
                      u'view/letter_view.xml',
                      u'view/partner_view.xml',
                      u'view/proposal_view.xml',
                      u'view/meeting_view.xml',
                      u'data/cooperative_properties.xml',
                      u'data/associate_properties.xml',
                      u'data/topic_properties.xml',
                      u'data/book_properties.xml',
                      u'data/letter_properties.xml',
                      u'data/partner_properties.xml',
                      u'data/proposal_properties.xml',
                      u'data/meeting_properties.xml',
                      u'data/cooperative_track.xml',
                      u'data/associate_track.xml',
                      u'data/topic_track.xml',
                      u'data/book_track.xml',
                      u'data/letter_track.xml',
                      u'data/partner_track.xml',
                      u'data/proposal_track.xml',
                      u'data/meeting_track.xml',
                      u'workflow/proposal_workflow.xml',
                      u'workflow/letter_workflow.xml',
                      'security/ir.model.access.csv',
                      u'view/coop_menuitem.xml'],
    'version': 'No version',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
