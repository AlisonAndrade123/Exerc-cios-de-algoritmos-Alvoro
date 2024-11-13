n1 = int(input('n1: '))
n2 = int(input('n2: '))
operacao = input('Digite a operação: [+,-,/,*] ')
if operacao == '+':
    print(n1 + n2)
elif operacao == '-':
    print(n1 - n2)
elif operacao == '/':
    print(n1 / n2)
elif operacao == '*':
    print(n1 * n2)
else:
    print('Operação inválida!')