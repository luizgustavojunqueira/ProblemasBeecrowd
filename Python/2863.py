while True:
    try:

        t = int(input())

        fastest = 11

        for i in range(t):
            x = float(input())
            if x < fastest:
                fastest = x

        print(f"{fastest:.2f}")

    except EOFError:
        break