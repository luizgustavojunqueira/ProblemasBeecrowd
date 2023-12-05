while True:
    try:

        h, m = map(int, input().split())

        print(f"{h//30:02d}:{m//6:02d}")

    except EOFError:
        break