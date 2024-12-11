def contar_palavras(frase):
    palavras = frase.split()  
    return len(palavras)  

frase = "Este é um exemplo de frase"
quantidade = contar_palavras(frase)
print(f"A quantidade de palavras na frase é: {quantidade}")
