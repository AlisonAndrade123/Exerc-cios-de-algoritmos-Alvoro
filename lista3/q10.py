texto = input("Digite uma string: ")


vogais = "aeiouAEIOU"
contador = 0
indice = 0

while indice < len(texto):
    if texto[indice] in vogais:
        contador += 1
    indice += 1

print(f"Número de vogais na string: {contador}")
