from odoo import models,fields, api

class EnrollStudents(models.TransientModel):
    _name = 'enroll.students'
    _description = 'Enroll Students'

    class_ids = fields.Many2many('education.class', string='Class')
    student_ids = fields.Many2many('education.student', string = 'Students')
    enrollment_date = fields.Datetime(string = "Enrollment Date", required=True)
    current_model = fields.Char(compute='_compute_current_model')

    def action_enroll_student_apply(self):
        vals_list = []
        active_model = self.env.context.get('active_model')

        if active_model == 'education.class':
            class_ids = self.env[active_model].browse(self.env.context.get('active_ids'))
            student_ids = self.student_ids
        elif active_model == 'education.student':
            class_ids = self.class_ids
            student_ids = self.env[active_model].browse(self.env.context.get('active_ids'))
        for c in class_ids:
            for s in student_ids:
                vals = {
                    'enrollment_date': self.enrollment_date,
                    'class_id': c.id,
                    'student_id': s.id               
                }
                vals_list.append(vals)
        self.env['academy.enrollment'].create(vals_list)
        return

    @api.depends('class_ids')
    def _compute_current_model(self):
        for r in self:
            r.current_model = self.env.context.get('active_model')     