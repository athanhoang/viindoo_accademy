from odoo import models,fields
from datetime import datetime
class EnrollStudents(models.Model):
    _name = 'enroll.students'
    _description = 'Enroll Students'
    
    enrollment_date = fields.Datetime(string = "Enrollment Date",default=datetime.today())
    class_ids = fields.Many2many('education.class', string='Class')
    student_ids = fields.Many2many('education.student')
    