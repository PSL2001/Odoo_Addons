# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alumnos(models.Model):
    _name = 'estudiantes.alumnos'
    _description = 'estudiantes.alumnos'

    nombre = fields.Char("Nombre", help="Introduce el nombre", required=True, size = 20)
    apellidos = fields.Char("Apellidos", help="Introduce tus apellidos", required=True, size=40)
    edad = fields.Integer("Edad", required = True)
    activo = fields.Boolean("Activo", required = True, default = True)
    fecha_Inicio = fields.Date("Fecha de inicio de curso", required = True)
    curso = fields.Selection(selection = [("dam", "Desarrollo de Aplicaciones Multiplataforma"), ("daw", "Desarrollo de Aplicaciones Web"), ("cev", "Curso de Especializacion de Videojuegos")])

    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()
#
    #@api.depends('value')
    #def _value_pc(self):
    #    for record in self:
    #        record.value2 = float(record.value) / 100

class profesores(models.Model):
    _name = 'estudiantes.profesores'
    _description = 'estudiantes.profesores'

    nombre = fields.Char("Nombre", help="Introduce el nombre", required=True, size = 20)
    apellidos = fields.Char("Apellidos", help="Introduce tus apellidos", required=True, size=40)
    activo = fields.Boolean("Activo", required = True, default = True)
    asignatura = fields.Selection(selection = [("prog", "Programacion"), ("dis", "Diseño"), ("db", "Base de datos"), ("lm", "lenguaje de marcas")], required = True)
    descripcion = fields.Text("Descripcion", required=True)
    fecha_Inscripcion = fields.Date("Fecha de Inscripcion", required = True, default = lambda self: fields.Date.today())
   
class cursos(models.Model):
    _name = 'estudiantes.cursos'
    _description = 'estudiantes.cursos'

    nombre = fields.Char("Nombre", help="Introduce el nombre", required=True, size = 20)
    descripcion = fields.Text('Descripcion')
    fecha_creacion = fields.Date("Fecha de Creacion", required = True, default = lambda self: fields.Date.today())
    activo = fields.Boolean("Activo", required = True, default = True)
    precio = fields.Float("Precio", required = True)
    #Campo que calcula el total de dias que lleva existiendo el curso desde su fecha de creacion
    dias = fields.Integer("Dias", compute = "_value_pc", store = True)

    @api.depends('fecha_creacion')
    def _value_pc(self):
        for record in self:
            record.dias = (fields.Date.today() - record.fecha_creacion).days
    

