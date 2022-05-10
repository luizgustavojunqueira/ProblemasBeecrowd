import re

n = int(input())

regExPlaca = re.compile('[A-Z]{3}-[0-9]{4}')

for i in range(n):

    placa = input()

    if regExPlaca.match(placa):
        digitoFinal = int(placa[7])

        if digitoFinal == 1 or digitoFinal == 2:
            print("MONDAY")
        elif digitoFinal == 3 or digitoFinal == 4:
            print("TUESDAY")
        elif digitoFinal == 5 or digitoFinal == 6:
            print("WEDNESDAY")
        elif digitoFinal == 7 or digitoFinal == 8:
            print("THURSDAY")
        elif digitoFinal == 9 or digitoFinal == 0:
            print("FRIDAY")
        
    else:
        print("FAILURE")