import argparse
from pathlib import Path

from ingestion.filesystem import collect_xml_files
from parsing.cfdi_parser import parse_cfdi_xml, parse_cfdi_xml_debug
from services.cfdi_service import clasificar_por_rfc
from reports.excel_report import build_excel_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--rfc", required=True)

    args = parser.parse_args()

    input_dir = Path(args.input)
    files = collect_xml_files(input_dir)

    print(f"first file found: {files[0] if files else 'N/A'}")
    parse_cfdi_xml_debug(files[0]) if files else print("No files to debug")

    records = [r for f in files if (r := parse_cfdi_xml(f))]

    data = clasificar_por_rfc(records, args.rfc)
    print(f"Registros encontrados: {len(records)}")
    print(f"Registros clasificados: {len(data['ingresos']) + len(data['egresos'])}")
    print(f"primer registro encontrado: {records[0] if records else 'N/A'}")
    wb = build_excel_report(data)
    wb.save(args.output)

    print(f"Procesados: {len(records)}")


if __name__ == "__main__":
    main()