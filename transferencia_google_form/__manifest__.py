# -*- coding: utf-8 -*-
{
    'name': 'Transferencia de documentos por Google Form',
    'version': '1.0',
    'category': 'others',
    'description': """
        Tramsferenia de documentos
    """,
    'author': 'Ministerio de Salud(MINSA) '
              'Developers',
    'depends': [
    ],
    'data': [
        # Data
        'data/data.xml',

        # Security
        'security/security.xml',
        'security/ir.model.access.csv',

        # Views
        'views/views.xml',
        # 'views/views_approval_process.xml',
        'views/menus.xml',

        # Reports
        'report/report_views.xml',
    ],
    'active': True,
    'application': True,
}
