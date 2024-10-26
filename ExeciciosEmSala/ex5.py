nome = input("Digite seu nome: ")
sexo = input('Digite seu sexo[M/F/O]: ')
idade = int(input('Digite sua idade: '))

if sexo in 'Ff':
    print(f'Olá {nome}, Você é uma mulher de {idade} anos')
elif sexo in 'Mm':
    print(f'Olá {nome}, Você é uma homem de {idade} anos')
elif sexo in 'Oo':
    print(f'Olá {nome}, Você não se indentifica com M ou F e tem {idade} anos')