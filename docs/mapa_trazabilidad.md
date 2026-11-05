# Mapa objetivo → fuente → indicador → página → decisión

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

## Enlaces cerrados después de consulta e iteración

Aplicar herramientas de análisis → [tres verificaciones](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json) → [consulta revisada](../wiki/consulta_negocio.md) → priorizar registros con evidencia. Centralizar/analizar → [JSON y exportador](../wiki/comparacion_exportacion.md) → [399 comparaciones](../evidencias/segunda_ingesta/comparacion/comparacion.json) → conservar exportación fiel sin confundirla con vigencia. Generar información útil → [cinco respuestas y tres pasos](../wiki/respuestas_paso_6.md) → revisión y asignación humana pendientes.
