while True:
    try:

        palavras = input().split()
        total = 0
        iniciais = []

        ultimaInicial = palavras[0][0].lower()
        letras = ultimaInicial

        for i in range(1, len(palavras)):

            p = palavras[i][0].lower()
        
            if p != ultimaInicial:
                iniciais.append(letras)
                ultimaInicial = p
                letras = ""
                
            letras += p
            
        iniciais.append(letras)

        for l in iniciais:
            if len(l) >= 2:
                total += 1

        print(total)

    except EOFError:
        break