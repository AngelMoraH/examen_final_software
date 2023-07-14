from model import Cuenta

cuenta = Cuenta(numero="918273475",nombre="Juan",saldo=100000,contactos=["456789123"])
cuenta2 = Cuenta(numero="456789123",nombre="Jean",saldo=100000,contactos=["918273475"])


db_cuentas: list[Cuenta] = [cuenta,cuenta2]



def get_cuenta_by_numero(numero):
    return next((c for c in db_cuentas if c.numero == numero), None)