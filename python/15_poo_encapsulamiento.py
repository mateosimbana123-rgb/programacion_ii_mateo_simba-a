class Guerrero:
    nombre: str
    _poder: int

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self._poder = poder

    def get_poder(self):
        return self._poder

vegeta = Guerrero("vegeta", 8000)
print("Guerrero:", vegeta.nombre)
print("Poder:", vegeta.get_poder())


class CuentaZeni:
    titular: str
    _saldo: int

    def __init__(self, titular: str, _saldo: int):
        self.titular = titular
        self._saldo = _saldo
    
    def get_saldo(self):
        return self._saldo

    def retirar_dinero(self, cantidad:int):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print("Retiro realizado", cantidad)
        else:
            print("Retiro no permitido")

cuenta = CuentaZeni("Mr. Satán", 5000)
print("Titular:", cuenta.titular)
print("saldo inicial", cuenta.get_saldo())
cuenta.retirar_dinero(500)
print("saldo final", cuenta.get_saldo())

