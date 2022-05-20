while True:
    try:

        frase = input()

        res = ""

        aux = 1

        for i in range(len(frase)):
            if frase[i] != " ":
                
                if aux == 1:
                    aux = 0
                    res += frase[i].upper()
                else:
                    res += frase[i].lower()
                    aux = 1
            else:
                res += " "

        print(res)

    except EOFError:
        break