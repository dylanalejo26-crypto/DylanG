import random


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente



tam = random.randint(5, 10) 
head = None 


for i in range(tam):
    data = random.randint(0, 100)  
    head = Nodo(data, head)        


print("Valores en la lista enlazada:")
actual = head
while actual is not None:
    print(actual.dato, end=" → ")
    actual = actual.siguiente
print("None\n")


def get_MIN(head):
    if head is None:
        return None
    min_val = head.dato
    actual = head.siguiente
    while actual is not None:
        if actual.dato < min_val:
            min_val = actual.dato
        actual = actual.siguiente
    return min_val

def get_MAX(head):
    if head is None:
        return None
    max_val = head.dato
    actual = head.siguiente
    while actual is not None:
        if actual.dato > max_val:
            max_val = actual.dato
        actual = actual.siguiente
    return max_val


print(f"Cantidad de nodos creados: {tam}")
print(f"Valor mínimo en la lista: {get_MIN(head)}")
print(f"Valor máximo en la lista: {get_MAX(head)}")