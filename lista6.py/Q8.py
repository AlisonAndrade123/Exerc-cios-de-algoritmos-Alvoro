def verifica_maioridade(idade):
    if idade >= 18:
        return f"Maior de idade"
    else:
        return f"Menor de idade"

print(verifica_maioridade(12))
print(verifica_maioridade(18))