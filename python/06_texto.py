#string cadenas de caracteres
jedi = "qui-Gon Jinn"
aprendiz = "Obi-Wan Kenobi"
droide = "R2-D2"
planeta = "Naboo"
codigo = "327"

print("El jedi es:", jedi)
print("El jedi es:", type(jedi))

print("El aprendiz es:", aprendiz)
print("El aprendiz es:", type(aprendiz))

print("El droide es:", droide)
print("El droide es:", type(droide))

print("El planeta es:", planeta)
print("El planeta es:", type(planeta))

print("El código es:", codigo)
print("El código es:", type(codigo))

#--------------------------------------------------------------------------------------

longitud_jedi = len(jedi)
print("La longitud del nombre del jedi es:", str(longitud_jedi))

longitud_aprendiz = len(aprendiz)
print("La longitud del nombre del aprendiz es:", str(longitud_aprendiz))
#---------------------------------------------------------------------------------------

mensaje = "La federacion de comercio ha establecido un bloqueo en Naboo"
print("El mensaje es:", mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayusculas es:", mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minusculas es:", mensaje_minusculas)

#_--------------------------------------------------------------------------------------
comunicado = "Los Jedi son enviados a Naboo"
print("El comunicado es:", comunicado)
nuevo_comunicado = comunicado.replace("Naboo", "Tatooine")
print("El nuevo comunicado es:", nuevo_comunicado)


planetas = "Naboo, Tatooine, Coruscant, ALderaan"
planetas_lista = planetas.split(", ")
print(planetas_lista)
print("La lista de planetas es:", str(planetas_lista))



droide = "R2-D2"
print("El droide es:", droide)
print("El primer caracter del droide es:", droide[0])
print("El segundo caracter del droide es:", droide[1])
print("El tercer caracter del droide es:", droide[2])
print("El cuarto caracter del droide es:", droide[3])
print("El quinto caracter del droide es:", droide[4])
print("El último caracter del droide es:", droide[-1])

planeta = "Naboo"
print("El planeta es:", + planeta)
print("EL planeta sin espacios es:", planeta.strip())