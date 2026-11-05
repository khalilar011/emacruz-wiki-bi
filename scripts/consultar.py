"""Conserva la respuesta inicial después de leer índice y páginas, antes de verificar."""
import json
from comun import ROOT, ahora, sha, guardar, json_out, log

def main():
    out=ROOT/'evidencias/consulta_y_verificaciones'
    if (out/'respuesta_inicial.md').exists():
        raise SystemExit('Respuesta inicial ya conservada.')
    orden=['wiki/index.md','wiki/objetivos.md','wiki/fuentes.md','wiki/indicadores.md','wiki/hallazgos.md','wiki/diccionario_datos.md']
    reads=[]
    for path in orden:
        contenido=(ROOT/path).read_text(encoding='utf-8')
        reads.append({'ruta':path,'leido':ahora(),'sha256':sha(ROOT/path),'caracteres':len(contenido)})
    s=json.loads((ROOT/'evidencias/primera_ingesta/calculo_v1/analisis.json').read_text(encoding='utf-8'))
    claims={'V1':s['total_evaluables'],'V2':s['faltantes']['Fin']['ausencias_semanticas'],'V3':{'numerador':s['numerador'],'denominador':s['total_evaluables'],'ids':s['ids_cumplen']}}
    json_out(out/'lectura_y_afirmaciones.json',{'ejecutado':ahora(),'orden_lectura':reads,'afirmaciones':claims,'estado':'Inicial, antes de verificación independiente'})
    guardar(out/'respuesta_inicial.md','''# Respuesta inicial de la consulta

Estado: propuesta generada por IA antes del contraste independiente. Fuente/versiones y límites: [wiki de fuentes](../../wiki/fuentes.md). Pregunta: ¿Qué tan completa y consistente es la información disponible sobre días y horarios de recolección por sector o zona, y qué registros requieren revisión antes de utilizarse en Alerta Ruta?

Se consultó primero el índice y luego las páginas pertinentes, según [registro de lectura](lectura_y_afirmaciones.json).

**V1.** La wiki documenta **21 registros evaluables** en Frecuencias, no 21 distritos ni 21 rutas físicas. [Fuentes](../../wiki/fuentes.md), [cálculo](../primera_ingesta/calculo_v1/analisis.json).

**V2.** **15 de 21** registros carecen de Fin: F01–F06 y F13–F21. Nueve (F13–F21) tampoco tienen Inicio; las seis primeras filas no informan sector. [Hallazgos](../../wiki/hallazgos.md), [detalle por fila](../primera_ingesta/calculo_v1/registros_evaluados.csv).

**V3.** Cumplen la regla documental **6/21 = 28,57 %**, F07–F12. Las cuatro franjas 20:00 → 04:00 se aceptan por su nota de madrugada siguiente. Los 21 patrones semanales concuerdan con las banderas. [KPI y alcance](../../wiki/indicadores.md).

Se propone revisar primero horas de F13–F21 y el fin de F01–F06, junto con el sector desconocido. F17/F20 requieren mapas por posibles solapamientos; F21 no permite afirmar Norte/Sur. Incluso F07–F12 carecen de vigencia acreditada y no se aprueban para uso operativo por este cálculo. Faltan feriados en 20 registros y distritos en 12; no se dispone de imágenes para verificar transcripción y límites. [Hallazgos](../../wiki/hallazgos.md), [fuentes originales](../../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx).

La wiki apoya priorizar la revisión documental. No demuestra cobertura real, cumplimiento de recolección, actualidad oficial o acumulación. Conclusiones de negocio pendientes de [revisión humana](../../docs/revision_humana.md). El JSON todavía no se incorporó.

[Índice](../../wiki/index.md)
''')
    log('Consulta inicial desde la wiki','Se leyó primero índice y después objetivos, fuentes, indicadores, hallazgos y diccionario. [Orden y hashes](../evidencias/consulta_y_verificaciones/lectura_y_afirmaciones.json). Se guardó [respuesta inicial](../evidencias/consulta_y_verificaciones/respuesta_inicial.md) con tres afirmaciones derivadas del cálculo real: 21 filas, 15 sin Fin y 6 que cumplen. Todavía no se marca ninguna como contrastada por lectura independiente.')
    print('Respuesta inicial conservada, con trazabilidad de lectura y afirmaciones.')

if __name__=='__main__':
    main()
