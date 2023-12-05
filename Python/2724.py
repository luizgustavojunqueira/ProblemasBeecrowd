n = int(input())

for i in range(n):
    t = int(input())

    perigosos = []

    for j in range(t):
        perigosos.append(input())
    
    u = int(input())
    mistura = []

    for j in range(u):
        mistura.append(input())

    for y in range(u):
        ok = False

        for x in range(t):

            if perigosos[x] in mistura[y]:
                checarProximo = mistura[y].split(perigosos[x])

                if len(checarProximo) > 1:
                    checa = checarProximo[1]

                    
                    if checa[0].isupper() and checa[0].isnumeric():
                        ok += 1
                else:
                    ok += 1
        
        if ok != 0:
            print("Abortar")
        else:
            print("Prossiga")
        
    print()