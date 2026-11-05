# Fuentes disponibles

Versión 1.0. [Procedencia, permisos y hashes](../fuentes/procedencia.md). El Excel es fuente tabular primaria de esta implementación; README/CRISP-DM son evidencias de objetivos, no observaciones de recolección.

| Hoja del [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) | Rango observado | Filas no vacías sin encabezado | Uso |
| --- | --- | --- | --- |
| Frecuencias | A1:R22 | 21 | Unidad: combinación zona, turno y frecuencia transcrita de una imagen, según Fuentes!A12:B12. Base del KPI. |
| Distritos | A1:C17 | 16 | Catálogo: quince identificadores numéricos y DMI. No contiene un enlace completo distrito → frecuencia. |
| Servicios | A1:C12 | 11 | Catálogo de servicios; no son once recojos ni once horarios. |
| Fuentes | A1:E16 | 13 | Siete filas IMG01–IMG07 (2–8) y seis filas metodológicas (11–16). Las filas 9–10 están vacías. |

Observación reproducida en [inspección íntegra](../evidencias/primera_ingesta/inspeccion_excel.json) y [cálculo corregido](../evidencias/primera_ingesta/calculo_v1/analisis.json), mediante [lector OOXML](../scripts/comun.py). No hay fórmulas en las celdas leídas: el lector las rechaza si aparecen. Las horas son cadenas `HH:MM`, las banderas de días son enteros y Distrito mezcla números con DMI. No se convirtió el libro ni se completaron ausencias.

El archivo tiene fecha interna de modificación 2026-10-15T16:29:10Z; eso no establece un período operativo. La hoja Fuentes marca “No indicada” en la vigencia de las siete imágenes. Las imágenes originales no están presentes y no hay clave `Fuente ID` por fila de Frecuencias. La atribución detallada imagen → registro queda limitada al texto metodológico y no se inventa una clave foránea.

La documentación de [datos](../fuentes/referencia_remota/data/README.md), [registro de fuentes](../fuentes/referencia_remota/docs/fuentes-datos.md) e [historia SCRUM-22](../fuentes/referencia_remota/docs/historias/SCRUM-22.md) exige conservar ausencias y reconocer vigencia no acreditada. El JSON localizado remotamente se reserva para una segunda ingesta y aún no aporta resultados a esta página.

[Diccionario](diccionario_datos.md) · [Indicadores](indicadores.md) · [Índice](index.md)

## Versión 2.0: evidencia técnica incorporada

El párrafo que reservaba el JSON describe el estado histórico de la primera ingesta. Ahora se incorporó [JSON original](../fuentes/referencia_remota/web/data/frecuencias.json) y [exportador](../fuentes/referencia_remota/scripts/export_web_data.py) del commit remoto fijado. Se conserva el estado anterior en [instantánea previa](../evidencias/segunda_ingesta/antes/estado.json).

JSON y Excel tienen 21 registros y los mismos IDs/orden. Se contrastaron las 18 variables originales y fila_origen (399 valores en total) sin diferencias. No se omite ninguna columna de Frecuencias, pero Distritos, Servicios y Fuentes no forman parte del JSON. La wiki preserva ese contexto que el derivado no incluye. [Prueba de equivalencia](../evidencias/segunda_ingesta/comparacion/comparacion.json), [mapeo y límites](comparacion_exportacion.md).
