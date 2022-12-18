from odoo import models,fields

class EnrollStudents(models.TransientModel):
    _name = 'enroll.students'
    _description = 'Enroll Students'
    
    class_ids = fields.Many2many('education.class', string='Class')
    student_ids = fields.Many2many('education.student', required=True)
    enrollment_date = fields.Datetime(string = "Enrollment Date", required=True)

    def action_enroll_student_apply(self):
        active_model = self.env.context.get('active_model')
        class_ids = self.env[active_model].browse(self.env.context.get('active_ids'))
        vals_list = []
        
        for c in class_ids:
            for s in self.student_ids:
                vals = {
                    'enrollment_date': self.enrollment_date,
                    'class_id': class_ids.id,
                    'student_id': self.student_ids.id               
                }
                vals_list.append(vals)
                self.env['academy.enrollment'].create(vals_list)
            return
