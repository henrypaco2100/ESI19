# -*- coding: utf-8 -*-
{
    "name": "ESI Theme Core v19",
    "summary": "Identidad visual ESI estable para Odoo 19 Community",
    "version": "19.0.2.0.0",
    "category": "Themes/Backend",
    "author": "ESI - Especialistas en Sistemas Integrados",
    "website": "https://esibolivia.store",
    "license": "LGPL-3",
    "depends": ["web"],
    "data": [
        "views/webclient_templates.xml",
    ],
    "assets": {
        # ESI correccion V2: CSS puro. No se modifican variables SCSS globales
        # para evitar conflictos de compilacion con MuK y otros temas.
        "web.assets_backend": [
            "esi_theme_core_v19/static/src/css/backend.css",
        ],
        "web.assets_frontend": [
            "esi_theme_core_v19/static/src/css/frontend.css",
        ],
    },
    "installable": True,
    "application": False,
}
