while True:
    try:

        letras = list(input())

        n = int(input())

        lampadas = list(map(int, input().split()))

        msg = ""

        for i in range(n):
            msg += letras[lampadas[i] - 1]

        print(msg)

    except EOFError:
        break