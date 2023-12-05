while True:
    try:

        f = input()
        f = f.replace("@", "a").replace("&", "e").replace("!", "i").replace("*", "o").replace("#", "u")
        print(f)

    except EOFError:
        break