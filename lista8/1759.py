valor = int(input())

saida = ''

for i in range(valor):
    if i != valor -1:
        saida += 'Ho '
    else: saida += 'Ho!'

print(saida)