'''def inverter(p):
    return p[::-1]

print(inverter('amor'))'''

def inverter(p):
    if len(p) <= 1:
        return p
    return p[-1] + inverter(p[:-1]) 

print(inverter('amor'))