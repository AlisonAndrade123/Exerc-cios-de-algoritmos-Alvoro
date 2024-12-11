import statistics

numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8]

media = statistics.mean(numeros)

mediana = statistics.median(numeros)

moda = statistics.mode(numeros)

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
