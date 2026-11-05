# Objetivos, utilidad y pregunta BI

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
