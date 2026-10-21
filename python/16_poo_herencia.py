class Guerrero:
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

class Androide:
    nombre: str
    energia: int
    def __init__(self, nombre: str, energia: int):
        self.nombre= nombre
        self.energia = energia

    def mostrar_energia(self):
        print("Androide: ", self.nombre)
        print("Energia: ", self.energia)

class AndroideRecargable (Androide):
    def __init__(self, nombre: str, energia:int):
        super().__init__(nombre, energia)

    def recargar(self, cantidad:int):
        if cantidad > 0:
            self.energia += cantidad

androide17 = AndroideRecargable ("Numero 17", 600)
print("========ANTES DE RECARGAR===============")
androide17.mostrar_energia()
androide17.recargar (100)
print("========DESPUES DE RECARGAR========== ")
<<<<<<< HEAD
androide17.mostrar_energia()

class AlmacenSemillas:
    __cantidad: int

    def __init__(self, cantidad_inicial: int):
        if cantidad_inicial >= 0:
            self.__cantidad = cantidad_inicial
        else:
            self.__cantidad = 0

    def get_cantidad(self) -> int:
        return self.__cantidad

    def set_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def entregar_semillas(self, cantidad: int):
        if cantidad > 0 and cantidad <= self.__cantidad:
            self.__cantidad -= cantidad
            print(f"Se entregaron {cantidad} semillas con éxito.")
        else:
            print(f"No se pueden entregar {cantidad} semillas. Inventario insuficiente o cantidad inválida.")

# Crea un objeto con 10 semillas
almacen_karin = AlmacenSemillas(10)

print(f"Cantidad inicial en el almacén: {almacen_karin.get_cantidad()}")

# Realiza una entrega de 3 semillas a Goku y después intenta entregar 9 a Yajirobe
print(f"Goku solicita 3 semillas")
almacen_karin.entregar_semillas(3)

print("Yajirobe solicita 9 semillas")
almacen_karin.entregar_semillas(9)

# Muestra la cantidad final disponible
print(f"Cantidad final disponible en el almacén: {almacen_karin.get_cantidad()}")
=======
androide17.mostrar_energia()
>>>>>>> eae7082 (feat(2026-10-21): agregar proyecto django y actualizacion de python)
