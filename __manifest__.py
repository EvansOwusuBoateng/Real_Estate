{
    'name': 'Estate Application',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties',
    'author': 'Evans Owusu Boateng',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Ensure this file exists
        'views/estate_property_views.xml',  # Ensure this file exists
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
    ],
    'installable': True,
    'application': True,
}
