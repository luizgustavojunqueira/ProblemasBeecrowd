n, x = map(int, input().split())
tamanhos = list(input())
p, m, g = map(int, input().split())

qntMulharas = 1
tamanhoUltimaMulhara = x

i = 0

while i < len(tamanhos):

    if tamanhos[i] == "P":
        if p > tamanhoUltimaMulhara:
            tamanhos.insert(0, "P")
            i -= 1
        else:
            tamanhoUltimaMulhara -= p

    elif tamanhos[i] == "M":
        if m > tamanhoUltimaMulhara:
            tamanhos.insert(0, "M")
            i -= 1
        else:
            tamanhoUltimaMulhara -= m

    elif tamanhos[i] == "G":
        if g > tamanhoUltimaMulhara:
            tamanhos.insert(0, "G")
            i -= 1
        else:
            tamanhoUltimaMulhara -= g

    if tamanhoUltimaMulhara <= 0:
        qntMulharas += 1
        tamanhoUltimaMulhara = x

    i += 1

print(qntMulharas)