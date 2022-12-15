# -*- coding: utf-8 -*-
{
    'name': "empresas",

    'summary': """
    Modulo para la gestion de empresas""",

    'description': """
        Modulo para la gestion de empresas, clientes y empleados de un negocio, con la posibilidad de crear, editar y eliminar empresas, clientes y empleados.
    """,

    'author': "Pablo Sánchez López",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        #Reportes
        'reports/report_company.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
