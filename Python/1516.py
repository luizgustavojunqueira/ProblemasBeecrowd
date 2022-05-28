n, m = map(int, input().split())

while n != 0 and m != 0:
    matriz = []

    for i in range(n):
        matriz.append(input())

    a, b = map(int, input().split())

    tL, tC = int(a / n), int(b / m)

    novasLinhas = []

    for i in range(n):
        nL = []
        for k in range(m):
            nL.append(tC * matriz[i][k])
        for i in range(tL):
            novasLinhas.append(nL)

    for l in novasLinhas:
        print("".join(l))

    n, m = map(int, input().split())
    print()