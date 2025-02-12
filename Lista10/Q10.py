#10. Desenvolva uma função recursiva para calcular o produto dos elementos de uma lista.

def produto(l):
    if len(l) == 0:  
        return 1
    return l[0] * produto(l[1:])  


print(produto([2, 3, 4]))  
print(produto([5, 1, 10]))  
print(produto([7]))  
print(produto([]))  
