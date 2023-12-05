while True:
    try:

        frase = input()
        res = ""

        i = 0

        t = len(frase) - 1
        while i < t:
            if frase[i] == " " and (frase[i+1] == "," or frase[i+1] == "."):
                res += frase[i+1]
                i += 2
            else:
                res += frase[i]
                i += 1

        print(res)

    except EOFError:
        break