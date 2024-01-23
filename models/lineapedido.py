# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class lineapedido(models.Model):
    _name = 'odoo_basico.lineapedido'
    _description = 'Este es el modulo'

    name = fields.Char(required=True, size=20, string='Título')
    descripcion = fields.Text(string='A descripción: ')
    # Os campos Many2one crean un campo na BD
    pedido_id = fields.Many2one('odoo_basico.pedido', ondelete="cascade", required=True)