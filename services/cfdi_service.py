from typing import List, Dict
from domain.cfdi import CFDIRecord


def clasificar_por_rfc(records: List[CFDIRecord], rfc: str) -> Dict[str, List[CFDIRecord]]:
    return {
        "ingresos": [r for r in records if r.es_ingreso(rfc)],
        "egresos": [r for r in records if r.es_egreso(rfc)],
    }