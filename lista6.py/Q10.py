def verifica_palindromo(string):

    stringInvertido = string[::-1]
    
    if string == stringInvertido:
        return f'A palavra lida é um palíndromo.'
    else:
        return f'A palavra lida não é um palíndromo.'

palavra = input('Informe a palavra: ')
print(verifica_palindromo(palavra))