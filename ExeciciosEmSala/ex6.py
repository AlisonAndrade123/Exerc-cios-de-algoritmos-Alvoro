nome = input("Digite seu nome: ")
sexo = input('Digite seu sexo[M/F/O]: ')
ano = int(input('Digite seu ano de nascimento: '))
idade = 2024 - ano

if sexo in 'Ff':
    print(f'Olá {nome}, Você é uma mulher de {idade} anos')
elif sexo in 'Mm':
    print(f'Olá {nome}, Você é uma homem de {idade} anos')
elif sexo in 'Oo':
    print(f'Olá {nome}, Você não se indentifica com M ou F e tem {idade} anos')

if idade % 2 == 0:
    print('Sua idade é PAR')
else:
    print('Sua idade é ÍMPAR')

if ano % 4 == 0 or ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano que você nasceu é BISSEXTO')
else:
    print(f'O ano que você nasceu não é BISSEXTO')