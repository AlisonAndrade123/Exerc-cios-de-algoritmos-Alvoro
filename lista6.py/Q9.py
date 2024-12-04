def fatorial(n):

    fatorial = 1

    contador = n

    while contador > 1:
        fatorial *= contador  
        contador -= 1 
    return f"O fatorial de {n} é {fatorial}"

n = int(input("Digite um número para calcular seu fatorial: "))
print(fatorial(n))
