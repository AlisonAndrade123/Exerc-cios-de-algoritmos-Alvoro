#6. Implemente uma função recursiva para calcular o MDC (máximo divisor comum) de dois números.

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(48, 18)) 
print(mdc(4,6)) 
