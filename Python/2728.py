while True:
    try:
    
        palavras = input().split("-")

        ehBug = True

        if palavras[0][0].lower() == "c" or palavras[0][-1].lower() == "c":
            if palavras[1][0].lower() == "o" or palavras[1][-1].lower() == "o":
                if palavras[2][0].lower() == "b" or palavras[2][-1].lower() == "b":
                    if palavras[3][0].lower() == "o" or palavras[3][-1].lower() == "o":
                        if palavras[4][0].lower() == "l" or palavras[4][-1].lower() == "l":
                            ehBug = False

        if ehBug:
            print("BUG")
        else:
            print("GRACE HOPPER")

    except EOFError:
        break