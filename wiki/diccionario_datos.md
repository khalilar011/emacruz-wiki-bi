# Diccionario de datos observados

Versión 1.0. Fuente: [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), campos y tipos extraídos en [inspección](../evidencias/primera_ingesta/inspeccion_excel.json). Significados descriptivos de la transcripción y decisiones analíticas de la wiki; no equivalen a definiciones institucionales aprobadas.

## Frecuencias

| Campo | Significado y control |
| --- | --- |
| ID | Identificador textual de la fila de frecuencia (F01–F21). No es una ruta ni un servicio ejecutado. Debe ser único. |
| Sector publicado | Etiqueta A (Oeste), B (Este) o No indicado. No se imputa desde zona. |
| Zona | Nombre publicado de zona: Norte, Sur, Centro, Casco Viejo o No indicada en fila. No representa un polígono completo. |
| Delimitación / área | Texto de anillos, área o subzona de mapa. La presencia de texto no demuestra delimitación geográfica suficiente. |
| Distritos indicados | Lista textual de DM o referencia industrial. No indicada en doce registros. No es clave normalizada. |
| Días publicados | Texto de días o intervalo, incluyendo Diario y Solo sábado. Se contrasta con las siete banderas. |
| Lun | Bandera de Lun: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Mar | Bandera de Mar: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Mié | Bandera de Mié: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Jue | Bandera de Jue: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Vie | Bandera de Vie: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Sáb | Bandera de Sáb: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Dom | Bandera de Dom: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia. |
| Feriados | Sí o No indicado observado. No indicado no significa No. Se controla aparte del KPI semanal. |
| Turno | Día o Noche publicado. No determina por sí mismo una hora exacta. |
| Inicio | Cadena HH:MM o No indicado. Hora local nominal sin fecha asociada. |
| Fin | Cadena HH:MM o No indicado. Puede ser madrugada siguiente solo con nota explícita. |
| Nota de revisión | Observación heredada que explica ausencias, cruce nocturno o posibles solapamientos. |

## Hojas complementarias

| Hoja y campo | Significado observado |
| --- | --- |
| Distritos: Distrito | Identificador de distrito: enteros 1–15 y texto DMI; conservar el tipo original. |
| Distritos: Nombre publicado | Denominación publicada del distrito. |
| Distritos: Sector | Sector A (Oeste) o B (Este) asociado al distrito. |
| Servicios: N.º servicio | Identificador entero del catálogo 1–11. |
| Servicios: Descripción publicada | Descripción textual del servicio. |
| Servicios: Sectores | A y B en los once servicios; no prueba ejecución. |
| Fuentes: Fuente ID | IMG01–IMG07 en las primeras siete filas; las seis restantes contienen nombres de criterios. |
| Fuentes: Contenido | Descripción del aviso o texto metodológico según fila. |
| Fuentes: Imagen recibida | Nombre de archivo de imagen transcrita, no copia presente. Nulo en criterios. |
| Fuentes: Detalle extraído | Resumen de la imagen; nulo en criterios. |
| Fuentes: Vigencia del aviso | No indicada en siete imágenes, nulo en criterios. No acredita vigencia. |

`_fila_excel` es un campo técnico añadido por el lector, no una columna original. Se preservan valores fuente; las ausencias semánticas y controles se aplican solo en derivados. No se unen automáticamente Distritos y Frecuencias por sector.

[Indicadores](indicadores.md) · [Fuentes](fuentes.md) · [Índice](index.md)

## Versión 2.0: representación JSON

El [exportador original](../fuentes/referencia_remota/scripts/export_web_data.py) contiene FIELD_MAP y DAY_MAP. Se comparó su mapeo usando AST sin ejecutarlo ni cambiarlo. [Comparador](../scripts/comparar_excel_json.py), [resultado](../evidencias/segunda_ingesta/comparacion/comparacion.json).

| Excel | JSON | Transformación |
| --- | --- | --- |
| ID, Sector publicado, Zona, Delimitación / área, Distritos indicados | id, sector, zona, area, distritos | Texto, espacios de extremos eliminados |
| Días publicados, Feriados, Turno, Inicio, Fin, Nota de revisión | dias_publicados, feriados, turno, inicio, fin, nota_revision | Texto; nulo/vacío se representaría No indicado |
| Lun, Mar, Mié, Jue, Vie, Sáb, Dom | dias.lun/mar/mie/jue/vie/sab/dom | Entero 0/1 → booleano false/true en esta base |
| Coordenada física de fila | fila_origen | Entero de fila original, de 2 a 22 |

Metadatos del contenedor: fuente (nombre del libro), hoja (Frecuencias), total_registros (21), frecuencias (lista). No hay campos de vigencia, fecha de exportación ni hash del Excel. El exportador acepta otras marcas de días y convierte un día nulo a false; la base actual usa exclusivamente enteros 0/1, por lo que esa pérdida potencial no ocurrió en los registros comparados. Si cambia el dominio, debe revisarse el exportador y no convertir desconocido en día negativo por defecto.
