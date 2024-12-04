import math

def verifica_quadrado_perfeito(n):
    if n < 0:
        return f"{n} Não é um quadrado perfeito é um número negativo"
    raiz = int(math.sqrt(n))
    if raiz ** 2 == n:
        return f"{n} é um quadrado perfeito."
    else:
        return f"{n} não é um quadrado perfeito."

print(verifica_quadrado_perfeito(4)) 
print(verifica_quadrado_perfeito(2)) 