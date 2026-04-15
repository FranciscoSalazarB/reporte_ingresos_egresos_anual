from dataclasses import dataclass
from typing import Optional, List, Any


@dataclass
class CFDIRecord:
    version_cfdi: str = ""
    mes: Optional[int] = None
    fecha_emision: str = ""
    tipo_comprobante: str = ""
    rfc_receptor: str = ""
    nombre_receptor: str = ""
    rfc_emisor: str = ""
    nombre_emisor: str = ""
    serie: str = ""
    folio: str = ""
    uuid: str = ""
    metodo_pago: str = ""
    imp_local_trasladado: Optional[float] = None
    forma_pago: str = ""
    moneda: str = ""
    tipo_cambio: Optional[float] = None
    subtotal: Optional[float] = None
    iva_trasladado8: Optional[float] = None
    iva_trasladado16: Optional[float] = None
    ieps_trasladado: Optional[float] = None
    ieps_trasladado_cuota: Optional[float] = None
    total_impuestos_retenidos: Optional[float] = None
    iva_retenido: Optional[float] = None
    isr_retenido: Optional[float] = None
    descuento: Optional[float] = None
    total: Optional[float] = None
    estatus: str = ""
    cfdi_relacionados: str = ""
    fecha_cancelacion: str = ""
    estatus_cancelacion: str = ""
    imp_local_retenido: Optional[float] = None
    conceptos: str = ""
    regimen_fiscal_emisor: str = ""
    residencia_fiscal_receptor: str = ""
    imp_local_importe_traslado: Optional[float] = None
    tiene_iva_exento: str = ""
    base_tasa_cero: Optional[float] = None
    ieps_retenido_cuota: Optional[float] = None
    domicilio_fiscal_receptor: str = ""

    def to_row(self) -> List[Any]:
        return list(self.__dict__.values())

    def es_ingreso(self, rfc: str) -> bool:
        return self.rfc_emisor == rfc

    def es_egreso(self, rfc: str) -> bool:
        return self.rfc_receptor == rfc