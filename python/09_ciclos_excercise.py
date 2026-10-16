"""
control de Flota de naboo
"""
naves = [
    {
    "nombre": "Caza N-1",
    "combustible": 80,
    "droides": ["R2-D2","R2, A6"]
},
    {
     "nombre": "Caza Real",
    "combustible": 35,
    "droides": ["R2-N3"]
},
    { 
     "nombre": "Caza Real",
    "combustible": 65,
    "droides": ["R2-D2","R2, A6"]
}
]

naves_listas = 0
naves_recargada = 0
total_droides = 0
total_ciclos = 0
for numero, nave in enumerate (naves, start = 1):
    print(f"--- Nave: {numero}-{nave}")
    if nave ["combustible"]>=50:
        print("Estado inicial: LISTA")
        naves_listas += 1
    else:
        print("Estado inicial: RECARGAR")
        naves_recargada += 1
        ciclo = 0
        while nave ["combustible"] <= 50:
            ciclo += 1
            nave ["combustible"] += 10
        total_ciclos += ciclo
        print("Recarga Completada")
        print("Estado Final: LISTA")
    total_droides += len(nave["droides"])
    for droide in nave ["droides"]:
        print(f"droide:{droide}")

print("=================================")
print("RESUMEN")
print("=================================")
print(f"Total naves: {len(naves)}")
print(f"Naves listas inicialmente: {naves_listas}")
print(f"Naves recargadas: {naves_recargada}")
print(f"Total Droides: {total_droides}")
print(f"Total Ciclos: {total_ciclos}")