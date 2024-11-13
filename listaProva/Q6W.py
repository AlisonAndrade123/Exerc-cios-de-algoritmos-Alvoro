n = int(input('Digite um número: '))
fatorial = 1
cont = 1
while cont <= n:
    fatorial *= cont
    cont += 1
print(fatorial)