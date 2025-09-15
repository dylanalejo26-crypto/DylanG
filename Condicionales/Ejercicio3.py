#Solicita 3 numeros al usuario y decir cual es el d

def numero_medio(n1, n2, n3):
    if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
        return n1
    elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3):
        return n2
    else:
        return n3
n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
n3 = int(input("Digite el tercer numero: "))    

medio = numero_medio(n1, n2, n3)

print(f"El numero del medio es: {medio}")
