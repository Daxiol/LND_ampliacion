# -*- coding: utf-8 -*-
from odoo import http

# class Alumnado(http.Controller):
#     @http.route('/alumnado/alumnado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alumnado/alumnado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alumnado.listing', {
#             'root': '/alumnado/alumnado',
#             'objects': http.request.env['alumnado.alumnado'].search([]),
#         })

#     @http.route('/alumnado/alumnado/objects/<model("alumnado.alumnado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alumnado.object', {
#             'object': obj
#         })