# Comparación antes/después de las ingestas

Versiones reales, conservadas sin Git: [primera ingesta](../evidencias/primera_ingesta/estado.json), [antes de segunda](../evidencias/segunda_ingesta/antes/estado.json) y [después de segunda](../evidencias/segunda_ingesta/despues/estado.json). Cada estado es un ZIP de archivos existentes, con fecha real y hashes. El primer ZIP se produjo antes de la consulta, auditoría y lectura del JSON. El estado anterior a la segunda incluye consulta y auditoría ya ejecutadas; permite separar sus cambios de los debidos al JSON.

| Aspecto | Primera ingesta / antes de incorporar JSON | Después de segunda ingesta | Interpretación |
| --- | --- | --- | --- |
| Evidencias analíticas | Excel y README/documentación existentes | Se añaden JSON y exportador fijados al mismo commit | Nueva evidencia técnica, no fuente independiente de negocio |
| Registros y KPI | 21 filas, 6 cumplen, 28,57 % | 21 filas, 6 cumplen, 28,57 % | Se confirma, no se inventa un cambio numérico |
| Fidelidad del JSON | No comprobada, contenido no incorporado | 399 valores contrastados, 0 diferencias y bytes idénticos | Se resuelve incertidumbre sobre exportación de esta versión |
| Faltantes y medianoche | 15 sin Fin, 9 sin Inicio; 4 cruces documentados | Conservados en JSON | No se corrigen horarios en los originales |
| Contexto de otras hojas | Distritos/Servicios/Fuentes documentados | Se confirma que JSON no exporta esas hojas | La wiki preserva contexto fuera del derivado |
| Procedencia interna del JSON | Desconocida antes de leerlo | Sin hash Excel ni fecha de exportación embebidos | Commit y comparación dan trazabilidad externa; mejora futura propuesta |
| Páginas de la wiki | Objetivos, fuentes, diccionario, KPI, hallazgos y log; luego consulta/revisión | Se actualizan fuentes, diccionario, KPI, hallazgos, consulta, revisión, índice y log; se añaden comparación y respuestas del paso 6 | Documentación cambia aunque cifras no cambien |
| Conclusiones operativas | No acreditadas | Siguen no acreditadas | Faltan vigencia, permisos, imágenes/mapas y revisión humana |

Resultados reales de las comparaciones de archivos: [primera → segunda](../evidencias/segunda_ingesta/diferencias_desde_primera/cambios.json) y [antes → después de segunda](../evidencias/segunda_ingesta/diferencias_desde_antes/cambios.json). Cada salida lista creados, modificados, retirados y enlaces agregados/retirados por página. Los parches exactos son [primera → segunda](../evidencias/segunda_ingesta/diferencias_desde_primera/paginas.diff) y [antes → después](../evidencias/segunda_ingesta/diferencias_desde_antes/paginas.diff). Se generaron con [comparar_estados.py](../scripts/comparar_estados.py) sobre archivos de los ZIP, sin reconstruir estados desde la versión final.

Evidencia de datos: [comparación Excel/JSON](../evidencias/segunda_ingesta/comparacion/comparacion.json) y [operación de actualización](../evidencias/segunda_ingesta/actualizacion.json). No hubo contradicciones nuevas entre valores; las diferencias de representación (nombres de campo, 0/1 frente a booleanos, coordenada añadida) se resuelven con el mapa explícito. Los posibles solapamientos heredados quedan pendientes, conservando ambas referencias.

El estado después contiene también documentos preparatorios y scripts de cierre añadidos durante esta etapa; la lista de archivos permite distinguirlos de las páginas analíticas. Los resultados de validación y diff se guardan fuera de los ZIP y se producen después de congelarlos para evitar hashes autorreferentes. El log final añade esos eventos sin alterar el log histórico del ZIP.

[Página de exportación](../wiki/comparacion_exportacion.md) · [Revisión](../wiki/revision_calidad.md) · [Índice](../wiki/index.md)
