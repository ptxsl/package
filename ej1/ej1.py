from Romano import Romano

numero=int(input("Inserta un número a romanizar: "))

funcion=Romano(numero)

print(f"{numero} : {funcion.romanizar()}")