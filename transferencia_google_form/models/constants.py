# -*- coding: utf-8 -*-
MINSA = '01'
OP = '02'
INSTITUTOS = '03'
HOSPITALES = '04'
DIRIS = '05'
ASESORES = '06'

SELECTION_CATEG_INST = [
    (MINSA, 'Minsa-Central'),
    (OP, 'OP'),
    (INSTITUTOS, 'Institutos'),
    (HOSPITALES, 'Hospitales'),
    (DIRIS, 'Diris'),
    (ASESORES, 'Asesores'),
]

ANEXO_02 = '02'
ANEXO_03 = '03'
ANEXO_04 = '04'
ANEXO_05 = '05'
ANEXO_06 = '06'
ANEXO_07 = '07'
ANEXO_08 = '08'
ANEXO_09 = '09'
ANEXO_10 = '10'
ANEXO_11 = '11'
ANEXO_12 = '12'
ANEXO_13 = '13'

SELECTION_ANEXO = [
    (ANEXO_02, u'Anexo N° 02: Informe para la Transferencia de Gestión'),
    (ANEXO_03, u'Anexo N° 03: Reporte del Estado Situacional de los Sistemas Administrativos'),
    (ANEXO_04, u'Anexo N° 04: Listado de los procesos de contratación en trámite y en ejecución'),
    (ANEXO_05, u'Anexo N° 05: Listado de garantías vigentes a favor de la entidad'),
    (ANEXO_06, u'Anexo N° 06: Relación de bienes inmuebles'),
    (ANEXO_07, u'Anexo N° 07: Relación de proyectos y obras gestionadas durante el periodo ejercido'),
    (ANEXO_08, u'Anexo N° 08: Proyectos y obras exoneradas del Sistema Nacional de Inversión Pública'),
    (ANEXO_09, u'Anexo N° 09: Resumen de expedientes de procesos legales'),
    (ANEXO_10, u'Anexo N° 10: Proceso de implementación del Sistema de Control Interno'),
    (ANEXO_11, u'Anexo N° 11: Informe sobre actividades desarrolladas y resultados por el Equipo de Mejora '
               u'Continua para la implementación de la simplificación administrativa'),
    (ANEXO_12, u'Anexo N° 12: Portal de Transparencia Estándar'),
    (ANEXO_13, u'Anexo N° 13: Acta de Transferencia de Gestión'),
]

TIPODOC_DNI = '01'
TIPODOC_CE = '03'

SELECTION_TIPODOCUMENTO = [
    (TIPODOC_DNI, 'DNI'),
    (TIPODOC_CE, 'Carnet de Extranjería'),
]

PENDIENTE = 'pendiente'
NO_CUMPLE = 'no_cumple'
CUMPLE = 'cumple'
NO_APLICA = 'no_aplica'

SELECTION_STATE_ANEXO = [
    (PENDIENTE, 'Pendiente'),
    (NO_CUMPLE, 'No cumple'),
    (CUMPLE, 'Cumple'),
    (NO_APLICA, 'No aplica'),
]
