# -*- coding: utf-8 -*-
{
    "name": "ESI Theme Login v19",
    "summary": "Inicio de sesion corporativo ESI compatible con Odoo 19",
    "version": "19.0.2.0.0",
    "category": "Themes/Backend",
    "author": "ESI - Especialistas en Sistemas Integrados",
    "website": "https://esibolivia.store",
    "license": "LGPL-3",
    "depends": ["esi_theme_core_v19", "auth_signup"],
    "data": [
        "views/login_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "esi_theme_login_v19/static/src/css/login.css",
        ],
    },
    "installable": True,
    "application": False,
}
