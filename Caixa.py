import os
nome = str(input('Digite seu nome: '))
cpf = str(input('Digite seu CPF: '))
saldo = 1000
saldo2 = 0

while True:
    print('''Escolha uma das opçoes a seguir: 
      1. Depositar
      2. Sacar
      3. Transferir
      4. Consultar saldo
      5. Sair''')
    opcao = str(input())
    if opcao == '1':
        depositar = int(input('Digite valor a ser depositado: R$'))
        saldo += depositar
    elif opcao == '2':
        sacar = int(input('Digite o valor a ser sacado: R$'))
        saldo -= sacar
    elif opcao == '3':
        transferir = int(input('Digite um valor para transferência: R$'))
        saldo -= transferir
        saldo2 += transferir
    elif opcao == '4':
        print(f'Seu saldo é: R${saldo}')
        print(f'O saldo da pessoa 2 é: R${saldo2}')
    elif opcao == '5':
        os.system('cls')
        break
        
