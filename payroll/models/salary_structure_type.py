from odoo import models, fields


class SalaryStructureType(models.Model):
    _name = "salary.structure.type"
    _description = "Salary Structure Type"

    name = fields.Char(string="Structure Type Name", required=True)
    code = fields.Char(string="Code")

    country_id = fields.Many2one('res.country', string="Country")
    default_wage_type = fields.Selection([
        ('hourly', 'Hourly'),
        ('monthly', 'Monthly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly')
    ], string="Default Wage Type")

    default_scheduled_pay = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi-annually', 'Semi-Annually'),
        ('annually', 'Annually')
    ], string="Default Scheduled Pay")

    # Removed the Many2one fields
    # default_working_hours_id = fields.Many2one('resource.calendar', string="Default Working Hours")
    # regular_pay_structure_id = fields.Many2one('hr.payroll.structure', string="Regular Pay Structure")
    
    # You can add alternative fields here if needed
    # For example, you might want to replace them with Char fields or other data types
    default_working_hours = fields.Char(string="Default Working Hours")
    regular_pay_structure = fields.Many2one(
        'hr.payroll.structure', 
        string="Regular Pay Structure",
        ondelete='cascade',
        default=lambda self: self._get_default_pay_structure()
    )

    def _get_default_pay_structure(self):
        # Custom logic to fetch default structure if needed
        # For example, you can return a specific structure based on conditions
        return self.env['hr.payroll.structure'].search([('name', '=', 'Default Structure')], limit=1)   # Updated Many2one field to link to UnpaidWorkEntryType model
    default_work_entry_type = fields.Many2one(
        'unpaid.work.entry.type', 
        string="Default Work Entry Type", 
        help="Link to the default work entry type"
    )