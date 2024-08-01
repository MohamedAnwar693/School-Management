from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import date

class School(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'School Student Information'

    name = fields.Many2one('res.partner', string='Student')
    address = fields.Char(string='Address')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    admin_date = fields.Date(string='Admin Date', default=fields.date.today())
    admin_code = fields.Char(string='Admin Code', copy=False, readonly=False,
                             index=True, default=lambda self: _('New'))
    officer_id = fields.Many2one('res.users', string='Officer', default=lambda self: self.env.user)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], string='State', default='draft')


    @api.model
    def create(self, vals_list):
        if vals_list.get('admin_code', 'New') == 'New':
            vals_list['admin_code'] = self.env['ir.sequence'].next_by_code('school.student.sequence') or 'New'
            result = super(School, self).create(vals_list)
            return result

    @api.onchange('name')
    def onchange_name(self):
        self.address = self.name.street

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    @api.constrains('dob')
    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.dob > today:
                raise ValidationError(_('Invalid date of Birth'))
            if (rec.class_id > 12) or (rec.class_id < 1):
                raise ValidationError(_('Invalid Class'))

    _sql_constraints = [('unique_admin', 'unique(admin_code)', 'This admin code is already exist')]


class ClassStudent(models.Model):
    _name = 'class.student'
    _description = 'Class Student Information'

    name = fields.Char(string='Name')

