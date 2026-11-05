"""Copia inicial, hashes y extracción íntegra del texto docente (sin scripts/CSS)."""
import argparse
import base64
import hashlib
import json
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from comun import ROOT, ahora, sha, json_out, guardar, leer_excel, log

class TextoHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.texto = []
        self.quote = []
        self.inquote = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'blockquote':
            self.inquote = True
        if tag in ('p','h1','h2','h3','h4','li','tr','td','th','br') and not self.skip:
            self.texto.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'):
            self.skip -= 1
        if tag == 'blockquote':
            self.inquote = False
        if tag in ('p','h1','h2','h3','h4','li','tr') and not self.skip:
            self.texto.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.texto.append(data)
            if self.inquote:
                self.quote.append(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--original', type=Path, required=True)
    parser.add_argument('--consigna', type=Path, required=True)
    args = parser.parse_args()
    if (ROOT/'fuentes/manifiesto.json').exists():
        raise SystemExit('Fuentes ya preservadas. No se sobrescribe evidencia histórica.')
    inicio = ahora()
    entries = []
    local_state = {}
    for p in sorted(args.original.rglob('*')):
        if p.is_file() and '.git' not in p.relative_to(args.original).parts:
            local_state[p.relative_to(args.original).as_posix()] = sha(p)
    for rel in ['README.md','data/Base_Emacruz_sectores_y_frecuencias.xlsx']:
        src = args.original/rel
        dst = ROOT/'fuentes/originales'/rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        entries.append({'ruta': dst.relative_to(ROOT).as_posix(), 'origen': str(src), 'consulta': ahora(), 'sha256': sha(dst), 'identica_origen': sha(src)==sha(dst), 'tipo': 'copia local', 'version': '29a44d875600d3ddc88fb53bafce80469902ce50'})
    remote = json.loads((ROOT/'evidencias/recuperacion_remota_inicial.json').read_text(encoding='utf-8'))
    tree = json.loads(remote['tree']['content'])
    for rel, content in remote['files'].items():
        dst = ROOT/'fuentes/referencia_remota'/rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        raw = base64.b64decode(content['content'])
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert blob == content['sha'], (rel, 'blob Git no coincide')
        dst.write_bytes(raw)
        entries.append({'ruta': dst.relative_to(ROOT).as_posix(), 'origen': content['display_url'], 'consulta': ahora(), 'sha256': sha(dst), 'git_blob_sha1': blob, 'version': tree['sha'], 'tipo': 'GitHub conector, base64'})
    src = args.consigna
    dst = ROOT/'fuentes/consigna'/src.name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    entries.append({'ruta': dst.relative_to(ROOT).as_posix(), 'origen': str(src), 'consulta': ahora(), 'sha256': sha(dst), 'identica_origen': sha(src)==sha(dst), 'version': '2026-11-03, metadato del HTML', 'tipo': 'consigna docente local'})
    html = TextoHTML()
    html.feed(dst.read_text(encoding='utf-8-sig'))
    texto = '\n'.join(line.strip() for line in ''.join(html.texto).splitlines() if line.strip())
    guardar('fuentes/consigna/texto_completo.txt', texto+'\n')
    prompt = ' '.join(''.join(html.quote).split())
    assert '[nombre]' in prompt and '[pregunta de negocio]' in prompt
    guardar('prompts/prompt_inicial.md', '# Prompt genérico original\n\nTranscripción íntegra del bloque de cita de la sección 3, sin sustituir campos. Se normalizan únicamente los saltos de línea del HTML y los espacios de presentación.\n\nFuente: [HTML docente](../fuentes/consigna/Tarea_wiki_IA_proyecto_BI.html), versión 2026-11-03.\n\n'+prompt+'\n\n[Índice](../wiki/index.md)\n')
    local_excel = ROOT/'fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx'
    raw = local_excel.read_bytes()
    git_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    expected = next(f['sha'] for f in tree['tree'] if f['path']=='data/Base_Emacruz_sectores_y_frecuencias.xlsx')
    assert git_blob == expected, 'Excel local distinto de referencia remota: revisar versiones'
    json_out('fuentes/manifiesto.json', {'inicio': inicio, 'fin': ahora(), 'archivos': entries, 'excel_git_blob_local': git_blob, 'excel_git_blob_remoto': expected, 'original_path': str(args.original), 'original_state': local_state, 'remote_commit': tree['sha']})
    wb = leer_excel()
    json_out('evidencias/primera_ingesta/inspeccion_excel.json', {'ejecutado': ahora(), **wb})
    log('Preservación e inspección de fuentes', 'Se copiaron Excel y README locales sin alterar originales; se recuperó documentación de GitHub fijada por commit. El JSON solo se localizó en el árbol remoto y aún no se incorporó ni analizó. Hashes en [manifiesto](../fuentes/manifiesto.json). HTML leído como [texto completo](../fuentes/consigna/texto_completo.txt); prompt extraído de su sección 3. Se constató copia local antigua y ausencia local de AGENTS/JSON. Se emplea Python 3.14.3 estándar: openpyxl no instalado. El comando exploratorio `py --version` no existe y la enumeración de la carpeta personal fue denegada; no afectan las fuentes recuperadas.')
    print(json.dumps({'hojas': {k: {'columnas': v['columns'], 'registros':len(v['rows']), 'muestra': v['rows'][:3]} for k,v in wb['sheets'].items()}}, ensure_ascii=False, indent=2))

if __name__=='__main__':
    main()
