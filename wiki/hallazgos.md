# Hallazgos verificables

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

## Versión 2.0: qué confirmó la evidencia nueva

**Cálculo/observación técnica:** el [JSON incorporado](../fuentes/referencia_remota/web/data/frecuencias.json) conserva las 21 filas, las ausencias horarias y las notas de medianoche. Hubo 0 diferencias en 399 valores comparados; la proyección coincide byte por byte. [Resultado reproducible](../evidencias/segunda_ingesta/comparacion/comparacion.json).

**Cambio de conocimiento:** en la primera ingesta no se había comprobado si Alerta Ruta conservaba la programación del Excel. Ahora se confirma la fidelidad de esta exportación y la ausencia de las hojas complementarias en el JSON. No se encontraron nuevos hechos operativos ni correcciones a horarios. El KPI, prioridades y limitaciones permanecen iguales. Es una dependencia técnica confirmada, no una segunda fuente independiente de EMACRUZ.

**Pendiente adicional de mantenimiento:** el JSON no embebe fecha de exportación ni hash del Excel; se propone añadirlos en una tarea futura del repositorio original, con autorización. La wiki no modifica ese exportador.
