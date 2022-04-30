while True:

    try:

        c, n = map(int, input().split())

        cifra1 = list(input())
        cifra2 = list(input())

        for i in range(n):
            textoCripto = input()
            
            textoDescripto = ""

            for j in range(len(textoCripto)):

                if textoCripto[j].upper() in cifra1:

                    if textoCripto[j].isupper():
                        textoDescripto += cifra2[cifra1.index(textoCripto[j].upper())]
                    else:
                        textoDescripto += cifra2[cifra1.index(textoCripto[j].upper())].lower()

                elif textoCripto[j].upper() in cifra2:

                    if textoCripto[j].isupper():
                        textoDescripto += cifra1[cifra2.index(textoCripto[j].upper())]
                    else:
                        textoDescripto += cifra1[cifra2.index(textoCripto[j].upper())].lower()

                else:
                    textoDescripto += textoCripto[j]

            print(textoDescripto)  

        print()      

    except EOFError:
        break