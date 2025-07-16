# Copyright (C) 2022 Trevi Software (https://trevi.et)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

# from odoo import fields, models


# class HrLeaveType(models.Model):
#     _inherit = "hr.leave.type"

#     code = fields.Char(string="Payroll Code")

# Copyright (C) 2022 Trevi Software (https://trevi.et)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HrLeaveType(models.Model):
    _inherit = "hr.leave.type"

    code = fields.Char(string="Payroll Code")
    generate_work_entry = fields.Boolean(string="Generate Work Entry", default=False)
    work_entry_type_id = fields.Many2one(
        'hr.work.entry.type',
        string='Work Entry Type',
        help="Defines the work entry type that will be used when generating work entries for this time off."
    )



