# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee"

    slip_ids = fields.One2many(
        "hr.payslip", "employee_id", string="Payslips", readonly=True
    )
    payslip_count = fields.Integer(
        compute="_compute_payslip_count",
        groups="payroll.group_payroll_user",
    )

    def _compute_payslip_count(self):
        for employee in self:
            employee.payslip_count = len(employee.slip_ids)

   
    custom_contract_count = fields.Integer(string="Custom Contract Count", compute="_compute_custom_contract_count")

    def _compute_custom_contract_count(self):
        for employee in self:
            employee.custom_contract_count = len(employee.custom_contract_ids)


