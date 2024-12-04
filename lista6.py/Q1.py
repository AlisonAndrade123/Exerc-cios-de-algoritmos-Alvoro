def multiplicacao(*n):
    resultado = 1
    for numero in n:
        resultado *= numero
    return resultado

print(multiplicacao(1,2,3,4,5))