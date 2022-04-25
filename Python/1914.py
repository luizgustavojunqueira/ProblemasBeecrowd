qntCasos = int(input())

for i in range(qntCasos):

    j1, escolha1, j2, escolha2 = input().split()

    numJ1, numJ2 = map(int, input().split())

    if (numJ1 + numJ2) % 2 == 0:
        if escolha1 == "PAR":
            print(j1)
        else:
            print(j2)
    else:
        if escolha1 == "IMPAR":
            print(j1)
        else:
            print(j2)