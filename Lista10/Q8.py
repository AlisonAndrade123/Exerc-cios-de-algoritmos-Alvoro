#8. Desenvolva uma função recursiva para encontrar o máximo divisor comum de dois números.

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(48, 18))  
