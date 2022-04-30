while True:
    try:

        m = int(input())

        somaNotasXCH = 0
        chTotal = 0

        for i in range(m):
            nota, ch = map(int, input().split())

            somaNotasXCH += nota * ch
            chTotal += ch

        IndiceRA = somaNotasXCH / (chTotal * 100)

        print(f"{IndiceRA:.4f}")

    except EOFError:
        break