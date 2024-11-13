n = int(input("Quantos números: "))

primeiro = 0
segundo = 1

contador = 0

while contador < n:
    print(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo  
    contador += 1
