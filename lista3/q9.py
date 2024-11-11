numero = int(input("Digite um número para calcular seu fatorial: "))

fatorial = 1

contador = numero

while contador > 1:
    fatorial *= contador  
    contador -= 1 
print(f"O fatorial de {numero} é {fatorial}")
