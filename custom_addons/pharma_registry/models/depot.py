# -*- coding: utf-8 -*-
"""Modèle décrivant les dépôts pharmaceutiques de proximité."""

from odoo import fields, models


class PharmaDepot(models.Model):
    """Dépôt  ajoutant les informations de gestion."""

    _name = "pharma.depot"
    _description = "Dépôt de médicaments"
    _inherit = "pharma.establishment.base"

    name = fields.Char(string="Nom du dépôt", required=True)
    numero_telephone = fields.Char(string="Numéro téléphone", required=True)
    annee_ouverture = fields.Integer(string="Année d'ouverture", required=True)
    responsable_nom = fields.Char(string="Prénom et nom responsable / dépositaire", required=True)
    sexe_responsable = fields.Selection(
        [("f", "Féminin"), ("m", "Masculin"), ("na", "Non renseigné")],
        string="Sexe",
    )
