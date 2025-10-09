# -*- coding: utf-8 -*-
"""Manufacturing facility information."""

from odoo import fields, models


class PharmaFabrication(models.Model):
    """Extends the base mixin with production-specific workforce fields."""

    _name = "pharma.fabrication"
    _description = "Établissement de fabrication"
    _inherit = "pharma.establishment.base"

    name = fields.Char(string="Nom de l'établissement", required=True)
    numero_telephone = fields.Char(string="Numéro téléphone", required=True)
    annee_ouverture = fields.Integer(string="Année d'ouverture", required=True)
    responsable_nom = fields.Char(string="Prénom et nom responsable", required=True)
    nombre_employe_pharmacien = fields.Integer(string="Nombre d'employés pharmaciens", required=True)
    nombre_employe_non_pharmacien = fields.Integer(string="Nombre d'employés non pharmaciens", required=True)
    nombre_agent_securite = fields.Integer(string="Nombre d'agents de sécurité", required=True)
    nombre_agent_hygiene = fields.Integer(string="Nombre d'agents d'hygiène", required=True)
    currency_id = fields.Many2one(
        "res.currency",
        string="Devise",
        default=lambda self: self.env.company.currency_id.id if self.env.company else None,
    )
    chiffre_affaire = fields.Monetary(string="Chiffre d'affaires", currency_field="currency_id")
