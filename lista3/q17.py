numero = float(input("Digite um número (ou 's' para parar): "))
menor = numero  

while True:
    entrada = input("Digite outro número (ou 's' para parar): ")
    if entrada.lower() == 's':  
        break
    numero = float(entrada)
    if numero < menor:  
        menor = numero

print(f"O menor número digitado foi: {menor}")
