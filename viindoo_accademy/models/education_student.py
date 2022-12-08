from odoo import models,fields,api
    
class EducationStudent(models.Model):
    _name = 'education.student'
    _description= 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(readonly=True, compute='_compute_name')
    class_ids = fields.Many2many(comodel_name='education.class', string='Class', relation='class_education_rel',
                                 column1='student_id', column2='class_id')
    class_id = fields.Many2one(comodel_name='education.class')
    active = fields.Boolean(default=True)
    country_id = fields.Many2one('res.country',string="Country")
    ethnic_id = fields.Many2one('education.student.ethnic')
    user_id = fields.Many2one('res.users', string='Student', store=True)
    
    @api.onchange('ethnic_id')
    def _onchange_country(self):
        self.country_id = self.ethnic_id.country_ids[-1:]

    @api.depends("user_id")
    def _compute_name(self):
        for r in self:
            r.name = r.user_id.name