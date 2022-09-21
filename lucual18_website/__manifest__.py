# -*- coding: utf-8 -*-
{
    'name': "Lucual18",

    'summary': """
        This is a module to show and customize the Lucual18 oficial website
        """,

    'description': """
       Website Lucual18
    """,

    'author': "Lucual18",
    'application': True,

    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    "depends": ["website"],

    # always loaded
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/contact/contact.xml',
        'views/contact/thanks_contact.xml',
        'views/about/about.xml',
        'views/home/home.xml',
        'views/home/home_sections/banner_section.xml',
        'views/home/home_sections/services_section.xml',
        'views/home/home_sections/products_section.xml',
        'views/home/home_sections/team_section.xml',
        'views/home/home_sections/references_section.xml',
        'views/services/automation.xml',
        'views/services/erp.xml',
        'views/services/corp_design.xml',
        'views/services/outsourcing.xml',
        'views/services/scraping_web.xml',
        'views/services/software_dev.xml',
    ],

    "assets": {
        'web.assets_frontend': [
            "/lucual18_website/static/src/css/home_style.css",
            "/lucual18_website/static/src/css/services_style.css",
            # "/lucual18_website/static/src/js/script.js",
        ],
    }

}
