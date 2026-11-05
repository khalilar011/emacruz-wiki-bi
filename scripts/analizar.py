"""KPI documental v1.0. Salidas nuevas por ejecución; originales en solo lectura."""
import argparse
import csv
import io
import re
import unicodedata
from collections import Counter
from comun import ROOT, XLSX, ahora, sha, guardar, json_out, leer_excel

DIAS = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
NOMBRES = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
AUSENTES = {'', 'no indicado','no indicada','no indicados','no indicadas','no indicada en fila'}

def normal(v):
    return ''.join(c for c in unicodedata.normalize('NFD', str(v if v is not None else '').strip().lower()) if not unicodedata.combining(c))

def ausente(v):
    return v is None or normal(v) in AUSENTES

def dias_texto(v):
    s = normal(v)
    if s == 'diario':
        return set(range(7))
    s = s.replace(' y feriados','')
    m = re.fullmatch('('+'|'.join(NOMBRES)+') a ('+'|'.join(NOMBRES)+')',s)
    if m:
        a,b = [NOMBRES.index(x) for x in m.groups()]
        return set(range(a,b+1)) if a<=b else None
    s = s.removeprefix('solo ')
    tokens = re.split(r',\s*| y ',s)
    return {NOMBRES.index(t) for t in tokens} if tokens and all(t in NOMBRES for t in tokens) else None

def minutos(v):
    if not isinstance(v,str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',v.strip()):
        return None
    h,m = map(int,v.strip().split(':'))
    return h*60+m

def calcular():
    wb = leer_excel()
    freq = wb['sheets']['Frecuencias']
    rows = freq['rows']
    ids = Counter(r['ID'] for r in rows)
    payloads = Counter(tuple(r[c] for c in freq['columns']) for r in rows)
    details = []
    for r in rows:
        problemas = []
        if ausente(r['ID']):
            problemas.append('ID ausente')
        if ids[r['ID']]>1:
            problemas.append('ID duplicado')
        if payloads[tuple(r[c] for c in freq['columns'])]>1:
            problemas.append('fila duplicada exacta')
        if ausente(r['Sector publicado']) and ausente(r['Zona']):
            problemas.append('sector y zona ausentes')
        if ausente(r['Delimitación / área']):
            problemas.append('delimitación ausente')
        binary = all(type(r[c]) is int and r[c] in (0,1) for c in DIAS)
        active = {i for i,c in enumerate(DIAS) if r[c]==1} if binary else None
        parsed = dias_texto(r['Días publicados'])
        dias_validos = bool(binary and active and parsed == active)
        if not dias_validos:
            problemas.append('días ausentes, inválidos o discordantes')
        turno = normal(r['Turno'])
        if turno not in ('dia','noche'):
            problemas.append('turno ausente o desconocido')
        ini,fin = minutos(r['Inicio']),minutos(r['Fin'])
        for col, minute in [('Inicio',ini),('Fin',fin)]:
            if ausente(r[col]):
                problemas.append(col+' ausente')
            elif minute is None:
                problemas.append(col+' formato inválido')
        cruce = False
        duracion = None
        if ini is not None and fin is not None:
            if fin < ini:
                cruce = turno=='noche' and 'madrugada siguiente' in normal(r['Nota de revisión'])
                if not cruce:
                    problemas.append('fin anterior sin evidencia de cruce')
            if ini == fin:
                problemas.append('intervalo de duración cero o ambiguo')
            if fin>ini or cruce:
                duracion = (fin-ini)%1440
        details.append({'ID':r['ID'],'fila_excel':r['_fila_excel'],'sector':r['Sector publicado'],'zona':r['Zona'],'turno':r['Turno'],'dias_validos':dias_validos,'cruce_documentado':cruce,'duracion_minutos':duracion,'cumple_kpi':not problemas,'motivos':'; '.join(problemas),'sector_ausente':ausente(r['Sector publicado']),'zona_ausente':ausente(r['Zona']),'distritos_ausentes':ausente(r['Distritos indicados']),'feriados_ausentes':ausente(r['Feriados'])})
    n = len(rows)
    valid = sum(d['cumple_kpi'] for d in details)
    groups = {}
    for campo in ['sector','zona','turno']:
        groups[campo] = {}
        for v in sorted({d[campo] for d in details}):
            subset = [d for d in details if d[campo]==v]
            num = sum(d['cumple_kpi'] for d in subset)
            groups[campo][v] = {'numerador':num,'denominador':len(subset),'porcentaje':100*num/len(subset)}
    missing = {c: {'vacios_fisicos':sum(r[c] is None or str(r[c]).strip()=='' for r in rows), 'ausencias_semanticas':sum(ausente(r[c]) for r in rows)} for c in freq['columns']}
    summary = {'regla':'KPI documental v1.0','excel_sha256':sha(XLSX),'metadatos_excel':wb['metadata'],'hojas':{k:{'registros_no_vacios':len(v['rows']),'columnas':v['columns'],'dimension':v['dimension']} for k,v in wb['sheets'].items()},'total_evaluables':n,'numerador':valid,'porcentaje':100*valid/n if n else None,'ids_cumplen':[d['ID'] for d in details if d['cumple_kpi']],'ids_no_cumplen':[d['ID'] for d in details if not d['cumple_kpi']],'faltantes':missing,'dias_validos':sum(d['dias_validos'] for d in details),'cruces_documentados':sum(d['cruce_documentado'] for d in details),'ids_duplicados':[k for k,c in ids.items() if c>1],'duplicados_exactos_excedentes':sum(c-1 for c in payloads.values()),'filtros':groups}
    return summary,details

def ejecutar(out):
    summary,details = calcular()
    json_out(out/'analisis.json', {'ejecutado':ahora(),**summary})
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=list(details[0]) if details else ['ID'])
    writer.writeheader()
    writer.writerows(details)
    guardar(out/'registros_evaluados.csv',stream.getvalue())
    print(f'KPI = {summary["numerador"]}/{summary["total_evaluables"]} = {summary["porcentaje"]:.6f}%')
    return summary

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',type=str,required=True)
    args=p.parse_args()
    out=ROOT/args.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists() and any(out.iterdir()):
        raise SystemExit('La salida ya contiene evidencia. Use una carpeta nueva.')
    ejecutar(out)
