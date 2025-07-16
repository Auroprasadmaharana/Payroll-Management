from odoo import models, api

class WorkEntryTypeSetup(models.TransientModel):
    _name = 'work.entry.type.setup'
    _description = 'Setup Work Entry Types'

    def create_default_work_entry_types(self):
        WorkEntryType = self.env['hr.work.entry.type']
        company_country = self.env.company.country_id.id

        types_to_create = [
            {
                'name': 'Sick Leave',
                'code': 'SICK',
                'is_leave': True,
                'color': 3,
                'unforeseen': False,
                'rounding': 0.01,
            },
            {
                'name': 'Personal Leave',
                'code': 'PERS',
                'is_leave': True,
                'color': 5,
                'unforeseen': False,
                'rounding': 0.01,
            },
            {
                'name': 'Vacancy',
                'code': 'VACAN',
                'is_leave': False,
                'color': 6,
                'unforeseen': False,
                'rounding': 0.01,
            },
        ]

        for entry in types_to_create:
            if not WorkEntryType.search([('code', '=', entry['code'])], limit=1):
                entry['country_id'] = company_country
                WorkEntryType.create(entry)
