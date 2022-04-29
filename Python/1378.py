#Memory Limite Exceeded - But it works

n = int(input())

while n > 0:

    pontos = []
    combinacoes = []

    for i in range(n):
        pontos.append(list(map(int, input().split())))

    for i in range(n-1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                combinacoes.append([pontos[i], pontos[j], pontos[k]])

    totalTriangulos = 0

    for c in combinacoes:
        dist1 = ((c[1][0] - c[0][0]) ** 2 + (c[1][1] - c[0][1]) ** 2) ** (1/2)
        dist2 = ((c[2][0] - c[0][0]) ** 2 + (c[2][1] - c[0][1]) ** 2) ** (1/2)
        dist3 = ((c[2][0] - c[1][0]) ** 2 + (c[2][1] - c[1][1]) ** 2) ** (1/2)

        if (dist1 == dist2 and dist2 != dist3) or (dist3 == dist2 and dist2 != dist1) or (dist1 == dist3 and dist1 != dist2):
            totalTriangulos += 1

    print(totalTriangulos)

    n = int(input())