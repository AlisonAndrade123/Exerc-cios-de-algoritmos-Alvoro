import random
n = int(input('Digite cara ou coroa [1 para cara e 2 para coroa]: '))
numero1 = random.randint(1, 2)
if numero1 == 1:
    print('cara')
    if n == numero1:
        print('Voce acertou!')
    elif n != numero1:
        print('Voce errou!')
else:
    print('coroa')
    if n == numero1:
        print('Voce acertou!')
    elif n != numero1:
        print('Voce errou!')