N = int(input())

a, b = 0, 1

for i in range(N):
    if i < N - 1:
        print(a, end=" ")
    else:
        print(a)
    a, b = b, a + b
