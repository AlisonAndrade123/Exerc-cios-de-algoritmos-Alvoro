def verificar_presenca(numero, lista):
    if numero in lista:
        return True
    else:
        return False

lista_numeros = [1, 2, 3, 4, 5]
numero = 3

resultado = verificar_presenca(numero, lista_numeros)
print(f"O número {numero} está na lista? {resultado}")
