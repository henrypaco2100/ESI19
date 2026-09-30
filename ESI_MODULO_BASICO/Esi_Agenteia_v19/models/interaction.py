# -*- coding: utf-8 -*-
import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from odoo import _, api, fields, models
from odoo.exceptions import UserError


AREA_SELECTION = [
    ('sales', 'Ventas'),
    ('purchase', 'Compras'),
    ('inventory', 'Inventario'),
    ('importation', 'Importación'),
    ('manufacturing', 'Fabricación'),
    ('pos', 'POS'),
    ('accounting', 'Contabilidad'),
]


class EsiAiInteraction(models.Model):
    _name = 'esi.ai.interaction'
    _description = 'Interacción con Agente IA ESI'
    _order = 'create_date desc, id desc'

    name = fields.Char(string='Asunto', required=True, default=lambda self: _('Nueva consulta'))
    area = fields.Selection(AREA_SELECTION, string='Área', required=True, default='sales', index=True)
    prompt = fields.Text(string='Consulta', required=True)
    answer = fields.Text(string='Respuesta', readonly=True, copy=False)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('done', 'Respondida'),
        ('error', 'Error'),
    ], string='Estado', default='draft', required=True, readonly=True, copy=False, index=True)
    user_id = fields.Many2one('res.users', string='Usuario', required=True,
                              default=lambda self: self.env.user, readonly=True, index=True)
    company_id = fields.Many2one('res.company', string='Compañía', required=True,
                                 default=lambda self: self.env.company, readonly=True, index=True)
    model_name = fields.Char(string='Modelo utilizado', readonly=True, copy=False)
    response_id = fields.Char(string='ID de respuesta', readonly=True, copy=False)
    input_tokens = fields.Integer(string='Tokens de entrada', readonly=True, copy=False)
    output_tokens = fields.Integer(string='Tokens de salida', readonly=True, copy=False)
    duration_seconds = fields.Float(string='Duración (s)', digits=(10, 2), readonly=True, copy=False)
    error_message = fields.Text(string='Detalle del error', readonly=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['user_id'] = self.env.user.id
            vals['company_id'] = self.env.company.id
        return super().create(vals_list)

    def write(self, vals):
        if not self.env.su and not self.env.user.has_group('Esi_Agenteia_v19.group_esi_ai_manager'):
            forbidden = {'user_id', 'company_id', 'answer', 'state', 'model_name',
                         'response_id', 'input_tokens', 'output_tokens',
                         'duration_seconds', 'error_message'}
            if forbidden.intersection(vals):
                raise UserError(_('Estos campos los actualiza el agente IA.'))
            if any(rec.state != 'draft' for rec in self):
                raise UserError(_('Solo se pueden editar consultas en borrador.'))
        return super().write(vals)

    def action_reset_draft(self):
        for rec in self:
            if rec.state == 'error':
                rec.sudo().write({'state': 'draft', 'error_message': False})

    def action_ask(self):
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('Solo se puede enviar una consulta en borrador.'))
        if not self.prompt or not self.prompt.strip():
            raise UserError(_('Escriba una consulta antes de enviarla.'))
        if len(self.prompt) > 12000:
            raise UserError(_('La consulta supera el límite de 12.000 caracteres.'))

        params = self.env['ir.config_parameter'].sudo()
        key = params.get_param('esi_agenteia.api_key')
        model = params.get_param('esi_agenteia.model') or 'gpt-5.6-terra'
        try:
            max_tokens = int(params.get_param('esi_agenteia.max_output_tokens') or 1200)
        except (TypeError, ValueError):
            max_tokens = 1200
        max_tokens = max(100, min(max_tokens, 8000))
        if not key:
            raise UserError(_('Configure la clave API en Agente IA > Ajustes.'))

        area_name = dict(AREA_SELECTION).get(self.area, self.area)
        payload = {
            'model': model,
            'instructions': (
                'Eres el asistente empresarial de ESI para el área de %s. '
                'Responde en español con claridad. No afirmes tener acceso a datos de Odoo '
                'ni haber creado o modificado documentos; solo conoces el texto enviado '
                'en esta consulta. Si faltan datos para un cálculo, indícalo.'
            ) % area_name,
            'input': self.prompt,
            'max_output_tokens': max_tokens,
            'store': False,
        }
        request = Request(
            'https://api.openai.com/v1/responses',
            data=json.dumps(payload).encode('utf-8'),
            headers={'Authorization': 'Bearer %s' % key,
                     'Content-Type': 'application/json'},
            method='POST',
        )
        started = time.monotonic()
        try:
            with urlopen(request, timeout=45) as response:
                result = json.load(response)
        except HTTPError as exc:
            # No guardamos el cuerpo remoto para evitar incluir información sensible.
            message = _('La API respondió con HTTP %s. Revise clave, modelo y cuota.') % exc.code
            self.sudo().write({'state': 'error', 'error_message': message,
                               'duration_seconds': time.monotonic() - started})
            return True
        except (URLError, TimeoutError, ValueError) as exc:
            message = _('No se pudo completar la consulta con la API: %s') % type(exc).__name__
            self.sudo().write({'state': 'error', 'error_message': message,
                               'duration_seconds': time.monotonic() - started})
            return True

        parts = []
        for item in result.get('output', []):
            if item.get('type') == 'message':
                for content in item.get('content', []):
                    if content.get('type') == 'output_text':
                        parts.append(content.get('text', ''))
        usage = result.get('usage') or {}
        answer = '\n'.join(parts).strip()
        status = 'done' if answer else 'error'
        self.sudo().write({
            'answer': answer,
            'state': status,
            'error_message': False if answer else _('La API no devolvió texto. Estado: %s') % result.get('status', ''),
            'model_name': result.get('model') or model,
            'response_id': result.get('id') or False,
            'input_tokens': usage.get('input_tokens', 0),
            'output_tokens': usage.get('output_tokens', 0),
            'duration_seconds': time.monotonic() - started,
        })
        return True
