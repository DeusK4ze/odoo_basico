# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_basico.suceso'
    _description = 'Este es el modulo'
    name = fields.Char(required=True, size=20, string="Suceso")
    descripcion = fields.Text(string="A Descripción do Suceso")
    nivel = fields.Selection([('Baixo', 'Baixo'), ('Medio', 'Medio'), ('Alto', 'Alto')], string='Nivel')
