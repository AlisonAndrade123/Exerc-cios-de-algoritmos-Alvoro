#5. Crie uma função recursiva para encontrar o número de dígitos de um número inteiro.

def contar_digitos(n):
    if n == 0:  
        return 1
    if n < 10:  
        return 1
    return 1 + contar_digitos(n // 10)  


print(contar_digitos(999999923434))  
print(contar_digitos(12345))  
print(contar_digitos(0))  
print(contar_digitos(70000))  
