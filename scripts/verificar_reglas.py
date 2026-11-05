"""Casos sintéticos mínimos de reglas; NO son datos ni mediciones de EMACRUZ."""
import argparse
from comun import ROOT, ahora, json_out
from analizar import ausente, dias_texto, minutos

def ejecutar(out):
    casos=[
        ('cero binario no es ausencia', not ausente(0)),
        ('None sí es ausencia', ausente(None)),
        ('marcador textual sí es ausencia', ausente('No indicada en fila')),
        ('día específico conserva sábado', dias_texto('Solo sábado')=={5}),
        ('rango inclusivo martes a sábado', dias_texto('Martes a sábado')=={1,2,3,4,5}),
        ('diario equivale a siete días', dias_texto('Diario')==set(range(7))),
        ('texto desconocido no se adivina', dias_texto('ocasionalmente') is None),
        ('00:00 hora válida', minutos('00:00')==0),
        ('24:00 hora inválida', minutos('24:00') is None),
        ('minuto 60 inválido', minutos('06:60') is None),
    ]
    result={'ejecutado':ahora(),'naturaleza':'Casos sintéticos para verificar reglas de software; no observaciones de negocio.','casos':[{'descripcion':k,'cumple':v} for k,v in casos],'cumple':all(v for _,v in casos)}
    json_out(out,result)
    print(f'Controles de reglas: {sum(v for _,v in casos)}/{len(casos)}')
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--salida',required=True)
    a=p.parse_args()
    out=ROOT/a.salida
    out.resolve().relative_to(ROOT.resolve())
    if out.exists():
        raise SystemExit('Use salida nueva.')
    if not ejecutar(out)['cumple']:
        raise SystemExit(1)
