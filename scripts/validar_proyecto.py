"""Valida integridad, requisitos, secuencia histórica, contenido y enlaces propios."""
import argparse
import base64
import hashlib
import json
import re
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile
from comun import ROOT, XLSX, ahora, sha, json_out
from auditar_enlaces import auditar
from preparar_fuentes import TextoHTML

OBLIGATORIOS=['AGENTS.md','README.md','requirements.txt','.gitignore','fuentes/procedencia.md','fuentes/manifiesto.json','wiki/index.md','wiki/objetivos.md','wiki/fuentes.md','wiki/diccionario_datos.md','wiki/indicadores.md','wiki/hallazgos.md','wiki/consulta_negocio.md','wiki/revision_calidad.md','wiki/respuestas_paso_6.md','wiki/log.md','prompts/prompt_inicial.md','prompts/prompt_mejorado.md','prompts/justificacion_mejoras.md','docs/decisiones_metodologicas.md','docs/mapa_trazabilidad.md','docs/revision_humana.md','docs/matriz_cumplimiento.md','docs/comparacion_ingestas.md','evidencias/primera_ingesta/estado.json','evidencias/consulta_y_verificaciones/respuesta_inicial.md','evidencias/consulta_y_verificaciones/contraste/verificaciones.json','evidencias/segunda_ingesta/despues/estado.json','evidencias/segunda_ingesta/comparacion/comparacion.json','evidencias/revision/enlaces_antes.json','evidencias/revision/enlaces_corregidos.json']

def validar(out):
    json_out(out,{'inicio':ahora(),'estado':'Validación en ejecución, resultado pendiente','cumple':None})
    checks=[]
    def add(nombre,ok,detalle):
        checks.append({'comprobacion':nombre,'cumple':bool(ok),'detalle':detalle})
    faltan=[p for p in OBLIGATORIOS if not (ROOT/p).is_file() or (ROOT/p).stat().st_size==0]
    add('Archivos obligatorios presentes y no vacíos',not faltan,faltan)
    folders=['fuentes','wiki','prompts','scripts','docs','evidencias/primera_ingesta','evidencias/consulta_y_verificaciones','evidencias/segunda_ingesta','evidencias/revision']
    add('Componentes poblados',all((ROOT/p).is_dir() and any((ROOT/p).iterdir()) for p in folders),folders)
    manifest=json.loads((ROOT/'fuentes/manifiesto.json').read_text(encoding='utf-8'))
    integrity=[]
    for e in manifest['archivos']:
        p=ROOT/e['ruta']
        ok=p.exists() and sha(p)==e['sha256']
        if ok and 'git_blob_sha1' in e:
            raw=p.read_bytes()
            ok=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==e['git_blob_sha1']
        integrity.append({'ruta':e['ruta'],'coincide':ok})
    add('SHA-256 y blobs Git de fuentes preservadas',all(e['coincide'] for e in integrity),integrity)
    original=Path(manifest['original_path'])
    original_result={'disponible':False,'nota':'El cálculo portable usa fuentes preservadas. El original solo se comprueba si sigue accesible.'}
    if original.is_dir():
        current={p.relative_to(original).as_posix():sha(p) for p in original.rglob('*') if p.is_file() and '.git' not in p.relative_to(original).parts}
        original_result={'disponible':True,'coincide':current==manifest['original_state'],'archivos':list(current),'alcance':'Archivos de trabajo fuera de .git. Solo se ejecutaron lecturas; no se hizo fetch en repositorio original.'}
        add('Original de proyecto-emacruz intacto',current==manifest['original_state'],original_result)
    else:
        add('Copias portables disponibles sin original',all((ROOT/e['ruta']).exists() for e in manifest['archivos']),original_result)
    snapshots=[]
    for folder in ['primera_ingesta','segunda_ingesta/antes','segunda_ingesta/despues']:
        m=json.loads((ROOT/'evidencias'/folder/'estado.json').read_text(encoding='utf-8'))
        path=ROOT/m['archivo']
        valid=sha(path)==m['sha256_zip']
        with ZipFile(path) as z:
            valid=valid and set(z.namelist())==set(m['archivos']) and all(hashlib.sha256(z.read(p)).hexdigest()==h for p,h in m['archivos'].items())
        snapshots.append({'etapa':folder,'fecha':m['ejecutado'],'cumple':valid,'archivos':set(m['archivos'])})
    target='fuentes/referencia_remota/web/data/frecuencias.json'
    query=json.loads((ROOT/'evidencias/consulta_y_verificaciones/lectura_y_afirmaciones.json').read_text(encoding='utf-8'))
    incorporation=json.loads((ROOT/'evidencias/segunda_ingesta/incorporacion.json').read_text(encoding='utf-8'))
    dates=[snapshots[0]['fecha'],query['ejecutado'],snapshots[1]['fecha'],incorporation['ejecutado'],snapshots[2]['fecha']]
    sequence=all(datetime.fromisoformat(a)<=datetime.fromisoformat(b) for a,b in zip(dates,dates[1:]))
    add('ZIP y hashes íntegros',all(s['cumple'] for s in snapshots),[{k:v for k,v in s.items() if k!='archivos'} for s in snapshots])
    add('Dos ingestas distintas y orden real',sequence and target not in snapshots[0]['archivos'] and target not in snapshots[1]['archivos'] and target in snapshots[2]['archivos'],{'fechas_ordenadas':dates,'json_ausente_primera':target not in snapshots[0]['archivos'],'json_presente_segunda':target in snapshots[2]['archivos']})
    add('Consulta leyó primero índice',query['orden_lectura'][0]['ruta']=='wiki/index.md',query['orden_lectura'])
    verify=json.loads((ROOT/'evidencias/consulta_y_verificaciones/contraste/verificaciones.json').read_text(encoding='utf-8'))
    add('Tres afirmaciones contrastadas',len(verify['verificaciones'])>=3 and verify['coinciden_todas'],[{k:c[k] for k in ['id','estado','observado']} for c in verify['verificaciones']])
    comparison=json.loads((ROOT/'evidencias/segunda_ingesta/comparacion/comparacion.json').read_text(encoding='utf-8'))
    add('Comparación Excel JSON ejecutada',comparison['coincide'] and comparison['comparaciones_de_valores_incluida_fila']==399,{'comparaciones':comparison['comparaciones_de_valores_incluida_fila'],'diferencias':comparison['diferencias']})
    a=json.loads((ROOT/'evidencias/primera_ingesta/calculo_v1/analisis.json').read_text(encoding='utf-8'))
    b=json.loads((ROOT/'evidencias/segunda_ingesta/calculo/analisis.json').read_text(encoding='utf-8'))
    same={k:a[k]==b[k] for k in ['excel_sha256','regla','numerador','total_evaluables','ids_cumplen','faltantes']}
    add('Resultados consistentes entre ingestas',all(same.values()),same)
    html=TextoHTML()
    html.feed((ROOT/'fuentes/consigna/Tarea_wiki_IA_proyecto_BI.html').read_text(encoding='utf-8-sig'))
    quote=' '.join(''.join(html.quote).split())
    prompt=(ROOT/'prompts/prompt_inicial.md').read_text(encoding='utf-8')
    add('Prompt docente íntegro y campos originales',quote in prompt and all(t in quote for t in ['[nombre]','[objetivos]','[evidencias]','[pregunta de negocio]']),{'comparacion':'Bloque de cita HTML normalizando solo espacios de presentación','caracteres':len(quote)})
    step=(ROOT/'wiki/respuestas_paso_6.md').read_text(encoding='utf-8')
    add('Cinco preguntas y pasos priorizados desarrollados',all(f'## {i}.' in step for i in range(1,6)) and all(t in step for t in ['Responsable propuesto','Insumo necesario','Producto verificable','Criterio de finalización']),{'preguntas':len(re.findall(r'^## [1-5]\.',step,re.M))})
    matrix=(ROOT/'docs/matriz_cumplimiento.md').read_text(encoding='utf-8')
    add('Ocho criterios con estado sin nota asignada',all(f'| {i}.' in matrix for i in range(1,9)) and 'no calificaciones obtenidas' in matrix,{'criterios':len(re.findall(r'^\| [1-8]\.',matrix,re.M))})
    md=[p for folder in ['wiki','docs','prompts'] for p in (ROOT/folder).glob('*.md')]+[ROOT/'README.md',ROOT/'AGENTS.md',ROOT/'fuentes/procedencia.md']
    incomplete=[p.relative_to(ROOT).as_posix() for p in md if len(p.read_text(encoding='utf-8').split())<40 or re.search(r'\b(?:TODO|Lorem ipsum)\b',p.read_text(encoding='utf-8'))]
    add('Markdown desarrollado sin relleno o archivos vacíos',not incomplete,incomplete)
    human=(ROOT/'docs/revision_humana.md').read_text(encoding='utf-8')
    add('Aprobación humana explícitamente pendiente','No se ha recibido aprobación' in human and 'Estado actual: **pendiente**' in human,{'estado':'Pendiente, sin firmas o aprobaciones inventadas'})
    prohibited=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.suffix.lower() in ('.docx','.pdf') and p.is_file()]
    git_local=(ROOT/'.git').exists()
    git_root=None
    git_ok=True
    if git_local:
        run=subprocess.run(['git','-c',f'safe.directory={ROOT.as_posix()}','rev-parse','--show-toplevel'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        git_root=run.stdout.strip()
        git_ok=run.returncode==0 and Path(git_root).resolve()==ROOT.resolve() and (ROOT/'.git').is_dir()
    nested=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('.git') if p!=ROOT/'.git']
    add('Git independiente autorizado, sin repositorios anidados ni informe Word/PDF',git_ok and not nested and not prohibited,{'git_local':git_local,'raiz_git':git_root,'anidados':nested,'word_pdf':prohibited,'publicacion':'Etapa privada autorizada por el usuario el 05/11/2026. Este control no afirma que exista publicación remota.'})
    errors=[]
    for p in (ROOT/'scripts').glob('*.py'):
        try:
            compile(p.read_text(encoding='utf-8'),str(p),'exec')
        except SyntaxError as e:
            errors.append(str(e))
    add('Sintaxis de todos los scripts Python',not errors,errors)
    for folder in ['diferencias_desde_primera','diferencias_desde_antes']:
        m=json.loads((ROOT/'evidencias/segunda_ingesta'/folder/'cambios.json').read_text(encoding='utf-8'))
        add('Diferencias reales '+folder,bool(m['creados']) and bool(m['modificados']) and bool(m['cambios_enlaces']),{'creados':len(m['creados']),'modificados':len(m['modificados']),'paginas_con_enlaces':len(m['cambios_enlaces'])})
    links=auditar()
    add('Enlaces locales y páginas wiki accesibles',links['cumple'],links)
    result={'ejecutado':ahora(),'python':sys.version,'checks':checks,'total':len(checks),'aprobadas':sum(c['cumple'] for c in checks),'cumple':all(c['cumple'] for c in checks),'limite':'Controles automáticos y revisión IA de contenido. No certifica vigencia o permiso institucional ni aceptación humana.'}
    json_out(out,result)
    print(json.dumps({'comprobaciones':result['total'],'aprobadas':result['aprobadas'],'cumple':result['cumple'],'fallos':[c['comprobacion'] for c in checks if not c['cumple']]},ensure_ascii=True))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True)
    a=p.parse_args()
    out=ROOT/a.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists():
        raise SystemExit('Use salida nueva.')
    if not validar(out)['cumple']:
        raise SystemExit(1)
