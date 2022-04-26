while True:
    try:
        hr, min = input().split(":")   
        hr, min = int(hr), int(min)    

        diferencaHrs = 8 - (hr+1)

        if diferencaHrs == 0:
            print(f"Atraso maximo: {min}")
        elif diferencaHrs < 0:
            print(f"Atraso maximo: {min+60*(-diferencaHrs)}")
        else:
            print(f"Atraso maximo: 0")
        

    except EOFError:
        break