from odoo import fields, models
 
 
class UnpaidWorkEntryType(models.Model):
    _name = 'unpaid.work.entry.type'
    _description = 'Unpaid Work Entry Type'
 
    name = fields.Char(string='Name', required=True)
    payroll_code = fields.Char(string='Payroll Code')
    color = fields.Integer(string='Color')
    country_id = fields.Many2one('res.country', string='Country')
    structure_id = fields.Many2one('salary.structure.type', string='Structure Type')
    note = fields.Text(string="Description")
    external_code = fields.Char(string="External Code")
    rounding = fields.Selection([
        ('no_rounding', 'No Rounding'),
        ('half_day', 'Half Day'),
        ('day', 'Day')
    ], string="Rounding")
    time_off = fields.Boolean(string="Time Off?")
    unforeseen_absence = fields.Boolean(string="Unforeseen Absence?")

    # New Many2one field to link to UnpaidWorkEntryType
    default_work_entry_type = fields.Many2one(
        'unpaid.work.entry.type', 
        string="Default Work Entry Type", 
        help="Link to the default work entry type"
    )