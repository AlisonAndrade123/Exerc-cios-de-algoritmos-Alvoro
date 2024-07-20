from random import randint
from time import sleep

jogador_vitorias = 0
computador_vitorias = 0
while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 12)
    print(f'O computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 12)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('Jogador VENCE!')
            jogador_vitorias += 1
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
            computador_vitorias += 1
        else:
            print('JOGADA INVÁLIDA!')

    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE!')
            computador_vitorias += 1
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('Jogador VENCE!')
            jogador_vitorias += 1
        else:
            print('JOGADA INVÁLIDA!')

    elif computador == 2:
        if jogador == 0:
            print('Jogador VENCE!')
            jogador_vitorias += 1
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
            computador_vitorias += 1
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('JOGADA INVÁLIDA!')

    if jogador_vitorias == 3 or computador_vitorias == 3:
        break