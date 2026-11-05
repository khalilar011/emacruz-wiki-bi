"""Audita candidatos Git, fuentes, ZIP y secretos sin mostrar valores sensibles.

La búsqueda es heurística; no acredita licencias ni sustituye revisión humana.
Cada salida es nueva. El repositorio original se lee, nunca se modifica.
"""
import argparse
import base64
import hashlib
import io
import json
import re
import subprocess
import posixpath
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile, is_zipfile

from comun import ROOT, ahora, json_out, sha
from auditar_enlaces import enlaces


def git(*args, input=None):
    run = subprocess.run(
        ['git', '-c', f'safe.directory={ROOT.as_posix()}', *args],
        cwd=ROOT, input=input, capture_output=True, text=True, encoding='utf-8',
    )
    if run.returncode:
        raise RuntimeError(run.stderr.strip())
    return run.stdout


def estado_original(manifest):
    original = Path(manifest['original_path'])
    if not original.is_dir():
        return {'disponible': False, 'archivos': {}}
    return {
        'disponible': True,
        'alcance': 'Todos los archivos, incluidos metadatos Git; solo lecturas.',
        'archivos': {
            p.relative_to(original).as_posix(): sha(p)
            for p in sorted(original.rglob('*')) if p.is_file()
        },
    }


def auditar(out, base_original=None):
    manifest = json.loads((ROOT/'fuentes/manifiesto.json').read_text(encoding='utf-8'))
    paths = sorted(set(git('ls-files', '--cached', '--others', '--exclude-standard', '-z').split('\0')) - {''})
    patterns = {
        'token_github': r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\b',
        'clave_aws': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
        'token_slack': r'\bxox[baprs]-[A-Za-z0-9-]{20,}\b',
        'clave_openai': r'\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}\b',
        'clave_privada': r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
        'credencial_en_url': r'https?://[^\s/:]+:[^\s/@]+@',
        'asignacion_secreto': r'''(?i)\b(?:password|passwd|api_key|access_token|client_secret)\b\s*[=:]\s*["'][^"'\s]{12,}["']''',
    }
    findings, contacts, archives = [], [], []
    count = 0

    def scan(label, raw, depth=0):
        nonlocal count
        count += 1
        if is_zipfile(io.BytesIO(raw)):
            if depth > 5:
                raise ValueError('Profundidad ZIP no revisada: '+label)
            with ZipFile(io.BytesIO(raw)) as z:
                bad = z.testzip()
                if bad:
                    raise ValueError('ZIP dañado: '+label)
                archives.append({'ruta': label, 'entradas': len(z.namelist())})
                for name in z.namelist():
                    if not name.endswith('/'):
                        if '.git' in Path(name).parts:
                            findings.append({'ruta': label+'!'+name, 'tipo': 'git_anidado_en_zip'})
                        scan(label+'!'+name, z.read(name), depth+1)
            return
        try:
            text = raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            findings.append({'ruta': label, 'tipo': 'binario_no_inspeccionado'})
            return
        for kind, pattern in patterns.items():
            for match in re.finditer(pattern, text):
                findings.append({'ruta': label, 'tipo': kind, 'linea': text.count('\n', 0, match.start())+1})
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
        if emails:
            contacts.append({'ruta': label, 'correos_detectados': len(emails)})
        # Los recuperados base64 también se inspeccionan, sin imprimir sus bytes.
        if label.endswith('.json'):
            try:
                value = json.loads(text)
            except ValueError:
                return
            def decode(obj):
                if isinstance(obj, dict):
                    if obj.get('encoding') == 'base64' and isinstance(obj.get('content'), str):
                        scan(label+'!base64', base64.b64decode(obj['content']), depth+1)
                    for child in obj.values():
                        decode(child)
                elif isinstance(obj, list):
                    for child in obj:
                        decode(child)
            decode(value)

    nested = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('.git') if p != ROOT/'.git']
    symlinks, temporary, prohibited = [], [], []
    for relative in paths:
        p = ROOT/relative
        if p.is_symlink():
            symlinks.append(relative)
            continue
        if not p.is_file():
            raise ValueError('Candidato ausente: '+relative)
        if p.suffix.lower() in {'.pyc', '.tmp', '.temp', '.pem', '.key', '.p12', '.pfx'} or p.name.startswith('.env') or '__pycache__' in p.parts:
            temporary.append(relative)
        if p.suffix.lower() in {'.docx', '.pdf'}:
            prohibited.append(relative)
        scan(relative, p.read_bytes())
    integrity = [{'ruta': e['ruta'], 'coincide': (ROOT/e['ruta']).is_file() and sha(ROOT/e['ruta']) == e['sha256']} for e in manifest['archivos']]
    originals = estado_original(manifest)
    same = None
    if base_original:
        before = json.loads(base_original.read_text(encoding='utf-8'))['original']
        same = before['disponible'] and originals['disponible'] and before['archivos'] == originals['archivos']
    ignored_examples = ['.env', '.venv/pyvenv.cfg', 'scripts/__pycache__/prueba.pyc', 'secrets.json', 'archivo.tmp']
    ignored = git('check-ignore', '-z', '--stdin', input='\0'.join(ignored_examples)+'\0').strip('\0').split('\0')
    source_paths = [e['ruta'] for e in manifest['archivos']]
    missing = [p for p in source_paths if p not in paths]
    # Evalúa destinos contra los candidatos, no solo contra el disco local.
    # GitHub distingue mayúsculas/minúsculas y solo muestra lo incluido en Git.
    own_pages = [ROOT/'README.md', ROOT/'AGENTS.md', ROOT/'fuentes/procedencia.md']
    own_pages += [p for folder in ['wiki', 'docs', 'prompts', 'evidencias'] for p in (ROOT/folder).rglob('*.md')]
    missing_links = []
    link_count = 0
    for p in own_pages:
        relative = p.relative_to(ROOT).as_posix()
        for ref in enlaces(p.read_text(encoding='utf-8')):
            if re.match(r'^[a-zA-Z]+:', ref):
                continue
            target = unquote(ref.strip('<>').split('#')[0])
            if not target:
                continue
            link_count += 1
            target = posixpath.normpath(posixpath.join(posixpath.dirname(relative), target))
            if target not in paths and not any(s.startswith(target.rstrip('/')+'/') for s in paths):
                missing_links.append({'origen': relative, 'enlace': ref, 'destino': target})
    result = {
        'ejecutado': ahora(), 'candidatos': len(paths), 'archivos': paths,
        'unidades_inspeccionadas': count, 'archivos_comprimidos': archives,
        'hallazgos_credenciales_o_binarios': findings,
        'correos_heredados_para_revision': contacts,
        'repositorios_anidados': nested, 'enlaces_simbolicos': symlinks,
        'temporales_o_secretos_por_nombre': temporary, 'word_pdf': prohibited,
        'integridad_fuentes': integrity, 'fuentes_excluidas_por_error': missing,
        'enlaces_en_candidatos': {'revisados': link_count, 'destinos_ausentes': missing_links, 'alcance': 'Destinos relativos de Markdown propio en el árbol candidato, distinguiendo mayúsculas y minúsculas. No equivale a comprobar el render remoto o anclas.'},
        'ejemplos_ignorados': ignored, 'original': originals,
        'original_identico_a_base': same,
        'limites': 'Búsqueda heurística con patrones, ZIP/OOXML y base64. Los nombres, rutas locales y metadatos académicos heredados se conservan solo para la entrega privada solicitada. Sin autorización institucional, licencia pública ni examen de imágenes ausentes.',
        'cumple': not any([findings, nested, symlinks, temporary, prohibited, missing, missing_links]) and all(e['coincide'] for e in integrity) and set(ignored)==set(ignored_examples) and (same is not False),
    }
    json_out(out, result)
    print(json.dumps({k: result[k] for k in ['candidatos', 'unidades_inspeccionadas', 'hallazgos_credenciales_o_binarios', 'fuentes_excluidas_por_error', 'original_identico_a_base', 'cumple']}, ensure_ascii=True))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--salida', required=True, type=Path)
    parser.add_argument('--base-original', type=Path)
    args = parser.parse_args()
    out = ROOT/args.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists():
        raise SystemExit('Use una salida nueva.')
    baseline = ROOT/args.base_original if args.base_original else None
    if not auditar(out, baseline)['cumple']:
        raise SystemExit(1)
