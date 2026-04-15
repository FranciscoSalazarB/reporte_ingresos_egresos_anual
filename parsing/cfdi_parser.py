import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Optional

from domain.cfdi import CFDIRecord


NAMESPACES = {
    "cfdi": "http://www.sat.gob.mx/cfd/4",
    "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital",
}


def safe_float(value: Optional[str]) -> Optional[float]:
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def parse_fecha_iso(fecha: str) -> str:
    if not fecha:
        return ""
    try:
        return datetime.fromisoformat(fecha).isoformat(timespec="seconds")
    except ValueError:
        return fecha


def month_from_fecha(fecha: str) -> Optional[int]:
    try:
        return datetime.fromisoformat(fecha).month
    except:
        return None


def get_attr(node, attr):
    return node.attrib.get(attr, "") if node is not None else ""


def find(node, path):
    return node.find(path, NAMESPACES)


def parse_cfdi_xml(xml_path: Path) -> Optional[CFDIRecord]:
    try:
        root = ET.parse(xml_path).getroot()
    except ET.ParseError:
        return None

    # 🔥 usar namespace explícito (más robusto)
    emisor = root.find("{http://www.sat.gob.mx/cfd/4}Emisor")
    receptor = root.find("{http://www.sat.gob.mx/cfd/4}Receptor")
    timbre = root.find(".//{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital")

    fecha_raw = root.attrib.get("Fecha", "")
    fecha = parse_fecha_iso(fecha_raw)

    return CFDIRecord(
        version_cfdi=root.attrib.get("Version", ""),
        mes=month_from_fecha(fecha),
        fecha_emision=fecha,
        tipo_comprobante=root.attrib.get("TipoDeComprobante", ""),

        rfc_emisor=get_attr(emisor, "Rfc"),
        nombre_emisor=get_attr(emisor, "Nombre"),

        rfc_receptor=get_attr(receptor, "Rfc"),
        nombre_receptor=get_attr(receptor, "Nombre"),

        total=safe_float(root.attrib.get("Total")),

        uuid=get_attr(timbre, "UUID"),

        serie=root.attrib.get("Serie", ""),
        folio=root.attrib.get("Folio", ""),
        metodo_pago=root.attrib.get("MetodoPago", ""),
        forma_pago=root.attrib.get("FormaPago", ""),
        moneda=root.attrib.get("Moneda", ""),
        subtotal=safe_float(root.attrib.get("SubTotal")),
    )

def parse_cfdi_xml_debug(xml_path: Path) -> Optional[CFDIRecord]:
    try:
        root = ET.parse(xml_path).getroot()
        print(root.tag)
    except ET.ParseError:
        return None
    record = parse_cfdi_xml(xml_path)
    print(f"Parsed {xml_path}: {record}")
    return record