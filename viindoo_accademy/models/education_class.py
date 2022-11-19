from odoo import models,fields

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True, string='Title')
    description = fields.Html('Description')
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('draft','Draft'),
            ('confirmed','Confirmed'),
            ('done','Done'),
            ('cancelled','Canccelled')
            ],
        default='draft')
    books = fields.Char(string="Books")
    student_ids = fields.Many2many(comodel_name='education.student',relation='class_education_rel',
                                   column1='class_id', column2='student_id')

    def _confirm(self,vals):
        self.write({'state': 'confirmed'})
    
    def _done(self,vals):
        self.write({'state': 'done'})
    
    def _cancel(self,vals):
        self.write({'state': 'cancelled'})