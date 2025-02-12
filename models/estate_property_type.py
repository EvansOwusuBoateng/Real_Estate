from odoo import models, fields

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=1)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
