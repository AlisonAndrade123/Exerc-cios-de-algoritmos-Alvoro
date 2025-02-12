#1. Crie uma função recursiva que retorne a soma dos primeiros `n` números naturais.

def soma_naturais(n):
    if n == 0:  
        return 0
    return n + soma_naturais(n - 1)  

print(soma_naturais(5))  
