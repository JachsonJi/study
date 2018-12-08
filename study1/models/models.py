# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class study1(models.Model):
#     _name = 'study1.study1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class course(models.Model):
    _name='course'
    _description='科目表'
    
    name=fields.Char(u'科目',size='100')
    