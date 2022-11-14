from odoo import models,fields

class EducationClass(models.Model):
    _name = 'education.class'
    _inherit = 'education.class'
    
    contry_id = fields.Many2one(comodel_name="res.country", string = "Country")