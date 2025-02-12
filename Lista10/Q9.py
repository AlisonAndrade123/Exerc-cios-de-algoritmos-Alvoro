#9. Crie uma função recursiva para determinar se uma lista está ordenada.

def lista_ordenada(lista):
    if len(lista) <= 1:
        return True
    if lista[0] > lista[1]:
        return False
    return lista_ordenada(lista[1:])


print(lista_ordenada([1, 2, 3, 4, 5]))  
print(lista_ordenada([10, 20, 30, 25, 40]))  
print(lista_ordenada([7]))  
print(lista_ordenada([]))  
