def classificar_riqueza(salario):
    if salario < 1000:
        return "Baixa Renda"
    elif 1000 <= salario < 5000:
        return "Média Renda"
    elif 5000 <= salario < 10000:
        return "Alta Renda"
    elif 10000 <= salario < 100000:
        return "Rico"
    elif 100000 <= salario < 1000000:
        return "Milionário"
    elif 1000000 <= salario < 1000000000:
        return "Bilionário"
    else:
        return "Trilionário"

print(classificar_riqueza(300))
print(classificar_riqueza(4000))
print(classificar_riqueza(8000))
print(classificar_riqueza(25000))
print(classificar_riqueza(500000))
print(classificar_riqueza(500000000))
print(classificar_riqueza(50000))
