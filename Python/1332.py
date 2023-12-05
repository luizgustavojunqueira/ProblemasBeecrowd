n = int(input())

for i in range(n):
    p = input()

    t = len(p)

    if t == 5:
        print(3)
    else:
        c = 0

        if p[0] == "o":
            c += 1
        if p[1] == "n":
            c += 1
        if p[2] == "e":
            c += 1

        if c >= 2:
            print(1)
        else:
            print(2)