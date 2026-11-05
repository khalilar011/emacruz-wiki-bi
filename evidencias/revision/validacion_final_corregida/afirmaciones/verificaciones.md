# Tres verificaciones sustantivas

Ejecución real: 2026-11-03T21:22:30-04:00. [Script independiente](../../../../scripts/verificar_afirmaciones.py), [fuente](../../../../fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) y [detalle JSON](verificaciones.json). Afirmaciones capturadas antes del contraste en [respuesta inicial](../../../../evidencias/consulta_y_verificaciones/respuesta_inicial.md).

## V1: confirmada

Afirmación: 21 registros evaluables en Frecuencias. Fuente/localización: Frecuencias!A2:R22.

Procedimiento: Contar filas XML no totalmente vacías después de encabezado, preservando coordenadas; no usar dimensión o recuento de otras hojas.

Resultado observado: `21`. Corrección: no requerida.

## V2: confirmada

Afirmación: 15 registros con Fin ausente. Fuente/localización: Frecuencias!Q2:Q22.

Procedimiento: Leer columna Q y reconocer nulo, vacío y marcadores de ausencia. Registrar celdas e IDs.

Resultado observado: `15`. Corrección: no requerida.

## V3: confirmada

Afirmación: 6 de 21 cumplen KPI v1.0: F07–F12, 28,57 %. Fuente/localización: Frecuencias!A2:R22; notas R8:R11.

Procedimiento: Reconstruir controles desde celdas: IDs, duplicados, sector/zona, delimitación, turno, vocabulario de días contra G:M, horas y cruce explícito. Comparar IDs, numerador y denominador, sin llamar al analizador.

Resultado observado: `{"numerador": 6, "denominador": 21, "ids": ["F07", "F08", "F09", "F10", "F11", "F12"]}`. Corrección: no requerida.

Los tres contrastes confirman las cifras iniciales, sin introducir errores deliberados. La verificación técnica no aprueba conclusiones operativas. Los cuatro cruces son F07–F10; se obtuvieron además 21 días concordantes.

[Índice](../../../../wiki/index.md)
