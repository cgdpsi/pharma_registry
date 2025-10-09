"""Shared building blocks for every pharma establishment model."""

# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PharmaEstablishmentBase(models.AbstractModel):
    """Abstract model capturing the geographical footprint of an entity."""

    _name = "pharma.establishment.base"
    _description = "Base établissement pharmaceutique"

    region_id = fields.Many2one(
        "pharma.geo.region",
        string="Région",
        required=True,
        help="Région d'implantation",
    )
    department_id = fields.Many2one(
        "pharma.geo.department",
        required=True,
        string="Département",
        help="Département correspondant à la région",
    )
    commune_id = fields.Many2one(
        "pharma.geo.commune",
        required=True,
        string="Commune",
        help="Commune correspondant au département",
    )
    code = fields.Char(
        string="Code",
        # required=True,
        copy=False,
        readonly=True,
        # default=lambda self: self._generate_code_prefix(),
    )
    quartier = fields.Char(string="Quartier / Village / Hameau", required=True)
    adresse = fields.Char(string="Adresse exacte", required=True)
    latitude = fields.Float(string="Latitude", default=False, digits=(10, 6))
    longitude = fields.Float(string="Longitude", default=False, digits=(10, 6))
    points_geolocalisation = fields.Char(
        string="Points de géolocalisation",
        compute="_compute_points_geolocalisation",
        inverse="_inverse_points_geolocalisation",
        store=True,
    )
    observations = fields.Text(string="Observations")
    active = fields.Boolean(default=True, string="Actif")
    photo = fields.Image(string="Photo", max_width=1024, max_height=1024)

    @api.constrains("department_id", "region_id")
    def _check_region_coherence(self):
        """Vérifier si le département appartient à la région"""

        for record in self:
            if (
                record.department_id
                and record.region_id
                and record.department_id.region_id != record.region_id
            ):
                raise ValidationError(
                    "Le département choisi n'appartient pas à la région sélectionnée."
                )

    @api.constrains("commune_id", "department_id")
    def _check_department_coherence(self):
        """Ensure the commune belongs to the same department as the record."""

        for record in self:
            if (
                record.commune_id
                and record.department_id
                and record.commune_id.department_id != record.department_id
            ):
                raise ValidationError(
                    "La commune choisie n'appartient pas au département sélectionné."
                )

    @api.depends("latitude", "longitude")
    def _compute_points_geolocalisation(self):
        """ Afficher la latitude et la longitude séparée par une virgule"""

        for record in self:
            if record.latitude not in (False, None) and record.longitude not in (False, None):
                record.points_geolocalisation = f"{record.latitude},{record.longitude},"
            else:
                record.points_geolocalisation = False

    def _inverse_points_geolocalisation(self):
        """Allow manual edition of the comma-separated coordinates if needed."""

        for record in self:
            value = (record.points_geolocalisation or "").strip()
            if not value:
                record.latitude = False
                record.longitude = False
                continue

            parts = [p.strip() for p in value.split(",") if p.strip()]
            if len(parts) >= 2:
                try:
                    lon = float(parts[0])
                    lat = float(parts[1])
                except ValueError:
                    continue
                record.longitude = lon
                record.latitude = lat

    @api.model
    def create(self, vals):
        if not vals.get("code"):
            vals["code"] = self._generate_code_prefix()
        return super().create(vals)

    def _generate_code_prefix(self):
        """Generate an identifier with a type-specific prefix."""

        prefix_map = {
            "pharma.officine": "off",
            "pharma.depot": "dep",
            "pharma.grossiste": "gros",
            "pharma.agence": "agen",
            "pharma.fabrication": "eta",
        }
        sequence_map = {
            "pharma.officine": "pharma.officine.code",
            "pharma.depot": "pharma.depot.code",
            "pharma.grossiste": "pharma.grossiste.code",
            "pharma.agence": "pharma.agence.code",
            "pharma.fabrication": "pharma.fabrication.code",
        }

        prefix = prefix_map.get(self._name, "etab")
        seq_code = sequence_map.get(self._name, "pharma.establishment.code")
        number = self.env["ir.sequence"].next_by_code(seq_code)
        if not number:
            number = self.env["ir.sequence"].next_by_code("pharma.establishment.code") or "0001"
        return f"{prefix}-{number}"
