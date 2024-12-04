import matematica
import limpaTela

while opcaoDesejada != 5:
    limpaTela.limpaTela()

    print("""
    Selecione uma opção:
        
    1 - Adição
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
        
        """)

    opcaoDesejada = int(input("OPÇÃO: "))

    limpaTela.limpaTela()

    if opcaoDesejada >= 1 and opcaoDesejada != 5:
        numero1 = int(input("NÚMERO 1: "))
        numero2 = int(input("NÚMERO 2: "))

    resultado = 0

    match opcaoDesejada:
        case 1: 
            resultado = matematica.adicao(numero1, numero2)
        case 2:
            resultado = matematica.subtracao(numero1, numero2)
        case 3:
            resultado = matematica.multiplicacao(numero1, numero2)
        case 4:
            resultado = matematica.divisao(numero1, numero2)
        case 5: 
            parada = True
        case _:
            print("OPÇÃO INVALIDA")
        
    if parada == False:

        print(f'RESULTADO = {resultado}')

        limpaTela.limpaTela()
