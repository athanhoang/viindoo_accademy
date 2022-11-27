from odoo import models,fields,api
    
class EducationStudent(models.Model):
    _name = 'education.student'
    _description= 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Name')
    class_ids = fields.Many2many(comodel_name='education.class', string='Class', relation='class_education_rel',
                                 column1='student_id', column2='class_id')
    class_id = fields.Many2one(comodel_name="education.class")
    active = fields.Boolean(default=True)
    country_ids = fields.Many2many('res.country',string="Country",  )
    ethnic_ids = fields.Many2many('education.student.ethnic','ethnic_ids')
    
    @api.onchange('ethnic_ids')
    def _onchange_country(self):
        if self.ethnic_ids:
            self.country_ids = self.ethnic_ids.country_ids