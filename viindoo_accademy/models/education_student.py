from odoo import models,fields
    
class EducationStudent(models.Model):
    _name = 'education.student'
    _description= 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name')
    class_ids = fields.Many2many(comodel_name='education.class', string='Class', relation='class_education_rel',
                                 column1='student_id', column2='class_id')
    active = fields.Boolean(default=True)