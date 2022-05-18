def rotate(a, n):
    return a[n:] + a[:n]

pChave = input()

n = int(input())

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
relacoesLetras = []
vogais = ["a", "e", "i", "o", "u"]

for i in range(26):
    relacoesLetras.append(letras)
    letras = rotate(letras, 1)

for i in range(n):

    msg = input()
    palavras = msg.split()
    palavrasCripto = []

    j = 0

    for k in range(len(palavras)):
        if palavras[k][0] in vogais:
            palavrasCripto.append(palavras[k])
        else:
            palavraCripto = ""
            for l in range(len(palavras[k])):
                posLetraVertical = (ord(pChave[j]) % 97)
                posLetraHorizontal = (ord(palavras[k][l]) % 97)
                letra = relacoesLetras[posLetraVertical][posLetraHorizontal]
                palavraCripto += letra
                if j == len(pChave) - 1:
                    j = 0
                else:
                    j += 1
            
            palavrasCripto.append(palavraCripto)

    print(" ".join(palavrasCripto))