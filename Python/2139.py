mesesEDias = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    try:
    
        mes, dia = map(int, input().split())

        if mes == 12:
            if dia == 24:
                print("E vespera de natal!")
            elif dia == 25:
                print("E natal!")
            elif dia > 25:
                print("Ja passou!")
        else:        

            mes -= 1
            diasTotal = dia

            for i in range(mes):
                diasTotal += mesesEDias[i]
            
            print(f"Faltam {360 - diasTotal} dias para o natal!")

    except EOFError:
        break