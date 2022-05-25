def verificarPedras(n, numPedras):
    for i in range(n):
        if numPedras[i] == i+1:
            return i

    return -1

def mudarPedras(n, numPedras):

    numPedras[n] -= n+1

    for i in range(n):
        numPedras[i] += 1

    return numPedras

n = int(input())

while n != -1:

    numPedras = [int(i) for i in input().split()]

    v = verificarPedras(n, numPedras)

    while v != -1:
        numPedras = mudarPedras(v, numPedras)
        v = verificarPedras(n, numPedras)

    if sum(numPedras) == 0:
        print("S")
    else:
        print("N")

    n = int(input())
