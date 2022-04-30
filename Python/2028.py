caso = 1

while True:
    
    try:
        n = int(input())

        qntNumeros = 1

        for i in range(1, n+1):
            qntNumeros += i

        if qntNumeros == 1:
            print(f"Caso {caso}: {qntNumeros} numero")
        else:
            print(f"Caso {caso}: {qntNumeros} numeros")

        if qntNumeros == 1:
            print(0)
        else:
            print("0 ", end = "")

        for i in range(n+1):
            for j in range(i):
                if i == n and j == n-1:
                    print(i)
                else:
                    print(i, end = " ")

        print()

        caso += 1

    except EOFError:
        break