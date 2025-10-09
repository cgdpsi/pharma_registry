# -*- coding: utf-8 -*-
"""Représentation des agences de promotion pharmaceutique."""

from odoo import fields, models


class PharmaAgence(models.Model):
    """Fiche d'agence intégrant les identifiants réglementaires et les effectifs."""

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
    chiffre_affaire = fields.Float(string="Chiffre d'affaires (FCFA)")
    laboratoire_represente = fields.Char(string="Nom du laboratoire représenté")
