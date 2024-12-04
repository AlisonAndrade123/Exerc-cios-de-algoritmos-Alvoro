def categoria_numero(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        if num % 2 == 0:
            return "Positivo e Par"
        else:
            return "Positivo e Ímpar"
    else:
        if num % 2 == 0:
            return "Negativo e Par"
        else:
            return "Negativo e Ímpar"

print(categoria_numero(10)) 
print(categoria_numero(11))  
print(categoria_numero(-6))
print(categoria_numero(-7))
print(categoria_numero(0)) 
