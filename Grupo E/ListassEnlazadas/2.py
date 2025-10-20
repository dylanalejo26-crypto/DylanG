
import random


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



head = None


tam = random.randint(5, 10)
print("Se crearán", tam, "nodos.\n")


for i in range(tam):
    numero = random.randint(0, 100) 
    nuevo = Nodo(numero)              

    if head is None:
      
        head = nuevo
    else:
       
        actual = head
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

print("Los valores en la lista son:")
actual = head
while actual is not None:
    print(actual.dato, end=" → ")
    actual = actual.siguiente
print("None\n")


def sumar_lista(head):
    total = 0
    actual = head
    while actual is not None:
        total += actual.dato  
        actual = actual.siguiente
    return total



print("La suma total de los valores en la lista es:", sumar_lista(head))
