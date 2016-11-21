
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
    _name = 'gymmaterial'
    _description = 'Material de gimnasio.'
    _columns = {
        'name': fields.char('First name', size=64, required=True),
        'quantity': fields.integer("quantity"),
        'materialType': fields.selection([
        ('instruments','Instruments'),
        ('clothes','Clothes'),
        ('others','Others'),
        ],'Type of Material'),
        'gymusers_ids': fields.many2many( 'gymuser','gymuser_material_rel', 'gymmaterial_id', 'gymuser_id', 'Users with hired material.'),
        'gymclass_ids': fields.many2many( 'gymclass','gymuser_material_rel', 'gymmaterial_id', 'gymclass_id', 'Classes with hired material'),
    }
    _defaults = {  
        'materialType': "instruments",  
        }