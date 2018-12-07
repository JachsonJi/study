# -*- coding: utf-8 -*-
from odoo import http

# class Study1(http.Controller):
#     @http.route('/study1/study1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/study1/study1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('study1.listing', {
#             'root': '/study1/study1',
#             'objects': http.request.env['study1.study1'].search([]),
#         })

#     @http.route('/study1/study1/objects/<model("study1.study1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('study1.object', {
#             'object': obj
#         })