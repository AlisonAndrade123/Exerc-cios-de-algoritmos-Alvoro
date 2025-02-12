#14. Escreva uma função recursiva para calcular a soma dos cubos dos primeiros n números naturais.

def soma_cubos(n):
    if n == 1:  
        return 1
    return n**3 + soma_cubos(n - 1)  

n = 4
print(soma_cubos(n))  