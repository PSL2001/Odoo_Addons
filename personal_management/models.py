#El archivo con la clase del personal
from odoo import fields, models

#models.model es la clase padre, nuestra clase heredará de esta
class Personal(models.Model):
    _name = "personal.personal"

    name = fields.Char("Nombre")
    surname = fields.Char("Apellidos")
    continente = fields.Selection(selection=[("africa","Africa"), ("asia", "Asia"), ("europa", "Europa"), ("oceania", "Oceania"), ("america", "America")])