n = int(input())

for i in range(n):
    x = int(input())
    bulbs = list(bin(x)[2:])

    aux = 0
    tamanho = 0

    for bulb in bulbs:
        if bulb == "1":
            aux += 1
        else:
            aux = 0

        if aux > tamanho:
            tamanho = aux
    
    print(tamanho)