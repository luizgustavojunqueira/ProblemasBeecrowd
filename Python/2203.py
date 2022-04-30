from math import sqrt

while True:
    try:
        xf, yf, xi, yi, vi, rAtaque, rCorvos = map(int, input().split())

        dist = sqrt((xi - xf) ** 2 + (yi - yf) ** 2) + vi* 1.5

        if dist <= rAtaque + rCorvos:
            print("Y")
        else:
            print("N")

    except EOFError:
        break