palavra = input('Digite um palavra: ')
palavraInvertida = ''
for c in range(len(palavra) -1, -1, -1):
    palavraInvertida += palavra[c]
print(palavraInvertida)