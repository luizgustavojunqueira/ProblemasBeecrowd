while True:
    try:
        h, m = map(int, input().split())

        numTestes = (h*60) // m

        valores = list(map(float , input().split()))
        media = sum(valores)

        media = media / numTestes

        precisao = 0

        for i in range(numTestes):
            precisao += (valores[i] - media) ** 2

        precisao /= numTestes - 1
        precisao = (precisao) ** (1/2)

        print(f"{precisao:.5f}")
    except EOFError:
        break