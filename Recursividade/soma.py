'''def soma(a, b):
    a += 1
    b += 1
    return soma(a,b)

soma(1,2)'''

def soma(n):
    if n == 0:
        return 0
    return (n % 10) + soma(n // 10)

print(soma(896))


