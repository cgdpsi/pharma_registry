# -*- coding: utf-8 -*-
"""Model storing the detailed profile of community pharmacies (officines)."""

from odoo import fields, models


class PharmaOfficine(models.Model):
    """Pharmacy record enriched with workforce & business indicators."""

    _name = "pharma.officine"
    _description = "Officine"
    _inherit = "pharma.establishment.base"

    name = fields.Char(string="Nom de l'officine", required=True)
    numero_telephone = fields.Char(string="Numéro téléphone", required=True)
    annee_creation = fields.Integer(string="Année de création", required=True)
    annee_exploitation = fields.Integer(string="Année d'exploitation", required=True)
    statut = fields.Selection(
        [
            ("transfert", "Transfert"),
            ("rachat", "Rachat"),
            ("creation","Création"),
        ],
        string="Statut (Transfert / Rachat / Création)",
    )
    titulaire_nom = fields.Char(string="Prénom et nom titulaire / pharmacien responsable", required=True)
    numero_ordre = fields.Char(string="Numéro d'inscription ordre des pharmaciens", required=True)
    sexe_titulaire = fields.Selection(
        [("f", "Féminin"), ("m", "Masculin"),],
        string="Sexe",
    )
    tranche_age = fields.Selection(
        [
            ("moins_30", "Moins de 30 ans"),
            ("30_39", "30 - 39 ans"),
            ("40_49", "40 - 49 ans"),
            ("50_59", "50 - 59 ans"),
            ("60_plus", "60 ans et plus"),
            ("na", "Non renseigné"),
        ],
        string="Tranche d'âge",
    )
    nombre_assistants = fields.Integer(string="Nombre d'assistants")
    nombre_employe_pharmacien = fields.Integer(string="Nombre d'employés pharmaciens")
    nombre_employe_non_pharmacien = fields.Integer(string="Nombre d'employés non pharmaciens")
    nombre_agent_securite = fields.Integer(string="Nombre d'agents de sécurité")
    nombre_agent_hygiene = fields.Integer(string="Nombre d'agents d'hygiène")
    currency_id = fields.Many2one(
        "res.currency",
        string="Devise",
        default=lambda self: self.env.company.currency_id.id if self.env.company else None,
    )
    chiffre_affaire = fields.Monetary(string="Chiffre d'affaires", currency_field="currency_id")
    nombre_vehicule = fields.Integer(string="Nombre de véhicules (livraison / transfert)")
