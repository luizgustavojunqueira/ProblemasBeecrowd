while True:
    try:

        m = int(input())

        if  m < 90 or m == 360:
            print('Bom Dia!!')
        elif m < 180:
            print('Boa Tarde!!')
        elif m < 270:
            print('Boa Noite!!')
        elif m < 360:
            print('De Madrugada!!')

    except EOFError:
        break