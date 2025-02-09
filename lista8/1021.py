valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor_centavos = int(valor * 100)

print("NOTAS:")
for nota in notas:
    nota_centavos = int(nota * 100)  
    quantidade = valor_centavos // nota_centavos
    print(f"{quantidade} nota(s) de R$ {nota:.2f}")
    valor_centavos %= nota_centavos

print("MOEDAS:")
for moeda in moedas:
    moeda_centavos = int(moeda * 100)  
    quantidade = valor_centavos // moeda_centavos
    print(f"{quantidade} moeda(s) de R$ {moeda:.2f}")
    valor_centavos %= moeda_centavos
