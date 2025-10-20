def Acomule (n):
    if n == 0:
        return 0
    else:
        return n + Acomule(n-1)
print(Acomule(5))
