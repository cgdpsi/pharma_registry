# -*- coding: utf-8 -*-
{
    "name": "Registre Pharmaceutique",
    "summary": "Gestion des établissements pharmaceutiques (officine, dépôt, grossiste, agence, fabrication)",
    "version": "16.0.1.0.0",
    "author": "Fatima",
    "category": "Industries",
    "license": "LGPL-3",
    "depends": [
        "base",
        "web",
        "contacts"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequences.xml",
        "wizards/import_geo_views.xml",
        "wizards/import_establishment_views.xml",
        "views/geo_views.xml",
        "views/officine_views.xml",
        "views/depot_views.xml",
        "views/grossiste_views.xml",
        "views/agence_views.xml",
        "views/fabrication_views.xml",
        "views/menus.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "pharma_registry/static/src/scss/pharma_forms.scss",
        ],
    },
    "application": True,
    "installable": True,
}
