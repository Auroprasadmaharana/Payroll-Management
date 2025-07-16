from odoo import fields, models, api

class HrContract(models.Model):
    _inherit = "hr.contract"
    _description = "Employee Contract"

    # Basic Info
    name = fields.Char(string='Contract Reference', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    department_id = fields.Many2one('hr.department', string='Department')
    job_title = fields.Char(string='Job Title', related='employee_id.job_title', store=True, readonly=False)

    # Contract Details
    contract_type_id = fields.Many2one('hr.contract.type', string='Contract Type')
    start_date = fields.Date(string='Contract Start Date')
    end_date = fields.Date(string='Contract End Date')

    # Salary & Structure
    struct_id = fields.Many2one("hr.payroll.structure", string="Salary Structure")
    salary_structure_type_id = fields.Many2one('hr.payroll.structure.type', string='Salary Structure Type')
    wage_type = fields.Selection([
        ('fixed', 'Fixed Wage'),
        ('variable', 'Variable Wage'),
    ], string='Wage Type', default='fixed')
    wage = fields.Float(string='Wage (₹)', default=0.0)

    # Schedule
    schedule_pay = fields.Selection([
        ("monthly", "Monthly"),
        ("quarterly", "Quarterly"),
        ("semi-annually", "Semi-annually"),
        ("annually", "Annually"),
        ("weekly", "Weekly"),
        ("bi-weekly", "Bi-weekly"),
        ("bi-monthly", "Bi-monthly"),
    ], string="Scheduled Pay", index=True, default="monthly",
       help="Defines the frequency of the wage payment.")
    resource_calendar_id = fields.Many2one('resource.calendar', required=True, help="Employee's working schedule.")

    # Allowances
    supplementary_allowance = fields.Float(string='Supplementary Allowance', default=0.0)
    driver_salary = fields.Float(string="Driver Salary (₹)", default=0.0)
    hra_percentage = fields.Float(string="HRA Percentage", default=0.0)
    gratuity = fields.Float(string='Gratuity (₹)', default=0.0)

    # Deductions
    tds = fields.Float(string='TDS (₹)', default=0.0)
    provident_fund = fields.Float(string='Provident Fund (₹)', default=0.0)
    voluntary_provident_fund = fields.Float(string='Voluntary Provident Fund (%)', default=0.0)
    medical_insurance = fields.Float(string='Medical Insurance (₹)', default=0.0)
    leave_allowance = fields.Float(string='Leave Allowance (₹)', default=0.0)
    esic_amount = fields.Float(string='ESIC Amount (₹)', default=0.0)

    # Work Type
    part_time = fields.Boolean(string="Part Time")
    standard_calendar = fields.Boolean(string="Standard 40 hours/week")
    part_time_work_entry_type = fields.Char(string="Part Time Work Entry Type")

    # Status
    # state = fields.Selection([
    #     ('new', 'New'),
    #     ('running', 'Running'),
    #     ('expired', 'Expired'),
    #     ('cancelled', 'Cancelled'),
    # ], string='Status', default='new', tracking=True)

    # # Status Actions
    # def action_set_new(self):
    #     self.write({'state': 'new'})

    # def action_set_running(self):
    #     self.write({'state': 'running'})

    # def action_set_expired(self):
    #     self.write({'state': 'expired'})

    # def action_set_cancelled(self):
    #     self.write({'state': 'cancelled'})


    # TDS Calculation
    def calculate_tds(self):
        for contract in self:
            hra = contract.wage * contract.hra_percentage / 100.0
            gross_income = (
                contract.wage +
                contract.driver_salary +
                contract.supplementary_allowance +
                hra
            )
            contract.tds = gross_income * 0.10  # Flat 10%

    def get_all_structures(self):
        structures = self.mapped("struct_id")
        return list(set(structures._get_parent_structure().ids)) if structures else []
    