t = int(input())

for i in range(t):
    n, m = [int(i) for i in input().split()]
    votosCandidatos = [0 for i in range(n)]
    votos = [int(i) for i in input().split()]

    for v in votos:
        votosCandidatos[v-1] += 1
    
    ganhador = -1

    for j in range(n):
        if votosCandidatos[j] > (m / 2):
            ganhador = j+1
            break

    print(ganhador)