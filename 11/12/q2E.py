def elementos_unicos(lista):
    return list(set(lista))

lista_com_repetidos = [1, 2, 2, 3, 4, 4, 5]
unicos = elementos_unicos(lista_com_repetidos)
print(f"Elementos únicos: {unicos}")
