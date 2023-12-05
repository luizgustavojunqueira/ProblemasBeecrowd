while True:
    try:
        n = int(input())

        i = 0
        while n>1:
            i += 1
            n /= 2

        print(i)

    except EOFError:
        break