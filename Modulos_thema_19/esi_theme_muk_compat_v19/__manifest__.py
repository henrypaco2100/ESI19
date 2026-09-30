# -*- coding: utf-8 -*-
{
    "name": "ESI Theme - MuK Compatibility v19",
    "summary": "Capa visual ESI cargada despues de MuK Backend Theme",
    "version": "19.0.2.0.0",
    "category": "Themes/Backend",
    "author": "ESI - Especialistas en Sistemas Integrados",
    "website": "https://esibolivia.store",
    "license": "LGPL-3",
    # Dependencia intencional: garantiza que este CSS se cargue despues de MuK.
    "depends": ["esi_theme_core_v19", "muk_web_theme"],
    "assets": {
        "web.assets_backend": [
            "esi_theme_muk_compat_v19/static/src/css/muk_compat.css",
        ],
    },
    "installable": True,
    "application": False,
}
