while True:
    try:

        n = int(input())

        votos = list(map(int, input().split()))

        votosAFavor = 0

        for v in votos:
            if v:
                votosAFavor += 1

        if votosAFavor >= (2/3) * n:
            print("impeachment")
        else:
            print("acusacao arquivada")        

    except EOFError:
        break