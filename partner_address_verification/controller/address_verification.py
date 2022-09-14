import requests
from odoo import http, _
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging
_logger = logging.getLogger(__name__)

class AddressVerification(WebsiteSale):    

    def checkout_form_validate(self, mode, all_form_values, data):
        error, error_message = super().checkout_form_validate(mode, all_form_values, data)
        config_setting_obj = request.env['res.config.settings'].sudo().get_values()
        auth_id = config_setting_obj.get('auth_id', False)
        auth_token = config_setting_obj.get('auth_token', False)
        state_name = request.env['res.country.state'].search([('id', '=', data.get('state_id'))], limit=1).name
        try:
            url = "https://us-street.api.smartystreets.com/street-address?auth-id=%s&auth-token=%s&street=%s&street2=%s&city=%s&state=%s&zipcode=%s"%(auth_id, auth_token, data.get('street'), data.get('street2'), data.get('city'), state_name, data.get('zip'))
            res = requests.get(url)
            
            if res.status_code != 200:
                error["address"] = 'error'
                error_message.append(_('Invalid Address'))
                _logger.info('========Address Validation Failed!!=============%r',res)
            else:
                _logger.info('========Address Validation Successfull!!=============%r',res)
        except Exception as e:
            _logger.info('========Address Validation Failed!!=============%r',e)
        return error, error_message