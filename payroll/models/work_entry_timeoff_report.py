from odoo import models, fields, api
 
class WorkEntryTimeoffReport(models.Model):
    _name = 'work.entry.timeoff.report'
    _description = 'Time Off to Report'
 
    name = fields.Char(string='Description', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_from = fields.Date(string='Start Date', required=True)
    date_to = fields.Date(string='End Date', required=True)
    reason = fields.Text(string='Reason for Leave')
    approved = fields.Selection([
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('refused', 'Refused')
    ], default='to_approve', string='Status', tracking=True)
 
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments")
 
    # New fields
    department_id = fields.Many2one('hr.department', string='Department')
    time_off_type_id = fields.Many2one(
    'unpaid.work.entry.type',
    string='Time Off Type',
    domain=[('time_off', '=', True)],
    required=True
)

    requested_duration = fields.Float(string='Requested (Days/Hours)', compute='_compute_requested_duration', store=True)
    payslip_state = fields.Selection([
    ('next', 'To compute in next payslip'),
    ('current', 'Computed in current payslip'),
    ('defer', 'To defer to next payslip')
], string='Payslip State', default='next')
 
 
    @api.depends('date_from', 'date_to')
    def _compute_requested_duration(self):
        for record in self:
            if record.date_from and record.date_to:
                start_date = fields.Date.from_string(record.date_from)
                end_date = fields.Date.from_string(record.date_to)
                duration = (end_date - start_date).days
                record.requested_duration = duration  # You can modify the logic for hours if needed
 
    def action_approve(self):
        self.write({'approved': 'approved'})
 
    def action_refuse(self):
        self.write({'approved': 'refused'})