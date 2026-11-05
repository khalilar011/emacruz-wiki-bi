# Matriz de cumplimiento de la rúbrica docente

Referencia: [HTML docente, sección 5](../fuentes/consigna/Tarea_wiki_IA_proyecto_BI.html), fecha declarada 2026-11-03. Los puntos son los pesos de la rúbrica, no calificaciones obtenidas. No se asigna un total ni se simula evaluación docente. Estado de implementación local, contrastable mediante enlaces; la aceptación humana se registra aparte.

| Criterio | Peso | Estado | Evidencia concreta y límite |
| --- | --- | --- | --- |
| 1. Alineación con proyecto BI | 15 | Cumplido en implementación | [Objetivos existentes, usuarios, decisiones y resultados](../wiki/objetivos.md), [mapa objetivo → fuente → KPI → página → decisión](mapa_trazabilidad.md), pregunta respondida sin inventar cobertura o predicción |
| 2. Arquitectura y reglas de wiki | 15 | Cumplido en implementación | [AGENTS](../AGENTS.md), [fuentes con integridad](../fuentes/manifiesto.json), [índice enlazado](../wiki/index.md), [log](../wiki/log.md), auditoría de enlaces y control de privacidad/versiones |
| 3. Prompt adaptado y justificado | 10 | Cumplido en implementación | [Original íntegro, campos genéricos conservados](../prompts/prompt_inicial.md), [mejorado específico](../prompts/prompt_mejorado.md), [justificación](../prompts/justificacion_mejoras.md); comprobación automática contra el bloque HTML |
| 4. Ingesta y trazabilidad | 15 | Parcial: ejecución completa, aceptación humana pendiente | [Dos evidencias iniciales y estado real](../evidencias/primera_ingesta/resumen.md), [evidencia nueva y segundo estado](../evidencias/segunda_ingesta/resumen.md), hashes, [cambios](comparacion_ingestas.md). El HTML exige revisar modificaciones antes de aceptarlas: revisión IA realizada, aceptación por persona no recibida |
| 5. Calidad semántica y analítica | 10 | Cumplido en implementación | [KPI completo](../wiki/indicadores.md), [diccionario](../wiki/diccionario_datos.md), [hallazgos](../wiki/hallazgos.md), cálculo reproducible 6/21 y separación de hechos/inferencias. Pertinencia de reglas propuesta, pendiente de persona |
| 6. Consulta y verificación | 15 | Cumplido técnicamente | [Respuesta inicial y lectura del índice](../evidencias/consulta_y_verificaciones/lectura_y_afirmaciones.json), [tres verificaciones independientes](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json), [respuesta revisada](../wiki/consulta_negocio.md). Tres confirmadas; no se introdujeron errores artificiales |
| 7. Revisión e iteración | 10 | Cumplido en implementación | [Auditoría semántica y correcciones](../wiki/revision_calidad.md), [fallo de enlaces real](../evidencias/revision/enlaces_antes.json), [repetición corregida](../evidencias/revision/enlaces_corregidos.json), [estados antes/después](comparacion_ingestas.md), comparación Excel/JSON sin diferencias |
| 8. Próximos pasos y reproducibilidad | 10 | Cumplido en implementación | [Cinco respuestas y tres pasos con responsables propuestos/insumos/productos/criterios](../wiki/respuestas_paso_6.md), [README con comandos](../README.md), [validación integral](../evidencias/revision/validacion_final_corregida/resultado.json) y scripts sin dependencias |

**Pendientes deliberados:** elaborar y entregar el informe académico separado, publicar/inicializar Git en otra tarea y recibir las aprobaciones humanas que no han ocurrido. La falta de vigencia, imágenes, mapas o permiso institucional es una limitación real diagnosticada; no impide documentarla y reproducir el diagnóstico, pero sí limita uso operativo. No hay fuente imprescindible del cálculo sustituida por datos fabricados.

La autoevaluación de cumplimiento técnico no es aceptación de reglas o conclusiones de negocio. [Registro de revisión humana](revision_humana.md). Antes de entregar el informe, incorporar revisión personal y comprobar el texto del informe contra estas evidencias.

[Índice](../wiki/index.md)
