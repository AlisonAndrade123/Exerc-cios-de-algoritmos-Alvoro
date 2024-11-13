soma = 0
multiplicacao = 1
while soma <= 100:
    n = float(input('Digite um número: '))
    soma += n
    multiplicacao *= n
print(multiplicacao)
print(soma)