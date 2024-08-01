from odoo import api, fields, models, _


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _rec_name = 'student_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Teacher Information'

    name = fields.Char(string='Name', required=True)
    hire_date = fields.Date(string='Hire Date', default=fields.date.today())
    student_id = fields.Many2one('school.student', string='Student')
    class_id = fields.Integer(string='Class', related='student_id.class_id')
    subject_id = fields.Many2many('exam.sub', string='Subjects')
