# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'author': "Mohamed Anwar",
    'website': 'www.odoo.com',
    'summary': 'School Management Software',
    'sequence': -92,
    'depends': ['base', 'mail', 'contacts', 'report_xlsx', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/school.xml',
        'views/school_items.xml',
        'views/exam.xml',
        'views/teacher.xml',
        'report/school_report.xml',
        'report/student_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
