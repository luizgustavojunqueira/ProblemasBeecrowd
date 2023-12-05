import math

while True:
    try:

        n, l, c = [int(i) for i in input().split()]
        poema = input().split()

        paginas = []
        pag = poema[0] + " "

        i = 1

        while i < n:
            if len(pag) + len(poema[i]) <= c:
                pag += f"{poema[i]} "
                i += 1
            else:
                paginas.append(pag)
                pag = ""

        paginas.append(pag)
        
        print(math.ceil(len(paginas) / l))

    except EOFError:
        break