from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Exam(models.Model):
    _name = 'school.exam'
    _rec_name = 'student_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'School Exam Information'

    student_id = fields.Many2one('school.student', string='Student')
    class_id = fields.Integer(string='Class', related='student_id.class_id')
    exam_subject = fields.Many2one('exam.sub', string='Subject')
    fee = fields.Float(string='Exam Fee')
    officer_id = fields.Many2one('res.partner', string='Exam Officer')

    @api.constrains('fee')
    def exam_fee(self):
        if not self.fee:
            raise ValidationError(_('Enter The Exam Fee Amount'))


class Subject(models.Model):
    _name = 'exam.sub'
    _rec_name = 'subject_id'

    subject_id = fields.Char(string='subject')
    code = fields.Char(string='Code')
