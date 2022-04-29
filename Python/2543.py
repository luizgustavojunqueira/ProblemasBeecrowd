while True:
    try:

        n, i = map(int, input().split())

        numCS = 0

        for j in range(n):
            id, jogo = map(int, input().split())

            if id == i and jogo == 0:
                numCS += 1
            
        print(numCS)

    except EOFError:
        break