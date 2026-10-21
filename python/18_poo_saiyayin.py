<<<<<<< HEAD
from 17_poo_guerrero import Guerrero

Class Saiyayin (Guerrero):
=======
from poo_guerrero import Guerrero

class Saiyayin (Guerrero):
>>>>>>> eae7082 (feat(2026-10-21): agregar proyecto django y actualizacion de python)
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi poderoso nombre es:", self.nombre)

class Saiyajin (Guerrero):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def transformarse(self):
        print(self.nombre, "se transforma en Super Saiyajin")

goku = Saiyajin ("Goku")
goku.presentarse()
goku.transformarse()