# -*- coding: utf-8 -*-
# from odoo import http


# class ViindooAccademy(http.Controller):
#     @http.route('/viindoo_accademy/viindoo_accademy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viindoo_accademy/viindoo_accademy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('viindoo_accademy.listing', {
#             'root': '/viindoo_accademy/viindoo_accademy',
#             'objects': http.request.env['viindoo_accademy.viindoo_accademy'].search([]),
#         })

#     @http.route('/viindoo_accademy/viindoo_accademy/objects/<model("viindoo_accademy.viindoo_accademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viindoo_accademy.object', {
#             'object': obj
#         })
