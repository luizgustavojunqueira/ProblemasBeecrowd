while True:
    try:

        n = int(input())

        numEPR, numEHD, numIntrusos = 0, 0, 0

        for i in range(n):
            mat, sigla = input().split()

            if sigla == "EPR":
                numEPR += 1
            elif sigla == "EHD":
                numEHD += 1
            else:
                numIntrusos += 1

        print(f"EPR: {numEPR}")
        print(f"EHD: {numEHD}")
        print(f"INTRUSOS: {numIntrusos}")

    except EOFError:
        break