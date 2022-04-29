n = int(input())

for i in range(n):
    maior = 0
    maiorpos = 0
    menor = 11
    menorpos = 0
    
    nome = input()
    gd = float(input())

    notas = list(map(float, input().split()))

    for j in range(7):
        if notas[j] > maior:
            maior = notas[j]
            maiorpos = j
        if notas[j] < menor:
            menor = notas[j]
            menorpos = j

    if maiorpos < menorpos:
        notas.pop(maiorpos)
        notas.pop(menorpos-1)
    else:
        notas.pop(menorpos)
        notas.pop(maiorpos-1)

    notaFinal = 0

    for j in range(5):
        notaFinal += notas[j]
    
    notaFinal *= gd

    print(f"{nome} {notaFinal:.2f}")