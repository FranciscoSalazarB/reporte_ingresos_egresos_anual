from pathlib import Path
from typing import List


def collect_xml_files(input_dir: Path) -> List[Path]:
    return sorted([p for p in input_dir.rglob("*.xml") if p.is_file()])