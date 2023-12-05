n = int(input())

for i in range(n):

    qt, s = [int(i) for i in input().split()]
    valores = [int(i) for i in input().split()]

    menorDiferenca = abs(s - valores[0])
    posMenorDiferenca = 0

    for j in range(qt):
        if abs(s - valores[j]) < menorDiferenca:
            menorDiferenca = abs(s - valores[j])
            posMenorDiferenca = j
        
    print(posMenorDiferenca + 1)