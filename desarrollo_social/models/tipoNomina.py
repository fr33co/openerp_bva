# -*- coding: utf-8 -*-

#import time # Necesario para las funciones de Fecha

from openerp.osv import osv, fields

class tipoNomina(osv.Model):
	_name="becados.tiponomina"

	_columns = {
		'tipo_nomina': fields.char(string = "Tipo de Nómina", size = 150, required = True),
	}
