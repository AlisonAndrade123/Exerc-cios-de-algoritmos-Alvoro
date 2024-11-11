texto = input("Digite uma string: ")

invertido = ""
indice = len(texto) - 1 

while indice >= 0:
    invertido += texto[indice]
    indice -= 1  

print(f"String invertida: {invertido}")
