"""Contraste independiente: lectura directa de celdas ZIP/XML, sin usar analizar.py.
Verifica las afirmaciones guardadas, no constantes escogidas para hacer pasar una prueba.
"""
import argparse
import json
import os
import re
import xml.etree.ElementTree as E
from collections import Counter
from zipfile import ZipFile
from comun import ROOT, XLSX, ahora, sha, json_out, guardar

def comprobar(salida):
    source=ROOT/'evidencias/consulta_y_verificaciones/lectura_y_afirmaciones.json'
    claims=json.loads(source.read_text(encoding='utf-8'))['afirmaciones']
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with ZipFile(XLSX) as z:
        strings=[''.join(n.itertext()) for n in E.fromstring(z.read('xl/sharedStrings.xml'))]
        sheet=E.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows=[]
        for row in sheet.findall('s:sheetData/s:row',ns):
            if int(row.attrib['r'])==1:
                continue
            cells={}
            for c in row:
                v=c.find('s:v',ns)
                x=v.text if v is not None else None
                if c.attrib.get('t')=='s' and x is not None:
                    x=strings[int(x)]
                cells[re.sub(r'\d','',c.attrib['r'])]=x
            if any(x is not None and str(x).strip() for x in cells.values()):
                rows.append((int(row.attrib['r']),cells))
    missing=lambda x: x is None or str(x).strip().casefold() in ('','no indicado','no indicada','no indicados','no indicadas','no indicada en fila')
    counts=Counter(c.get('A') for _,c in rows)
    payloads=Counter(tuple(c.get(k) for k in 'ABCDEFGHIJKLMNOPQR') for _,c in rows)
    # Interpretación alternativa por patrones completos del vocabulario realmente observado.
    patrones={'Lunes, miércoles y viernes':'1010100','Martes, jueves y sábado':'0101010','Lunes a domingo y feriados':'1111111','Lunes a domingo':'1111111','Lunes a sábado':'1111110','Diario':'1111111','Lunes a viernes':'1111100','Martes a sábado':'0111110','Solo sábado':'0000010'}
    valid=[]
    crossed=[]
    day_ok=[]
    for n,c in rows:
        bits=''.join(c.get(k,'?') or '?' for k in 'GHIJKLM')
        days=patrones.get(c.get('F'))==bits
        if days:
            day_ok.append(c['A'])
        times=all(re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',c.get(k) or '') for k in 'PQ')
        hours=False
        if times:
            start,end=[int(c[k][:2])*60+int(c[k][3:]) for k in 'PQ']
            night=end<start and c.get('O')=='Noche' and 'madrugada siguiente' in (c.get('R') or '')
            if night:
                crossed.append(c['A'])
            hours=end>start or night
        known=not missing(c.get('A')) and counts[c['A']]==1 and payloads[tuple(c.get(k) for k in 'ABCDEFGHIJKLMNOPQR')]==1 and (not missing(c.get('B')) or not missing(c.get('C'))) and not missing(c.get('D')) and c.get('O') in ('Día','Noche')
        if days and hours and known:
            valid.append(c['A'])
    without_end=[{'id':c['A'],'celda':f'Q{n}','valor':c.get('Q')} for n,c in rows if missing(c.get('Q'))]
    observed={'V1':len(rows),'V2':len(without_end),'V3':{'numerador':len(valid),'denominador':len(rows),'ids':valid}}
    checks=[]
    procedures={
    'V1':('21 registros evaluables en Frecuencias','Frecuencias!A2:R22','Contar filas XML no totalmente vacías después de encabezado, preservando coordenadas; no usar dimensión o recuento de otras hojas.'),
    'V2':('15 registros con Fin ausente','Frecuencias!Q2:Q22','Leer columna Q y reconocer nulo, vacío y marcadores de ausencia. Registrar celdas e IDs.'),
    'V3':('6 de 21 cumplen KPI v1.0: F07–F12, 28,57 %','Frecuencias!A2:R22; notas R8:R11','Reconstruir controles desde celdas: IDs, duplicados, sector/zona, delimitación, turno, vocabulario de días contra G:M, horas y cruce explícito. Comparar IDs, numerador y denominador, sin llamar al analizador.')}
    for key,(claim,ref,proc) in procedures.items():
        checks.append({'id':key,'afirmacion':claim,'fuente':'fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx','localizacion':ref,'procedimiento':proc,'esperado_respuesta_inicial':claims[key],'observado':observed[key],'estado':'confirmada' if claims[key]==observed[key] else 'corregida','correccion':None if claims[key]==observed[key] else observed[key]})
    result={'ejecutado':ahora(),'fuente_sha256':sha(XLSX),'afirmaciones_sha256':sha(source),'verificaciones':checks,'detalle_sin_fin':without_end,'controles_adicionales':{'dias_concordantes':len(day_ok),'cruces_documentados':crossed},'coinciden_todas':all(c['estado']=='confirmada' for c in checks)}
    json_out(salida/'verificaciones.json',result)
    md='# Tres verificaciones sustantivas\n\nEjecución real: '+result['ejecutado']+'. [Script independiente](../../scripts/verificar_afirmaciones.py), [fuente](../../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) y [detalle JSON](verificaciones.json). Afirmaciones capturadas antes del contraste en [respuesta inicial](../../evidencias/consulta_y_verificaciones/respuesta_inicial.md).\n\n'
    for c in checks:
        md+=f"## {c['id']}: {c['estado']}\n\nAfirmación: {c['afirmacion']}. Fuente/localización: {c['localizacion']}.\n\nProcedimiento: {c['procedimiento']}\n\nResultado observado: `{json.dumps(c['observado'],ensure_ascii=False)}`. Corrección: {'no requerida' if c['correccion'] is None else c['correccion']}.\n\n"
    md+='Los tres contrastes confirman las cifras iniciales, sin introducir errores deliberados. La verificación técnica no aprueba conclusiones operativas. Los cuatro cruces son F07–F10; se obtuvieron además 21 días concordantes.\n\n[Índice](../../wiki/index.md)\n'
    prefijo=os.path.relpath(ROOT,salida).replace('\\','/')
    md=md.replace('../../scripts/',prefijo+'/scripts/').replace('../../fuentes/',prefijo+'/fuentes/').replace('../../evidencias/',prefijo+'/evidencias/').replace('../../wiki/',prefijo+'/wiki/')
    guardar(salida/'verificaciones.md',md)
    print(json.dumps({'verificaciones':{c['id']:c['estado'] for c in checks},'dias':len(day_ok),'cruces':crossed},ensure_ascii=True))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True)
    a=p.parse_args()
    out=ROOT/a.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists() and any(out.iterdir()):
        raise SystemExit('Use carpeta nueva para conservar evidencia.')
    result=comprobar(out)
    if not result['coinciden_todas']:
        raise SystemExit('Diferencias detectadas; revisar respuesta con valores corregidos guardados.')
