lista = []

n = int(input('n: '))

while n != 0:
    lista.append(n)
    n = int(input('n: '))
    
lista.sort()
print(lista)
print(lista[0])
print(lista[-1])