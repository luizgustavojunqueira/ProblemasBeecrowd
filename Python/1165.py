n = int(input())

for i in range(n):
    x = int(input())

    numDivisores = 0
    for j in range(1, x+1):
        if x % j == 0:
            numDivisores += 1
    if numDivisores == 2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")