# -*- coding: utf-8 -*-
"""Wholesale distributors of pharmaceutical products."""

from odoo import fields, models


class PharmaGrossiste(models.Model):
    """Grossiste combines location info with workforce and logistics data."""

    _name = "pharma.grossiste"
    _description = "Grossiste répartiteur"
    _inherit = "pharma.establishment.base"

    name = fields.Char(string="Nom grossiste répartiteur", required=True)
    numero_telephone = fields.Char(string="Numéro téléphone", required=True)
    annee_ouverture = fields.Integer(string="Année d'ouverture", required=True)
    responsable_nom = fields.Char(string="Prénom et nom responsable / directeur", required=True)
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
    nombre_vehicule = fields.Integer(string="Nombre de véhicules (livraison / transfert)")
