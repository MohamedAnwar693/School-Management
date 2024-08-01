from odoo import api, fields, models, _


class SchoolItems(models.Model):
    _name = 'school.items'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'School Item Information'
    # _rec_name = 'class_id'

    student_id = fields.Many2many('school.student', string='Student', help="Student")
    class_id = fields.Integer(string='Class', related='student_id.class_id')
    division = fields.Char(string='Division', related='student_id.division')
    admin_date = fields.Date(string='Admin Date', related='student_id.admin_date')
    product_ids = fields.Many2many('product.product', string='Items')

    # @api.onchange('class_id')
    # def change_class(self):
    #     student = self.env['school.student'].search([('class_id', '=', self.class_id.id)])
    #     print("student", student)
    #     val = self.env['school.student'].browse(self.class_id)
    #     print("val", val)
    #     self.student_id = student
