# -*- coding: utf-8 -*-
"""Référentiel géographique hiérarchique (région ➔ département ➔ commune)."""

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class PharmaGeoRegion(models.Model):
    """Niveau administratif supérieur utilisé par chaque établissement."""

    _name = "pharma.geo.region"
    _description = "Région sanitaire"
    _order = "name"

    name = fields.Char(string="Région", required=True)
    department_ids = fields.One2many("pharma.geo.department", "region_id", string="Départements")

    _sql_constraints = [
        ("pharma_geo_region_name_unique", "unique(name)", "Cette région existe déjà."),
    ]


class PharmaGeoDepartment(models.Model):
    """Niveau intermédiaire rattaché à une région et regroupant des communes."""

    _name = "pharma.geo.department"
    _description = "Département sanitaire"
    _order = "name"

    name = fields.Char(string="Département", required=True)
    region_id = fields.Many2one("pharma.geo.region", string="Région", required=True, ondelete="restrict")
    commune_ids = fields.One2many("pharma.geo.commune", "department_id", string="Communes")

    _sql_constraints = [
        (
            "pharma_geo_department_unique",
            "unique(name, region_id)",
            "Ce département existe déjà pour cette région.",
        ),
    ]


class PharmaGeoCommune(models.Model):
    """Plus petite entité administrative, liée à un département et à une région."""

    _name = "pharma.geo.commune"
    _description = "Commune sanitaire"
    _order = "name"

    name = fields.Char(string="Commune", required=True)
    region_id = fields.Many2one("pharma.geo.region", string="Région", required=True, ondelete="restrict")
    department_id = fields.Many2one(
        "pharma.geo.department",
        string="Département",
        required=True,
        ondelete="restrict",
    )

    _sql_constraints = [
        (
            "pharma_geo_commune_unique",
            "unique(name, department_id)",
            "Cette commune existe déjà pour ce département.",
        ),
    ]

    @api.constrains("department_id")
    def _check_department_region(self):
        """Valider que le département appartient à la région sélectionnée."""

        for record in self:
            if record.department_id.region_id != record.region_id:
                raise ValidationError("Le département doit appartenir à la région sélectionnée.")

    @api.onchange("region_id")
    def _onchange_region_id(self):
        """Réinitialiser ou restreindre les départements lorsqu'on change de région."""

        if self.department_id and self.department_id.region_id != self.region_id:
            self.department_id = False
        if self.region_id:
            return {
                "domain": {"department_id": [("region_id", "=", self.region_id.id)]}
            }
        return {"domain": {"department_id": []}}

    @api.onchange("department_id")
    def _onchange_department_id(self):
        """Reporter automatiquement la région depuis le département choisi."""

        if self.department_id:
            self.region_id = self.department_id.region_id
