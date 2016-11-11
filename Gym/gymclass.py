# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2014 TRESCloud S.A. (http://www.trescloud.com). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class gymclass(osv.Model):

    _name = 'gymclass'
    _description = 'Class scheduled in a gym'
    _columns = {
            'name': fields.char('Class name', size=64, required=True),
            'start': fields.datetime('Starts',required=True, autodate = True),
            'end': fields.datetime('Ends',required=True, autodate = True),
            'capacity': fields.integer("Capacity"),
            'gymusers_ids': fields.many2many( 'gymuser','gymuser_gymclass_rel',
            'gymclass_id', 'gymuser_id', 'Confirmed users'),
            'activityType': fields.selection([
            ('dance','Dance'),
            ('aerobic','Aerobic'),
            ('anaerobic','Anaerobic'),
            ('relax','Relax'),
            ],'Type of activity'),
        }