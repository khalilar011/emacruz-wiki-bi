# Consulta de negocio revisada técnicamente

Versión 1.0, tras primera ingesta y tres contrastes. **Pendiente de aprobación humana.** Pregunta: “¿Qué tan completa y consistente es la información disponible sobre días y horarios de recolección por sector o zona, y qué registros requieren revisión antes de utilizarse en Alerta Ruta?”

**Respuesta:** la información semanal es consistente en sus días, pero incompleta en horas. El Excel contiene **21 registros evaluables** (Frecuencias, filas 2–22). **6/21 = 28,57 %** cumplen el KPI documental v1.0: F07–F12, filas 8–13. Los otros **15/21 = 71,43 %** carecen de Fin y nueve también de Inicio. Son registros de programación, no distritos únicos, rutas físicas ni recojos ejecutados. [Tres verificaciones independientes](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json), [Excel original preservado](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), [reglas del KPI](indicadores.md).

Los **21 patrones semanales** concuerdan con Lun–Dom. F07–F10 (filas 8–11) contienen 20:00 → 04:00 y una nota explícita de madrugada siguiente; esas cuatro franjas son coherentes como cruce de día, de ocho horas. No se invierte ni completa ningún valor original. [Lectura independiente y controles adicionales](../evidencias/consulta_y_verificaciones/contraste/verificaciones.json), [hallazgos](hallazgos.md).

| Registros a revisar | Evidencia observada | Propuesta de acción, pendiente de persona |
| --- | --- | --- |
| F13–F21, filas 14–22 | Inicio y Fin No indicado | Recuperar ambas horas y confirmar vigencia antes de usar como programación exacta |
| F01–F06, filas 2–7 | Fin y sector No indicado | Obtener fin/sector sin deducir A/B por semejanza |
| F21, fila 22 | Zona No indicada en fila, distrito DM 15 | Aclarar zona/delimitación, sin asignar Norte/Sur |
| F17/F20, filas 18/21, con F16/F19 | Notas de posible solapamiento, no polígonos disponibles | Revisar mapas; no borrar como duplicados ni declarar contradicción demostrada |
| Todos, incluidos F07–F12 | Vigencia no acreditada y relación imagen → fila incompleta | Confirmar aviso original, período y autorización antes de decisión operativa |

Localización de cada fila y motivo: [detalle calculado](../evidencias/primera_ingesta/calculo_v1/registros_evaluados.csv); fuente primaria: [Excel](../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx), hoja Frecuencias y criterios Fuentes!A12:B16. La prioridad anterior es una inferencia de mantenimiento documental, sujeta a [revisión humana](../docs/revision_humana.md).

Por sector publicado: A tiene 6/6 filas que cumplen; B, 0/9; sin sector, 0/6. Son proporciones del archivo, no cobertura ni desempeño de EMACRUZ. Hay 12 registros sin distritos y 20 sin información de feriados, controles complementarios que no forman parte del KPI semanal por sector **o** zona. [Cálculo y desgloses](../evidencias/primera_ingesta/calculo_v1/analisis.json), [definición y límites](indicadores.md).

**Vacíos e incertidumbres:** las siete imágenes descritas en Fuentes!A2:E8 tienen vigencia No indicada y sus originales no están incorporados. La fecha interna del libro (2026-10-15T16:29:10Z) no acredita vigencia. No puede verificarse precisión cartográfica ni transcripción visual. Tampoco se puede responder sobre cumplimiento operativo, cobertura municipal, acumulación o predicción con estos datos. [Procedencia](../fuentes/procedencia.md), [fuentes](fuentes.md), [plan CRISP-DM existente](../fuentes/referencia_remota/docs/plan-crisp-dm.md).

**Resultado del contraste:** V1 (21 filas), V2 (15 sin Fin) y V3 (6 que cumplen, IDs y denominador) quedaron confirmadas mediante lectura directa XML independiente del analizador. No hubo correcciones numéricas que aplicar a la [respuesta inicial](../evidencias/consulta_y_verificaciones/respuesta_inicial.md). Se precisa aquí la separación entre prioridad documental y uso operativo, junto con tabla de acciones y alcance de los feriados. No se ha recibido aceptación humana ni se autoriza la incorporación operativa de estos horarios.

[Verificaciones](../evidencias/consulta_y_verificaciones/contraste/verificaciones.md) · [Índice](index.md)

## Actualización 2.0 tras la segunda ingesta

El diagnóstico numérico permanece igual. Se confirma que la representación JSON de Alerta Ruta conserva los mismos 21 registros y los faltantes: 0 diferencias en 399 valores, incluidos fila_origen y días booleanos. [Comparación](../evidencias/segunda_ingesta/comparacion/comparacion.json), [exportador fuente](../fuentes/referencia_remota/scripts/export_web_data.py).

Esta nueva evidencia permite afirmar fidelidad de exportación para la versión fijada; no permite afirmar vigencia o validez institucional. Las tres verificaciones originales siguen confirmadas. La decisión de usar o corregir registros continúa pendiente de persona. [Antes/después](../docs/comparacion_ingestas.md).
