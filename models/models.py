# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Matter(models.Model):
    _name = 'matter.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
    matter_no = fields.Char(string="Matter Number",
                            default=lambda self: _('New'), requires=False, readonly=True,)
    client_id = fields.Many2one(comodel_name="res.partner", string="Client", required=False, )
    open_date = fields.Date(string="Openning Date", required=False, )
    type_matter = fields.Selection(string="Type", selection=[('civil', 'Civil'), ('criminal', 'Criminal'), ], required=False, )
    category_matter = fields.Selection(string="Category", selection=[('first', 'First'), ('second', 'Second')])
    lawyer = fields.Many2one(comodel_name="res.user", string="Lawyer Assigned")

    @api.model
    def create(self, vals):
        if vals.get('matter_no', _('New')) == _('New'):
            vals['matter_no'] = self.env['ir.sequence'].next_by_code('increment_matter') or _('New')
        result = super(Matter, self).create(vals)
        return result

class Evidence(models.Model):
    _name = 'evidence.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()

class Actions(models.Model):
    _name = 'actions.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()
class Courts(models.Model):
    _name = 'courts.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()

class Judge(models.Model):
    _name = 'judge.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()


class Documents(models.Model):
    _name = 'documents.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()


class Expenses(models.Model):
    _name = 'expenses.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()


class Task(models.Model):
    _name = 'task.24law'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char()


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    is_lawyer = fields.Boolean(string="Lawyer", default=True)







# class 24law(models.Model):
#     _name = '24law.24law'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100