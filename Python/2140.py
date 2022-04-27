n, m = map(int, input().split())

while not n == m == 0:

    troco = m-n

    notas = [2, 5, 10, 20, 50, 100]

    possivel = False

    for i in range(6):
        for j in range(6):
            if notas[i] != notas[j] and notas[i] + notas[j] == troco:
                possivel = True
                print("possible")
                break
        if possivel:
            break

    if not possivel:
        print("impossible")

    n, m = map(int, input().split())
