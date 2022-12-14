# -*- coding: utf-8 -*-

# from odoo import models, fields, api


class company(models.Model):
    _name = 'empresas.company'
    _description = 'empresas.company'

    name = fields.Char(string="Nombre", required=True)
    cif = fields.Char(string="CIF", required=True)
    description = fields.Text(string="Descripción")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    

class empleado(models.Model):
    _name = 'empresas.empleado'
    _description = 'empresas.empleado'

    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    description = fields.Text(string="Descripción")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    company_id = fields.Many2one('empresas.company', string="Empresa")

class cliente(models.Model):
    _name = 'empresas.cliente'
    _description = 'empresas.cliente'

    name = fields.Char(string="Nombre", required=True)
    cif = fields.Char(string="CIF", required=True)
    description = fields.Text(string="Descripción")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    company_id = fields.Many2one('empresas.company', string="Empresa")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
