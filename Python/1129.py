n = int(input())

letras = "ABCDE"

while n != 0:

    for j in range(n):
        valores = list(map(int, input().split()))

        posZero = -1
        erro = False

        for i in range(5):
            if valores[i] <= 127:
                if posZero == -1:
                    posZero = i
                else:
                    erro = True

        if erro or posZero == -1:
            print("*")
        else:
            print(f"{letras[posZero]}")

    n = int(input())