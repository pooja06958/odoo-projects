# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auth_id = fields.Char("Auth ID")
    auth_token = fields.Char("Auth Token")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        res.update(
            {
            'auth_id':IrDefault.get('res.config.settings', 'auth_id'),
            'auth_token':IrDefault.get('res.config.settings', 'auth_token'),
            }
        )
        return res

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.default'].sudo().set(
            'res.config.settings', 'auth_id', self.auth_id)
        self.env['ir.default'].sudo().set(
            'res.config.settings', 'auth_token', self.auth_token)
        return res
