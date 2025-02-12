#4. Crie uma função recursiva para calcular o valor mínimo e máximo em uma lista de números.

def limites(l, max, min):
    if len(l) == 0:
        return[max, min]
    e = l[0]
    if min == None or e < min:
        min = e
    if max == None or e > max:
        max = e
    return limites(l[1:], max,min)

print(limites([3, 1, 7, 0, 5], None, None))  
print(limites([-10, 4, 2, 9], None, None))   
print(limites([8], None, None)) 