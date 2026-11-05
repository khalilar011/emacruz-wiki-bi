# Revisión de calidad de la wiki

Versión 1.0. Auditoría IA posterior a la consulta y anterior a incorporar el JSON. Aprobación humana pendiente. [Auditor de enlaces](../scripts/auditar_enlaces.py), [resultado inicial ejecutado](../evidencias/revision/enlaces_antes.json). Este control cubre Markdown propio; las copias originales se preservan sin corregir sus referencias externas.

| ID y aspecto auditado | Observación real | Corrección o justificación |
| --- | --- | --- |
| A01 Enlaces rotos | Cuatro destinos incorrectos en el documento de verificaciones: un nivel de carpeta omitido | Se corrigieron enlaces y el generador calcula rutas relativas según la carpeta elegida. Se repite auditoría después del arreglo. |
| A02 Páginas aisladas | Ninguna de las páginas existentes de la wiki quedó fuera del recorrido desde índice | Mantener enlaces al añadir consulta, revisión y segunda ingesta. |
| A03 Duplicación | Cero archivos Markdown propios idénticos; cifras resumidas en varias páginas enlazan la definición canónica | No eliminar resúmenes útiles. Los avisos generales y sectorizados permanecen separados según Fuentes!A14:B14. |
| A04 Perfil de ausencias | La ejecución analítica inicial clasificó ceros binarios como ausentes | Corregido antes de congelar ingesta 1. [Primer resultado histórico](../evidencias/primera_ingesta/calculo/analisis.json) conserva el fallo; [resultado corregido](../evidencias/primera_ingesta/calculo_v1/analisis.json) es la referencia vigente. KPI 6/21 permanece igual. |
| A05 Contradicciones de horarios | Fin menor que Inicio en cuatro filas con nota explícita de madrugada siguiente | Se documentó cruce en lugar de alterar valores. Los posibles solapamientos F17/F20 siguen pendientes de mapas, sin tratarse como duplicados probados. |
| A06 Afirmaciones sin respaldo | Las cifras de consulta tienen tres contrastes independientes; inferencias/prioridades están etiquetadas | Vigencia, transcripción visual, permisos y utilidad operativa siguen sin evidencia suficiente y se expresan como pendientes. |
| A07 Indicador ambiguo | “Programación completa” podría interpretarse como incluir feriados o identificación por distrito | La definición especifica programación semanal ordinaria por sector o zona, controles auxiliares separados y aprobación humana pendiente. No se mide cobertura municipal. |
| A08 Vigencia/versiones | README local antiguo frente a documentación remota más reciente. Excel coincide por blob Git; ninguna fecha demuestra vigencia | Se conservan ambas versiones fijadas, fechas de consulta y huellas. No se “actualiza” un horario sin fuente nueva autorizada. |
| A09 Consistencia semántica de fuentes | Fuentes contiene 13 filas no vacías, de las que solo siete son imágenes y seis son criterios | Wiki y diccionario distinguen ambas categorías. No se afirma que existan trece avisos. |
| A10 Fechas y aceptación | Fechas reales en manifiestos/ejecuciones, metadato del Excel y fecha docente diferenciados | No se fabrican fechas de revisión; registro humano permanece pendiente. |

Referencias: [Excel y hojas](fuentes.md), [KPI](indicadores.md), [verificaciones](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json), [decisiones](../docs/decisiones_metodologicas.md). La inspección semántica fue realizada por IA y no es una aprobación humana. El HTML pide revisión antes de aceptar cambios; queda expresamente pendiente esa aceptación.

[Índice](index.md)

## Iteración después de incorporar JSON

Se confirmó mapeo íntegro de Frecuencias, 0 diferencias en la comparación, y se precisó que el JSON no exporta las otras tres hojas ni embebe vigencia/hash del libro. La potencial conversión de días nulos a false pertenece al comportamiento del exportador; no se observó en la base binaria actual. No se atribuye esa posibilidad a filas reales.

El resultado corregido de la auditoría previa fue [0 enlaces rotos en 168 enlaces locales](../evidencias/revision/enlaces_corregidos.json). Los archivos modificados y las diferencias se conservarán junto al estado posterior. Las revisiones finales amplían el control a nuevos documentos y a hashes, estructura, secuencia y reproducción. [Comparación de datos](../evidencias/segunda_ingesta/comparacion/comparacion.json) · [Registro de decisiones](../docs/decisiones_metodologicas.md).

## Corrección de cierre posterior al segundo estado

La [primera validación integral](../evidencias/revision/validacion_final/proyecto.json) aprobó 19 de 20 controles; detectó que README enlazaba el propio reporte antes de que el validador lo hubiera escrito. El destino quedó disponible al terminar, pero el orden hacía fallar la primera ejecución. Se corrigió el validador para registrar primero el inicio real, con resultado explícitamente pendiente, y guardar después el resultado completo. Se repitió la reproducción en una carpeta nueva, sin borrar el fallo: los cinco procesos finalizaron con exit_code 0 y la validación integral aprobó **20/20 controles** el 2026-11-03T21:22:31-04:00. Las [evidencias finales](../evidencias/revision/validacion_final_corregida/resultado.json) contienen códigos de salida y [detalle de comprobaciones](../evidencias/revision/validacion_final_corregida/proyecto.json). Este ajuste no cambia cálculos ni estados de las ingestas, que permanecen intactos.
