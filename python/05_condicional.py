# Condicional if
# simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")
    
# Condicional if-else

creditos = int(input("Ingrese la cantidad de créditos que tiene: "))
precio_repuesto = int(input("Ingrese el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficiente crédito para comprar el repuesto")
    
# if anidado

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran créditos")
    else:
        print("Te quedas justo con los créditos necesarios")
else:
    print("No tienes suficiente crédito para comprar el repuesto")
    
# Condicional if-elif-else

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto y te quedas justo con los créditos necesarios")
else:
    print("No tienes suficiente crédito para comprar el repuesto")