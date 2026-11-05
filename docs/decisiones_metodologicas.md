# Decisiones metodológicas

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
