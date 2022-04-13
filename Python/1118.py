continuar = 1

while continuar != 2:
    n1 = 0
    n2 = 0

    if continuar == 1:
        while True:
            n1 = float(input())
            if 0 <= n1 <= 10:
                break
            else:
                print("nota invalida")

        while True:
            n2 = float(input())
            if 0 <= n2 <= 10:
                break
            else:
                print("nota invalida")

        media = (n1 + n2) / 2
        print(f"media = {media:.2f}")

    continuar = int(input("novo calculo (1-sim 2-nao)\n"))