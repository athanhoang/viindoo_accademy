from odoo import models,fields
    
class Enrollment(models.Model):
    _name = 'academy.enrollment'
    _description= 'Enrollment of student & class'

    name = fields.Char(String = "Code",default=id)
    enrollment_date = fields.Datetime(string = "Enrollment Date", required=True)
    class_id = fields.Many2one('education.class', string='Class', required=True)
    student_id = fields.Many2one('education.student',required=True)