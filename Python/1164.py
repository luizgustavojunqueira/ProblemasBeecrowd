n = int(input())

for i in range(n):
    x = int(input())

    somaDivisores = 0
    for j in range(1, x):
        if x % j == 0:
            somaDivisores += j
    
    if somaDivisores == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")