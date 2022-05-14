n = int(input())

for i in range(n):
    x = int(input())

    alturas = list(map(int, input().split()))
    alturas.sort()

    for j in range(x):
        if j == x - 1:
            print(alturas[j])
        else:
            print(alturas[j], end = " ")