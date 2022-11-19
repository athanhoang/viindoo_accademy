from odoo import models,fields

class EducationClass(models.Model):
    _name = 'education.class.vip'
    _inherit = ['education.class']
    
    currency_id = fields.Many2one('res.currency',string = "Currency",
                                  default=lambda self: self.env.company.currency_id)
    credit = fields.Monetary(string = 'Credit')
    student_ids = fields.Many2many(comodel_name='education.student',
                                   relation='class_education_vip_rel',column1='class_vip_id', column2='student_id')