while True:
    try:
        datas = []
        presencas = []
        dataMaiorPresencas = 0
        maiorPresencas = 0

        n, d = map(int, input().split())

        for i in range(d):
            data, pessoas = input().split(" ", 1)
            presencas.append(list(map(int, pessoas.split())))
            datas.append(data)

        for i in range(d):
            soma = sum(presencas[i])
            if soma > maiorPresencas:
                dataMaiorPresencas = i
                maiorPresencas = soma

        if maiorPresencas == n:
            print(f"{datas[dataMaiorPresencas]}")
        else:
            print("Pizza antes de FdI")
    except EOFError:
        break