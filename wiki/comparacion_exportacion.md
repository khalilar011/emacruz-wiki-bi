# Comparación de Excel y representación JSON

Versión 1.0, segunda ingesta real. Evidencias: [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), [JSON](../fuentes/referencia_remota/web/data/frecuencias.json) y [exportador](../fuentes/referencia_remota/scripts/export_web_data.py), commit 5fba63ec96844fa1373b6c5703fce54430b52de8. [Procedencia](../fuentes/procedencia.md).

Ejecución: 2026-11-03T21:15:30-04:00. [Comparador Python](../scripts/comparar_excel_json.py) lee el Excel, obtiene mapas del exportador con AST, proyecta registros y contrasta por ID. No ejecuta el exportador ni escribe en la copia fuente. [Resultado completo](../evidencias/segunda_ingesta/comparacion/comparacion.json), [proyección reproducida](../evidencias/segunda_ingesta/comparacion/proyeccion_reproducida.json).

| Control | Resultado observado |
| --- | --- |
| Registros Excel / JSON / total declarado | 21 / 21 / 21 |
| IDs y orden | Mismos IDs F01–F21 y mismo orden; 0 IDs extra o duplicados JSON |
| Variables originales | 18, ninguna columna de Frecuencias omitida |
| Comparaciones | 378 valores de origen + 21 coordenadas fila_origen = 399 |
| Diferencias | 0 |
| Tipos de días | 147 banderas enteras 0/1 comparadas con booleanos JSON de tipo real bool |
| Bytes de la proyección | Idénticos al JSON preservado, SHA-256 `b4c5f3d2bccffc5e7b530ff27a9fa00c175167ff039b95305815a3d0a7ce298c` |
| Hojas que no exporta | Distritos, Servicios y Fuentes |
| KPI | Recálculo 6/21 = 28,57 %, sin sumar ambas representaciones |

**Relación:** el JSON es una transformación del Excel, no una fuente independiente de horarios. Conserva “No indicado”, la zona faltante de F21 y las notas de cruce de F07–F10. El exportador recorta espacios y representa nulos textuales como No indicado. En esta versión los días están completos en 0/1; el código admite convertir un día nulo a false, riesgo potencial que debe revisarse si cambian datos. No se observó tal caso aquí.

**Conclusión técnica:** se resolvió la incertidumbre sobre fidelidad de esta exportación. No se detectaron contradicciones que requieran escoger una fuente sobre otra. Siguen pendientes transcripción contra imágenes, vigencia, permisos, polígonos y revisión humana. El JSON no embebe fecha de exportación, versión del libro ni su hash. El commit y esta comparación aportan trazabilidad externa para esta wiki.

[Diccionario](diccionario_datos.md) · [Antes/después](../docs/comparacion_ingestas.md) · [Índice](index.md)
