# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (http://www.akretion.com)
# Benoît GUILLOT <benoit.guillot@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    new = fields.Boolean('New product')

    @api.model
    def compute_new_product(self, limit):
        new_products = self.search([('new', '=', True)])
        new_products.write({'new': False})
        new_products = self.search(
            [('shopinvader_bind_ids', '!=', False)],
            limit=limit,
            order='create_date desc')
        new_products.write({'new': True})
