"""Genera las páginas de la primera ingesta desde cálculos ejecutados y fuentes leídas.
No es un servicio de IA: documenta la ejecución asistida por Codex en esta sesión.
"""
import json
from comun import ROOT, ahora, guardar, json_out, log, leer_excel
from analizar import calcular

def main():
    if (ROOT/'evidencias/primera_ingesta/estado.zip').exists():
        raise SystemExit('Primera ingesta congelada; no reconstruir historia.')
    s,d=calcular()
    t=ahora()
    manifest=json.loads((ROOT/'fuentes/manifiesto.json').read_text(encoding='utf-8'))
    docs={}
    docs['fuentes/procedencia.md']=f'''# Procedencia y conservación

Consulta inicial ejecutada: {manifest['inicio']} a {manifest['fin']}. Fechas UTC−04:00. El [manifiesto](manifiesto.json) conserva origen exacto, ruta copiada, consulta, versión y SHA-256 de cada archivo. [Registro remoto](../evidencias/recuperacion_remota_inicial.json): respuestas base64 y árbol con commit.

| Evidencia | Procedencia, versión y relación | Permisos y limitaciones |
| --- | --- | --- |
| [Excel](originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) | Copia idéntica del repositorio local `proyecto-emacruz`, commit 29a44d875600d3ddc88fb53bafce80469902ce50. Blob Git coincide con el Excel del commit remoto 5fba63ec96844fa1373b6c5703fce54430b52de8. SHA-256: `{s['excel_sha256']}`. Modificación interna: {s['metadatos_excel']['modified']}. | Uso y copia local académica solicitados por el usuario. Interlocutor institucional, autorización EMACRUZ, licencia y vigencia operativa no acreditados. Metadatos personales heredados presentes; revisar antes de publicar. |
| [README local](originales/README.md) y [README remoto](referencia_remota/README.md) | Objetivos existentes. Copias de versiones local/remota diferenciadas. | Evidencia de intención académica, no validación institucional. Nombres de equipo ya presentes; no se amplían datos personales. |
| [Documentación CRISP-DM](referencia_remota/docs/plan-crisp-dm.md), [historia SCRUM-22](referencia_remota/docs/historias/SCRUM-22.md), [fuentes](referencia_remota/docs/fuentes-datos.md), [datos](referencia_remota/data/README.md) | GitHub, commit remoto fijado arriba. Se comprueba blob Git al decodificar base64. Aclaran alcance y ausencia de permisos/vigencia. | La ficha de origen institucional sigue pendiente en el proyecto original. La historia es contexto, no una orden de crear el Excel piloto. |
| [AGENTS original](referencia_remota/AGENTS.md) | No existe en la copia local antigua; recuperado del mismo commit remoto. | Solo referencia documental. No se ejecutan sus acciones de Jira o publicación. |
| [Consigna HTML](consigna/Tarea_wiki_IA_proyecto_BI.html) y [texto extraído](consigna/texto_completo.txt) | Copia idéntica de Downloads. Autor del documento: Business Intelligence II, Unidad 3; fecha declarada 2026-11-03. | Uso académico local solicitado. No se deduce permiso de redistribución docente. El texto incluye todos los requisitos legibles, sin ejecutar scripts. |

La hoja Fuentes registra siete imágenes IMG01–IMG07 recibidas según sus nombres el 09/10/2026; las imágenes no están incorporadas a este proyecto. No se han comprobado visualmente los avisos ni se atribuye su transcripción a un organismo sin evidencia adicional. Hay otras seis filas de criterios metodológicos en esa hoja; no son seis imágenes más. Las fechas en nombres no son fechas de vigencia.

El árbol remoto localiza `web/data/frecuencias.json`, ausente localmente. Su contenido no se usa en esta primera ingesta. La segunda deberá documentar exportador y dependencia respecto al Excel antes de interpretar coincidencias.

[Fuentes de la wiki](../wiki/fuentes.md) · [Índice](../wiki/index.md)
'''
    docs['wiki/objetivos.md']='''# Objetivos, utilidad y pregunta BI

Versión 1.0, primera ingesta. **Hecho documental:** el [README original](../fuentes/originales/README.md), secciones Objetivo general y específicos, propone analizar gestión y recolección de residuos con ciencia de datos y BI. Los cinco objetivos siguientes se conservan; las decisiones y resultados son su operacionalización académica propuesta para esta wiki.

| Objetivo existente | Decisión que puede apoyar | Usuario propuesto | Fuente y resultado esperado | Evidencia de utilidad |
| --- | --- | --- | --- | --- |
| Organizar y centralizar datos | Qué versión usar como base y qué evidencia falta | Mantenedor de datos | Excel, README y documentación → inventario íntegro | Hashes y [procedencia](../fuentes/procedencia.md) recuperables |
| Analizar información de recolección | Qué registros revisar por programación incompleta | Analista/mantenedor | Frecuencias → KPI y lista por fila | Recalcular numerador, denominador y motivos en [indicadores](indicadores.md) |
| Identificar patrones y problemáticas | Priorizar horarios ausentes y límites territoriales ambiguos | Analista y revisor temático | Notas y Fuentes del Excel → [hallazgos](hallazgos.md) | Contrastar cada ID, sin generalizar a cobertura real |
| Aplicar herramientas de análisis | Aceptar o corregir resultados automáticos | Equipo académico | Python + Excel → verificaciones repetibles | Comandos, controles y salidas conservadas |
| Generar información útil para mejoras | Preparar correcciones propuestas antes de usar en Alerta Ruta | Mantenedor y responsables humanos; ciudadano como usuario posterior | Wiki enlazada → consulta y prioridades | Revisión humana pendiente y criterios de cierre, sin aprobación simulada |

**Pregunta principal:** “¿Qué tan completa y consistente es la información disponible sobre días y horarios de recolección por sector o zona, y qué registros requieren revisión antes de utilizarse en Alerta Ruta?”

**Contexto preservado:** el [plan CRISP-DM](../fuentes/referencia_remota/docs/plan-crisp-dm.md) también plantea estudiar factores de acumulación bajo restricciones de diésel y comunicar estados/avisos aprobados. Esta wiki apoya comprensión y preparación de datos; las frecuencias no prueban acumulación, retrasos, ejecución ni predicción. No se reemplaza ese objetivo de investigación con un modelo inventado. El [AGENTS original](../fuentes/referencia_remota/AGENTS.md) describe roles previstos de carga, aprobación y consulta. No acredita implantación oficial de EMACRUZ.

**Inferencia propuesta:** una lista localizada por ID puede reducir el trabajo de búsqueda del mantenedor. **Resultado esperado, todavía sin medir:** que la persona revise y complete la programación. No existen mediciones de ahorro de tiempo, satisfacción o mejora operativa.

[Mapa de trazabilidad](../docs/mapa_trazabilidad.md) · [Índice](index.md)
'''
    docs['wiki/fuentes.md']=f'''# Fuentes disponibles

Versión 1.0. [Procedencia, permisos y hashes](../fuentes/procedencia.md). El Excel es fuente tabular primaria de esta implementación; README/CRISP-DM son evidencias de objetivos, no observaciones de recolección.

| Hoja del [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) | Rango observado | Filas no vacías sin encabezado | Uso |
| --- | --- | --- | --- |
| Frecuencias | A1:R22 | 21 | Unidad: combinación zona, turno y frecuencia transcrita de una imagen, según Fuentes!A12:B12. Base del KPI. |
| Distritos | A1:C17 | 16 | Catálogo: quince identificadores numéricos y DMI. No contiene un enlace completo distrito → frecuencia. |
| Servicios | A1:C12 | 11 | Catálogo de servicios; no son once recojos ni once horarios. |
| Fuentes | A1:E16 | 13 | Siete filas IMG01–IMG07 (2–8) y seis filas metodológicas (11–16). Las filas 9–10 están vacías. |

Observación reproducida en [inspección íntegra](../evidencias/primera_ingesta/inspeccion_excel.json) y [cálculo corregido](../evidencias/primera_ingesta/calculo_v1/analisis.json), mediante [lector OOXML](../scripts/comun.py). No hay fórmulas en las celdas leídas: el lector las rechaza si aparecen. Las horas son cadenas `HH:MM`, las banderas de días son enteros y Distrito mezcla números con DMI. No se convirtió el libro ni se completaron ausencias.

El archivo tiene fecha interna de modificación {s['metadatos_excel']['modified']}; eso no establece un período operativo. La hoja Fuentes marca “No indicada” en la vigencia de las siete imágenes. Las imágenes originales no están presentes y no hay clave `Fuente ID` por fila de Frecuencias. La atribución detallada imagen → registro queda limitada al texto metodológico y no se inventa una clave foránea.

La documentación de [datos](../fuentes/referencia_remota/data/README.md), [registro de fuentes](../fuentes/referencia_remota/docs/fuentes-datos.md) e [historia SCRUM-22](../fuentes/referencia_remota/docs/historias/SCRUM-22.md) exige conservar ausencias y reconocer vigencia no acreditada. El JSON localizado remotamente se reserva para una segunda ingesta y aún no aporta resultados a esta página.

[Diccionario](diccionario_datos.md) · [Indicadores](indicadores.md) · [Índice](index.md)
'''
    defs={
    'ID':'Identificador textual de la fila de frecuencia (F01–F21). No es una ruta ni un servicio ejecutado. Debe ser único.',
    'Sector publicado':'Etiqueta A (Oeste), B (Este) o No indicado. No se imputa desde zona.',
    'Zona':'Nombre publicado de zona: Norte, Sur, Centro, Casco Viejo o No indicada en fila. No representa un polígono completo.',
    'Delimitación / área':'Texto de anillos, área o subzona de mapa. La presencia de texto no demuestra delimitación geográfica suficiente.',
    'Distritos indicados':'Lista textual de DM o referencia industrial. No indicada en doce registros. No es clave normalizada.',
    'Días publicados':'Texto de días o intervalo, incluyendo Diario y Solo sábado. Se contrasta con las siete banderas.',
    'Feriados':'Sí o No indicado observado. No indicado no significa No. Se controla aparte del KPI semanal.',
    'Turno':'Día o Noche publicado. No determina por sí mismo una hora exacta.',
    'Inicio':'Cadena HH:MM o No indicado. Hora local nominal sin fecha asociada.',
    'Fin':'Cadena HH:MM o No indicado. Puede ser madrugada siguiente solo con nota explícita.',
    'Nota de revisión':'Observación heredada que explica ausencias, cruce nocturno o posibles solapamientos.'}
    wb=leer_excel()
    dictionary='# Diccionario de datos observados\n\nVersión 1.0. Fuente: [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), campos y tipos extraídos en [inspección](../evidencias/primera_ingesta/inspeccion_excel.json). Significados descriptivos de la transcripción y decisiones analíticas de la wiki; no equivalen a definiciones institucionales aprobadas.\n\n## Frecuencias\n\n| Campo | Significado y control |\n| --- | --- |\n'
    for c in wb['sheets']['Frecuencias']['columns']:
        meaning=defs.get(c, f'Bandera de {c}: entero 1 significa día marcado, 0 significa día no marcado. El cero es un valor válido, no una ausencia.')
        dictionary+=f'| {c} | {meaning} |\n'
    dictionary+='\n## Hojas complementarias\n\n| Hoja y campo | Significado observado |\n| --- | --- |\n'
    other={'Distrito':'Identificador de distrito: enteros 1–15 y texto DMI; conservar el tipo original.','Nombre publicado':'Denominación publicada del distrito.','Sector':'Sector A (Oeste) o B (Este) asociado al distrito.','N.º servicio':'Identificador entero del catálogo 1–11.','Descripción publicada':'Descripción textual del servicio.','Sectores':'A y B en los once servicios; no prueba ejecución.','Fuente ID':'IMG01–IMG07 en las primeras siete filas; las seis restantes contienen nombres de criterios.','Contenido':'Descripción del aviso o texto metodológico según fila.','Imagen recibida':'Nombre de archivo de imagen transcrita, no copia presente. Nulo en criterios.','Detalle extraído':'Resumen de la imagen; nulo en criterios.','Vigencia del aviso':'No indicada en siete imágenes, nulo en criterios. No acredita vigencia.'}
    for k,v in wb['sheets'].items():
        if k!='Frecuencias':
            for c in v['columns']:
                dictionary+=f'| {k}: {c} | {other[c]} |\n'
    dictionary+='\n`_fila_excel` es un campo técnico añadido por el lector, no una columna original. Se preservan valores fuente; las ausencias semánticas y controles se aplican solo en derivados. No se unen automáticamente Distritos y Frecuencias por sector.\n\n[Indicadores](indicadores.md) · [Fuentes](fuentes.md) · [Índice](index.md)\n'
    docs['wiki/diccionario_datos.md']=dictionary
    docs['wiki/indicadores.md']=f'''# Indicadores de calidad documental

Versión de regla 1.0. Propuesta académica pendiente de aprobación humana. Fuente: [Excel preservado](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), SHA-256 `{s['excel_sha256']}`, modificado internamente {s['metadatos_excel']['modified']}. No hay período operativo acreditado. Cálculo ejecutado: [analisis.json](../evidencias/primera_ingesta/calculo_v1/analisis.json); implementación: [analizar.py](../scripts/analizar.py).

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
'''
    docs['wiki/hallazgos.md']='''# Hallazgos verificables

Versión 1.0. Fuente analizada: Excel conservado, modificación interna 2026-10-15T16:29:10Z. Los resultados proceden del [cálculo ejecutado](../evidencias/primera_ingesta/calculo_v1/analisis.json), con localización por ID/fila en [CSV](../evidencias/primera_ingesta/calculo_v1/registros_evaluados.csv). [Definición del KPI](indicadores.md).

| Tipo | Hallazgo y localización | Consecuencia propuesta |
| --- | --- | --- |
| Cálculo | 6 de 21 cumplen KPI (28,57 %): F07–F12, Frecuencias filas 8–13. | Conservar como programación semanal documentalmente completa, con vigencia y aprobación pendientes. |
| Observación/cálculo | F01–F06, filas 2–7: Fin y sector No indicado. Inicio 06:00 o 19:00. | Solicitar fin y sector de esos avisos; no asignar A/B por analogía. |
| Observación/cálculo | F13–F21, filas 14–22: Inicio y Fin No indicado. | Priorizar recuperación de horas exactas; turno no basta. |
| Observación | F21, fila 22: Zona = No indicada en fila; DM 15 sí figura. | Solicitar zona o delimitación autorizada; no inferir Norte/Sur. |
| Cálculo | F07–F10, filas 8–11: 20:00 → 04:00 con nota de madrugada siguiente. | Interpretar cruce documentado, no corregirlo como inversión horaria. |
| Cálculo | 21/21 patrones semanales concuerdan con banderas; 0 IDs repetidos y 0 filas exactamente duplicadas. | Conservar días publicados. Esto no resuelve superposiciones territoriales. |
| Observación | F17 (fila 18) y F20 (fila 21) contienen notas de posible solapamiento; Fuentes!A15:B15 describe límites textuales insuficientes. | Revisar F16/F17 y F19/F20 con mapas antes de fusionar. Posibilidad, no contradicción probada. |
| Observación/cálculo | 12 registros sin distritos, 20 sin feriados; Fuentes filas 2–8: siete avisos con vigencia No indicada. | No habilitar consultas universales por distrito ni afirmar calendario de feriados o actualidad. |

**Inferencia:** la carencia de horas es el principal impedimento del KPI en esta versión: las quince filas que no cumplen carecen de Fin. Se puede priorizar completar horarios, sujeto a revisión humana. No significa que quince zonas carezcan de recolección. El [criterio de la fuente](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), Fuentes!A13:B13, define No indicado como falta de información en la imagen, no ausencia de servicio.

**Incertidumbre:** sin las imágenes originales no se pueden validar transcripción, polígonos ni vigencia. Fuentes no incorpora una clave de imagen por cada fila de frecuencia; no se crea una relación exacta inventada. README y CRISP-DM no son fuentes de medición operativa.

[Fuentes](fuentes.md) · [Objetivos](objetivos.md) · [Índice](index.md)
'''
    docs['docs/decisiones_metodologicas.md']='''# Decisiones metodológicas

Versión 1.0. Base normativa: [HTML docente](../fuentes/consigna/Tarea_wiki_IA_proyecto_BI.html), secciones 1–5, leído íntegramente en [texto extraído](../fuentes/consigna/texto_completo.txt). Las decisiones se aplican al trabajo solicitado; las reglas del KPI son propuestas académicas, no reglas institucionales.

| Decisión | Justificación, alcance y estado |
| --- | --- |
| Carpeta independiente | La consigna habla del repositorio del proyecto. El usuario exige carpeta separada y prohíbe Git ahora; se implementa aquí sin alterar el original. |
| Informe aplazado | El HTML pide informe breve. Se preparan evidencias y respuestas en Markdown; el usuario reserva elaboración/entrega para otra tarea. No hay Word/PDF. |
| Revisión IA y humana separadas | El HTML solicita revisar modificaciones y conclusiones. Codex revisa automáticamente y documenta propuestas locales. La aceptación humana sigue pendiente; no se equipara a validación automática. |
| Dos versiones de repositorio | Copia local antigua 29a44d8 y referencia remota fijada 5fba63e. Se conservan ambas, sin actualizar ni hacer fetch en el repositorio original. Excel local coincide con blob remoto. |
| Python estándar para OOXML | El libro es pequeño y sin fórmulas. Se usa zipfile/XML para lectura exacta y scripts reproducibles sin instalar openpyxl. El lector rechaza fórmulas y encabezados ambiguos; no es un lector Excel universal. |
| Unidad y ausencias semánticas | Fuentes!A12:B13 explica unidad y No indicado. No se usan las 61 filas combinadas como denominador. Cero binario es valor válido. |
| Días, medianoche y duplicados | [KPI v1.0](../wiki/indicadores.md): concordancia semanal, cruce solo documentado, duplicados retenidos y excluidos del numerador. Feriados y distritos se diagnostican aparte. |
| Sin vinculación territorial inventada | Mismo sector no demuestra que todo distrito comparta todas las frecuencias. Solapamientos requieren mapas y persona responsable. |
| Ingestas auténticas | Congelar primera versión antes de consulta/auditoría y antes de leer JSON. Después recuperar exportador y JSON, comparar y conservar otra versión. |
| Privacidad y publicación | Uso local solicitado. Permiso EMACRUZ/docente y licencia de redistribución no acreditados. Se preservan bytes pero se excluyen copias sensibles del futuro Git hasta revisar permisos. |

No se ejecutan tareas de la historia SCRUM-22, no se fabrican avisos ni observaciones. Los objetivos predictivos del proyecto se documentan como no respondibles con programación sola.

[Revisión humana](revision_humana.md) · [Mapa](mapa_trazabilidad.md) · [Índice](../wiki/index.md)
'''
    docs['docs/mapa_trazabilidad.md']='''# Mapa objetivo → fuente → indicador → página → decisión

Versión 1.0. Objetivos textuales del [README](../fuentes/originales/README.md); decisiones propuestas para revisión humana. El [plan CRISP-DM](../fuentes/referencia_remota/docs/plan-crisp-dm.md) conserva además la investigación sobre acumulación.

| Objetivo | Fuente/evidencia | Indicador o control | Página | Decisión apoyada y límite |
| --- | --- | --- | --- | --- |
| Centralizar datos | Excel, README, [manifiesto](../fuentes/manifiesto.json) | Hashes, inventario de hojas y campos | [Fuentes](../wiki/fuentes.md) | Elegir versión analizada; no acredita vigencia |
| Analizar recolección | Frecuencias filas 2–22 | KPI v1.0, 6/21 | [Indicadores](../wiki/indicadores.md) | Priorizar quince filas incompletas; no mide cobertura |
| Identificar patrones/problemáticas | Inicio/Fin, notas F17/F20, hoja Fuentes | Ausencias, concordancia de días y cruce nocturno | [Hallazgos](../wiki/hallazgos.md) | Solicitar horas y mapas; no fusionar solapamientos supuestos |
| Aplicar análisis | [Python](../scripts/analizar.py) y salidas ejecutadas | Reproducción y tres verificaciones posteriores | [Índice](../wiki/index.md) | Aceptar cálculo técnico al comprobarlo; reglas pendientes de persona |
| Generar información para mejoras | Documentación y evidencia por fila | Lista de incidencias y pendientes | [Objetivos](../wiki/objetivos.md) | Preparar corrección autorizada, sin modificar fuente |
| Investigar factores de acumulación, contexto CRISP-DM | Plan existente; faltan mediciones de acumulación/diésel/operaciones | No calculable con las frecuencias | [Objetivos](../wiki/objetivos.md) | Diseñar futura captura de observaciones; no afirmar predicción |

[Decisiones](decisiones_metodologicas.md) · [Índice](../wiki/index.md)
'''
    docs['docs/revision_humana.md']='''# Registro de revisión humana y asuntos pendientes

Estado actual: **pendiente**. No se ha recibido aprobación de una persona sobre reglas, datos o conclusiones. Esta tabla registra solicitudes de revisión futuras y no contiene firmas ni fechas de aprobación inventadas. La instrucción del usuario autoriza trabajo local; no prueba una validación temática o institucional.

| Asunto para revisión | Rol propuesto, sin asignación confirmada | Evidencia que debe revisar | Estado |
| --- | --- | --- | --- |
| Definición de registro evaluable, obligatoriedad de campos y KPI semanal | Docente o analista BI del equipo | [Indicadores](../wiki/indicadores.md) y código | Pendiente |
| Conclusión de priorizar F01–F06 y F13–F21 | Responsable del mantenimiento de datos | [Hallazgos](../wiki/hallazgos.md), filas originales y CSV | Pendiente |
| Vigencia y transcripción de avisos, zonas, feriados y solapamientos | Interlocutor autorizado de EMACRUZ, por identificar | Excel e imágenes originales aún ausentes | Pendiente |
| Relación distrito → frecuencia y alcance geográfico | Responsable temático/cartográfico, por asignar | Mapas/polígonos y catálogo autorizado | Pendiente |
| Uso y futura publicación de copias, metadatos personales y consigna | Titular de datos/documento y responsable académico | [Procedencia](../fuentes/procedencia.md), originales y .gitignore | Pendiente |
| Aceptación de páginas modificadas por IA | Integrante del equipo o docente, por asignar | Estados y diferencias conservados | Pendiente |

Para registrar una aprobación real se añadirá fecha obtenida al recibirla, persona/rol identificado con autorización, alcance exacto, versión/huellas revisadas, decisión y referencia de la evidencia. No marcar la tabla como completa por ejecutar scripts. Las propuestas pueden conservarse en la wiki para revisión, pero no se aplican a decisiones operativas.

El informe académico separado y la publicación GitHub se harán en otra tarea por instrucción expresa. Las carencias de fuentes son resultados del diagnóstico, no datos que deban inventarse para cerrar la implementación.

[Reglas](../AGENTS.md) · [Índice](../wiki/index.md)
'''
    docs['README.md']='''# EMACRUZ – Wiki de conocimiento BI asistida por IA

Implementación académica independiente de Alerta Ruta, Business Intelligence II, Unidad 3, consigna 03/11/2026. Navegación: [wiki/index.md](wiki/index.md). La programación publicada permite diagnosticar calidad documental; no acredita servicio ejecutado, vigencia institucional ni predicción de acumulación.

La primera ingesta incorpora Excel y objetivos/documentación existentes. Se conserva una instantánea antes de la consulta y de incorporar JSON. Las conclusiones propuestas requieren [revisión humana](docs/revision_humana.md). El informe académico final y GitHub están reservados para otra tarea.

## Estructura

```text
emacruz-wiki-bi/
  fuentes/      originales, documentación remota fijada, consigna y hashes
  wiki/         índice, objetivos, fuentes, diccionario, KPI, hallazgos y log
  prompts/      original docente, versión EMACRUZ y justificación
  evidencias/   primera ingesta, consulta, segunda ingesta y revisión
  scripts/      lectura, cálculo y conservación de estados
  docs/         decisiones, mapa de trazabilidad y revisión humana
  AGENTS.md
  README.md
  requirements.txt
  .gitignore
```

## Reproducción

Python 3.10 o posterior; ejecución original con Python 3.14.3 en Windows. No requiere paquetes externos ni acceso de red para analizar las fuentes ya copiadas. Desde esta carpeta:

```powershell
python --version
python -X utf8 scripts/analizar.py --salida salidas/analisis_nuevo
```

Usar una carpeta nueva en cada ejecución: los scripts no sobrescriben evidencias históricas. La captura inicial de fuentes es específica del entorno de esta sesión; los cálculos posteriores leen las copias portables. Ver [método](docs/decisiones_metodologicas.md) y [reglas](AGENTS.md). No crear Git ni publicar automáticamente. Las exclusiones de copias originales se revisarán junto con permisos antes de una publicación futura.
'''
    names=['objetivos','fuentes','diccionario_datos','indicadores','hallazgos','log']
    docs['wiki/index.md']='# EMACRUZ — índice de conocimiento\n\nEstado: primera ingesta, versión 1.0. Fuentes conservadas y cálculos reales; conclusiones propuestas pendientes de revisión humana. La consulta, auditoría y segunda ingesta se ejecutarán después de congelar este estado.\n\n'+''.join(f'- [{n.replace("_"," ")} ]({n}.md)\n' for n in names)+'\n- [Reglas del agente](../AGENTS.md)\n- [Procedencia](../fuentes/procedencia.md)\n- [Prompt docente](../prompts/prompt_inicial.md), [mejorado](../prompts/prompt_mejorado.md) y [justificación](../prompts/justificacion_mejoras.md)\n- [Decisiones metodológicas](../docs/decisiones_metodologicas.md)\n- [Mapa de trazabilidad](../docs/mapa_trazabilidad.md)\n- [Revisión humana](../docs/revision_humana.md)\n- [Cálculo de primera ingesta](../evidencias/primera_ingesta/calculo_v1/analisis.json)\n- [Inicio y reproducción](../README.md)\n'
    for p,content in docs.items():
        guardar(p,content)
    json_out('evidencias/primera_ingesta/operacion.json',{'ejecutado':t,'evidencias':['Excel local y README local','documentación remota con commit fijado','HTML docente como requisitos'],'creados':sorted(docs),'modificados':['wiki/log.md'],'aporte_excel':'Inventario, diccionario, KPI y hallazgos por registro','aporte_readme_docs':'Objetivos originales, decisiones y límites de inferencia/predicción','json_ingerido':False,'incertidumbres':['Vigencia y permiso institucional no acreditados','Imágenes originales no disponibles','Revisión humana pendiente']})
    log('Corrección del analizador antes de congelar la primera ingesta','La primera ejecución en [calculo](../evidencias/primera_ingesta/calculo/analisis.json) clasificó erróneamente banderas 0 como ausencias por usar `v or ""`. Se corrigió normalización para distinguir None de 0 y se repitió en [calculo_v1](../evidencias/primera_ingesta/calculo_v1/analisis.json). El KPI no cambió (6/21), pero el perfil de ausencias binarias sí. También se corrigió un paréntesis de impresión en preparar_fuentes.py tras un SyntaxError previo a su ejecución. Se conservan ambos resultados analíticos, sin presentar el inicial como validación final.')
    log('Primera ingesta ejecutada','Entradas: Excel, README y documentación de objetivos. Se generaron índice, objetivos, fuentes, diccionario, indicadores, hallazgos, procedencia, método, mapa, registro humano y README. [Inventario de archivos y aportes](../evidencias/primera_ingesta/operacion.json). KPI v1.0 = 6/21 (28,57 %); faltan horas Fin en quince filas. El JSON aún no se leyó. Las conclusiones están pendientes de revisión humana.')
    print('Primera ingesta: páginas desarrolladas, cálculo v1 y operación registrados.')

if __name__=='__main__':
    main()
