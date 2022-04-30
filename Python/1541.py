entrada = input()

while entrada != '0':
    
    a, b, percent = map(int, entrada.split())

    areaCasa = a*b

    ladoTerreno = int((areaCasa / (percent/100)) ** (1/2))

    print(ladoTerreno)

    entrada = input()