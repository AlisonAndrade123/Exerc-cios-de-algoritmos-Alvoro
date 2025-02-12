#12. Desenvolva uma função recursiva para imprimir uma lista de trás para frente.
def imprimir_reverso(lista, i=0):
    if i < len(lista):
        imprimir_reverso(lista, i + 1)  
        print(lista[i])  

lista = [1, 2, 3, 4, 5]
imprimir_reverso(lista)
