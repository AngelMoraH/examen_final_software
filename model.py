from datetime import date

class Operaciones():
    numero_cuenta: str | None = None
    numero_destino: str | None = None
    fecha: str | None = None
    valor: float | None = None
    
    def __init__(self, numero_cuenta: str, numero_destino: str, fecha: str, valor : float):
        self.numero_cuenta=numero_cuenta
        self.numero_destino=numero_destino
        self.fecha=fecha
        self.valor=valor
        

class Cuenta():
    numero: str | None = None
    nombre: str | None = None
    saldo: int | None = 0
    contactos: list[str] | None = []
    operaciones: list[Operaciones] | None = []

    def __init__(self, numero: str,nombre: str, saldo: int, contactos: list[str]):
        self.numero=numero
        self.nombre=nombre
        self.saldo=saldo
        self.contactos=contactos
    
    def getEnvios(self)->list:
        return [ operacion for operacion in self.operaciones if operacion.numero_destino != self.numero ]
    
    def getRecepcion(self)->list:
        return [ operacion for operacion in self.operaciones if operacion.numero_destino == self.numero ]
    
    def historial(self)->object:
        return {"saldo":self.saldo,"operaciones":{"envio":self.getEnvios(),"recepcion":self.getRecepcion()}}
    def recepcion(self,monto,cuenta):
        recepcion = Operaciones(numero_cuenta=cuenta,numero_destino=self.numero,fecha=date.today().strftime('%d/%m/%Y'),valor=monto)
        self.operaciones.append(recepcion)
        self.saldo += monto
        return {"cuenta":self.numero,"cuenta de envio ":cuenta,"fecha":recepcion.fecha,"monto":recepcion.valor,"saldo restante":self.saldo},True
        
    def pagar(self,monto,destino)->object:
        
        if self.saldo<0:
            return {"mensaje":"No posee Saldo"},False
        if monto>self.saldo:
            return {"mensaje":"No posee suficiente saldo"},False
        if destino not in self.contactos:
            return {"mensaje":"No se encuentra numero destino en sus contactos"},False
        
        pago = Operaciones(numero_cuenta=self.numero,numero_destino=destino,fecha=date.today().strftime('%d/%m/%Y'),valor=monto)
        self.operaciones.append(pago)
        self.saldo -= monto
        return {"cuenta":self.numero,"cuenta destino":destino,"fecha":pago.fecha,"monto":pago.valor,"saldo restante":self.saldo},True
        
    

