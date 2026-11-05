"""Diferencias reales de archivos y enlaces entre instantáneas ZIP con hashes."""
import argparse
import difflib
import hashlib
import json
from zipfile import ZipFile
from comun import ROOT, ahora, sha, guardar, json_out
from auditar_enlaces import enlaces

def comparar(antes,despues,out):
    a=json.loads((ROOT/antes/'estado.json').read_text(encoding='utf-8'))
    b=json.loads((ROOT/despues/'estado.json').read_text(encoding='utf-8'))
    assert sha(ROOT/a['archivo'])==a['sha256_zip']
    assert sha(ROOT/b['archivo'])==b['sha256_zip']
    aa,bb=a['archivos'],b['archivos']
    nuevos=sorted(set(bb)-set(aa))
    retirados=sorted(set(aa)-set(bb))
    cambiados=sorted(p for p in set(aa)&set(bb) if aa[p]!=bb[p])
    diffs=[]
    edges=[]
    with ZipFile(ROOT/a['archivo']) as za,ZipFile(ROOT/b['archivo']) as zb:
        for p in cambiados+nuevos+retirados:
            if not p.endswith('.md'):
                continue
            ta=za.read(p).decode('utf-8') if p in aa else ''
            tb=zb.read(p).decode('utf-8') if p in bb else ''
            diffs.extend(difflib.unified_diff(ta.splitlines(keepends=True),tb.splitlines(keepends=True),fromfile='antes/'+p,tofile='despues/'+p))
            ea,eb=set(enlaces(ta)),set(enlaces(tb))
            if ea!=eb:
                edges.append({'pagina':p,'enlaces_agregados':sorted(eb-ea),'enlaces_retirados':sorted(ea-eb)})
    json_out(out/'cambios.json',{'ejecutado':ahora(),'antes':{'fecha':a['ejecutado'],'manifiesto':str(antes/'estado.json').replace('\\','/'),'zip_sha256':a['sha256_zip']},'despues':{'fecha':b['ejecutado'],'manifiesto':str(despues/'estado.json').replace('\\','/'),'zip_sha256':b['sha256_zip']},'creados':nuevos,'modificados':cambiados,'retirados':retirados,'cambios_enlaces':edges,'nota':'La propia captura registra su asiento de log después del ZIP. Este diff no altera estados históricos.'})
    guardar(out/'paginas.diff',''.join(diffs) or 'Sin diferencias Markdown.\n')
    print(json.dumps({'nuevos':len(nuevos),'modificados':len(cambiados),'retirados':len(retirados),'paginas_con_cambio_enlaces':len(edges)},ensure_ascii=True))

if __name__=='__main__':
    from pathlib import Path
    p=argparse.ArgumentParser()
    p.add_argument('--antes',type=Path,required=True)
    p.add_argument('--despues',type=Path,required=True)
    p.add_argument('--salida',type=Path,required=True)
    a=p.parse_args()
    for path in [a.antes,a.despues,a.salida]:
        (ROOT/path).resolve().relative_to(ROOT.resolve())
    if (ROOT/a.salida).exists() and any((ROOT/a.salida).iterdir()):
        raise SystemExit('Use salida nueva.')
    comparar(a.antes,a.despues,a.salida)
