#2. Crie uma função recursiva que verifique se uma string é um palíndromo.

def palindromo(p):
    if len(p) <= 1:  
        return True
    if p[0] != p[-1]:  
        return False
    return palindromo(p[1:-1])  

print(palindromo("radar"))  
print(palindromo("python"))  
print(palindromo("ana"))  
