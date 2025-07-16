from odoo import models, fields

class OtherInputType(models.Model):
    _name = 'payroll.other.input.type'
    _description = 'Other Input Type'

    name = fields.Char(string='Input Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)

    # ✅ New fields as per your request
    available_in_attachments = fields.Boolean(string='Available in Attachments')
    is_quantity = fields.Boolean(string='Is Quantity?')
    no_end_date = fields.Boolean(string='No End Date by Default')
# ✅ Correct Many2one field pointing to salary rule
    availability_in_structure_id = fields.Many2one(
        'hr.salary.rule',
        string='Availability in Structure',
        help='Link this input type to a specific salary rule'
    )

    salary_rule_ids = fields.Many2many(
        'hr.salary.rule',
        string='Salary Rules',
        help="Select the salary rules that will be associated with this input type."
    )