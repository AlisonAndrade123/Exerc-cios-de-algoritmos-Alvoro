'''def potencia (x,y):
    return x**y

print(potencia(2,3))'''

def potencia(x, y):
    if y == 0:
        return 1
    return x * potencia(x, y-1)

print(potencia(2, 1))  
