"""Incorpora bytes remotos después de primera ingesta, consulta y auditoría reales."""
import base64
import hashlib
import json
from comun import ROOT, ahora, sha, json_out, log

def main():
    manifest_path=ROOT/'fuentes/manifiesto.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    src=ROOT/'evidencias/recuperacion_remota_segunda.json'
    before=ROOT/'evidencias/segunda_ingesta/antes/estado.json'
    assert before.exists() and (ROOT/'evidencias/primera_ingesta/estado.zip').exists()
    assert (ROOT/'evidencias/consulta_y_verificaciones/contraste/verificaciones.json').exists()
    audit=json.loads((ROOT/'evidencias/revision/enlaces_corregidos.json').read_text(encoding='utf-8'))
    assert audit['cumple']
    pack=json.loads(src.read_text(encoding='utf-8'))
    tree=json.loads(json.loads((ROOT/'evidencias/recuperacion_remota_inicial.json').read_text(encoding='utf-8'))['tree']['content'])
    entries=[]
    for path,v in pack['files'].items():
        dst=ROOT/'fuentes/referencia_remota'/path
        if dst.exists():
            raise SystemExit('Segunda evidencia ya existe, no sobrescribir.')
        raw=base64.b64decode(v['content'])
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        expected=next(n['sha'] for n in tree['tree'] if n['path']==path)
        assert blob==v['sha']==expected
        dst.parent.mkdir(parents=True,exist_ok=True)
        dst.write_bytes(raw)
        entries.append({'ruta':dst.relative_to(ROOT).as_posix(),'origen':v['display_url'],'consulta':ahora(),'sha256':sha(dst),'git_blob_sha1':blob,'version':pack['commit'],'tipo':'GitHub conector, base64','ingesta':2,'relacion':'JSON derivado de Excel; exportador documenta transformación'})
    manifest['archivos'].extend(entries)
    manifest['segunda_incorporacion']=ahora()
    json_out(manifest_path,manifest)
    json_out('evidencias/segunda_ingesta/incorporacion.json',{'ejecutado':ahora(),'fuentes_nuevas':entries,'estado_previo':json.loads(before.read_text(encoding='utf-8'))['sha256_zip'],'aporte':'Nueva evidencia técnica de la representación de Frecuencias en Alerta Ruta, no fuente independiente de negocio','incertidumbres':['Vigencia y permiso institucional continúan sin acreditar','JSON sin hash del Excel ni fecha de exportación embebidos']})
    log('Segunda ingesta: incorporación auténtica de evidencia','Después del estado previo, consulta y auditoría, se incorporaron JSON y exportador originales del commit fijado, comprobando blobs. [Incorporación](../evidencias/segunda_ingesta/incorporacion.json). Estas evidencias no existían en la primera instantánea y no se usaron en su cálculo. Se compararán las 18 variables de Frecuencias y fila_origen, sin alterar el proyecto original.')
    print('JSON y exportador preservados y registrados. Comparación pendiente de ejecutar.')

if __name__=='__main__':
    main()
