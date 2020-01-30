# -*- coding: utf-8 -*-
from odoo import http

# class 24law(http.Controller):
#     @http.route('/24law/24law/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/24law/24law/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('24law.listing', {
#             'root': '/24law/24law',
#             'objects': http.request.env['24law.24law'].search([]),
#         })

#     @http.route('/24law/24law/objects/<model("24law.24law"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('24law.object', {
#             'object': obj
#         })