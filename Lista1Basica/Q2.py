#4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
alturaString = str(altura)
print(alturaString)
alturaInt = int(altura)
print(alturaInt)
estudante = True
print(estudante)
if not nome:
    print("O nome está vazio.")
else:
    print("O nome não está vazio.")
if idade >= 18:
    print('Maior de idade.')
else:
    print('Menor de idade.')
mensagem = f'Meu nome é {nome} é minha idade é {idade}'
print(mensagem)
print(nome[0])
print(nome[-1])
caracteres = len(nome)
print(caracteres)
if 'a' in nome.lower():
    print(f'O nome {nome} contem a letra A')
else:
    print(f'O nome {nome} não contem a letra A')
pontoDivisao = len(nome) // 2
primeira_parte = nome[:pontoDivisao]
segunda_parte = nome[pontoDivisao:]
print("Primeira parte:", primeira_parte)
print("Segunda parte:", segunda_parte)
nomeMinusculas = nome.lower()
print(nomeMinusculas)
nomeMaiusculas = nome.upper()
print(nomeMaiusculas)
nome_invertido = nome[::-1]
print(nome_invertido)
string = input('Informe a palavra: ')
stringInvertido = string[::-1]
if string == stringInvertido:
    print('A palavra lida é um palíndromo.')
else:
    print('A palavra lida não é um palíndromo.')