entrada = input() 

p, j1, j2, r, a = map(int, entrada.split(" "))

escolhaJogador = p
numeroEscolhido1 = j1
numeroEscolhido2 = j2
roubou = bool(r)
acusado = bool(a)
resultado = 1 if (numeroEscolhido1 + numeroEscolhido2)%2 == 0 else 0

vitoria1 = roubou and not acusado
vitoria2 = not roubou and acusado and escolhaJogador == resultado
vitoria3 = escolhaJogador == resultado and not roubou and not acusado

vitoria = vitoria1 or vitoria2 or vitoria3

ganhador = 1 if vitoria else 2

print(f"Jogador {ganhador} ganha!")