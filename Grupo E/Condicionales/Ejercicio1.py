
import math
def operaciones(a, b):
    if a > b:   
        return f"{a} elevado a la {b} es: {a ** b}"
    elif a < b:
        return (f"Raíz cuadrada de {a} es: {math.sqrt(a)}\n"
                f"Raíz cuadrada de {b} es: {math.sqrt(b)}")
    else:      
        suma = a + b
        return (f"La suma es: {suma}\n"
                f"Seno: {math.sin(suma)}\n"
                f"Coseno: {math.cos(suma)}\n"
                f"Tangente: {math.tan(suma)}")


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print(operaciones(a,b))