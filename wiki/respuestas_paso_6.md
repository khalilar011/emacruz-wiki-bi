# Respuestas preparatorias del paso 6

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
| 3. Instituir actualización y validación de utilidad | Mantenedor de wiki y revisor académico; asignación pendiente | Nuevas versiones autorizadas, scripts, observaciones de usuarios/mantenedores | Nueva ingesta registrada, exportación comparada, respuesta revisada y registro de utilidad | Cambios de versión generan hashes/estado anterior, comparaciones y auditoría sin enlaces rotos; persona acepta conclusiones y registra utilidad observada. La [publicación en GitHub](../docs/publicacion_github.md) ya está completada; el informe se elaborará por separado |

## 5. ¿Cómo se mantendrá actualizada?

Ante un cambio de datos: conservar nueva copia autorizada con fecha de consulta, versión y hash, mantener la anterior y registrar diferencia por ID/campo. Ejecutar `analizar.py`, `verificar_afirmaciones.py`, `comparar_excel_json.py` y la validación integral en carpeta nueva. Actualizar fuentes, diccionario si cambia esquema, indicadores, hallazgos, consulta e índice; añadir operación al log y conservar instantánea real. Un cambio del esquema detiene la lectura hasta ajustar el código explícitamente.

Ante un cambio de definición: nueva versión de regla con justificación, aprobación humana y recálculo comparativo, sin reetiquetar el resultado histórico como si usara la nueva regla. Ante nueva evidencia contradictoria: conservar ambas referencias, explicar alcance y dejar decisión pendiente hasta resolverla. El JSON nunca se contará como fuente independiente. La frecuencia de revisión se propone por evento de cambio y antes de cada uso operativo; no se inventa un calendario institucional.

Las nuevas afirmaciones de una consulta se capturan antes de su verificación. El verificador actual contrasta las tres afirmaciones históricas de esta ejecución: una versión nueva requiere registrar nuevas afirmaciones y conservar las antiguas. [AGENTS](../AGENTS.md), [método](../docs/decisiones_metodologicas.md), [log](log.md), [reproducción](../README.md).

[Índice](index.md)
