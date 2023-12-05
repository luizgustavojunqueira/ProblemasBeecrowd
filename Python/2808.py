posi, posf = input().split()

posiLetra, posiNum = ord(posi[0]), int(posi[1])
posfLetra, posfNum = ord(posf[0]), int(posf[1])

if (abs(posfLetra - posiLetra) == 1 and abs(posfNum - posiNum) == 2) or (abs(posfLetra - posiLetra) == 2 and abs(posfNum - posiNum) == 1):
    print("VALIDO")
else:
    print("INVALIDO")