while True:
    try:

        n = int(input())

        sec = 0

        if n % 100 == 0:
            sec = n // 100
        else:
            sec = (n + (100 - n % 100)) // 100

        print(sec)

    except EOFError:
        break