n = int(input())

for i in range(n):
    listaCompras = []

    entrada = input().split()

    for e in entrada:
        if e not in listaCompras:
            listaCompras.append(e)

    listaCompras.sort()

    for j in range(len(listaCompras)):
        if j < len(listaCompras) - 1:
            print(listaCompras[j], end = " ")
        else:
            print(listaCompras[j])