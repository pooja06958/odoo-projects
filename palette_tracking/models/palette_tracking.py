from odoo import models, fields, api

class PaletteTracking(models.Model):

    _name = 'palette.tracking'
    _description = "Palette Tracking"

    def _get_balance(self):
        for obj in self:
            obj.balance = obj.palette_count_plus - obj.palette_count_minus

    picking_id = fields.Many2one('stock.picking', string='Picking', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    license_plate = fields.Char(string='License Plate', translate=True)
    picking_partner_id = fields.Many2one('res.partner', string='Picking Partner', related='picking_id.partner_id')
    picking_date_done = fields.Datetime(string='Picking Done Date', related='picking_id.date_done')
    palette_count_plus = fields.Integer(string='Palette Count Plus')
    palette_count_minus = fields.Integer(string='Palette Count Minus')
    balance = fields.Integer(string='Balance', compute="_get_balance")
