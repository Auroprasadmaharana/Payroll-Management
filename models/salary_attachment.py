from odoo import models, fields, api
 
class HrSalaryAttachment(models.Model):
    _name = 'hr.salary.attachment'
    _description = 'Salary Attachment'
 
    name = fields.Char(string='Attachment Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    attachment_type_id = fields.Many2one(
    'payroll.other.input.type',
    string='Type',
    required=True,
    help='Specify the type of input such as Legal, Loan, or Other.'
)

    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    document = fields.Binary(string='Document')
    payslip_amount = fields.Monetary(string='Payslip Amount', currency_field='currency_id')
    total_amount = fields.Monetary(string='Total Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id.id)
    allow_negative = fields.Boolean(string='Negative Value Allowed?')
    notes = fields.Text(string='Notes')
# New Status Field
    status = fields.Selection([
        ('new', 'New'),
        ('running', 'Running'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='new')
 
    def action_set_new(self):
        for rec in self:
            rec.status = 'new'
 
    def action_set_running(self):
        for rec in self:
            rec.status = 'running'
 
    def action_set_expired(self):
        for rec in self:
            rec.status = 'expired'
 
    def action_set_cancelled(self):
        for rec in self:
            rec.status = 'cancelled'
 