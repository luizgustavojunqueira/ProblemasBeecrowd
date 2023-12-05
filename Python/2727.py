alfabeto = "abcdefghijklmnopqrstuvwxyz"

while True:
    try:

        n = int(input())

        for i in range(n):
            cod = input().split()
            pos = len(cod[0]) + 3*(len(cod) - 1) - 1

            print(alfabeto[pos])

    except EOFError:
        break