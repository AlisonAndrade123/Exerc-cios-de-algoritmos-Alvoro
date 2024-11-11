texto = input("Digite uma string: ")
caractere = input("Digite o caractere que deseja contar: ")

contador = 0
indice = 0

while indice < len(texto):
    if texto[indice] == caractere:
        contador += 1
    indice += 1

print(f"O caractere '{caractere}' aparece {contador} vezes na string.")
