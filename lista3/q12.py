contador = 1

while contador <= 100:
    if contador % 17 == 0:
        print(f"Número divisível por 17 encontrado: {contador}")
        break  
    print(contador)
    contador += 1
