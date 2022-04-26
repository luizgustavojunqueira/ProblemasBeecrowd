caso = 1

while True:
    try:
        n1 = input()
        n2 = input()

        numSubsequencias = 0
        posUltima = 0

        for i in range(len(n2)):
            x = 0
            for j in range(i, i + len(n1)):
                if j < len(n2):
                    x = x * 10 + int(n2[j])
            if x == int(n1):
                numSubsequencias += 1
                posUltima = i + 1

        print(f"Caso #{caso}:")

        if numSubsequencias > 0:
            print(f"Qtd.Subsequencias: {numSubsequencias}")
            print(f"Pos: {posUltima}")
        else:
            print("Nao existe subsequencia")

        caso += 1

        print()

    except EOFError:
        break