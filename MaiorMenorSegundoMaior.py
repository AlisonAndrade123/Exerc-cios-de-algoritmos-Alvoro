import math

maior_1 = -math.inf
maior_2 = 0
menor = math.inf

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        print(f'Maior número é {maior_1}')
        print(f'Segundo maior número é {maior_2}')
        print(f'Menor número é {menor}')
        break
    else:
        if n > maior_1:
            maior_2 = maior_1
            maior_1 = n
        elif n > maior_2:
            maior_2 = n
        if n < menor:
            menor = n