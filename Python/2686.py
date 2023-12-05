while True:
    try:

        m = float(input())

        if m < 90 or m == 360:
            print("Bom Dia!!")
        elif m < 180:
            print("Boa Tarde!!")
        elif m < 270:
            print("Boa Noite!!")
        elif m < 360:
            print("De Madrugada!!")

        segundos = 21600 + (86400/360) * m

        h = segundos // 3600
        segundos %= 3600
        m = segundos // 60
        segundos %= 60

        if h >= 24:
            h -= 24

        print(f"{int(h):02d}:{int(m):02d}:{int(segundos):02d}")

    except EOFError:
        break
