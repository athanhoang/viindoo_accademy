from odoo import models,fields
    
class EducationStudent(models.Model):
    _name = 'education.student.ethnic'
    _description= 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name')
    country_ids = fields.Many2many('res.country',string="Country")
    description = fields.Html()
    student_ids = fields.Many2many('education.student','ethnic_ids')