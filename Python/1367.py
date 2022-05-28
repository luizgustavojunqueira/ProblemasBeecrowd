n = int(input())

while n != 0:

    exCorretos = []
    exErrados = []
    tempoTotal = 0

    for i in range(n):
        ex, tempo, julg = input().split()
        tempo = int(tempo)

        if julg == "correct":
            tempoTotal += tempo
            if ex in exErrados:
                tempoTotal += 20 * exErrados.count(ex)
            if ex not in exCorretos:
                exCorretos.append(ex)
        else:
            exErrados.append(ex)

    print(len(exCorretos), tempoTotal)

    n = int(input())