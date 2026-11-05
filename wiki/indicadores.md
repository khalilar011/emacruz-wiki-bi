# Indicadores de calidad documental

Versión de regla 1.0. Propuesta académica pendiente de aprobación humana. Fuente: [Excel preservado](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), SHA-256 `cbc88d35f868abb898139e0e11f64dc134754a644d90430807ad701cae39b59a`, modificado internamente 2026-10-15T16:29:10Z. No hay período operativo acreditado. Cálculo ejecutado: [analisis.json](../evidencias/primera_ingesta/calculo_v1/analisis.json); implementación: [analizar.py](../scripts/analizar.py).

## KPI principal: porcentaje de registros con programación completa y válida

**Fórmula:** 100 × registros que satisfacen todos los controles / registros evaluables. Resultado real: **6 / 21 × 100 = 28,57 %**. Unidad: porcentaje de filas documentales. Granularidad: una fila de Frecuencias (combinación zona, turno y frecuencia de una imagen). Versión analizada: huella anterior, consulta de esta ejecución; no se etiqueta como cobertura anual o municipal.

**Evaluable:** cada fila no totalmente vacía de Frecuencias después del encabezado. Se incluyen filas con faltantes, ID ausente o repetido en el denominador; solo se excluyen filas totalmente vacías. No se suman Distritos, Servicios o Fuentes a ese total. Si no hay filas, resultado no disponible y nunca 0 % por defecto.

**Información necesaria:** ID informado y único; al menos sector o zona conocido; delimitación/área informada; turno Día o Noche; Días publicados interpretable; las siete banderas de días válidas; Inicio y Fin exactos en formato de 24 horas `HH:MM`. La delimitación textual satisface presencia, pero su precisión territorial se revisa aparte.

**Días válidos:** siete enteros 0/1, al menos uno activo y concordancia exacta con el texto. Se interpretan nombres españoles, listas con comas/y, rangos inclusivos sin vuelta semanal, Diario = lunes a domingo y Solo sábado. El sufijo “y feriados” se separa del patrón semanal. Una expresión desconocida o bandera no binaria falla, sin adivinar su significado. Cero significa día no marcado y nunca faltante.

**Horas válidas:** HH:MM entre 00:00 y 23:59. Fin mayor que Inicio da intervalo del mismo día. Fin menor que Inicio requiere turno Noche y nota “madrugada siguiente”; duración = (fin − inicio) módulo 1440. Inicio igual a fin es ambiguo y no cumple. No se impone una duración óptima inventada ni se deduce la hora de un turno. F07–F10 tienen cruce documentado de 20:00 a 04:00 (480 minutos); F11–F12, 06:00 a 16:00 (600 minutos).

**Ausencias:** nulo, cadena vacía/espacios, No indicado/a/os/as y No indicada en fila son ausencias semánticas, con normalización de mayúsculas/acentos solo para comparar. No se rellenan. Se conservan originales. **Duplicados:** se reportan IDs repetidos y filas de las 18 columnas idénticas, excluyendo únicamente la coordenada añadida. Todos los integrantes de esos grupos fallan el numerador, permanecen en denominador; no se borran ni fusionan. Posibles solapamientos territoriales no se declaran duplicados sin polígonos.

**Filtros disponibles:** sector publicado, zona y turno, con numerador y denominador recalculados por grupo en la salida. Sector A: 6/6 = 100 %; B: 0/9 = 0 %; sin sector: 0/6 = 0 %. Son grupos de registros del archivo, no tasas de servicio de sectores urbanos. Zona y turno se conservan también en CSV para revisar filas.

**Controles complementarios:** 21/21 filas tienen patrón semanal concordante; 15/21 = 71,43 % carecen de Fin y 9/21 = 42,86 % de Inicio; 6 carecen de sector, 1 de zona, 12 de distritos, 20 de información sobre feriados. Hay 0 IDs duplicados y 0 duplicados exactos excedentes. Los 21 registros tienen cero celdas físicamente vacías en las 18 columnas, pero contienen faltantes expresados en texto: presencia física no es completitud semántica.

**Límites:** el KPI solo exige programación semanal ordinaria, no distrito ni feriados porque mide sector **o** zona. Feriados no informados se publican como limitación independiente. Un registro que cumple no se convierte en vigente, geográficamente inequívoco, autorizado u operacionalmente validado. La relación distrito → frecuencia, la vigencia y los posibles solapamientos requieren evidencia adicional. No se mide cobertura real, puntualidad, toneladas, acumulación ni recogidas ejecutadas.

[Detalle por fila](../evidencias/primera_ingesta/calculo_v1/registros_evaluados.csv) · [Hallazgos](hallazgos.md) · [Índice](index.md)

## Confirmación en segunda ingesta

Regla permanece en versión 1.0. El [recálculo del Excel](../evidencias/segunda_ingesta/calculo/analisis.json) vuelve a obtener 6/21 = 28,57 %. La [equivalencia con el JSON](../evidencias/segunda_ingesta/comparacion/comparacion.json) confirma conservación de las 18 variables utilizadas, incluidas notas nocturnas y faltantes. No cambia población ni numerador y no se suma el JSON como otras 21 observaciones independientes. Esta confirmación técnica no aporta vigencia ni aprobación humana.
