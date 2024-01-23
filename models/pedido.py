# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class pedido(models.Model):
    _name = 'odoo_basico.pedido'
    _description = 'Este es el modulo'

    name = fields.Char(required=True, size=20, string='Título')
    descripcion = fields.Text(string='A descripción: ')
    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')



