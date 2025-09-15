#Determinar si un numero es primo o no 

n1 = int(input("Digita un numero y te dire si es primo o no: "))

def Tio(n1):

    if n1 % 2 == 0:

        print(f"El numero {n1} no es primo")
    else:
        print(f"El numero {n1} es primo")

Tio(n1)
