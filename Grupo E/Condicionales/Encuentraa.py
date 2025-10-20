
num = [4, 7, 2, 7, 9, 7, 5, 2]


Incontrar = int(input("Escribe el número que quieres buscar: "))


if Incontrar in num:
    print("El número", Incontrar, "sí está en la lista.")


    primera_posicion = num.index(Incontrar)
    print("Está por primera vez en la posición:", primera_posicion)


    cantidad = num.count(Incontrar)

    if cantidad > 1:
        print("El número aparece", cantidad, "veces en total.")

        posiciones = []
        for i in range(len(num)):
            if num[i] == Incontrar:
                posiciones.append(i)

        print("Se encuentra en las posiciones:", posiciones)
    else:
        print("El número aparece solo una vez.")

else:
    print(" El número", Incontrar, "NO está en la lista.")
