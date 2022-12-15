# -*- coding: utf-8 -*-

from odoo import models, fields, api


class company(models.Model):
    _name = 'empresas.company'
    _description = 'empresas.company'

    name = fields.Char(string="Nombre", required=True, help="Nombre de la empresa", size=100)
    cif = fields.Char(string="CIF", required=True, help="CIF de la empresa", size=9)
    description = fields.Text(string="Descripción", help="Descripción de la empresa")
    phone = fields.Char(string="Teléfono", help="Teléfono de la empresa", size=9, default="000000000", required=True)
    email = fields.Char(string="Email", help="Email de la empresa", size=100, required=True)
    

class empleado(models.Model):
    _name = 'empresas.empleado'
    _description = 'empresas.empleado'

    name = fields.Char(string="Nombre", required=True, help="Nombre del empleado", size=100, default="Jhon Doe")
    dni = fields.Char(string="DNI", required=True, help="DNI del empleado", size=9, default="00000000A")
    description = fields.Text(string="Descripción", help="Descripción del empleado", default="Empleado de la empresa")
    phone = fields.Char(string="Teléfono", help="Teléfono del empleado", size=9, default="000000000", required=True)
    email = fields.Char(string="Email", help="Email del empleado", size=100, required=True)
    company_id = fields.Many2one('empresas.company', string="Empresa", required=True, help="Empresa del empleado", ondelete='cascade', index=True, copy=False)
    #Campo fechaContratacion con fecha actual por defecto
    fechaContratacion = fields.Date(string="Fecha de contratación", help="Fecha de contratación del empleado", default=fields.Date.today)
    #Campo diasTrabajados que se calcula con la diferencia de dias entre la fecha actual y la fecha de contratacion
    diasTrabajados = fields.Integer(string="Días trabajados", help="Días trabajados por el empleado", compute="_diasTrabajados", store=True)

    #Funcion que calcula los dias trabajados
    @api.depends('fechaContratacion')
    def _diasTrabajados(self):
        for record in self:
            record.diasTrabajados = (fields.Date.today() - record.fechaContratacion).days

class cliente(models.Model):
    _name = 'empresas.cliente'
    _description = 'empresas.cliente'

    name = fields.Char(string="Nombre", required=True, help="Nombre del cliente", size=100, default="Jhon Doe")
    cif = fields.Char(string="CIF", required=True, help="CIF del cliente", size=9, default="00000000A")
    description = fields.Text(string="Descripción", help="Descripción del cliente", default="Cliente de la empresa")
    phone = fields.Char(string="Teléfono", help="Teléfono del cliente", size=9, default="000000000", required=True)
    email = fields.Char(string="Email", help="Email del cliente", size=100, required=True)
    company_id = fields.Many2one('empresas.company', string="Empresa", required=True, help="Empresa del cliente", ondelete='cascade', index=True, copy=False)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
