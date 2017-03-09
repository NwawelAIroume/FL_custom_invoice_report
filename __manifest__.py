# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Identymed Addon',
    'version': '1.0',
    'author' : 'David Schuler',
    'category' : 'Sales',
    'summary': 'Custom invoice report',
    'depends':['sale',
               'account'
               ],
    'description': """
Custom invoice report
""",
    'data': ['report/custom_report_invoice.xml'],
    'application': True,
}