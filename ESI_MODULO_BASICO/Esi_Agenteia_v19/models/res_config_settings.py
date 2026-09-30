from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    esi_ai_api_key = fields.Char(
        string='Clave API de OpenAI',
        config_parameter='esi_agenteia.api_key',
        groups='base.group_system',
    )
    esi_ai_model = fields.Char(
        string='Modelo',
        config_parameter='esi_agenteia.model',
        default='gpt-5.6-terra',
        groups='base.group_system',
    )
    esi_ai_max_output_tokens = fields.Integer(
        string='Máximo de tokens de respuesta',
        config_parameter='esi_agenteia.max_output_tokens',
        default=1200,
        groups='base.group_system',
    )
