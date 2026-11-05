"""Captura inmutable del estado real conservando rutas relativas desde la raíz."""
import argparse
import json
from zipfile import ZipFile, ZIP_DEFLATED
from comun import ROOT, ahora, sha, json_out, log

def capturar(nombre):
    out = ROOT/'evidencias'/nombre
    out.mkdir(parents=True,exist_ok=True)
    archive = out/'estado.zip'
    if archive.exists():
        raise SystemExit('Instantánea ya existente; no se sobrescribe.')
    paths = [p for folder in ['wiki','docs','prompts','scripts','fuentes'] for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    paths += [ROOT/n for n in ['AGENTS.md','README.md','requirements.txt','.gitignore'] if (ROOT/n).exists()]
    entries = {}
    with ZipFile(archive,'w',ZIP_DEFLATED) as z:
        for p in sorted(paths):
            rel = p.relative_to(ROOT).as_posix()
            z.write(p, rel)
            entries[rel] = sha(p)
    meta = {'ejecutado':ahora(),'archivo':archive.relative_to(ROOT).as_posix(),'sha256_zip':sha(archive),'archivos':entries,'alcance':'Fuentes, wiki, prompts, docs, scripts y archivos raíz existentes en este instante. Evidencias externas no se duplican. Rutas internas desde raíz.'}
    json_out(out/'estado.json',meta)
    log('Instantánea '+nombre, f'Se conservó el estado real de {len(entries)} archivos en [{nombre}](../evidencias/{nombre}/estado.json), con ZIP y hashes. El propio asiento se añade después de la captura para evitar autorreferencia.')
    print(json.dumps({'instantanea':nombre,'archivos':len(entries),'fecha':meta['ejecutado']},ensure_ascii=True))

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('nombre')
    a=p.parse_args()
    (ROOT/'evidencias'/a.nombre).resolve().relative_to((ROOT/'evidencias').resolve())
    capturar(a.nombre)
