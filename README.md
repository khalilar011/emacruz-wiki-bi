# EMACRUZ – Wiki de conocimiento BI asistida por IA

Implementación académica independiente de Alerta Ruta, Business Intelligence II, Unidad 3, consigna 03/11/2026. Navegación: [wiki/index.md](wiki/index.md). La programación publicada permite diagnosticar calidad documental; no acredita servicio ejecutado, vigencia institucional ni predicción de acumulación.

Se ejecutaron dos ingestas reales: primero Excel y objetivos/documentación; después, JSON y exportador de Alerta Ruta. Los estados se preservaron antes de consultar/auditar e incorporar la segunda evidencia. Las conclusiones propuestas requieren [revisión humana](docs/revision_humana.md). La publicación fue completada en el repositorio **público** [khalilar011/emacruz-wiki-bi](https://github.com/khalilar011/emacruz-wiki-bi), con rama principal `main`; ver [estado y comprobaciones](docs/publicacion_github.md). El informe académico final se elaborará por separado. El repositorio original no se modifica.

## Estructura

```text
emacruz-wiki-bi/
  fuentes/      originales, documentación remota fijada, consigna y hashes
  wiki/         índice, objetivos, fuentes, diccionario, KPI, hallazgos,
                consulta, comparación, revisión, respuestas del paso 6 y log
  prompts/      original docente, versión EMACRUZ y justificación
  evidencias/   primera_ingesta/ (inspección, cálculo y estado.zip)
                consulta_y_verificaciones/ (inicial y tres contrastes)
                segunda_ingesta/ (antes/después, comparación y diffs)
                revision/ (auditorías y validación_final/)
  scripts/      lectura, cálculos, verificaciones, enlaces y reproducción
  docs/         decisiones, mapa, comparación, rúbrica y revisión humana
  AGENTS.md
  README.md
  requirements.txt
  .gitignore
  .gitattributes
```

## Fuentes y resultados reales

Excel y README copiados del repositorio local original (commit 29a44d875600d3ddc88fb53bafce80469902ce50). Documentación, JSON y exportador recuperados de [GitHub](https://github.com/khalilar011/proyecto-emacruz/tree/5fba63ec96844fa1373b6c5703fce54430b52de8), fijados al commit 5fba63ec96844fa1373b6c5703fce54430b52de8. El blob del Excel local coincide con el remoto. HTML docente de Downloads, versión declarada 03/11/2026. [Procedencia y permisos](fuentes/procedencia.md), [hashes y rutas exactas](fuentes/manifiesto.json).

El Excel contiene Frecuencias (21 filas), Distritos (16), Servicios (11) y Fuentes (13 filas no vacías: siete imágenes referenciadas y seis criterios). El KPI de programación semanal completa y válida es **6/21 = 28,57 %**, IDs F07–F12. Quince carecen de Fin, nueve de Inicio, seis de sector y una de zona; 21/21 patrones semanales concuerdan. Se reconocieron cuatro cruces nocturnos explícitos. Cero IDs duplicados y cero filas exactamente duplicadas. [Definición, filtros y límites](wiki/indicadores.md), [detalle por fila](evidencias/primera_ingesta/calculo_v1/registros_evaluados.csv).

Las tres afirmaciones comprobadas (21 filas, 15 sin Fin y 6/21 con IDs) quedaron confirmadas por lectura XML independiente. La segunda ingesta contrastó 399 valores, incluidos 378 valores originales y 21 coordenadas: **cero diferencias**, con proyección de bytes idéntica al JSON. El KPI permanece igual. [Consulta](wiki/consulta_negocio.md), [comparación de exportación](wiki/comparacion_exportacion.md), [antes/después](docs/comparacion_ingestas.md).

No se mide cobertura ni cumplimiento real de recolección. Vigencia, permisos institucionales, imágenes originales, límites cartográficos y relación detallada distrito → frecuencia siguen sin acreditación suficiente. Su ausencia es un resultado del diagnóstico. Las fuentes existentes no bastan para predecir acumulación o medir toneladas. Las conclusiones son propuestas para revisión humana.

## Instalación y reproducción

Python 3.10 o posterior; ejecución original con Python 3.14.3 en Windows. No requiere paquetes externos ni acceso de red para analizar las fuentes ya copiadas. Desde esta carpeta:

```powershell
python --version
# Opcional: entorno aislado, sin necesidad de activar scripts PowerShell.
python -m venv .venv
# requirements.txt contiene solo comentarios: no hay paquetes externos.
.venv/Scripts/python.exe -m pip install -r requirements.txt
python -X utf8 scripts/reproducir.py --salida salidas/reproduccion_01
```

La reproducción ejecuta análisis, tres verificaciones independientes, comparación Excel/JSON, diez controles de reglas y validación integral. Conserva comandos, fechas, stdout/stderr, códigos de salida y JSON de resultados. Se verifican además integridad de copias y ZIP, secuencia de ingestas, prompt contra HTML, estructura/contenido, ocho criterios y enlaces Markdown propios. Si el repositorio original está accesible, se comparan sus archivos de trabajo con los hashes iniciales. En otro equipo se utilizan las copias preservadas; el control del original se informa como no disponible, sin inventar una comprobación.

Comandos individuales, desde raíz, usando nombres de salida nuevos:

```powershell
python -X utf8 scripts/analizar.py --salida salidas/analisis_nuevo
python -X utf8 scripts/verificar_afirmaciones.py --salida salidas/contraste_nuevo
python -X utf8 scripts/comparar_excel_json.py --salida salidas/comparacion_nueva
python -X utf8 scripts/verificar_reglas.py --salida salidas/reglas_nuevas.json
python -X utf8 scripts/auditar_enlaces.py --salida salidas/enlaces_nuevos.json
python -X utf8 scripts/validar_proyecto.py --salida salidas/proyecto_nuevo.json
python -X utf8 scripts/comparar_estados.py --antes evidencias/segunda_ingesta/antes --despues evidencias/segunda_ingesta/despues --salida salidas/diff_nuevo
```

Usar una carpeta nueva en cada ejecución: los scripts no sobrescriben evidencias históricas. El contraste independiente verifica las afirmaciones históricas guardadas. Para otra versión de datos hay que registrar nuevas afirmaciones antes de verificarlas y conservar las anteriores. Los scripts de primera/segunda ingesta son registro reproducible de preparación de esta sesión y rechazan reejecución sobre historia ya congelada. No regenerar dos ingestas desde un único estado final.

La [validación ejecutada de cierre](evidencias/revision/validacion_final_corregida/resultado.json) y [controles detallados](evidencias/revision/validacion_final_corregida/proyecto.json) permiten revisar lo que efectivamente se ejecutó. La [matriz de cumplimiento](docs/matriz_cumplimiento.md) contiene los ocho criterios, evidencias y estado sin asignar nota docente. [Registro cronológico](wiki/log.md).

## Errores corregidos y pendientes

Se corrigió un paréntesis antes de ejecutar la preparación, el perfil que confundía 0 con ausencia (sin cambiar KPI), una errata del prompt sobre duplicados y cuatro enlaces relativos en la evidencia de verificaciones. Se conservan [análisis inicial con fallo](evidencias/primera_ingesta/calculo/analisis.json), [corrección](evidencias/primera_ingesta/calculo_v1/analisis.json), [auditoría fallida](evidencias/revision/enlaces_antes.json) y [repetición sin enlaces rotos](evidencias/revision/enlaces_corregidos.json). El [primer cierre](evidencias/revision/validacion_final/proyecto.json) obtuvo 19/20 porque el propio informe enlazado todavía no se había guardado durante la comprobación. Se corrigió el orden de escritura del reporte y se repitió toda la reproducción en carpeta nueva, sin borrar el fallo.

Pendientes humanos: aceptar cambios IA, aprobar reglas y conclusiones, confirmar vigencia/transcripción/territorio y permisos de redistribución pública. Roles propuestos sin asignación ficticia en [revisión humana](docs/revision_humana.md) y [tres próximos pasos](wiki/respuestas_paso_6.md). El informe separado no se incluye. La publicación en GitHub conserva la historia analítica y no cambia el KPI.

Las fuentes y ZIP de estados contienen copias originales y metadatos heredados; `.gitignore` incluye esas evidencias y excluye secretos, cachés y temporales. `.gitattributes` conserva los bytes exactos al clonar. La visibilidad pública fue confirmada por el usuario y comprobada en GitHub. Esa disponibilidad no acredita permiso institucional de EMACRUZ, autorización docente de redistribución, licencia pública ni vigencia: esas revisiones siguen pendientes. Ver [publicación GitHub](docs/publicacion_github.md), [método](docs/decisiones_metodologicas.md) y [AGENTS](AGENTS.md).

Para repetir el control de archivos y publicación, usando una salida nueva:

```powershell
python -X utf8 scripts/auditar_publicacion.py --salida salidas/publicacion_nueva.json
```

La auditoría revisa candidatos de Git, exclusiones, hashes, repositorios anidados y patrones de credenciales, incluidos ZIP/OOXML y respuestas base64. Es un control heurístico; no certifica permisos ni ausencia absoluta de secretos. Los resultados actuales se conservan en [evidencias/publicacion](evidencias/publicacion/).
