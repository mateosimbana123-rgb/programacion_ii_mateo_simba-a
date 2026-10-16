print("===== CONTROL DE ENERGIA === ")
energia_texto = "ochenta"

try:
    energia = int(energia_texto)
    print(energia)
except ValueError:
    print("Error debe ser numerico")

    
print("Fin del sistema")
"""
ValueError
TypeError
KeyError
IndexError
ZeroDivisionError
"""

def calcular_energia(total, cantidad):
    try:
        resultado = total / cantidad
    except ZeroDivisionError as Error:
        print("Error: division entre cero")
        return None
    except TypeError:
        print("Error: division entre cero")
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1:", calcular_energia(100,4))
print("Caso 2:", calcular_energia(100,0))
print("Caso 3:", calcular_energia(100,"cuatro"))


print("==========DIAGNÓSTICO R2-D2========== ")
try:
    energía = int("cuatro")
    imprimir("energía", energía)
except ValueError: 
    print("Error de lectura")
else:
    print("diagnóstico completado")
finally:
    print("Cerrando diagnostico")


def validar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser numero entero")
    if energia<0 or energia<100:
        raise ValueError("La energia debe estar entre 0 y 100")
    return energia


try:
    resultado = validar_energia(60)
    print("Energia",resultado)
except (TypeError, ValueError) as error:
    print("Error:", error)