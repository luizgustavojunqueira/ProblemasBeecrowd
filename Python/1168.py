n = int(input())

qntLedNumero = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(n):
    num = input()

    qntLeds = 0

    for j in range(len(num)):
        qntLeds += qntLedNumero[int(num[j])]

    print(f"{qntLeds} leds")