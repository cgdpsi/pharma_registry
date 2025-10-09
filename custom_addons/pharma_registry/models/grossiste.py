# -*- coding: utf-8 -*-
"""Grossistes répartiteurs de produits pharmaceutiques."""

from odoo import fields, models


class PharmaGrossiste(models.Model):
    """Grossiste qui combine localisation, effectifs et données logistiques."""

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
    chiffre_affaire = fields.Float(string="Chiffre d'affaires (FCFA)")
    nombre_vehicule = fields.Integer(string="Nombre de véhicules (livraison / transfert)")
