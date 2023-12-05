def pegarPosMaior(l):
    posMaior = 0
    for i in range(len(l)):
        if l[i] > l[posMaior]:
            posMaior = i
    return posMaior

def pegarPosMenor(l):
    posMenor = len(l)-1
    for i in range(len(l)):
        if l[i] < l[posMenor]:
            posMenor = i
    return posMenor

while True:
    try:
        n = int(input())

        for i in range(n):
            m = int(input())
            lista = list(map(int, input().split()))

            impares = [i for i in lista if i % 2 == 1]

            res = []

            for i in range(len(impares)):
                if i % 2 == 0:
                    posMaior = pegarPosMaior(impares)
                    res.append(impares[posMaior])
                    impares.pop(posMaior)
                else:
                    posMenor = pegarPosMenor(impares)
                    res.append(impares[posMenor])
                    impares.pop(posMenor)

            for i in range(len(res)):
                if i == len(res) - 1:
                    print(res[i])
                else:
                    print(res[i], end = " ")
            
            if len(res) == 0:
                print()

    except EOFError:
        break