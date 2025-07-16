from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrPayrollStructure(models.Model):
    _name = "hr.payroll.structure"
    _description = "Salary Structure"

    @api.model
    def _get_parent(self):
        return self.env.ref("hr_payroll.structure_base", False)

    name = fields.Char(required=True)
    code = fields.Char(string="Reference")
    structure_type_id = fields.Many2one(
        "salary.structure.type", string="Salary Structure Type", required=True
    )

    template = fields.Selection([
        ('payslip', 'Payslip'),
        ('bonus', 'Bonus')
    ], string="Template", default="payslip")

    use_worked_day_lines = fields.Boolean("Use Worked Day Lines", default=True)
    payslip_name = fields.Char("Payslip Name")
    hide_basic_on_pdf = fields.Boolean("Hide Basic On Pdf")
    country_id = fields.Many2one("res.country", string="Country")
    year_to_date_computation = fields.Boolean("Year to Date Computation")
    default_scheduled_pay = fields.Selection([
        ('monthly', 'Monthly'),
        ('bi-weekly', 'Bi-Weekly'),
        ('weekly', 'Weekly')
    ], string="Default Scheduled Pay", default="monthly")

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        copy=False,
        default=lambda self: self.env.company,
    )
    note = fields.Text(string="Description")

    parent_id = fields.Many2one(
        "hr.payroll.structure", string="Parent", default=_get_parent
    )
    children_ids = fields.One2many(
        "hr.payroll.structure", "parent_id", string="Children", copy=True
    )

    rule_ids = fields.Many2many(
        "hr.salary.rule",
        "hr_structure_salary_rule_rel",
        "struct_id",
        "rule_id",
        string="Salary Rules",
    )

    unpaid_work_entry_ids = fields.Many2many(
    'unpaid.work.entry.type',
    string='Unpaid Work Entry Types'
)
 
    other_input_type_ids = fields.Many2many(
        'payroll.other.input.type',
        'structure_other_input_rel',
        'structure_id',
        'input_type_id',
        string="Other Input Types"
    )
 

    require_code = fields.Boolean(
        "Require code",
        compute="_compute_require_code",
        default=lambda self: self._compute_require_code(),
    )

    def _compute_require_code(self):
        require = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("payroll.require_code_and_category")
        )
        self.require_code = require
        return require

    @api.constrains("parent_id")
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_("You cannot create a recursive salary structure."))

    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {}, code=_("%s (copy)") % self.code)
        return super().copy(default)

    def get_all_rules(self):
        all_rules = []
        for struct in self:
            all_rules += struct.rule_ids._recursive_search_of_rules()
        return all_rules

    def _get_parent_structure(self):
        parent = self.mapped("parent_id")
        if parent:
            parent = parent._get_parent_structure()
        return parent + self
