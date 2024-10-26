numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
else:
    if numero1 < numero2 and numero1 < numero3:
        print(numero1)
if numero2 > numero1 and numero1 > numero3:
    print(numero2)
else:
    if numero2 < numero1 and numero1 < numero3:
        print(numero2)
if numero3 > numero1 and numero3 > numero2:
    print(numero3)
else:
    if numero3 < numero1 and numero3 < numero2:
        print(numero3)