# Procedencia y conservación

Consulta inicial ejecutada: 2026-11-03T21:05:36-04:00 a 2026-11-03T21:05:36-04:00. Fechas UTC−04:00. El [manifiesto](manifiesto.json) conserva origen exacto, ruta copiada, consulta, versión y SHA-256 de cada archivo. [Registro remoto](../evidencias/recuperacion_remota_inicial.json): respuestas base64 y árbol con commit.

| Evidencia | Procedencia, versión y relación | Permisos y limitaciones |
| --- | --- | --- |
| [Excel](originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx) | Copia idéntica del repositorio local `proyecto-emacruz`, commit 29a44d875600d3ddc88fb53bafce80469902ce50. Blob Git coincide con el Excel del commit remoto 5fba63ec96844fa1373b6c5703fce54430b52de8. SHA-256: `cbc88d35f868abb898139e0e11f64dc134754a644d90430807ad701cae39b59a`. Modificación interna: 2026-10-15T16:29:10Z. | Uso y copia local académica solicitados por el usuario. Interlocutor institucional, autorización EMACRUZ, licencia y vigencia operativa no acreditados. Metadatos personales heredados presentes; revisar antes de publicar. |
| [README local](originales/README.md) y [README remoto](referencia_remota/README.md) | Objetivos existentes. Copias de versiones local/remota diferenciadas. | Evidencia de intención académica, no validación institucional. Nombres de equipo ya presentes; no se amplían datos personales. |
| [Documentación CRISP-DM](referencia_remota/docs/plan-crisp-dm.md), [historia SCRUM-22](referencia_remota/docs/historias/SCRUM-22.md), [fuentes](referencia_remota/docs/fuentes-datos.md), [datos](referencia_remota/data/README.md) | GitHub, commit remoto fijado arriba. Se comprueba blob Git al decodificar base64. Aclaran alcance y ausencia de permisos/vigencia. | La ficha de origen institucional sigue pendiente en el proyecto original. La historia es contexto, no una orden de crear el Excel piloto. |
| [AGENTS original](referencia_remota/AGENTS.md) | No existe en la copia local antigua; recuperado del mismo commit remoto. | Solo referencia documental. No se ejecutan sus acciones de Jira o publicación. |
| [Consigna HTML](consigna/Tarea_wiki_IA_proyecto_BI.html) y [texto extraído](consigna/texto_completo.txt) | Copia idéntica de Downloads. Autor del documento: Business Intelligence II, Unidad 3; fecha declarada 2026-11-03. | Uso académico local solicitado. No se deduce permiso de redistribución docente. El texto incluye todos los requisitos legibles, sin ejecutar scripts. |

La hoja Fuentes registra siete imágenes IMG01–IMG07 recibidas según sus nombres el 09/10/2026; las imágenes no están incorporadas a este proyecto. No se han comprobado visualmente los avisos ni se atribuye su transcripción a un organismo sin evidencia adicional. Hay otras seis filas de criterios metodológicos en esa hoja; no son seis imágenes más. Las fechas en nombres no son fechas de vigencia.

El árbol remoto localiza `web/data/frecuencias.json`, ausente localmente. Su contenido no se usa en esta primera ingesta. La segunda deberá documentar exportador y dependencia respecto al Excel antes de interpretar coincidencias.

[Fuentes de la wiki](../wiki/fuentes.md) · [Índice](../wiki/index.md)

## Segunda ingesta: JSON y exportador

Incorporación y consulta de esta sesión en [registro](../evidencias/segunda_ingesta/incorporacion.json). Se preservaron [frecuencias.json](referencia_remota/web/data/frecuencias.json) y [export_web_data.py](referencia_remota/scripts/export_web_data.py), commit 5fba63ec96844fa1373b6c5703fce54430b52de8. Se verificaron base64, blob Git y SHA-256, añadidos al [manifiesto](manifiesto.json).

El exportador declara dependencia del Excel/hoja Frecuencias: renombra once campos, convierte siete banderas a booleanos y añade fila_origen. La [comparación ejecutada](../evidencias/segunda_ingesta/comparacion/comparacion.json) confirma 378 valores originales y 21 coordenadas, sin diferencias y con reproducción idéntica de bytes. Las otras tres hojas no se exportan. La equivalencia no constituye corroboración institucional independiente. El JSON no contiene hash del libro ni fecha de exportación; su anclaje en esta wiki es el commit y la comparación conservada. Permiso de redistribución/vigencia sigue no acreditado.

## Entrega privada solicitada el 05/11/2026

El usuario solicita preparar Git y conservar estas fuentes en un repositorio independiente privado de su cuenta. Es una autorización del usuario para esa entrega académica; el permiso institucional, la licencia pública y la vigencia continúan **No acreditados**. No se incorporan nuevas fuentes ni se realiza una tercera ingesta. Los originales, respuestas base64 y ZIP históricos se mantienen byte a byte. Se revisan patrones de credenciales y contenidos comprimidos, sin retirar metadatos ni divulgar sus valores en los resúmenes. Las fuentes heredadas requieren revisión adicional antes de cualquier publicación pública. [Estado y evidencia de preparación](../docs/publicacion_github.md).
