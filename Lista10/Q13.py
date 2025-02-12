#13. Implemente uma função recursiva para calcular a soma dos quadrados dos primeiros n números naturais.

def soma_quadrados(n):
    if n == 1:  
        return 1
    return n**2 + soma_quadrados(n - 1)  

n = 4
print(soma_quadrados(n))  
