from statistics import mode
lista = []
for i in range(10):
    n = int(input('n: '))
    lista.append(n)

media = sum(lista) / len(lista)
mediana = (lista[4] + lista[5]) / 2

print(media)
print(mediana)
moda = mode(lista)
print(moda)

