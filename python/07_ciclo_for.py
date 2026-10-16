# ciclo for

naves=[
    "Caza N-1",
    "Nave real de Naboo",
    "Transporte"
]
for nave in naves:
    print("Inspecionando", nave)

print("inspección realizada")

rondas = []

print("Tipo de Rondas:", type (rondas))

for ronda in rondas:
    print(f"Ronda de vigilancia: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")

droides = range(1,17,3)

print("Tipo de Droides:", type(droides))
for droide in droides:
    print(f"Reparar : droide B1-{droide}")
    print(f"Tipo de dato droide : {type(droide)}")

planetas =[
    "Naboo",
    "Tatooine",
    "Coruscant"
]
recorrido = enumerate(planetas, start=1)

for posicion, planeta in recorrido:
    print(f"Destino{posicion}:{planeta}")
    print(f"Tipos de dato {type(posicion)}:{type(planeta)}")

paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos"
]

for pais in paises:
    if pais == "Chile":
       continue
    if pais == "Brasil":
       break
    print(f"Pais visitado:{pais}")

jedi ={}
jedi_activo = {
    "nombre": "Obiwan",
    "fuerza": "120",
    "estilo_pelea": "Samurai",
    "misiones": ["Guerra alderan", "secuestro palpatine", "escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana"
    }
}
print(jedi_activo)
nave = dict(nombre = "AZ-1", capacidad = 8, turbo_laser = 2)
print(nave)

jedi["nombre"] = "luck"
jedi["fuerza"] = 150
print(jedi)

for clave, valor in jedi_activo.items():
    print(f"{clave}{valor}")