from odoo import models, fields
 
class PayrollReport(models.Model):
    _name = 'hr.payroll.report'
    _description = 'Payroll Report'
 
    name = fields.Char(string='Report Name', required=True)
    report_date = fields.Date(string='Report Date')
    total_employees = fields.Integer(string='Total Employees')
    total_wages = fields.Float(string='Total Wages')