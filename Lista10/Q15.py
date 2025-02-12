#15. Desenvolva uma função recursiva para determinar se uma sequência de parênteses é válida.

def parenteses(p, c = 0):
    if len(p) == 0:
        return c == 0
    e = p[0]
    if e == '(':
        return parenteses(p[1:], c + 1)
    elif e == ')':
        if c > 0:
            return parenteses(p[1:], c - 1)
        else:
            return False
    else:
        return parenteses(p[1:], c)
    
print(parenteses('()(()'))