while True:
    try:
        n, m = map(int,input().split())
        numeros = list(map(int, input().split()))
        numeros.sort()

        soma=0

        for i in range(n-1, n-m-1, -1):
            soma+=int(numeros[i])

        print(soma)

    except EOFError: 
        break