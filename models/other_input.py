class OtherInput(models.Model):
    _name = 'other.input'
    _description = 'Other Input'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    amount = fields.Float(string='Amount')
