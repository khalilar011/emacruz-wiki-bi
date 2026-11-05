# Registro cronológico de operaciones

Fechas reales con desplazamiento UTC−04:00 (America/La_Paz). Operador: agente IA Codex. Aprobaciones humanas registradas por separado.

[Índice](index.md)

## 2026-11-03T21:05:36-04:00 — Preservación e inspección de fuentes

Se copiaron Excel y README locales sin alterar originales; se recuperó documentación de GitHub fijada por commit. El JSON solo se localizó en el árbol remoto y aún no se incorporó ni analizó. Hashes en [manifiesto](../fuentes/manifiesto.json). HTML leído como [texto completo](../fuentes/consigna/texto_completo.txt); prompt extraído de su sección 3. Se constató copia local antigua y ausencia local de AGENTS/JSON. Se emplea Python 3.14.3 estándar: openpyxl no instalado. El comando exploratorio `py --version` no existe y la enumeración de la carpeta personal fue denegada; no afectan las fuentes recuperadas.

## 2026-11-03T21:10:52-04:00 — Corrección del analizador antes de congelar la primera ingesta

La primera ejecución en [calculo](../evidencias/primera_ingesta/calculo/analisis.json) clasificó erróneamente banderas 0 como ausencias por usar `v or ""`. Se corrigió normalización para distinguir None de 0 y se repitió en [calculo_v1](../evidencias/primera_ingesta/calculo_v1/analisis.json). El KPI no cambió (6/21), pero el perfil de ausencias binarias sí. También se corrigió un paréntesis de impresión en preparar_fuentes.py tras un SyntaxError previo a su ejecución. Se conservan ambos resultados analíticos, sin presentar el inicial como validación final.

## 2026-11-03T21:10:52-04:00 — Primera ingesta ejecutada

Entradas: Excel, README y documentación de objetivos. Se generaron índice, objetivos, fuentes, diccionario, indicadores, hallazgos, procedencia, método, mapa, registro humano y README. [Inventario de archivos y aportes](../evidencias/primera_ingesta/operacion.json). KPI v1.0 = 6/21 (28,57 %); faltan horas Fin en quince filas. El JSON aún no se leyó. Las conclusiones están pendientes de revisión humana.

## 2026-11-03T21:10:52-04:00 — Instantánea primera_ingesta

Se conservó el estado real de 34 archivos en [primera_ingesta](../evidencias/primera_ingesta/estado.json), con ZIP y hashes. El propio asiento se añade después de la captura para evitar autorreferencia.

## 2026-11-03T21:12:23-04:00 — Consulta inicial desde la wiki

Se leyó primero índice y después objetivos, fuentes, indicadores, hallazgos y diccionario. [Orden y hashes](../evidencias/consulta_y_verificaciones/lectura_y_afirmaciones.json). Se guardó [respuesta inicial](../evidencias/consulta_y_verificaciones/respuesta_inicial.md) con tres afirmaciones derivadas del cálculo real: 21 filas, 15 sin Fin y 6 que cumplen. Todavía no se marca ninguna como contrastada por lectura independiente.

## 2026-11-03T21:13:03-04:00 — Consulta revisada y contrastada

V1, V2 y V3 confirmadas por lectura XML independiente. Se guardó wiki/consulta_negocio.md y se enlazó desde índice. Cifras iniciales conservadas; se precisó acción por grupo, alcance semanal y revisión humana pendiente. Auditoría de enlaces iniciada después de la consulta.

## 2026-11-03T21:14:22-04:00 — Auditoría y corrección antes de segunda ingesta

Se registró revisión semántica en wiki/revision_calidad.md y se incorporó al índice. Auditoría inicial: cuatro enlaces rotos. Se corrigió documento/generador y se repitió: evidencias/revision/enlaces_corregidos.json, 168 enlaces locales, cero rotos, cero páginas wiki aisladas y cero duplicados exactos. También se aclaró una errata del prompt sobre duplicados sin cambiar reglas. Pendientes: vigencia, mapas, imágenes, permisos y aceptación humana. Un parche de enlaces con fecha de ejecución mal transcrita fue rechazado sin modificar archivos y se reaplicó leyendo la fecha real.

## 2026-11-03T21:14:23-04:00 — Instantánea segunda_ingesta/antes

Se conservó el estado real de 39 archivos en [segunda_ingesta/antes](../evidencias/segunda_ingesta/antes/estado.json), con ZIP y hashes. El propio asiento se añade después de la captura para evitar autorreferencia.

## 2026-11-03T21:15:30-04:00 — Segunda ingesta: incorporación auténtica de evidencia

Después del estado previo, consulta y auditoría, se incorporaron JSON y exportador originales del commit fijado, comprobando blobs. [Incorporación](../evidencias/segunda_ingesta/incorporacion.json). Estas evidencias no existían en la primera instantánea y no se usaron en su cálculo. Se compararán las 18 variables de Frecuencias y fila_origen, sin alterar el proyecto original.

## 2026-11-03T21:17:46-04:00 — Segunda ingesta: comparación y actualización de conocimiento

Comparación ejecutada: 399 valores, 0 diferencias; proyección idéntica en bytes. Recálculo del Excel: 6/21 (28,57 %). Se actualizaron fuentes, procedencia, diccionario, indicadores, hallazgos, consulta, revisión, mapa e índice; se creó comparación de exportación y respuestas del paso 6. [Archivos y aportes](../evidencias/segunda_ingesta/actualizacion.json). El diagnóstico se mantiene; se añade fidelidad técnica del derivado y omisión de las otras hojas. No hay contradicciones nuevas ni aprobación humana.

## 2026-11-03T21:21:34-04:00 — Preparación del cierre y matriz docente

Se documentaron ocho criterios con evidencias, sin puntuación autoasignada: siete cumplidos técnicamente y criterio de ingesta parcial por aceptación humana pendiente. Se prepararon scripts de reproducción, integridad y comparación entre estados, README completo y documentación de antes/después. Se aclaró que el conector GitHub devuelve texto en fetch; una tentativa de parsearlo como metadatos JSON falló y se usó fetch_file base64 con comprobación de blob para conservar bytes. No se crearon Git, Word, PDF ni publicación.

## 2026-11-03T21:21:34-04:00 — Instantánea segunda_ingesta/despues

Se conservó el estado real de 52 archivos en [segunda_ingesta/despues](../evidencias/segunda_ingesta/despues/estado.json), con ZIP y hashes. El propio asiento se añade después de la captura para evitar autorreferencia.

## 2026-11-03T21:22:30-04:00 — Cierre: fallo detectado y corrección

La reproducción inicial ejecutó análisis, afirmaciones, comparación y reglas con exit_code 0; validación integral: 19/20 por enlace al propio reporte todavía no guardado. Se conserva evidencias/revision/validacion_final. Se ajustó el orden de escritura del validador y se actualizaron README, matriz y revisión para apuntar al cierre corregido. Los ZIP de las ingestas no se alteran. Se repite toda la reproducción en nueva carpeta por esta corrección.

## 2026-11-03T21:23:38-04:00 — Cierre técnico completado

Reproducción corregida: cinco procesos con exit_code 0; control integral 20/20, reglas 10/10, tres afirmaciones confirmadas y comparación de 399 valores sin diferencias. Se verificaron fuentes/ZIP y archivos de trabajo originales idénticos a hashes iniciales. Se añadieron resumen de revisión y resultado fechado a wiki/revision_calidad.md e índice. La elaboración del informe separado y las aprobaciones humanas siguen pendientes; no se creó repositorio Git ni se publicó.

## 2026-11-03T21:23:38-04:00 — Instantánea revision/cierre

Se conservó el estado real de 52 archivos en [revision/cierre](../evidencias/revision/cierre/estado.json), con ZIP y hashes. El propio asiento se añade después de la captura para evitar autorreferencia.

## 2026-11-03T21:24:20-04:00 — Auditoría final y entrega local

Se ejecutó evidencias/revision/enlaces_cierre.json: 341 enlaces locales, cero rotos, cero páginas wiki aisladas y cero Markdown propios exactamente duplicados. Se conservó estado de cierre adicional sin alterar las ingestas. Se genera inventario SHA-256 de entrega, excluyendo este mismo inventario y caches de Python. No hay aceptación humana registrada.

## 2026-11-05T03:07:32-04:00 — Preparación Git privada y reanudación de publicación

Por solicitud expresa del usuario se prepararon .gitignore, .gitattributes y AGENTS v1.1, se actualizaron README, índice, procedencia y revisión humana, y se adaptó validar_proyecto.py a la etapa Git independiente. Se añadió scripts/auditar_publicacion.py y docs/publicacion_github.md. No se ingirieron nuevas fuentes ni se modificó el KPI. Se conservó [auditoría inicial fallida](../evidencias/publicacion/auditoria_inicial.json) por entrada CRLF en check-ignore, se corrigió con separadores NUL y se ejecutó [auditoría corregida](../evidencias/publicacion/auditoria_corregida.json), sin credenciales reconocibles ni fuentes excluidas. La [reproducción corregida](../evidencias/publicacion/validacion_corregida/resultado.json) completó cinco procesos: 20/20 controles integrales, 10/10 reglas, tres afirmaciones confirmadas y 399 valores sin diferencias. Los 34 archivos del original, incluidos metadatos Git, coinciden con la captura anterior. La interrupción había dejado main sin commit ni origin; git add volvió a fallar por permiso denegado sobre .git/index.lock. La CLI no accede a GitHub, el conector devuelve 404 sin capacidad de crear repositorios y el navegador había sido rechazado automáticamente. [Estado remoto observado](../evidencias/publicacion/estado_remoto_reanudacion.json) y [detalle de preparación](../docs/publicacion_github.md). Pendientes: resolver acceso autorizado a Git/red, commit, creación privada si corresponde, push y comprobación remota. No se generaron Word, PDF ni informe académico, ni se inventó aprobación humana. Se corrigió la codificación de este nuevo asiento y del registro remoto tras detectar sustituciones de tildes en la entrada estándar de PowerShell; se utilizó un parche UTF-8.

## 2026-11-05T03:09:12-04:00 — Cierre local de la preparación privada

La [auditoría de cierre](../evidencias/publicacion/auditoria_cierre.json) pasó: 152 candidatos al momento de lectura, cero patrones de credenciales, once fuentes íntegras y original idéntico (34 archivos incluidos metadatos Git). La [auditoría de enlaces](../evidencias/publicacion/enlaces_cierre.json) comprobó 373 destinos locales sin rotos ni páginas wiki aisladas. Se verificaron también destinos contra el árbol candidato. El estado final consultado sigue en main, sin commit, sin archivos preparados ni origin: .git/index.lock y .git/config no admiten escritura en este entorno. No existe confirmación de creación remota ni push. No se ha modificado proyecto-emacruz ni se ha generado informe académico. Estado y limitaciones en [publicación GitHub](../docs/publicacion_github.md).

## 2026-11-05T03:25:47-04:00 — Actualización documental de la publicación pública

El usuario confirmó que el repositorio ya estaba publicado y era público. El conector GitHub comprobó propietario khalilar011, visibilidad public, rama principal main y coincidencia inicial con el commit ed3a072299674d1bfff81edf7df7e99f13b48382. Se actualizan README.md, docs/publicacion_github.md, wiki/index.md, AGENTS.md, docs/revision_humana.md, docs/decisiones_metodologicas.md, docs/matriz_cumplimiento.md, la referencia de publicación en wiki/respuestas_paso_6.md y comentarios de .gitignore. Se mantienen pendientes los permisos institucionales y las aprobaciones humanas. Los asientos anteriores y evidencias de intentos bloqueados son históricos y no se sobrescriben. No se cambian fuentes, scripts, bases de datos, análisis, indicadores ni evidencias académicas. La auditoría de enlaces se ejecutó sin destinos rotos; se repetirá tras añadir este asiento. Git add falló por permiso denegado en .git/index.lock y la conexión Git de la CLI no está disponible; se prepara la publicación del commit documental mediante el conector autorizado, sin force. La sincronización del historial local se debe comprobar aparte. El informe académico sigue sin elaborarse. [Estado de publicación](../docs/publicacion_github.md).

## 2026-11-05T03:27:22-04:00 — Cierre documental con escritura bloqueada

La documentación local refleja la publicación pública completada y conserva permisos institucionales y revisiones humanas pendientes. La auditoría de enlaces posterior al primer asiento comprobó 385 destinos sin rotos. Se corrigió el salto de línea del asiento nuevo para que diff --check pase, conservando exactamente el prefijo histórico del log. El intento de crear el árbol documental mediante el conector GitHub devolvió HTTP 403, Resource not accessible by integration. No se creó commit ni se actualizó main remoto. Persisten el permiso denegado de git add sobre .git/index.lock y el fallo de conexión Git de la CLI. La actualización documental queda en el árbol local; commit, push y sincronización siguen pendientes. Los resultados de esta comprobación se guardan en salidas/actualizacion_documentacion_20261105_0324, excluida de Git, sin modificar evidencias académicas. No se elaboró informe. [Estado de publicación](../docs/publicacion_github.md).
