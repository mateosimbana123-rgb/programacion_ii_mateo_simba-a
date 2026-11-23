combustible = 100
vuelta = 1

while combustible >= 20: 
    print(f"vuelta{vuelta}")
    print(f"combustible inicial:{combustible}")

    combustible -= 20
    print(f"combustible restante:{combustible}")
    vuelta += 1

print(" Carrera finalizada")