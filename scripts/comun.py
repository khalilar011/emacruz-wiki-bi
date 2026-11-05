"""Lectura OOXML sin dependencias, utilidades y reloj real. Nunca escribe fuentes."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import hashlib
import json
import posixpath
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / 'fuentes/originales/data/Base_Emacruz_sectores_y_frecuencias.xlsx'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def ahora():
    return datetime.now(timezone(timedelta(hours=-4))).isoformat(timespec='seconds')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def guardar(path, contenido):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contenido, encoding='utf-8', newline='\n')

def json_out(path, data):
    guardar(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def leer_excel(path=XLSX):
    """Lee valores OOXML sin aplicar formato. Rechaza fórmulas y encabezados ambiguos.
    Conserva filas Excel para trazabilidad. No infiere fechas desde estilos.
    """
    with ZipFile(path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(si.itertext()) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels = {r.attrib['Id']: r.attrib['Target'] for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        book = ET.fromstring(z.read('xl/workbook.xml'))
        sheets = {}
        for sheet in book.find('m:sheets', NS):
            target = rels[sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
            target = target.lstrip('/') if target.startswith('/') else posixpath.normpath('xl/' + target)
            xml = ET.fromstring(z.read(target))
            rows = []
            cell_types = {}
            for row in xml.findall('m:sheetData/m:row', NS):
                vals = {}
                for c in row:
                    coord = c.attrib['r']
                    letters = ''.join(x for x in coord if x.isalpha())
                    index = 0
                    for ch in letters:
                        index = index * 26 + ord(ch) - 64
                    if c.find('m:f', NS) is not None:
                        raise ValueError(f'Fórmula no soportada en {sheet.attrib["name"]}!{coord}')
                    v = c.find('m:v', NS)
                    val = v.text if v is not None else None
                    typ = c.attrib.get('t', 'n')
                    if typ == 's' and val is not None:
                        val = strings[int(val)]
                    elif typ == 'inlineStr':
                        val = ''.join(c.find('m:is', NS).itertext())
                    elif val is not None and typ in ('n', 'b'):
                        val = float(val) if '.' in val else int(val)
                    vals[index] = val
                    cell_types[coord] = typ
                if any(v is not None and str(v).strip() for v in vals.values()):
                    rows.append((int(row.attrib['r']), vals))
            if not rows:
                sheets[sheet.attrib['name']] = {'columns': [], 'rows': [], 'dimension': None}
                continue
            headers = [rows[0][1].get(i) for i in range(1, max(rows[0][1]) + 1)]
            if None in headers or len(headers) != len(set(headers)):
                raise ValueError('Encabezados vacíos o repetidos')
            records = []
            for n, values in rows[1:]:
                if max(values, default=0) > len(headers):
                    raise ValueError('Datos fuera de encabezados')
                records.append({'_fila_excel': n, **{str(h): values.get(i) for i, h in enumerate(headers, 1)}})
            dimension = xml.find('m:dimension', NS)
            sheets[sheet.attrib['name']] = {'columns': headers, 'rows': records, 'dimension': dimension.attrib.get('ref') if dimension is not None else None, 'cell_types': cell_types}
        core = ET.fromstring(z.read('docProps/core.xml'))
        metadata = {c.tag.split('}')[-1]: c.text for c in core}
    return {'sheets': sheets, 'metadata': metadata}

def log(operacion, detalle):
    p = ROOT / 'wiki/log.md'
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text('# Registro cronológico de operaciones\n\nFechas reales con desplazamiento UTC−04:00 (America/La_Paz). Operador: agente IA Codex. Aprobaciones humanas registradas por separado.\n\n[Índice](index.md)\n', encoding='utf-8')
    with p.open('a', encoding='utf-8') as f:
        f.write(f'\n## {ahora()} — {operacion}\n\n{detalle}\n')
