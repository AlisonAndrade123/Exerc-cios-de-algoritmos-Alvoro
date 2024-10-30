# 13, 14, 15, 16, 17, 18, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print(f'{nome}{idade}')
print(f'{nome[0]}')
print(f'{nome[-1]}')
print(f'{len(nome)}')
if 'A' in nome.upper():
    print(f'O nome {nome} contem a letra A')
else:
    print(f'O nome {nome} não contem a letra A')
pontoDivisao = len(nome) // 2
primeiraParte = nome[:pontoDivisao]
segundaParte = nome[pontoDivisao:]
print("Primeira parte:", primeiraParte)
print("Segunda parte:", segundaParte)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
soma = n1 + n2
print(soma)
print(n1 * n2)
if n1 % 2 == 0:
    print('PAR')
else:
    print('IMPAR')
if n1 < 0:
    print('Negativo')
else:
    print('Positivo')
if n1 > n2:
    print(n1)
else:
    print(n2)
ano = int(input('Informe o ano: '))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('Bissexto')
else:
    print('Não Bissexto')
print(f'{nome[2]}')
for c in nome:
    print(c)
print()
print(f'{nome[1]}')
if nome[0] == 'a':
    print('O nome começa com A')
else: 
    print('O nome não começa com A')
if nome[-1] == 'a':
    print('O nome termina com A')
else: 
    print('O nome não termina com A')
texto = "banana"
novoTexto = ""
for caractere in texto:
    if caractere == "a":
        novoTexto += "o"
    else:
        novoTexto += caractere
print(novoTexto)
string1 = "Olá, "
string2 = "mundo!"
resultado = string1 + string2
print(resultado)
texto2 = "   Olá, mundo!   "
texto2SemEspacos = texto.strip()
print(f"'{texto2SemEspacos}'") 
string = input('Informe a palavra: ')
stringInvertido = string[::-1]
if string == stringInvertido:
    print('A palavra lida é um palíndromo.')
else:
    print('A palavra lida não é um palíndromo.')
cont = 0
for c in nome:
    if c == 'a':
        cont += 1
print(cont)
texto3 = "Olá, mundo! Como você está?"
texto3ComHifens = texto3.replace(" ", "-")
print(texto3ComHifens)
texto4 = input('Digite: ')
if texto4.isdigit():
    print("A string contém apenas dígitos.")
else:
    print("A string contém caracteres não numéricos.")
texto5 = input('Digite: ')
if texto.isalpha():
    print("A string contém apenas letras.")
else:
    print("A string contém caracteres não alfabéticos.")