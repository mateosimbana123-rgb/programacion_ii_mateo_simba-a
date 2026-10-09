# Operadores

'''
Operadores Aritméticos
+  (Suma)
-  (Resta)
*  (Multiplicación)
/  (División)
%  (Módulo)
** (Potenciación)
'''

valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
potencia = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)

print("Tabla de multiplicar del 5:")
multiplicador = 5
print(multiplicador,"x 1 =", multiplicador * 1)
print(multiplicador,"x 2 =", multiplicador * 2)
print(multiplicador,"x 3 =", multiplicador * 3)
print(multiplicador,"x 4 =", multiplicador * 4)
print(multiplicador,"x 5 =", multiplicador * 5)
print(multiplicador,"x 6 =", multiplicador * 6)
print(multiplicador,"x 7 =", multiplicador * 7)
print(multiplicador,"x 8 =", multiplicador * 8)
print(multiplicador,"x 9 =", multiplicador * 9)
print(multiplicador,"x 10 =", multiplicador * 10)

# 1. Solicitar el peso del paquete en kilogramos (permite decimales)
peso = float(input("Ingrese el peso del paquete en kilogramos: "))

# 2. Solicitar la zona de destino (número del 1 al 3)
zona = int(input("Ingrese la zona de destino (1, 2 o 3): "))

# 3. Calcular el costo según la zona
if zona == 1:
    precio_por_kilo = 5.0
    costo_total = peso * precio_por_kilo
# 4. Muestre en pantalla el costo final del envío
    print(f"El costo final del envío a la Zona 1 (América) es: ${costo_total:.2f}")

elif zona == 2:
    precio_por_kilo = 7.5
    costo_total = peso * precio_por_kilo
# 4. Muestre en pantalla el costo final del envío
    print(f"El costo final del envío a la Zona 2 (Europa) es: ${costo_total:.2f}")

elif zona == 3:
    precio_por_kilo = 10.0
    costo_total = peso * precio_por_kilo
# 4. Muestre en pantalla el costo final del envío
    print(f"El costo final del envío a la Zona 3 (Resto del mundo) es: ${costo_total:.2f}")

else:
# Mensaje de error si la zona no es válida (no realiza el cálculo)
    print("Error: La zona ingresada no es válida. Debe elegir un número entre 1 y 3.")