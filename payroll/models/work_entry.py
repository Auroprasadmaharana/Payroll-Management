from odoo import models, fields, api
 
class HrWorkEntryCustom(models.Model):
    _name = 'hr.work.entry.custom'
    _description = 'Custom Work Entry'
 
    name = fields.Char(string='Work Entry Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_from = fields.Datetime(string='Start Time', required=True)
    date_to = fields.Datetime(string='End Time', required=True)
    work_type = fields.Selection([
        ('normal', 'Normal Work'),
        ('overtime', 'Overtime'),
        ('holiday', 'Holiday'),
        ('leave', 'Leave')
    ], string='Type', default='normal')
    notes = fields.Text(string='Notes')
 
    def action_open_custom_work_entry_form(self):
        return {
            'name': 'Create Custom Work Entry',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.work.entry.custom',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_employee_id': self.employee_id.id,
            }
        }
 