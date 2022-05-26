printar = False

while True:
    try:

        linha = input()

        if "</body>" in linha:
            printar = False

        if printar:
            print(linha)

        if "<body>" in linha:
            printar = True       

    except EOFError:
        break