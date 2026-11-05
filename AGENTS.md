# Agente de la wiki EMACRUZ

Versión 1.2. Instrucciones para esta carpeta independiente. El AGENTS del proyecto original se conserva solo como evidencia, no gobierna esta wiki. La solicitud inicial del 05/11/2026 autorizó preparar Git y publicar una entrega independiente privada. Posteriormente el usuario confirmó que el repositorio ya está publicado y es público, y solicitó actualizar su documentación en `main`. Ese estado no acredita permiso institucional, licencia ni aprobación de reglas o conclusiones. No cambiar la visibilidad ni los accesos como parte de esta actualización documental.

## Objetivo y alcance

Mantener conocimiento BI verificable sobre calidad de la programación publicada de recolección para Alerta Ruta. Reutilizar los objetivos de [README original](fuentes/originales/README.md) y los límites del [plan CRISP-DM](fuentes/referencia_remota/docs/plan-crisp-dm.md). No desarrollar un nuevo portal, pronosticar sin observaciones ni presentar el prototipo como herramienta oficial. El estado del repositorio público se documenta en [el registro de publicación](docs/publicacion_github.md). Esta tarea solo actualiza documentación; no modifica bases, análisis, indicadores ni evidencias académicas. No desplegar ni redactar informe académico en esta etapa.

## Estructura y fuentes autorizadas

`fuentes/` contiene originales intactos y referencias con [manifiesto](fuentes/manifiesto.json). `wiki/` es conocimiento derivado. `prompts/` conserva las instrucciones. `scripts/` implementa cálculos. `evidencias/` conserva ejecuciones y estados reales. `docs/` contiene decisiones, trazabilidad y aprobaciones pendientes. Las fuentes autorizadas son el Excel local, README, HTML docente y documentación del repositorio khalilar011/proyecto-emacruz fijada por commit. Incorporar el JSON derivado solo en la segunda ingesta. Toda ampliación debe documentar procedencia, versión, permiso y relación con las anteriores.

## Conservación, fechas y permisos

No modificar, mover ni borrar el repositorio `proyecto-emacruz` ni los originales copiados. Comparar SHA-256 antes/después. Recuperar bytes remotos mediante base64 y comprobar blob Git contra commit. La fecha de consulta debe obtenerse del reloj; la fecha de modificación del Excel y los nombres de imágenes no demuestran vigencia. Registrar “No acreditado” cuando falte permiso institucional. El usuario autoriza este análisis y copia local académica; no atribuir esa autorización a EMACRUZ ni deducir licencia pública de un repositorio visible.

## Markdown y trazabilidad

Usar UTF-8, títulos claros, enlaces relativos con `/`, nombres de archivo en minúsculas y sin espacios para páginas nuevas. Cada página de la wiki enlaza el índice y las fuentes pertinentes. Toda cifra importante cita versión, hoja/fila o resultado ejecutado y script. Etiquetar hechos observados, cálculos, inferencias, supuestos y resultados esperados. No mezclar frecuencias con recojos ejecutados, ni filas de fuentes con imágenes distintas. No inferir relaciones distrito → frecuencia solo por pertenencia al mismo sector.

## Creación y actualización

Leer primero [índice](wiki/index.md), buscar páginas existentes por concepto y actualizar la página canónica. Crear otra solo si hay un tema distinto y evidencia útil. Enlazarla desde el índice y páginas relacionadas. Evitar copias del mismo hallazgo salvo resúmenes enlazados. Registrar en [log](wiki/log.md) fecha real, operación, entradas, archivos creados/modificados, aporte BI, errores e incertidumbres. Conservar una instantánea con hashes antes de cada ingesta posterior; no reconstruir retrospectivamente una primera ingesta.

## Contradicciones y reglas analíticas

Conservar las dos versiones y sus referencias; explicar el conflicto, su alcance y qué falta para resolverlo. No elegir por conveniencia ni sobrescribir datos. La fuente de negocio primaria es Excel; el JSON es una transformación técnica, no una corroboración independiente. Mantener separadas las filas generales sin sector. Los posibles solapamientos requieren polígonos y revisión humana. Definir el KPI en [indicadores](wiki/indicadores.md) con reglas antes de calcular: población, numerador, ausencias, duplicados, días, horas, medianoche, unidad, filtros y versión. Toda modificación de regla exige nueva versión y recálculo, sin alterar la evidencia histórica.

## Validación y revisión humana

Ejecutar análisis Python, tres verificaciones contra originales, comparación Excel/JSON, auditoría de enlaces y comprobación de entregables. Guardar salida y fallos, corregir y repetir con nombre distinto. No decir “validado” sin ejecución ni confundir control automático con aprobación humana. Rechazar cambios de esquema o fórmulas no soportados hasta ajustar el lector explícitamente. Las conclusiones que afecten decisiones se guardan como propuestas pendientes, sujetas a [revisión humana](docs/revision_humana.md). No inventar aprobadores, firmas, fechas ni validación con EMACRUZ. El agente puede preparar toda evidencia local autorizada; una persona debe aprobar reglas y conclusiones antes de usarlas operativamente.

## Privacidad

No incorporar credenciales, conversaciones privadas, datos de vecinos ni ubicaciones personales. Conservar metadatos originales sin divulgar información personal innecesaria en resúmenes. La copia binaria puede contener metadatos personales heredados: revisar permisos antes de publicación futura y usar exclusiones de Git. No descargar las imágenes de WhatsApp por rutas deducidas ni publicar documentos institucionales sin permiso. Registrar fuentes ausentes en lugar de fabricarlas.
