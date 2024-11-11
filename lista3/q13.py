n = int(input('Digite um número: '))
while n != 0:
    
    ehprimo = True

    if n <= 1:
        ehprimo = False

    for i in range(2, n):
        if n % i == 0:
            ehprimo = False
            break

    if ehprimo == True:
        print('EH PRIMO')
    else:
        print('NÃO É PRIMO')
        
    n = int(input('Digite um número: '))