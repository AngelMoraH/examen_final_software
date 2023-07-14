from fastapi import APIRouter
from bd import db_cuentas,get_cuenta_by_numero
router = APIRouter()

@router.get("/billetera/contactos")
def get_contactos(minumero:str|None=None):
    temp=[]
    if minumero is None:
        return {"message": "Faltan datos"}
    
    for cuenta in db_cuentas:
        if cuenta.numero == minumero:
            temp=cuenta.contactos
    for numero in temp:
        for cuenta in db_cuentas:
            if cuenta.numero == numero:
                return {"contactos": [f"{cuenta.numero}:{cuenta.nombre}"] }
        

#/billetera/pagar?minumero=21345&numerodestino=123&valor=100
@router.get("/billetera/pagar")
def pagar(minumero:str|None=None,numerodestino:str|None=None,valor:float|None=None ):
    if minumero is None or numerodestino is None or valor is None:
        return {"message": "Faltan datos"}
    cuenta = get_cuenta_by_numero(minumero)
    if cuenta != None:
        response,exito = cuenta.pagar(valor,numerodestino)
        if exito:
            cuenta2 = get_cuenta_by_numero(numerodestino)
            cuenta2.recepcion(monto=valor,cuenta=minumero)
            return f"Realizado en {response['fecha']}"
    
    return {"mensaje":"Operacion no realizada"}


#/billetera/historial?minumero=123
@router.get("/billetera/historial")
def get_historial(minumero:str|None=None):
    if minumero is None:
        return {"message": "Faltan datos"}
    cuenta = get_cuenta_by_numero(minumero)
    if cuenta is None:
        return {"message": "cuenta no encontrada"}
    return cuenta.historial()
