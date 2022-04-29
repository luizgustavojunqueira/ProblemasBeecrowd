while True:
    try:
        t = int(input())

        expressoes = []
        nomesErro = []

        for i in range(t):
            expressoes.append(input())

        for i in range(t):
            nome, exp, op = input().split()
            exp = int(exp)

            x, resto = expressoes[exp-1].split()
            y, z = resto.split("=")

            x, y, z = int(x), int(y), int(z)

            if op == "+":
                if x + y != z:
                    nomesErro.append(nome)
            elif op == "-":
                if x - y != z:
                    nomesErro.append(nome)
            elif op == "*":
                if x * y != z:
                    nomesErro.append(nome)
            elif op == "I":
                if x * y == z or x + y == z or x - y == z:
                    nomesErro.append(nome)

        if t == len(nomesErro):

            print("None Shall Pass!")

        elif len(nomesErro) == 0:

            print("You Shall All Pass!")

        else:

            nomesErro.sort()
            saida = ""

            for i in nomesErro:

                if i != nomesErro[-1]:

                    saida += i + " "

                else:

                    saida += i

            print(saida)

    
    except EOFError:
        break

