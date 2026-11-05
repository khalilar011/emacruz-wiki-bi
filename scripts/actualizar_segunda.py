"""Actualiza conocimiento después de la comparación real. No reconstruye ingesta 1."""
import json
from comun import ROOT, ahora, guardar, json_out, log

def anexar(path,texto):
    p=ROOT/path
    guardar(path,p.read_text(encoding='utf-8')+'\n'+texto+'\n')

def main():
    if (ROOT/'evidencias/segunda_ingesta/actualizacion.json').exists():
        raise SystemExit('Actualización ya registrada; no repetir sobre historia.')
    c=json.loads((ROOT/'evidencias/segunda_ingesta/comparacion/comparacion.json').read_text(encoding='utf-8'))
    assert c['coincide']
    changed=[]
    additions={
    'fuentes/procedencia.md':'''## Segunda ingesta: JSON y exportador

Incorporación y consulta de esta sesión en [registro](../evidencias/segunda_ingesta/incorporacion.json). Se preservaron [frecuencias.json](referencia_remota/web/data/frecuencias.json) y [export_web_data.py](referencia_remota/scripts/export_web_data.py), commit 5fba63ec96844fa1373b6c5703fce54430b52de8. Se verificaron base64, blob Git y SHA-256, añadidos al [manifiesto](manifiesto.json).

El exportador declara dependencia del Excel/hoja Frecuencias: renombra once campos, convierte siete banderas a booleanos y añade fila_origen. La [comparación ejecutada](../evidencias/segunda_ingesta/comparacion/comparacion.json) confirma 378 valores originales y 21 coordenadas, sin diferencias y con reproducción idéntica de bytes. Las otras tres hojas no se exportan. La equivalencia no constituye corroboración institucional independiente. El JSON no contiene hash del libro ni fecha de exportación; su anclaje en esta wiki es el commit y la comparación conservada. Permiso de redistribución/vigencia sigue no acreditado.''',
    'wiki/fuentes.md':'''## Versión 2.0: evidencia técnica incorporada

El párrafo que reservaba el JSON describe el estado histórico de la primera ingesta. Ahora se incorporó [JSON original](../fuentes/referencia_remota/web/data/frecuencias.json) y [exportador](../fuentes/referencia_remota/scripts/export_web_data.py) del commit remoto fijado. Se conserva el estado anterior en [instantánea previa](../evidencias/segunda_ingesta/antes/estado.json).

JSON y Excel tienen 21 registros y los mismos IDs/orden. Se contrastaron las 18 variables originales y fila_origen (399 valores en total) sin diferencias. No se omite ninguna columna de Frecuencias, pero Distritos, Servicios y Fuentes no forman parte del JSON. La wiki preserva ese contexto que el derivado no incluye. [Prueba de equivalencia](../evidencias/segunda_ingesta/comparacion/comparacion.json), [mapeo y límites](comparacion_exportacion.md).''',
    'wiki/diccionario_datos.md':'''## Versión 2.0: representación JSON

El [exportador original](../fuentes/referencia_remota/scripts/export_web_data.py) contiene FIELD_MAP y DAY_MAP. Se comparó su mapeo usando AST sin ejecutarlo ni cambiarlo. [Comparador](../scripts/comparar_excel_json.py), [resultado](../evidencias/segunda_ingesta/comparacion/comparacion.json).

| Excel | JSON | Transformación |
| --- | --- | --- |
| ID, Sector publicado, Zona, Delimitación / área, Distritos indicados | id, sector, zona, area, distritos | Texto, espacios de extremos eliminados |
| Días publicados, Feriados, Turno, Inicio, Fin, Nota de revisión | dias_publicados, feriados, turno, inicio, fin, nota_revision | Texto; nulo/vacío se representaría No indicado |
| Lun, Mar, Mié, Jue, Vie, Sáb, Dom | dias.lun/mar/mie/jue/vie/sab/dom | Entero 0/1 → booleano false/true en esta base |
| Coordenada física de fila | fila_origen | Entero de fila original, de 2 a 22 |

Metadatos del contenedor: fuente (nombre del libro), hoja (Frecuencias), total_registros (21), frecuencias (lista). No hay campos de vigencia, fecha de exportación ni hash del Excel. El exportador acepta otras marcas de días y convierte un día nulo a false; la base actual usa exclusivamente enteros 0/1, por lo que esa pérdida potencial no ocurrió en los registros comparados. Si cambia el dominio, debe revisarse el exportador y no convertir desconocido en día negativo por defecto.''',
    'wiki/indicadores.md':'''## Confirmación en segunda ingesta

Regla permanece en versión 1.0. El [recálculo del Excel](../evidencias/segunda_ingesta/calculo/analisis.json) vuelve a obtener 6/21 = 28,57 %. La [equivalencia con el JSON](../evidencias/segunda_ingesta/comparacion/comparacion.json) confirma conservación de las 18 variables utilizadas, incluidas notas nocturnas y faltantes. No cambia población ni numerador y no se suma el JSON como otras 21 observaciones independientes. Esta confirmación técnica no aporta vigencia ni aprobación humana.''',
    'wiki/hallazgos.md':'''## Versión 2.0: qué confirmó la evidencia nueva

**Cálculo/observación técnica:** el [JSON incorporado](../fuentes/referencia_remota/web/data/frecuencias.json) conserva las 21 filas, las ausencias horarias y las notas de medianoche. Hubo 0 diferencias en 399 valores comparados; la proyección coincide byte por byte. [Resultado reproducible](../evidencias/segunda_ingesta/comparacion/comparacion.json).

**Cambio de conocimiento:** en la primera ingesta no se había comprobado si Alerta Ruta conservaba la programación del Excel. Ahora se confirma la fidelidad de esta exportación y la ausencia de las hojas complementarias en el JSON. No se encontraron nuevos hechos operativos ni correcciones a horarios. El KPI, prioridades y limitaciones permanecen iguales. Es una dependencia técnica confirmada, no una segunda fuente independiente de EMACRUZ.

**Pendiente adicional de mantenimiento:** el JSON no embebe fecha de exportación ni hash del Excel; se propone añadirlos en una tarea futura del repositorio original, con autorización. La wiki no modifica ese exportador.''',
    'wiki/consulta_negocio.md':'''## Actualización 2.0 tras la segunda ingesta

El diagnóstico numérico permanece igual. Se confirma que la representación JSON de Alerta Ruta conserva los mismos 21 registros y los faltantes: 0 diferencias en 399 valores, incluidos fila_origen y días booleanos. [Comparación](../evidencias/segunda_ingesta/comparacion/comparacion.json), [exportador fuente](../fuentes/referencia_remota/scripts/export_web_data.py).

Esta nueva evidencia permite afirmar fidelidad de exportación para la versión fijada; no permite afirmar vigencia o validez institucional. Las tres verificaciones originales siguen confirmadas. La decisión de usar o corregir registros continúa pendiente de persona. [Antes/después](../docs/comparacion_ingestas.md).''',
    'wiki/revision_calidad.md':'''## Iteración después de incorporar JSON

Se confirmó mapeo íntegro de Frecuencias, 0 diferencias en la comparación, y se precisó que el JSON no exporta las otras tres hojas ni embebe vigencia/hash del libro. La potencial conversión de días nulos a false pertenece al comportamiento del exportador; no se observó en la base binaria actual. No se atribuye esa posibilidad a filas reales.

El resultado corregido de la auditoría previa fue [0 enlaces rotos en 168 enlaces locales](../evidencias/revision/enlaces_corregidos.json). Los archivos modificados y las diferencias se conservarán junto al estado posterior. Las revisiones finales amplían el control a nuevos documentos y a hashes, estructura, secuencia y reproducción. [Comparación de datos](../evidencias/segunda_ingesta/comparacion/comparacion.json) · [Registro de decisiones](../docs/decisiones_metodologicas.md).''',
    'docs/mapa_trazabilidad.md':'''## Enlaces cerrados después de consulta e iteración

Aplicar herramientas de análisis → [tres verificaciones](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json) → [consulta revisada](../wiki/consulta_negocio.md) → priorizar registros con evidencia. Centralizar/analizar → [JSON y exportador](../wiki/comparacion_exportacion.md) → [399 comparaciones](../evidencias/segunda_ingesta/comparacion/comparacion.json) → conservar exportación fiel sin confundirla con vigencia. Generar información útil → [cinco respuestas y tres pasos](../wiki/respuestas_paso_6.md) → revisión y asignación humana pendientes.'''}
    for path,text in additions.items():
        anexar(path,text)
        changed.append(path)
    guardar('wiki/comparacion_exportacion.md',f'''# Comparación de Excel y representación JSON

Versión 1.0, segunda ingesta real. Evidencias: [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), [JSON](../fuentes/referencia_remota/web/data/frecuencias.json) y [exportador](../fuentes/referencia_remota/scripts/export_web_data.py), commit 5fba63ec96844fa1373b6c5703fce54430b52de8. [Procedencia](../fuentes/procedencia.md).

Ejecución: {c['ejecutado']}. [Comparador Python](../scripts/comparar_excel_json.py) lee el Excel, obtiene mapas del exportador con AST, proyecta registros y contrasta por ID. No ejecuta el exportador ni escribe en la copia fuente. [Resultado completo](../evidencias/segunda_ingesta/comparacion/comparacion.json), [proyección reproducida](../evidencias/segunda_ingesta/comparacion/proyeccion_reproducida.json).

| Control | Resultado observado |
| --- | --- |
| Registros Excel / JSON / total declarado | 21 / 21 / 21 |
| IDs y orden | Mismos IDs F01–F21 y mismo orden; 0 IDs extra o duplicados JSON |
| Variables originales | 18, ninguna columna de Frecuencias omitida |
| Comparaciones | 378 valores de origen + 21 coordenadas fila_origen = 399 |
| Diferencias | 0 |
| Tipos de días | 147 banderas enteras 0/1 comparadas con booleanos JSON de tipo real bool |
| Bytes de la proyección | Idénticos al JSON preservado, SHA-256 `{c['json_sha256']}` |
| Hojas que no exporta | Distritos, Servicios y Fuentes |
| KPI | Recálculo 6/21 = 28,57 %, sin sumar ambas representaciones |

**Relación:** el JSON es una transformación del Excel, no una fuente independiente de horarios. Conserva “No indicado”, la zona faltante de F21 y las notas de cruce de F07–F10. El exportador recorta espacios y representa nulos textuales como No indicado. En esta versión los días están completos en 0/1; el código admite convertir un día nulo a false, riesgo potencial que debe revisarse si cambian datos. No se observó tal caso aquí.

**Conclusión técnica:** se resolvió la incertidumbre sobre fidelidad de esta exportación. No se detectaron contradicciones que requieran escoger una fuente sobre otra. Siguen pendientes transcripción contra imágenes, vigencia, permisos, polígonos y revisión humana. El JSON no embebe fecha de exportación, versión del libro ni su hash. El commit y esta comparación aportan trazabilidad externa para esta wiki.

[Diccionario](diccionario_datos.md) · [Antes/después](../docs/comparacion_ingestas.md) · [Índice](index.md)
''')
    guardar('wiki/respuestas_paso_6.md','''# Respuestas preparatorias del paso 6

Versión 1.0, después de dos ingestas. Material para redactar posteriormente el informe académico separado; no constituye ese informe. Fuente docente: [sección 2.6 del HTML](../fuentes/consigna/Tarea_wiki_IA_proyecto_BI.html). Conclusiones propuestas pendientes de [revisión humana](../docs/revision_humana.md).

## 1. ¿Qué decisión BI puede apoyarse ahora y cuál no?

Se puede priorizar revisión documental de F01–F06 y F13–F21: quince filas carecen de Fin, y nueve de Inicio. La wiki ofrece localización por ID/fila, KPI 6/21 y evidencias comprobadas. También se puede comprobar que esta exportación no introduce diferencias frente al Excel. [Consulta revisada](consulta_negocio.md), [verificaciones](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json), [comparación](../evidencias/segunda_ingesta/comparacion/comparacion.json).

No hay evidencia suficiente para decidir horarios vigentes para ciudadanos, cobertura real, cumplimiento del servicio, acumulación bajo escasez de diésel o predicción. Faltan confirmación institucional, imágenes/polígonos y observaciones operativas. Los objetivos de investigación del [plan existente](../fuentes/referencia_remota/docs/plan-crisp-dm.md) se conservan con ese límite.

## 2. ¿Qué cambió entre ingestas o qué se confirmó?

La primera ingesta conocía el Excel y objetivos, pero no había comprobado la representación del prototipo. La segunda incorporó JSON y exportador fijados por commit. Se confirmó 21/21 registros, 18 variables originales, 399 valores comparados con fila_origen y cero diferencias, incluso bytes idénticos al reproducir la proyección. El KPI permanece 28,57 % y las prioridades no cambian. La nueva conclusión es fidelidad técnica del derivado; no son nuevos horarios ni corroboración independiente. Se documentó que el JSON omite las hojas complementarias y no embebe vigencia/hash del Excel. [Comparación](comparacion_exportacion.md), [estados y diferencias](../docs/comparacion_ingestas.md).

## 3. ¿Qué falta para alcanzar cada resultado esperado?

| Resultado esperado de la wiki | Evidencia producida | Fuente, cálculo o validación que falta |
| --- | --- | --- |
| Inventario centralizado y trazable | [Manifiesto](../fuentes/manifiesto.json), copias y commits | Interlocutor, permiso institucional/licencia y período operativo; no faltan hashes técnicos de los archivos incorporados |
| Calidad de programación cuantificada | [KPI y filtros](indicadores.md), CSV y tres contrastes | Aprobación humana de reglas y recuperación autorizada de horas para mejorar calidad; el cálculo ya se ejecutó |
| Problemáticas localizadas | [Hallazgos](hallazgos.md) por fila | Imágenes originales, mapas/polígonos para solapamientos, zona F21, sector general, feriados y vínculo distrito → frecuencia |
| Herramientas y resultados reproducibles | Scripts, resultados y comparación Excel/JSON | Revisión del código y ejecución por una persona externa para aceptación independiente; no simular esa ejecución |
| Información útil para propuestas de mejora | [Consulta](consulta_negocio.md) y prioridades | Responsable asignado, revisión temática y medición posterior de utilidad con mantenedores/usuarios |
| Investigación de acumulación / comunicación de estados del proyecto original | [Objetivos y límites](objetivos.md) | Series de recolección ejecutada, acumulación medida, restricciones de diésel, estados aprobados y evaluación contra línea base. No calculables desde frecuencias solas |

## 4. Tres siguientes pasos en orden de prioridad

Roles propuestos; ninguna asignación real está confirmada. No se fija una fecha de cierre inventada.

| Prioridad | Responsable propuesto | Insumo necesario | Producto verificable | Criterio de finalización |
| --- | --- | --- | --- | --- |
| 1. Revisar y autorizar evidencia y reglas | Responsable académico/analista BI con interlocutor autorizado de EMACRUZ; asignación pendiente | KPI v1.0, originales, avisos, permisos y consulta | Acta o registro de revisión con alcance/versión/decisión y permisos conocidos | Persona identificada revisa reglas, quince incidencias horarias y vigencia; acepta o rechaza explícitamente cada conclusión y documenta qué sigue no acreditado |
| 2. Completar o aclarar programación y territorio | Mantenedor de datos y responsable cartográfico; asignación pendiente | Horarios autorizados, mapas, sector de avisos generales, zona F21, catálogo distrito/frecuencia, feriados | Nueva versión derivada con trazabilidad por celda e incidencias resueltas o justificadas | Cada incidencia tiene fuente y estado; se recalcula KPI y se contrastan las modificaciones sin cambiar originales, sin exigir artificialmente 100 % |
| 3. Instituir actualización y validación de utilidad | Mantenedor de wiki y revisor académico; asignación pendiente | Nuevas versiones autorizadas, scripts, observaciones de usuarios/mantenedores | Nueva ingesta registrada, exportación comparada, respuesta revisada y registro de utilidad | Cambios de versión generan hashes/estado anterior, comparaciones y auditoría sin enlaces rotos; persona acepta conclusiones y registra utilidad observada. Publicación e informe se tramitan en sus tareas posteriores |

## 5. ¿Cómo se mantendrá actualizada?

Ante un cambio de datos: conservar nueva copia autorizada con fecha de consulta, versión y hash, mantener la anterior y registrar diferencia por ID/campo. Ejecutar `analizar.py`, `verificar_afirmaciones.py`, `comparar_excel_json.py` y la validación integral en carpeta nueva. Actualizar fuentes, diccionario si cambia esquema, indicadores, hallazgos, consulta e índice; añadir operación al log y conservar instantánea real. Un cambio del esquema detiene la lectura hasta ajustar el código explícitamente.

Ante un cambio de definición: nueva versión de regla con justificación, aprobación humana y recálculo comparativo, sin reetiquetar el resultado histórico como si usara la nueva regla. Ante nueva evidencia contradictoria: conservar ambas referencias, explicar alcance y dejar decisión pendiente hasta resolverla. El JSON nunca se contará como fuente independiente. La frecuencia de revisión se propone por evento de cambio y antes de cada uso operativo; no se inventa un calendario institucional.

Las nuevas afirmaciones de una consulta se capturan antes de su verificación. El verificador actual contrasta las tres afirmaciones históricas de esta ejecución: una versión nueva requiere registrar nuevas afirmaciones y conservar las antiguas. [AGENTS](../AGENTS.md), [método](../docs/decisiones_metodologicas.md), [log](log.md), [reproducción](../README.md).

[Índice](index.md)
''')
    guardar('evidencias/primera_ingesta/resumen.md','''# Evidencia de primera ingesta

Primero se incorporaron Excel y objetivos/documentación, se calculó KPI, se generaron páginas y se congeló el estado. [Operación y archivos](operacion.json), [estado con fecha y hashes](estado.json), [ZIP real](estado.zip). La instantánea no contiene JSON ni exportador. [Cálculo vigente de la ingesta](calculo_v1/analisis.json), [inspección íntegra](inspeccion_excel.json).

El resultado `calculo/` es el intento inicial con perfil erróneo de ceros; se conserva como evidencia del error, no como salida válida. La corrección está descrita en [log](../../wiki/log.md). El resumen se añade ahora después de la segunda ingesta; no se atribuye a la fecha de la instantánea ni altera sus bytes.

[Índice](../../wiki/index.md)
''')
    guardar('evidencias/segunda_ingesta/resumen.md','''# Evidencia de segunda ingesta

Nueva evidencia técnica: JSON derivado y exportador original, incorporados después de conservar primera ingesta, responder, verificar y auditar. [Estado antes](antes/estado.json), [incorporación con fecha y hashes](incorporacion.json), [comparación ejecutada](comparacion/comparacion.json), [recálculo Excel](calculo/analisis.json).

Resultado: 21 registros en ambos formatos; 399 valores comparados, cero diferencias y reproducción de bytes idéntica. El KPI permanece 6/21. La evidencia confirma fidelidad de exportación; no acredita vigencia o servicio real. [Página de comparación](../../wiki/comparacion_exportacion.md). Estado posterior y diferencias se enlazan desde [comparación de ingestas](../../docs/comparacion_ingestas.md).

[Índice](../../wiki/index.md)
''')
    guardar('evidencias/consulta_y_verificaciones/resumen.md','''# Evidencia de consulta y tres verificaciones

Se conserva [orden real de lectura y afirmaciones](lectura_y_afirmaciones.json), [respuesta inicial](respuesta_inicial.md), [resultado independiente](contraste/verificaciones.json) y [explicación de las tres comprobaciones](contraste/verificaciones.md). V1: 21 filas; V2: 15 sin Fin; V3: 6/21 e IDs F07–F12. Las tres confirmadas.

[Respuesta revisada](../../wiki/consulta_negocio.md). No se simularon errores para producir correcciones. Los enlaces de la evidencia sí requirieron arreglo durante auditoría, conservada en [primer resultado](../revision/enlaces_antes.json).

[Índice](../../wiki/index.md)
''')
    guardar('wiki/index.md','''# EMACRUZ — índice de conocimiento

Estado: dos ingestas ejecutadas. KPI documental v1.0, 6/21 = 28,57 %. La segunda ingesta confirmó fidelidad del JSON sin cambiar el diagnóstico. Conclusiones y reglas pendientes de revisión humana. Fuentes fijadas por hashes/commit; no se acredita vigencia operativa.

## Páginas de la wiki

- [Objetivos, usuarios y utilidad](objetivos.md)
- [Fuentes y versiones](fuentes.md)
- [Diccionario de datos](diccionario_datos.md)
- [Indicadores y reglas del KPI](indicadores.md)
- [Hallazgos por registro](hallazgos.md)
- [Consulta de negocio revisada](consulta_negocio.md)
- [Comparación de exportación Excel/JSON](comparacion_exportacion.md)
- [Revisión de calidad](revision_calidad.md)
- [Cinco respuestas preparatorias del paso 6](respuestas_paso_6.md)
- [Registro cronológico real](log.md)

## Método y evidencias

- [Reglas del agente](../AGENTS.md) y [README de ejecución](../README.md)
- [Procedencia](../fuentes/procedencia.md) y [manifiesto de integridad](../fuentes/manifiesto.json)
- [Prompt docente](../prompts/prompt_inicial.md), [mejorado](../prompts/prompt_mejorado.md) y [justificación](../prompts/justificacion_mejoras.md)
- [Decisiones metodológicas](../docs/decisiones_metodologicas.md)
- [Mapa objetivo → fuente → indicador → página → decisión](../docs/mapa_trazabilidad.md)
- [Revisión humana y asuntos pendientes](../docs/revision_humana.md)
- [Primera ingesta](../evidencias/primera_ingesta/resumen.md)
- [Consulta y verificaciones](../evidencias/consulta_y_verificaciones/resumen.md)
- [Segunda ingesta](../evidencias/segunda_ingesta/resumen.md)

El informe académico separado y la publicación se realizarán en tareas posteriores. Los archivos de conocimiento actuales son material de trabajo verificable, sin aprobación operativa atribuida a EMACRUZ.
''')
    changed+=['wiki/index.md','wiki/log.md']
    json_out('evidencias/segunda_ingesta/actualizacion.json',{'ejecutado':ahora(),'evidencias_nuevas':['JSON original','exportador original'],'modificados':changed,'creados':['wiki/comparacion_exportacion.md','wiki/respuestas_paso_6.md','evidencias/primera_ingesta/resumen.md','evidencias/segunda_ingesta/resumen.md','evidencias/consulta_y_verificaciones/resumen.md'],'confirmado':'KPI 6/21; faltantes y cruces preservados; 399 comparaciones sin diferencias','cambio_conclusion':'Fidelidad de la exportación ahora comprobada; sin nuevo dato operativo','pendientes':['Revisión humana','Vigencia, imágenes, polígonos y permisos']})
    log('Segunda ingesta: comparación y actualización de conocimiento','Comparación ejecutada: 399 valores, 0 diferencias; proyección idéntica en bytes. Recálculo del Excel: 6/21 (28,57 %). Se actualizaron fuentes, procedencia, diccionario, indicadores, hallazgos, consulta, revisión, mapa e índice; se creó comparación de exportación y respuestas del paso 6. [Archivos y aportes](../evidencias/segunda_ingesta/actualizacion.json). El diagnóstico se mantiene; se añade fidelidad técnica del derivado y omisión de las otras hojas. No hay contradicciones nuevas ni aprobación humana.')
    print('Conocimiento actualizado con segunda evidencia; cinco respuestas y resúmenes guardados.')

if __name__=='__main__':
    main()
