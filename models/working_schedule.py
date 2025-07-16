# models/working_schedule.py
from odoo import models, fields

class WorkingSchedule(models.Model):
    _inherit = 'resource.calendar'

    description = fields.Text(string='Description')
