qn = int(input('Digite a qtde. de vezes: '))
for i in range(qn):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        print('PAR')
    elif n % 2 == 1:
        print('IMPAR')