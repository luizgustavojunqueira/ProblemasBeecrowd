n = int(input())

while n != 0:

    comandos = input()

    direcao = 1 # 1 = N, 2 = L , 3 = S, 4 = O

    for i in range(n):
        if comandos[i] == "D":
            direcao += 1
        else:
            direcao -= 1

    direcao = (direcao) % 4

    if direcao == 1:
        print("N")
    elif direcao == 2:
        print("L")
    elif direcao == 3:
        print("S")
    else:
        print("O")

    n = int(input())