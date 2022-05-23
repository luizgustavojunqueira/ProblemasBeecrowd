while True:
    try:

        t = int(input())

        termos = input().split(" + ")
        novosTermos = []
        
        for i in range(t):
            c, e = map(int, termos[i].split("x"))

            if e == 2:
                nt = f"{c*e}x"
            else:
                nt = f"{c*e}x{e-1}"

            novosTermos.append(nt)

        print(" + ".join(novosTermos))

    except EOFError:
        break