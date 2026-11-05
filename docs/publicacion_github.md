# Publicación completada en GitHub

La wiki está publicada en el repositorio **público** [khalilar011/emacruz-wiki-bi](https://github.com/khalilar011/emacruz-wiki-bi), con rama principal `main`. El usuario confirmó este estado y el conector GitHub lo comprobó el 05/11/2026. La solicitud inicial contemplaba una entrega privada; ese estado fue reemplazado por la publicación pública ya realizada. No se cambió la visibilidad durante esta actualización documental.

| Elemento | Resultado comprobado al iniciar la actualización |
| --- | --- |
| Propietario | `khalilar011` |
| Visibilidad | Pública (`visibility: public`, consultado mediante el conector GitHub) |
| Rama principal | `main` |
| Remoto local `origin` | `https://github.com/khalilar011/emacruz-wiki-bi.git` |
| Commit inicial publicado | [`ed3a072299674d1bfff81edf7df7e99f13b48382`](https://github.com/khalilar011/emacruz-wiki-bi/commit/ed3a072299674d1bfff81edf7df7e99f13b48382) |
| Mensaje de ese commit | `Implementar wiki BI asistida por IA para EMACRUZ` |
| Comparación inicial local/remoto | GitHub confirmó `main` idéntica al commit local anterior: cero commits por delante y cero por detrás |

Esta revisión actualiza documentación y comentarios sobre la publicación. Conserva bases de datos, análisis, indicadores, scripts y evidencias académicas. El informe académico final se elaborará y entregará por separado.

## Alcance y permisos

El usuario comunicó que el repositorio ya estaba publicado con visibilidad pública y pidió actualizar la documentación. Se registra ese estado observado sin atribuirlo a una autorización de EMACRUZ o del docente. El permiso institucional, la autorización docente de redistribución, la licencia pública y la vigencia operativa siguen **No acreditados**. La disponibilidad pública en GitHub no demuestra esos permisos. Los archivos preservan nombres y metadatos académicos heredados; no se amplían en los resúmenes. Las reglas, conclusiones y aceptación de cambios IA siguen pendientes de [revisión humana](revision_humana.md).

Se incluyen originales, consigna, respuestas base64 y ZIP históricos porque forman parte de las evidencias requeridas y de los controles de integridad. Se inspeccionan también sus contenidos. No se modifican sus bytes ni se eliminan fallos anteriores. No se añaden imágenes de WhatsApp, conversaciones privadas, datos de vecinos, Word, PDF ni informe académico final.

## Antecedentes de preparación

Los problemas siguientes corresponden a intentos anteriores a la publicación confirmada. Los registros y errores se conservan como historia; no describen el estado actual del repositorio.

- No existía repositorio Git local. Se inicializó una raíz independiente con rama `main`, sin copiar historial ni `.git` del proyecto original.
- El `.gitignore` anterior excluía originales, documentación remota y ZIP necesarios para ejecutar las validaciones. Se adaptó para conservar la entrega y mantener exclusiones de secretos, entornos y temporales.
- El validador exigía ausencia de Git por corresponder a la etapa anterior. Se cambia ese control para comprobar independencia de la raíz Git y ausencia de repositorios anidados e informe Word/PDF. Los resultados históricos permanecen intactos.
- Se añade `.gitattributes` para evitar conversiones de fin de línea que invalidarían hashes de fuentes y evidencias al clonar.
- Git detectó propiedad distinta entre el usuario del equipo y la cuenta aislada del agente. Se utiliza `git -c safe.directory=<esta carpeta>` en cada comando; no se cambia la configuración global ni la identidad existente.
- El entorno denegó escrituras en `.git/config`: fallaron entonces la configuración local de `core.autocrlf` y el alta de `origin`. El remoto ya está configurado en la copia actual. `.gitattributes` protege los bytes independientemente de aquella configuración fallida.
- La primera auditoría nueva no reconoció todos los ejemplos ignorados: Windows convirtió el separador de entrada estándar en CRLF. Se corrige usando registros NUL en `git check-ignore -z --stdin`. Se conserva la salida inicial y se repite con otro nombre; ese fallo no afecta los resultados BI.
- Durante aquella reanudación, `git add` volvió a fallar al crear `.git/index.lock` por permiso denegado. En ese intento no se prepararon archivos en el índice ni se creó commit. La publicación posterior quedó confirmada por el commit inicial indicado arriba.

## Resultados locales ejecutados

La [reproducción inicial](../evidencias/publicacion/validacion_inicial/resultado.json) terminó antes de la interrupción. La ejecución corregida pendiente no había creado resultados; se reanudó sin sobrescribir evidencias. La [reproducción corregida](../evidencias/publicacion/validacion_corregida/resultado.json) completó cinco procesos con código 0: análisis, tres afirmaciones, comparación Excel/JSON, reglas y validación integral. El [control integral](../evidencias/publicacion/validacion_corregida/proyecto.json) pasó 20/20, los controles de reglas 10/10 y la comparación encontró cero diferencias en 399 valores. No se modificaron el KPI ni sus reglas analíticas.

La [auditoría inicial de publicación](../evidencias/publicacion/auditoria_inicial.json) conserva el fallo de separadores; la [corregida](../evidencias/publicacion/auditoria_corregida.json) pasó. Sus 136 candidatos corresponden al momento de esa ejecución, antes de guardar los resultados posteriores. Se inspeccionaron archivos, ZIP, XML/OOXML y respuestas base64: cero patrones de credenciales encontrados, once fuentes del manifiesto íntegras y ninguna excluida por error. Se compararon los 34 archivos del repositorio original, incluidos sus metadatos Git, con la captura de la auditoría inicial: todos idénticos. Los correos/metadatos académicos heredados no se reproducen en los resúmenes y se conservan con las fuentes; su redistribución sigue sujeta a revisión. La revisión de patrones es heurística.

El cierre comprobó también destinos de enlaces relativos contra el árbol candidato, con distinción de mayúsculas y minúsculas. La publicación fue confirmada posteriormente mediante GitHub; los conteos siguientes corresponden a aquellas ejecuciones y no se recalculan al actualizar la documentación.

La [auditoría de cierre](../evidencias/publicacion/auditoria_cierre.json) pasó: 152 candidatos en el momento de lectura, cero patrones de credenciales, fuentes íntegras, destinos relativos presentes y original idéntico. La [auditoría de enlaces](../evidencias/publicacion/enlaces_cierre.json) comprobó 373 enlaces locales sin destinos rotos, páginas wiki aisladas ni duplicados exactos. Los reportes generados después de inventariar candidatos incrementaron ese inventario. El [estado remoto registrado](../evidencias/publicacion/estado_remoto_reanudacion.json) describía commit y push pendientes durante aquel intento: se preserva como evidencia histórica, sin atribuirle el estado actual.

## Antecedentes de acceso remoto

En los intentos iniciales, `gh` estaba instalado (2.100.0). `gh auth status` terminó con código 1 e informó token inválido. La consulta `gh repo view` falló por conexión de socket no permitida hacia GitHub; no pudo distinguirse un fallo real de credencial de la imposibilidad de comprobarla por red. No se extrajeron tokens ni se escribieron credenciales en la carpeta.

En aquella etapa el conector GitHub reconoció a `khalilar011`, pero devolvió 404 al consultar el repositorio objetivo. El navegador no estaba disponible y la revisión automática rechazó el control de Chrome. Esos resultados se conservan en los registros anteriores; la consulta actual del conector sí confirma el repositorio, su visibilidad pública y su rama `main`.

**Publicación remota completada**: repositorio, visibilidad pública y commit inicial comprobados en GitHub. Las [evidencias de publicación](../evidencias/publicacion/) conservan sus estados y fechas originales; el [log](../wiki/log.md) registra la actualización documental sin sobrescribir los intentos anteriores.

## Comprobación de sincronización

Las actualizaciones de documentación se publican en `main` respetando el historial existente, sin `push --force`. La autenticación se gestiona fuera de los archivos del proyecto; no se incorporan contraseñas ni tokens.

La sincronización se comprueba contrastando el commit local con la cabeza remota y verificando que el árbol de trabajo quede limpio. Si se usa el conector como alternativa a la CLI, debe distinguirse la actualización remota de la sincronización del historial local y registrarse cualquier limitación real.

El proyecto `proyecto-emacruz` mantiene su repositorio e historial independientes. En esta tarea solo se trabaja dentro de `emacruz-wiki-bi`; no se modifican las bases, los análisis ni las evidencias académicas.

[Índice](../wiki/index.md) · [Procedencia](../fuentes/procedencia.md) · [Revisión humana](revision_humana.md)
