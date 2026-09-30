# -*- coding: utf-8 -*-
{
    'name': 'ESI Agente IA',
    'version': '19.0.1.0.0',
    'summary': 'Agentes IA por área y registro de interacciones',
    'author': 'ESI - Especialistas en Sistemas Integrados',
    'website': 'https://esibolivia.store',
    'category': 'Productivity',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/interaction_views.xml',
        'views/settings_views.xml',
        'views/menus.xml',
    ],
    'application': True,
    'installable': True,
}
