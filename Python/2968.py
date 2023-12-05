v, n = map(int, input().split())

totalSigns = v * n

for i in range(1, 10):
    signs = (totalSigns * i) / 10
    if signs % 1 != 0:
        signs += 1
    signs = int(signs)

    if i == 9:
        print(signs)
    else:
        print(signs, end = " ")
