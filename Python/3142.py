import math

while True:
    try:

        s = input()

        n = 0
        j = 0
        for i in range(len(s)-1, -1, -1):
            n += (ord(s[i]) - 64) * math.pow(26, j)
            j += 1

        if n >= 16384:
            print("Essa coluna nao existe Tobias!")
        else:
            print(int(n))

    except EOFError:
        break