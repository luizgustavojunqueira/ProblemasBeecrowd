while True:
    try:

        leg = input()

        if leg == "direita":
            print("frances")
        elif leg == "esquerda":
            print("ingles")
        elif leg == "nenhuma":
            print("portugues")
        else:
            print("caiu")

    except EOFError:
        break