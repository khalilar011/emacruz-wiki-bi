"""Auditoría de Markdown propio. Copias originales externas se excluyen explícitamente."""
import argparse
import hashlib
import json
import re
from urllib.parse import unquote
from comun import ROOT, ahora, json_out

def enlaces(text):
    text=re.sub(r'```.*?```','',text,flags=re.S)
    return re.findall(r'\[[^\]]*\]\(([^\n]*?)\)',text)

def auditar():
    pages=[ROOT/x for x in ['README.md','AGENTS.md']]
    pages += [ROOT/'fuentes/procedencia.md']
    pages += [p for folder in ['wiki','docs','prompts'] for p in (ROOT/folder).glob('*.md')]
    pages += list((ROOT/'evidencias').rglob('*.md'))
    pages=[p for p in pages if p.exists()]
    broken=[]
    graph={p.resolve():[] for p in pages}
    count=0
    for p in pages:
        for ref in enlaces(p.read_text(encoding='utf-8')):
            if re.match(r'^[a-zA-Z]+:',ref):
                continue
            target=unquote(ref.strip('<>').split('#')[0])
            if not target:
                continue
            q=(p.parent/target).resolve()
            count+=1
            if not q.exists():
                broken.append({'origen':p.relative_to(ROOT).as_posix(),'enlace':ref})
            if q in graph:
                graph[p.resolve()].append(q)
    root=(ROOT/'wiki/index.md').resolve()
    visited=set()
    stack=[root]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph.get(node,[]))
    orphans=[p.relative_to(ROOT).as_posix() for p in pages if p.parent==ROOT/'wiki' and p.resolve() not in visited]
    hashes={}
    for p in pages:
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        hashes.setdefault(h,[]).append(p.relative_to(ROOT).as_posix())
    duplicates=[ps for ps in hashes.values() if len(ps)>1]
    return {'ejecutado':ahora(),'alcance':'Markdown propio en raíz/wiki/docs/prompts/evidencias y fuentes/procedencia; se excluyen copias originales, enlaces web y archivos dentro de ZIP. Comprueba destinos de archivo, no anclas HTML externas.','paginas':len(pages),'enlaces_locales':count,'rotos':broken,'aisladas_wiki':orphans,'duplicados_exactos':duplicates,'cumple':not broken and not orphans and not duplicates}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True)
    args=p.parse_args()
    target=ROOT/args.salida
    target.resolve().relative_to(ROOT.resolve())
    if target.exists():
        raise SystemExit('Use salida nueva.')
    result=auditar()
    json_out(target,result)
    print(json.dumps(result,ensure_ascii=True))
    if not result['cumple']:
        raise SystemExit(1)
