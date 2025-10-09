# -*- coding: utf-8 -*-
"""Representation of pharmaceutical promotion agencies."""

from odoo import fields, models


class PharmaAgence(models.Model):
    """Agency record including regulatory identifiers and staffing."""

    _name = "pharma.agence"
    _description = "Agence de promotion"
    _inherit = "pharma.establishment.base"

    name = fields.Char(string="Nom de l'agence de promotion", required=True)
    numero_telephone = fields.Char(string="Numéro téléphone", required=True)
    annee_ouverture = fields.Integer(string="Année d'ouverture", required=True)
    numero_agrement = fields.Char(string="Numéro de l'agrément", required=True)
    date_agrement = fields.Date(string="Date de l'agrément", required=True)
    pharmacien_responsable = fields.Char(string="Prénom et nom du pharmacien responsable", required=True)
    nombre_employe_pharmacien = fields.Integer(string="Nombre d'employés pharmaciens", required=True)
    nombre_employe_non_pharmacien = fields.Integer(string="Nombre d'employés non pharmaciens", required=True)
    currency_id = fields.Many2one(
        "res.currency",
        string="Devise",
        default=lambda self: self.env.company.currency_id.id if self.env.company else None,
    )
    chiffre_affaire = fields.Monetary(string="Chiffre d'affaires", currency_field="currency_id")
    laboratoire_represente = fields.Char(string="Nom du laboratoire représenté")
