"""Ejecuta las comprobaciones completas en una carpeta nueva, sin tocar historia."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from comun import ROOT, ahora, guardar, json_out

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True,type=Path)
    a=p.parse_args()
    out=ROOT/a.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists():
        raise SystemExit('Use una carpeta de salida que no exista.')
    out.mkdir(parents=True)
    json_out(out/'resultado.json',{'inicio':ahora(),'estado':'Ejecución iniciada, resultados pendientes','cumple':None})
    jobs=[('analisis',['analizar.py','--salida',str(a.salida/'analisis')]),('afirmaciones',['verificar_afirmaciones.py','--salida',str(a.salida/'afirmaciones')]),('comparacion',['comparar_excel_json.py','--salida',str(a.salida/'comparacion')]),('reglas',['verificar_reglas.py','--salida',str(a.salida/'reglas.json')]),('proyecto',['validar_proyecto.py','--salida',str(a.salida/'proyecto.json')])]
    result=[]
    for name,args in jobs:
        cmd=[sys.executable,'-X','utf8',str(ROOT/'scripts'/args[0]),*args[1:]]
        start=ahora()
        run=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        guardar(out/(name+'.log'),run.stdout+run.stderr)
        result.append({'control':name,'inicio':start,'fin':ahora(),'comando':cmd,'exit_code':run.returncode})
        print(f'{name}: exit_code={run.returncode}')
        if run.returncode:
            print(run.stdout+run.stderr)
            break
    final={'ejecutado':ahora(),'operaciones':result,'cumple':len(result)==len(jobs) and all(x['exit_code']==0 for x in result),'politica':'Evidencias históricas intactas; carpeta nueva por ejecución. Los contrastes usan las afirmaciones históricas capturadas, no sustituyen validación de nuevas fuentes.'}
    json_out(out/'resultado.json',final)
    if not final['cumple']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
