from odoo import models,fields,api
from odoo.exceptions import UserError

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
            (' ','Confirmed'),
            ('done','Done'),
            ('cancelled','Canccelled')
            ],
        default='draft')
    books = fields.Char(string="Books")
    student_id = fields.One2many('education.student',"class_id")
    student_ids = fields.Many2many(comodel_name='education.student',relation='class_education_rel',
                                   column1='class_id', column2='student_id')
    students_count = fields.Integer(string="Total student", compute="_count_student", store=True)
    historical_count = fields.Integer(string="Historical Total student", compute="_count_students", store=True)
    company_id = fields.Many2one(comodel_name='res.company',String="Company", default=lambda self: self.env.company)
    start_date = fields.Datetime(string = "Start date")
    end_date = fields.Datetime(string = "End date")
    responsible_id = fields.Many2one('res.users', string='Responsible', store=True)

    _sql_constraints = [('class_name_unique','unique(name)',"The name of Class must be unique")]
    
    @api.depends('student_id')
    def _count_student(self):
        for r in self:
            r.students_count =  len(r.student_id)

    @api.depends('student_ids')            
    def _count_students(self):
        for r in self:
            r.historical_count =  len(r.student_ids)

    @api.constrains('start_date','end_date')            
    def _validate_date(self):
        for r in self:
            if r.start_date and r.end_date and r.start_date > r.end_date:
                raise UserError("End date can't set before Start date")
            


    # def _confirm(self,vals):
    #     self.write({'state': 'confirmed'})
    #
    # def _done(self,vals):
    #     self.write({'state': 'done'})
    #
    # def _cancel(self,vals):
    #     self.write({'state': 'cancelled'})