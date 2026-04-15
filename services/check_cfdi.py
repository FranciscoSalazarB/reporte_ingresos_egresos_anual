import requests

URL = "https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc"

def consultar_cfdi(uuid, rfc_emisor, rfc_receptor, total):
    import requests

    url = "https://consultaqr.facturaelectronica.sat.gob.mx/ConsultaCFDIService.svc"

    expresion = f"?re={rfc_emisor}&rr={rfc_receptor}&tt={total}&id={uuid}"

    # 🔥 CLAVE: escapar XML
    expresion_xml = expresion.replace("&", "&amp;")

    soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                      xmlns:tem="http://tempuri.org/">
       <soapenv:Header/>
       <soapenv:Body>
          <tem:Consulta>
             <tem:expresionImpresa>{expresion_xml}</tem:expresionImpresa>
          </tem:Consulta>
       </soapenv:Body>
    </soapenv:Envelope>"""

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://tempuri.org/IConsultaCFDIService/Consulta"
    }

    response = requests.post(url, data=soap_body.encode("utf-8"), headers=headers)

    return response.text

if __name__ == "__main__":
    uuid = "0F42DAFF-D573-47E3-AA46-C65C04C02204"
    rfc_emisor = "MOMM801103TLA"
    rfc_receptor = "PCL170614SY5"
    total = "1740.00"

    result = consultar_cfdi(uuid, rfc_emisor, rfc_receptor, total)
    print(result)