def soma_ate_zero():
    soma = 0  
    numero = int(input("Digite um número (ou 0 para sair): "))
    while numero != 0:  
        soma += numero  
        numero = int(input("Digite um número (ou 0 para sair): ")) 
    return soma  


print(soma_ate_zero())

