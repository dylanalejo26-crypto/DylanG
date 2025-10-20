#Pregunta cuanto tiene y decir cuanto le falta o sobra para comprar el celular de 1 millon 
celular = 1000000
dinero = int(input("Digita cuanto dinero tienes para comprar el celular que vale COP1'000.000: "))

def Calculo(celular, dinero):
    
    if dinero < celular:
       m =  celular-dinero
       print(f" Te hace falta COP{m} para comprar el celular")
    else:
        m = dinero-celular
        print(f" Te sobran COP{m} para comprar el celular")

Calculo(celular, dinero)