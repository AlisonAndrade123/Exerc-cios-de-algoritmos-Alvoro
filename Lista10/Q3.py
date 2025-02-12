#3. Desenvolva uma função recursiva que conte o número de ocorrências de um caractere específico em uma string.

def contar_ocorrencias(p, c):
    if not p:  
        return 0
    return (p[0] == c) + contar_ocorrencias(p[1:], c)  

print(contar_ocorrencias('amor', 'a'))  
print(contar_ocorrencias('banana', 'a'))  
print(contar_ocorrencias('teste', 'e'))  

    