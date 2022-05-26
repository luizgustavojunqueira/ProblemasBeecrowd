d, n = input().split()

while d != '0' and n != '0':

    res = "0"

    for i in range(len(n)):
        if n[i] != d:
            res += n[i]

    print(int("".join(res)))

    d, n = input().split()