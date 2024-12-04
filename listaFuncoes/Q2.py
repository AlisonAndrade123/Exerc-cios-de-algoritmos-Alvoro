def par_ou_impar(n):
    if n % 2 == 0:
        return f'PAR'
    elif n % 2 == 1:
        return f'IMPAR'
    
print(par_ou_impar(3))
s = par_ou_impar(int(input('')))
print(s)