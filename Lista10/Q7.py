def decimal_para_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_para_binario(n // 2) + str(n % 2)


print(decimal_para_binario(10))  
print(decimal_para_binario(25))  
