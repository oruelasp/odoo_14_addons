# -*- coding: utf-8 -*-

from odoo import api, fields, models


class TransferenciaForm(models.Model):
    _name = 'transferencia.form'
    _description = u'Transferencia de cargo'
    _order = 'marca_temporal'

    lot_number = fields.Char('Número lote')
    marca_temporal = fields.Datetime('Marca Temporal')
    correo = fields.Char('Correo')
    name = fields.Char('Nombres y apellidos')
    dni = fields.Char('DNI')
    municipalidad = fields.Char('Municiplaidad')
    departamento = fields.Char('Departamento')
    provincia = fields.Char('Provincia')
    distrito = fields.Char('Distrito')
    nombre_mercado = fields.Char('Mercado')
    codigo_mercado = fields.Char('Código Mercado')

    f0 = fields.Char('Fotografía del Acta de Visita de supervisión para la verificación en campo')
    f11 = fields.Char('MEDIDA 1')
    f12 = fields.Char('NO MEDIDA 1')
    f21 = fields.Char('MEDIDA 2')
    f22 = fields.Char('NO MEDIDA 2')
    f31 = fields.Char('MEDIDA 3')
    f32 = fields.Char('NO MEDIDA 3')
    f41 = fields.Char('MEDIDA 4')
    f42 = fields.Char('NO MEDIDA 4')
    f51 = fields.Char('MEDIDA 5')

    f52 = fields.Char('NO MEDIDA 5')
    f61 = fields.Char('MEDIDA 6')
    f62 = fields.Char('NO MEDIDA 6')
    f71 = fields.Char('MEDIDA 7')
    f72 = fields.Char('NO MEDIDA 7')
    f81 = fields.Char('MEDIDA 8')
    f82 = fields.Char('NO MEDIDA 8')
    f91 = fields.Char('MEDIDA 9')
    f92 = fields.Char('NO MEDIDA 9')
    f101 = fields.Char('MEDIDA 10')

    f102 = fields.Char('NO MEDIDA 10')
    f111 = fields.Char('MEDIDA 11')
    f112 = fields.Char('NO MEDIDA 11')
    f121 = fields.Char('MEDIDA 12')
    f122 = fields.Char('NO MEDIDA 12')
    f131 = fields.Char('MEDIDA 13')
    f132 = fields.Char('NO MEDIDA 13')
    f141 = fields.Char('MEDIDA 14')
    f142 = fields.Char('NO MEDIDA 14')
    f151 = fields.Char('MEDIDA 15')

    f152 = fields.Char('NO MEDIDA 15')
    f161 = fields.Char('MEDIDA 16')
    f162 = fields.Char('NO MEDIDA 16')
    f171 = fields.Char('MEDIDA 17')
    f172 = fields.Char('NO MEDIDA 17')
    f181 = fields.Char('MEDIDA 18')
    f182 = fields.Char('NO MEDIDA 18')
    f191 = fields.Char('MEDIDA 19')
    f192 = fields.Char('NO MEDIDA 19')
    f201 = fields.Char('MEDIDA 20')
    f202 = fields.Char('NO MEDIDA 20')

    @api.model
    def create(self, vals):
        return super(TransferenciaForm, self).create(vals)
