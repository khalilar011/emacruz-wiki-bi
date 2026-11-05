# Preparación del repositorio independiente

Solicitud recibida el 05/11/2026: preparar y publicar `khalilar011/emacruz-wiki-bi` en GitHub, inicialmente **privado**. URL objetivo: https://github.com/khalilar011/emacruz-wiki-bi. Una URL objetivo no prueba que el repositorio exista ni que se haya subido contenido.

## Alcance y permisos

La solicitud autoriza el depósito académico privado de esta entrega y sus fuentes para conservar su reproducibilidad. Sustituye la prohibición de crear Git de la etapa inicial. La autorización procede del usuario; no se atribuye a EMACRUZ ni al docente. El permiso institucional, la licencia de redistribución pública y la vigencia operativa siguen **No acreditados**. No cambiar a público ni agregar colaboradores sin revisar estos asuntos. Los archivos preservan nombres y metadatos académicos heredados; no se amplían en los resúmenes.

Se incluyen originales, consigna, respuestas base64 y ZIP históricos porque forman parte de las evidencias requeridas y de los controles de integridad. Se inspeccionan también sus contenidos. No se modifican sus bytes ni se eliminan fallos anteriores. No se añaden imágenes de WhatsApp, conversaciones privadas, datos de vecinos, Word, PDF ni informe académico final.

## Problemas observados y correcciones

- No existía repositorio Git local. Se inicializó una raíz independiente con rama `main`, sin copiar historial ni `.git` del proyecto original.
- El `.gitignore` anterior excluía originales, documentación remota y ZIP necesarios para ejecutar las validaciones. Se adapta para la entrega privada y conserva exclusiones de secretos, entornos y temporales.
- El validador exigía ausencia de Git por corresponder a la etapa anterior. Se cambia ese control para comprobar independencia de la raíz Git y ausencia de repositorios anidados e informe Word/PDF. Los resultados históricos permanecen intactos.
- Se añade `.gitattributes` para evitar conversiones de fin de línea que invalidarían hashes de fuentes y evidencias al clonar.
- Git detectó propiedad distinta entre el usuario del equipo y la cuenta aislada del agente. Se utiliza `git -c safe.directory=<esta carpeta>` en cada comando; no se cambia la configuración global ni la identidad existente.
- El entorno denegó escrituras en `.git/config`: fallaron la configuración local de `core.autocrlf` y el alta de `origin`. No se afirma que el remoto esté configurado. `.gitattributes` protege los bytes independientemente de esa configuración fallida.
- La primera auditoría nueva no reconoció todos los ejemplos ignorados: Windows convirtió el separador de entrada estándar en CRLF. Se corrige usando registros NUL en `git check-ignore -z --stdin`. Se conserva la salida inicial y se repite con otro nombre; ese fallo no afecta los resultados BI.
- Tras reanudar, `git add` volvió a fallar al crear `.git/index.lock` por permiso denegado. No se prepararon archivos en el índice, no existe commit y no se intentó un push sin esos requisitos.

## Resultados locales ejecutados

La [reproducción inicial](../evidencias/publicacion/validacion_inicial/resultado.json) terminó antes de la interrupción. La ejecución corregida pendiente no había creado resultados; se reanudó sin sobrescribir evidencias. La [reproducción corregida](../evidencias/publicacion/validacion_corregida/resultado.json) completó cinco procesos con código 0: análisis, tres afirmaciones, comparación Excel/JSON, reglas y validación integral. El [control integral](../evidencias/publicacion/validacion_corregida/proyecto.json) pasó 20/20, los controles de reglas 10/10 y la comparación encontró cero diferencias en 399 valores. No se modificaron el KPI ni sus reglas analíticas.

La [auditoría inicial de publicación](../evidencias/publicacion/auditoria_inicial.json) conserva el fallo de separadores; la [corregida](../evidencias/publicacion/auditoria_corregida.json) pasó. Sus 136 candidatos corresponden al momento de esa ejecución, antes de guardar los resultados posteriores. Se inspeccionaron archivos, ZIP, XML/OOXML y respuestas base64: cero patrones de credenciales encontrados, once fuentes del manifiesto íntegras y ninguna excluida por error. Se compararon los 34 archivos del repositorio original, incluidos sus metadatos Git, con la captura de la auditoría inicial: todos idénticos. Los correos/metadatos académicos heredados no se reproducen en los resúmenes y se conservan con las fuentes para la entrega privada autorizada. La revisión de patrones es heurística.

El cierre comprueba también destinos de enlaces relativos contra el árbol candidato, con distinción de mayúsculas y minúsculas. La verificación desde GitHub y del README renderizado permanece pendiente hasta que exista publicación confirmada.

La [auditoría de cierre](../evidencias/publicacion/auditoria_cierre.json) pasó: 152 candidatos en el momento de lectura, cero patrones de credenciales, fuentes íntegras, destinos relativos presentes y original idéntico. La [auditoría de enlaces](../evidencias/publicacion/enlaces_cierre.json) comprobó 373 enlaces locales sin destinos rotos, páginas wiki aisladas ni duplicados exactos. Los reportes generados después de inventariar candidatos incrementan ese inventario; no son archivos ya preparados en el índice. El [estado remoto registrado](../evidencias/publicacion/estado_remoto_reanudacion.json) mantiene commit y push pendientes por los bloqueos descritos.

## Acceso remoto y estado

`gh` está instalado (2.100.0). `gh auth status` terminó con código 1 e informó token inválido. La consulta `gh repo view` falló por conexión de socket no permitida hacia GitHub; no se puede distinguir un fallo real de credencial de la imposibilidad de comprobarla por red. No se extraen tokens ni se escriben credenciales en la carpeta.

El conector GitHub reconoció a `khalilar011`, pero devolvió 404 al consultar el repositorio objetivo: puede ser inexistente o no accesible para la instalación. El conector disponible no ofrece creación de repositorios. El acceso del navegador no estaba disponible, y la revisión automática rechazó el control de Chrome con el motivo «Computer Use was not approved to use Google Chrome». No se elude ese rechazo.

**Publicación remota pendiente**: no se confirma repositorio creado, visibilidad remota, commit remoto ni push. Las comprobaciones locales se registran en [evidencias de publicación](../evidencias/publicacion/) con fechas reales; el [log](../wiki/log.md) registra las operaciones. Esta página se actualizará únicamente ante resultados reales.

## Reanudación segura

La autenticación se realiza fuera de los archivos del proyecto mediante el [procedimiento oficial de GitHub CLI](https://cli.github.com/manual/gh_auth_login): `gh auth login --hostname github.com --git-protocol https --web`, y después `gh auth status`. Si persiste el bloqueo de red del entorno, debe restablecerse el acceso autorizado antes de reintentar. No enviar contraseñas ni tokens al agente.

Consultar primero `gh repo view khalilar011/emacruz-wiki-bi --json name,owner,isPrivate,defaultBranchRef,url`. Ante 404 autenticado, confirmar que el repositorio no existe antes de crearlo privado. Si existe, inspeccionar ramas e historial y no sobrescribir trabajo remoto. No utilizar `push --force`. El remoto local puede apuntar a la URL objetivo aun cuando la creación remota siga pendiente.

Una vez creado y revisado el remoto, ejecutar `git push -u origin main`, confirmar que el hash remoto coincide con el local y revisar árbol, README y enlaces. El estado local no prueba esa comprobación remota.

[Índice](../wiki/index.md) · [Procedencia](../fuentes/procedencia.md) · [Revisión humana](revision_humana.md)
