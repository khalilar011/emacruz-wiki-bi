"""Compara las 18 variables originales y fila_origen usando el mapa del exportador.
No ejecuta ni modifica el exportador original. Proyección independiente y local.
"""
import argparse
import ast
import hashlib
import json
from collections import Counter
from comun import ROOT, XLSX, ahora, sha, json_out, guardar, leer_excel

JSON_FILE=ROOT/'fuentes/referencia_remota/web/data/frecuencias.json'
EXPORTADOR=ROOT/'fuentes/referencia_remota/scripts/export_web_data.py'

def comparar(out):
    wb=leer_excel()
    rows=wb['sheets']['Frecuencias']['rows']
    maps={}
    for node in ast.parse(EXPORTADOR.read_text(encoding='utf-8')).body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ('FIELD_MAP','DAY_MAP'):
                    maps[target.id]=ast.literal_eval(node.value)
    if set(maps)!= {'FIELD_MAP','DAY_MAP'}:
        raise ValueError('Exportador sin mapas reconocidos')
    payload=json.loads(JSON_FILE.read_text(encoding='utf-8'))
    expected=[]
    for r in rows:
        rec={dst:str(r[src]).strip() if r[src] is not None and str(r[src]).strip() else 'No indicado' for src,dst in maps['FIELD_MAP'].items()}
        if any(type(r[src]) is not int or r[src] not in (0,1) for src in maps['DAY_MAP']):
            raise ValueError('Días distintos del dominio 0/1 observado; revisar transformación')
        rec['dias']={dst:bool(r[src]) for src,dst in maps['DAY_MAP'].items()}
        rec['fila_origen']=r['_fila_excel']
        expected.append(rec)
    regenerated={'fuente':XLSX.name,'hoja':'Frecuencias','total_registros':len(expected),'frecuencias':expected}
    got=payload.get('frecuencias',[])
    counts=Counter(r.get('id') for r in got)
    repeated=[k for k,v in counts.items() if v>1]
    by_id={r.get('id'):r for r in got}
    diffs=[]
    comparisons=0
    for exp in expected:
        rec=by_id.get(exp['id'])
        if rec is None:
            diffs.append({'id':exp['id'],'problema':'Falta registro JSON'})
            continue
        if set(rec)!=set(exp):
            diffs.append({'id':exp['id'],'problema':'Claves distintas','esperadas':list(exp),'observadas':list(rec)})
        for key,val in exp.items():
            if key=='dias':
                for day,active in val.items():
                    comparisons+=1
                    actual=rec.get('dias',{}).get(day)
                    if actual!=active or type(actual) is not bool:
                        diffs.append({'id':exp['id'],'campo':'dias.'+day,'excel_transformado':active,'json':actual})
            else:
                comparisons+=1
                if rec.get(key)!=val or type(rec.get(key)) is not type(val):
                    diffs.append({'id':exp['id'],'campo':key,'excel_transformado':val,'json':rec.get(key)})
    extra=sorted(set(by_id)-{r['id'] for r in expected})
    metadata={k:{'esperado':v,'observado':payload.get(k),'coincide':payload.get(k)==v} for k,v in regenerated.items() if k!='frecuencias'}
    bytes_expected=(json.dumps(regenerated,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    guardar(out/'proyeccion_reproducida.json',bytes_expected.decode('utf-8'))
    uncovered=set(wb['sheets']['Frecuencias']['columns'])-set(maps['FIELD_MAP'])-set(maps['DAY_MAP'])
    result={'ejecutado':ahora(),'excel_sha256':sha(XLSX),'json_sha256':sha(JSON_FILE),'exportador_sha256':sha(EXPORTADOR),'registros_excel':len(rows),'registros_json':len(got),'total_declarado_json':payload.get('total_registros'),'ids_duplicados_json':repeated,'ids_extra_json':extra,'comparaciones_de_valores_incluida_fila':comparisons,'variables_originales_comparadas':len(maps['FIELD_MAP'])+len(maps['DAY_MAP']),'valores_originales_comparados':len(expected)*(len(maps['FIELD_MAP'])+len(maps['DAY_MAP'])),'diferencias':diffs,'metadatos_comparados':metadata,'columnas_frecuencias_no_exportadas':sorted(uncovered),'hojas_no_exportadas':[k for k in wb['sheets'] if k!='Frecuencias'],'orden_ids_coincide':[r['id'] for r in expected]==[r.get('id') for r in got],'proyeccion_identica_bytes':bytes_expected==JSON_FILE.read_bytes(),'proyeccion_sha256':hashlib.sha256(bytes_expected).hexdigest(),'limite':'Equivalencia del derivado de esta versión; no valida imágenes, vigencia ni operación. El JSON no aporta fecha de exportación ni hash de Excel embebido.'}
    result['coincide']=not(diffs or repeated or extra or uncovered) and payload==regenerated and result['proyeccion_identica_bytes']
    json_out(out/'comparacion.json',result)
    print(json.dumps({k:result[k] for k in ['registros_excel','registros_json','comparaciones_de_valores_incluida_fila','diferencias','proyeccion_identica_bytes','coincide']},ensure_ascii=True))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True)
    a=p.parse_args()
    out=ROOT/a.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists() and any(out.iterdir()):
        raise SystemExit('Use salida nueva.')
    if not comparar(out)['coincide']:
        raise SystemExit(1)
