N = int(input())

for _ in range(N):
    X = int(input())  
    if X == 0:
        print("NULL")  
    else:
        if X % 2 == 0:
            parImpar = "EVEN"
        else:
            parImpar = "ODD"
        
        if X > 0:
            negativoPositivo = "POSITIVE"
        else:
            negativoPositivo = "NEGATIVE"
        
        print(f"{parImpar} {negativoPositivo}")