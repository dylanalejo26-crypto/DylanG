#Recibe Numeros Hasta Hber uno Negativo 
while True:
    n = int(input("Digite un número (negativo para salir): "))
    if n < 0:
        print("Programa finalizado.")
        break
    else:
        print(f"Digitaste: {n}")
