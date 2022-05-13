b = int(input())
g = int(input())

if g % 2 == 1:
    g -= 1

falta = int((g/2) - b)

if falta > 0:
    print(f"Faltam {falta} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")
