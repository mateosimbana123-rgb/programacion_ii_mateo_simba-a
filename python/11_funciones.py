## FUNCIONES
def activar_sistema():
    print("==sistema de naboo==")
    print("sistema de control activado")

activar_sistema()

# Funciones con parametro

def saludar_jedi(nombre):
    print(f" Que la fuerza te acompañe : {nombre}")

saludar_jedi ("Qui-Gon Jim")
saludar_jedi ("Obi-Wan Kenobi")

def mostrar_nave(nombre, combustible):
    print(f"Nave: {nombre} - Combustible: {combustible}")

mostrar_nave("Caza N-1", 80)

#Funciones que devuelven dato o informacion
# return

def calcular_combustible(inicial, consumo):
    restante = inicial - consumo
    return restante

def calcular_combustible_2(inicial, consumo):
    restante = inicial - consumo
    return restante

resultado = calcular_combustible(100,25)
print(f"Combustible: {resultado}")

resultado = calcular_combustible_2(100,35)
print(f"Combustible: {resultado}")

print(f"Combustible: {calcular_combustible_2(100,15)}")